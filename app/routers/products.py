from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.crud.product import get_products, get_product, create_product, update_product, delete_product
from app.crud.category import get_category
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.post("/", response_model=ProductResponse, status_code=201)
def generate_product(product: ProductCreate, db: Session = Depends(get_db)):
    category = get_category(db, product.categoria_id)
    if not category:
        raise HTTPException(status_code=404, detail="La categoría especificada no existe")
    return create_product(db, product)

@router.put("/{product_id}", response_model=ProductResponse)
def modify_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    category = get_category(db, product.categoria_id)
    if not category:
        raise HTTPException(status_code=404, detail="La categoría especificada no existe")
    updated = update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(product_id: int, db: Session = Depends(get_db)):
    deleted = delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None