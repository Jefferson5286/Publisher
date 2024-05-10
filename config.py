from decouple import config


class Config:
    DATABASE_URL = config('DATABASE_URL')
    LEVEL = config('LEVEL')


env: Config = Config()
