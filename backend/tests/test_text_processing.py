from app.text_processing.cleaner import TextCleaner
from app.text_processing.normalizer import TextNormalizer
from app.text_processing.paragraph_builder import ParagraphBuilder
from app.text_processing.processor import TextProcessor


def test_text_cleaner():
    text = "Hello      World\n\n\nThis    is\tECIP"

    cleaned = TextCleaner.clean(text)

    assert cleaned == "Hello World\n\nThis is ECIP"


def test_text_normalizer():
    text = "“ECIP”\r\nIt’s running."

    normalized = TextNormalizer.normalize(text)

    assert normalized == "\"ECIP\"\nIt's running."


def test_paragraph_builder():
    text = (
        "This Agreement\n"
        "is entered\n"
        "between both parties.\n\n"
        "Payment shall\n"
        "be made within\n"
        "30 days."
    )

    paragraph = ParagraphBuilder.build(text)

    expected = (
        "This Agreement is entered between both parties.\n\n"
        "Payment shall be made within 30 days."
    )

    assert paragraph == expected


def test_text_processor():
    text = (
        "“Enterprise     Contract”\n\n"
        "This   Agreement\n"
        "is entered\n"
        "between both parties."
    )

    processed = TextProcessor.process(text)

    expected = (
        "\"Enterprise Contract\"\n\n"
        "This Agreement is entered between both parties."
    )

    assert processed == expected