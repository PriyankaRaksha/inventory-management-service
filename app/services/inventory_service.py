def update_stock(id, qty):
    product = db.get(id)
    product.stock -= qty
    return product