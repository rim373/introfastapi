from sqlalchemy import create_engine, Column, Integer, String
from .database import Base

# Define To Do class inheriting from Base
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))

