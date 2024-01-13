from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.shopping_cart import ShoppingCart as DBShoppingCart
from src.schemas.shopping_cart import ShoppingCart, ShoppingCartItemCreate, ShoppingCartItemUpdate
from src.utils.auth import get_current_user

router = APIRouter()

# Get Shopping Cart
@router.get("/shopping_cart/", response_model=ShoppingCart, summary="Get the shopping cart")
def get_shopping_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get the shopping cart for the current user.

    Returns the shopping cart items for the current user.
    """
    # Query the shopping cart for the current user
    db_shopping_cart = db.query(DBShoppingCart).filter_by(customer_id=current_user.id).first()

    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    return db_shopping_cart

# Add Product to Shopping Cart
@router.post("/shopping_cart/add_product/", summary="Add a product to the shopping cart")
def add_product_to_shopping_cart(
    item: ShoppingCartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Add a product to the shopping cart for the current user.

    - **item**: The product item to add to the shopping cart (product_id, quantity).

    Returns a success message.
    """
    # Query the shopping cart for the current user
    db_shopping_cart = db.query(DBShoppingCart).filter_by(customer_id=current_user.id).first()

    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    # Check if the product item already exists in the shopping cart
    existing_item = next((i for i in db_shopping_cart.items if i.product_id == item.product_id), None)

    if existing_item:
        # Update the quantity of the existing item
        existing_item.quantity += item.quantity
    else:
        # Add the new item to the shopping cart
        db_shopping_cart.items.append(DBShoppingCartItem(**item.dict(), shopping_cart=db_shopping_cart))

    db.commit()

    return {"message": "Product added to the shopping cart successfully"}

# Remove Product from Shopping Cart
@router.post("/shopping_cart/remove_product/", summary="Remove a product from the shopping cart")
def remove_product_from_shopping_cart(
    item: ShoppingCartItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Remove a product from the shopping cart for the current user.

    - **item**: The product item to remove from the shopping cart (product_id, quantity).

    Returns a success message.
    """
    # Query the shopping cart for the current user
    db_shopping_cart = db.query(DBShoppingCart).filter_by(customer_id=current_user.id).first()

    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    # Check if the product item exists in the shopping cart
    existing_item = next((i for i in db_shopping_cart.items if i.product_id == item.product_id), None)

    if existing_item:
        if item.quantity is None or existing_item.quantity <= item.quantity:
            # Remove the item from the shopping cart
            db_shopping_cart.items.remove(existing_item)
        else:
            # Reduce the quantity of the existing item
            existing_item.quantity -= item.quantity

        db.commit()

    return {"message": "Product removed from the shopping cart successfully"}
