from pathlib import Path


def validate_file(source: Path) -> None:
    """Validate an uploaded file."""

    if not source.exists():
        raise FileNotFoundError(f"File does not exist: {source}")

    if not source.is_file():
        raise ValueError(f"Not a valid file: {source}")

    if source.stat().st_size == 0:
        raise ValueError("File is empty.")