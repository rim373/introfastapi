from typing import Union,Optional,List,Annotated
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@app.post("/q",response_model=QuestionRequest, status_code=status.HTTP_201_CREATED)
def create_question(q:QuestionRequest,db:db_dependency):
      # create a new database session
    #session = SessionLocal()

    # create an instance of the ToDo database model
    qdb =Question(content = q.content)

    # add it to the session and commit it
    db.add(qdb)
    db.commit()
    db.refresh(qdb)
    for choice in q.choices :
        choice_db =Response(response_text=choice.response_text,is_correct=choice.is_correct,question_id=qdb.id)
        db.add(choice_db)
    db.commit()
    
    # close the session
    #session.close()

    # return the id
    return qdb


@app.get("/",response_model = List[QuestionRequest])
def read_all_questions(db:db_dependency):
    # get all todo items
    question_list = db.query(Question).all()
    finallist=[]
    #k=0
    for question in question_list :
        response = db.query(Response).filter(Response.question_id == question.id).all()
        l=[]
        for i in response:
            res=ResponseItem
            res.response_text=i.response_text
            res.is_correct=i.is_correct
            l.append(res)
        qa=QuestionRequest
        qa.content=question.content
        qa.choices=l
        
        finallist.append(qa)


    return finallist





@app.get("/q/{id}")
def read_question(id: int,db:db_dependency):
   
    # get the quetions item with the given id
    question = db.query(Question).get(id)
    response = db.query(Response).filter(Response.question_id == id).all()
    

    if not question:
        raise HTTPException(status_code=404, detail=f"the question with id {id} not found")
    r=dict()
    k=0
    for i in response:
        k+=1
        res=dict()
        res["response"]=i.response_text
        res["is correct"]=i.is_correct
        r[k]=res
        


    return {"question":question.content,"responses":r}



    
   

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
def update_response(id_question: int,id_response:int , newresponseitem: str,db:db_dependency):


 

   # get the question item with the given id
    question= db.query(Question).get(id_question)

     # check if quetion item with given id exists. If not, raise exception and return 404 not found response
    if not question :
        raise HTTPException(status_code=404, detail=f"question item with id {id_question} not found")
    
    # get the question item with the given id
    response = db.query(Response).filter(Response.question_id==id_question).all()

    # update question item with the given task (if an item with the given id was found)
    test = "false"
    if response:
        for i in response:
            if i.id == id_response:
                test = "true"
                i.response_text = newresponseitem
                db.commit()
          

   


    if test=="false" :
        raise HTTPException(status_code=404, detail=f"response item with id {id_response} in the question {id_question} not found")


    return {"question":question.content,"response":newresponseitem}


@app.delete("/q/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(id: int,db:db_dependency):

    # get the quetion item with the given id
    question = db.query(Question).get(id)

    # get the responses for the question with the given id
    response=db.query(Response).filter(Response.question_id==id)

    #delete responses related to this question
    if response :
        for i in response :
            db.delete(i)
            db.commit()

    #delelte question with given id
    if question:
        db.delete(question)
        db.commit()
    
    else:
        raise HTTPException(status_code=404, detail=f"question item with id {id} not found")

    return None


@app.delete("/res/{id_question}/{id_response}", status_code=status.HTTP_204_NO_CONTENT)
def delete_response(id_question: int,id_response:int,db:db_dependency):

    
     # get  the question with the given id
     question= db.query(Question).get(id_question)

    # get the responses item for the question with the given id
     response= db.query(Response).filter(Response.question_id==id_question).all()

     test = "false"
     # if question item with given id exists, delete it from the database. Otherwise raise 404 error
     for i in response :
         if i.id == id_response :
             test = "true" 
             db.delete(i)
             db.commit()
             
     if not question  :
         raise HTTPException(status_code=404, detail=f"question item with id {id_question} not found")
     if test=="false" :
         raise HTTPException(status_code=404, detail=f"response item with id {id_response} in the question {id_question} not found")


     return f"response with id ={id_response} of the question {question.id} is delated"







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