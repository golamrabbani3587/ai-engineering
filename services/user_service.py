from sqlalchemy.orm import Session
from core.security import hash_password

from db.models import User
from schemas.user import UserCreate

from passlib.context import CryptContext

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

def verify_password(plain_password, hashed_password):
    if len(plain_password.encode("utf-8")) > 72:
        return False

    return pwd_context.verify(plain_password, hashed_password)



# 🔐 THIS IS REQUIRED (bcrypt engine setup)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)




def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)