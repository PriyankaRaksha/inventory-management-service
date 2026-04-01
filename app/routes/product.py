from fastapi import APIRouter
from app.services.product_service import add_product

router = APIRouter()

products = []

@router.post("/products")
@router.post("/products")

def create_product(name:str,quantity:int):

    return add_product(name,quantity)