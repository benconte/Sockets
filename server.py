import socket
import threading

HEADER = 1024
HOST = '172.17.0.4'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECTED'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_len = int(msg_length)
            msg = conn.recv(msg_len).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                print(f"[USER] - {addr} disconnected")
                connected = False
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

            print(f"[{addr}] {msg}")
            conn.send("MSG received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
