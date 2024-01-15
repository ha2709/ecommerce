import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from routers import (
    user_router, 
    product_router, 
    discount_router, 
    customer_router, 
    cart_router, 
    order_router, 
    login_router)
app = FastAPI()
load_dotenv()
FRONTEND_URL = os.getenv("FRONTEND_URL")
BASE_URL = os.getenv("BASE_URL")

# List of allowed origins (use "*" to allow all origins)
origins = [
    "*",
    FRONTEND_URL,
    BASE_URL
]

# Add middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can allow specific origins or use ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
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

 
app.include_router(cart_router.router, prefix="/cart")
app.include_router(customer_router.router, prefix="/customers")
app.include_router(discount_router.router, prefix="/discounts")
app.include_router(login_router.router, prefix="/login")
app.include_router(order_router.router, prefix="/order")
app.include_router(product_router.router, prefix="/products")
app.include_router(user_router.router, prefix="/users")


