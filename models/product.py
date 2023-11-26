from pydantic import BaseModel, Field
from typing import Optional, List

class Product(BaseModel):
    id: Optional[int] = Field(default=None, ge=1, le=2000)
    name: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=100)
    price: float = Field(..., gt=0, le=100000)
    category: str = Field(..., min_length=5, max_length=50)
    rating: float = Field(..., gt=0, le=5)
    availableSizes: Optional[List[str]] = None
    colorOptions: Optional[List[str]] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Ultra Comfort Running Shoes",
                "description": "Lightweight and breathable running shoes with enhanced cushioning.",
                "price": 79.99,
                "category": "Footwear",
                "rating": 4.5,
                "availableSizes": ["7", "8", "9", "10", "11"],
                "colorOptions": ["Blue", "Black", "White"]
            }
        }
    }    