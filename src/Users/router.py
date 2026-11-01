from fastapi import APIRouter, Depends
from src.Users.dtos import UserSchema
from src.utils.db import get_db
from src.Users import controller

User_Router = APIRouter(prefix='/user')

@User_Router.post('/')
def Create_user(body : UserSchema, db = Depends(get_db) ):
    return controller.register(body, db)