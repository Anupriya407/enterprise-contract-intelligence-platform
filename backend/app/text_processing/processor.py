from app.text_processing.cleaner import TextCleaner
from app.text_processing.normalizer import TextNormalizer
from app.text_processing.paragraph_builder import ParagraphBuilder


class TextProcessor:
    """Main text processing pipeline."""

    @staticmethod
    def process(text: str) -> str:
        """
        Process OCR text through the complete pipeline.
        """

        text = TextCleaner.clean(text)
        text = TextNormalizer.normalize(text)
        text = ParagraphBuilder.build(text)

        return text