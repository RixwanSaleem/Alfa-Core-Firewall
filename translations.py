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
        
        # Networks
        "networks_title": "Network Configuration",
        "networks_dhcp": "DHCP Server",
        "networks_ethernet": "Ethernet",
        "networks_config": "Configuration",
        
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
        "system_install": "Install Package",
        "system_install_btn": "Install",
        "system_remove": "Remove Package",
        "system_remove_btn": "Remove",
        "system_quick_install": "Quick Install",
        "system_installed_count": "Total Packages",
        "system_install_all": "Install All Updates",
        "system_uptodate": "System is up to date",
        
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
        "service_save": "Save Configuration",
        "service_installed": "Installed",
        "service_not_installed": "Not Installed",
        
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
        "btn_close": "Close",
        "btn_edit": "Edit",
        "btn_view": "View",
        "confirm_delete": "Are you sure you want to delete this?",
        "confirm_restart": "This will restart the service. Continue?",
        "confirm_update": "Install all available updates? This may take several minutes.",
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
        
        # System Settings
        "system_title": "Systemeinstellungen",
        "system_updates": "Systemaktualisierungen",
        "system_updates_available": "Verfügbare Updates",
        "system_last_update": "Letzte Aktualisierung",
        "system_packages": "Installierte Pakete",
        "system_search": "Pakete durchsuchen",
        "system_search_btn": "Suchen",
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
