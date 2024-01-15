from fastapi import FastAPI
import subprocess
from src.routers import (
    user_router, 
    product_router, 
    discount_router, 
    customer_router, 
    cart_router, 
    order_router, 
    login_router)
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
app.include_router(cart_router.router, prefix="/cart")
app.include_router(customer_router.router, prefix="/customers")
app.include_router(discount_router.router, prefix="/discounts")
app.include_router(login_router.router, prefix="/login")
app.include_router(order_router.router, prefix="/order")
app.include_router(product_router.router, prefix="/products")
app.include_router(user_router.router, prefix="/users")


