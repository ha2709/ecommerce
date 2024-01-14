from sqlalchemy import Column,  Float, ForeignKey, Enum
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
    # Add a foreign key constraint to link to the Product model
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
 
    # Discount percentage (e.g., 10% discount as 0.10)
    percentage = Column(Float, nullable=False)

    # Define the relationship with a primaryjoin expression
    products = relationship('Product', primaryjoin='Discount.product_id == Product.id')
    
    # Define the relationship to ProductCategory with the foreign_keys argument
    product_category = relationship('ProductCategory', back_populates='discounts', foreign_keys=[product_category_id])
    
    def calculate_discounted_price(self, original_price):
        # Calculate the discounted price based on the percentage
        return original_price - (original_price * self.percentage)
