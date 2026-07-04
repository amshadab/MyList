from sqlmodel import Session
from models import User
from schemas import UserRegister

def register(user:UserRegister, session:Session):
    new_user=user(
        fname=user.fname,
        lname=user.lname,
        email=user.email,
        password=user.password
    )

    

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user