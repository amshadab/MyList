from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
from database import get_session
from schemas.task_schema import TaskCreate,TaskResponse
from services.task_service import createTask,get_all_tasks,update_task,isChecked_task
from utils.dependencies import get_current_user

router=APIRouter(prefix="/task",tags=["Task"])

@router.post("/create/{todo_list_id}",response_model=TaskResponse)
def create(todo_list_id:int,task:TaskCreate,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=createTask(todo_list_id,task,current_user,session)
        return result
    except Exception as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.get("/get/{todo_list_id}")
def get_tasks(todo_list_id,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=get_all_tasks(todo_list_id,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.put("/update/{task_id}")
def update(task_id:int,task_update:TaskCreate,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=update_task(task_id,task_update,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.put("/mark/{task_id}")
def isChecked(task_id:int,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=isChecked_task(task_id,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
        