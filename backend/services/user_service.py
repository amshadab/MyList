from sqlmodel import Session,select
from models import User
from schemas.user_schema import UserRegister
from utils.password import hash_password
def register(user:UserRegister, session:Session):
    statement=select(User).where(user.email==User.email)
    old_user=session.exec(statement).first()

    if(old_user):
        return {"error":"User already exist"}
    

    new_user=User(
        fname=user.fname,
        lname=user.lname,
        email=user.email,
        password=hash_password(user.password)
    )

    

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user