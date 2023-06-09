"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///it_company.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase):
    pass


class Workers(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(Integer)
    position_id = Column(Integer, ForeignKey("positions.id"))
    position = relationship("Positions", back_populates="employees")


class Positions(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    employees = relationship("Workers", back_populates="position")


Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    admin = Positions(name='ИБшник',
                      employees=[Workers(name='Игнат', experience=3), Workers(name='Виталик', experience=5)])
    developer = Positions(name='Сисадмин',
                          employees=[Workers(name='Саша', experience=2), Workers(name='Катя', experience=7)])
    db.add_all([admin, developer])
    db.commit()


def show_positions(worker_name):
    with Session(bind=engine) as db:
        worker = db.query(Workers).filter_by(name=worker_name).first()
        if worker is None:
            print(f'Работник {worker_name} не найден')
        else:
            positions = [worker.position.name]
            print(f'Должности работника {worker_name}: {positions}')


def show_employees_by_position(position_name):
    with Session(bind=engine) as db:
        position = db.query(Positions).filter_by(name=position_name).first()
        if position is None:
            print(f'Должность {position_name} не найдена')
        else:
            employees = [e.name for e in position.employees]
            print(f'Работники на должности {position_name}: {employees}')


def show_employees_by_position_and_experience(position_name):
    with Session(bind=engine) as db:
        employees = db.query(Workers).join(Positions).filter(
            Positions.name == position_name,
            Workers.experience > 5
        ).all()
        if not employees:
            print(f'Работники с должностью {position_name} и стажем больше 5 лет не найдены')
        else:
            print(f'Работники на должности {position_name} со стажем более 5 лет:')
            for employee in employees:
                print(f'- {employee.name}')


show_positions('Катя')
show_employees_by_position('ИБшник')
show_employees_by_position_and_experience('Сисадмин')
