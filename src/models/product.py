from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.models.base import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    price = Column(Float)
    department_id = Column(UUID(as_uuid=True), ForeignKey('departments.id'))
    category_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'))
    # Define a relationship with the ProductCategory model
    category = relationship('ProductCategory', back_populates='products')
    department = relationship('Department', back_populates='products')
