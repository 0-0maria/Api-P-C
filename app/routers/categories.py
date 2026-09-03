from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, CategoryResponse
from app.crud.category import get_categories, get_category, create_category, update_category, delete_category
from app.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

@router.post("/", response_model=CategoryResponse, status_code=201)
def generate_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.put("/{category_id}", response_model=CategoryResponse)
def modify_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    updated = update_category(db, category_id, category)
    if not updated:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return updated

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_category(category_id: int, db: Session = Depends(get_db)):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return None