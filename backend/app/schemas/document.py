from pydantic import BaseModel, ConfigDict


class DocumentUploadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    message: str
    document_id: str
    filename: str
    content_type: str
    file_path: str