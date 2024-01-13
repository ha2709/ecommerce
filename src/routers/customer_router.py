from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.customer import Customer
from src.models.order import Order

router = APIRouter()

 

# Define an endpoint to categorize customers based on successful orders
@router.get("/categorize/{user_id}", response_model=str)
async def categorize_customer(user_id: str, db: Session = Depends(get_db)):
    # Fetch the customer's data, including the number of successful orders
    customer = db.query(Customer).filter_by(id=user_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

   # Categorize the customer based on the number of successful orders
    customer_category = customer.categorize()
    
    # Return the customer category as a string
    return customer_category.value  

 