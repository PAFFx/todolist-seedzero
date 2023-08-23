from pydantic import BaseModel

class todo_model(BaseModel):
    title: str
    description: str = ""
    complete: bool = False

    
