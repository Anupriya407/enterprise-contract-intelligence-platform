from app.db.session import SessionLocal
from app.models.document import Document
from app.services.ocr_service import OCRService

db = SessionLocal()

document = db.query(Document).first()

OCRService.process_document(db, document)

print(document.ocr_status)
print(document.ocr_completed_at)
print(document.extracted_text[:500])

db.close()