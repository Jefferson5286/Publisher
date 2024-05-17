from typing import Literal, Dict, AnyStr

from config import env

from odmantic.engine import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from redis.asyncio.client import Redis


class Database:
    engine: AIOEngine
    client: AsyncIOMotorClient
    level: Literal['DEBUG', 'TEST', 'RELEASE']

    def __init__(self,
                 database_name: AnyStr,
                 url: Dict[Literal['DEBUG', 'TEST', 'RELEASE'], AnyStr],
                 level: Literal['DEBUG', 'TEST', 'RELEASE'] = 'DEBUG'):
        """
            Responsável por lidar com o controle de carregamento e gerenciamento do mando de dados.

        :param database_name: Nome do banco de dados.

        :param url: Defina a URL para conexão. É um dict contendo alternativa para cada level.

        :param level: Level de conexão com banco de dados.

            TEST:
                Carrega um banco de Dados dedicado a testes unitários. Limpa o banco a dada execução. Não existem
            restrições no uso da função de limpar o banco de dados durante execução.

            DEBUG:
                Level onde a conexão é feita, o banco é limpo durante cada execução. E sem proteção do uso do método
            que limpa o banco de dados. Conecta a um banco de dados para fins de desenvolvimento.

            RELEASE:
                O Banco é conectado, existe restrição total ao usa da função de limpeza de banco. Dados persistentes.
        """

        if all([value not in url.keys() for value in ('TEST', 'DEBUG', 'RELEASE')]):
            raise Exception("o parâmetro key, deve ser um objeto com as key: ('TEST', 'DEBUG', 'RELEASE')")

        self.level = level

        self.database_name = database_name
        self.url = url

        self._first_load_engine = True
        self._first_load_client = True

        self.load_client()
        self.load_engine()

    def load_client(self):
        """Carrega o banco de dados"""

        self.client = AsyncIOMotorClient(self.url[self.level])

    def load_engine(self):
        """Carrega a engine do banco de dados"""

        self.engine = AIOEngine(self.client, self.database_name)


database_url: Dict[Literal['DEBUG', 'TEST', 'RELEASE'], AnyStr] = {
    'TEST': 'mongodb://localhost:27017/',
    'DEBUG': 'mongodb://localhost:27017/',
    'RELEASE': env.MONGODB_URL
}


database = Database('Publisher', database_url, env.LEVEL)
cache = Redis.from_url(f'redis://{env.REDIS_USERNAME}:{env.REDIS_PASSWORD}@{env.REDIS_ENDPOINT}/0')
