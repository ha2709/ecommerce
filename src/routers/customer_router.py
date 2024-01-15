from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_async_db
from src.models.customer import Customer
from src.models.order import Order

router = APIRouter()


# Define an endpoint to categorize customers based on successful orders
@router.get("/categorize/{user_id}", response_model=str)
async def categorize_customer(user_id: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously fetch the customer's data, including the number of successful orders,
    and categorize the customer based on that.
    """
    result = await db.execute(select(Customer).filter_by(id=user_id))
    customer = result.scalars().first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Categorize the customer based on the number of successful orders
    customer_category = customer.categorize()

    # Return the customer category as a string
    return customer_category.value
