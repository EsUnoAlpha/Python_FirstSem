import socket
import threading

from database_manager import DatabaseManager


class ChatServer:
    # Класс для запуска сервера чата.
    # Атрибуты: db_manager (DatabaseManager): менеджер базы данных пользователей.
    # clients (list): список клиентских сокетов.
    def __init__(self):
        # Создает объект ChatServer.
        self.db_manager = DatabaseManager('users.db')
        self.clients = []

    def broadcast(self, message):
        # Рассылает сообщение всем клиентам.
        # Аргументы: message (str): сообщение для рассылки.
        for client in self.clients:
            client.sendall(message.encode())

    def handle_client(self, client, addr):
        # Обрабатывает сообщения от клиента.
        # Аргументы: client (socket.socket): клиентский сокет.
        # addr (tuple): адрес клиента.

        # Обработчик сообщений от клиента. Разбирает сообщения на действия "register" или "login".
        # При успешной регистрации или входе в чат рассылает сообщения о событии всем клиентам.
        username = None
        while True:
            try:
                msg = client.recv(1024).decode()
                if not username:
                    action, user, passw = msg.split("|")
                    if action == "register":
                        success = self.db_manager.register_user(user, passw)
                        if success:
                            client.sendall("register_success".encode())
                        else:
                            client.sendall("register_fail".encode())
                    elif action == "login":
                        success = self.db_manager.authorize_user(user, passw)
                        if success:
                            client.sendall("login_success".encode())
                            username = user
                            self.broadcast(f"{username} has joined the chat.")
                        else:
                            client.sendall("login_fail".encode())
                else:
                    self.broadcast(f"{username}: {msg}")
            except Exception as e:
                print(f"Error: {e}")
                if client in self.clients:
                    self.clients.remove(client)
                if username:
                    self.broadcast(f"{username} has left the chat.")
                client.close()
                break

    def start_server(self):
        # Запускает сервер чата.Создает и прослушивает сокет.
        # Для каждого подключения запускает новый поток обработки клиента.
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('10.82.56.16', 12345))
        server.listen(5)
        print("Server started.")
        while True:
            client, addr = server.accept()
            print(f"Client {addr} connected.")
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    # Точка входа в приложение.Создает объект ChatServer и запускает сервер чата.
    chat_server = ChatServer()
    chat_server.start_server()

