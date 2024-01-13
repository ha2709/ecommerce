
from typing import List, Optional

from src.models.shopping_cart_item import ShoppingCartItem

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_id: str, quantity: int):
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += quantity
                return 
        self.items.append(ShoppingCartItem(product_id=product_id, quantity=quantity))

    def remove_item(self, product_id: str, quantity: Optional[int] = None):
        for item in self.items:
            if item.product_id == product_id:
                if quantity is None or item.quantity <= quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                return

    def get_cart_items(self) -> List[ShoppingCartItem]:
        return self.items