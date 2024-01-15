from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_async_db
from models.shopping_cart import ShoppingCart as DBShoppingCart
from models.shopping_cart_item import ShoppingCartItem
from schemas.shopping_cart import (
    ShoppingCart,
    ShoppingCartItemCreate,
    ShoppingCartItemUpdate,
)
from models.user import User
from utils.auth import get_current_user
 
router = APIRouter()

 

# Get Shopping Cart
@router.get(
    "", response_model=ShoppingCart, summary="Get the shopping cart"
)
async def get_shopping_cart(
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    """
    Asynchronously get the shopping cart for the current user.
    """
    result = await db.execute(
        select(DBShoppingCart).filter_by(customer_id=current_user.id)
    )
    db_shopping_cart = result.scalars().first()

    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    return db_shopping_cart

 
 
# Add Product to Shopping Cart
@router.post(
    "/add_product", 
    summary="Add a product to the shopping cart"
)
async def add_product_to_shopping_cart(
    item: ShoppingCartItemCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    # """
    # Asynchronously add a product to the shopping cart for the current user.
    # """
    print(52)

    result = await db.execute(select(DBShoppingCart).filter_by(product_id=item.product_id))
    db_shopping_cart = result.scalars().first()

    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    existing_item = next((i for i in db_shopping_cart.items if i.product_id == item.product_id), None)

    if existing_item:
        existing_item.quantity += item.quantity
    else:
        db_shopping_cart.items.append(ShoppingCartItem(**item.dict(), shopping_cart=db_shopping_cart))

    await db.commit()

    # product = Product.query.filter(Product.id == product_id)
    # cart_item = CartItem(product=product)
    # db.session.add(cart_item)
    # db.session.commit()

    return {"message": "Product added to the shopping cart successfully"}

    


# Remove Product from Shopping Cart
@router.post(
    "/remove_product", summary="Remove a product from the shopping cart"
)
async def remove_product_from_shopping_cart(
    item: ShoppingCartItemUpdate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    """
    Asynchronously remove a product from the shopping cart for the current user.
    """
    result = await db.execute(
        select(DBShoppingCart).filter_by(customer_id=current_user.id)
    )
    db_shopping_cart = result.scalars().first()
    if not db_shopping_cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    existing_item = next(
        (i for i in db_shopping_cart.items if i.product_id == item.product_id), None
    )

    if existing_item:
        if item.quantity is None or existing_item.quantity <= item.quantity:
            db_shopping_cart.items.remove(existing_item)
        else:
            existing_item.quantity -= item.quantity

        await db.commit()

    return {"message": "Product removed from the shopping cart successfully"}
