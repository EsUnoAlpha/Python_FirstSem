import socket
from threading import Thread
from database_users import sigh_in, sigh_up

client_sockets = set()

# Получаем локальный IP-адрес сервера
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Локальный IP: {local_ip}")

# Создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.82.104.206', 55005))
sock.listen(10)


def recieve(cs, address):
    # Функция для получения сообщений от клиента
    while True:
        try:
            message = cs.recv(1024).decode()
        except:
            # Если возникла ошибка при получении сообщения, удаляем сокет клиента
            client_sockets.remove(cs)
        else:
            # Отправляем полученное сообщение всем клиентам, кроме отправителя
            for i in client_sockets:
                i.send(bytes(f"{address}: {message}".encode()))


def connection(conn, address):
    # Функция для обработки соединения с клиентом
    while True:
        check = conn.recv(1024).decode()
        if check == "1":
            # Если пользователь хочет войти в аккаунт, получаем от него логин и пароль
            login = conn.recv(1024).decode()
            password = conn.recv(1024).decode()
            # Вызываем функцию sigh_in для проверки данных пользователя
            if name := sigh_in(login, password):
                # Если данные верны, отправляем клиенту сообщение об успешной авторизации
                response = f"Пользователь {name} авторизован"
                conn.send(response.encode())
                # Добавляем сокет клиента в множество
                user_name = name
                client_sockets.add(conn)
                break
            else:
                # Если данные неверны, отправляем клиенту сообщение об ошибке
                conn.send("Неверный логин или пароль".encode())

        if check == "2":
            # Если пользователь хочет зарегистрироваться, получаем от него логин, пароль и имя
            login = conn.recv(1024).decode()
            password = conn.recv(1024).decode()
            name = conn.recv(1024).decode()
            # Вызываем функцию sigh_up из модуля database для добавления нового пользователя в базу данных
            if name := sigh_up(login, password, name):
                # Если регистрация прошла успешно, отправляем клиенту сообщение об успешной регистрации
                response = f"Пользователь {name} зарегестрировался"
                conn.send(response.encode())
                print(response)
            else:
                conn.send("Имя пользователя занято".encode())
    recieve(conn, user_name)


print("Пошла жара")


def main(conn):
    # Функция для отправки пользователю списка доступных действий
    msg = ('1 - Вход, 2 - регистрация')
    conn.send(msg.encode())


# Функция для обработки входящих соединений от клиентов
def accept_client(server_sock):
    while True:
        # Принимаем входящее соединение
        client_conn, client_address = server_sock.accept()
        print(f"Connected from {client_address}")

        # Вызываем функцию main()
        main(client_conn)

        # Запускаем новый поток для обработки соединения с клиентом
        Thread(target=connection, args=(client_conn, client_address), daemon=True).start()


# Запускаем прослушивание входящих соединений в отдельном потоке
while True:
    th2 = Thread(target=accept_client, args=(sock,), daemon=True)
    th2.start()
