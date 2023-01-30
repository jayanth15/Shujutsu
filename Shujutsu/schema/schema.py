from pydantic import BaseModel, constr, validator, ValidationError
from typing import Optional
import re

class UserLogin(BaseModel):
    email: str
    password: str

    @validator('email')
    def validate_email(cls, v):
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(email_regex, v):
            return v
        raise ValueError('invalid email')

class Register(BaseModel):
    firstname: str
    lastname: str | None = None
    email: str
    password: str
    confirm_password: str

    @validator('confirm_password')
    def validate_password(cls, v, values, **kwargs):
        print(values, v)
        if 'password' in values and v != values["password"]:
            raise ValueError('password did not match')
        return v

    @validator('email')
    def validate_email(cls, v):
        print("Raising error here ?")
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(email_regex, v):
            print(v)
            print("DATA OF V: ", v)
            return v
        raise ValueError('invalid email')


class CreateTeam(BaseModel):
    name: str
    members: Optional[list]


class AddMembers(BaseModel):
    _id: str
    members: list