from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST", "localhost") 
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_PORT: str = os.getenv("DB_PORT")


setting = Settings()