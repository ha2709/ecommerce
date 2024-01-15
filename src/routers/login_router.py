from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
# from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import  timedelta
from src.utils.auth import create_access_token
from src.services.user_service import authenticate_user
from src.models.token import Token
from src.database import get_async_db
router = APIRouter()
# The token expires after 60 minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 60
@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_async_db)):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
