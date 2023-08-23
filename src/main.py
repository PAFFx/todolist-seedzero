from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .schemas import todo_model

app = FastAPI()

@app.on_event("startup")
async def init_db():
    client = AsyncIOMotorClient("mongodb://root:rootpassword@localhost:27017")
    await init_beanie(database=client.todos)

@app.get('')
def get_todos():
    return "OK"
