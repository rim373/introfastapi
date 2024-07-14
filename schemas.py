from pydantic import BaseModel,Json
from typing import Dict,List, Union




class ResponseItem(BaseModel):
    response_text: str
    is_correct: bool


class QuestionRequest(BaseModel):
    content: str
    choices : List[ResponseItem]



