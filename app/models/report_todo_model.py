from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class ReportTodo(Base):
    __tablename__ = "report_todos"

    id = Column(Integer, primary_key=True, index=True)
    percentage = Column(Integer, nullable=False)

    todo_id = Column(Integer, ForeignKey("todos.id"))