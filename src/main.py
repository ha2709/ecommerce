from fastapi import FastAPI
 
from src.routers import user_router, product_router, discount_router, customer_router, cart_router, order_router
import subprocess
 
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Define a route to trigger the scheduler externally
@app.get("/run-scheduler")
def run_scheduler():
    try:
        subprocess.run(["python", "scripts/scheduler.py"], check=True)
        return {"message": "Scheduler executed successfully."}
    except Exception as e:
        return {"message": f"Scheduler failed: {str(e)}"}

# Include  user router
app.include_router(user_router.router, prefix="/users")
app.include_router(product_router.router, prefix="/products")
app.include_router(discount_router.router, prefix="/discounts")
app.include_router(customer_router.router, prefix="/customers")
app.include_router(cart_router.router, prefix="/cart")
app.include_router(order_router.router, prefix="/order")