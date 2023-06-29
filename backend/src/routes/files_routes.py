from fastapi import APIRouter, Body, Request, Form, Response, HTTPException, status, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import List, Annotated

router = APIRouter()

@router.post("/", response_description="upload file", status_code=status.HTTP_200_OK)
async def create_file(request: Request, file: UploadFile, songId: Annotated[str, Form()],):
    fileId = request.app.MongoDb.InsertFile(songId, file.file)
    file = request.app.MongoDb.findFileById(fileId)
    return {"content": file.read(), "fileName": file.filename}

@router.get("/{fileName}", response_description="get file", status_code=status.HTTP_200_OK)
async def get_file(request: Request, fileName: str):
    file = request.app.MongoDb.findFileByName(fileName)
    content = file.read()
    return {"content": content}