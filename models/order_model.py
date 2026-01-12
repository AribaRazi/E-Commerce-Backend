from db import get_connection

def create_order(user_id,total_amount,order_status):
    conn=get_connection()
    cursor=conn.cursor()
 
    query="""
        INSERT INTO ORDERS(user_id, total_amount, order_status)
        VALUES
        (%s,%s,%s)
            """
    cursor.execute(query,(user_id,total_amount,order_status))
    conn.commit()
    order_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return order_id
   
def add_order_items(order_id, product_id, quantity, price):
    conn=get_connection()
    cursor=conn.cursor()
 
    query="""
        INSERT INTO ORDER_ITEMS(order_id, product_id, quantity, price)
        VALUES
        (%s,%s,%s,%s)
            """
    cursor.execute(query,(order_id, product_id, quantity, price))
    conn.commit()

    cursor.close()
    conn.close()

    return True

def get_orders_by_users(user_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
 
    query="""
        Select * from orders where user_id=%s
            """
    cursor.execute(query,(user_id,))
    orders=cursor.fetchall()
    cursor.close()
    conn.close()

    return orders  


