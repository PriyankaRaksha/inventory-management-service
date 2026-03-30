from fastapi import APIRouter

router = APIRouter()

products = []

@router.post("/products")
def create_product(name:str, quantity:int):

    product = {
        "name": name,
        "quantity": quantity
    }

    products.append(product)

    return product