from fastapi import APIRouter
from app.api.v1 import api, items

router = APIRouter()

router.include_router(api.router)
router.include_router(items.router)