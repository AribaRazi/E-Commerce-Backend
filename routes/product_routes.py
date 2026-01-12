from flask import Blueprint,jsonify
from services.product_service import fetch_all_products,fetch_product_by_id

product_bp=Blueprint("products",__name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = fetch_all_products()
    return jsonify(products)

@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = fetch_product_by_id(product_id)
    return jsonify(product)