from fastapi import APIRouter, HTTPException, Depends
from schema import schema
from methods.errors import format
from database.usertable import UserLoginTable
from methods.auth import AuthHandler
from database.connection import UserLogin

auth = AuthHandler()
PROTECTED = [Depends(auth.decode_token)]

userlogin = APIRouter(tags=["userlogin"], prefix="/login")
user = APIRouter(tags=["user"], prefix="/user")
register = APIRouter(tags=["register"], prefix="/register")
new_user = APIRouter(tags=["new_user"], prefix="/user_info", dependencies=PROTECTED)

@register.post("")
def register_user(data: schema.Register):
    find_user = UserLogin.find_one({"userid": data.userid})
    if find_user is None:
        insert_data = {
            "userid": data.userid,
            "password": data.password,
            "token": None
            }
        user = UserLogin.insert_one(insert_data)
        return {"_id": str(user.inserted_id)}
    return {"_id": False}


@userlogin.post("")
async def user_login(data: schema.UserLogin):
    data = data.dict()
    userid = data["userid"]
    password = data["password"]
    user_info = {
        "userid": userid,
        "password": password
    }
    verify_login = auth.authenticate_user(userid, password)
    if not verify_login:
        raise HTTPException(status_code=401, detail={"error": "Invalid username/passowrd"})
    token = {"token": await auth.encode_token(user_info)}
    return token

@new_user.post("")
def get_user_info(
            data: str,
            current_user: schema.UserLogin=Depends(auth.decode_token)):
    print(current_user)
    print(data)
    return {"status": True}
