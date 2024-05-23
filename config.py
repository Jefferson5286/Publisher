from decouple import config


class Config:
    MONGODB_URL = config('MONGODB_URL')

    LEVEL = config('LEVEL')

    REDIS_PASSWORD = config('REDIS_PASSWORD')
    REDIS_ENDPOINT = config('REDIS_ENDPOINT')
    REDIS_DATABASE = config('REDIS_DATABASE')
    REDIS_USERNAME = config('REDIS_USERNAME')

    BREVO_EMAIL_HOST = config('BREVO_EMAIL_HOST')
    BREVO_EMAIL_PORT = int(config('BREVO_EMAIL_PORT'))
    BREVO_EMAIL_USER = config('BREVO_EMAIL_USER')
    BREVO_EMAIL_PASSWORD = config('BREVO_EMAIL_PASSWORD')

    BASE_URL = config('BASE_URL')


env: Config = Config()
