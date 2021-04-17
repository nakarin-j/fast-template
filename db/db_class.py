from sqlalchemy import Column, BigInteger, DateTime, String, func
from sqlalchemy.orm import registry, declared_attr

from datetime import datetime

mapper_registry = registry()

@mapper_registry.as_declarative_base()
class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(BigInteger, primary_key=True)
    
    created_date = Column(DateTime, nullable=False, server_default=func.utcnow())
    created_by = Column(String(80), nullable=False)

    updated_date = Column(DateTime, nullable=False, server_default=func.utcnow())
    updated_by = Column(String(80), nullable=False)
