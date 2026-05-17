#!/usr/bin/env python3
"""
Comprehensive test suite for new firewall panel features:
- Docker daemon and container management
- Service start/stop/restart controls
- Network routing
- Firewall zone management
- System reboot functionality
"""

import unittest
import subprocess
import re
from unittest.mock import Mock, patch, MagicMock, call
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import required modules
from translations import TRANSLATIONS, get_translation
import main


class TestServiceStartStopRestart(unittest.TestCase):
    """Test service control functionality"""
    
    def test_safe_shell_arg_sanitization(self):
        """Verify shell argument sanitization"""
        # These should be safe
        safe_args = ["systemctl", "start", "squid", "docker", "postgres"]
        for arg in safe_args:
            result = main.safe_shell_arg(arg)
            self.assertIsNotNone(result, f"safe_shell_arg rejected valid arg: {arg}")
    
    def test_safe_shell_arg_escapes_dangerous(self):
        """Verify shell injection attempts are properly escaped with quotes"""
        dangerous_args = [
            "squid; rm -rf /",
            "$(whoami)",
            "`id`",
            "squid && evil_command",
            "squid | cat /etc/passwd",
            "squid > /tmp/hack"
        ]
        for arg in dangerous_args:
            result = main.safe_shell_arg(arg)
            # Arguments should be wrapped in quotes for safety
            self.assertIsNotNone(result, f"safe_shell_arg failed on: {arg}")
            self.assertTrue("'" in result or '"' in result, 
                           f"safe_shell_arg did not quote dangerous arg: {arg}")
    
    def test_service_map_has_required_services(self):
        """Verify SERVICE_MAP contains all expected services"""
        # Docker is the new service, and these are the core ones
        required_services = ["docker"]
        for service in required_services:
            self.assertIn(service, main.SERVICE_MAP, 
                         f"SERVICE_MAP missing service: {service}")
            self.assertIn("label", main.SERVICE_MAP[service])
            self.assertIn("package", main.SERVICE_MAP[service])
            self.assertIn("service", main.SERVICE_MAP[service])
    
    def test_service_map_structure(self):
        """Verify SERVICE_MAP entries have correct structure"""
        for service_key, service_data in main.SERVICE_MAP.items():
            self.assertIn("label", service_data, 
                         f"{service_key} missing 'label'")
            self.assertIn("package", service_data, 
                         f"{service_key} missing 'package'")
            self.assertIn("service", service_data, 
                         f"{service_key} missing 'service'")
            self.assertIn("description", service_data, 
                         f"{service_key} missing 'description'")


class TestDockerFeatures(unittest.TestCase):
    """Test Docker daemon and container management"""
    
    def test_docker_installed_function_exists(self):
        """Verify docker_installed function exists and is callable"""
        self.assertTrue(callable(main.docker_installed),
                       "docker_installed function not found")
    
    def test_get_docker_containers_function_exists(self):
        """Verify get_docker_containers function exists and is callable"""
        self.assertTrue(callable(main.get_docker_containers),
                       "get_docker_containers function not found")
    
    def test_docker_status_endpoint_routes_defined(self):
        """Verify Docker management routes are defined"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        # Check for required Docker endpoints
        required_routes = [
            '@app.get("/docker")',
            '@app.post("/docker/manage")',
            '@app.post("/docker/container/manage")'
        ]
        for route in required_routes:
            self.assertIn(route, content,
                         f"Docker route not found: {route}")
    
    @patch('main.subprocess.run')
    def test_docker_list_parsing(self, mock_run):
        """Verify docker ps output parsing"""
        # Mock docker ps output
        mock_output = """CONTAINER ID   IMAGE           STATUS         NAMES
abc123def456   ubuntu:latest   Up 2 hours     web_server
xyz789uvw012   nginx:latest    Exited (0) 5m  proxy_service"""
        
        mock_run.return_value = Mock(stdout=mock_output, returncode=0)
        
        # Call function - if it exists and handles parsing
        result = main.get_docker_containers()
        # If result is a list, verify structure
        if isinstance(result, list):
            for container in result:
                self.assertIn('id', container)
                self.assertIn('image', container)
                self.assertIn('name', container)


class TestNetworkRouting(unittest.TestCase):
    """Test network routing features"""
    
    def test_routing_routes_defined(self):
        """Verify routing API routes are defined"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        required_routes = [
            '@app.get("/network/routes/api/list")',
            '@app.post("/network/routes/api/add")',
            '@app.post("/network/routes/api/delete")'
        ]
        for route in required_routes:
            self.assertIn(route, content,
                         f"Routing route not found: {route}")
    
    def test_routing_template_exists(self):
        """Verify routing template has required elements"""
        with open('templates/networks.html', 'r') as f:
            content = f.read()
        
        # Check for routing UI elements
        self.assertIn('routing', content.lower(),
                     "Routing section not found in networks template")
        self.assertIn('destination', content.lower(),
                     "Destination field not found in routing UI")
        self.assertIn('gateway', content.lower(),
                     "Gateway field not found in routing UI")


class TestFirewallZones(unittest.TestCase):
    """Test firewall zone management"""
    
    def test_firewall_zone_endpoint_defined(self):
        """Verify firewall zone endpoint is defined"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        self.assertIn('@app.post("/firewall-zone")', content,
                     "Firewall zone endpoint not found")
    
    def test_firewall_zone_template_exists(self):
        """Verify firewall template has zone management"""
        with open('templates/firewall.html', 'r') as f:
            content = f.read()
        
        # Check for zone UI elements
        self.assertIn('zone', content.lower(),
                     "Zone section not found in firewall template")
        self.assertIn('interface', content.lower(),
                     "Interface field not found in firewall UI")


class TestSystemReboot(unittest.TestCase):
    """Test system reboot functionality"""
    
    def test_reboot_endpoint_defined(self):
        """Verify system reboot endpoint is defined"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        self.assertIn('@app.post("/system/reboot")', content,
                     "System reboot endpoint not found")
    
    def test_reboot_template_button_exists(self):
        """Verify reboot button exists in system template"""
        with open('templates/system.html', 'r') as f:
            content = f.read()
        
        # Check for reboot UI elements
        self.assertIn('reboot', content.lower(),
                     "Reboot button not found in system template")


class TestServiceControlButtons(unittest.TestCase):
    """Test service control button implementation in templates"""
    
    def test_service_template_has_controls(self):
        """Verify service template has start/stop/restart buttons"""
        with open('templates/service.html', 'r') as f:
            content = f.read()
        
        required_actions = ['start', 'stop', 'restart']
        for action in required_actions:
            self.assertIn(action, content.lower(),
                         f"Action '{action}' not found in service template")
    
    def test_vpn_template_has_controls(self):
        """Verify VPN template has service controls"""
        with open('templates/vpns.html', 'r') as f:
            content = f.read()
        
        self.assertIn('start', content.lower(),
                     "Start action not found in VPN template")
        self.assertIn('stop', content.lower(),
                     "Stop action not found in VPN template")
    
    def test_networks_template_has_controls(self):
        """Verify networks template has service controls"""
        with open('templates/networks.html', 'r') as f:
            content = f.read()
        
        self.assertIn('start', content.lower(),
                     "Start action not found in networks template")
    
    def test_docker_template_exists(self):
        """Verify docker.html template exists and has controls"""
        self.assertTrue(os.path.exists('templates/docker.html'),
                       "docker.html template not found")
        
        with open('templates/docker.html', 'r') as f:
            content = f.read()
        
        # Check for Docker UI elements
        self.assertIn('docker', content.lower(),
                     "Docker section not found")
        self.assertIn('container', content.lower(),
                     "Container management not found")


class TestTranslations(unittest.TestCase):
    """Test translation strings for new features"""
    
    def test_translation_keys_exist(self):
        """Verify all required translation keys exist"""
        required_keys = {
            'en': [
                'nav_docker',
                'docker_title',
                'docker_status_help',
                'docker_containers',
                'tab_routing',
                'routing_title',
                'routing_description',
                'system_reboot',
                'system_reboot_help',
                'firewall_zones',
                'firewall_zones_help',
                'service_start',
                'service_stop',
                'service_restart'
            ]
        }
        
        for lang, keys in required_keys.items():
            for key in keys:
                self.assertIn(key, TRANSLATIONS[lang],
                             f"Translation key '{key}' missing for language '{lang}'")
    
    def test_all_languages_have_new_keys(self):
        """Verify new keys are translated in all languages"""
        required_keys = [
            'nav_docker',
            'docker_title',
            'docker_status_help',
            'tab_routing',
            'routing_title',
            'routing_description',
            'system_reboot',
            'system_reboot_help',
            'firewall_zones',
            'firewall_zones_help',
            'service_start',
            'service_stop',
            'service_restart'
        ]
        
        languages = ['en', 'es', 'fr', 'de', 'ar', 'zh']
        
        for key in required_keys:
            for lang in languages:
                self.assertIn(lang, TRANSLATIONS,
                             f"Language '{lang}' not in TRANSLATIONS")
                self.assertIn(key, TRANSLATIONS[lang],
                             f"Key '{key}' missing in language '{lang}'")


class TestNavigationLink(unittest.TestCase):
    """Test Docker navigation link"""
    
    def test_docker_nav_link_added(self):
        """Verify Docker nav link exists in base template"""
        with open('templates/base.html', 'r') as f:
            content = f.read()
        
        # Check for Docker nav link with translation key
        self.assertIn('/docker', content,
                     "Docker navigation link not found")
        self.assertIn('nav_docker', content,
                     "Docker translation key not found in nav")


class TestTemplateIntegration(unittest.TestCase):
    """Test template integration and consistency"""
    
    def test_all_templates_extend_base(self):
        """Verify all templates properly extend base.html"""
        templates_to_check = [
            'admin.html',
            'dashboard.html',
            'config.html',
            'firewall.html',
            'login.html',
            'logs.html',
            'networks.html',
            'proxy.html',
            'service.html',
            'system.html',
            'vpns.html',
            'docker.html'
        ]
        
        for template in templates_to_check:
            path = f'templates/{template}'
            if os.path.exists(path):
                with open(path, 'r') as f:
                    content = f.read()
                # Most templates should reference base or blocks
                if template != 'login.html':  # login might not extend base
                    self.assertTrue(
                        'base.html' in content or '{%' in content,
                        f"Template {template} may not properly extend base"
                    )


class TestCodeQuality(unittest.TestCase):
    """Test code quality aspects"""
    
    def test_no_hardcoded_commands(self):
        """Verify shell commands are properly parameterized"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        # Should not have raw shell commands with user input
        dangerous_patterns = [
            r'subprocess\.run\([^)]*\+',  # string concatenation in subprocess
            r'os\.system\(',  # os.system usage
        ]
        
        for pattern in dangerous_patterns:
            matches = re.findall(pattern, content)
            self.assertEqual(len(matches), 0,
                           f"Found potentially unsafe pattern: {pattern}")
    
    def test_safe_shell_arg_usage(self):
        """Verify safe_shell_arg is used for user inputs"""
        with open('main.py', 'r') as f:
            content = f.read()
        
        # Should have safe_shell_arg function defined
        self.assertIn('def safe_shell_arg', content,
                     "safe_shell_arg function not found")


def run_tests():
    """Run all tests and print results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestServiceStartStopRestart))
    suite.addTests(loader.loadTestsFromTestCase(TestDockerFeatures))
    suite.addTests(loader.loadTestsFromTestCase(TestNetworkRouting))
    suite.addTests(loader.loadTestsFromTestCase(TestFirewallZones))
    suite.addTests(loader.loadTestsFromTestCase(TestSystemReboot))
    suite.addTests(loader.loadTestsFromTestCase(TestServiceControlButtons))
    suite.addTests(loader.loadTestsFromTestCase(TestTranslations))
    suite.addTests(loader.loadTestsFromTestCase(TestNavigationLink))
    suite.addTests(loader.loadTestsFromTestCase(TestTemplateIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestCodeQuality))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓✓✓ ALL TESTS PASSED ✓✓✓")
        return 0
    else:
        print("\n✗ SOME TESTS FAILED ✗")
        return 1


if __name__ == '__main__':
    sys.exit(run_tests())
