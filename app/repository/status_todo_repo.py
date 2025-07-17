from sqlalchemy.orm import Session
from app.models.status_todo import StatusTodo

def create_status_todo(db: Session, status: str, todo_id: int):
    status_todo = StatusTodo(status=status, todo_id=todo_id)
    db.add(status_todo)
    db.commit()
    db.refresh(status_todo)
    return status_todo

def get_all_status_todo(db: Session):
    return db.query(StatusTodo).all()

def get_status_todo_by_id(db: Session, status_todo_id: int):
    return db.query(StatusTodo).filter(StatusTodo.id == status_todo_id).first()

def update_status_todo(db: Session, status_todo: StatusTodo, status: str, todo_id: int):
    status_todo.status = status
    status_todo.todo_id = todo_id
    db.commit()
    db.refresh(status_todo)
    return status_todo

def delete_status_todo(db: Session, status_todo: StatusTodo):
    db.delete(status_todo)
    db.commit()