from sqlmodel import insert
from models import Task

def create(task,session):
    statement=insert(Task).values(task)
    session
    