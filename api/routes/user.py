from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from core.jwt import create_access_token
from core.security import verify_password
from core.deps import get_current_user

from db.database import get_db
from schemas.user import UserCreate
from schemas.user import UserResponse
from services.user_service import register_user
from services.user_service import get_all_users

from pydantic import BaseModel, EmailStr

from db.models import User

router = APIRouter(prefix="/users", tags=["Users"])

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post(
    "/register",
    response_model=UserResponse
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return register_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    

@router.post("/login")
def login(
    payload: UserLogin,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == payload.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )

    if not verify_password(
        payload.password,
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Wrong password"
        )

    token = create_access_token(
        data={
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/", dependencies=[Depends(get_current_user)])
def fetch_users(db: Session = Depends(get_db)):
    return get_all_users(db)