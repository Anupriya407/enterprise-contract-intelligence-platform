from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.document import OCRStatus


class SearchResult(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    filename: str
    content_type: str
    file_size: int
    ocr_status: OCRStatus
    page_count: int | None
    word_count: int | None
    created_at: datetime


class SearchResponse(BaseModel):
    results: list[SearchResult]
    total: int
    page: int
    size: int