from fastapi import APIRouter
from fastapi import APIRouter

from app.api.v1.documents import router as documents_router
from app.api.v1.health import router as health_router
from app.core.constants import API_V1_PREFIX

api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix=API_V1_PREFIX,
)

api_router.include_router(
    documents_router,
    prefix=API_V1_PREFIX,
)