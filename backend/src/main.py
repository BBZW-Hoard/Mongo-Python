from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.song_routes import router as song_router
from src.routes.playlist_routes import router as playlist_router
import os
from src.modules.MongoDb import MongoDb

connectionString = os.environ["DB_CONNECTION"] if "DB_CONNECTION" in os.environ  else "mongoDb"
dbName = os.environ["DB_NAME"] if "DB_NAME" in os.environ  else "JukeBox"

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_db_client():
    app.MongoDb = MongoDb(connectionString)
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.MongoDb.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}

app.include_router(song_router, tags=["songs"], prefix="/songs")
app.include_router(playlist_router, tags=["playlists"], prefix="/playlists")

