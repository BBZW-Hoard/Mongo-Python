from pymongo import MongoClient
from fastapi import FastAPI
from src.routes import router as book_router
import os

connectionString = os.environ["DB_CONNECTION"] if "DB_CONNECTION" in os.environ  else "mongoDb"
dbName = os.environ["DB_NAME"] if "DB_NAME" in os.environ  else "JukeBox"

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(connectionString)
    app.database = app.mongodb_client[dbName]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}

app.include_router(book_router, tags=["songs"], prefix="/songs")

