from pydantic import BaseModel
from typing import Optional

class TodoBody(BaseModel):
    title: str| None = None
    description: str| None = None
    complete: bool| None = None


    
