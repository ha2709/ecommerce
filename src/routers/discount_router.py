from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_async_db
from src.models.user import User
from src.utils.auth import get_current_user
from src.models.discount import Discount
from src.models.customer_category import CustomerCategory
from src.schemas.discount import DiscountCreate, DiscountResponse
router = APIRouter()


# Define an endpoint to get the discount percentage for a specific customer and product category
@router.get("")
async def get_discount_percentage(
    customer_category: CustomerCategory,
    product_category: str,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
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


@router.post("", response_model=DiscountResponse, status_code=status.HTTP_201_CREATED)
async def create_discount(
    discount_data: DiscountCreate, 
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new discount configuration.
    """
    new_discount = Discount(
        percentage=discount_data.percentage,
        customer_category=discount_data.customer_category,
        product_category_id=discount_data.product_category_id,
     
    )
    async with db as session:
        session.add(new_discount)
        await session.commit()
        await session.refresh(new_discount)
        return new_discount