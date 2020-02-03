from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jwt import decode, PyJWTError
from starlette.status import HTTP_401_UNAUTHORIZED
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from ..schemas import users
from ..schemas import tokens
from ..models import User
from ..operations.users import db_create_user, db_get_user
from ..utilities.tokens import (
    create_access_token,
    oauth2_scheme,
    get_password_hash,
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    CREDENTIALS_EXCEPTION,
    SECRET_KEY,
)

router = APIRouter()


def authenticate_user(user_name: str, user_pass: str, db: Session):
    db_user = db_get_user(db, lookup_email=user_name)
    if not db_user:
        return False
    if not verify_password(user_pass, db_user.passwordHash):
        return False
    return db_user


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise CREDENTIALS_EXCEPTION
        token_data = tokens.TokenData(username=username)
    except PyJWTError:
        raise CREDENTIALS_EXCEPTION
    current_user = db_get_user(db, lookup_email=token_data.username)
    if current_user is None:
        raise CREDENTIALS_EXCEPTIONS
    return current_user


# NOTE: Attempts to login the user. If the password doesn't match the hashed password authentication fails.
@router.post("/token", response_model=tokens.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.userEmail}, expires_delta=access_token_expires
    )
    return tokens.Token(access_token=access_token)


@router.post("/", response_model=users.UserResponse)
def create_user(user_to_create: users.UserCreate, db: Session = Depends(get_db)):
    db_user = db_get_user(db, lookup_email=user_to_create.userEmail)
    if db_user:
        raise HTTPException(
            status_code=409, detail="Email is already associated to an account."
        )
    password_hash = get_password_hash(user_to_create.password)
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
        boards=current_user.boards,
    )
