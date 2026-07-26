from app.ocr.pdf_converter import PDFConverter
from app.ocr.engine import OCREngine

images = PDFConverter.convert(
    "storage/documents/0e819e3b-53dc-4352-9afb-b063e004aba5.pdf"
)

text = OCREngine.extract_text(images[0])

print(text)