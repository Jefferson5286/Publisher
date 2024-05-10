from typing import Union

from bundles.enum.user import UserSexEnum

from odmantic import Model
from pydantic import constr, EmailStr


class UserModel(Model):
    username: Union[str, None] = None
    password: str
    email: EmailStr

    name: Union[str, None] = None
    surname: Union[str, None] = None

    sex: Union[UserSexEnum, None] = None
    phone: Union[str, None] = None

    account_creation_date: str
    birth_date: Union[str, None] = None
