from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///films1.sql"

engine = create_engine(sqlite_database)

class Base (DeclarativeBase): pass

class Films(Base):

    __tablename__ = "film"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Integer)
    genre = Column(String)
    rate = Column(Integer)

Base.metadata.create_all(bind=engine)

def create(f_name, f_date, f_genre, f_rate):
    with Session(autoflush=False, bind=engine) as db:
        #создаем объект Person для добавления в бд
        film = Films(name=f_name, date=f_date, genre = f_genre, rate = f_rate)
        db.add(film) # добавляем в бд
        db.commit() # сохраняем изменения или db.refresh()

def info_by_name(name_film):
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).filter(Films.name == name_film).all()
        for i in films:
            print(i.name)

def info():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).all()
        for i in films:
            print(i.name)


def change_by_id(id_ch, name, date, genre, rate):
    with Session(autoflush=False, bind=engine) as db: # получаем один объект, у которого id=1
        film = db.query(Films).filter(Films.id==id_ch).first()
        if (film != None):
            # print(f"{film.id}.{film.name} ({film.date}), {film.genre}, {film.rate}")
            film.name = name
            film.date = date
            film.genre = genre
            film.rate = rate
            db.commit()

def delete(id_del):
    with Session(autoflush=False, bind=engine) as db:
        dele = db.query(Films).filter(Films.id==id_del).first()
        db.delete(dele) # удаляем обьект
        db.commit() # сохраняем изменения

create("Джон уик", 2014, 'Боевик', 9)
create("Джон Уик 2", 2017, 'Боевик', 8)
create("Джон Уик 3", 2019, 'Боевик', 7)
info()
change_by_id(3, "Джон Уик 4", 2023, 'Боевик', 10)
info()
delete(3)
info()