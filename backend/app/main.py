from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import logger

logger.info("Starting ECIP Backend")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }