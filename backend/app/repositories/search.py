from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.base import BaseRepository


class SearchRepository(BaseRepository):
    """Repository for document search operations."""

    def __init__(self, db: Session):
        super().__init__(db)

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
        search = f"%{query}%"

        query_builder = self.db.query(Document).filter(
            or_(
                Document.filename.ilike(search),
                Document.extracted_text.ilike(search),
            )
        )

        if ocr_status:
            query_builder = query_builder.filter(
                Document.ocr_status == ocr_status
            )

        if content_type:
            query_builder = query_builder.filter(
                Document.content_type == content_type
            )

        if min_pages is not None:
            query_builder = query_builder.filter(
                Document.page_count >= min_pages
            )

        if max_pages is not None:
            query_builder = query_builder.filter(
                Document.page_count <= max_pages
            )

        if min_words is not None:
            query_builder = query_builder.filter(
                Document.word_count >= min_words
            )

        if max_words is not None:
            query_builder = query_builder.filter(
                Document.word_count <= max_words
            )

        total = query_builder.with_entities(
            func.count(Document.id)
        ).scalar()

        sort_columns = {
            "created_at": Document.created_at,
            "filename": Document.filename,
            "file_size": Document.file_size,
            "page_count": Document.page_count,
            "word_count": Document.word_count,
        }

        sort_column = sort_columns.get(
            sort_by,
            Document.created_at,
        )

        if sort_order.lower() == "asc":
            query_builder = query_builder.order_by(
                sort_column.asc()
            )
        else:
            query_builder = query_builder.order_by(
                sort_column.desc()
            )

        documents = (
            query_builder
            .offset(skip)
            .limit(limit)
            .all()
        )

        return documents, total