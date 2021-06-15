from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config.default as Config


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{Config.setting.db_user}"
    f":{Config.setting.db_pwd}@localhost:{Config.setting.db_port}/{Config.setting.db_name}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)