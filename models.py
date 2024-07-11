from sqlalchemy import create_engine, Column, Integer, String , ForeignKey
from sqlalchemy.orm import Session,sessionmaker , relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base


# Define Question class inheriting from Base
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))
    response = Column(String)


