from typing import List
from fastapi import  Depends
from src.models.product import Product
from src.models.customer import Customer
from src.models.discount import Discount

from src.models.customer import Customer
from src.models.product_category import ProductCategory
from src.schemas.order import OrderItemCreate
from sqlalchemy.orm import Session
from src.database import get_async_db
from typing import List

def calculate_total_price(
    order_items: List[OrderItemCreate], 
    customer: Customer,
    db: Session = Depends(get_async_db), 
    ):
    total_price = 0.0

    # Iterate through the order items
    for order_item in order_items:
        product = db.query(Product).filter_by(id=order_item.product_id).first()

        if product:
            # Calculate the original price of the product
            original_price = product.price

            # Apply discounts based on customer category and product category
            discount_percentage = get_discount_percentage(db, customer, product.category)
            discounted_price = calculate_discounted_price(original_price, discount_percentage)

            # Add the discounted price to the total
            total_price += discounted_price * order_item.quantity

    return total_price

def get_discount_percentage(
    product_category: ProductCategory,
    customer: Customer, 
    db: Session = Depends(get_async_db)):
    # Query the discounts table to get the discount percentage based on customer category and product category
    discount = db.query(Discount).filter_by(
        customer_category=customer.category,
        product_category_id=product_category.id
    ).first()

    if discount:
        return discount.percentage
    else:
        return 0.0

def calculate_discounted_price(original_price, discount_percentage):
    return original_price - (original_price * discount_percentage)

# You can then use this `calculate_total_price` function in the order creation endpoint.
