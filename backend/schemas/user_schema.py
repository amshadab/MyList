from sqlmodel import SQLModel
from pydantic import EmailStr

class UserRegister(SQLModel):
    fname:str
    lname:str
    email:EmailStr
    password:str


class UserLogin(SQLModel):
    email:EmailStr
    password:str


class UserResponse(SQLModel):
    fname:str
    lname:str
    email:EmailStr