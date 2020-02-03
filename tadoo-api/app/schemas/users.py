from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    userEmail: str
    userFullName: str


# Database Model
class User(UserBase):
    userId: int
    passwordHash: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserResponse(BaseModel):
    userEmail: str
    userFullName: str
    userId: int

