from models.payment_model import (
    create_payment,
    get_payment_by_order_id,
    update_payment_status
)

def initiate_payment(order_id, payment_method):
    if not order_id or order_id <= 0:
        raise ValueError("Invalid order ID")

    if not payment_method:
        raise ValueError("Payment method is required")

    payment_id = create_payment(
        order_id=order_id,
        payment_method=payment_method,
        payment_status="PENDING"
    )

    return payment_id


def fetch_payment_by_order(order_id):
    if order_id <= 0:
        raise ValueError("Invalid order ID")

    return get_payment_by_order_id(order_id)


def change_payment_status(payment_id, status):
    if status not in ["SUCCESS", "FAILED"]:
        raise ValueError("Invalid payment status")

    update_payment_status(payment_id, status)
    return True
