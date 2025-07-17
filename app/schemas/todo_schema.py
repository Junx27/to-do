from pydantic import BaseModel

class TodoCreate(BaseModel):
    name: str
    description: str | None = None

class TodoOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = {
        "from_attributes": True
    }
