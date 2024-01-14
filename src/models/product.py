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
    # order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'))
    # Define the relationship to ProductCategory with the foreign_keys argument
    category = relationship('ProductCategory', back_populates='products', foreign_keys=[category_id])
    department = relationship('Department', back_populates='products')
    # Define the relationship to Order (many-to-one)
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'))
    order = relationship('Order', back_populates='products_association')
    ## Define the many-to-many relationship to Order via OrderProduct
    # orders_association = relationship('Order', secondary='order_products', back_populates='products_association')