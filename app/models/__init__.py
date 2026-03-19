from app.models.movie import Movie
from app.models.user import User

"""
Example of an easy way to define what you want to be put in import * ( useful for a public project).
from app.models import * will only import :
=> Movie, User
"""

__all__ = ["Movie", "User"]
