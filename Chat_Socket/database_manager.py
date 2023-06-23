import sqlite3


class DatabaseManager:
    #m Класс для работы с базой данных пользователей.
    # Атрибуты: db_name (str): имя базы данных.
    def __init__(self, db_name):
        # Создает объект DatabaseManager с указанным именем базы данных.
        # Аргументы: db_name (str): имя базы данных.
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        # Инициализирует базу данных, создавая таблицу для хранения пользователей.
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (username TEXT PRIMARY KEY, password TEXT)''')
            conn.commit()

    def register_user(self, username, password):
        # Регистрирует нового пользователя в базе данных.
        # Аргументы: username (str): имя пользователя.
        # password (str): пароль пользователя.
        # Возвращает: bool: True, если регистрация прошла успешно, иначе - False.
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
                conn.commit()
                print(f"User {username} registered successfully.")

                return True
            except sqlite3.IntegrityError:
                print(f"User {username} registration failed.")

                return False

    def authorize_user(self, username, password):
        # Авторизует пользователя в базе данных.
        # Аргументы: username (str): имя пользователя.
        # password (str): пароль пользователя.
        # Возвращает: bool: True, если пользователь авторизован, иначе - False.
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            if user is not None:
                print(f"User {username} authorized successfully.")
            else:
                print(f"User {username} authorization failed.")

            return user is not None

    def get_all_users(self):
        # Возвращает список имен всех пользователей из базы данных.
        # Возвращает: List[str]: список имен всех пользователей из базы данных.
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users")
            users = cursor.fetchall()
            return [user[0] for user in users]
