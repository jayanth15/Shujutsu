from fastapi import FastAPI
from operations import users

app = FastAPI()

app.include_router(users.register)
app.include_router(users.userlogin)
app.include_router(users.new_user)

@app.get("/base")
def get_data():
    return {"Shujutsu": "Working"}