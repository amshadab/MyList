from models import TodoList,Task
from sqlmodel import select,Session
from fastapi import Depends
from utils.dependencies import get_current_user
from database import get_session

def createtodo(todolist, current_user, session):

    print("User ID:", current_user.id)
    print("Title:", todolist.title)

    if not todolist.title:
        raise ValueError("Empty")

    new_list = TodoList(
        title=todolist.title,
        user_id=current_user.id
    )

    session.add(new_list)
    session.commit()
    session.refresh(new_list)

    print("Created Todo:", new_list)

    return new_list

def updateTodo(todo_id,todolistupdate,current_user,session):
    if(not todolistupdate.title):
        raise ValueError("Empty")
    
    statement=select(TodoList).where(TodoList.id==todo_id,TodoList.user_id==current_user.id)
    
    todo=session.exec(statement).first()
    
    if not todo:
        raise ValueError("Todolist not exist")
    
    todo.title=todolistupdate.title
    session.add(todo)
    session.commit()
    session.refresh(todo)
    
    return todo

def deleteTodo(todo_id,current_user,session):
    todo=session.exec(select(TodoList).where(TodoList.id==todo_id,TodoList.user_id==current_user.id)).first()
    
    if not todo:
        raise ValueError("Todolist not exist")
    
    tasks = session.exec(
        select(Task).where(
            Task.todo_list_id == todo.id
        )
    ).all()
    
    for task in tasks:
        session.delete(task)
    
    session.delete(todo)
    session.commit()
    
    return "Successfully deleted Todolist"

def get_all_todo(current_user,session):
    todolist=session.exec(select(TodoList).where(TodoList.user_id==current_user.id)).all()
    
    return todolist
    
def get_todo(todo_list_id,current_user=Depends(get_current_user),session:Session=Depends(get_session)):
    statement=select(TodoList).where(current_user.id==TodoList.user_id,todo_list_id==TodoList.id)
    todo=session.exec(statement).first()
    if not todo:
        raise ValueError("Todolist not found")
    return todo

def get_by_id(todo_id,current_user,session):
    statement=select(TodoList).where(TodoList.id==todo_id,TodoList.user_id==current_user.id)
    
    todo=session.exec(statement).first()
    
    if not todo:
        raise ValueError("Todo not found")
    
    return todo