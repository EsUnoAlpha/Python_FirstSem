from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

# убрал ошибку в названии базы данных и добавил параметр check_same_thread для подключения к SQLite в многопоточном приложении
sqlite_database = "sqlite:///authorization.db?check_same_thread=False"

engine = create_engine(sqlite_database)

# исправил ошибку в создании базового класса
Base = declarative_base()


class Authorization(Base):
    __tablename__ = "authorizations"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind=engine)

# изменен вызов sessionmaker на функцию, чтобы передать параметр autoflush
Session = sessionmaker(bind=engine, autoflush=False)


def start():
    start_auth = input('1 - Войти, 2 - Зарегестрироваться\n')
    if '2' in start_auth:
        sigh_up()
    elif '1' in start_auth:
        sigh_in()


def sigh_up():
    name = input('Введите имя пользователя: ')
    passwd = input('Введите пароль: ')
    hashed_pass = generate_password_hash(f"{passwd}", 'sha256')
    with Session() as db:
        auth = Authorization(username=name, password=hashed_pass)
        db.add(auth)
        db.commit()
    start()


def sigh_in():
    with Session() as db:
        users = db.query(Authorization).all()
        list_of_users = list()
        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        for i in users:
            list_of_users.append(i.username)  # добавил имя пользователя в список пользователей
            unhashed = check_password_hash(f"{i.password}", f"{passwd}")
            if login == i.username and unhashed is True:  # исправил проверку имени пользователя и пароля
                print("Вход выполнен")
                return
        if login not in list_of_users:
            print("Нет такого пользователя")
        else:
            print("Неправильный пароль")


def info():
    with Session() as db:
        users = db.query(Authorization).all()
        for i in users:
            print(i.username, i.password)


start()
info()