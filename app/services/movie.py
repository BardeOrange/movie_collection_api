from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate


def create_movie(db: Session, movie_data: MovieCreate) -> Movie:
    """Create a new movie in the database."""
    movie = Movie(**movie_data.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def get_movie(db: Session, movie_id: int) -> Optional[Movie]:
    """Get a single movie by ID."""
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_movies(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    search: Optional[str] = None,
    genre: Optional[str] = None
) -> list[Movie]:
    """Get a list of movies with optional filtering."""
    query = db.query(Movie)

    if search:
        query = query.filter(
            or_(
                Movie.title.ilike(f"%{search}%"),
                Movie.director.ilike(f"%{search}%")
            )
        )

    if genre:
        query = query.filter(Movie.genre.ilike(f"%{genre}%"))

    return query.offset(skip).limit(limit).all()


def update_movie(
    db: Session,
    movie_id: int,
    movie_data: MovieUpdate
) -> Optional[Movie]:
    """Update an existing movie."""
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        return None

    update_data = movie_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(movie, field, value)

    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int) -> bool:
    """Delete a movie by ID. Returns True if deleted."""
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        return False

    db.delete(movie)
    db.commit()
    return True
