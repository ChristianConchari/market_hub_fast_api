from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    customer = "customer"

class User(BaseModel):
    """
    Represents a user in the system.
    """
    id : Optional[int] = None
    userName: str = Field(min_length=5, max_length=15)
    email: str = Field(min_length=5, max_length=15, type="email")
    password: str = Field(min_length=8, max_length=50, type="password")
    role: Role = Field(...)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "userName": "John Doe",
                "email": "johnDoe@email.com",
                "password": "Password123",
                "role": "customer"
            }
        }
    }
    