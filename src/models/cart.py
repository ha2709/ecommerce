 

from typing import List, Optional

class CartItem:
    def __init__(self, product_id: str, quantity: int):
        self.product_id = product_id
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_id: str, quantity: int):
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product_id, quantity))

    def remove_item(self, product_id: str, quantity: Optional[int] = None):
        for item in self.items:
            if item.product_id == product_id:
                if quantity is None or item.quantity <= quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                return

    def get_cart_items(self) -> List[CartItem]:
        return self.items
