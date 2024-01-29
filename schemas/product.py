from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class Size(str, Enum):
    S7 = "7"
    S8 = "8"
    S9 = "9"
    S10 = "10"
    S11 = "11"

class Color(str, Enum):
    Blue = "Blue"
    Black = "Black"
    White = "White"

class Product(BaseModel):
    id: Optional[int] = Field(default=None, ge=1, le=2000)
    name: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=100)
    price: float = Field(..., gt=0, le=100000)
    category: str = Field(..., min_length=5, max_length=50)
    rating: float = Field(..., gt=0, le=5)
    availableSizes: Optional[List[Size]] = None
    colorOptions: Optional[List[Color]] = None

model_config = {
    "json_schema_extra": {
        "example": {
            "name": "Ultra Comfort Running Shoes",
            "description": "Lightweight and breathable running shoes with enhanced cushioning.",
            "price": 79.99,
            "category": "Footwear",
            "rating": 4.5,
            "availableSizes": [Size.S7, Size.S8, Size.S9, Size.S10, Size.S11],
            "colorOptions": [Color.Blue, Color.Black, Color.White]
        }
    }
}