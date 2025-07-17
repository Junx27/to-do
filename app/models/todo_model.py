from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)

class StatusTodo(Base):
    __tablename__ = "status_todos"
    
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)

    todo_id = Column(Integer, ForeignKey("todos.id"))

