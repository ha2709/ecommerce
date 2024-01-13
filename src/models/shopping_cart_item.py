from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.models.base import Base

class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_items'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    quantity = Column(Integer)
    shopping_cart_id = Column(UUID(as_uuid=True), ForeignKey('shopping_carts.id'))  # Add this line

    # Define a relationship with the Product model
    product = relationship('Product', back_populates='shopping_cart_items')

    # Define a relationship with the ShoppingCart model
    shopping_cart = relationship('ShoppingCart', back_populates='items')