from datetime import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import CheckConstraint, DateTime, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OCRStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Document(Base):
    __tablename__ = "documents"

    __table_args__ = (
        Index("ix_documents_filename", "filename"),
        Index("ix_documents_created_at", "created_at"),
        CheckConstraint(
            "char_length(filename) > 0",
            name="ck_documents_filename_not_empty",
        ),
        CheckConstraint(
            "char_length(file_path) > 0",
            name="ck_documents_file_path_not_empty",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(1024),
        nullable=False,
    )

    content_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        nullable=False,
    )

    file_hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
    )

    # =========================
    # OCR Fields
    # =========================

    ocr_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default=OCRStatus.PENDING.value,
        server_default=OCRStatus.PENDING.value,
    )

    extracted_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ocr_completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # =========================
    # Metadata Fields
    # =========================

    page_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    character_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    word_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    line_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    paragraph_count: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    # =========================
    # Timestamps
    # =========================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )