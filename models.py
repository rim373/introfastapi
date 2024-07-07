from sqlalchemy import create_engine, Column, Integer, String , ForeignKey
from sqlalchemy.orm import Session,sessionmaker , relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base

# Define Question class inheriting from Base
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))
    responses = relationship("Response", back_populates="question")

class Response(Base):
    __tablename__ = 'réponses'
    id= Column(Integer, primary_key=True)
    correction =  Column(String(50))
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship("Question", back_populates="responses")
