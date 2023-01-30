from bson import ObjectId

def create_id():
    _id = ObjectId()
    return str(_id)