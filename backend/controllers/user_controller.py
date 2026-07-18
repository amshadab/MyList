from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from schemas.user_schema import UserRegister,UserLogin
from database import get_session
from services.user_service import register,login,log_out_user
from utils.dependencies import get_current_user

router=APIRouter(prefix="/user",tags=["Users"])

@router.post("/register")
def register_user(user:UserRegister,session:Session=Depends(get_session)):
    try:
        reuslt= register(user,session)
        return reuslt
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.post("/login")
def login_user(user:UserLogin,session:Session=Depends(get_session)):
    try:
        result=login(user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@router.post("/logout")
def log_out():
    return log_out_user()

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    try:
        return current_user
    except ValueError as e:
        raise HTTPException(status_code=408,detail=str(e))