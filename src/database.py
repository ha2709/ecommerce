from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv 
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
load_dotenv()
DATABASE_URL = "postgresql://admin:1234@localhost/pinchi"
# DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL  )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

 
# Import all modules here that might define models so that
# they are registered properly on the metadata. Otherwise,
# SQLAlchemy might not be aware of them.
from src.models.user import User
from src.models.department import Department
from src.models.product import Product
from src.models.order import Order
from src.models.shopping_cart import ShoppingCartItem


# Create the tables
Base.metadata.create_all(bind=engine)