from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.product import Product, ProductCreate, ProductUpdate
from src.models.product import Product as DBProduct
# from src.models.department import Department
from src.utils.auth import get_current_user
from src.models.user import User


router = APIRouter()

# Get All Products
@router.get(
    "/products/", 
    response_model=list[Product], 
    summary="Get all products")
def get_all_products(db: Session = Depends(get_db)):
    """
    Get all products.

    Returns a list of all products.
    """
    products = db.query(DBProduct).all()
    return products
# Create Product
@router.post("/products/", response_model=Product, summary="Create a new product")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new product.

    - **product**: The product information (name, price, category_id).
    
    Returns the created product.
    """
    # Check if the product category belongs to the user's department
    if product.category.department_id != current_user.department_id:
        raise HTTPException(status_code=403, detail="You are not allowed to create products in this category")

    # Create the product in the database
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

# Update Product
@router.put("/products/{product_id}", response_model=Product, summary="Update a product")
def update_product(
    product_id: str,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update an existing product.

    - **product_id**: The ID of the product to update.
    - **product_update**: The updated product information (name, price, category_id).

    Returns the updated product.
    """
    # Check if the product exists
    db_product = db.query(Product).filter_by(id=product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Check if the product category belongs to the user's department
    if db_product.category.department_id != current_user.department_id:
        raise HTTPException(status_code=403, detail="You are not allowed to update products in this category")

    # Update the product
    for key, value in product_update.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product

# Delete Product
@router.delete("/products/{product_id}", summary="Delete a product")
def delete_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Delete an existing product.

    - **product_id**: The ID of the product to delete.
    
    Returns a success message.
    """
    # Check if the product exists
    db_product = db.query(Product).filter_by(id=product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Check if the product category belongs to the user's department
    if db_product.category.department_id != current_user.department_id:
        raise HTTPException(status_code=403, detail="You are not allowed to delete products in this category")

    # Delete the product
    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted successfully"}
