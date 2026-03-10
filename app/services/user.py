from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.utils import hash_password, verify_password


def create_user(db: Session, user_data: UserCreate) -> User:
    """Create a new user with hashed password."""
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Find a user by username."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Find a user by email."""
    return db.query(User).filter(User.email == email).first()


def authenticate_user(
    db: Session,
    username: str,
    password: str
) -> Optional[User]:
    """Verify credentials and return user if valid."""
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user