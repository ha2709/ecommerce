import os
from dotenv import load_dotenv 
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.schemas.user import UserCreate, UserResponse
from src.database import SessionLocal
from src.models.token import VerificationToken
from src.services.user_service import  create_user
from src.services.email import send_verification_email
from src.database import create_verification_token
from src.utils.token import generate_verification_token
router = APIRouter()
load_dotenv()
 

BASE_URL = os.getenv("BASE_URL")

@router.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(SessionLocal)):
    
    # Generate a unique verification token (replace with your logic)
    verification_token = generate_verification_token()
    # Construct the verification link using BASE_URL
    verification_link = f"{BASE_URL}/verify?token={verification_token}"

 
    # Store the verification link in the database
    token = create_verification_token(db, user.email, verification_link)

     # Send the verification email
    send_verification_email(user.email, verification_link)
    db_user = create_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Convert the UUID to a string for the response
    user_response = UserResponse(id=str(db_user.id), email=db_user.email)

    return user_response



# Endpoint to handle verification (user clicks the link)

@router.get("/verify/")
async def verify_user(token: str, db: Session = Depends(SessionLocal)):
    # Check if the token exists in the database
    verification_token = db.query(VerificationToken).filter_by(token=token).first()

    if verification_token:
        # Mark the email as verified in your database (replace with your database logic)
        # Remove the token from the database (optional)
        db.delete(verification_token)
        db.commit()
        
        # Get the email associated with the token
        email = verification_token.email
        
        return {"message": f"Email {email} verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid verification token")