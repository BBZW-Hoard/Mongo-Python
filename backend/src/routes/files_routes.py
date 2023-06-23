from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from src.models.File import File, FileUpdate
router = APIRouter()

@router.get("/{id}", response_description="get list of songs", status_code=status.HTTP_200_OK, response_model=File)
def get_file(id: str, request: Request):
    file = request.app.MongoDb.findFileById(id)
    return file

@router.post("/", response_description="Create a new song", status_code=status.HTTP_201_CREATED, response_model=File)
def create_file(request: Request, file: File = Body(...)):
    file = jsonable_encoder(file)
    new_file = request.app.MongoDb.InsertFile(file)
    created_file = request.app.MongoDb.findFileById(new_file)
    return created_file 