from sqlalchemy.orm import Session

from .. import models

from ..schemas.boards import BoardCreate


def db_get_board(db: Session, lookup_id: int):
    return db.query(models.Board).filter(models.Board.boardId == lookup_id).first()


def db_get_boards(db: Session):
    return db.query(models.Board).all()


def db_create_board(db: Session, obj: BoardCreate):
    db_board = models.Board(**obj.dict())
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board
