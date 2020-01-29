from sqlalchemy.orm import Session

from ..models import BoardList
from ..schemas.lists import BoardListCreate


def db_create_list(db: Session, obj: BoardListCreate):
    db_list = BoardList(**obj.dict())
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list
