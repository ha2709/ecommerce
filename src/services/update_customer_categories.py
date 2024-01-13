from sqlalchemy.orm import Session
from src.models.customer import Customer, CustomerCategory

def update_customer_categories(db: Session):
    # Define the thresholds for category upgrades
    bronze_threshold = 20
    silver_threshold = 50

    # Retrieve customers who need category updates
    customers_to_update = db.query(Customer).filter(Customer.order_count >= bronze_threshold).all()

    for customer in customers_to_update:
        if customer.order_count < silver_threshold:
            # Move from Bronze to Silver
            customer.category = CustomerCategory.SILVER
        else:
            # Move from Silver to Gold
            customer.category = CustomerCategory.GOLD

    db.commit()
