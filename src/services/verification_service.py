from sqlalchemy.ext.asyncio import AsyncSession
from src.models.token import VerificationToken

async def create_verification_token(db: AsyncSession, email: str, token: str):
    db_token = VerificationToken(email=email, token=token)
    db.add(db_token)
    await db.commit()  # Use await for the commit
    await db.refresh(db_token)  # Use await for the refresh
    return db_token