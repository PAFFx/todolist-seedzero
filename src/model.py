from beanie import Document

class Todo(Document):
    title: str
    description: str = ""
    complete: bool = False

