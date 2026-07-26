import fitz
from PIL import Image


class PDFConverter:
    """Convert PDF pages into PIL images."""

    @staticmethod
    def convert(pdf_path: str) -> list[Image.Image]:
        images = []

        pdf = fitz.open(pdf_path)

        for page in pdf:
            pixmap = page.get_pixmap(dpi=300)

            image = Image.frombytes(
                "RGB",
                (pixmap.width, pixmap.height),
                pixmap.samples,
            )

            images.append(image)

        pdf.close()

        return images