import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.56.1"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE= "!DISCONNECT"
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


userNickname = input("Enter your nickname = ")
print(f"Welcome {userNickname}")

while True:
    a = input("Type your message, if you want to quit press to q = \n")

    if (a == "q"):
        print("See you soon...")
        break
    else:
        send(a)