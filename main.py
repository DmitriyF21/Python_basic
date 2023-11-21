from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

Db_url = 'sqlite:///./sql_apps.db'

engine = create_engine(Db_url,connect_args={"check_same_thread": False})

Base = declarative_base()

class Person(Base):
    __tablename__ = "People"
    id = Column(Integer,primary_key=True, index=True)
    name = Column (String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI()
