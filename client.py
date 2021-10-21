import socket

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECTED'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

new_msg = ''

run = True
while run:
    print("waiting for msg: :)")
    new_msg = input("MSg: ")
    if new_msg == 'disconnect':
        break
    if new_msg != '':
        send(new_msg)
    else:
        print("Msg can't be empty")
    


send(DISCONNECT_MSG)
