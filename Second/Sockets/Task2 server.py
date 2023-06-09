"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9023))
sock.listen(5)
conn, addr = sock.accept()
print(f"Connected: {addr}")
while True:
    requests = input("Введите название файла: ")
    if requests == "off":
        break
    else:
        conn.send(bytes(requests, encoding="UTF-8"))
        data = conn.recv(1024).decode()
        if data != "error":
            response = len(data.split())
            conn.send(bytes(f"Файл содержит: {response} слов", encoding="UTF-8"))
        else:
            print("Такого фала не существует")
conn.close()