from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    id: str
    email: str
    password: str