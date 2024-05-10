from fastapi import FastAPI
from routes import router


def main() -> FastAPI:
    publisher = FastAPI()

    publisher.include_router(router)

    return publisher


app = main()
