"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.33.142.84', 55000))
sock.listen(1)
print('server is running')
while True:
    conn, addr = sock.accept()
    print('connected: ', addr)
    data = conn.recv(1024)
    print(str(data))
    if data == 'Bye':
        conn.close()
    else:
        snd = input('Введите сообщение: ')
        conn.send(snd.encode())
