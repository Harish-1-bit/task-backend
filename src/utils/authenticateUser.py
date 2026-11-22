
from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.utils.auth import verify_access_token
from src.utils.db import get_db
from src.Users.models import UserModel


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):

    # Get token from cookie
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login first"
        )

    # Verify JWT token
    user_id = verify_access_token(token)

    # Find user in database
    user = db.query(UserModel).filter(
        UserModel.id == int(user_id)
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user
