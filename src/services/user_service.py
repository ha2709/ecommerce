from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.models.user import User as UserModel   
from src.schemas.user import UserCreate       # Import your UserCreate schema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate) -> UserModel:
    # Hash the user password
    hashed_password = pwd_context.hash(user.password)
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Mock database to store verification tokens (replace with your database)
verification_tokens = {}
