from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
# строка подключения
sqlite_database = "sqlite:///persons.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)
# СОЗДaeм базовый класс для моделей
class Base (DeclarativeBase): pass
# Создаем модель, объекты которой будут храниться в бд
class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)
    # создаем таблицы
Base.metadata.create_all(bind=engine)