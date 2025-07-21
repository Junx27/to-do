from sqlalchemy.orm import Session
from app.models.report_todo_model import ReportTodo

def create_report_todo(db: Session, percentage: int, todo_id: int):
    report_todo = ReportTodo(percentage=percentage, todo_id=todo_id)
    db.add(report_todo)
    db.commit()
    db.refresh(report_todo)
    return report_todo

def get_all_report_todo(db: Session):
    return db.query(ReportTodo).all()

def get_report_todo_by_id(db: Session, report_todo_id: int):
    return db.query(ReportTodo).filter(ReportTodo.id == report_todo_id).first()

def update_report_todo(db: Session, report_todo: ReportTodo, percentage: int, todo_id: int):
    report_todo.percentage = percentage
    report_todo.todo_id = todo_id
    db.commit()
    db.refresh(report_todo)
    return report_todo

def delete_report_todo(db: Session, report_todo: ReportTodo):
    db.delete(report_todo)
    db.commit()