from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, CategoryResponse
from app.crud.category import get_categories, create_category
from app.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.post("/", response_model=CategoryResponse, status_code=201)
def generate_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)