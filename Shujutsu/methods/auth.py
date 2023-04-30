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
        username = user_info["userid"]
        password = user_info["password"]
        payload = {
            "time": datetime.now().strftime("%y_%m_%d_%H_%M_%S"),
            "userid": username,
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
            "userid": username
        }
        set_token = {
            "$set": {
                "token": token
            }
        }
        insert_token = UserLoginTable.update_one(condition, set_token)
        if insert_token.modified_count == 0:
            detail = "Unable to insert token into UserLogin Table"
            raise HTTPException(status_code=401, detail=detail)
        return token

    async def authenticate_user(self, userid, password):
        userid = {
            "userid": userid
        }
        result = UserLoginTable.find_one(userid)
        if result and result["password"] == password:
            return result
        return False

    async def decode_token(self, credentials: UserLogin = Depends(security)):
        token = credentials.credentials
        try:
            payload = jwt.decode(token, self.TEAM_SECRET, algorithms=["HS256"])
            userid = payload["userid"]
            self.username = userid
            password = payload["password"]
            if not await self.authenticate_user(userid, password):
                raise HTTPException(status_code=401, detail={
                                    "error": "invalid username/password"})
            if not self.verify_token(userid, token):
                raise HTTPException(status_code=401, detail={
                                    "error": "Unable to find username/token"})
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail={
                                "error": "Invalid token"})
        return userid

    def check_login(self, token):
        print(token)
        return token

    def verify_token(self, userid, token):
        # token = token.encode("utf-8")
        condition = {
            "userid": userid,
            "token": token
        }
        find_token = UserLoginTable.find_one(condition)
        if not find_token:
            raise HTTPException(status_code=401, detail={
                                "error": "Invalid token"})
        return True
