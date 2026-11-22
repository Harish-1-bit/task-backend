import jwt
from fastapi import HTTPException
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os

load_dotenv()

secret_key = os.getenv('JWT_SECRET')
algorithm = "HS256"
token_expire = 30

def create_access_token(user_id:int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=token_expire)

    payload = {
        'sub':str(user_id),
        'exp':expire
    }
    token = jwt.encode(payload,secret_key,algorithm=algorithm)

    return token


def verify_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=[algorithm]
        )

        return payload.get("sub")

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )