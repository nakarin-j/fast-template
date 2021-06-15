from pydantic import BaseSettings
from os.path import abspath

class Settings(BaseSettings):
    db_user: str
    db_name: str
    db_pwd: str
    db_port: str

    secret_code: str = 'secret_code_here'
    algs: str = 'HS256'

    class Config:
        env_file = abspath(".env")


setting = Settings()