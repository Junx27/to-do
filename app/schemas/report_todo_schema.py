from pydantic import BaseModel

class ReportTodoCreate(BaseModel):
    percentage: int
    todo_id: int

class ReportTodoOut(BaseModel):
    id: int
    percentage: int
    todo_id: int

    model_config = {
        "from_attributes": True
    }