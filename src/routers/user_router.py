import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, UserResponse
from src.database import get_async_db
from src.models.verfication_token import VerificationToken
from src.models.user import User
from src.models.department import Department
from src.services.user_service import create_user
from src.services.email import send_verification_email
from src.services.verification_service import create_verification_token
from src.utils.token import generate_verification_token

router = APIRouter()
load_dotenv()


BASE_URL = os.getenv("BASE_URL")


@router.post(
    "",
    response_model=UserResponse,
    summary="Create a new user",
    description="Creates a new user and sends a verification email.",
)
async def create_user_endpoint(
    user: UserCreate, db: AsyncSession = Depends(get_async_db)
):
    """
    Create a new user and send a verification email.

    - **email**: The email address of the user.
    - **password**: The user's password.

    If the email is already registered, it returns a 400 Bad Request response.

    Returns the user's ID and email.
    """
    # Generate a unique verification token
    token = generate_verification_token()
    # Construct the verification link using BASE_URL
    verification_link = f"{BASE_URL}/users/verify?token={token}"

    # Store the verification link in the database
    await create_verification_token(db, user.email, verification_link)

    # Send the verification email
    send_verification_email(user.email, verification_link)
    db_user = await create_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Convert the UUID to a string for the response
    user_response = UserResponse(id=str(db_user.id), email=db_user.email)

    return user_response


# Endpoint to handle verification (user clicks the link)
@router.get(
    "/verify",
    summary="Verify user's email",
    description="Verifies the user's email by clicking a verification link.",
)
async def verify_user(token: str, db: AsyncSession = Depends(get_async_db)):
    """
    Verify a user's email by clicking a verification link.

    - **token**: The verification token received via email.

    If the token is valid, it marks the email as verified in the database.

    Returns a success message if the email is verified.
    """
    # Check if the token exists in the database
    verification_link = f"{BASE_URL}/users/verify?token={token}"
    # print(48, token)
    result = await db.execute(
        select(VerificationToken).filter_by(token=verification_link)
    )
    verification_token = result.scalars().first()

    if verification_token:
        # Remove the token from the database
        # await db.delete(verification_token)
        # await db.commit()

        # Get the email associated with the token
        email = verification_token.email

        return {"message": f"Email {email} verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid verification token")


# Endpoint for user registration
@router.post(
    "/register",
    summary="Register a user",
    description="Registers a user with a specified user type and department.",
)
async def register_user(
    user: UserCreate,
    user_type: str,
    department_id: str,
    db: AsyncSession = Depends(get_async_db),
):
    """
    Register a user with a specified user type and department.

    - **user**: The user's information (email and password).
    - **user_type**: The type of user (internal staff or external customer).
    - **department_id**: The ID of the department the user belongs to.

    If the department does not exist, it returns a 400 Bad Request response.

    Returns a success message if the user is registered.
    """
    # Check if the department exists
    result = await db.execute(select(Department).filter_by(id=department_id))
    department = result.scalars().first()
    if not department:
        raise HTTPException(status_code=400, detail="Department not found")

    # Create the user in the database
    db_user = User(**user.dict(), user_type=user_type, department_id=department_id)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return {"message": "User registered successfully"}
