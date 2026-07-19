from datetime import datetime,timedelta
from jose import jwt 
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES,REFRESH_TOKEN_EXPIRE_DAYS

def create_access_token(user_id:int):
    expire= datetime.now()+timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    payload={
        "sub":str(user_id),
        "exp":expire,
        "type":"access"
    }
    
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    
    return token

def verify_access_token(token):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
    return payload


def create_refresh_token(user_id:int):
    expire=datetime.now()+timedelta(days=int(REFRESH_TOKEN_EXPIRE_DAYS))
    
    payload={
        "sub":str(user_id),
        "exp":expire,
        "type":"refresh"
    }
    
    refresh_token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return refresh_token
    

def verify_refresh_token(token):
    
    if(token is None):
        raise ValueError("Refresh Token missing")
    
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    
    if payload.get("type")!="refresh":
        raise ValueError("Invalid refresh token")
    
    return payload