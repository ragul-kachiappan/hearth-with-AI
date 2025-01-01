from starlette.config import Config
from starlette.datastructures import Secret

config = Config("../../.env")


DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_USER = config("DATABASE_USER")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_NAME = config("DATABASE_NAME")
DATABASE_HOST = config("DATABASE_HOST")
DATABASE_PORT = config("DATABASE_PORT", default=5432)
SECRET_KEY = config("SECRET_KEY", cast=Secret)

database_url: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
