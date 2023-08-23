from beanie import Document

class todo_doc(Document):
    title: str
    description: str = ""
    complete: bool = False

    class settings:
        name = "todos"
