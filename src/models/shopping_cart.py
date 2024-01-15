from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from models.base import Base

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
 
    product_id = Column(
        UUID(as_uuid=True), ForeignKey("products.id")
    )
    items = relationship("ShoppingCartItem", back_populates="shopping_cart")