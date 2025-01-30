from flask import jsonify, request
from models.user_model import user_collection
from bson import ObjectId

def get_users():
    users = list(user_collection.find({}, {"password": 0}))

    # Convert `_id` to string for JSON serialization
    for user in users:
        user["id"] = str(user.pop("_id"))

    return jsonify(users)

def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    if user:
        user["id"] = str(user.pop("_id"))
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

def create_user():
    data = request.json
    
    if "email" in data:
        existing_user = user_collection.find_one({"email": data["email"]})

        if existing_user:
            return jsonify({"error": "A user with the same email is present"}), 400

    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    user_collection.insert_one(data)
    return jsonify({"message": "User created"}), 201

def update_user(user_id):
    data = request.json

    if data.get("email"):  # Check if email exists in request
        existing_user = user_collection.find_one({"email": data["email"], "_id": {"$ne": ObjectId(user_id)}})
        if existing_user:
            return jsonify({"error": "A user with the same email is present"}), 400

    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return jsonify({"message": "User updated"})

def delete_user(user_id):
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return jsonify({"message": "User deleted"})
