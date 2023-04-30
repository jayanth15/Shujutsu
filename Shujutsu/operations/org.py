from fastapi import APIRouter, HTTPException, Depends
from schema import schema
from database.connection import Org, UserOrg
from methods.auth import AuthHandler

auth = AuthHandler()
PROTECTED = [Depends(auth.decode_token)]

teams = APIRouter(tags=["org"], prefix="/org", dependencies=PROTECTED)

@teams.post("/create_org")
def create_org(
            data: schema.CreateOrg,
            userid: schema.UserLogin=Depends(auth.decode_token)):
    find_org = Org.find_one({"name": data.name})
    if find_org is None:
        insert_data = {
            "name": data.name,
            "created_by": userid,
            "members": data.members
        }
        for member in data.members:
            find_user_orgs = UserOrg.find_one({"userid": member})
            user_data = {
                "userid": member,
                "org":[data.name]
            }
            if find_user_orgs is not None:
                find_user_orgs["org"].append(data.name)
            UserOrg.update_one(
                {"userid": member},
                {"$set": user_data},
                {"upsert": True}
                )
        insert_org = Org.insert_one(insert_data)
        return {"_id": insert_org.inserted_id}
    return {"_id": False}

@teams.get("/get_org")
def list_org(userid: schema.UserLogin=Depends(auth.decode_token)):
    get_orgs = UserOrg.find_one({"userid": userid.userid})
    orginizations = []
    for org in get_orgs["org"]:
        orginizations.append(org)
    return {"orginizations": orginizations}

@teams.post("/add_members")
def add_members(
            data: schema.Members,
            userid: schema.UserLogin=Depends(auth.decode_token)):
    find_org = Org.find_one({"org": data.org})
    if find_org is not None and find_org["created_by"] == userid:
        members = find_org["members"]
        for mem in data.members:
            if mem not in members:
                members.append(mem)
        insert_members = Org.update_one({"org": data.org}, {"members": members})
        if insert_members.modified_count == 0:
            return {"status": False}
    return {"status": True}

@teams.post('/remove_members')
def remove_members(
            data: schema.Members,
            email: schema.UserLogin=Depends(auth.decode_token)):
    members = data.members
    condition = {
        "org": data.org
    }
    orginization = Org.find_one(condition)
    existing_members = orginization["members"]
    for index, member in enumerate(existing_members):
        if member in members:
            existing_members.pop(index)
    insert_condition = {
        "$set": {
                    "members": existing_members,
                    "added_by": email
                }
    }
    results = Org.update_one(condition, insert_condition)
    if results.modified_count == 1:
        return {"status": True}
    return {"status": False}
