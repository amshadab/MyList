from sqlmodel import Session, select
from pydantic import EmailStr
from models import User
from schemas.user_schema import UserRegister
from utils.password import hash_password,verify_password


def register(user: UserRegister, session: Session):

    statement = select(User).where(user.email == User.email)
    old_user = session.exec(statement).first()

    if user.fname == "" or user.lname == "":
        raise ValueError("All Field must be required")

    if old_user:
        raise ValueError("User Already Exist")

    new_user = User(
        fname=user.fname,
        lname=user.lname,
        email=user.email,
        password=hash_password(user.password),
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def login(user,session):
    if(not user.email or not user.password):
        raise ValueError("All field must be require")
    
    statement = select(User).where(user.email == User.email)
    old_user = session.exec(statement).first()
    
    if(not old_user):
        raise ValueError("User not found")
    
    if(not verify_password(user.password,old_user.password)):
        raise ValueError("Incorrect Password")
    
    return {user.email,user.password}