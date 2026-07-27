class ParagraphBuilder:
    """Reconstructs readable paragraphs from OCR text."""

    @staticmethod
    def build(text: str) -> str:
        """
        Reconstruct paragraphs by joining broken lines.

        Blank lines are treated as paragraph separators.
        """

        if not text:
            return ""

        paragraphs = []

        for block in text.split("\n\n"):
            lines = [line.strip() for line in block.split("\n") if line.strip()]

            if lines:
                paragraphs.append(" ".join(lines))

        return "\n\n".join(paragraphs)