import socket
import threading

SERVER_IP = "192.168.1.20"  # change to server IP
PORT = 5000

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\nServer disconnected")
                break
            print(f"\nServer: {data.decode()}\nYou: ", end="")
        except:
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
print("Connected to server")

# Start receive thread
threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

# Send loop
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client_socket.send(msg.encode())

client_socket.close()
