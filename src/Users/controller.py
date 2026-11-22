from src.Users.dtos import UserSchema, loginScheme
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.Users.models import UserModel
from fastapi import HTTPException, status
from src.utils.hash import hash_password, verify_password

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


def login_user(body: loginScheme, db:Session):
    data = body.model_dump()
    user = db.query(UserModel).filter(
        or_(
        userName = data['userName'],
        email = data['email']
    )).first()
    check_password = verify_password(data['password'],user.password)
    if(check_password):
        return {'status':status.HTTP_200_OK,'data':user}
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail='User password or username not correct')