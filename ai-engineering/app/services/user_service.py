from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate


def create_user(db: Session, user: UserCreate) -> User:
    """Create and persist a new user."""
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password,   # hash this in production!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """Return a single user by primary key, or None."""
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Return a paginated list of all users."""
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str) -> User | None:
    """Return a single user by email, or None."""
    return db.query(User).filter(User.email == email).first()

