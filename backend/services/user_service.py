from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from utils.auth_jwt import create_access_token,create_refresh_token,verify_refresh_token
from models import User
from schemas.user_schema import UserRegister
from utils.password import hash_password, verify_password


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


def login(user, session):
    response = JSONResponse(content={"message":"Login Successfully"})
    if not user.email or not user.password:
        raise ValueError("All field must be require")

    statement = select(User).where(user.email == User.email)
    old_user = session.exec(statement).first()

    if not old_user:
        raise ValueError("User not found")

    if not verify_password(user.password, old_user.password):
        raise ValueError("Incorrect Password")

    access_token = create_access_token(old_user.id)
    refresh_token=create_refresh_token(old_user.id)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
    )
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax"
    )
    return response

def log_out_user():
    response=JSONResponse(
        content={"message":"Logout Successful"}
    )
    
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return response

def refresh_access_token(refresh_token):
    payload=verify_refresh_token(refresh_token)
    user_id=payload.get("sub")
    new_access_token=create_access_token(int(user_id))
    
    response=JSONResponse(
        content={"message":"Access Token refreshed"}
    )
    
    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        secure=False,
        samesite="lax",
    )
    
    return response
    
    