from sqlmodel import SQLModel

class TodoListCreate(SQLModel):
    title:str

class TodoListUpdate(SQLModel):
    title:str

class TodoListResponse(SQLModel):
    id:str
    title:str

