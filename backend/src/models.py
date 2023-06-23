import uuid
from pydantic import BaseModel, Field
from typing import Optional


class Song(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    attributes: object = Field(None)
    duartion: int = Field(...)
    rating: float = Field(...)
    url: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Forest of Jnana and Vidya",
                "attributes": [
                    "Genshin Impact"
                ],
                "duartion": 65,
                "rating": 4.5,
                "url": "public/songs/a-call-to-the-soul.mp3"
            }
        }

class SongUpdate(BaseModel):
    name: Optional[str]
    attributes: Optional[object]
    duartion: Optional[int]
    rating: Optional[float]
    url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Forest of Jnana and Vidya",
                "attributes": [
                    "Genshin Impact"
                ],
                "duartion": 65,
                "rating": 4.5,
                "url": "public/songs/a-call-to-the-soul.mp3"
            }
        }

class Playlist(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    song: list[Song] = Field(None)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Test",
                "songs": []
            }
        }

class PlaylistUpdate(BaseModel):
    name: Optional[str]
    song: Optional[list]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Test",
                "songs": []
            }
        }