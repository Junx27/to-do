from pydantic import BaseModel

class TodoCreate(BaseModel):
    name: str
    description: str | None = None

class TodoOut(TodoCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
