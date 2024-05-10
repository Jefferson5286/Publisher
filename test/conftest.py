from main import app
from database.connection import database

from pytest_asyncio import fixture
from httpx import AsyncClient, ASGITransport

client_db = database.client.get_database('Publisher')


@fixture(scope='function')
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://localhost:8000/') as _:
        yield _
