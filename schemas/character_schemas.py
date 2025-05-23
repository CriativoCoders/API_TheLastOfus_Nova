# character_schemas.py

from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CharacterBaseSchema(SCBaseModel):
    name: str
    role: str
    personality: Optional[str] = None
    background: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class CharacterSchema(CharacterBaseSchema):
    id: int

class CharacterCreateSchema(CharacterBaseSchema):
    pass

class CharacterUpdateSchema(CharacterBaseSchema):
    name: Optional[str] = None
    role: Optional[str] = None