class DocumentStatistics:
    """Calculate document statistics."""

    @staticmethod
    def calculate(
        file_metadata: dict,
        text_metadata: dict,
    ) -> dict:
        """
        Calculate document statistics.
        """

        page_count = max(file_metadata.get("page_count", 1), 1)
        paragraph_count = max(text_metadata.get("paragraph_count", 1), 1)

        statistics = {
            "words_per_page": (
                text_metadata["word_count"] / page_count
            ),
            "characters_per_page": (
                text_metadata["character_count"] / page_count
            ),
            "words_per_paragraph": (
                text_metadata["word_count"] / paragraph_count
            ),
        }

        return statistics