import socket
import threading
import os
import json

SERVER = ("127.0.0.1", 5000)
PORT = int(input("Enter peer port: "))
FOLDER = "shared_files"

os.makedirs(FOLDER, exist_ok=True)

def register():
    data = {
        "command": "REGISTER",
        "ip": "127.0.0.1",
        "port": PORT,
        "files": os.listdir(FOLDER)
    }

    s = socket.socket()
    s.connect(SERVER)
    s.send(json.dumps(data).encode())
    print(s.recv(1024).decode())
    s.close()

def listen():
    s = socket.socket()
    s.bind(("127.0.0.1", PORT))
    s.listen()
    print("Peer is listening...")

    while True:
        conn, addr = s.accept()
        filename = conn.recv(1024).decode()
        path = os.path.join(FOLDER, os.path.basename(filename))

        if os.path.isfile(path):
            conn.sendall(b"FOUND")
        else:
            conn.sendall(b"NOT FOUND")

        conn.close()

def search():
    name = input("Enter filename: ")
    data = {"command": "SEARCH", "filename": name}

    s = socket.socket()
    s.connect(SERVER)
    s.send(json.dumps(data).encode())
    print(s.recv(1024).decode())
    s.close()

threading.Thread(target=listen, daemon=True).start()
register()

while True:
    choice = input("1- Search  2- Exit: ")

    if choice == "1":
        search()
    elif choice == "2":
        break
