from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.report_todo_schema import ReportTodoCreate, ReportTodoOut
from app.services import report_todo_service
from utils.response import success_response

router = APIRouter()

@router.post("/report-todo")
def create_report_todo(report_todo: ReportTodoCreate, db: Session = Depends(get_db)):
    result = report_todo_service.create_report_todo_service(db, report_todo)
    return success_response(data=ReportTodoOut.model_validate(result).model_dump(), message="OK")

@router.get("report-todo")
def get_all_report_todo(db: Session = Depends(get_db)):
    report_todos = report_todo_service.get_all_report_todo_service(db)
    return success_response(data=[ReportTodoOut.model_validate(t).model_dump() for t in report_todos])

