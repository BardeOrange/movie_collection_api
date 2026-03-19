from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class MovieBase(BaseModel):
    """Base schema with shared fields."""
    title: str = Field(..., min_length=1, max_length=255, examples=["Inception"])
    director: str = Field(..., min_length=1, max_length=255, examples=["Christopher Nolan"])
    year: int = Field(..., ge=1888, le=2030, examples=[2010])
    genre: str = Field(..., min_length=1, max_length=100, examples=["Sci-Fi"])
    rating: float = Field(default=0.0, ge=0.0, le=10.0, examples=[8.8])
    description: Optional[str] = Field(default=None, examples=["A mind-bending thriller"])


class MovieCreate(MovieBase):
    """Schema for creating a new movie."""
    pass


class MovieUpdate(BaseModel):
    """Schema for updating a movie. All fields optional."""
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    director: Optional[str] = Field(default=None, min_length=1, max_length=255)
    year: Optional[int] = Field(default=None, ge=1888, le=2030)
    genre: Optional[str] = Field(default=None, min_length=1, max_length=100)
    rating: Optional[float] = Field(default=None, ge=0.0, le=10.0)
    description: Optional[str] = None


class MovieResponse(MovieBase):
    """Schema for movie responses. Includes DB-generated fields."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
