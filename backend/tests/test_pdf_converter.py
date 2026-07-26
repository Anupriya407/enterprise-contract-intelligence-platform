from app.ocr.pdf_converter import PDFConverter

images = PDFConverter.convert(
    "storage/documents/0e819e3b-53dc-4352-9afb-b063e004aba5.pdf"
)

print(f"Pages: {len(images)}")