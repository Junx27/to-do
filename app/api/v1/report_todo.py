from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.report_todo_schema import ReportTodoCreate, ReportTodoOut
from app.services import report_todo_service
from app.utils.response import success_response

router = APIRouter()

@router.post("/report-todo")
def create_report_todo(report_todo: ReportTodoCreate, db: Session = Depends(get_db)):
    result = report_todo_service.create_report_todo_service(db, report_todo)
    return success_response(data=ReportTodoOut.model_validate(result).model_dump(), message="OK", status_code=201)

@router.get("/report-todo")
def get_all_report_todo(db: Session = Depends(get_db)):
    report_todos = report_todo_service.get_all_report_todo_service(db)
    return success_response(data=[ReportTodoOut.model_validate(t).model_dump() for t in report_todos])

@router.get("/report-todo/{id}")
def get_report_todo_by_id(id: int, db: Session = Depends(get_db)):
    report_todo = report_todo_service.get_report_todo_by_id_service(db, id)
    if not report_todo:
        return success_response(message="Not found", status_code=404)
    return success_response(data=ReportTodoOut.model_validate(report_todo).model_dump())

@router.put("/report-todo/{id}")
def update_report_todo(id: int, data: ReportTodoCreate, db: Session = Depends(get_db)):
    result =  report_todo_service.update_report_todo_service(db, id, data)
    if not result:
        return success_response(message="Not found", status_code=404)
    return success_response(data=ReportTodoOut.model_validate(result).model_dump(), message="OK")

@router.delete("/report-todo/{id}")
def delete_report_todo(id: int, db: Session = Depends(get_db)):
    success = report_todo_service.delete_report_todo_service(db, id)
    if not success:
        return success_response(message="Not found", status_code=404)
    return success_response(message="Deleted")