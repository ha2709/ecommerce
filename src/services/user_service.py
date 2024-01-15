from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import User as UserModel
from schemas.user import UserCreate
from sqlalchemy.future import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate
from models.user import User as UserModel
from passlib.context import CryptContext
from models.user import User
# Create a password context instance
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(db: AsyncSession, user: UserCreate) -> UserModel:
    """
    Asynchronously create a new user in the database.

    Args:
    - db (AsyncSession): The SQLAlchemy asynchronous session.
    - user (UserCreate): The user schema with user data.

    Returns:
    - UserModel: The created user model instance.
    """
    # Hash the user password
    hashed_password = pwd_context.hash(user.password)
    
    # Create a new user instance
    db_user = UserModel(email=user.email, hashed_password=hashed_password)

    # Add and commit the new user to the database
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user


async def authenticate_user(email: str, password: str, db: AsyncSession):
    print(44, "authenticate_user ",email)
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalars().first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

