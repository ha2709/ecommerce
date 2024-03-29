from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from database import get_async_db
from schemas.product import Product, ProductCreate, ProductUpdate
from models.product import Product as DBProduct
from utils.auth import get_current_user
from models.user import User

router = APIRouter()


# Get All Products
@router.get("", response_model=list[Product], summary="Get all products")
async def get_all_products(
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(DBProduct))
    products = result.scalars().all()
    return products


# Create Product
@router.post("", response_model=Product, summary="Create a new product")
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    new_product = DBProduct(**product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


# Update Product
@router.put("/{product_id}", response_model=Product, summary="Update a product")
async def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    stmt = (
        update(DBProduct)
        .where(DBProduct.id == product_id)
        .values(**product_update.dict(exclude_unset=True))
    )
    await db.execute(stmt)
    await db.commit()
    return await db.get(DBProduct, product_id)


# Delete Product
@router.delete("/{product_id}", summary="Delete a product")
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_async_db),
    current_user: User = Depends(get_current_user),
):
    stmt = delete(DBProduct).where(DBProduct.id == product_id)
    await db.execute(stmt)
    await db.commit()
    return {"message": "Product deleted successfully"}
