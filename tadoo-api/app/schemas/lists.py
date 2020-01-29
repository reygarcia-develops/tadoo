from pydantic import BaseModel
from typing import List

from .cards import Card


class BoardListBase(BaseModel):
    listName: str
    boardId: int


# Database Model
class BoardList(BoardListBase):
    listId: int
    cards: List[Card] = []

    class Config:
        orm_mode = True


class BoardListCreate(BoardListBase):
    pass


class BoardListResponse(BoardList):
    pass
