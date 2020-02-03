from pydantic import BaseModel


class CardBase(BaseModel):
    cardName: str
    cardDescription: str
    listId: int
    boardId: int


# Database Model
class Card(CardBase):
    cardId: int

    class Config:
        orm_mode = True


class CardCreate(CardBase):
    pass


class CardResponse(Card):
    pass
