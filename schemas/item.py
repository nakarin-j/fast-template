
from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str


class ItemInput(ItemBase):
    description: Optional[str]


class Item(BaseModel):
    id: int
    name: str
    description: str
    created_by: str
    created_date: str
    updated_by: str
    updated_date: str