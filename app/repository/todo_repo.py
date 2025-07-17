from sqlalchemy.orm import Session
from app.models.todo_model import Todo

def create_todo(db: Session, name: str, description: str | None):
    todo = Todo(name=name, description=description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_all_todos(db: Session):
    return db.query(Todo).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo: Todo, name: str, description: str | None):
    todo.name = name
    todo.description = description
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()
