from db import get_connection
def get_all_products():
    conn=get_connection()
    cursor=conn.cursor()

    query="""
        select * from products"""
    cursor.execute(query)

    products=cursor.fetchall()
    cursor.close()
    conn.close()

    return products

def get_product_by_id(product_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
 
    query="""
        select * from products where id=%s
            """
    cursor.execute(query,(product_id,))
    
    products=cursor.fetchone()

    cursor.close()
    conn.close()

    return products

def update_stock(product_id,new_stock):
    conn=get_connection()
    cursor=conn.cursor()
 
    query="""
        update products SET stock=%s Where id=%s
            """
    cursor.execute(query,(new_stock,product_id))
    conn.commit()


    conn.close()
    cursor.close()
    return True