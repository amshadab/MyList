from fastapi import Cookie,HTTPException,Depends
from models import User
from sqlmodel import Session
from database import get_session
from utils.auth_jwt import verify_access_token
def get_current_user(session:Session=Depends(get_session),access_token:str=Cookie(None)):
    if(access_token is None):
        raise HTTPException(status_code=404,detail="Invalid access token")
    
    payload=verify_access_token(access_token)
    
    user_id=payload.get("sub")
    
    if user_id is None:
        raise HTTPException(status_code=401,detail="Invalid Token")
    
    user=session.get(User,int(user_id))
    
    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    
    return user