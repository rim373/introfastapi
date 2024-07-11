from pydantic import BaseModel,Json
from typing import Dict,List, Union




class ResponseItem(BaseModel):
    response: str
    correct: bool


class QuestionRequest(BaseModel):
    content: str
    response :Json
    class Config:
        orm_mode = True



