from fastapi import Depends, FastAPI, Header, HTTPException

from app import models
from app.database import engine

# Router imports
from .routers import boards, cards, lists, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(boards.router, prefix="/boards", tags=["boards"])
app.include_router(lists.router, prefix="/lists", tags=["lists"])
app.include_router(cards.router, prefix="/cards", tags=["cards"])
