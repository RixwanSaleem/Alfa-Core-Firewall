import os
import shlex
import shutil
import subprocess
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
# Set max_age to 600 seconds (10 minutes) for auto-logout
app.add_middleware(SessionMiddleware, secret_key="ALFA_PRO_KEY_99", max_age=600)
templates = Jinja2Templates(directory="templates")

ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "password")
PASSWD_FILE = "/etc/squid/passwd"
OCSERV_PASSWD_FILE = "/var/lib/ocserv/ocpasswd"

SERVICE_MAP = {
    "dhcp-server": {
        "label": "DHCP Server",
        "package": "dhcp-server",
        "service": "dhcpd",
        "description": "Manage the DHCP allocation service for local network clients."
    },
    "ethernet": {
        "label": "Ethernet",
        "package": "NetworkManager",
        "service": "NetworkManager",
        "description": "Manage wired Ethernet and network adapter services."
    },
    "ipsec": {
        "label": "IPSec",
        "package": "strongswan",
        "service": "strongswan",
        "description": "Manage IPsec VPN tunnels and encrypted site-to-site connections."
    },
    "ssl": {
        "label": "SSL VPN",
        "package": "stunnel",
        "service": "stunnel",
        "description": "Manage SSL-based VPN tunnels and secure transport channels."
    },
    "ssh": {
        "label": "SSH",
        "package": "openssh-server",
        "service": "sshd",
        "description": "Manage SSH remote access, secure shell connections and tunnels."
    },
    "vpn": {
        "label": "VPN",
        "package": "openvpn",
        "service": "openvpn",
        "description": "Manage generic VPN client/server tunnels for remote access."
    },
    "ocserv": {
        "label": "OCSERV",
        "package": "ocserv",
        "service": "ocserv",
        "description": "Manage OpenConnect VPN server for secure client access."
    }
}

def run_cmd(cmd):
    clean_env = os.environ.copy()
    clean_env.pop("PYTHONPATH", None)
    clean_env.pop("VIRTUAL_ENV", None)
    clean_env["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, env=clean_env)


def run_cmd_input(cmd, input_text: str):
    clean_env = os.environ.copy()
    clean_env.pop("PYTHONPATH", None)
    clean_env.pop("VIRTUAL_ENV", None)
    clean_env["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    if isinstance(cmd, list):
        return subprocess.run(cmd, capture_output=True, text=True, env=clean_env, input=input_text)
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, env=clean_env, input=input_text)


def safe_shell_arg(value: str) -> str:
    return shlex.quote(value or "")


def get_stats():
    is_installed = run_cmd("rpm -q squid").returncode == 0
    return {
        "installed": is_installed,
        "squid_active": run_cmd("systemctl is-active squid").stdout.strip() == "active",
        "fw_active": run_cmd("systemctl is-active firewalld").stdout.strip() == "active",
        "uptime": run_cmd("uptime -p").stdout.strip(),
        "load": run_cmd("uptime | awk -F'load average:' '{ print $2 }'").stdout.strip()
    }

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USER and password == ADMIN_PASS:
        request.session["logged_in"] = True
        return RedirectResponse(url="/", status_code=303)
    return RedirectResponse(url="/login?error=1", status_code=303)

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login")

@app.get("/")
async def dashboard(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    conns = run_cmd("netstat -an | grep :3128 | wc -l").stdout.strip()
    installed_services = []
    for key, service in SERVICE_MAP.items():
        if is_package_installed(service["package"]):
            installed_services.append({
                "key": key,
                "label": service["label"],
                "active": is_service_active(service["service"])
            })
    return templates.TemplateResponse(request=request, name="dashboard.html", context={"request": request, **get_stats(), "connections": conns, "installed_services": installed_services})

@app.get("/proxy")
async def proxy_page(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    stats = get_stats()
    users = []
    if stats["installed"] and os.path.exists(PASSWD_FILE):
        with open(PASSWD_FILE, "r") as f:
            users = [line.split(":")[0] for line in f if ":" in line]
    config = Path("/etc/squid/squid.conf").read_text() if os.path.exists("/etc/squid/squid.conf") else ""
    return templates.TemplateResponse(request=request, name="proxy.html", context={"request": request, **stats, "proxy_users": users, "config": config})

@app.get("/firewall")
async def firewall_page(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    ports = run_cmd("firewall-cmd --list-ports").stdout.strip()
    return templates.TemplateResponse(request=request, name="firewall.html", context={"request": request, **get_stats(), "open_ports": ports.split()})

@app.get("/logs")
async def logs_page(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    logs = run_cmd("tail -n 100 /var/log/squid/access.log").stdout
    return templates.TemplateResponse(request=request, name="logs.html", context={"request": request, **get_stats(), "logs": logs})

@app.get("/network")
@app.get("/networks")
async def networks_page(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    service_keys = ["dhcp-server", "ethernet"]
    services = []
    for key in service_keys:
        service = lookup_service(key)
        if not service:
            continue
        installed = is_package_installed(service["package"])
        active = is_service_active(service["service"]) if installed else False
        services.append({
            "key": key,
            "label": service["label"],
            "description": service["description"],
            "installed": installed,
            "active": active,
        })
    return templates.TemplateResponse(request=request, name="networks.html", context={"request": request, **get_stats(), "services": services})

@app.get("/vpns")
@app.get("/vpn")
async def vpns_page(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    service_keys = ["ipsec", "ssl", "ssh", "vpn", "ocserv"]
    services = []
    for key in service_keys:
        service = lookup_service(key)
        if not service:
            continue
        installed = is_package_installed(service["package"])
        active = is_service_active(service["service"]) if installed else False
        services.append({
            "key": key,
            "label": service["label"],
            "description": service["description"],
            "installed": installed,
            "active": active,
        })
    return templates.TemplateResponse(request=request, name="vpns.html", context={"request": request, **get_stats(), "services": services})


def lookup_service(service_key: str):
    return SERVICE_MAP.get(service_key)


def is_package_installed(package_name: str) -> bool:
    return run_cmd(f"rpm -q {safe_shell_arg(package_name)}").returncode == 0


def is_service_active(service_name: str) -> bool:
    return run_cmd(f"systemctl is-active {safe_shell_arg(service_name)}").stdout.strip() == "active"


def get_ocserv_users() -> list:
    """Get list of OCSERV users from ocpasswd file"""
    users = []
    if os.path.exists(OCSERV_PASSWD_FILE):
        with open(OCSERV_PASSWD_FILE, 'r') as f:
            for line in f:
                if line.strip() and ':' in line:
                    username = line.strip().split(':')[0]
                    users.append(username)
    return users


def get_ocserv_connected_users() -> list:
    """Get connected OCSERV users using occtl"""
    connected = []
    result = run_cmd(f"occtl -s /var/run/occtl.socket show-users")
    if result.returncode != 0:
        return connected
    for line in result.stdout.strip().split('\n'):
        text = line.strip()
        if not text or text.lower().startswith("no active"):
            continue
        connected.append(text)
    return connected


def create_ocserv_user(username: str, password: str) -> bool:
    """Create or update OCSERV user with password"""
    try:
        os.makedirs(os.path.dirname(OCSERV_PASSWD_FILE), exist_ok=True)
        ocpasswd_bin = shutil.which("ocpasswd")
        input_text = f"{password}\n{password}\n"

        if ocpasswd_bin:
            # Always use -c flag with database path
            cmd = [ocpasswd_bin, "-c", OCSERV_PASSWD_FILE, username]
            result = run_cmd_input(cmd, input_text)
            if result.returncode == 0:
                os.chmod(OCSERV_PASSWD_FILE, 0o600)
                return True
            print(f"ocpasswd failed: {result.stderr.strip()}")
            return False

        # Fallback only if ocpasswd is unavailable
        existing_users = {}
        if os.path.exists(OCSERV_PASSWD_FILE):
            with open(OCSERV_PASSWD_FILE, 'r') as f:
                for line in f:
                    if ':' in line:
                        parts = line.strip().split(':', 1)
                        if len(parts) == 2:
                            user, pass_val = parts
                            existing_users[user] = pass_val

        existing_users[username] = password
        with open(OCSERV_PASSWD_FILE, 'w') as f:
            for user, pass_val in existing_users.items():
                f.write(f"{user}:{pass_val}\n")
        os.chmod(OCSERV_PASSWD_FILE, 0o600)
        return True
    except Exception as e:
        print(f"Error creating OCSERV user: {e}")
        return False


def delete_ocserv_user(username: str) -> bool:
    """Delete OCSERV user"""
    try:
        if not os.path.exists(OCSERV_PASSWD_FILE):
            return True
        ocpasswd_bin = shutil.which("ocpasswd")
        if ocpasswd_bin:
            # Correct syntax: ocpasswd -c <db_path> -d <username>
            result = run_cmd(f"{safe_shell_arg(ocpasswd_bin)} -c {safe_shell_arg(OCSERV_PASSWD_FILE)} -d {safe_shell_arg(username)}")
            if result.returncode == 0:
                return True
            print(f"ocpasswd delete failed: {result.stderr.strip()}")
            return False

        existing_users = {}
        with open(OCSERV_PASSWD_FILE, 'r') as f:
            for line in f:
                if ':' in line:
                    user, pass_val = line.strip().split(':', 1)
                    existing_users[user] = pass_val
        if username in existing_users:
            del existing_users[username]
        with open(OCSERV_PASSWD_FILE, 'w') as f:
            for user, pass_val in existing_users.items():
                f.write(f"{user}:{pass_val}\n")
        return True
    except Exception as e:
        print(f"Error deleting OCSERV user: {e}")
        return False


@app.get("/service/{service_key}")
async def service_page(request: Request, service_key: str):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")
    service = lookup_service(service_key)
    if not service:
        return RedirectResponse(url="/", status_code=303)
    installed = is_package_installed(service["package"])
    active = is_service_active(service["service"]) if installed else False
    category = "network" if service_key in {"dhcp-server", "ethernet"} else "vpn"
    context = {
        "request": request,
        **get_stats(),
        "service_key": service_key,
        "service_label": service["label"],
        "description": service["description"],
        "package_name": service["package"],
        "service_name": service["service"],
        "installed": installed,
        "active": active,
        "nav_section": category,
        "ocserv_users": get_ocserv_users() if service_key == "ocserv" else [],
        "ocserv_connections": get_ocserv_connected_users() if service_key == "ocserv" else []
    }
    return templates.TemplateResponse(request=request, name="service.html", context=context)

@app.post("/service/{service_key}/manage")
async def manage_service(service_key: str, action: str = Form(...)):
    service = lookup_service(service_key)
    if not service:
        return RedirectResponse(url="/", status_code=303)
    pkg = safe_shell_arg(service["package"])
    svc = safe_shell_arg(service["service"])
    if action == "install":
        run_cmd(f"dnf install {pkg} -y")
    elif action == "uninstall":
        run_cmd(f"systemctl stop {svc} && dnf remove {pkg} -y")
    elif action == "enable":
        run_cmd(f"systemctl enable --now {svc}")
    elif action == "disable":
        run_cmd(f"systemctl disable --now {svc}")
    elif action == "restart":
        run_cmd(f"systemctl restart {svc}")
    elif action == "start":
        run_cmd(f"systemctl start {svc}")
    return RedirectResponse(url=f"/service/{service_key}", status_code=303)

@app.post("/manage")
async def manage_squid(action: str = Form(...)):
    if action == "install":
        run_cmd("dnf install squid httpd-tools -y && mkdir -p /etc/squid && touch /etc/squid/passwd && systemctl enable --now squid")
    elif action == "uninstall":
        run_cmd("systemctl stop squid && dnf remove squid -y")
    elif action in {"start", "stop", "restart"}:
        run_cmd(f"systemctl {action} squid")
    return RedirectResponse(url="/proxy", status_code=303)

@app.post("/proxy-user")
async def manage_user(action: str = Form(...), username: str = Form(...), password: str = Form(None)):
    safe_file = safe_shell_arg(PASSWD_FILE)
    safe_user = safe_shell_arg(username)
    if action == "add":
        safe_pass = safe_shell_arg(password or "")
        run_cmd(f"htpasswd -b {safe_file} {safe_user} {safe_pass}")
    else:
        run_cmd(f"htpasswd -D {safe_file} {safe_user}")
    run_cmd("systemctl restart squid")
    return RedirectResponse(url="/proxy", status_code=303)

@app.post("/ocserv-user")
async def manage_ocserv_user(action: str = Form(...), username: str = Form(...), password: str = Form(None)):
    if action == "add" or action == "reset":
        if not password:
            return RedirectResponse(url="/service/ocserv", status_code=303)
        success = create_ocserv_user(username, password)
        if success:
            run_cmd("systemctl restart ocserv")  # Restart service to pick up changes
    elif action == "delete":
        success = delete_ocserv_user(username)
        if success:
            run_cmd("systemctl restart ocserv")
    return RedirectResponse(url="/service/ocserv", status_code=303)

@app.get("/service/{service_key}/config")
async def service_config(request: Request, service_key: str):
    if not request.session.get("logged_in"):
        return RedirectResponse("/login")

    service = lookup_service(service_key)
    if not service:
        return RedirectResponse(url="/", status_code=303)

    # Define config file paths for each service
    config_files = {
        "ocserv": "/etc/ocserv/ocserv.conf",
        "ipsec": "/etc/strongswan/strongswan.conf",
        "ssl": "/etc/stunnel/stunnel.conf",
        "ssh": "/etc/ssh/sshd_config",
        "vpn": "/etc/openvpn/server.conf",
        "dhcp-server": "/etc/dhcp/dhcpd.conf",
        "ethernet": "/etc/sysconfig/network-scripts/ifcfg-eth0"
    }

    config_path = config_files.get(service_key)
    if not config_path:
        return RedirectResponse(url=f"/service/{service_key}", status_code=303)

    config_content = ""
    if os.path.exists(config_path):
        try:
            config_content = Path(config_path).read_text()
        except:
            config_content = "# Unable to read configuration file"

    return templates.TemplateResponse(request=request, name="config.html", context={
        "request": request,
        **get_stats(),
        "service_key": service_key,
        "service_label": service["label"],
        "config_path": config_path,
        "config_content": config_content
    })

@app.post("/service/{service_key}/config")
async def save_service_config(service_key: str, config_content: str = Form(...)):
    config_files = {
        "ocserv": "/etc/ocserv/ocserv.conf",
        "ipsec": "/etc/strongswan/strongswan.conf",
        "ssl": "/etc/stunnel/stunnel.conf",
        "ssh": "/etc/ssh/sshd_config",
        "vpn": "/etc/openvpn/server.conf",
        "dhcp-server": "/etc/dhcp/dhcpd.conf",
        "ethernet": "/etc/sysconfig/network-scripts/ifcfg-eth0"
    }

    config_path = config_files.get(service_key)
    if config_path and os.path.exists(config_path):
        try:
            Path(config_path).write_text(config_content)
            # Restart service after config change
            service = lookup_service(service_key)
            if service:
                run_cmd(f"systemctl restart {safe_shell_arg(service['service'])}")
        except:
            pass

    return RedirectResponse(url=f"/service/{service_key}/config", status_code=303)

@app.post("/manage-firewall")
async def manage_fw(action: str = Form(...)):
    if action in {"start", "stop", "restart", "status"}:
        run_cmd(f"systemctl {action} firewalld")
    return RedirectResponse(url="/firewall", status_code=303)

@app.post("/firewall-port")
async def manage_port(action: str = Form(...), port: str = Form(None)):
    if port:
        p = port.strip()
        if p:
            p = p if "/" in p else f"{p}/tcp"
            safe_port = safe_shell_arg(p)
            run_cmd(f"firewall-cmd --{action}-port={safe_port} && firewall-cmd --permanent --{action}-port={safe_port} && firewall-cmd --reload")
    return RedirectResponse(url="/firewall", status_code=303)

@app.post("/save-config")
async def save_config(config_text: str = Form(...)):
    if os.path.exists("/etc/squid/squid.conf"):
        Path("/etc/squid/squid.conf").write_text(config_text); run_cmd("systemctl restart squid")
    return RedirectResponse(url="/proxy", status_code=303)
