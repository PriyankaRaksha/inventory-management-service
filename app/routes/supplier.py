from fastapi import APIRouter

router = APIRouter()

@router.post("/suppliers")

def add_supplier(name:str):

    return {
        "supplier": name,
        "status": "added"
    }