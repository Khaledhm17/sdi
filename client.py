import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 7000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

print("Connected to server.")

while True:
    message = input("Enter message (or 'quit' to exit): ")
    if message.lower() == "quit":
        break

    # Send message to server
    client_socket.send(message.encode("utf-8"))

    # Receive response
    response = client_socket.recv(1024)
    print("Server:", response.decode("utf-8"))

client_socket.close()

print("Disconnected from server.")
