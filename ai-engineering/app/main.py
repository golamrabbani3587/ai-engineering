from fastapi import FastAPI

from app.database import engine, Base
from app.routes.user import router as user_router

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Engineering API")

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "AI Engineering API is running"}
