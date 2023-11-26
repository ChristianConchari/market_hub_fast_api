from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    userName: str = Field(min_length=5, max_length=15)
    email: str = Field(min_length=5, max_length=15, type="email")
    password: str = Field(min_length=8, max_length=50, type="password")
    role: str = Field(..., pattern="^(admin|customer)$")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "userName": "customer",
                "email": "user@mail.com",
                "password": "Hola1234",
                "role": "admin"
            }
        }
    }