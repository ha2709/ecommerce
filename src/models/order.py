from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models.base import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String)
    total_price = Column(Float)

    user = relationship("User", back_populates="orders")
    # Define a one-to-many relationship with OrderProduct

    # Add a foreign key to link to the Customer table
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="orders")
    # Rename this relationship to match the back_populates in OrderItem
    order_items = relationship("OrderItem", back_populates="order")
    # order_products = relationship('OrderProduct', backref=backref('order', uselist=False))
