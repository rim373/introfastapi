from pydantic import BaseModel


class QuestionRequest(BaseModel):
    content: str
    class Config:
        orm_mode = True
    
class ResponseRequest(BaseModel):

    correction : str
    question_id : int
    class Config:
        orm_mode = True