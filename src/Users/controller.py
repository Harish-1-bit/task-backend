from src.Users.dtos import UserSchema
from sqlalchemy.orm import Session

def register(body : UserSchema, db : Session ):
    print(body)
    return {'message':'user created'}