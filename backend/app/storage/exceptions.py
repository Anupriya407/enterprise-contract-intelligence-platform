class StorageError(Exception):
    """Base exception for storage errors."""


class FileStorageError(StorageError):
    """Raised when storing a file fails."""


class FileDeletionError(StorageError):
    """Raised when deleting a file fails."""


class FileNotFoundStorageError(StorageError):
    """Raised when a stored file cannot be found."""