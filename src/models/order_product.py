from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.models.base import Base
class OrderProduct(Base):
    __tablename__ = 'order_products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'))
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
