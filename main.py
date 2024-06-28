from typing import Union,Optional,List
from fastapi import FastAPI, status , Depends
from pydantic import BaseModel 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker
from fastapi import HTTPException

#from database import Base, engine , Question





class QuestionRequest(BaseModel):
    content: str
    class Config:
        orm_mode = True





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





# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)




# Initialize app
app = FastAPI()




@app.get("/",response_model = List[QuestionRequest])
def read_all_questions():
     # create a new database session
    session = SessionLocal()

    # get all todo items
    question_list = session.query(Question).all()

    # close the session
    session.close()

    return question_list



@app.get("/q/{id}")
def read_question(id: int):
     # create a new database session
    session = SessionLocal()

    # get the quetions item with the given id
    question = session.query(Question).get(id)

    # close the session
    session.close()

    if not question:
        raise HTTPException(status_code=404, detail=f"the question with id {id} not found")

    return f" The question number: {question.id} is: {question.content}"



@app.post("/q",response_model=QuestionRequest, status_code=status.HTTP_201_CREATED)
def create_question(q:QuestionRequest):
      # create a new database session
    session = SessionLocal()

    # create an instance of the ToDo database model
    qdb = Question(content = q.content)

    # add it to the session and commit it
    session.add(qdb)
    session.commit()
    session.refresh(qdb)

    # close the session
    session.close()

    # return the id
    return qdb
    
   

@app.put("/q/{id}")
def update_question(id: int, content: str):

    # create a new database session
    session = SessionLocal()

    # get the question item with the given id
    question = session.query(Question).get(id)

    # update question item with the given task (if an item with the given id was found)
    if question:
        question.content = content
        session.commit()

    # close the session
    session.close()

    # check if quetion item with given id exists. If not, raise exception and return 404 not found response
    if not question:
        raise HTTPException(status_code=404, detail=f"question item with id {id} not found")

    return quetion



@app.delete("/q/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quetion(id: int):

    # create a new database session
    session = SessionLocal()

    # get the quetion item with the given id
    quetion = session.query(Question).get(id)

    # if quetion item with given id exists, delete it from the database. Otherwise raise 404 error
    if quetion:
        session.delete(quetion)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"quetion item with id {id} not found")

    return None

