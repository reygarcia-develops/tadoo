from fastapi import Depends, FastAPI, Header, HTTPException
from starlette.middleware.cors import CORSMiddleware


# Router imports
from .routers import boards, lists, cards, users

from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(boards.router, prefix="/boards", tags=["boards"])
app.include_router(lists.router, prefix="/lists", tags=["lists"])
app.include_router(cards.router, prefix="/cards", tags=["cards"])

