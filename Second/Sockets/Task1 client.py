import socket


def func():
    data = ''
    msg = input('Введите сообщение: ')
    sock.send(msg, encoding = 'UTF-8')
    data = sock.recv(1024)
    print(data)
    if data == 'bye':
        sock.close()
    else:
        func()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.33.142.84', 55000))
data = ""
msg = input('Введите сообщение: ')
while True:
    sock.send(bytes(msg, encoding = 'UTF-8'))
    data = sock.recv(1024)
    print(data)
    if data == 'Bye':
        sock.close()
    else:
        msg = input('Введите сообщение: ')
        sock.send(bytes(msg, encoding = 'UTF-8'))