"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


sqlite_database = "sqlite:///metanit2.db"
engine = create_engine(sqlite_database)

class Base(DeclarativeBase): pass
class Readers(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship("Books", back_populates="readers")

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    bookname = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey("readers.id"))
    readers = relationship("Readers", back_populates="books")


with Session(autoflush=False, bind=engine) as db:
    alpha = Readers(name = 'Alpha')
    beta = Readers(name = 'Beta')

    book1 = Books(bookname = 'Пикник на обочние', author = 'Аркадий и Борис Стругацкие')
    book2 = Books(bookname = 'Мастер и Маргарита', author = 'Михаил Булгаков')
    



