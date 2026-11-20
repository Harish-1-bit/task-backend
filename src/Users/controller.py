from src.Users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.Users.models import UserModel
from fastapi import HTTPException, status
from src.utils.hash import hash_password

def register(body : UserSchema, db : Session ):
    data=body.model_dump()
    exist_user = db.query(UserModel).filter(
        UserModel.email == data['email']
    ).first()
    if exist_user :
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail='User Already exist')
    hashwd_password = hash_password(data['password'])
    new_user = UserModel(name = data['name'], email = data['email'],userName = data['userName'],password = hashwd_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status":status.HTTP_201_CREATED, "data":new_user}