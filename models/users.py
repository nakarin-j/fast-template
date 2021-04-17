from sqlalchemy import Column, Integer, String, DateTime
from db.db_class import Base
from datetime import datetime

class User(Base):
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    created_date = Column(DateTime)

    def __repr__(self):
        return f"<User id: {self.id} name: {self.first_name} {self.last_name}"