"""
Network Details and WiFi Password Viewer
Shows all saved WiFi networks with their passwords and current network details
"""

import subprocess
import re
import socket
import platform
import os

# Enable ANSI colors on Windows
os.system("")


class Colors:
    """ANSI color codes for terminal output"""
    # Text colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    # Reset
    RESET = "\033[0m"
    
    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"


def print_header(text):
    """Print a styled header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}{text.center(60)}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")


def print_subheader(text):
    """Print a styled subheader"""
    print(f"{Colors.MAGENTA}{'-' * 60}{Colors.RESET}")


def print_label(label, value, label_color=Colors.GREEN, value_color=Colors.WHITE):
    """Print a styled label-value pair"""
    print(f"{label_color}{label}: {Colors.RESET}{value_color}{value}{Colors.RESET}")


def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")


def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ {text}{Colors.RESET}")


def get_system_info():
    """Get basic system network information"""
    print_header("SYSTEM NETWORK INFORMATION")
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print_label("Hostname", hostname, Colors.CYAN)
        print_label("Local IP Address", local_ip, Colors.CYAN)
        print_label("Platform", f"{platform.system()} {platform.release()}", Colors.CYAN)
    except Exception as e:
        print_error(f"Error getting system info: {e}")
    print()


def get_current_network():
    """Get currently connected network details"""
    print_header("CURRENT NETWORK CONNECTION")
    
    try:
        # Get current connection info
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        if result.returncode == 0:
            output = result.stdout
            
            # Extract current SSID first
            current_ssid = None
            ssid_match = re.search(r"^\s*SSID\s*:\s*(.+)$", output, re.MULTILINE)
            if ssid_match:
                current_ssid = ssid_match.group(1).strip()
            
            # Parse important fields
            fields = ["State", "SSID", "BSSID", "Network type", "Radio type", 
                     "Authentication", "Cipher", "Channel", "Receive rate", 
                     "Transmit rate", "Signal"]
            
            for line in output.split('\n'):
                for field in fields:
                    if field in line and ":" in line:
                        parts = line.strip().split(":", 1)
                        if len(parts) == 2:
                            label = parts[0].strip()
                            value = parts[1].strip()
                            # Highlight signal strength
                            if "Signal" in label:
                                signal_val = int(value.replace("%", "")) if "%" in value else 0
                                if signal_val >= 70:
                                    print_label(label, value, Colors.GREEN, Colors.GREEN)
                                elif signal_val >= 40:
                                    print_label(label, value, Colors.YELLOW, Colors.YELLOW)
                                else:
                                    print_label(label, value, Colors.RED, Colors.RED)
                            elif "SSID" in label and "BSSID" not in label:
                                print_label(label, value, Colors.MAGENTA, Colors.BOLD + Colors.WHITE)
                            else:
                                print_label(label, value, Colors.BLUE)
                        break
            
            # Get password for currently connected network
            if current_ssid:
                password_result = subprocess.run(
                    ["netsh", "wlan", "show", "profile", current_ssid, "key=clear"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                
                if password_result.returncode == 0:
                    password_match = re.search(r"Key Content\s*:\s*(.*)", password_result.stdout)
                    password = password_match.group(1).strip() if password_match else "No password / Open network"
                    print_label("Password", password, Colors.GREEN, Colors.BOLD + Colors.YELLOW)
                else:
                    print_warning("Could not retrieve password for current network")
        else:
            print_warning("No wireless interface found or not connected")
    except Exception as e:
        print_error(f"Error getting current network: {e}")
    print()


def get_saved_wifi_passwords():
    """Get all saved WiFi networks and their passwords"""
    print_header("SAVED WIFI NETWORKS WITH PASSWORDS")
    
    try:
        # Get list of all saved WiFi profiles
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        if result.returncode != 0:
            print_error("Could not retrieve WiFi profiles")
            return
        
        # Extract profile names
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)
        
        if not profiles:
            print_warning("No saved WiFi networks found")
            return
        
        print_info(f"Found {Colors.BOLD}{len(profiles)}{Colors.RESET}{Colors.CYAN} saved network(s):")
        print()
        
        for i, profile in enumerate(profiles, 1):
            profile = profile.strip()
            
            # Get password for each profile
            try:
                password_result = subprocess.run(
                    ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                
                if password_result.returncode == 0:
                    output = password_result.stdout
                    
                    # Extract password
                    password_match = re.search(r"Key Content\s*:\s*(.*)", output)
                    password = password_match.group(1).strip() if password_match else "No password / Open network"
                    
                    # Extract security type
                    security_match = re.search(r"Authentication\s*:\s*(.*)", output)
                    security = security_match.group(1).strip() if security_match else "Unknown"
                    
                    # Extract connection mode
                    connection_match = re.search(r"Connection mode\s*:\s*(.*)", output)
                    connection_mode = connection_match.group(1).strip() if connection_match else "Unknown"
                    
                    print(f"{Colors.BOLD}{Colors.WHITE}[{i}]{Colors.RESET} {Colors.BOLD}{Colors.CYAN}{profile}{Colors.RESET}")
                    print_label("    Security Type", security, Colors.BLUE)
                    print_label("    Password", password, Colors.GREEN, Colors.BOLD + Colors.YELLOW)
                    print_label("    Connection Mode", connection_mode, Colors.BLUE)
                    print_subheader("")
                    
            except Exception as e:
                print_error(f"Error getting password for '{profile}': {e}")
                print_subheader("")
                
    except Exception as e:
        print_error(f"Error retrieving WiFi profiles: {e}")


def get_network_adapters():
    """Get network adapter information"""
    print_header("NETWORK ADAPTERS")
    
    try:
        result = subprocess.run(
            ["ipconfig", "/all"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        if result.returncode == 0:
            # Print relevant sections
            lines = result.stdout.split('\n')
            for line in lines:
                line = line.rstrip()
                if not line:
                    continue
                    
                # Color code different types of information
                if "adapter" in line.lower():
                    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{line}{Colors.RESET}")
                elif "Description" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.BLUE)
                elif "Physical Address" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.CYAN)
                elif "IPv4" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.GREEN, Colors.BOLD + Colors.GREEN)
                elif "IPv6" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.GREEN)
                elif "Default Gateway" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.YELLOW, Colors.BOLD + Colors.YELLOW)
                elif any(keyword in line for keyword in ["DHCP", "DNS Servers", "Subnet Mask"]):
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        print_label(parts[0].strip(), parts[1].strip(), Colors.BLUE)
    except Exception as e:
        print_error(f"Error getting adapter info: {e}")


def main():
    print(f"\n{Colors.BOLD}{Colors.BG_BLUE}{Colors.WHITE}")
    print("=" * 60)
    print("      🌐 NETWORK DETAILS & WIFI PASSWORD VIEWER 🔐      ")
    print("=" * 60)
    print(f"{Colors.RESET}\n")
    
    # Check if running on Windows
    if platform.system() != "Windows":
        print_error("This script is designed for Windows OS only.")
        return
    
    get_system_info()
    get_current_network()
    get_saved_wifi_passwords()
    get_network_adapters()
    
    print(f"\n{Colors.BOLD}{Colors.BG_GREEN}{Colors.WHITE}")
    print("=" * 60)
    print("              ✅ SCAN COMPLETE ✅                       ")
    print("=" * 60)
    print(f"{Colors.RESET}\n")


if __name__ == "__main__":
    main()
