from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.routers import movie, auth

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="A REST API to manage your personal movie collection",
    version="1.0.0",
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(movie.router, prefix="/api/v1")


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint."""
    return {
        "app": settings.app_name,
        "status": "running",
        "docs": "/docs"
    }
