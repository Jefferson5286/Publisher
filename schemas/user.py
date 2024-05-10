from bundles.enum.user import UserSexEnum

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str = None
    password: str
    name: str = None
    surname: str = None
    email: EmailStr
    phone: str = None
    birth_date: str = None
    sex: UserSexEnum = None
