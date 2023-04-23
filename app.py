from fastapi import FastAPI
from pymongo import MongoClient
import pymongo
from config.config import settings

app = FastAPI()


@app.get("/")
async def root():
    client = MongoClient(settings.MONGO_DB)
    db = client.kpnagar     # Getting a Database
    collection = db.test    # Getting a Collection
    print(collection)
    return "Demo of MongoDB with FastAPI"