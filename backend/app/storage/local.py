from pathlib import Path

from app.core.config import settings
from app.storage.interfaces import Storage


class LocalStorage(Storage):
    """Local filesystem storage implementation."""

    def __init__(self, root_directory: Path | None = None):
        self._root_directory = (
            root_directory
            if root_directory is not None
            else Path(settings.STORAGE_DIRECTORY)
        )

        self._root_directory.mkdir(parents=True, exist_ok=True)

    def save(self, source: Path) -> Path:
        raise NotImplementedError

    def delete(self, file_path: Path) -> None:
        """Delete a stored file if it exists."""

        target = self._root_directory / file_path

        if target.exists():
            target.unlink()

    def exists(self, file_path: Path) -> bool:
        return (self._root_directory / file_path).exists()

    def get_path(self, file_path: Path) -> Path:
        """Return the absolute path of a stored file."""

        target = self._root_directory / file_path

        if not target.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        return target.resolve()