from fastapi import Depends, FastAPI, Header, HTTPException

# Router imports
from .routers import boards, lists, cards

from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(boards.router, prefix="/boards", tags=["boards"])
app.include_router(lists.router, prefix="/lists", tags=["lists"])
app.include_router(cards.router, prefix="/cards", tags=["cards"])

