def update_stock(product_id, quantity):
    product = db.get(product_id)

    if product.stock < quantity:
        raise Exception("Insufficient stock")

    product.stock -= quantity

    return product

def fetch_stock_history(product_id):
    return db.query(
        "SELECT * FROM stock_history WHERE product_id=%s",
        product_id
    )