from typing import Optional
from beanie import Document

class todos(Document):
    title: str | None = None
    description: str| None = None
    complete: bool| None = None

