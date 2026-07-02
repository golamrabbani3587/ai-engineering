from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate, UserResonse
from app.services.user_service import create_user, get_user_by_id, get_all_users, get_user_by_email

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResonse, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/{user_id}", response_model=UserResonse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[UserResonse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_users(db=db, skip=skip, limit=limit)
