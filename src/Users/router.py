from fastapi import APIRouter, Depends
from src.Users.dtos import UserSchema, loginScheme
from src.utils.db import get_db
from src.Users import controller

User_Router = APIRouter(prefix='/user')

@User_Router.post('/register')
def Create_user(body : UserSchema, db = Depends(get_db) ):
    return controller.register(body, db)

@User_Router.post('/login')
def Login_user(body: loginScheme, db=Depends(get_db)):
    return controller.login_user(body, db)