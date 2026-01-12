from flask import Blueprint, request, jsonify
from services.payment_service import (
    initiate_payment,
    fetch_payment_by_order,
    change_payment_status
)

payment_bp = Blueprint("payments", __name__)

# creating payment
@payment_bp.route("/payments", methods=["POST"])
def create_payment():
    data = request.get_json()

    order_id = data.get("order_id")
    payment_method = data.get("payment_method")

    if not order_id or not payment_method:
        return jsonify({"error": "Invalid payment data"}), 400

    payment_id = initiate_payment(order_id, payment_method)

    return jsonify({
        "success": True,
        "data": {
            "payment_id": payment_id,
            "status": "PENDING"
        },
        "error": None
    }), 201


# get payment by order
@payment_bp.route("/payments/order/<int:order_id>", methods=["GET"])
def get_payment(order_id):
    payment = fetch_payment_by_order(order_id)

    return jsonify({
        "success": True,
        "data": {
            "payment_id": payment[0],
            "order_id": payment[1],
            "payment_method": payment[2],
            "payment_status": payment[3]
        },
        "error": None
    })


# update payment
@payment_bp.route("/payments/<int:payment_id>", methods=["PATCH"])
def update_payment(payment_id):
    data = request.get_json()
    status = data.get("status")

    if not status:
        return jsonify({"error": "Status is required"}), 400

    change_payment_status(payment_id, status)

    return jsonify({
        "success": True,
        "data": {
            "message": "Payment status updated"
        },
        "error": None
    })
