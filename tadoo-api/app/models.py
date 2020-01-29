from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Board(Base):
    __tablename__ = "boards"

    boardId = Column("id", Integer, primary_key=True, index=True)
    boardName = Column("board_name", String)
    isFavorite = Column("is_favorite", Boolean, default=False)

    lists = relationship("BoardList", back_populates="board")

class BoardList(Base):
    __tablename__ = "lists"

    boardId = Column("board_id", ForeignKey("boards.id"))
    listId = Column("id", Integer, primary_key=True, index=True)
    listName = Column("list_name", String)

    board = relationship("Board", back_populates="lists")
    cards = relationship("Card", back_populates="lists")

class Card(Base):
    __tablename__ = "cards"

    listId = Column("board_id", ForeignKey("lists.id"))
    cardId = Column("id", Integer, primary_key=True, index=True)
    cardName = Column("card_name", String)
    cardDescription = Column("card_description", String)

    lists = relationship("BoardList", back_populates="cards")