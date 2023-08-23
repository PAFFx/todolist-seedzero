from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str = ""
    complete: bool = False

class Todos(BaseModel):
    todos: list[Todo]

    
