from sqlalchemy.orm import Session

from .. import models

from ..schemas.users import UserCreate


def db_create_user(db: Session, obj: UserCreate):
    db_user = models.User(**obj.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def db_get_user(db: Session, lookup_email: str):
    return db.query(models.User).filter(models.User.userEmail == lookup_email).first()
