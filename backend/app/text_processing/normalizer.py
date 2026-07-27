import unicodedata


class TextNormalizer:
    """Normalizes OCR text into a consistent format."""

    @staticmethod
    def normalize(text: str) -> str:
        """
        Normalize OCR text.

        Steps:
        1. Normalize Unicode characters.
        2. Standardize line endings.
        3. Replace smart quotes with standard quotes.
        """

        if not text:
            return ""

        # Normalize Unicode
        text = unicodedata.normalize("NFKC", text)

        # Standardize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace smart double quotes
        text = text.replace("“", '"')
        text = text.replace("”", '"')

        # Replace smart apostrophes
        text = text.replace("‘", "'")
        text = text.replace("’", "'")

        return text