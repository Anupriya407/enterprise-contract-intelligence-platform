import re


class TextCleaner:
    """Performs basic cleanup on OCR text."""

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean raw OCR text.

        Steps:
        1. Replace tabs with spaces.
        2. Remove trailing and leading whitespace.
        3. Collapse multiple spaces into one.
        4. Collapse multiple blank lines into a single blank line.
        """

        if not text:
            return ""

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove leading/trailing whitespace
        text = text.strip()

        # Replace multiple spaces with one space
        text = re.sub(r"[ ]{2,}", " ", text)

        # Replace multiple blank lines with a single blank line
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        return text