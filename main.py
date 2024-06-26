from typing import Union,Optional

from fastapi import FastAPI, status

from pydantic import BaseModel 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///question.db")

# Create a DeclarativeMeta instance
Base = declarative_base()


# Define To Do class inheriting from Base
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


@app.get("/")
def root():
    return "Hello in my app"



@app.post("/q", status_code=status.HTTP_201_CREATED)
def create_question():
    return "create Question item"


@app.get("/q/{id}")
def read_question(id: int):
    return "read question item with id {id}"


@app.put("/q/{id}")
def update_question(id: int):
    return "update question item with id {id}"

@app.delete("/q/{id}")
def delete_question(id: int):
    return "delete question item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read question list"
