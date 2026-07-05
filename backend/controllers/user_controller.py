from fastapi import APIRouter,Depends
from sqlmodel import Session
from schemas.user_schema import UserRegister
from database import get_session
from services.user_service import register

router=APIRouter(prefix="/users",tags=["Users"])

@router.get("/")
def get_user():
    return "This is User router"

@router.post("/register")
def register_user(user:UserRegister,session:Session=Depends(get_session)):
    return register(user,session)