from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class OrgCreate(BaseModel):
    organization_name: constr(min_length=3, max_length=100)# type: ignore
    email: EmailStr
    password: constr(min_length=6, max_length=512) # type: ignore


class OrgOut(BaseModel):
    organization_name: str
    email: EmailStr


class AdminLogin(BaseModel):
    email: EmailStr
    password: str