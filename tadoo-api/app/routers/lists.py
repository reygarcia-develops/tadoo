from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from .users import get_current_user
from ..database import get_db
from ..models import User
from ..operations.boards import db_get_board
from ..operations.lists import db_create_list
from ..schemas.lists import BoardList, BoardListCreate, BoardListResponse


router = APIRouter()


@router.post("/", response_model=BoardListResponse)
def create_list(
    list_to_create: BoardListCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_board = db_get_board(db=db, board_id=list_to_create.boardId, user_id=current_user.userId)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_create_list(db=db, obj=list_to_create)
