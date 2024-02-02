"""
This module contains the implementation of the product router, which handles the
CRUD operations for products.
"""
from typing import List
from fastapi import Path, Query, Depends
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session

from schemas.product import Product
from middlewares.jwt_bearer import JWTBearer

from services.product import ProductService

product_router = APIRouter()

@product_router.get("/products", tags=['products'], response_model=List[Product], status_code=200)
def get_products() -> List[Product]:
    """
    Retrieve a list of products.

    Returns:
        List[Product]: The list of products.
    """
    db = Session()
    products = ProductService(db).get_products()
    return JSONResponse(content=products, status_code=200)

@product_router.get("/products/{product_id}", tags=['products'], response_model=Product, status_code=200)
def get_product(product_id: int = Path(ge=1, le=2000)) -> Product:
    """
    Retrieve a product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        Product: The product object.

    Raises:
        HTTPException: If the product is not found.

    """
    db = Session()
    product = ProductService(db).get_product(product_id)

    if not product:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(product), status_code=200)

@product_router.get("/products/", tags=['products'], response_model=List[Product], status_code=200)
def get_products_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Product]:
    """
    Get products by category.

    Args:
        category (str): The category of the products.

    Returns:
        List[Product]: A list of products matching the specified category.

    Raises:
        JSONResponse: If no products are found, returns a JSON response with a 404 status code.
    """
    db = Session()
    product = ProductService(db).get_products_by_category(category)

    if not product:
        return JSONResponse(content={"message": "No products found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(product), status_code=200)

@product_router.post("/products",
                     tags=['products'],
                     response_model=dict,
                     status_code=201,
                     dependencies=[Depends(JWTBearer())]
                    )
def create_product(product: Product) -> dict:
    """
    Creates a new product.

    Args:
        product (Product): The product object to be created.

    Returns:
        dict: A dictionary containing the message "Product created successfully".

    Raises:
        None

    Examples:
        >>> product = Product(name="Example Product", price=10.99)
        >>> create_product(product)
        {'message': 'Product created successfully'}

    """
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(content={"message": "Product created successfully"}, status_code=201)

@product_router.put("/products/{id}", tags=['products'], dependencies=[Depends(JWTBearer())])
def update_product(product_id: int, product: Product):
    """
    Updates a product with the given product_id using the provided product data.

    Args:
        product_id (int): The ID of the product to be updated.
        product (Product): The updated product data.

    Returns:
        JSONResponse: The response containing the updated product data 
        or an error message if the product is not found.
    """
    db = Session()
    product = ProductService(db).update_product(product_id, product)
    
    if not product:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    return JSONResponse(content={
        "message": "Product updated successfully", 
        "data": product.dict()
    }, status_code=200)


@product_router.delete("/products/{id}",
                       tags=['products'],
                       response_model=dict,
                       status_code=200,
                       dependencies=[Depends(JWTBearer())]
                      )
def delete_product(product_id: int) -> dict:
    """
    Deletes a product from the list of products based on the given product ID.

    Args:
        product_id (int): The ID of the product to be deleted.

    Returns:
        dict: A dictionary containing the response message.

    Raises:
        None
    """
    db = Session()
    product = ProductService(db).get_product(product_id)
    
    if not product:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    ProductService(db).delete_product(product_id)
    return JSONResponse(content={"message": "Product deleted successfully"}, status_code=200)
