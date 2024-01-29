from config.database import Base
from sqlalchemy import Column, Integer, String, Enum

class User(Base):
    """
    Represents a user in the system.
    """

    __tablename__ = "users"    

    id = Column(Integer, primary_key=True)
    userName = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(Enum('admin', 'customer'), nullable=False)