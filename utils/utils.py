from typing import List
from models.product import Product

def find_product_by_id(product_id: int, products: List[Product]):
    for item in products:
        if item['id'] == product_id:
            return item
    return None
