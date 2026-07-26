from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.exceptions.custom_exceptions import (
    DocumentAlreadyExistsException,
    InvalidDocumentException,
)
from app.models.document import Document
from app.repositories.document import DocumentRepository
from app.schemas.document import DocumentUploadResponse
from app.services.base import BaseService
from app.services.ocr_service import OCRService
from app.storage.hashing import calculate_sha256
from app.storage.local import LocalStorage


class DocumentService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repository = DocumentRepository(db)
        self.storage = LocalStorage()

    def create(self, document: Document) -> Document:
        try:
            document = self.repository.create(document)
            self.db.commit()
            self.db.refresh(document)
            return document
        except Exception:
            self.db.rollback()
            raise

    async def upload(self, file: UploadFile) -> DocumentUploadResponse:
        # Validate filename
        if not file.filename:
            raise InvalidDocumentException("Filename is required.")

        # Validate content type
        if not file.content_type:
            raise InvalidDocumentException("Content type is required.")

        # Validate file extension
        extension = Path(file.filename).suffix.lower()

        if extension not in settings.ALLOWED_FILE_EXTENSIONS:
            raise InvalidDocumentException(
                f"Unsupported file extension: {extension}"
            )

        # Validate MIME type
        allowed_content_types = {
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        }

        if file.content_type not in allowed_content_types:
            raise InvalidDocumentException(
                "Unsupported content type."
            )

        # Save file
        stored_path = self.storage.save(file)

        try:
            absolute_path = self.storage.get_path(stored_path)

            # Validate file size
            file_size = absolute_path.stat().st_size

            if file_size > settings.MAX_UPLOAD_SIZE:
                raise InvalidDocumentException(
                    "File exceeds maximum upload size."
                )

            # Calculate SHA-256 hash
            file_hash = calculate_sha256(absolute_path)

            # Duplicate detection
            existing_document = self.repository.get_by_hash(file_hash)

            if existing_document is not None:
                raise DocumentAlreadyExistsException()

            # Create database record
            document = Document(
                filename=file.filename,
                file_path=str(stored_path),
                content_type=file.content_type,
                file_size=file_size,
                file_hash=file_hash,
            )

            document = self.create(document)

            # -------------------------
            # Process OCR
            # -------------------------
            OCRService.process_document(
                db=self.db,
                document=document,
            )

            return DocumentUploadResponse(
            message="Document uploaded successfully",
            document_id=document.id,
            filename=document.filename,
            content_type=document.content_type,
            file_path=document.file_path,
            ocr_status=document.ocr_status,
            ocr_completed_at=document.ocr_completed_at,
            )

        except Exception:
            if self.storage.exists(stored_path):
                self.storage.delete(stored_path)
            raise