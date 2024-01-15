from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_async_db
from src.models.discount import Discount
from src.models.customer_category import CustomerCategory

router = APIRouter()


# Define an endpoint to get the discount percentage for a specific customer and product category
@router.get("/discount/")
async def get_discount_percentage(
    customer_category: CustomerCategory,
    product_category: str,
    db: AsyncSession = Depends(get_async_db),
):
    """
    Asynchronously fetch the discount for the given customer category and product category.
    """
    result = await db.execute(
        select(Discount).filter_by(
            customer_category=customer_category, product_category=product_category
        )
    )
    discount = result.scalars().first()

    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")

    return {"discount_percentage": discount.percentage}
