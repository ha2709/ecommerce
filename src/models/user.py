from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
import uuid
from models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_staff = Column(Boolean, default=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"))
    # Define a relationship with the Department model
    department = relationship("Department", back_populates="users")

    orders = relationship("Order", back_populates="user")

    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="user")
