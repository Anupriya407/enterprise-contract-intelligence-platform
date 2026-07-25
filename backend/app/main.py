from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Enterprise Contract Intelligence Platform",
    version="1.0.0",
    description="ECIP Backend API",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Enterprise Contract Intelligence Platform"
    }