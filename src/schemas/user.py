from pydantic import BaseModel, EmailStr

# User Create schema for incoming data
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User schema for outgoing data (e.g., for responses)
class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True  # Allows the model to work with ORM objects


class UserResponse(BaseModel):
    id: str  # UUID as a string
    email: str