from models.product_model import (
    get_all_products as get_all_products_model,
    get_product_by_id as get_product_by_id_model
)

def fetch_all_products():
    return get_all_products_model()


def fetch_product_by_id(product_id):
    if product_id <= 0:
        raise ValueError("Invalid product ID")

    product = get_product_by_id_model(product_id)

    if not product:
        raise Exception("Product not found")

    return product


def check_stock(product_id, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    product = get_product_by_id_model(product_id)

    if not product:
        raise Exception("Product not found")

    _, stock = product

    if stock < quantity:
        raise Exception("Insufficient stock")

    return True
