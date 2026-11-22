from fastapi import APIRouter, Depends, Response
from src.Users.dtos import UserSchema, loginScheme
from src.utils.db import get_db
from src.Users import controller

User_Router = APIRouter(prefix='/user')

@User_Router.post('/register')
def Create_user(body : UserSchema, db = Depends(get_db) ):
    return controller.register(body, db)

@User_Router.post('/login')
def Login_user(body: loginScheme, response:Response, db=Depends(get_db)):
   result = controller.login_user(body, db)
   response.set_cookie(
       key='access_token',
       value=result['token'],
       httponly=True,
        secure=False,  # True in production with HTTPS
        samesite="lax",
        max_age=30 * 60,
        path="/"
   )
   return {
           "message": "Login successful",
           "user": result["data"],
           'token':result['token']
       }