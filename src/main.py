from fastapi import FastAPI, Response, responses
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .schemas import TodoBody
from .model import Todo

app = FastAPI()

@app.on_event("startup")
async def init_db():
    client = AsyncIOMotorClient("mongodb://root:rootpassword@localhost:27017")
    await init_beanie(database=client.todos)



@app.get('/todos')
async def get_todos() -> list[Todo]:
    todos = await Todo.find().to_list()
    return todos

@app.get('/todos/{todo_id}',status_code= 200)
async def get_todo(todo_id: str, response: Response) -> Todo | str:
    todo = await Todo.get(todo_id)
    if todo == None:
        response.status_code = 404
        return "Not Found"
    return todo

