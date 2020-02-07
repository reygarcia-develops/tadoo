from pydantic import BaseModel
from typing import List

from .boards import Board


class UserBase(BaseModel):
    userEmail: str
    userFullName: str


# Database Model
class User(UserBase):
    userId: int
    passwordHash: str
    boards: List[Board] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    userPassword: str


class UserResponse(BaseModel):
    userEmail: str
    userFullName: str
    userId: int
    boards: List[Board] = []

