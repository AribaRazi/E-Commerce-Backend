from db import get_connection
def create_user(name,email,password_hash):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
            INSERT INTO USERS(name,email,password_hash)
            VALUES(%s,%s,%s)
            """
    cursor.execute(query,(name,email,password_hash))
    conn.commit()

    cursor.close()
    conn.close()

    return cursor.lastrowid

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_id(user_id):
    conn=get_connection()
    cursor=conn.cursor()

    query="select * from users where id=%s"
    cursor.execute(query,(user_id,))

    user=cursor.fetchone()

    cursor.close()
    conn.close()

    return user

