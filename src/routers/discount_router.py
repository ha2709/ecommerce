from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.discount import Discount
from src.models.customer_category import CustomerCategory
# from typing import Optional

router = APIRouter()

# Define an endpoint to get the discount percentage for a specific customer and product category
@router.get("/discount/")
async def get_discount_percentage(
    customer_category: CustomerCategory,
    product_category: str,
    db: Session = Depends(get_db)
):
    # Fetch the discount for the given customer category and product category
    discount = db.query(Discount).filter_by(
        customer_category=customer_category,
        product_category=product_category
    ).first()
    
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")

    return {"discount_percentage": discount.percentage}
