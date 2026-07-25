from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Contract Intelligence Platform",
    version="1.0.0",
    description="ECIP Backend API"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Enterprise Contract Intelligence Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }