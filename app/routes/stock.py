from fastapi import APIRouter

router = APIRouter()

@router.get("/stock")

def get_stock():

    return {
        "total_products": 20,
        "available": 18,
        "out_of_stock": 2
    }