from datetime import datetime,timedelta
from jose import jwt 
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

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

