# services/ → business logic + transactions
# transaction means All operations succeed OR everything is rolled back

from db import get_connection

def place_order(user_id, items):
    # its like a shopping cart

    conn = get_connection()
    conn.start_transaction()
    cursor = conn.cursor()

    try:
        total_amount = sum(item["quantity"] * item["price"] for item in items)

        # Creating order
        order_query = """
            INSERT INTO orders (user_id, total_amount, order_status)
            VALUES (%s, %s, %s)
        """
        cursor.execute(order_query, (user_id, total_amount, "PLACED"))
        order_id = cursor.lastrowid

        # Inserting order items & update stock
        for item in items:
            # insert order item
            cursor.execute(
                """
                INSERT INTO order_items (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, item["product_id"], item["quantity"], item["price"])
            )

            # update stock
            cursor.execute(
                """
                UPDATE products
                SET stock = stock - %s
                WHERE id = %s AND stock >= %s
                """,
                (item["quantity"], item["product_id"], item["quantity"])
            )

            if cursor.rowcount == 0:
                raise Exception("Insufficient stock")


        conn.commit()
        return order_id

    except Exception as e:
        conn.rollback()
        raise e
    
    finally:
        cursor.close()
        conn.close()
