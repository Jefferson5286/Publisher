from exceptions.database import PermissionLevelNotAccept
from config import env
from .connection import cache

from motor.motor_asyncio import AsyncIOMotorDatabase


async def clear_db(database: AsyncIOMotorDatabase) -> None:
    """
        Limpa o banco de dados. Usado somente para testes. Levanta o erro 'PermissionLevelNotAccept' caso o nível
    não seja equivalente.

    :param database: Uma instância AsyncIOMotorDatabase, com o banco de dados alvo.
    """

    if env.LEVEL not in ('TEST', 'DEBUG'):
        raise PermissionLevelNotAccept()

    collections = await database.list_collection_names()

    for collection in collections:
        await database.get_collection(collection).drop()

    async with cache as _:
        items = await _.keys()

        await _.delete(*items)
