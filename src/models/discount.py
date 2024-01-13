from sqlalchemy import Column, String, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.models.base import Base
from src.models.customer import CustomerCategory   

class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    
    # Foreign key relationships
    customer_category = Column(Enum(CustomerCategory), nullable=False)
    product_category_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'))

    # Discount percentage (e.g., 10% discount as 0.10)
    percentage = Column(Float, nullable=False)

    # Define a relationship with the Product model (assuming a one-to-many relationship)
    products = relationship('Product', back_populates='discount')
    
    # Define a relationship with the ProductCategory model
    product_category = relationship('ProductCategory', back_populates='discounts')
    
    def calculate_discounted_price(self, original_price):
        # Calculate the discounted price based on the percentage
        return original_price - (original_price * self.percentage)
