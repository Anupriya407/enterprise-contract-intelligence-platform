from fastapi import APIRouter, Depends, File, Query, UploadFile, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.document import DocumentUploadResponse
from app.schemas.search import SearchResponse, SearchResult
from app.services.document import DocumentService
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    service = DocumentService(db)
    return await service.upload(file)


@router.get(
    "/search",
    response_model=SearchResponse,
    status_code=status.HTTP_200_OK,
)
def search_documents(
    q: str = Query(..., min_length=1),
    ocr_status: str | None = Query(None),
    content_type: str | None = Query(None),
    min_pages: int | None = Query(None, ge=1),
    max_pages: int | None = Query(None, ge=1),
    min_words: int | None = Query(None, ge=0),
    max_words: int | None = Query(None, ge=0),
    sort_by: str = Query("created_at"),
    sort_order: str = Query("desc"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    skip = (page - 1) * size

    service = SearchService(db)

    documents, total = service.search_documents(
    query=q,
    ocr_status=ocr_status,
    content_type=content_type,
    min_pages=min_pages,
    max_pages=max_pages,
    min_words=min_words,
    max_words=max_words,
    sort_by=sort_by,
    sort_order=sort_order,
    skip=skip,
    limit=size,
    )

    return SearchResponse(
        results=[SearchResult.model_validate(doc) for doc in documents],
        total=total,
        page=page,
        size=size,
    )