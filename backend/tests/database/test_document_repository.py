from app.db.session import SessionLocal
from app.models.document import Document
from app.repositories.document import DocumentRepository


def test_create_document():
    db = SessionLocal()

    try:
        repository = DocumentRepository(db)

        document = Document(
            filename="test.pdf",
            file_path="storage/test.pdf",
            content_type="application/pdf",
        )

        repository.create(document)
        db.commit()

        assert document.id is not None

    finally:
        db.rollback()
        db.close()