from pydantic import BaseModel, constr, validator, ValidationError
from typing import Optional
import re

class UserLogin(BaseModel):
    userid: str
    password: str

class Register(BaseModel):
    userid: str
    password: str
    confirm_password: str

    @validator('confirm_password')
    def validate_password(cls, v, values, **kwargs):
        print(values, v)
        if 'password' in values and v != values["password"]:
            raise ValueError('password did not match')
        return v


class CreateOrg(BaseModel):
    name: str
    members: Optional[list]

class Members(BaseModel):
    org: str
    members: list

class Tasks(BaseModel):
    title: str
    description: str
    assigned_to: str
    status: str
    org: str
    created_at: str

class UpdateTask(BaseModel):
    org: str
    task_id: str
    description: str
    status: str
    updated_by: str
    updated_at:str
