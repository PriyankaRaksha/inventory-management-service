from fastapi import APIRouter

router = APIRouter()

@router.post("/orders")

def create_order(product:str,quantity:int):

    return {
        "product":product,
        "quantity":quantity,
        "status":"order placed"
    }