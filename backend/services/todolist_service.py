from models import TodoList

def create(todolist,current_user,session):
    if(not todolist.title):
        raise ValueError("Empty")
    
    new_list=TodoList(title=todolist.title,user_id=current_user.id)
    
    session.add(new_list)
    session.commit()
    session.refresh(new_list)
    
    return new_list