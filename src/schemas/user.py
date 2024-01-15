from pydantic import BaseModel, EmailStr


# User Create schema for incoming data
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# User schema for outgoing data (e.g., for responses)
class UserResponse(BaseModel):
    id: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows the model to work with ORM objects
