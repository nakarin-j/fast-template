from pydantic import BaseSettings
from os.path import abspath

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_NAME: str
    DB_PWD: str
    DB_PORT: str
    class Config:
        env_file = abspath(".env")


setting = Settings()