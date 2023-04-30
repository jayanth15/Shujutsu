import pymongo

cluster = pymongo.MongoClient('mongodb://localhost:27017/')
db = cluster["Shujutsu"]
Users = db["Users"]
UserLogin = db["UserLogin"]
Teams = db["Teams"]
Org = db["Org"]
UserOrg = db["UerOrg"]
Tasks = db["Tasks"]
