from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.constants import ROOT_TAG, WELCOME_MESSAGE
from app.core.lifespan import lifespan
from app.middleware.request_logger import RequestLoggingMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.add_middleware(RequestLoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/", tags=[ROOT_TAG])
def root():
    return {
        "message": f"{WELCOME_MESSAGE} {settings.APP_NAME}"
    }