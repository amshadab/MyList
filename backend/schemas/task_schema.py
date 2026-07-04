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

    model_config = {"from_attributes": True}