from pathlib import Path

from app.metadata.file_metadata import FileMetadataExtractor
from app.metadata.statistics import DocumentStatistics
from app.metadata.text_metadata import TextMetadataExtractor


class MetadataExtractor:
    """Main metadata extraction pipeline."""

    @staticmethod
    def extract(
        file_path: Path,
        text: str,
    ) -> dict:
        """
        Extract all document metadata.
        """

        file_metadata = FileMetadataExtractor.extract(file_path)

        text_metadata = TextMetadataExtractor.extract(text)

        statistics = DocumentStatistics.calculate(
            file_metadata=file_metadata,
            text_metadata=text_metadata,
        )

        return {
            **file_metadata,
            **text_metadata,
            **statistics,
        }