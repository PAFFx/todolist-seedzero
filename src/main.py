from fastapi import FastAPI, Response, responses
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .schemas import TodoBody
from .model import todos

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    client = AsyncIOMotorClient("mongodb://root:rootpassword@localhost:27017")
    await init_beanie(database=client.todos, document_models=[todos])



@app.get('/todos')
async def get_todos() -> list[todos]:
    res = await todos.find().to_list()
    return res

@app.get('/todos/{todo_id}',status_code= 200)
async def get_todo(todo_id: str, response: Response) -> todos | str:
    todo = await todos.get(todo_id)
    if todo == None:
        response.status_code = 404
        return "Not Found"
    return todo

@app.post('/todos', status_code=201)
async def create_todo(todo_body: TodoBody):
    todo = todos(**todo_body.model_dump())
    await todo.insert()
    return todo



