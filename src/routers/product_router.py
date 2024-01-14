from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_async_db
from src.schemas.product import Product, ProductCreate, ProductUpdate
from src.models.product import Product as DBProduct
# from src.models.department import Department
from src.utils.auth import get_current_user
from src.models.user import User

router = APIRouter()

# Get All Products
@router.get("/products/", response_model=list[Product], summary="Get all products")
async def get_all_products(db: AsyncSession = Depends(get_async_db)):
    """
    Get all products asynchronously.

    Returns a list of all products.
    """
    result = await db.execute(select(DBProduct))
    products = result.scalars().all()
    return products

# Create Product
@router.post("/products/", response_model=Product, summary="Create a new product")
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    # Function body here

# Update Product
@router.put("/products/{product_id}", response_model=Product, summary="Update a product")
async def update_product(
    product_id: str,
    product_update: ProductUpdate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    # Function body here

# Delete Product
@router.delete("/products/{product_id}", summary="Delete a product")
async def delete_product(
    product_id: str,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    # Function body here
