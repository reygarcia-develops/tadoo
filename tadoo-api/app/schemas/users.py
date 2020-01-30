from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    userEmail: str
    userFullName: str


# Database Model
class User(UserBase):
    userId: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserResponse(User):
    pass
