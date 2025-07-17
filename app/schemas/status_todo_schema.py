from pydantic import BaseModel

class StatusTodoCreate(BaseModel):
    status: str
    todo_id: int

class StatusTodoOut(BaseModel):
    id: int
    status: str
    todo_id: int

    model_config = {
        "from_attributes": True
    }