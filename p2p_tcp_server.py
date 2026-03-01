import socket
import threading

HOST = "10.190.172.210"
PORT = 5000

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("\nClient disconnected")
                break
            print(f"\nClient: {data.decode()}\nYou: ", end="")
        except:
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {PORT}...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Start receive thread
threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

# Send loop
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    conn.send(msg.encode())

conn.close()
server_socket.close()
