from sqlalchemy.orm import Session
from src.models.token import VerificationToken

def create_verification_token(db: Session, email: str, token: str):
    db_token = VerificationToken(email=email, token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token