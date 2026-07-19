from fastapi import APIRouter,HTTPException,Depends
from schemas.todolist_schema import TodoListCreate
from schemas.task_schema import TodoDetailResponse
from sqlmodel import Session
from database import get_session
from services.todolist_service import createtodo,updateTodo,deleteTodo,get_all_todo,get_by_id
from utils.dependencies import get_current_user
from schemas.todolist_schema import TodoListResponse,TodoListUpdate


router = APIRouter(prefix="/list",tags=["List"])


@router.post("/create",response_model=TodoListResponse)
def create(todolist:TodoListCreate,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result=createtodo(todolist,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.put("/update/{todo_id}")
def update(todo_id: int,todolistupdate:TodoListUpdate,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result = updateTodo(todo_id,todolistupdate,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.delete("/delete/{todo_id}")
def delete(todo_id:int,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result = deleteTodo(todo_id,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))

@router.get("/get_todo")
def get_todos(current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result = get_all_todo(current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=409,detail=str(e))
    
@router.get("/get_by_id/{todo_id}",response_model=TodoDetailResponse)
def get_todo_by_id(todo_id:int, current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    try:
        result = get_by_id(todo_id,current_user,session)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))