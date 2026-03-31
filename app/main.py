from fastapi import FastAPI
from app.routes import product

app = FastAPI()

app.include_router(product.router)

@app.get("/")
def home():
    return {"message": "Inventory Management Service Running"}

@app.get("/health")
def health():
    return {"status":"ok"}