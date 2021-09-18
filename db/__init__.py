from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config.default as Config


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{Config.setting.DB_USERNAME}"
    f":{Config.setting.DB_PASSWORD}@{Config.setting.DB_HOST}:{Config.setting.DB_PORT}/{Config.setting.DB_NAME}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)