from pathlib import Path
from uuid import uuid4


def generate_storage_filename(source: Path) -> str:
    """Generate a unique filename while preserving the extension."""

    extension = source.suffix.lower()

    return f"{uuid4()}{extension}"