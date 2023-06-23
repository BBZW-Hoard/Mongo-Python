import uuid
from pydantic import BaseModel, Field
from typing import Optional


class File(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    songId: str = Field(...)
    File: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "songId": "1",
                "File": "123123"
            }
        }


class FileUpdate(BaseModel):
    File: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "File": "123123"
            }
        }