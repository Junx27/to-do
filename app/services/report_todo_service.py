from sqlalchemy.orm import Session
from app.repository import report_todo_repo
from app.schemas.report_todo_schema import ReportTodoCreate, ReportTodoOut

def create_report_todo_service(db: Session, report_todo_in: ReportTodoCreate):
    return report_todo_repo.create_report_todo(db, report_todo_in.percentage, report_todo_in.todo_id)

def get_all_report_todo_service(db: Session):
    return report_todo_repo.get_all_report_todo(db)

def get_report_todo_by_id_service(db: Session, report_todo_id: int):
    return report_todo_repo.get_report_todo_by_id(db, report_todo_id)

def update_report_todo_service(db: Session, report_todo_id: int, data: ReportTodoCreate):
    report_todo = report_todo_repo.get_report_todo_by_id(db, report_todo_id)
    if not report_todo:
        return None
    return report_todo_repo.update_report_todo(db, report_todo, data.percentage, data.todo_id)

def delete_report_todo_service(db: Session, report_todo_id: int):
    report_todo = report_todo_repo.get_report_todo_by_id(db, report_todo_id)
    if not report_todo:
        return False
    report_todo_repo.delete_report_todo(db, report_todo)
    return True