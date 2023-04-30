from fastapi import FastAPI
from pymongo import MongoClient
import pymongo
from config.config import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb_client = MongoClient(settings.MONGO_URL)
    mongodb_database = mongodb_client[settings.MONGO_DB]
    yield
    mongodb_client.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "Demo of MongoDB with FastAPI"