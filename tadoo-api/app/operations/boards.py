from sqlalchemy.orm import Session

from .. import models

from ..schemas.boards import BoardCreate


def db_get_board(db: Session, board_id: int, user_id: int):
    return (
        db.query(models.Board)
        .filter(models.Board.boardId == board_id and models.Board.userId == user_id)
        .first()
    )


def db_get_boards(db: Session, user_id: int):
    return db.query(models.Board).filter(models.Board.userId == user_id).all()


def db_create_board(db: Session, obj: BoardCreate, user_id: int):
    db_board = models.Board(**obj.dict(), userId=user_id)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board
