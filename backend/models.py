from datetime import datetime,timezone
from typing import Optional
from sqlmodel import Field,SQLModel
from pydantic import EmailStr

def _now()->datetime:
    return datetime.now(timezone.utc)

class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    fname:str
    lname:str
    email:EmailStr
    password:str

class TodoList(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    title:str
    
    user_id:int=Field(foreign_key="user.id")

class Task(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    title:str
    completed:bool=Field(default=False)

    todo_list_id:int=Field(foreign_key="todolist.id")
    