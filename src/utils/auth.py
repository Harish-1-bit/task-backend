import jwt
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
    token = jwt.decode(payload,secret_key,algorithm=algorithm)

    return token