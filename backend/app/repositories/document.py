from sqlalchemy import select

from app.models.document import Document
from app.repositories.base import BaseRepository


class DocumentRepository(BaseRepository):
    def create(self, document: Document) -> Document:
        self.db.add(document)
        self.db.flush()
        self.db.refresh(document)
        return document

    def get_by_id(self, document_id: str) -> Document | None:
        statement = select(Document).where(Document.id == document_id)
        return self.db.scalar(statement)

    def get_by_hash(self, file_hash: str) -> Document | None:
        statement = select(Document).where(Document.file_hash == file_hash)
        return self.db.scalar(statement)

    def get_all(self) -> list[Document]:
        statement = select(Document)
        return list(self.db.scalars(statement).all())

    def delete(self, document: Document) -> None:
        self.db.delete(document)
