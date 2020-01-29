from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..schemas.cards import CardCreate, CardResponse
from ..operations.cards import db_create_card

from app.database import get_db


router = APIRouter()


@router.post("/", response_model=CardResponse)
def create_card(card_to_create: CardCreate, db: Session = Depends(get_db)):
    return db_create_card(db=db, obj=card_to_create)
