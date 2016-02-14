from pymongo import MongoClient

MONGODB_URI = 'mongodb://heroku_mkt3h9sk:heirlr5tqt4cchtstvsld3di12@ds059185.mongolab.com:59185/heroku_mkt3h9sk' 
client = MongoClient(MONGODB_URI)
db = client.get_default_database()
users = db['users']
'''
client = MongoClient()
db = client.codemon
users = db.users
'''
def userExists(userid):
    return users.find({"userid": userid}).count() > 0
    
def insertUser(userid):
    print(userid)
    users.insert(
        {"userid": userid, "codemon": {"exp": 0}}
    )

def addExperience(userid, amount):
    users.update_one(
        {"userid": userid},
        {"$inc": {"codemon.exp": amount}}
    )

def getExperience(userid):
    return users.find_one({"userid": userid})["codemon"]["exp"]