from typing import List
from pydantic import BaseModel, UUID4, Field


class ShoppingCartBase(BaseModel):
    product_id: UUID4
    quantity: int


class ShoppingCartItemCreate(ShoppingCartBase):
    pass


class ShoppingCartItemUpdate(ShoppingCartBase):
    pass


class ShoppingCart(BaseModel):
    id: UUID4
    customer_id: UUID4
    items: List[ShoppingCartItemCreate]
