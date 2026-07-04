from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from contextlib import asynccontextmanager

app=FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    SQLModel.metadata.create_all(engine)

    yield

    # Shutdown code
    # (Nothing to do for now)

@app.get("/")
def home():
    return "Hello"

