import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings
from app.storage.interfaces import Storage
from app.storage.exceptions import (
    FileDeletionError,
    FileNotFoundStorageError,
)

class LocalStorage(Storage):
    """Local filesystem storage implementation."""

    def __init__(self, root_directory: Path | None = None):
        self._root_directory = (
            root_directory
            if root_directory is not None
            else Path(settings.STORAGE_DIRECTORY)
        )

        self._root_directory.mkdir(parents=True, exist_ok=True)

    def save(self, file: UploadFile) -> Path:
        """Save an uploaded file to local storage."""

        extension = Path(file.filename).suffix
        filename = f"{uuid4()}{extension}"

        destination = self._root_directory / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return Path(filename)

    def delete(self, file_path: Path) -> None:
        """Delete a stored file."""

        target = self._root_directory / file_path

        if not target.exists():
            raise FileNotFoundStorageError(f"File not found: {file_path}")

        try:
            target.unlink()
        except OSError as exc:
            raise FileDeletionError(
                f"Failed to delete file: {file_path}"
            ) from exc

    def exists(self, file_path: Path) -> bool:
        return (self._root_directory / file_path).exists()

    def get_path(self, file_path: Path) -> Path:
        """Return the absolute path of a stored file."""

        target = self._root_directory / file_path

        if not target.exists():
            raise FileNotFoundStorageError(
                f"File not found: {file_path}"
            )

        return target.resolve()