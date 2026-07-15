from models import TodoList
from sqlmodel import select

def createtodo(todolist,current_user,session):
    if(not todolist.title):
        raise ValueError("Empty")
    
    new_list=TodoList(title=todolist.title,user_id=current_user.id)
    
    session.add(new_list)
    session.commit()
    session.refresh(new_list)
    
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
    
    session.delete(todo)
    session.commit()
    
    return "Successfully deleted Todolist"
    