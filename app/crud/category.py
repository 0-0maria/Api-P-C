from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, category: CategoryCreate):
    new_category = Category(
        nombre=category.nombre,
        estado=category.estado
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category