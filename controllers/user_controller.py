from flask import jsonify, request
from models.user_model import user_collection
from bson import ObjectId

def get_users():
    users = list(user_collection.find({},{"password":0}))

    # Convert `_id` to string for JSON serialization
    # actuall _id is Objectid
    for user in users:
        user["id"] = str(user.pop("_id"))

    return jsonify(users)


def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    if user:
        # Convert `_id` to string for JSON serialization
        # actuall _id is Objectid
        user["id"] = str(user.pop("_id"))
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404
    # // Return 404 for missing user

def create_user():
    data = request.json
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400
    user_collection.insert_one(data)
    return jsonify({"message": "User created"}), 201

def update_user(user_id):
    data = request.json
    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return jsonify({"message": "User updated"})

def delete_user(user_id):
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return jsonify({"message": "User deleted"})