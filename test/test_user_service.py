from database.testing import clear_db
from database.connection import database

from httpx import AsyncClient
from pytest import mark


@mark.asyncio
async def test_create_user(client: AsyncClient) -> None:
    await clear_db(database.client['Publisher'])

    content = {
        'password': '1000',
        'email': 'exemple@email.com'
    }

    response = await client.post('/v1/account/create', json=content)

    assert response.status_code == 200
