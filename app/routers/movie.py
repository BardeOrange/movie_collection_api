from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from app.services import movie as movie_service
from app.models.user import User
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("/", response_model=MovieResponse, status_code=201)
def create_movie(
    movie_data: MovieCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 🔒 Protected
):
    """Create a new movie. Requires authentication."""
    return movie_service.create_movie(db=db, movie_data=movie_data)


@router.get("/", response_model=list[MovieResponse])
def get_movies(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    search: Optional[str] = Query(default=None),
    genre: Optional[str] = Query(default=None),
    db: Session = Depends(get_db)
):
    """Get all movies. Public endpoint."""
    return movie_service.get_movies(
        db=db, skip=skip, limit=limit, search=search, genre=genre
    )


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """Get a specific movie. Public endpoint."""
    movie = movie_service.get_movie(db=db, movie_id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(
    movie_id: int,
    movie_data: MovieUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 🔒 Protected
):
    """Update a movie. Requires authentication."""
    movie = movie_service.update_movie(
        db=db, movie_id=movie_id, movie_data=movie_data
    )
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.delete("/{movie_id}", status_code=204)
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 🔒 Protected
):
    """Delete a movie. Requires authentication."""
    deleted = movie_service.delete_movie(db=db, movie_id=movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")