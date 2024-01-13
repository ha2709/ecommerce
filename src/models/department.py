from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.models.base import Base

class Department(Base):
    __tablename__ = 'departments'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    
    # Define a relationship with the User model
    users = relationship('User', back_populates='department')
    products = relationship('Product', back_populates='department')
    # Define a relationship with the ProductCategory model
    product_categories = relationship('ProductCategory', back_populates='department')