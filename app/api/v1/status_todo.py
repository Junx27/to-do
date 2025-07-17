from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.status_todo_schema import StatusTodoCreate, StatusTodoOut
from app.services import status_todo_service
from app.utils.response import success_response

router = APIRouter()

@router.post("/status-todo")
def create_status_todo(status_todo: StatusTodoCreate, db: Session = Depends(get_db)):
    result = status_todo_service.create_status_todo_service(db, status_todo)
    return success_response(data=StatusTodoOut.from_orm(result).model_dump(), message="OK", status_code=201)

@router.get("/status-todo")
def get_all_status_todo(db: Session = Depends(get_db)):
    status_todos = status_todo_service.get_all_status_todo_service(db)
    return success_response(data=[StatusTodoOut.from_orm(t).model_dump() for t in status_todos])

@router.get("/status-todo/{id}")
def get_status_todo_by_id(id: int, db: Session = Depends(get_db)):
    status_todo = status_todo_service.get_status_todo_by_id_service(db, id)
    if not status_todo:
        return success_response(message="Not found", status_code=404)
    return success_response(data=StatusTodoOut.from_orm(status_todo).model_dump())

@router.put("/status-todo/{id}")
def update_status_todo(id: int, data: StatusTodoCreate, db: Session = Depends(get_db)):
    result = status_todo_service.update_status_todo_service(db, id, data)
    if not result:
        return success_response(message="Not found", status_code=404)
    return success_response(data=StatusTodoOut.from_orm(result).model_dump(), message="OK")

@router.delete("/status-todo/{id}")
def delete_status_todo(id: int, db: Session = Depends(get_db)):
    success = status_todo_service.delete_status_todo_service(db, id)
    if not success:
        return success_response(message="Not found", status_code=404)
    return success_response(message="Deleted")