from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.models.base import Base
from src.models.customer_category import CustomerCategory
from src.models.order_threshold import OrderThreshold
 

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    successful_orders = Column(Integer, default=0)  # Number of successful orders

    # Define a relationship with the User model (assuming a one-to-one relationship)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User', back_populates='customer')
    # Define a relationship to orders
    orders = relationship("Order", back_populates="customer")

    # Categorization logic
    def categorize(self):
        if 0 <= self.successful_orders <= OrderThreshold.TWENTY.value:
            return CustomerCategory.BRONZE
        elif OrderThreshold.TWENTY.value < self.successful_orders <= OrderThreshold.FIFTY.value:
            return CustomerCategory.SILVER
        else:
            return CustomerCategory.GOLD
