from beanie import Document

class todos(Document):
    title: str
    description: str = ""
    complete: bool = False

