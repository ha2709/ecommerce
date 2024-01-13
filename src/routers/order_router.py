from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db

from src.models.customer import Customer

from src.services.order_service import calculate_total_price
from src.utils.auth import get_current_user
from src.schemas.order import OrderCreate, Order
from typing import List

router = APIRouter()

@router.post("/orders/", response_model=Order, summary="Place an order")
def place_order(
    order_create: OrderCreate,
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user),
):
    """
    Place an order based on the items in the shopping cart.

    - **order_create**: The order information (customer_id, items).
    
    Returns the created order.
    """
    # Check if the customer is registered
    if current_user.user_id is None:
        raise HTTPException(status_code=401, detail="Only registered customers can place orders")

    # Implement logic to calculate the total price of the order, considering discounts
    total_price = calculate_total_price(db,order_create.items, current_user)

    # Create the order in the database
    db_order = Order(customer_id=current_user.id, total_price=total_price, status="Placed")
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # You can also update the successful orders count for the customer here
    # Example: current_user.successful_orders += 1
    # Save the updated customer information to the database

    return db_order

@router.get("/orders/history/", response_model=List[Order], summary="Fetch order history")
def fetch_order_history(
    db: Session = Depends(get_db),
    current_user: Customer = Depends(get_current_user),
):
    """
    Fetch the order history for the current customer.
    
    Returns a list of order history.
    """
    # Fetch the order history for the current customer
    orders = db.query(Order).filter_by(customer_id=current_user.id).all()

    return orders
