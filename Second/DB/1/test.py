from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

sqlite_database = "sqlite:///authorization1.sql"

engine = create_engine(sqlite_database)

class Base (DeclarativeBase): pass

class Authorization(Base):

    __tablename__ = "authorizations"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


Base.metadata.create_all(bind=engine)


def start():
    start_auth = input('1 - Войти, 2 - Зарегестрироваться\n')
    if '2' in start_auth:
        create()
    elif '1' in start_auth:
        login()


def create():
    name = input('Введите имя пользрвателя: ')
    passwd = input('Введите пароль: ')
    hashed_pass = generate_password_hash(f"{passwd}", 'sha256')
    with Session(autoflush=False, bind=engine) as db:
        auth = Authorization(username=name, password=hashed_pass)
        db.add(auth)
        db.commit()
    start()


def login():
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(Authorization).all()
        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        list_of_users = list()
        for i in users:
            list_of_users.append(i.username)
            unhashed = check_password_hash(f"{i.password}", f"{passwd}")
            if login in list_of_users and unhashed == True:
                print("Вход выполнен")
            else:
                print(list_of_users)
                if login != i.username:
                    print("Нет такого пользователя")
                else:
                    print("Неправильный пароль")


def info():
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(Authorization).all()
        for i in users:
            print(i.username, i.password)



start()
info()