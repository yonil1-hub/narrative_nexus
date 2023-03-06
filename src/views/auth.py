#!/usr/bin/python3
"""User Authentication Module
"""


from flask import Blueprint, request, jsonify
from json import dumps
from  models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError
from flask_jwt_extended import jwt_required
users_bp = Blueprint("users", __name__)

@users_bp.route("/api/users/create", methods=["POST"])
def create_user():
    """
    Creates a new User with the provided data.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error":"Not a Valid JSON"}), 400

    # Unpack the data
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    name = data.get("name")
    bio = data.get("bio")

    # Validation
    if not all([username, password, email]):
        return jsonify({"error": "Missing required data"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify ({"error":"Username is taken"}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({"error":"User with the same email detected"}), 409
    else:
        try:
            validation = validate_email(email, check_deliverability=True)
            email = validation.email
        except EmailNotValidError as e:
            return jsonify({"error": str(e)})
    
    if len(username) <= 3 and len(username) >= 20:
        return jsonify({"error":"Username must be between 4-20 characters"}), 400

    if len(password) < 8:
        return jsonify({"error":"Weak Password detected"}), 400

    # Create the User in database
    try:
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, email=email, name=name, bio=bio)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": e}), 500


    return jsonify({"message": "User created successfully"}), 201

@users_bp.route("/api/users/login", methods=["GET"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error":"Not a Valid JSON"}), 400
    
    # Unpack the data
    email = data.get("email")
    password = data.get("password")
    if not email:
        return jsonify({"error": "Missing Email"}), 400
    if not password:
        return jsonify({"error": "Missing Password"})

    user = User.query.filter_by(email=email).first()

    # Verify the user
    if user:
        if check_password_hash(user.password, password):
            return jsonify({"msg": "User verified"}), 200
        else:
            return jsonify({"error":"wrong password"}), 400
    else:
        return jsonify({"error":"User not found"}), 404

@users_bp.route("/api/users/logout", methods=["POST"])
def logout():
    """
    """
    pass

