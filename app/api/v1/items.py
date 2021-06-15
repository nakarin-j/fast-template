from models.item import Item
from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1 import PREFIX
from app.dependencies.db import get_db

import app.services.item_service as ItemService
import schemas.item as ItemSchemas

router = APIRouter(prefix=f"{PREFIX}/item")

@router.get('/')
def get_items(db: Session = Depends(get_db)):
    resp = ItemService.get_items(db)
    return resp


@router.post('/')
def create_item(item: ItemSchemas.ItemBase, db: Session = Depends(get_db)):
    ItemService.create_item(item, db)

    db.commit()
    return {"success": True}


@router.put('/{item_id}/')
def update_item(item_id: int, payload: ItemSchemas.ItemInput, db: Session = Depends(get_db)):
    ItemService.update_item(item_id, payload, db)

    db.commit()
    return {'success': True}


@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    ItemService.delete_item(item_id, db)
    return {'success': True}