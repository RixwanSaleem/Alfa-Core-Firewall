# AlfaCore - Firewall Panel Administration UI

A comprehensive FastAPI-based web administration interface for managing network services including Squid proxy, firewall rules, VPN services, and system settings on a Linux host.

## Project Overview

AlfaCore Panel provides a modern, user-friendly dashboard for managing:

## Example Pictures
<img src="assets/Dashboard.png" width="500"/>



### Core Services
- **Proxy Server** - Squid proxy configuration, user management, and traffic control
- **Firewall** - Port management and firewall rule configuration using `firewall-cmd`
- **Networks** - Ethernet and DHCP server management
- **VPNs** - Multiple VPN protocol support (OpenConnect, IPSec, SSL/TLS, SSH, OpenVPN)
- **Access Logs** - Real-time proxy access log monitoring
- **System Settings** - Package management, system updates, and package search
- **Administration** - User management, password changes, configuration backups

### Key Features
- 🔐 Secure session-based authentication with auto-logout (10 minutes)
- 📊 Real-time system status and service monitoring
- 🔧 Service installation, configuration, and lifecycle management
- 📦 DNF package management with search and install capabilities
- 💾 Automatic backup and restore of critical configurations
- 📝 Configuration file editing with live previews
- 🎨 Modern dark-themed responsive UI
- 👥 User management for OCSERV VPN and proxy services
- 🗣️ Multi languages

## Languages

English
Español
Français
Deutsch
Arabic
中文
 
## Project Structure

```
squid-panel/
├── python_squid_admin/
│   ├── main.py                 # FastAPI application with all endpoints
│   ├── requirements.txt         # Python package dependencies
│   ├── README.md                # This file
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── login.html           # Login page
│   │   ├── dashboard.html       # Main dashboard
│   │   ├── proxy.html           # Squid proxy management
│   │   ├── firewall.html        # Firewall configuration
│   │   ├── networks.html        # Network services
│   │   ├── vpns.html            # VPN services
│   │   ├── logs.html            # Access logs viewer
│   │   ├── service.html         # Individual service management
│   │   ├── config.html          # Configuration editor
│   │   ├── system.html          # System settings & package management
│   │   └── admin.html           # Administration panel
│   └── var/                     # Reserved for future use
└── systemd/
    └── squid-panel.service      # Systemd service configuration
```

## System Requirements

- **OS**: Fedora/RHEL/CentOS with systemd
- **Python**: 3.9 or higher
- **Root Access**: Required for service and firewall management
- **System Packages**:
  - `python3` and `python3-pip`
  - `firewalld` (for firewall management)
  - `squid` (optional, can be installed via UI)
  - `ocserv` (optional, for OpenConnect VPN)
  - `openssl` (for certificate generation)

## Prerequisites Installation

Install required system packages:

```bash
sudo dnf install epel-release -y
sudo dnf install python3 python3-pip python3-devel gcc httpd-tools certbot firewalld openssl -y
sudo systemctl enable --now firewalld
```

## Installation

### 1. Create Project Directory

```bash
sudo mkdir -p /opt/squid-panel/python_squid_admin
sudo cd /opt/squid-panel/python_squid_admin
```

### 2. Set Up Python Virtual Environment

```bash
sudo python3 -m venv venv
sudo source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
sudo pip install -r requirements.txt
```

## Configuration

### 1. Create Environment Configuration File

Create `/etc/squid-panel.env`:

```bash
sudo nano /etc/squid-panel.env
```

Add the following configuration:

```env
# Session and Authentication
SESSION_SECRET=ALFA_PRO_KEY_99
ADMIN_USER=admin
ADMIN_PASS=YourSecureAdminPassword

# Squid Configuration
SQUID_CONF=/etc/squid/squid.conf
SQUID_SERVICE=squid
SQUID_PORT=3128

# Backup Configuration
BACKUP_DIR=/var/backups/squid-panel
OCSERV_PASSWD_FILE=/var/lib/ocserv/ocpasswd
PASSWD_FILE=/etc/squid/passwd
```

Set proper permissions:

```bash
sudo chmod 600 /etc/squid-panel.env
```

### 2. Configure Firewall

Allow the web UI port:

```bash
sudo firewall-cmd --permanent --add-port=8444/tcp
sudo firewall-cmd --reload
```

### 3. Create Systemd Service

Create `/etc/systemd/system/squid-panel.service`:

```ini
[Unit]
Description=AlfaCore Squid Panel Administration UI
After=network.target firewalld.service
Wants=firewalld.service

[Service]
Type=simple
WorkingDirectory=/opt/squid-panel/python_squid_admin
EnvironmentFile=/etc/squid-panel.env
ExecStart=/opt/squid-panel/python_squid_admin/venv/bin/uvicorn main:app \
    --host 0.0.0.0 \
    --port 8444 \
    --reload
Restart=on-failure
RestartSec=10
User=root
StandardOutput=journal
StandardError=journal
SyslogIdentifier=squid-panel

[Install]
WantedBy=multi-user.target
```

For production with SSL, replace `ExecStart` with:

```bash
ExecStart=/opt/squid-panel/python_squid_admin/venv/bin/uvicorn main:app \
    --host 0.0.0.0 \
    --port 8444 \
    --ssl-certfile /etc/letsencrypt/live/YOUR-DOMAIN.COM/fullchain.pem \
    --ssl-keyfile /etc/letsencrypt/live/YOUR-DOMAIN.COM/privkey.pem
```

### 4. Enable and Start the Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable squid-panel
sudo systemctl start squid-panel
```

Check status:

```bash
sudo systemctl status squid-panel
```

View logs:

```bash
sudo journalctl -u squid-panel -f
```

## Running Locally

For development and testing:

```bash
cd /opt/squid-panel/python_squid_admin
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8444
```

Then access the application at: `http://localhost:8444/login`

## Default Credentials

- **Username**: `admin` (or configured `ADMIN_USER`)
- **Password**: `password` (or configured `ADMIN_PASS`)

⚠️ **IMPORTANT**: Change these credentials immediately in `/etc/squid-panel.env` before production deployment.

## Usage Guide

### Dashboard
View overall system status, installed services, and quick access to management pages.

### Proxy Server
- View active connections
- Manage proxy users (add/remove)
- Edit Squid configuration
- Start/stop/restart Squid service

### Firewall
- View open ports
- Add/remove firewall rules
- Enable/disable firewall service
- Persist rules permanently

### Networks
- Configure Ethernet interfaces
- Manage DHCP server
- View and edit network configurations

### VPNs
Manage multiple VPN technologies:
- **OpenConnect Server (OCSERV)** - User and connection management
- **IPSec (strongSwan)** - Site-to-site VPN configuration
- **SSL/TLS Tunnels (stunnel)** - Encrypted tunnels
- **SSH** - Secure shell access
- **OpenVPN** - Generic VPN server/client

For each VPN service, you can:
- View installation steps and example configurations
- Install/uninstall services
- Start/stop services
- Edit configuration files
- Manage users (where applicable)

### System Settings
- Check available system updates
- Search and install packages
- Remove installed packages
- View installed package count
- Monitor system resources

### Administration
- Change admin password
- Create system configuration backups
- Download backups for offline storage
- Delete old backups
- View backup history

## Security Considerations

### Authentication & Sessions
- ✓ Session-based authentication with 10-minute auto-logout
- ✓ Credentials stored in environment variables
- ⚠️ Change default admin credentials before production use
- ⚠️ Use strong, unique SESSION_SECRET in production

### System Access
- ⚠️ Application runs as root (required for system management)
- ⚠️ Web UI executes system commands - only expose on trusted networks
- ✓ All shell arguments are properly escaped using `shlex.quote()`
- ✓ Configuration file paths validated against BACKUP_DIR

### Best Practices
1. Run behind a reverse proxy with HTTPS/TLS
2. Use Let's Encrypt certificates (included in prerequisites)
3. Restrict firewall access to administrative networks
4. Regularly backup configurations using the admin panel
5. Monitor system logs: `sudo journalctl -u squid-panel -f`
6. Keep Python packages updated: `pip install --upgrade -r requirements.txt`

## Troubleshooting

### Service Won't Start
```bash
sudo systemctl status squid-panel
sudo journalctl -u squid-panel -n 50
```

### Port Already in Use
Change port in systemd service or check what's using 8444:
```bash
sudo netstat -tlnp | grep 8444
```

### Permission Denied
Ensure the application runs as root (User=root in systemd service) or with proper capabilities for system commands.

### Package Search Not Working
Verify `dnf` is installed and accessible:
```bash
sudo dnf search vim
```

### Backup Issues
Check backup directory permissions:
```bash
sudo ls -la /var/backups/squid-panel
```

## Logs and Monitoring

View real-time application logs:
```bash
sudo journalctl -u squid-panel -f
```

View Squid access logs:
```bash
sudo tail -f /var/log/squid/access.log
```

View firewall logs:
```bash
sudo journalctl -u firewalld -f
```

## API Endpoints

All endpoints require authentication via session login.

### Authentication
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /logout` - Logout

### Dashboard & Main Pages
- `GET /` - Dashboard
- `GET /proxy` - Proxy management
- `GET /firewall` - Firewall management
- `GET /logs` - Access logs
- `GET /networks` - Network configuration
- `GET /vpns` - VPN services
- `GET /system` - System settings
- `GET /admin` - Administration panel

### Service Management
- `GET /service/{service_key}` - Service details
- `POST /service/{service_key}/manage` - Service actions (install/start/stop/etc)
- `GET /service/{service_key}/config` - Service configuration editor
- `POST /service/{service_key}/config` - Save service configuration

### User Management
- `POST /proxy-user` - Manage Squid users
- `POST /ocserv-user` - Manage OCSERV VPN users

### System Management
- `POST /system/search-packages` - Search for packages
- `POST /system/install-updates` - Install system updates
- `POST /system/install-package` - Install a package
- `POST /system/remove-package` - Remove a package

### Administration
- `POST /admin/change-password` - Change admin password
- `POST /admin/create-backup` - Create configuration backup
- `GET /admin/download-backup/{backup_name}` - Download backup
- `POST /admin/delete-backup` - Delete backup

## Dependencies

See `requirements.txt` for detailed versions. Main dependencies:

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Jinja2** - Template engine
- **Starlette** - ASGI toolkit (for session middleware)
- **python-multipart** - Form data handling
- **itsdangerous** - Session security

## Author

**Rizwan Saleem**

## License

This project is provided as-is for system administration purposes.

## Support & Contribution

For issues, feature requests, or contributions, please contact the development team.

---

**Last Updated**: May 2026
**Version**: 2.0 (AlfaCore)
