from app.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from app.schemas.user import UserCreate, UserResponse, Token, TokenData

"""
Example of an easy way to define what you want to be put in import * ( useful for a public project).
from app.schemas import * will only import :
=> MovieCreate, MovieUpdate, MovieResponse, UserCreate, UserResponse, Token, TokenData
"""

__all__ = [
    "MovieCreate", "MovieUpdate", "MovieResponse",
    "UserCreate", "UserResponse", "Token", "TokenData"
]