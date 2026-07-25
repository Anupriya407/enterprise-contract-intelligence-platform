from fastapi import APIRouter

from app.core.constants import HEALTH_STATUS, HEALTH_TAG

router = APIRouter()


@router.get("/health", tags=[HEALTH_TAG])
def health():
    return {
        "status": HEALTH_STATUS
    }