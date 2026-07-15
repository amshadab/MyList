from sqlmodel import SQLModel

class TaskCreate(SQLModel):
    title:str

class TaskUpdate(SQLModel):
    title:str | None =None
    completed : bool | None=None

class TaskResponse(SQLModel):
    id: int
    title: str
    completed: bool
    todo_list_id: int
