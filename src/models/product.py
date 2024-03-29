from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models.base import Base

# from models.association import association_table
from models.shopping_cart import ShoppingCart


class Product(Base):
    __tablename__ = "products"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, index=True)
    price = Column(Float)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"))
    # Foreign key to Discount
    discount_id = Column(UUID(as_uuid=True), ForeignKey("discounts.id"))
    # Relationship with Discount
    discount = relationship("Discount", back_populates="products")
    # Foreign key to ProductCategory
    category_id = Column(UUID(as_uuid=True), ForeignKey("product_categories.id"))

    # Relationship with ProductCategory
    category = relationship("ProductCategory", back_populates="products")

    department = relationship("Department", back_populates="products")
    # Define a many-to-one relationship with Order

    order_products = relationship("OrderProduct", backref="product")

    order_items = relationship("OrderItem", backref="product_order_item")

    cart_items = relationship("ShoppingCart", backref="product")
