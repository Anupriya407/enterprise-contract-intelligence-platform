class ECIPException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class DocumentAlreadyExistsException(ECIPException):
    def __init__(self):
        super().__init__(
            message="Document already exists.",
            status_code=409,
        )


class InvalidDocumentException(ECIPException):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            status_code=400,
        )


class DocumentNotFoundException(ECIPException):
    def __init__(self):
        super().__init__(
            message="Document not found.",
            status_code=404,
        )