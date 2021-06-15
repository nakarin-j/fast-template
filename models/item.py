from typing import Counter
from db.db_class import Base
from sqlalchemy import Column, String, Text

class Item(Base):
    name = Column(String(50))
    description = Column(Text)

    def __repr__(self):
        return f"<Item: {self.name}/>"