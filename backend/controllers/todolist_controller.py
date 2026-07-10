from fastapi import APIRouter,HTTPException,Depends
from schemas.todolist_schema import TodoListCreate
from sqlmodel import Session
from database import get_session
from services.todolist_service import create
from utils.depencencies import get_current_user


router = APIRouter(prefix="/list",tags=["List"])


@router.post("/create")
def create_todolist(todolist:TodoListCreate,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=create(todolist,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))