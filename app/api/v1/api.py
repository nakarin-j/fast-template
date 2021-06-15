from fastapi import APIRouter
from app.api.v1 import PREFIX

router = APIRouter(prefix=f"{PREFIX}")

@router.get('/version')
def get_api_version():
    return {"version": "0.1"}