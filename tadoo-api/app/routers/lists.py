from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..schemas.lists import BoardList, BoardListCreate, BoardListResponse
from ..operations.lists import db_create_list
from ..operations.boards import db_get_board
from app.database import get_db


router = APIRouter()


# @board_router.get("/", response_model=List[BoardResponse])
# def get_boards(db: Session = Depends(get_db)):
#     return db_get_boards(db=db)


# @board_router.get("/{board_id}", response_model=BoardResponse)
# def get_board(board_id: int, db: Session = Depends(get_db)):
#     db_board = db_get_board(db, lookup_id=board_id)
#     if db_board is None:
#         raise HTTPException(status_code=404, detail="Board not found")
#     return db_board


@router.post("/", response_model=BoardListResponse)
def create_list(list_to_create: BoardListCreate, db: Session = Depends(get_db)):
    db_board = db_get_board(db=db, lookup_id=list_to_create.boardId)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_create_list(db=db, obj=list_to_create)
