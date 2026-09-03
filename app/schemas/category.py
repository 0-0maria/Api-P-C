from pydantic import BaseModel

class CategoryBase(BaseModel):
    nombre: str
    estado: bool = True

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True