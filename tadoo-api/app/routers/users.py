from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..schemas import users
from ..operations.users import db_create_user, db_get_user
from app.database import get_db


router = APIRouter()


@router.get("/{user_email}", response_model=users.UserResponse)
def get_user(user_email: str, db: Session = Depends(get_db)):
    db_user = db_get_user(db, lookup_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=users.UserResponse)
def create_user(user_to_create: users.UserCreate, db: Session = Depends(get_db)):
    return db_create_user(db=db, obj=user_to_create)
