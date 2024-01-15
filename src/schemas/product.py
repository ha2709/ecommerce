from pydantic import BaseModel
from uuid import UUID

# from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: float
    category_id: UUID


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: UUID

    class Config:
        orm_mode = True
