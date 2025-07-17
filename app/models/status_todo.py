from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class StatusTodo(Base):
    __tablename__ = "status_todos"
    
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)

    todo_id = Column(Integer, ForeignKey("todos.id"))