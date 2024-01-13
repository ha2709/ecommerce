# src/models/token.py

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
 
import uuid
from src.models.base import Base

class VerificationToken(Base):
    __tablename__ = 'verification_tokens'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, unique=True, index=True)
    token = Column(String, unique=True, nullable=False)
