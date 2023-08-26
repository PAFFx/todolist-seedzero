from pydantic import BaseModel
from typing import Optional

class TodoBody(BaseModel):
    title: Optional[str]| None = None
    description: str| None = None
    complete: bool| None = None


    
