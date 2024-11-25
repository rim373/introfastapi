from pydantic import BaseModel,Json
from typing import Dict,List, Union , Optional



class ResponseItem(BaseModel):
    response_text: str
    is_correct: bool

class ImageItem(BaseModel):
    #data: LargeBinary
    rendered_data: str
    name : str


class QuestionRequest(BaseModel):
    content: str
    choices : List[ResponseItem]
    #image: Optional[ImageItem] = None


class UserItem(BaseModel):
    cin : int
    full_name : str
    Email : str 
    password : str 


