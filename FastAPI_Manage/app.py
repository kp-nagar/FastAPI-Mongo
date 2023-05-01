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
    def callback(session, username, email, password, lastname=None):
        user_data = {
            'username': username,
            'email': email,
            'password': password,
            'lastname': lastname
        }
        db = app.mongodb_database
        user_collection = session.client.db.UserInformation

        # Add new user data to 'UserInformation' collection
        user_collection.insert_one(user_data, session=session)
        print("Transaction successful")
        return True
    
    def callback_wrapper(s):
        callback(
            s,
            username = settings.ADMIN_NAME,
            email = settings.ADMIN_EMAIL,
            password = settings.ADMIN_PASSWD
        )

    with app.mongodb_client.start_session() as session:
        session.with_transaction(callback_wrapper)
    """
    admin_user = {
        'username': settings.ADMIN_NAME,
        'email': settings.ADMIN_EMAIL,
        'password': settings.ADMIN_PASSWD
    }
    collection = app.mongodb_database.UserInformation
    
    collection.insert_one(admin_user)
    """
    return "Collection setup successfully."
