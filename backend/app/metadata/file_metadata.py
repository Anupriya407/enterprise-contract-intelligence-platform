from pathlib import Path

import fitz

from app.storage.hashing import calculate_sha256
from app.storage.mime import detect_mime_type


class FileMetadataExtractor:
    """Extract metadata from a document file."""

    @staticmethod
    def extract(file_path: Path) -> dict:
        """
        Extract file metadata.
        """

        document = fitz.open(file_path)

        metadata = {
            "filename": file_path.name,
            "file_size": file_path.stat().st_size,
            "mime_type": detect_mime_type(file_path),
            "file_hash": calculate_sha256(file_path),
            "page_count": document.page_count,
        }

        document.close()

        return metadata