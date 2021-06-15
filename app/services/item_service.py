from models import Item
from sqlalchemy.orm import Session

import schemas.item as ItemSchemas
import app.constant as Constant

def get_items(db: Session):
    return db.query(Item).all()


def get_item_by_id(id: int, db: Session):
    return db.query(Item).filter(Item.id == id).first()


def create_item(item: ItemSchemas.ItemBase, db: Session):
    item_obj = Item(
        **item.dict(), 
        created_by=Constant.CREATED_BY_SYSTEM, 
        updated_by=Constant.CREATED_BY_SYSTEM
    )
    
    db.add(item_obj)
    return item_obj


def update_item(item_id: int, payload: dict, db: Session):
    item = get_item_by_id(item_id, db)

    if not item:
        return {"message": f"Item id: {item_id} not found"}

    item.update(**payload.dict())


def delete_item(item_id: int, db: Session):
    item = get_item_by_id(item_id, db)
    db.delete(item)