from sqlalchemy import Column, BigInteger, DateTime, String
from sqlalchemy.orm import registry, declared_attr
from datetime import datetime

import re


mapper_registry = registry()

@mapper_registry.as_declarative_base()
class Base(object):

    @declared_attr
    def __tablename__(cls):
        tablename = re.sub('(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
        return tablename

    id = Column(BigInteger, primary_key=True)
    
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    created_by = Column(String(80), nullable=False)

    updated_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_by = Column(String(80), nullable=False)


    def update(self, **kwargs):
        keys = self.__table__.columns.keys()

        for key, value in kwargs.items():
            if not key in keys:
                continue

            setattr(self, key, value)
