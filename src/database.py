from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from src.models.token import VerificationToken

 
load_dotenv()
# DATABASE_URL = "postgresql://admin:1234@localhost/pinchi"
DATABASE_URL = os.environ.get("DATABASE_URL")
# print(12, DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Import all modules here that might define models so that
# they are registered properly on the metadata. Otherwise,
# SQLAlchemy might not be aware of them.
from src.models.user import User
from src.models.department import Department
from src.models.product import Product
from src.models.order import Order
from src.models.shopping_cart_item import ShoppingCartItem
from src.models.token import VerificationToken
from src.models.cart import CartItem
 
from src.models.customer import Customer
from src.models.discount import Discount
from src.models.order_item import OrderItem
from src.models.product_category import ProductCategory
from src.models.shopping_cart import ShoppingCart
 

# Create the tables
Base.metadata.create_all(bind=engine)
