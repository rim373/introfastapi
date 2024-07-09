from pydantic import BaseModel
from typing import Dict,List, Union




class ResponseItem(BaseModel):
    response: str
    score: int = 0 
    correct: str =""




class QuestionRequest(BaseModel):
    content: str
    response : Union[dict[int,ResponseItem], None] = None
    class Config:
        orm_mode = True


