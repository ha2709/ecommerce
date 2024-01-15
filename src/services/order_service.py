from typing import List
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.product import Product
from models.customer import Customer
from models.discount import Discount
from models.product_category import ProductCategory
from schemas.order import OrderItemCreate
from database import get_async_db  # Adjust this import according to your project structure

async def calculate_total_price(
    order_items: List[OrderItemCreate], 
    customer: Customer,
    db: AsyncSession = Depends(get_async_db)):
    total_price = 0.0

    for order_item in order_items:
        result = await db.execute(select(Product).filter_by(id=order_item.product_id))
        product = result.scalars().first()

        if product:
            original_price = product.price
            discount_percentage = await get_discount_percentage(product.category, customer, db)
            discounted_price = calculate_discounted_price(original_price, discount_percentage)
            total_price += discounted_price * order_item.quantity

    return total_price

async def get_discount_percentage(
    product_category: ProductCategory,
    customer: Customer, 
    db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(Discount).filter_by(
        customer_category=customer.category,
        product_category_id=product_category.id))
    discount = result.scalars().first()

    if discount:
        return discount.percentage
    else:
        return 0.0

def calculate_discounted_price(original_price, discount_percentage):
    return original_price - (original_price * discount_percentage / 100)
