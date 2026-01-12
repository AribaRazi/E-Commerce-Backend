from db import get_connection

def create_payment(order_id, payment_method, payment_status="PENDING"):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO payments (order_id, payment_method, payment_status)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (order_id, payment_method, payment_status))
    conn.commit()

    payment_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return payment_id


def get_payment_by_order_id(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT id, order_id, payment_method, payment_status
        FROM payments
        WHERE order_id = %s
    """
    cursor.execute(query, (order_id,))
    payment = cursor.fetchone()

    cursor.close()
    conn.close()

    return payment


def update_payment_status(payment_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE payments
        SET payment_status = %s
        WHERE id = %s
    """
    cursor.execute(query, (status, payment_id))
    conn.commit()

    cursor.close()
    conn.close()

    return True
