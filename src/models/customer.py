from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from models.base import Base
from models.customer_category import CustomerCategory
from models.order_threshold import OrderThreshold


class Customer(Base):
    __tablename__ = "customers"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    email = Column(String, unique=True, index=True)
    successful_orders = Column(Integer, default=0)  # Number of successful orders

    # Use backref to create the reverse relationship
    user = relationship("User", back_populates="customer", uselist=False)

    # Define a relationship with orders and specify the primaryjoin expression
    orders = relationship(
        "Order",
        back_populates="customer",
        primaryjoin="Customer.id == Order.customer_id",
    )

    # Categorization logic
    def categorize(self):
        if 0 <= self.successful_orders <= OrderThreshold.TWENTY.value:
            return CustomerCategory.BRONZE
        elif (
            OrderThreshold.TWENTY.value
            < self.successful_orders
            <= OrderThreshold.FIFTY.value
        ):
            return CustomerCategory.SILVER
        else:
            return CustomerCategory.GOLD
