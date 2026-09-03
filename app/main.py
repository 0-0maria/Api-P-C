from fastapi import FastAPI
from app.database import Base, engine
from app.routers import categories, products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Productos y Categorías",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"mensaje": "API de Productos y Categorías funcionando correctamente"}