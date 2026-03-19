from app.services import movie
from app.services import user

"""
Example of an easy way to define what you want to be put in import * ( useful for a public project).
from app.services import * will only import :
=> movie, user
"""

__all__ = ["movie", "user"]