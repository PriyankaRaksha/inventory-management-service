def update_stock(product_id, quantity):
    product = db.get(product_id)

    product.stock -= quantity

    return product