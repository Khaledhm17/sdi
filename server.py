import socket

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow quick restart of the server
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on port {PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode("utf-8")
        print(f"Received: {message}")

        # Process the client's request
        response = f"Server received: {message}"
        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    print(f"Client disconnected: {client_address}")
