from db.database import db
from bson import ObjectId

user_collection = db.users

user_schema = {
    "name": {"type": "string", "required": True},
    "email": {"type": "string", "required": True, "unique": True},
    "password": {"type": "string", "required": True}
}