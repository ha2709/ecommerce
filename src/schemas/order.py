from typing import List
from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class Order(BaseModel):
    id: str
    user_id: str
    status: str
    total_price: float
