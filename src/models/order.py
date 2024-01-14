from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.models.base import Base
from src.models.order_product import OrderProduct

class Order(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    # user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    status = Column(String)
    total_price = Column(Float)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.id'))
   
    # user = relationship('User', back_populates='orders')
   
    # Define a relationship with the Customer model (optional)
    customer = relationship('Customer', back_populates='orders')
    
    # Define the relationship to the OrderProduct association table
    # products = relationship('OrderProduct', back_populates='order')
     # Define a relationship to Product (one-to-many)
    products_association = relationship('Product', back_populates='order', foreign_keys='[Product.order_id]')
    def add_product(self, product):
        # Create an association between the order and a product
        order_product = OrderProduct(order=self, product=product)
        self.products.append(order_product)

    def remove_product(self, product):
        # Remove the association between the order and a product
        order_product = next((op for op in self.products if op.product == product), None)
        if order_product:
            self.products.remove(order_product)
