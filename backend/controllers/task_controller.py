from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from database import get_session
from schemas.task_schema import TaskCreate
from services.task_service import create

router=APIRouter(prefix="/tasks",tags=["Taks"])

@router.post("/get_Task")
def create_task(task:TaskCreate,session:Session=Depends(get_session)):
    try:
        result=create(task,session)
        return result
    except Exception as e:
        raise HTTPException(status_code=409,detail=str(e))