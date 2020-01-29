from pydantic import BaseModel
from typing import List

from .lists import BoardList


class BoardBase(BaseModel):
    boardName: str
    isFavorite: bool = False


# Database Model
class Board(BoardBase):
    boardId: int
    lists: List[BoardList] = []

    class Config:
        orm_mode = True


class BoardCreate(BoardBase):
    pass


class BoardResponse(Board):
    pass
