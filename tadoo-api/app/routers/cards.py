from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from .users import get_current_user
from ..models import User
from ..operations.boards import db_get_board
from ..operations.cards import db_create_card
from ..operations.lists import db_get_list
from ..schemas.cards import CardCreate, CardResponse


router = APIRouter()


@router.post("/", response_model=CardResponse)
def create_card(
    card_to_create: CardCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_board = db_get_board(
        db=db, board_id=card_to_create.boardId, user_id=current_user.userId
    )
    if db_board is None:
        raise HTTPException(status_code=404, detail="User board not found")
    db_list = db_get_list(
        db, list_id=card_to_create.listId, board_id=card_to_create.boardId
    )
    if db_list is None:
        raise HTTPException(status_code=404, detail="User list not found")

    return db_create_card(db=db, obj=card_to_create)
