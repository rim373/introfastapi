from typing import Union,Optional,List
from fastapi import FastAPI, status , Depends ,HTTPException
from sqlalchemy.orm import Session
from database import *
from models import *
from schemas import *
# from pydantic import BaseModel 



# Create the database
Base.metadata.create_all(engine)



# Initialize app
app = FastAPI()


@app.post("/q",response_model=QuestionRequest, status_code=status.HTTP_201_CREATED)
def create_question(q:QuestionRequest):
      # create a new database session
    session = SessionLocal()

    # create an instance of the ToDo database model
    qdb = Question(content = q.content , response =q.response )

    # add it to the session and commit it
    session.add(qdb)
    session.commit()
    session.refresh(qdb)

    # close the session
    session.close()

    # return the id
    return qdb


@app.get("/",response_model = List[QuestionRequest])
def read_all_questions():
     # create a new database session
    session = SessionLocal()

    # get all todo items
    question_list = session.query(Question).all()

    # close the session
    session.close()

    return  question_list



@app.get("/q/{id}")
def read_question(id: int):
     # create a new database session
    session = SessionLocal()

    # get the quetions item with the given id
    question = session.query(Question).filter(Question.id == id).first()

    # close the session
    session.close()

    if not question:
        raise HTTPException(status_code=404, detail=f"the question with id {id} not found")

    return question



    
   

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

    return question



@app.put("/r/{id_question}/{id_response}")
def update_response(id_question: int,id_response:int , newresponseitem: str):


    # create a new database session
    session = SessionLocal()

   # get the question item with the given id
    question = session.query(Question).get(id_question)

    # update question item with the given task (if an item with the given id was found)
    if question:
        question.response[id_response]["response"]= newresponseitem
        session.commit()
          

    # close the session
    session.close()

    # check if quetion item with given id exists. If not, raise exception and return 404 not found response
    if not question  :
        raise HTTPException(status_code=404, detail=f"question item with id {id_question} not found")
    if test=="false" :
        raise HTTPException(status_code=404, detail=f"response item with id {id_response} in the question {id_question} not found")


    return question


@app.delete("/q/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quetion(id: int):

    # create a new database session
    session = SessionLocal()

    # get the quetion item with the given id
    question = session.query(Question).get(id)

    # if quetion item with given id exists, delete it from the database. Otherwise raise 404 error
    if question:
        session.delete(question)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"question item with id {id} not found")

    return question


@app.delete("/res/{id_question}/{id_response}", status_code=status.HTTP_204_NO_CONTENT)
def delete_response(id_question: int,id_response:int):

     # create a new database session
     session = SessionLocal()

     # get the responses item for the question with the given id
     question= session.query(Question).get(id_question)
     test = "false"
     # if question item with given id exists, delete it from the database. Otherwise raise 404 error
     for i in question.response :
         if i.id == id_response :
             test = "true" 
             session.delete(i)
             session.commit()
             session.close()
     if not question  :
         raise HTTPException(status_code=404, detail=f"question item with id {id_question} not found")
     if test=="false" :
         raise HTTPException(status_code=404, detail=f"response item with id {id_response} in the question {id_question} not found")


     return question







""" 
@app.get("/res/{id}")
def read_responses(id: int):
     # create a new database session
    session = SessionLocal()

    # get the responses for the question with id
    question= session.query(Question).filter(Question.id == id).all()

    # close the session
    session.close()

    if not question:
        raise HTTPException(status_code=404, detail=f"the question with id {id} has not a response")
    finallist =dict()
    for i in question :
        finallist[i.id]=i.response

    return  finallist



@app.post("/r/{id}", status_code=status.HTTP_201_CREATED)
def create_response(id:int):
    session = SessionLocal()
    question = session.query(Question).get(id)
    if question is None:
        raise HTTPException(status_code=404, detail=f"the question with id {id} not found")

     # create an instance of the respponse database model
    rdb = Response(correction = r.correction) 
    rdb.question_id = id

     # add it to the session and commit it
    session.add(rdb)
    session.commit()
    session.refresh(rdb)

        # close the session
    session.close()
     

    # return the id
    return rdb




 """
# @app.delete("/res/{id_question}/{id_response}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_response(id_question: int,id_response:int):

#     # create a new database session
#     session = SessionLocal()

#     # get the responses item for the question with the given id
#     response= session.query(Question).filter(Question.question_id == id_question).all()
#     test = "false"
#     # if question item with given id exists, delete it from the database. Otherwise raise 404 error
#     for i in response :
#         if i.id == id_response :
#             test = "true" 
#             session.delete(i)
#             session.commit()
#             session.close()
#     if not response  :
#         raise HTTPException(status_code=404, detail=f"question item with id {id_question} not found")
#     if test=="false" :
#         raise HTTPException(status_code=404, detail=f"response item with id {id_response} in the question {id_question} not found")


#     return None



""" @app.get("/q/r")
def read_question_responses():
    session = SessionLocal()
    finallist = []

    # Fetch all questions
    questions = session.query(Question).all()

    # Loop through each question
    for question in questions:
        question_dict = {
            "question_content": question.content,
            "responses": []
        }

        # Fetch responses for the current question
        responses = session.query(Question).filter(Question.question_id == question.id).all()

        # Loop through responses and append to question_dict
        for response in responses:
            response_dict = {
                "response_id": response.id,
                "response_correction": response.correction
            }
            question_dict["responses"].append(response_dict)

        finallist.append(question_dict)

    # Close the session
    session.close()

    return finallist
 """