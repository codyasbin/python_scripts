import socket

# Example: Get your computer's hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Example: Get IP address
ip_address = socket.gethostbyname(hostname)
print(f"IP Address: {ip_address}")