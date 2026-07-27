from sqlalchemy.orm import Session

from app.repositories.search import SearchRepository


class SearchService:
    """Service for document search."""

    def __init__(self, db: Session):
        self.repository = SearchRepository(db)

    def search_documents(
        self,
        query: str,
        ocr_status: str | None = None,
        content_type: str | None = None,
        min_pages: int | None = None,
        max_pages: int | None = None,
        min_words: int | None = None,
        max_words: int | None = None,
        sort_by: str = "created_at",
        sort_order: str = "desc",
        skip: int = 0,
        limit: int = 10,
    ):
        return self.repository.search_documents(
            query=query,
            ocr_status=ocr_status,
            content_type=content_type,
            min_pages=min_pages,
            max_pages=max_pages,
            min_words=min_words,
            max_words=max_words,
            sort_by=sort_by,
            sort_order=sort_order,
            skip=skip,
            limit=limit,
        )