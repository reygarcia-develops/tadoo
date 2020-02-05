from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from .users import get_current_user
from ..schemas import boards
from ..models import User
from ..operations.boards import db_create_board, db_get_boards, db_get_board


router = APIRouter()


@router.get("/", response_model=List[boards.BoardResponse])
def get_boards(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db_get_boards(db=db, user_id=current_user.userId)


@router.get("/{board_id}", response_model=boards.BoardResponse)
def get_board(
    board_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db),
):
    db_board = db_get_board(db, board_id=board_id, user_id=current_user.userId)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board


@router.post("/", response_model=boards.BoardResponse)
def create_board(
    board_to_create: boards.BoardCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db_create_board(db=db, obj=board_to_create, user_id=current_user.userId)
