from config.database import Base
from sqlalchemy import Column, Integer, String, Float, List

class Product(Base):
    """
    Represents a product in the market hub.
    """

    __tablename__ = "products"    

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    rating = Column(Float, nullable=False)
    availableSizes = Column(List[String], nullable=True)
    colorOptions = Column(List[String], nullable=True)