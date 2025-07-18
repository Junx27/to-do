from pydantic import BaseModel

class CategoryCrate(BaseModel):
    name: str


class CategoryOut(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }