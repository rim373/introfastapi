from pydantic import BaseModel

class Question(BaseModel):
    content: str
    class Config:
        orm_mode = True
