from pydantic import BaseModel
from typing import Optional

class TodoBody(BaseModel):
    title: Optional[str]
    description: Optional[str]
    complete: Optional[bool]


    
