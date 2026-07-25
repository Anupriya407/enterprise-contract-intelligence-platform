from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("ECIP Backend started.")

    yield

    logger.info("ECIP Backend stopped.")