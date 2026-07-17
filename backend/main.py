from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from contextlib import asynccontextmanager
from controllers.user_controller import router as user_router
from controllers.todolist_controller import router as todolist_router
from controllers.task_controller import router as task_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    SQLModel.metadata.create_all(engine)

    yield

app=FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(todolist_router)
app.include_router(task_router)

