from pymongo import MongoClient
client = MongoClient()
db = client.codemon
users = db.users

def insertUser(username):
    users.insert(
        {"username": username, "codemon": {"exp": 0}}
    )

def addExperience(username, amount):
    users.update_one(
        {"username": username},
        {"$inc": {"codemon.exp": amount}}
    )
