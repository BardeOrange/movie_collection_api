from app.auth.utils import hash_password, verify_password, create_access_token
from app.auth.dependencies import get_current_user

"""
Example of an easy way to define what you want to be put in import * ( useful for a public project).
from app.auth import * will only import :
=> hash_password, verify_password, create_access_token, get_current_user
"""

__all__ = [
    "hash_password", "verify_password",
    "create_access_token", "get_current_user"
]
