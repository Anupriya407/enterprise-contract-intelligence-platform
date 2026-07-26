from sqlalchemy import text

from app.db.session import SessionLocal


def test_database_connection() -> None:
    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1
    finally:
        db.close()