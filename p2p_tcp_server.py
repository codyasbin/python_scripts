import socket



# Example: Get your computer's hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# Example: Get IP address
ip_address = "192.168.1.70"
print(f"IP Address: {ip_address}")

port =5000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((ip_address, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Listening on {ip_address}:{port}...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")

# Receive data from the client
# 5. Receive data loop
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Client:", data.decode())

client_socket.close()    