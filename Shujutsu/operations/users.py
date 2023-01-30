from fastapi import APIRouter, HTTPException, Depends
from schema import schema
from methods.errors import format
from database.usertable import UserLoginTable
from methods.auth import AuthHandler


auth = AuthHandler()
PROTECTED = [Depends(auth.decode_token)]

userlogin = APIRouter(tags=["userlogin"], prefix="/login")
user = APIRouter(tags=["user"], prefix="/user")
register = APIRouter(tags=["register"], prefix="/register")
new_user = APIRouter(tags=["new_user"], prefix="/user_info", dependencies=PROTECTED)


@register.post("")
def register_user(data: schema.Register):
    data = dict(data)
    table = UserLoginTable(data)
    data.update({"token": ""})
    verify_email = table.check_email()
    if verify_email:
        detail = "Email already registered"
        raise HTTPException(status_code=404, detail=detail)
    response = table.insert()
    if not response:
        msg = "Unable to insert"
        type = "Acknowledge error"
        fun = "register_user"
        return format(msg, type, fun)
    return {"status": True}

@userlogin.post("")
async def user_login(data: schema.UserLogin):
    data = data.dict()
    email = data["email"]
    password = data["password"]
    user_info = {
        "email": email,
        "password": password
    }
    verify_login = auth.authenticate_user(email, password)
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
