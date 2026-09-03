from pydantic import BaseModel
from app.schemas.category import CategoryResponse

class ProductBase(BaseModel):
    codigo: str
    nombre: str
    precio: float
    stock: int
    categoria_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    category: CategoryResponse

    class Config:
        from_attributes = True