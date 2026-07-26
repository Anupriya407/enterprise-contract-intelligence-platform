from pathlib import Path

from app.storage.interfaces import Storage


class LocalStorage(Storage):
    """Local filesystem storage implementation."""

    def __init__(self, root_directory: Path):
        self._root_directory = root_directory
        self._root_directory.mkdir(parents=True, exist_ok=True)

    def save(self, source: Path) -> Path:
        raise NotImplementedError

    def delete(self, file_path: Path) -> None:
        raise NotImplementedError

    def exists(self, file_path: Path) -> bool:
        return (self._root_directory / file_path).exists()

    def get_path(self, file_path: Path) -> Path:
        return self._root_directory / file_path