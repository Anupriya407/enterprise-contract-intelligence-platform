from fastapi import UploadFile

from app.storage.local import LocalStorage


class FileService:
    """Service responsible for file storage operations."""

    def __init__(self):
        self.storage = LocalStorage()

    def save(self, file: UploadFile):
        return self.storage.save(file)