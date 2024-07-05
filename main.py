from typing import Union,Optional,List
from fastapi import FastAPI, status , Depends
from pydantic import BaseModel 

app = FastAPI()



class New(BaseModel):
    name : str
    clas: str
    age : int


class NewUpdate(BaseModel):
    name : Optional[str] = None
    clas: Optional[str] = None
    age : Optional[int] = None



students={
    1:{
        "name" : "rim",
        "clas": "indp1d",
        "age" :21,
    }

}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return students[item_id]


@app.get("/test")
def testilna(grade:int ,nom: Union[str, None] = None):
    for student_id in Students:
        if students[student_id].name==nom:
            return Students[student_id]
    return{"data":"not found"}



@app.put("/item/{item_id}")
def update_item(item_id:int,item:NewUpdate):
    if item_id not in students :
        return{"error":"id "}
    if item.name != None:
        students[item_id].name = item.name
    if item.clas != None:
        students[item_id].clas = item.clas
    if item.age != None:
        students[item_id].age = item.age

    




@app.post("/create_student/{student_id}")
def createstudent(student_id:int,student:New):
    if student_id in students :
        return{"error":"id exist"}
    students[student_id]=student
    return
    students[students_id]



@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students :
        return{"Erro":"student does not exist"}
    del students[student_id]
    return{"Message":"student deleted successfully"}