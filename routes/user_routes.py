from flask import Blueprint, jsonify, request
from services.user_service import (
    register_user,
    fetch_user_by_email,
    fetch_user_by_id
)

user_bp = Blueprint("users", __name__)

# creating user
@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Invalid user details"}), 400

    user_id = register_user(name, email, password)

    return jsonify({
        "success": True,
        "data": {
            "user_id": user_id
        },
        "error": None
    }), 201


# get user by id
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = fetch_user_by_id(user_id)

    return jsonify({
        "success": True,
        "data": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        },
        "error": None
    })



# get user by email
@user_bp.route("/users/email/<string:user_email>", methods=["GET"])
def get_user_email(user_email):
    user = fetch_user_by_email(user_email)

    return jsonify({
        "success": True,
        "data": {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        },
        "error": None
    })
