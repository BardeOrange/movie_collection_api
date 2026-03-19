from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserCreate(BaseModel):
    """Schema for user registration."""
    username: str = Field(
        ..., min_length=3, max_length=50, examples=["johndoe"]
    )
    email: EmailStr = Field(..., examples=["john@example.com"])
    password: str = Field(
        ..., min_length=6, max_length=100, examples=["strongpassword123"]
    )


class UserResponse(BaseModel):
    """Schema for user responses. Never includes password."""
    id: int
    username: str
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    """Schema for JWT token response."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema for decoded token data."""
    user_id: int
    username: str
