from decouple import config


class Config:
    MONGODB_URL = config('MONGODB_URL')

    LEVEL = config('LEVEL')

    REDIS_PASSWORD = config('REDIS_PASSWORD')
    REDIS_ENDPOINT = config('REDIS_ENDPOINT')
    REDIS_DATABASE = config('REDIS_DATABASE')
    REDIS_USERNAME = config('REDIS_USERNAME')


env: Config = Config()
