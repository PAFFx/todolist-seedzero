from fastapi import FastAPI
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
