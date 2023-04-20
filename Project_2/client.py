import socket
import threading
import tkinter as tk
from tkinter import messagebox

from database_manager import DatabaseManager


class ChatClient:
    # Класс для запуска клиента чата.
    # Атрибуты: db_manager (DatabaseManager): менеджер базы данных пользователей.
    # client_socket (socket.socket): клиентский сокет.
    def __init__(self):
        #Создает объект ChatClient.
        self.db_manager = DatabaseManager('users.db')
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('10.82.56.16', 12345))

    def receive_messages(self):
        # Получает сообщения от сервера и добавляет их в виджет чата.
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                self.chat_text.config(state=tk.NORMAL)
                self.chat_text.insert(tk.END, msg + "\n")
                self.chat_text.config(state=tk.DISABLED)
            except Exception as e:
                print(f"Error: {e}")
                break

    def send_message(self, event=None):
        # Отправляет сообщение на сервер.
        msg = self.message_entry.get()
        if msg:
            self.message_entry.delete(0, tk.END)
            self.client_socket.sendall(msg.encode())

    def register(self):
        # Регистрирует нового пользователя.
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.client_socket.sendall(f"register|{username}|{password}".encode())
        response = self.client_socket.recv(1024).decode()
        if response == "register_success":
            messagebox.showinfo("Registration", "Registration successful!")
        else:
            messagebox.showerror("Registration", "Registration failed. Username already exists.")

    def login(self):
        # Входит в чат существующим пользователем.
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.client_socket.sendall(f"login|{username}|{password}".encode())
        response = self.client_socket.recv(1024).decode()
        if response == "login_success":
            self.open_chat_window(username)
        else:
            messagebox.showerror("Login", "Invalid username or password.")

    def open_login_window(self):
        #Открывает окно входа в чат.
        self.login_window = tk.Tk()
        self.login_window.title("Chat Login")

        tk.Label(self.login_window, text="Username:").grid(row=0, column=0)
        self.entry_username = tk.Entry(self.login_window)
        self.entry_username.grid(row=0, column=1)

        tk.Label(self.login_window, text="Password:").grid(row=1, column=0)
        self.entry_password = tk.Entry(self.login_window, show="*")
        self.entry_password.grid(row=1, column=1)

        tk.Button(self.login_window, text="Login", command=self.login).grid(row=2, column=0, pady=10)
        tk.Button(self.login_window, text="Register", command=self.register).grid(row=2, column=1)

        self.login_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.login_window.mainloop()

    def open_chat_window(self, username):
        # Открывает окно чата.
        # Аргументы: username (str): имя пользователя.
        self.login_window.destroy()
        self.chat_window = tk.Tk()
        self.chat_window.title(f"Chat - {username}")

        scrollbar = tk.Scrollbar(self.chat_window)
        scrollbar.grid(row=0, column=1, sticky=tk.NSEW)

        self.chat_text = tk.Text(self.chat_window, wrap=tk.WORD, yscrollcommand=scrollbar.set, state=tk.DISABLED)
        self.chat_text.grid(row=0, column=0, sticky=tk.NSEW)

        scrollbar.config(command=self.chat_text.yview)

        self.message_entry = tk.Entry(self.chat_window)
        self.message_entry.grid(row=1, column=0, sticky=tk.EW)
        self.message_entry.bind("<Return>", self.send_message)

        send_button = tk.Button(self.chat_window, text="Send", command=self.send_message)
        send_button.grid(row=1, column=1)

        self.chat_window.columnconfigure(0, weight=1)
        self.chat_window.rowconfigure(0, weight=1)

        threading.Thread(target=self.receive_messages, daemon=True).start()

        self.chat_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.chat_window.mainloop()

    def on_closing(self):
        # Обрабатывает закрытие окна.
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            if hasattr(self, 'chat_window'):
                self.chat_window.destroy()
            if hasattr(self, 'login_window'):
                self.login_window.destroy()
            self.client_socket.close()


if __name__ == "__main__":
    chat_client = ChatClient()
    chat_client.open_login_window()

