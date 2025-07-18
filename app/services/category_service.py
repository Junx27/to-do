from sqlalchemy.orm import Session
from app.repository import category_repo
from app.schemas.category_schema import CategoryCrate

def create_category_service(db: Session, categpry_in: CategoryCrate):
    return category_repo.create_category(db, categpry_in.name)

def get_all_category_service(db: Session):
    return category_repo.get_all_category(db)

def get_category_by_id_service(db: Session, category_id: int):
    return category_repo.get_category_by_id(db, category_id)

def update_category_service(db: Session, category_id: int, data: CategoryCrate):
    category = category_repo.get_category_by_id(db, category_id)
    if not category:
        return None
    return category_repo.update_category(db, category, data.name)

def delete_category_service(db: Session, categpry_id: int):
    category = category_repo.get_category_by_id(db, categpry_id)
    if not category:
        return False
    category_repo.delete_category(db, category)
    return True