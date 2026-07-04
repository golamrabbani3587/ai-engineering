from sqlalchemy.orm import Session
from core.security import hash_password

from db.models import User
from schemas.user import UserCreate


def register_user(db, user_data):
    hashed_pw = hash_password(user_data.password)

    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_all_users(db: Session):
    users = db.query(User).all()
    return users
