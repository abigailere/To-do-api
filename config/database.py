from pymongo import MongoClient
from config.settings import uri

client = MongoClient(uri)
db = client.todo_db
collection_name = db["todo_collection"]
