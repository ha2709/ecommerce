from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
 
from src.database import SessionLocal
# from src.schemas.user import UserCreate, UserResponse
# from src.models.user import User
# from src.services.user_service import create_user, send_verification_email
from src.routers import user 
 
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


app.include_router(user.router, prefix="/users") 

