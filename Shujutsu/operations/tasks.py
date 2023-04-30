from fastapi import APIRouter, HTTPException, Depends
from schema import schema
from database.connection import Tasks
from methods.auth import AuthHandler

auth = AuthHandler()
PROTECTED = [Depends(auth.decode_token)]

tasks = APIRouter(tags=["tasks"], prefix="/tasks", dependencies=PROTECTED)

@tasks.post("/create_task")
def create_task(
            data: schema.Tasks,
            userid: schema.UserLogin=Depends(auth.decode_token)):
    data = data.dict()
    data["created_by"] = userid
    insert_task = Tasks.insert_one(data)
    if insert_task is not None:
        return {"_id": insert_task.inserted_id}
    return {"_id": False}

@tasks.post("/update_task")
def update_task(data: )