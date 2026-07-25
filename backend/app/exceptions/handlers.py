from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import ECIPException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ECIPException)
    async def ecip_exception_handler(
        request: Request,
        exc: ECIPException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.message,
            },
        )