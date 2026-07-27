from app.text_processing.processor import TextProcessor


class TextProcessingService:
    """Service responsible for processing OCR text."""

    @staticmethod
    def process(text: str) -> str:
        """
        Process raw OCR text and return cleaned text.
        """

        return TextProcessor.process(text)