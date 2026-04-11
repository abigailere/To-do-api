from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

#GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

#FIND request method by title
@router.get("/{title}")
async def find_todo_by_title(title: str):
    todo = collection_name.find_one({"title": title})
    if todo:
        return individual_serial(todo)
    return {"error": "Todo not found"}

#POST request method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

#PUT request method
@router.put("/{id}")
async def put_todo(id: str, todo:Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    
#DELETE request method
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})



#DELETE request method to delete all todos - this is not how it works
# @router.delete.all("/")
# async def delete_all_todos():
#     collection_name.delete_many({})