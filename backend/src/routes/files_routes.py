from fastapi import APIRouter, Body, Request, Response, HTTPException, status, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import List, Annotated

router = APIRouter()

@router.post("/", response_description="upload file", status_code=status.HTTP_200_OK)
async def create_file(request: Request, file: UploadFile):
    songId = "2"
    fileId = request.app.MongoDb.InsertFile(file.filename, file.file)
    file = request.app.MongoDb.findFileById(fileId)
    return {"content": file.read()}

@router.get("/", response_description="get file", status_code=status.HTTP_200_OK)
async def get_file(request: Request, fileId: str):
    file = request.app.MongoDb.findFileById(fileId)
    content = file.read()
    return {"content": content}