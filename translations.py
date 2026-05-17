"""
Multi-language translation system for AlfaCore Squid Panel
Supports: English, Spanish, French, German, Arabic, Chinese
"""

LANGUAGES = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ar": "العربية",
    "zh": "中文"
}

TRANSLATIONS = {
    "en": {
        # Navigation
        "sidebar_main": "Main Console",
        "sidebar_services": "Services",
        "sidebar_system": "System",
        "nav_dashboard": "Dashboard",
        "nav_proxy": "Proxy Server",
        "nav_firewall": "Firewall",
        "nav_logs": "Access Logs",
        "nav_networks": "Networks",
        "nav_vpns": "VPNs",
        "nav_docker": "Docker",
        "nav_system": "System Settings",
        "nav_admin": "Administration",
        "nav_logout": "Logout",
        
        # Login Page
        "login_title": "AlfaCore - Login",
        "login_username": "Username",
        "login_password": "Password",
        "login_signin": "Sign In",
        "login_error": "Invalid username or password",
        
        # Dashboard
        "dashboard_title": "Dashboard",
        "dashboard_status": "System Status",
        "dashboard_services": "Installed Services",
        "dashboard_uptime": "System Uptime",
        "dashboard_load": "Load Average",
        "dashboard_installed": "Installed",
        "dashboard_status_active": "Active",
        "dashboard_status_inactive": "Inactive",
        "dashboard_total_services": "Total Services",
        "dashboard_total_services_desc": "Total managed services on this host.",
        "dashboard_active_services": "Active Services",
        "dashboard_active_services_desc": "Services currently running.",
        "dashboard_proxy_connections": "Proxy Connections",
        "dashboard_proxy_connections_desc": "Live active proxy sessions.",
        "dashboard_firewall_status": "Firewall Status",
        "dashboard_health_overview": "System Health Overview",
        "dashboard_service_status": "Service Status",
        
        # Docker
        "docker_title": "Docker Management",
        "docker_status_help": "Manage the Docker daemon and container lifecycle.",
        "docker_containers": "Docker Containers",
        "docker_no_containers": "No Docker containers found.",
        "docker_not_installed": "Docker is not installed or not available.",
        "docker_container_actions": "Container Actions",
        
        # Proxy Server
        "proxy_title": "Proxy Server",
        "proxy_connections": "Active Connections",
        "proxy_users": "Proxy Users",
        "proxy_add_user": "Add New User",
        "proxy_username": "Username",
        "proxy_password": "Password",
        "proxy_add": "Add User",
        "proxy_delete": "Delete",
        "proxy_config": "Squid Configuration",
        "proxy_save_config": "Save Configuration",
        "proxy_status": "Proxy Status",
        "proxy_start": "Start",
        "proxy_stop": "Stop",
        "proxy_restart": "Restart",
        "proxy_install": "Install Squid",
        "proxy_uninstall": "Uninstall Squid",
        
        # Firewall
        "firewall_title": "Firewall Configuration",
        "firewall_status": "Firewall Status",
        "firewall_ports": "Open Ports",
        "firewall_add_port": "Add Port",
        "firewall_port": "Port Number",
        "firewall_enable": "Enable Firewall",
        "firewall_disable": "Disable Firewall",
        "firewall_restart": "Restart Firewall",
        "firewall_zones": "Firewall Zones",
        "firewall_zones_help": "Assign interfaces to firewall zones for zone-based segmentation.",
        "firewall_zone": "Zone",
        "firewall_interface": "Interface",
        "firewall_add_interface": "Add to Zone",
        "firewall_remove_interface": "Remove from Zone",
        "firewall_no_interfaces": "No interfaces assigned",
        
        # Networks
        "networks_title": "Network Configuration",
        "networks_dhcp": "DHCP Server",
        "networks_ethernet": "Ethernet",
        "networks_config": "Configuration",
        "tab_routing": "Routing",
        "routing_title": "Routing",
        "routing_description": "Manage static network routes.",
        "routing_destination": "Destination",
        "routing_gateway": "Gateway",
        "routing_interface": "Interface",
        "routing_metric": "Metric",
        "routing_add_route": "Add Route",
        "routing_current_routes": "Current Routes",
        "routing_no_routes": "No routes configured.",
        "routing_route_added": "Route added successfully",
        
        # VPNs
        "vpns_title": "VPN Services",
        "vpn_ocserv": "OpenConnect VPN",
        "vpn_ipsec": "IPSec",
        "vpn_ssl": "SSL VPN",
        "vpn_ssh": "SSH",
        "vpn_openvpn": "OpenVPN",
        "vpn_install": "Install",
        "vpn_uninstall": "Uninstall",
        "vpn_start": "Start",
        "vpn_stop": "Stop",
        "vpn_restart": "Restart",
        "vpn_enable": "Enable",
        "vpn_disable": "Disable",
        "vpn_users": "Users",
        "vpn_connected": "Connected Users",
        "vpn_add_user": "Add User",
        "vpn_delete_user": "Delete User",
        "vpn_reset_password": "Reset Password",
        
        # System Settings
        "system_title": "System Settings",
        "system_updates": "System Updates",
        "system_updates_available": "Updates Available",
        "system_last_update": "Last Update",
        "system_packages": "Installed Packages",
        "system_search": "Search Packages",
        "system_search_btn": "Search",
        "system_search_help": "Search package repositories and install directly from results.",
        "system_install": "Install Package",
        "system_install_btn": "Install",
        "system_remove": "Remove Package",
        "system_remove_btn": "Remove",
        "system_quick_install": "Quick Install",
        "system_installed_count": "Total Packages",
        "system_install_all": "Install All Updates",
        "system_uptodate": "System is up to date",
        "system_reboot": "System Reboot",
        "system_reboot_help": "Restart the system immediately.",
        "system_reboot_btn": "Reboot",
        
        # Administration
        "admin_title": "Administration",
        "admin_password": "Change Admin Password",
        "admin_current_pass": "Current Password",
        "admin_new_pass": "New Password",
        "admin_confirm_pass": "Confirm Password",
        "admin_change_pass": "Change Password",
        "admin_language": "Change Language",
        "admin_backups": "Configuration Backups",
        "admin_create_backup": "Create Backup",
        "admin_backup_size": "Size",
        "admin_backup_date": "Date",
        "admin_download": "Download",
        "admin_delete": "Delete",
        "admin_total_backups": "Total Backups",
        
        # Service Configuration
        "service_title": "Service Configuration",
        "service_config": "Configuration File",
        "service_example": "Example Configuration",
        "service_install_steps": "Installation Steps",
        "service_config_prompt": "Edit the configuration file below and save your changes.",
        "service_example_help": "Use this example configuration as a starting point.",
        "service_install_steps_help": "Follow these setup steps to install and configure this service.",
        "config_path": "Configuration Path",
        "config_file_content": "Configuration Content",
        "service_save": "Save Configuration",
        "service_installed": "Installed",
        "service_not_installed": "Not Installed",
        "service_start": "Start",
        "service_stop": "Stop",
        "service_restart": "Restart",
        "service_enable": "Enable",
        "service_disable": "Disable",
        
        # Alerts and Messages
        "alert_success": "Success",
        "alert_error": "Error",
        "alert_warning": "Warning",
        "alert_info": "Information",
        "msg_password_changed": "Password changed successfully",
        "msg_invalid_password": "Invalid current password",
        "msg_passwords_not_match": "Passwords do not match",
        "msg_password_too_short": "Password must be at least 8 characters",
        "msg_backup_created": "Backup created successfully",
        "msg_backup_deleted": "Backup deleted successfully",
        "msg_package_installed": "Package installed successfully",
        "msg_package_removed": "Package removed successfully",
        "msg_user_added": "User added successfully",
        "msg_user_deleted": "User deleted successfully",
        "msg_config_saved": "Configuration saved successfully",
        
        # Buttons and Actions
        "btn_save": "Save",
        "btn_cancel": "Cancel",
        "btn_delete": "Delete",
        "btn_confirm": "Confirm",
        "btn_manage": "Manage",
        "btn_config": "Config",
        "btn_theme": "Theme",
        "btn_close": "Close",
        "btn_edit": "Edit",
        "btn_view": "View",
        "status_yes": "Yes",
        "status_no": "No",
        "confirm_delete": "Are you sure you want to delete this?",
        "confirm_restart": "This will restart the service. Continue?",
        "confirm_update": "Install all available updates? This may take several minutes.",
        
        # Network Interfaces
        "tab_services": "Services",
        "tab_interfaces": "Network Interfaces",
        "tab_noip": "Dynamic DNS",
        "interfaces_title": "Network Interfaces Management",
        "interfaces_add_new": "Add New Interface",
        "interfaces_name": "Interface Name",
        "interfaces_type": "Interface Type",
        "interfaces_bootproto": "Boot Protocol",
        "interfaces_ipaddr": "IP Address",
        "interfaces_prefix": "Prefix (CIDR)",
        "interfaces_gateway": "Default Gateway",
        "interfaces_dns1": "Primary DNS",
        "interfaces_dns2": "Secondary DNS",
        "no_interfaces": "No network interfaces configured yet",
        "btn_add_interface": "Add Interface",
        "btn_apply_config": "Apply Configuration",
        "interface_added": "Interface added successfully",
        "interface_deleted": "Interface deleted successfully",
        "confirm_delete": "Are you sure you want to delete this interface?",
        "confirm_apply": "Apply network configuration? This may restart network services.",
        "config_applied": "Network configuration applied successfully",
        "select_option": "Select an option",
        "optional": "Optional",
        "loading": "Loading...",
        
        # NoIP Configuration
        "noip_description": "Configure NoIP.com dynamic DNS client to keep your hostname pointing to your current IP address",
        "noip_username": "NoIP Email",
        "noip_password": "NoIP Password",
        "noip_hostname": "NoIP Hostname",
    },
    
    "es": {
        # Navigation
        "sidebar_main": "Consola Principal",
        "sidebar_services": "Servicios",
        "sidebar_system": "Sistema",
        "nav_dashboard": "Panel de Control",
        "nav_proxy": "Servidor Proxy",
        "nav_firewall": "Firewall",
        "nav_logs": "Registros de Acceso",
        "nav_networks": "Redes",
        "nav_vpns": "VPNs",
        "nav_system": "Configuración del Sistema",
        "nav_admin": "Administración",
        "nav_logout": "Cerrar Sesión",
        
        # Login Page
        "login_title": "AlfaCore - Inicio de Sesión",
        "login_username": "Usuario",
        "login_password": "Contraseña",
        "login_signin": "Iniciar Sesión",
        "login_error": "Usuario o contraseña inválidos",
        
        # Dashboard
        "dashboard_title": "Panel de Control",
        "dashboard_status": "Estado del Sistema",
        "dashboard_services": "Servicios Instalados",
        "dashboard_uptime": "Tiempo de Actividad",
        "dashboard_load": "Promedio de Carga",
        "dashboard_installed": "Instalado",
        "dashboard_status_active": "Activo",
        "dashboard_status_inactive": "Inactivo",
        "dashboard_total_services": "Servicios Totales",
        "dashboard_total_services_desc": "Servicios gestionados en este host.",
        "dashboard_active_services": "Servicios Activos",
        "dashboard_active_services_desc": "Servicios actualmente en ejecución.",
        "dashboard_proxy_connections": "Conexiones Proxy",
        "dashboard_proxy_connections_desc": "Sesiones proxy activas en vivo.",
        "dashboard_firewall_status": "Estado del Firewall",
        "dashboard_health_overview": "Resumen de Salud del Sistema",
        "dashboard_service_status": "Estado del Servicio",
        
        # Docker
        "nav_docker": "Docker",
        "docker_title": "Gestión de Docker",
        "docker_status_help": "Gestiona el demonio de Docker y el ciclo de vida de los contenedores.",
        "docker_containers": "Contenedores de Docker",
        "docker_no_containers": "No se encontraron contenedores de Docker.",
        "docker_not_installed": "Docker no está instalado o no disponible.",
        "docker_container_actions": "Acciones del Contenedor",
        
        # Routing
        "tab_routing": "Enrutamiento",
        "routing_title": "Enrutamiento",
        "routing_description": "Gestiona rutas de red estáticas.",
        "routing_destination": "Destino",
        "routing_gateway": "Puerta de Enlace",
        "routing_interface": "Interfaz",
        "routing_metric": "Métrica",
        "routing_add_route": "Agregar Ruta",
        "routing_current_routes": "Rutas Actuales",
        "routing_no_routes": "Sin rutas configuradas.",
        "routing_route_added": "Ruta agregada correctamente",
        
        # Firewall Zones
        "firewall_zones": "Zonas de Firewall",
        "firewall_zones_help": "Asigna interfaces a zonas de firewall para segmentación basada en zonas.",
        "firewall_zone": "Zona",
        "firewall_interface": "Interfaz",
        "firewall_add_interface": "Añadir a Zona",
        "firewall_remove_interface": "Eliminar de Zona",
        "firewall_no_interfaces": "Sin interfaces asignadas",
        
        # System
        "system_reboot": "Reinicio del Sistema",
        "system_reboot_help": "Reinicia el sistema inmediatamente.",
        "system_reboot_btn": "Reiniciar",
        
        # Service Actions
        "service_start": "Iniciar",
        "service_stop": "Detener",
        "service_restart": "Reiniciar",
        
        # Proxy Server
        "proxy_title": "Servidor Proxy",
        "proxy_connections": "Conexiones Activas",
        "proxy_users": "Usuarios Proxy",
        "proxy_add_user": "Agregar Usuario",
        "proxy_username": "Usuario",
        "proxy_password": "Contraseña",
        "proxy_add": "Agregar",
        "proxy_delete": "Eliminar",
        "proxy_config": "Configuración de Squid",
        "proxy_save_config": "Guardar Configuración",
        "proxy_status": "Estado del Proxy",
        "proxy_start": "Iniciar",
        "proxy_stop": "Detener",
        "proxy_restart": "Reiniciar",
        "proxy_install": "Instalar Squid",
        "proxy_uninstall": "Desinstalar Squid",
        
        # System Settings
        "system_title": "Configuración del Sistema",
        "system_updates": "Actualizaciones del Sistema",
        "system_updates_available": "Actualizaciones Disponibles",
        "system_last_update": "Última Actualización",
        "system_packages": "Paquetes Instalados",
        "system_search": "Buscar Paquetes",
        "system_search_btn": "Buscar",
        "system_search_help": "Buscar en los repositorios de paquetes e instalar directamente desde los resultados.",
        "system_install": "Instalar Paquete",
        "system_install_btn": "Instalar",
        "system_remove": "Eliminar Paquete",
        "system_remove_btn": "Eliminar",
        "system_quick_install": "Instalación Rápida",
        "system_installed_count": "Paquetes Totales",
        "system_install_all": "Instalar Todas las Actualizaciones",
        "system_uptodate": "El sistema está actualizado",
        
        # Administration
        "admin_title": "Administración",
        "admin_password": "Cambiar Contraseña de Administrador",
        "admin_current_pass": "Contraseña Actual",
        "admin_new_pass": "Nueva Contraseña",
        "admin_confirm_pass": "Confirmar Contraseña",
        "admin_change_pass": "Cambiar Contraseña",
        "admin_language": "Cambiar Idioma",
        "admin_backups": "Copias de Seguridad",
        "admin_create_backup": "Crear Copia de Seguridad",
        "admin_backup_size": "Tamaño",
        "admin_backup_date": "Fecha",
        "admin_download": "Descargar",
        "admin_delete": "Eliminar",
        "admin_total_backups": "Copias de Seguridad Totales",
        
        # Buttons
        "btn_save": "Guardar",
        "btn_cancel": "Cancelar",
        "btn_delete": "Eliminar",
        "btn_confirm": "Confirmar",
        "btn_manage": "Administrar",
        "btn_config": "Configuración",
        "btn_theme": "Tema",
        "status_yes": "Sí",
        "status_no": "No",
        
        # Network Interfaces
        "tab_services": "Servicios",
        "tab_interfaces": "Interfaces de Red",
        "tab_noip": "DNS Dinámico",
        "interfaces_title": "Gestión de Interfaces de Red",
        "interfaces_add_new": "Agregar Nueva Interfaz",
        "interfaces_name": "Nombre de la Interfaz",
        "interfaces_type": "Tipo de Interfaz",
        "interfaces_bootproto": "Protocolo de Inicio",
        "interfaces_ipaddr": "Dirección IP",
        "interfaces_prefix": "Prefijo (CIDR)",
        "interfaces_gateway": "Puerta de Enlace Predeterminada",
        "interfaces_dns1": "DNS Primario",
        "interfaces_dns2": "DNS Secundario",
        "no_interfaces": "Aún no hay interfaces de red configuradas",
        "btn_add_interface": "Agregar Interfaz",
        "btn_apply_config": "Aplicar Configuración",
        "interface_added": "Interfaz agregada correctamente",
        "interface_deleted": "Interfaz eliminada correctamente",
        "confirm_delete": "¿Está seguro de que desea eliminar esta interfaz?",
        "confirm_apply": "¿Aplicar configuración de red? Esto puede reiniciar los servicios de red.",
        "config_applied": "Configuración de red aplicada correctamente",
        "select_option": "Seleccionar una opción",
        "optional": "Opcional",
        "loading": "Cargando...",
        
        # NoIP Configuration
        "noip_description": "Configure el cliente de DNS dinámico NoIP.com para mantener su nombre de host apuntando a su dirección IP actual",
        "noip_username": "Correo de NoIP",
        "noip_password": "Contraseña de NoIP",
        "noip_hostname": "Nombre de Host de NoIP",
    },
    
    "fr": {
        # Navigation
        "sidebar_main": "Console Principale",
        "sidebar_services": "Services",
        "sidebar_system": "Système",
        "nav_dashboard": "Tableau de Bord",
        "nav_proxy": "Serveur Proxy",
        "nav_firewall": "Pare-feu",
        "nav_logs": "Journaux d'Accès",
        "nav_networks": "Réseaux",
        "nav_vpns": "VPNs",
        "nav_system": "Paramètres Système",
        "nav_admin": "Administration",
        "nav_logout": "Déconnexion",
        
        # Login Page
        "login_title": "AlfaCore - Connexion",
        "login_username": "Nom d'utilisateur",
        "login_password": "Mot de passe",
        "login_signin": "Se Connecter",
        "login_error": "Nom d'utilisateur ou mot de passe invalide",
        
        # Dashboard
        "dashboard_title": "Tableau de Bord",
        "dashboard_status": "État du Système",
        "dashboard_services": "Services Installés",
        "dashboard_uptime": "Uptime Système",
        "dashboard_load": "Charge Moyenne",
        "dashboard_installed": "Installé",
        "dashboard_status_active": "Actif",
        "dashboard_status_inactive": "Inactif",
        "dashboard_total_services": "Services Totaux",
        "dashboard_total_services_desc": "Services gérés sur cet hôte.",
        "dashboard_active_services": "Services Actifs",
        "dashboard_active_services_desc": "Services en cours d'exécution.",
        "dashboard_proxy_connections": "Connexions Proxy",
        "dashboard_proxy_connections_desc": "Sessions proxy actives en direct.",
        "dashboard_firewall_status": "État du Pare-feu",
        "dashboard_health_overview": "Aperçu de l'État du Système",
        "dashboard_service_status": "État du Service",
        
        # Docker
        "nav_docker": "Docker",
        "docker_title": "Gestion Docker",
        "docker_status_help": "Gérez le démon Docker et le cycle de vie des conteneurs.",
        "docker_containers": "Conteneurs Docker",
        "docker_no_containers": "Aucun conteneur Docker trouvé.",
        "docker_not_installed": "Docker n'est pas installé ou non disponible.",
        "docker_container_actions": "Actions du Conteneur",
        
        # Routing
        "tab_routing": "Routage",
        "routing_title": "Routage",
        "routing_description": "Gérez les routes réseau statiques.",
        "routing_destination": "Destination",
        "routing_gateway": "Passerelle",
        "routing_interface": "Interface",
        "routing_metric": "Métrique",
        "routing_add_route": "Ajouter une Route",
        "routing_current_routes": "Routes Actuelles",
        "routing_no_routes": "Aucune route configurée.",
        "routing_route_added": "Route ajoutée avec succès",
        
        # Firewall Zones
        "firewall_zones": "Zones Firewall",
        "firewall_zones_help": "Attribuez des interfaces aux zones de pare-feu pour la segmentation basée sur les zones.",
        "firewall_zone": "Zone",
        "firewall_interface": "Interface",
        "firewall_add_interface": "Ajouter à la Zone",
        "firewall_remove_interface": "Supprimer de la Zone",
        "firewall_no_interfaces": "Aucune interface attribuée",
        
        # System
        "system_reboot": "Redémarrage Système",
        "system_reboot_help": "Redémarrez le système immédiatement.",
        "system_reboot_btn": "Redémarrer",
        
        # Service Actions
        "service_start": "Démarrer",
        "service_stop": "Arrêter",
        "service_restart": "Redémarrer",
        
        # Proxy Server
        "proxy_title": "Serveur Proxy",
        "proxy_connections": "Connexions Actives",
        "proxy_users": "Utilisateurs Proxy",
        "proxy_add_user": "Ajouter Utilisateur",
        "proxy_username": "Nom d'utilisateur",
        "proxy_password": "Mot de passe",
        "proxy_add": "Ajouter",
        "proxy_delete": "Supprimer",
        "proxy_config": "Configuration Squid",
        "proxy_save_config": "Enregistrer Configuration",
        "proxy_status": "État du Proxy",
        "proxy_start": "Démarrer",
        "proxy_stop": "Arrêter",
        "proxy_restart": "Redémarrer",
        "proxy_install": "Installer Squid",
        "proxy_uninstall": "Désinstaller Squid",
        
        # System Settings
        "system_title": "Paramètres Système",
        "system_updates": "Mises à Jour du Système",
        "system_updates_available": "Mises à Jour Disponibles",
        "system_last_update": "Dernière Mise à Jour",
        "system_packages": "Paquets Installés",
        "system_search": "Rechercher Paquets",
        "system_search_btn": "Rechercher",
        "system_search_help": "Recherchez dans les dépôts de paquets et installez directement depuis les résultats.",
        "system_install": "Installer Paquet",
        "system_install_btn": "Installer",
        "system_remove": "Supprimer Paquet",
        "system_remove_btn": "Supprimer",
        "system_quick_install": "Installation Rapide",
        "system_installed_count": "Paquets Totaux",
        "system_install_all": "Installer Toutes les Mises à Jour",
        "system_uptodate": "Le système est à jour",
        
        # Administration
        "admin_title": "Administration",
        "admin_password": "Changer le Mot de Passe",
        "admin_current_pass": "Mot de Passe Actuel",
        "admin_new_pass": "Nouveau Mot de Passe",
        "admin_confirm_pass": "Confirmer Mot de Passe",
        "admin_change_pass": "Changer Mot de Passe",
        "admin_language": "Changer la Langue",
        "admin_backups": "Sauvegardes",
        "admin_create_backup": "Créer Sauvegarde",
        "admin_backup_size": "Taille",
        "admin_backup_date": "Date",
        "admin_download": "Télécharger",
        "admin_delete": "Supprimer",
        "admin_total_backups": "Sauvegardes Totales",
        
        # Buttons
        "btn_save": "Enregistrer",
        "btn_cancel": "Annuler",
        "btn_delete": "Supprimer",
        "btn_confirm": "Confirmer",
        "btn_manage": "Gérer",
        "btn_config": "Configurer",
        "btn_theme": "Thème",
        "status_yes": "Oui",
        "status_no": "Non",
        
        # Network Interfaces
        "tab_services": "Services",
        "tab_interfaces": "Interfaces Réseau",
        "tab_noip": "DNS Dynamique",
        "interfaces_title": "Gestion des Interfaces Réseau",
        "interfaces_add_new": "Ajouter une Nouvelle Interface",
        "interfaces_name": "Nom de l'Interface",
        "interfaces_type": "Type d'Interface",
        "interfaces_bootproto": "Protocole de Démarrage",
        "interfaces_ipaddr": "Adresse IP",
        "interfaces_prefix": "Préfixe (CIDR)",
        "interfaces_gateway": "Passerelle par Défaut",
        "interfaces_dns1": "DNS Primaire",
        "interfaces_dns2": "DNS Secondaire",
        "no_interfaces": "Aucune interface réseau configurée pour le moment",
        "btn_add_interface": "Ajouter une Interface",
        "btn_apply_config": "Appliquer la Configuration",
        "interface_added": "Interface ajoutée avec succès",
        "interface_deleted": "Interface supprimée avec succès",
        "confirm_delete": "Êtes-vous sûr de vouloir supprimer cette interface ?",
        "confirm_apply": "Appliquer la configuration réseau ? Cela peut redémarrer les services réseau.",
        "config_applied": "Configuration réseau appliquée avec succès",
        "select_option": "Sélectionner une option",
        "optional": "Optionnel",
        "loading": "Chargement...",
        
        # NoIP Configuration
        "noip_description": "Configurez le client DNS dynamique NoIP.com pour que votre nom d'hôte pointe vers votre adresse IP actuelle",
        "noip_username": "Email NoIP",
        "noip_password": "Mot de passe NoIP",
        "noip_hostname": "Nom d'Hôte NoIP",
    },
    
    "de": {
        # Navigation
        "sidebar_main": "Hauptkonsole",
        "sidebar_services": "Dienste",
        "sidebar_system": "System",
        "nav_dashboard": "Übersicht",
        "nav_proxy": "Proxy-Server",
        "nav_firewall": "Firewall",
        "nav_logs": "Zugriffsprotokolle",
        "nav_networks": "Netzwerke",
        "nav_vpns": "VPNs",
        "nav_system": "Systemeinstellungen",
        "nav_admin": "Verwaltung",
        "nav_logout": "Abmelden",
        
        # Login Page
        "login_title": "AlfaCore - Anmeldung",
        "login_username": "Benutzername",
        "login_password": "Passwort",
        "login_signin": "Anmelden",
        "login_error": "Ungültiger Benutzername oder Passwort",
        
        # Dashboard
        "dashboard_title": "Übersicht",
        "dashboard_status": "Systemstatus",
        "dashboard_services": "Installierte Dienste",
        "dashboard_uptime": "Systemlaufzeit",
        "dashboard_load": "Durchschnittslast",
        "dashboard_installed": "Installiert",
        "dashboard_status_active": "Aktiv",
        "dashboard_status_inactive": "Inaktiv",
        "dashboard_total_services": "Gesamte Dienste",
        "dashboard_total_services_desc": "Verwaltete Dienste auf diesem Host.",
        "dashboard_active_services": "Aktive Dienste",
        "dashboard_active_services_desc": "Derzeit ausgeführte Dienste.",
        "dashboard_proxy_connections": "Proxy-Verbindungen",
        "dashboard_proxy_connections_desc": "Live aktive Proxy-Sitzungen.",
        "dashboard_firewall_status": "Firewall-Status",
        "dashboard_health_overview": "Systemzustandsübersicht",
        "dashboard_service_status": "Dienststatus",
        
        # Docker
        "nav_docker": "Docker",
        "docker_title": "Docker-Verwaltung",
        "docker_status_help": "Verwalten Sie den Docker-Daemon und den Containerleben-zyklus.",
        "docker_containers": "Docker-Container",
        "docker_no_containers": "Keine Docker-Container gefunden.",
        "docker_not_installed": "Docker ist nicht installiert oder nicht verfügbar.",
        "docker_container_actions": "Container-Aktionen",
        
        # Routing
        "tab_routing": "Routing",
        "routing_title": "Routing",
        "routing_description": "Verwalten Sie statische Netzwerkrouten.",
        "routing_destination": "Ziel",
        "routing_gateway": "Gateway",
        "routing_interface": "Schnittstelle",
        "routing_metric": "Metrik",
        "routing_add_route": "Route Hinzufügen",
        "routing_current_routes": "Aktuelle Routen",
        "routing_no_routes": "Keine Routen konfiguriert.",
        "routing_route_added": "Route erfolgreich hinzugefügt",
        
        # Firewall Zones
        "firewall_zones": "Firewall-Zonen",
        "firewall_zones_help": "Weisen Sie Schnittstellen Firewall-Zonen zu für zonenbasierte Segmentierung.",
        "firewall_zone": "Zone",
        "firewall_interface": "Schnittstelle",
        "firewall_add_interface": "Zur Zone Hinzufügen",
        "firewall_remove_interface": "Aus Zone Entfernen",
        "firewall_no_interfaces": "Keine Schnittstellen zugewiesen",
        
        # System
        "system_reboot": "Systemstart",
        "system_reboot_help": "Starten Sie das System sofort neu.",
        "system_reboot_btn": "Neustart",
        
        # Service Actions
        "service_start": "Starten",
        "service_stop": "Stoppen",
        "service_restart": "Neu starten",
        
        # System Settings
        "system_title": "Systemeinstellungen",
        "system_updates": "Systemaktualisierungen",
        "system_updates_available": "Verfügbare Updates",
        "system_last_update": "Letzte Aktualisierung",
        "system_packages": "Installierte Pakete",
        "system_search": "Pakete durchsuchen",
        "system_search_btn": "Suchen",
        "system_search_help": "Durchsuchen Sie Paket-Repositories und installieren Sie direkt aus den Ergebnissen.",
        "system_install": "Paket installieren",
        "system_install_btn": "Installieren",
        "system_remove": "Paket entfernen",
        "system_remove_btn": "Entfernen",
        "system_quick_install": "Schnellinstallation",
        "system_installed_count": "Gesamtpakete",
        "system_install_all": "Alle Updates installieren",
        "system_uptodate": "System ist aktuell",
        
        # Administration
        "admin_title": "Verwaltung",
        "admin_password": "Admin-Passwort ändern",
        "admin_current_pass": "Aktuelles Passwort",
        "admin_new_pass": "Neues Passwort",
        "admin_confirm_pass": "Passwort bestätigen",
        "admin_change_pass": "Passwort ändern",
        "admin_language": "Sprache ändern",
        "admin_backups": "Sicherungen",
        "admin_create_backup": "Sicherung erstellen",
        "admin_backup_size": "Größe",
        "admin_backup_date": "Datum",
        "admin_download": "Herunterladen",
        "admin_delete": "Löschen",
        "admin_total_backups": "Gesamtsicherungen",
        
        # Buttons
        "btn_save": "Speichern",
        "btn_cancel": "Abbrechen",
        "btn_delete": "Löschen",
        "btn_confirm": "Bestätigen",
        "btn_manage": "Verwalten",
        "btn_config": "Konfigurieren",
        "btn_theme": "Thema",
        "status_yes": "Ja",
        "status_no": "Nein",
        
        # Network Interfaces
        "tab_services": "Dienste",
        "tab_interfaces": "Netzwerkschnittstellen",
        "tab_noip": "Dynamisches DNS",
        "interfaces_title": "Verwaltung von Netzwerkschnittstellen",
        "interfaces_add_new": "Neue Schnittstelle Hinzufügen",
        "interfaces_name": "Name der Schnittstelle",
        "interfaces_type": "Typ der Schnittstelle",
        "interfaces_bootproto": "Boot-Protokoll",
        "interfaces_ipaddr": "IP-Adresse",
        "interfaces_prefix": "Präfix (CIDR)",
        "interfaces_gateway": "Standardgateway",
        "interfaces_dns1": "Primäres DNS",
        "interfaces_dns2": "Sekundäres DNS",
        "no_interfaces": "Noch keine Netzwerkschnittstellen konfiguriert",
        "btn_add_interface": "Schnittstelle Hinzufügen",
        "btn_apply_config": "Konfiguration Anwenden",
        "interface_added": "Schnittstelle erfolgreich hinzugefügt",
        "interface_deleted": "Schnittstelle erfolgreich gelöscht",
        "confirm_delete": "Möchten Sie diese Schnittstelle wirklich löschen?",
        "confirm_apply": "Netzwerkkonfiguration anwenden? Dies kann Netzwerkdienste neu starten.",
        "config_applied": "Netzwerkkonfiguration erfolgreich angewendet",
        "select_option": "Option auswählen",
        "optional": "Optional",
        "loading": "Wird geladen...",
        
        # NoIP Configuration
        "noip_description": "Konfigurieren Sie den NoIP.com Dynamic DNS-Client, um Ihren Hostnamen auf Ihre aktuelle IP-Adresse zu verweisen",
        "noip_username": "NoIP E-Mail",
        "noip_password": "NoIP-Passwort",
        "noip_hostname": "NoIP-Hostname",
    },
    
    "ar": {
        # Navigation
        "sidebar_main": "وحدة التحكم الرئيسية",
        "sidebar_services": "الخدمات",
        "sidebar_system": "النظام",
        "nav_dashboard": "لوحة التحكم",
        "nav_proxy": "خادم الوكيل",
        "nav_firewall": "جدار الحماية",
        "nav_logs": "سجلات الوصول",
        "nav_networks": "الشبكات",
        "nav_vpns": "شبكات VPN",
        "nav_system": "إعدادات النظام",
        "nav_admin": "الإدارة",
        "nav_logout": "تسجيل الخروج",
        
        # Login Page
        "login_title": "AlfaCore - تسجيل الدخول",
        "login_username": "اسم المستخدم",
        "login_password": "كلمة المرور",
        "login_signin": "تسجيل الدخول",
        "login_error": "اسم مستخدم أو كلمة مرور غير صحيحة",
        
        # Dashboard
        "dashboard_title": "لوحة التحكم",
        "dashboard_status": "حالة النظام",
        "dashboard_services": "الخدمات المثبتة",
        "dashboard_uptime": "وقت التشغيل",
        "dashboard_load": "متوسط الحمل",
        "dashboard_installed": "مثبت",
        "dashboard_status_active": "نشط",
        "dashboard_status_inactive": "غير نشط",
        
        # System Settings
        "system_title": "إعدادات النظام",
        "system_updates": "تحديثات النظام",
        "system_updates_available": "التحديثات المتاحة",
        "system_last_update": "آخر تحديث",
        "system_packages": "الحزم المثبتة",
        "system_search": "البحث عن الحزم",
        "system_search_btn": "بحث",
        "system_search_help": "ابحث في مستودعات الحزم وقم بالتثبيت مباشرة من النتائج.",
        "system_install": "تثبيت الحزمة",
        "system_install_btn": "تثبيت",
        "system_remove": "إزالة الحزمة",
        "system_remove_btn": "إزالة",
        "system_quick_install": "التثبيت السريع",
        "system_installed_count": "إجمالي الحزم",
        "system_install_all": "تثبيت جميع التحديثات",
        "system_uptodate": "النظام محدث",
        
        # Administration
        "admin_title": "الإدارة",
        "admin_password": "تغيير كلمة مرور المسؤول",
        "admin_current_pass": "كلمة المرور الحالية",
        "admin_new_pass": "كلمة المرور الجديدة",
        "admin_confirm_pass": "تأكيد كلمة المرور",
        "admin_change_pass": "تغيير كلمة المرور",
        "admin_language": "تغيير اللغة",
        "admin_backups": "النسخ الاحتياطية",
        "admin_create_backup": "إنشاء نسخة احتياطية",
        "admin_backup_size": "الحجم",
        "admin_backup_date": "التاريخ",
        "admin_download": "تحميل",
        "admin_delete": "حذف",
        "admin_total_backups": "إجمالي النسخ الاحتياطية",
        
        # Buttons
        "btn_save": "حفظ",
        "btn_cancel": "إلغاء",
        "btn_delete": "حذف",
        "btn_confirm": "تأكيد",
        "btn_manage": "إدارة",
        "btn_config": "التكوين",
        "btn_theme": "الوضع",
        "status_yes": "نعم",
        "status_no": "لا",
        
        # Network Interfaces
        "tab_services": "الخدمات",
        "tab_interfaces": "واجهات الشبكة",
        "tab_noip": "DNS الديناميكي",
        "interfaces_title": "إدارة واجهات الشبكة",
        "interfaces_add_new": "إضافة واجهة جديدة",
        "interfaces_name": "اسم الواجهة",
        "interfaces_type": "نوع الواجهة",
        "interfaces_bootproto": "بروتوكول الإقلاع",
        "interfaces_ipaddr": "عنوان IP",
        "interfaces_prefix": "البادئة (CIDR)",
        "interfaces_gateway": "البوابة الافتراضية",
        "interfaces_dns1": "DNS الأساسي",
        "interfaces_dns2": "DNS الثانوي",
        "no_interfaces": "لم يتم تكوين واجهات شبكة حتى الآن",
        "btn_add_interface": "إضافة واجهة",
        "btn_apply_config": "تطبيق الإعدادات",
        "interface_added": "تمت إضافة الواجهة بنجاح",
        "interface_deleted": "تم حذف الواجهة بنجاح",
        "confirm_delete": "هل أنت متأكد من حذف هذه الواجهة؟",
        "confirm_apply": "تطبيق إعدادات الشبكة؟ قد يؤدي هذا إلى إعادة تشغيل خدمات الشبكة.",
        "config_applied": "تم تطبيق إعدادات الشبكة بنجاح",
        "select_option": "اختر خيار",
        "optional": "اختياري",
        "loading": "جاري التحميل...",
        
        # NoIP Configuration
        "noip_description": "قم بتكوين عميل NoIP.com DNS الديناميكي للحفاظ على اسم المضيف الخاص بك موجه إلى عنوان IP الحالي الخاص بك",
        "noip_username": "بريد NoIP الإلكتروني",
        "noip_password": "كلمة مرور NoIP",
        "noip_hostname": "اسم مضيف NoIP",
        
        # Docker
        "nav_docker": "Docker",
        "docker_title": "إدارة Docker",
        "docker_status_help": "إدارة خادم Docker وحياة دورة الحاويات.",
        "docker_containers": "حاويات Docker",
        "docker_no_containers": "لم يتم العثور على حاويات Docker.",
        "docker_not_installed": "Docker غير مثبت أو غير متاح.",
        "docker_container_actions": "إجراءات الحاوية",
        
        # Routing
        "tab_routing": "التوجيه",
        "routing_title": "التوجيه",
        "routing_description": "إدارة مسارات الشبكة الثابتة.",
        "routing_destination": "الوجهة",
        "routing_gateway": "البوابة",
        "routing_interface": "الواجهة",
        "routing_metric": "المقياس",
        "routing_add_route": "إضافة مسار",
        "routing_current_routes": "المسارات الحالية",
        "routing_no_routes": "لا توجد مسارات مكونة.",
        "routing_route_added": "تمت إضافة المسار بنجاح",
        
        # Firewall Zones
        "firewall_zones": "مناطق جدار الحماية",
        "firewall_zones_help": "أسند الواجهات إلى مناطق جدار الحماية للتقسيم بناءً على المنطقة.",
        "firewall_zone": "منطقة",
        "firewall_interface": "واجهة",
        "firewall_add_interface": "إضافة إلى منطقة",
        "firewall_remove_interface": "إزالة من منطقة",
        "firewall_no_interfaces": "لا توجد واجهات مسندة",
        
        # System
        "system_reboot": "إعادة تشغيل النظام",
        "system_reboot_help": "أعد تشغيل النظام فوراً.",
        "system_reboot_btn": "إعادة تشغيل",
        
        # Service Actions
        "service_start": "بدء التشغيل",
        "service_stop": "إيقاف",
        "service_restart": "إعادة تشغيل",
    },
    
    "zh": {
        # Navigation
        "sidebar_main": "主控制台",
        "sidebar_services": "服务",
        "sidebar_system": "系统",
        "nav_dashboard": "仪表板",
        "nav_proxy": "代理服务器",
        "nav_firewall": "防火墙",
        "nav_logs": "访问日志",
        "nav_networks": "网络",
        "nav_vpns": "VPN",
        "nav_system": "系统设置",
        "nav_admin": "管理",
        "nav_logout": "登出",
        
        # Login Page
        "login_title": "AlfaCore - 登录",
        "login_username": "用户名",
        "login_password": "密码",
        "login_signin": "登录",
        "login_error": "用户名或密码无效",
        
        # Dashboard
        "dashboard_title": "仪表板",
        "dashboard_status": "系统状态",
        "dashboard_services": "已安装的服务",
        "dashboard_uptime": "系统运行时间",
        "dashboard_load": "平均负载",
        "dashboard_installed": "已安装",
        "dashboard_status_active": "活跃",
        "dashboard_status_inactive": "非活跃",
        
        # System Settings
        "system_title": "系统设置",
        "system_updates": "系统更新",
        "system_updates_available": "可用更新",
        "system_last_update": "最后更新",
        "system_packages": "已安装的软件包",
        "system_search": "搜索软件包",
        "system_search_btn": "搜索",
        "system_search_help": "搜索软件包存储库并直接从结果中安装。",
        "system_install": "安装软件包",
        "system_install_btn": "安装",
        "system_remove": "删除软件包",
        "system_remove_btn": "删除",
        "system_quick_install": "快速安装",
        "system_installed_count": "总软件包",
        "system_install_all": "安装所有更新",
        "system_uptodate": "系统已更新",
        
        # Administration
        "admin_title": "管理",
        "admin_password": "更改管理员密码",
        "admin_current_pass": "当前密码",
        "admin_new_pass": "新密码",
        "admin_confirm_pass": "确认密码",
        "admin_change_pass": "更改密码",
        "admin_language": "更改语言",
        "admin_backups": "备份",
        "admin_create_backup": "创建备份",
        "admin_backup_size": "大小",
        "admin_backup_date": "日期",
        "admin_download": "下载",
        "admin_delete": "删除",
        "admin_total_backups": "总备份数",
        
        # Buttons
        "btn_save": "保存",
        "btn_cancel": "取消",
        "btn_delete": "删除",
        "btn_confirm": "确认",
        "btn_manage": "管理",
        "btn_config": "配置",
        "btn_theme": "主题",
        "status_yes": "是",
        "status_no": "否",
        
        # Network Interfaces
        "tab_services": "服务",
        "tab_interfaces": "网络接口",
        "tab_noip": "动态DNS",
        "interfaces_title": "网络接口管理",
        "interfaces_add_new": "添加新接口",
        "interfaces_name": "接口名称",
        "interfaces_type": "接口类型",
        "interfaces_bootproto": "启动协议",
        "interfaces_ipaddr": "IP地址",
        "interfaces_prefix": "前缀 (CIDR)",
        "interfaces_gateway": "默认网关",
        "interfaces_dns1": "主DNS",
        "interfaces_dns2": "备用DNS",
        "no_interfaces": "尚未配置网络接口",
        "btn_add_interface": "添加接口",
        "btn_apply_config": "应用配置",
        "interface_added": "接口添加成功",
        "interface_deleted": "接口删除成功",
        "confirm_delete": "确定要删除此接口吗？",
        "confirm_apply": "应用网络配置？这可能会重启网络服务。",
        "config_applied": "网络配置应用成功",
        "select_option": "选择选项",
        "optional": "可选",
        "loading": "加载中...",
        
        # NoIP Configuration
        "noip_description": "配置NoIP.com动态DNS客户端以保持您的主机名指向您的当前IP地址",
        "noip_username": "NoIP邮箱",
        "noip_password": "NoIP密码",
        "noip_hostname": "NoIP主机名",
        
        # Docker
        "nav_docker": "Docker",
        "docker_title": "Docker 管理",
        "docker_status_help": "管理 Docker 守护进程和容器生命周期。",
        "docker_containers": "Docker 容器",
        "docker_no_containers": "未找到 Docker 容器。",
        "docker_not_installed": "Docker 未安装或不可用。",
        "docker_container_actions": "容器操作",
        
        # Routing
        "tab_routing": "路由",
        "routing_title": "路由",
        "routing_description": "管理静态网络路由。",
        "routing_destination": "目标",
        "routing_gateway": "网关",
        "routing_interface": "接口",
        "routing_metric": "度量",
        "routing_add_route": "添加路由",
        "routing_current_routes": "当前路由",
        "routing_no_routes": "未配置路由。",
        "routing_route_added": "路由添加成功",
        
        # Firewall Zones
        "firewall_zones": "防火墙区域",
        "firewall_zones_help": "将接口分配给防火墙区域以进行基于区域的分段。",
        "firewall_zone": "区域",
        "firewall_interface": "接口",
        "firewall_add_interface": "添加到区域",
        "firewall_remove_interface": "从区域删除",
        "firewall_no_interfaces": "未分配接口",
        
        # System
        "system_reboot": "系统重启",
        "system_reboot_help": "立即重启系统。",
        "system_reboot_btn": "重启",
        
        # Service Actions
        "service_start": "开始",
        "service_stop": "停止",
        "service_restart": "重启",
    }
}

def get_translation(language: str, key: str, default: str = None) -> str:
    """
    Get a translated string
    
    Args:
        language: Language code (en, es, fr, de, ar, zh)
        key: Translation key
        default: Default value if key not found
        
    Returns:
        Translated string or default value
    """
    if language not in TRANSLATIONS:
        language = "en"  # Fallback to English
    
    if key in TRANSLATIONS[language]:
        return TRANSLATIONS[language][key]

    # Fall back to English when a translation is missing
    if language != "en" and key in TRANSLATIONS["en"]:
        return TRANSLATIONS["en"][key]
    
    if default:
        return default
    
    # Return the key itself if not found
    return key

def get_all_translations(language: str) -> dict:
    """
    Get all translations for a specific language
    
    Args:
        language: Language code
        
    Returns:
        Dictionary of all translations
    """
    if language not in TRANSLATIONS:
        language = "en"
    
    return TRANSLATIONS[language]
