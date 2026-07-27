from datetime import datetime
from pathlib import Path

from sqlalchemy.orm import Session

from app.models.document import Document, OCRStatus
from app.ocr.engine import OCREngine
from app.ocr.pdf_converter import PDFConverter
from app.services.text_processing_service import TextProcessingService
from app.storage.local import LocalStorage


class OCRService:
    _storage = LocalStorage()

    @staticmethod
    def process_document(
        db: Session,
        document: Document,
    ) -> None:
        """
        Run OCR on a stored PDF, process the extracted text,
        and update the document.
        """

        try:
            # Mark as processing
            document.ocr_status = OCRStatus.PROCESSING.value
            db.commit()
            db.refresh(document)

            # Resolve the absolute path of the stored PDF
            pdf_path = OCRService._storage.get_path(
                Path(document.file_path)
            )

            # Convert PDF to images
            images = PDFConverter.convert(str(pdf_path))

            # Extract text from each page
            extracted_pages: list[str] = []

            for image in images:
                text = OCREngine.extract_text(image)
                extracted_pages.append(text)

            # Combine OCR output
            raw_text = "\n\n".join(extracted_pages)

            # Process OCR text
            clean_text = TextProcessingService.process(raw_text)

            # Save processed text
            document.extracted_text = clean_text
            document.ocr_status = OCRStatus.COMPLETED.value
            document.ocr_completed_at = datetime.utcnow()

            db.commit()
            db.refresh(document)

        except Exception:
            db.rollback()

            document.ocr_status = OCRStatus.FAILED.value
            db.commit()

            raise