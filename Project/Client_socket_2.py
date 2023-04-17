import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = ""
sock.connect(("192.168.56.1", 55000))


def get_message():
    while True:
        messages = sock.recv(1024).decode()
        print(messages)


message = sock.recv(1024).decode()
while True:
    print(message)
    messages = input("Введите сообщение: ")
    sock.send(messages.encode())
    if messages == "1":
        login = input("Введите логин: ")
        sock.send(login.encode())
        password = input("Введите пароль: ")
        sock.send(password.encode())
        response = sock.recv(1024).decode()
        if "авторизован" in response:
            print(response)
            break
        print(response)
    if messages == "2":
        login = input("Введите логин: ")
        sock.send(login.encode())
        password = input("Введите пароль: ")
        sock.send(password.encode())
        name = input("Введите имя: ")
        sock.send(name.encode())
        response = sock.recv(1024).decode()
        print(response)
        continue

th = Thread(target=get_message, daemon=True)
th.start()

while True:
    messages = input("message:")
    data = datetime.now().strftime("%Y-%m-%d %H:%M")
    to_sent = f"{data} \n {messages}"
    sock.send(to_sent.encode())
