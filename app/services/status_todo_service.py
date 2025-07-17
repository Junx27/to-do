from sqlalchemy.orm import Session
from app.repository import status_todo_repo
from app.schemas.status_todo_schema import StatusTodoCreate

def create_status_todo_service(db: Session, status_todo_in: StatusTodoCreate):
    return status_todo_repo.create_status_todo(db, status_todo_in.status, status_todo_in.todo_id)

def get_all_status_todo_service(db: Session):
    return status_todo_repo.get_all_status_todo(db)

def get_status_todo_by_id_service(db: Session, status_todo_id: int):
    return status_todo_repo.get_status_todo_by_id(db, status_todo_id)

def update_status_todo_service(db: Session, status_todo_id: int, data: StatusTodoCreate):
    status_todo = status_todo_repo.get_status_todo_by_id(db, status_todo_id)
    if not status_todo:
        return None
    return status_todo_repo.update_status_todo(db, status_todo, data.status, data.todo_id)

def delete_status_todo_service(db: Session, status_todo_id: int):
    status_todo = status_todo_repo.get_status_todo_by_id(db, status_todo_id)
    if not status_todo:
        return False
    status_todo_repo.delete_status_todo(db, status_todo)
    return True