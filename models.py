from sqlalchemy import create_engine, Column, Integer, String , ForeignKey,Boolean
from sqlalchemy.orm import Session,sessionmaker , relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base


# Define Question class inheriting from Base
class Question(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))



# Define Response class inheriting from Base
class Response(Base):
    __tablename__ = 'Responses'
    id = Column(Integer, primary_key=True)
    response_text = Column(String(50))
    is_correct = Column(Boolean)
    question_id = Column(Integer,ForeignKey("Questions.id"))





