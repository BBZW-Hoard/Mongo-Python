from fastapi import APIRouter, Body, Request, Response, HTTPException, status, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import List, Annotated

router = APIRouter()

@router.post("/", response_description="upload file", status_code=status.HTTP_200_OK)
async def create_file(request: Request, file: Annotated[bytes, File()]):
    fileId = request.app.MongoDb.InsertFile(file)
    return {"content": fileId}