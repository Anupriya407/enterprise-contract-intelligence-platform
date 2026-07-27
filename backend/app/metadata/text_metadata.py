class TextMetadataExtractor:
    """Extract metadata from processed document text."""

    @staticmethod
    def extract(text: str) -> dict:
        """
        Extract text metadata.
        """

        if not text:
            return {
                "character_count": 0,
                "word_count": 0,
                "line_count": 0,
                "paragraph_count": 0,
            }

        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        metadata = {
            "character_count": len(text),
            "word_count": len(text.split()),
            "line_count": len(text.splitlines()),
            "paragraph_count": len(paragraphs),
        }

        return metadata