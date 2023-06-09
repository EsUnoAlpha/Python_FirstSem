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
    # создаем двух читателей и добавляем книги для каждого из них
    alpha = Readers(name='Alpha',
                    books=[Books(bookname='Книга 1', author='Автор 1'), Books(bookname='Книга 2', author='Автор 2')])
    beta = Readers(name='Beta',
                   books=[Books(bookname='Книга 3', author='Автор 3'), Books(bookname='Книга 4', author='Автор 4')])
    db.add_all([alpha, beta])
    db.commit()


# функция вывода всех книг для вводимого с клавиатуры читателя
def show_books():
    with Session(bind=engine) as db:
        reader_name = input('Введите имя читателя: ')
        reader = db.query(Readers).filter_by(name=reader_name).first()
        if reader is None:
            print(f'Читатель {reader_name} не найден')
        else:
            print(f'Книги читателя {reader.name}:')
            for book in reader.books:
                print(f'- {book.bookname} ({book.author})')


# вызывается функция для вывода всех книг для читателя "Alpha"
show_books()
