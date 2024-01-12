from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
 
from .database import SessionLocal
from src.schemas.user import UserCreate, UserResponse
from src.models.user import User
from src.services.user_service import create_user
 
 
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/users/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user