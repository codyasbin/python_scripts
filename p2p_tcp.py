import socket



# Example: Get your computer's hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Example: Get IP address
ip_address = socket.gethostbyname(hostname)
print(f"IP Address: {ip_address}")

port =5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)