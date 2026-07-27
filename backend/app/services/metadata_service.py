from pathlib import Path

from app.metadata.extractor import MetadataExtractor


class MetadataService:
    """Service responsible for document metadata extraction."""

    @staticmethod
    def extract(
        file_path: Path,
        text: str,
    ) -> dict:
        """
        Extract document metadata.
        """

        return MetadataExtractor.extract(
            file_path=file_path,
            text=text,
        )