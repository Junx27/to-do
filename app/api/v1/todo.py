from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.todo_schema import TodoCreate, TodoOut
from app.services import todo_service
from app.utils.response import custom_response

router = APIRouter()

@router.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    result = todo_service.create_todo_service(db, todo)
    return custom_response(data=TodoOut.from_orm(result).dict(), message="Created", status_code=201)

@router.get("/todos")
def get_all(db: Session = Depends(get_db)):
    todos = todo_service.get_all_todos_service(db)
    return custom_response(data=[TodoOut.from_orm(t).dict() for t in todos])

@router.get("/todos/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo_by_id_service(db, id)
    if not todo:
        return custom_response(message="Not found", status_code=404)
    return custom_response(data=TodoOut.from_orm(todo).dict())

@router.put("/todos/{id}")
def update(id: int, data: TodoCreate, db: Session = Depends(get_db)):
    result = todo_service.update_todo_service(db, id, data)
    if not result:
        return custom_response(message="Not found", status_code=404)
    return custom_response(data=TodoOut.from_orm(result).dict(), message="Updated")

@router.delete("/todos/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    success = todo_service.delete_todo_service(db, id)
    if not success:
        return custom_response(message="Not found", status_code=404)
    return custom_response(message="Deleted")
