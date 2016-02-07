from pymongo import MongoClient
client = MongoClient("MONGOLAB_URI")
db = client.codemon
users = db.users

def userExists(email):
    return users.find({"email": email}).count > 0

def insertUser(email):
    users.insert(
        {"email": email, "codemon": {"exp": 0}}
    )

def addExperience(email, amount):
    users.update_one(
        {"email": email},
        {"$inc": {"codemon.exp": amount}}
    )

def getExperience(email):
    return users.find({"email": email})["exp"]