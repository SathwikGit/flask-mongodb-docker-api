from pymongo import MongoClient

url = "mongodb://mongo:27017/StudentList"

# //whenever we import from this file this connection is made
# //so it is made at the start only
client = MongoClient(url)
db = client.get_database()

def get_db():
    return db