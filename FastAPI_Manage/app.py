from fastapi import FastAPI
from pymongo import MongoClient
import pymongo
from config.config import settings
from contextlib import asynccontextmanager


mongo_setup = dict()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(settings.MONGO_URL)
    app.mongodb_database = app.mongodb_client[settings.MONGO_DB]
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "Demo of MongoDB with FastAPI"


@app.get("/init")
async def init_databse():
    from src.api.v1 import repository
    
    def callback_wrapper(session):
        repository.insert_user(
            session,
            app.mongodb_database,
            username = settings.ADMIN_NAME,
            email = settings.ADMIN_EMAIL,
            password = settings.ADMIN_PASSWD
        )

    with app.mongodb_client.start_session() as session:
        session.with_transaction(callback_wrapper)
    return "Collection setup successfully."
