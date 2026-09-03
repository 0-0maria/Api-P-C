from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.crud.product import get_products, create_product
from app.crud.category import get_category
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/", response_model=ProductResponse, status_code=201)
def generate_product(product: ProductCreate, db: Session = Depends(get_db)):
    category = get_category(db, product.categoria_id)
    if not category:
        raise HTTPException(status_code=404, detail="La categoría especificada no existe")
    return create_product(db, product)