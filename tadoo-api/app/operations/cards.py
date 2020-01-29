from sqlalchemy.orm import Session

from ..models import Card
from ..schemas.cards import CardCreate


def db_create_card(db: Session, obj: CardCreate):
    db_card = Card(**obj.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card
