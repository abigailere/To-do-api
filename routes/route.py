from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos