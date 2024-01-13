 
from typing import  Optional
from src.models.cart import ShoppingCart

# Create a shopping cart instance
shopping_cart = ShoppingCart()

def add_to_cart(product_id: str, quantity: int):
    shopping_cart.add_item(product_id, quantity)

def remove_from_cart(product_id: str, quantity: Optional[int] = None):
    shopping_cart.remove_item(product_id, quantity)

def get_cart_items():
    return shopping_cart.get_cart_items()
