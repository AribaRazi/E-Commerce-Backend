# routes dont handle errors / errors are handled by services
from flask import Blueprint, jsonify, request
from services.order_service import place_order

order_bp = Blueprint("orders", __name__)

# creating order
@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    user_id = data.get("user_id")
    items = data.get("items")

    if not user_id or not items:
        return jsonify({"error": "Invalid order data"}), 400

    order_id = place_order(user_id, items)

    return jsonify({
        "success": True,
        "data": {
            "order_id": order_id
        },
        "error": None
    }), 201

