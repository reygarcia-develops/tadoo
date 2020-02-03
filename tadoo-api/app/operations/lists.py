from sqlalchemy.orm import Session

from ..models import BoardList
from ..schemas.lists import BoardListCreate


def db_get_list(db: Session, list_id: int, board_id: int):
    return (
        db.query(BoardList)
        .filter(BoardList.listId == list_id and BoardList.boardId == board_id)
        .first()
    )


def db_create_list(db: Session, obj: BoardListCreate):
    db_list = BoardList(**obj.dict())
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list
