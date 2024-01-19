from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.customer import Customer, CustomerCategory
from models.order import Order
from models.order_threshold import OrderThreshold


async def categorize_customers(db: AsyncSession):
    # Asynchronously query all customers
    result = await db.execute(select(Customer))
    customers = result.scalars().all()

    for customer in customers:
        # Calculate the number of successful orders asynchronously
        successful_orders_count = await calculate_successful_orders_count(
            db, customer.id
        )

        # Determine the current category
        current_category = customer.categorize()
        # Check if the category needs to be updated
        if (
            successful_orders_count > OrderThreshold.FIFTY.value
            and current_category != CustomerCategory.GOLD
        ):
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.GOLD
        elif (
            OrderThreshold.TWENTY.value
            < successful_orders_count
            <= OrderThreshold.FIFTY.value
            and current_category != CustomerCategory.SILVER
        ):
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.SILVER
        elif (
            successful_orders_count <= OrderThreshold.TWENTY.value
            and current_category != CustomerCategory.BRONZE
        ):
            customer.successful_orders = successful_orders_count
            customer.user.customer_category = CustomerCategory.BRONZE

    # Asynchronously commit the changes to the database
    await db.commit()


async def calculate_successful_orders_count(db: AsyncSession, customer_id: str) -> int:
    # Asynchronously query the database to retrieve successful orders for the customer
    result = await db.execute(
        select(Order).filter(Order.user_id == customer_id, Order.status == "successful")
    )
    successful_orders = result.scalars().all()
    return len(successful_orders)
