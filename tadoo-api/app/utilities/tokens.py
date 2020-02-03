import os

from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import encode
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from app.database import get_db
from ..operations.users import db_get_user

SECRET_KEY = os.getenv("SECRET_KEY")
CREDENTIALS_EXCEPTION = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# verfies password hashes match
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# hashes the plaintext password
def get_password_hash(plain_password: str):
    return pwd_context.hash(plain_password)


# creates the jwt access token
def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

