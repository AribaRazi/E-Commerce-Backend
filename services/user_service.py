from models.user_model import (
    create_user as create_user_model,
    get_user_by_email as get_user_by_email_model,
    get_user_by_id as get_user_by_id_model
)

def register_user(name, email, password):
    if not email:
        raise ValueError("Invalid email")

    if not password:
        raise ValueError("Password cannot be empty")

    return create_user_model(name, email, password)


def fetch_user_by_email(email):
    if not email:
        raise ValueError("Invalid email")

    user = get_user_by_email_model(email)

    if not user:
        raise Exception("User not found")

    return user


def fetch_user_by_id(user_id):
    if user_id <= 0:
        raise ValueError("Invalid user_id")

    user = get_user_by_id_model(user_id)

    if not user:
        raise Exception("User not found")

    return user
