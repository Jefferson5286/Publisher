from json import loads

from schemas.user import UserSchema
from services.user import create_user_account
from exceptions.user import UserAlreadyRegisterError, EmailAlreadyRegisterError

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post('/account/create')
async def create_user(data: UserSchema) -> JSONResponse:
    try:
        response = await create_user_account(
            username=data.username,
            password=data.password,
            name=data.name,
            surname=data.surname,
            phone=data.phone,
            email=data.email,
            sex=data.sex,
            birth_date=data.birth_date
        )

        return JSONResponse(loads(response.model_dump_json()), status_code=200)

    except UserAlreadyRegisterError:
        raise HTTPException(detail=f'Username <{data.username}> already registered', status_code=409)

    except EmailAlreadyRegisterError:
        raise HTTPException(detail=f'Email <{data.email} already registered', status_code=409)
