from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from src.models import Song
router = APIRouter()

@router.post("/", response_description="Create a new song", status_code=status.HTTP_201_CREATED, response_model=Song)
def create_book(request: Request, song: Song = Body(...)):
    song = jsonable_encoder(song)
    new_song = request.app.MongoDb.InsertToDB("songs", song)
    created_song = request.app.MongoDb.findDocument("songs", new_song)
    return created_song