from pydantic import BaseModel
from bson import ObjectId
from uuid import UUID

class User(BaseModel):
    id: str
    email: str
    password: str