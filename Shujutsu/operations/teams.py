from fastapi import APIRouter, HTTPException, Depends
from schema import schema
from methods.utils import create_id
from methods.errors import format
from database.connection import Teams
from methods.auth import AuthHandler

auth = AuthHandler()
PROTECTED = [Depends(auth.decode_token)]

teams = APIRouter(tags=["teams"], prefix="/teams", dependencies=PROTECTED)

@teams.post("/create_team")
def create_team(
            data: schema.CreateTeam,
            email: schema.UserLogin=Depends(auth.decode_token)):
    data = dict(data)
    _id = create_id()
    update = {
        "_id": _id,
        "admin": email
    }
    data.update(update)
    result = Teams.insert_one(data)
    if result.acknowledged:
        return {"status": True}
    return {"status": False}

@teams.get("/get_teams")
def list_teams(email: schema.UserLogin=Depends(auth.decode_token)):
    data = []
    condition = {
        "email": email
    }
    results = Teams.find(condition)
    results = list(results)
    for team in results:
        data.append(team["name"])
    return {"teams": data}

@teams.post("/add_members")
def add_members(
            data: schema.AddMembers,
            email: schema.UserLogin=Depends(auth.decode_token)):
    data = dict(data)
    _id = data["_id"]
    new_members = data["members"]
    condition = {
        "_id": _id
    }
    teams = Teams.find_one(condition)
    existing_members = teams["members"]
    for member in new_members:
        existing_members.append(member)
    insert_condition = {
        "$set": {
                    "members": existing_members,
                    "added_by": email
                }
    }
    results = Teams.update_one(condition, insert_condition)
    if results.acknowledged:
        return {"status": True}
    return {"status": False}

@teams.post('/remove_members')
def remove_members(
            data: schema.AddMembers,
            email: schema.UserLogin=Depends(auth.decode_token)):
    data = dict(data)
    _id = data["_id"]
    members = data["members"]
    condition = {
        "_id": _id
    }
    teams = Teams.find_one(condition)
    existing_members = teams["members"]
    for index, member in enumerate(existing_members):
        if member in members:
            existing_members.pop(index)
    insert_condition = {
        "$set": {
                    "members": existing_members,
                    "added_by": email
                }
    }
    results = Teams.update_one(condition, insert_condition)
    if results.acknowledged:
        return {"status": True}
    return {"status": False}