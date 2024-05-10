from uuid import uuid4
from datetime import datetime
from types import NoneType

from database.schemas.user import UserModel
from database.connection import database
from exceptions.user import UserAlreadyRegisterError, EmailAlreadyRegisterError

from argon2 import PasswordHasher


async def create_user_account(**data: str | NoneType) -> UserModel:
    exists = await database.engine.find_one(
        UserModel,
        (UserModel.username == data['username']) | (UserModel.email == data['email'])
    )

    if exists:
        if exists.username is not None:
            raise UserAlreadyRegisterError()

        if exists.email is not None:
            raise EmailAlreadyRegisterError()

    hasher = PasswordHasher()
    password = hasher.hash(data.get('password', ''))

    user = UserModel(
        username=data.get('username', f'user-{uuid4()}'),
        password=password,
        email=data['email'],
        name=data.get('name', None),
        surname=data.get('surname', None),
        sex=data.get('sex', None),
        phone=data.get('phone', None),
        birth_date=data.get('birth_date', None),
        account_creation_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    response = await database.engine.save(user)

    return response
