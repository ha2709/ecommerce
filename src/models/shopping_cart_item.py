from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models.base import Base

class ShoppingCartItem(Base):
    __tablename__ = "shopping_cart_items"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    quantity = Column(Integer)
    # Add a foreign key reference to the ShoppingCart model
    shopping_cart_id = Column(UUID(as_uuid=True), ForeignKey("shopping_cart.id"))

    product = relationship("Product")
    shopping_cart = relationship("ShoppingCart", back_populates="items")
