from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_async_db
from src.models.customer import Customer
from src.services.order_service import calculate_total_price
from src.utils.auth import get_current_user
from src.schemas.order import OrderCreate, Order
from typing import List

router = APIRouter()

@router.post("/orders/", response_model=Order, summary="Place an order")
async def place_order(
    order_create: OrderCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user: Customer = Depends(get_current_user),
):
    if current_user.user_id is None:
        raise HTTPException(status_code=401, detail="Only registered customers can place orders")

    total_price = await calculate_total_price(db, order_create.items, current_user)

    db_order = Order(customer_id=current_user.id, total_price=total_price, status="Placed")
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    return db_order

@router.get("/orders/history/", response_model=List[Order], summary="Fetch order history")
async def fetch_order_history(
    db: AsyncSession = Depends(get_async_db),
    current_user: Customer = Depends(get_current_user),
):
    result = await db.execute(select(Order).filter_by(customer_id=current_user.id))
    orders = result.scalars().all()

    return orders
