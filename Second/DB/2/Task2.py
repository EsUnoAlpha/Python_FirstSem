from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table(
    'association_table',
    Base.metadata,
    Column('worker_id', Integer, ForeignKey('workers.id')),
    Column('position_id', Integer, ForeignKey('positions.id'))
)

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    positions = relationship("Position", secondary=association_table, back_populates="workers")

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    workers = relationship("Worker", secondary=association_table, back_populates="positions")

engine = create_engine('sqlite:///company.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

positions = [
    Position(name="Сисадмин"),
    Position(name="ИБшник")
]
session.add_all(positions)
session.commit()

workers = [
    Worker(name="Катя", experience=3, positions=[positions[0]]),
    Worker(name="Саша", experience=7, positions=[positions[1]])
]
session.add_all(workers)
session.commit()

def worker_positions(worker_name):
    worker = session.query(Worker).filter_by(name=worker_name).first()
    if worker:
        positions = worker.positions
        if positions:
            print(f"Должности работника {worker_name}:")
            for position in positions:
                print(position.name)
        else:
            print("У работника нет должностей.")
    else:
        print("Работник не найден.")

def worker_by_position(position_name):
    position = session.query(Position).filter_by(name=position_name).first()
    if position:
        workers = position.workers
        if workers:
            print(f"Работники с должностью {position_name}:")
            for worker in workers:
                print(worker.name)
        else:
            print("Нет таких работников.")
    else:
        print("Нет такой должности.")

def workerby_position_and_experience(position_name):
    workers = session.query(Worker).join(association_table).join(Position).filter(Position.name == position_name, Worker.experience > 5).all()
    if workers:
        print(f"Работники на должности {position_name} со стажем больше 5:")
        for worker in workers:
            print(f"Имя: {worker.name}, Стаж: {worker.experience}")
    else:
        print(f"На должности нет работников со стажем больше 5.")

worker_positions('Катя')
worker_by_position('Сисадмин')
workerby_position_and_experience('ИБшник')