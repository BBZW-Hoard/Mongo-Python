from fastapi import APIRouter, Body, Request, Response, HTTPException, status, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import List

from src.models.File import File, FileUpdate
router = APIRouter()

@router.post("/", response_description="upload file", status_code=status.HTTP_200_OK, response_model=str)
def post_file(file: UploadFile):
    return {"filename": file.filename}