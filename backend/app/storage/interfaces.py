from abc import ABC, abstractmethod
from pathlib import Path


class Storage(ABC):
    """Abstract interface for storage providers."""

    @abstractmethod
    def save(self, source: Path) -> Path:
        """Store a file and return its stored path."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, file_path: Path) -> None:
        """Delete a stored file."""
        raise NotImplementedError

    @abstractmethod
    def exists(self, file_path: Path) -> bool:
        """Check whether a stored file exists."""
        raise NotImplementedError

    @abstractmethod
    def get_path(self, file_path: Path) -> Path:
        """Return the absolute path of a stored file."""
        raise NotImplementedError