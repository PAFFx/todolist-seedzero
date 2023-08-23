from beanie import Document

class Todo_doc(Document):
    title: str
    description: str = ""
    complete: bool = False

    class settings:
        name = "todos"
