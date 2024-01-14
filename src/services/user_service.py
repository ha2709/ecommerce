from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from src.models.user import User as UserModel
from src.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: AsyncSession, user: UserCreate) -> UserModel:
    # Hash the user password
    hashed_password = pwd_context.hash(user.password)
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()  # Use await for the commit
    await db.refresh(db_user)  # Use await for the refresh
    return db_user
