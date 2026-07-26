from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

from app.core.config import settings


class OCREngine:
    """Singleton PaddleOCR engine."""

    _ocr: PaddleOCR | None = None

    @classmethod
    def get_engine(cls) -> PaddleOCR:
        if cls._ocr is None:
            cls._ocr = PaddleOCR(
                use_angle_cls=True,
                lang=settings.OCR_LANGUAGE,
                use_gpu=settings.OCR_USE_GPU,
            )

        return cls._ocr

    @classmethod
    def extract_text(cls, image: Image.Image) -> str:
        """
        Extract text from a single image.
        """
        ocr = cls.get_engine()

        result = ocr.ocr(np.array(image), cls=True)

        lines = []

        if result:
            for block in result:
                if block is None:
                    continue

                for line in block:
                    lines.append(line[1][0])

        return "\n".join(lines)