from models import TodoList,Task
from sqlmodel import select
from services.todolist_service import get_todo


def createTask(todo_list_id,task,current_user,session):
    
    statement=select(TodoList).where(TodoList.id==todo_list_id,TodoList.user_id==current_user.id)
    todo=session.exec(statement).first()
    
    if not todo:
        raise ValueError("Todolist not found")
    
    new_task=Task(
        title=task.title,
        todo_list_id=todo.id
    )
    
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    
    return new_task

def get_all_tasks(todo_list_id,current_user,session):
    todo=get_todo(todo_list_id,current_user,session)
    
    statement=select(Task).where(Task.todo_list_id==todo.id)
    result = session.exec(statement).all()
    
    return result

def update_task(task_id,task_update,current_user,session):
    statement=select(Task).where(task_id==Task.id)
    task=session.exec(statement).first()
    
    if not task:
        raise ValueError("Task not found")
    
    get_todo(task.todo_list_id,current_user,session)
    
    task.title=task_update.title
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task
    
def isChecked_task(task_id,current_user,session):
    statement=select(Task).where(task_id==Task.id)
    get_task=session.exec(statement).first()
    
    if not get_task:
        raise ValueError("Task not found")
    
    get_todo(get_task.todo_list_id,current_user,session)
    
    get_task.completed = not get_task.completed
    
    session.add(get_task)
    session.commit()
    session.refresh(get_task)
    
    return get_task
    