from fastapi import FastAPI
from pymongo import MongoClient
from MongoDB_Connection import key, usr
from routes.route import router

app = FastAPI()
app.include_router(router)
