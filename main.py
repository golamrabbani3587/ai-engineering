from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import Base
from db.database import engine

from api.routes.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}