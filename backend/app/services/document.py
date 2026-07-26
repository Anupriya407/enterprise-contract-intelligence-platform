from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document import DocumentRepository
from app.services.base import BaseService


class DocumentService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repository = DocumentRepository(db)

    def create(self, document: Document) -> Document:
        try:
            document = self.repository.create(document)
            self.db.commit()
            self.db.refresh(document)
            return document
        except Exception:
            self.db.rollback()
            raise