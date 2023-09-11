from typing import Union, Optional, Any
import json

from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.mongodb.services.user import insertOneUser, findOneUser
from src.mongodb.models import User
from src.utils.mongodb import JSONEncoder
from pydantic import BaseModel
import logging
logger = logging.getLogger("main")


app = FastAPI()

class UserInput(BaseModel):
    email: str
    password: str

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.json_encoder = JSONEncoder

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/login")
def login_user():
    return {"message": "user logged in"}


class SignupResponse(BaseModel):
    data: Union[User, None] = None
    error: Union[str, None] = None

@app.post("/signup", response_model=User | Any, status_code=status.HTTP_201_CREATED)
def signup_user(user: UserInput, response: Response) -> Any:
    try:
        newUser = insertOneUser(vars(user))
        if (newUser.inserted_id):
            createdUser = findOneUser({ "_id": newUser.inserted_id })
            createdUser["id"] = str(createdUser.get("_id"))
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=createdUser)
        else:
            logger.warning("Hello")
            logger.warning(newUser)
    except Exception as e:
        logger.warning(e)
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content="Duplicate email")
    
    