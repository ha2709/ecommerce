from sqlalchemy import Column, String,  ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.models.base import Base

class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, unique=True, index=True)
    department_id = Column(UUID(as_uuid=True), ForeignKey('departments.id'))
    discount_id = Column(UUID(as_uuid=True), ForeignKey('discounts.id'))
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    # Define a relationship with the Department model
    department = relationship('Department', back_populates='product_categories')
    products = relationship('Product', back_populates='category')
    # Define the one-to-many relationship with the Discount model
    discounts = relationship('Discount', back_populates='product_category')
