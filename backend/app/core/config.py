from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    ALLOWED_ORIGINS: List[str] = Field(default_factory=list)

    DATABASE_URL: str

    STORAGE_DIRECTORY: str = "storage/documents"

    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  # 50 MB

    ALLOWED_FILE_EXTENSIONS: list[str] = [
        ".pdf",
        ".docx",
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()