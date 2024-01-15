from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from src.models.base import Base


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    # Define the relationship to items
    items = relationship("ShoppingCartItem", back_populates="shopping_cart")
