from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from ..schemas import boards
from ..operations.boards import db_create_board, db_get_boards, db_get_board


router = APIRouter()


@router.get("/", response_model=List[boards.BoardResponse])
def get_boards(db: Session = Depends(get_db)):
    return db_get_boards(db=db)


@router.get("/{board_id}", response_model=boards.BoardResponse)
def get_board(board_id: int, db: Session = Depends(get_db)):
    db_board = db_get_board(db, lookup_id=board_id)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board


@router.post("/", response_model=boards.BoardResponse)
def create_board(board_to_create: boards.BoardCreate, db: Session = Depends(get_db)):
    return db_create_board(db=db, obj=board_to_create)
