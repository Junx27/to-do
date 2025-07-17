from sqlalchemy.orm import Session
from app.repository import todo_repo
from app.schemas.todo_schema import TodoCreate

def create_todo_service(db: Session, todo_in: TodoCreate):
    return todo_repo.create_todo(db, todo_in.name, todo_in.description)

def get_all_todos_service(db: Session):
    return todo_repo.get_all_todos(db)

def get_todo_by_id_service(db: Session, todo_id: int):
    return todo_repo.get_todo_by_id(db, todo_id)

def update_todo_service(db: Session, todo_id: int, data: TodoCreate):
    todo = todo_repo.get_todo_by_id(db, todo_id)
    if not todo:
        return None
    return todo_repo.update_todo(db, todo, data.name, data.description)

def delete_todo_service(db: Session, todo_id: int):
    todo = todo_repo.get_todo_by_id(db, todo_id)
    if not todo:
        return False
    todo_repo.delete_todo(db, todo)
    return True
