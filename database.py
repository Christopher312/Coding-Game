MONGODB_URI = 'mongodb://heroku_mkt3h9sk:heirlr5tqt4cchtstvsld3di12@ds059185.mongolab.com:59185/heroku_mkt3h9sk' 

from pymongo import MongoClient
client = MongoClient(MONGODB_URI)
#client = MongoClient()
#db = client.codemon
#users = db.users

db = client.get_default_database()
users = db['users']

def userExists(email):
    return users.find({"email": email}).count() > 0

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