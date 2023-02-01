from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from config.db import engine
# from config.db import Base

Base = declarative_base()

class Task(Base):
    """Cada classe representa uma tabela do banco"""
    # Nome da tabela, se a variável não for
    # declarada será utilizado o nome da classe.
    __tablename__ = 'Task'

    # Colunas da tabela.
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    complete = Column('complete', Boolean)

    def __init__(self, name, complete=False):
        self.name = name
        self.complete = complete

Base.metadata.create_all(engine)