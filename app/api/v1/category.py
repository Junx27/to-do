from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.category_schema  import CategoryCrate, CategoryOut
from app.services import category_service
from app.utils.response import success_response

router = APIRouter()

@router.post("/category")
def create_category(category: CategoryCrate, db: Session = Depends(get_db)):
    result = category_service.create_category_service(db, category)
    return success_response(data=CategoryOut.model_validate(result).model_dump(), message="OK", status_code=201)

@router.get("/category")
def get_all_category(db: Session = Depends(get_db)):
    category = category_service.get_all_category_service(db)
    return success_response(data=[CategoryOut.model_validate(t).model_dump() for t in category])

@router.get("/category/{id}")
def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = category_service.get_category_by_id_service(db, id)
    if not category:
        return success_response(message="Not found", status_code=404)
    return success_response(data=CategoryOut.model_validate(category).model_dump())

@router.put("/category/{id}")
def update_category(id: int, data: CategoryCrate, db: Session = Depends(get_db)):
    result = category_service.update_category_service(db, id, data)
    if not result:
        return success_response(message="Not found", status_code=404)
    return success_response(data=CategoryOut.model_validate(result).model_dump(), message="OK")

@router.delete("/category/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    success = category_service.delete_category_service(db, id)
    if not success:
        return success_response(message="Not found", status_code=404)
    return success_response(message="Deleted")