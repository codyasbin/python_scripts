import socket

SERVER_IP = "192.168.1.20"
PORT = 5000

# 1. Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to server
client_socket.connect((SERVER_IP, PORT))
print("Connected to server")

# 3. Send messages
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client_socket.send(msg.encode())

client_socket.close()
