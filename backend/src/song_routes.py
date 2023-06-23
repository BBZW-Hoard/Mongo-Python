from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from src.models import Song, SongUpdate
router = APIRouter()

@router.get("/", response_description="get list of songs", status_code=status.HTTP_200_OK, response_model=List[Song])
def get_songs(request: Request):
    songs = request.app.MongoDb.getSongs()
    return songs

@router.get("/{id}", response_description="get list of songs", status_code=status.HTTP_200_OK, response_model=Song)
def get_song(id: str, request: Request):
    song = request.app.MongoDb.findSongById(id)
    return song

@router.delete("/{id}", response_description="delete song", status_code=status.HTTP_200_OK, response_model=Song)
def delete_song(id: str, request: Request):
    result = request.app.MongoDb.deleteDocument(id)
    return result

@router.post("/", response_description="Create a new song", status_code=status.HTTP_201_CREATED, response_model=Song)
def create_song(request: Request, song: Song = Body(...)):
    song = jsonable_encoder(song)
    new_song = request.app.MongoDb.InsertSong(song)
    created_song = request.app.MongoDb.findSongById(new_song.inserted_id)
    return created_song 

@router.put("/{id}", response_description="Edit a song", status_code=status.HTTP_201_CREATED, response_model=Song)
def update_song(id: str, request: Request, song: SongUpdate = Body(...)):
    song = {k: v for k, v in song.dict().items() if v is not None}
    if len(song) >= 1:
        update_result = request.app.MongoDb.UpdateSong(id, song) 
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with ID {id} not found")   
    if (
        existing_song := request.app.MongoDB.collection.find_one({"_id": id})
    ) is not None:
        return existing_song    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Song with ID {id} not found")