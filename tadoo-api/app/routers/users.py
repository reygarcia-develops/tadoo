from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED


from ..schemas import users
from ..models import User
from ..operations.users import db_create_user, db_get_user
from app.database import get_db


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def fake_password_hash(user_password: str):
    return "fakeHash" + user_password


def fake_decode_token(token, db: Session):
    # This doesn't provide any security at all
    # Check the next version
    return db_get_user(db, lookup_email=token)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = fake_decode_token(token, db)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# NOTE: Attempts to login the user. If the password doesn't match the hashed password authentication fails.
@router.post("/login", response_model=users.UserAuth)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = db_get_user(db, lookup_email=form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    password_hash = fake_password_hash(form_data.password)
    if password_hash != db_user.passwordHash:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return users.UserAuth(access_token=db_user.userEmail)


@router.post("/", response_model=users.UserResponse)
def create_user(user_to_create: users.UserCreate, db: Session = Depends(get_db)):
    db_user = db_get_user(db, lookup_email=user_to_create.userEmail)
    if db_user:
        raise HTTPException(
            status_code=409, detail="Email is already associated to an account."
        )
    password_hash = fake_password_hash(user_to_create.password)
    created_user = db_create_user(db=db, obj=user_to_create, passwordHash=password_hash)
    return users.UserResponse(
        userEmail=created_user.userEmail,
        userFullName=created_user.userFullName,
        userId=created_user.userId,
    )


@router.get("/", response_model=users.UserResponse)
def get_user(current_user: User = Depends(get_current_user)):
    return users.UserResponse(
        userEmail=current_user.userEmail,
        userFullName=current_user.userFullName,
        userId=current_user.userId,
    )
