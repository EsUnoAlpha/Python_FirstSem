from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from werkzeug.security import generate_password_hash, check_password_hash



sql_database = "sqlite:///users.db"
engine = create_engine(sql_database)


# Определяем базовый класс моделей ORM для декларативной базы данных
class Base(DeclarativeBase):
    pass


# Создаем таблицу базы данных ORM и модель данных для таблицы
class Authorization(Base):
    __tablename__ = "base_people"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    password = Column(String)
    name = Column(String)


# Создаем таблицы в базе данных, если их еще нет
Base.metadata.create_all(bind=engine)
# Создаем сессию ORM для выполнения операций в базе данных
db = Session(autoflush=False, bind=engine)


# Инициализируем базу данных начальными данными
def init():
    # Создаем объекты модели данных для начальных записей
    user_1 = Authorization(user_name="Саша", password=generate_password_hash("erfhiod", "sha256"), name="Alpha")
    user_2 = Authorization(user_name="Ваня", password=generate_password_hash("hgjdfjjsdksd", "sha256"), name="Beta")
    list_1 = [user_1, user_2]
    # Добавляем объекты в сессию ORM и фиксируем изменения в базе данных
    db.add_all(list_1)
    db.commit()






def sigh_up(login, password, name):
    # Если имя пользователя не занято, создаем нового пользователя в базе данных
    password_hash = generate_password_hash(password, "sha256")
    new_user = Authorization(user_name=login, password=password_hash, name=name)
    db.add(new_user)
    db.commit()
    return name


# Функция для авторизации пользователя
def sigh_in(login, password):
    try:
        user = db.query(Authorization).filter(Authorization.user_name == login).first()
        if check_password_hash(user.password, password):
            print(f"Пользователь {user.name} Успешно авторизовался")
            return user.name
        else:
            print("Неверный пароль")
    except:
        print("Неверный логин")



if __name__ == "__main__":
    init()
