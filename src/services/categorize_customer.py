from sqlalchemy.orm import Session
from src.models.customer import Customer, CustomerCategory
from src.models.order import Order
from src.models.order_threshold import OrderThreshold

def categorize_customers(db: Session):
    # Query all customers
    customers = db.query(Customer).all()

    for customer in customers:
        # Calculate the number of successful orders (you need to implement this logic)
        successful_orders_count = calculate_successful_orders_count(db, customer)

        # Determine the current category
        current_category = customer.categorize()

 

        # Check if the category needs to be updated
        if successful_orders_count > OrderThreshold.FIFTY.value and current_category != CustomerCategory.GOLD:
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.GOLD
        elif OrderThreshold.TWENTY.value < successful_orders_count <= OrderThreshold.FIFTY.value and current_category != CustomerCategory.SILVER:
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.SILVER
        elif successful_orders_count <= OrderThreshold.TWENTY.value and current_category != CustomerCategory.BRONZE:
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.BRONZE


    # Commit the changes to the database
    db.commit()


def calculate_successful_orders_count(db: Session, customer_id: str) -> int:
    # Query the database to retrieve successful orders for the customer
    successful_orders_count = (
        db.query(Order)
        .filter(Order.user_id == customer_id, Order.status == 'successful')
        .count()
    )
    return successful_orders_count