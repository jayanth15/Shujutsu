import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from database import connection
from schema.schema import UserLogin
from datetime import datetime

UserLoginTable = connection.UserLogin


class AuthHandler():
    security = HTTPBearer()
    TEAM_SECRET = "Kaijin"
    username = None

    async def encode_token(self, user_info):
        username = user_info["email"]
        password = user_info["password"]
        payload = {
            "time": datetime.now().strftime("%y_%m_%d_%H_%M_%S"),
            "username": username,
            "password": password
        }
        token = jwt.encode(
            payload,
            self.TEAM_SECRET,
            algorithm="HS256"
        )
        verify_user = self.authenticate_user(username, password)
        if not verify_user:
            detail = {
                "error": "Invalid Authentication"
            }
            raise HTTPException(status_code=401, detail=detail)
        condition = {
            "email": username
        }
        set_token = {
            "$set": {
                "token": token
            }
        }
        insert_token = UserLoginTable.update_one(condition, set_token)
        if not insert_token.acknowledged:
            detail = "Unable to insert token into UserLogin Table"
            raise HTTPException(status_code=401, detail=detail)
        return token

    async def authenticate_user(self, email, password):
        email = {
            "email": email
        }
        result = UserLoginTable.find_one(email)
        if result and result["password"] == password:
            return result
        return False

    async def decode_token(self, credentials: UserLogin = Depends(security)):
        token = credentials.credentials
        try:
            payload = jwt.decode(token, self.TEAM_SECRET, algorithms=["HS256"])
            username = payload["username"]
            self.username = username
            password = payload["password"]
            if not await self.authenticate_user(username, password):
                raise HTTPException(status_code=401, detail={
                                    "error": "invalid username/password"})
            if not self.verify_token(username, token):
                raise HTTPException(status_code=401, detail={
                                    "error": "Unable to find username/token"})
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail={
                                "error": "Invalid token"})
        return username

    def check_login(self, token):
        print(token)
        return token

    def verify_token(self, username, token):
        # token = token.encode("utf-8")
        condition = {
            "$or": [{"phone": username}, {"email": username}],
            "token": token
        }
        find_token = UserLoginTable.find_one(condition)
        if not find_token:
            raise HTTPException(status_code=401, detail={
                                "error": "Invalid token"})
        return True
