from pydantic import BaseModel, EmailStr, constr

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from pydantic import StringConstraints


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(max_length=72)]