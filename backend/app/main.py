from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine


app = FastAPI(
    title="Retail Resale Management System API",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/health/db")
def database_health_check() -> dict[str, str]:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"database": "healthy"}