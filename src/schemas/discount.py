from pydantic import BaseModel, UUID4
from typing import Optional
from src.models.customer_category import CustomerCategory  # Enum for customer categories

class DiscountCreate(BaseModel):
    percentage: float
    customer_category: CustomerCategory
    product_category_id: UUID4

class DiscountResponse(BaseModel):
    id: UUID4
    percentage: float
    customer_category: CustomerCategory
    product_category_id: UUID4

    class Config:
        orm_mode = True
