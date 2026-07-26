import mimetypes
from pathlib import Path


def detect_mime_type(file_path: Path) -> str:
    """Detect the MIME type of a file."""

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        return "application/octet-stream"

    return mime_type