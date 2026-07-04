from sqlmodel import SQLModel

class UserRegister(SQLModel):
    fname:str
    lname:str
    email:str
    password:str


class UserLogin(SQLModel):
    email:str
    passsword:str


class UserResponse(SQLModel):
    fname:str
    lname:str
    email:str