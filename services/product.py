"""
This module contains the implementation of the product service, which handles the
CRUD operations for products.
"""
from models.product import Product as ProductModel
from schemas.product import Product

class ProductService():
    """
    This class contains the implementation of the product service, which handles the
    CRUD operations for products.
    """
    def __init__(self, db) -> None:
        """
        Initializes the database connection object.

        Args:
            db: The database connection object.
        """
        self.db = db
    
    def get_products(self):
        """
        Retrieves all products from the database.

        Returns:
            List[ProductModel]: A list of all products.
        """
        return self.db.query(ProductModel).all()

    def get_product(self, product_id: int):
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            ProductModel: The product object.
        """
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    def get_products_by_category(self, category: str):
        """
        Retrieves products by category.

        Args:
            category (str): The category of the products.

        Returns:
            List[ProductModel]: A list of products matching the specified category.
        """
        return self.db.query(ProductModel).filter(ProductModel.category == category).all()
    
    def create_product(self, product: Product):
        """
        Creates a new product.

        Args:
            product (Product): The product object to create.
        """
        new_product = ProductModel(**product.dict())   
        self.db.add(new_product)
        self.db.commit()
        return new_product
    
    def update_product(self, product_id: int, product: Product):
        """
        Updates a product by its ID.

        Args:
            product_id (int): The ID of the product to update.
            product (Product): The product object with the updated data.
        """
        product_to_update = self.get_product(product_id)
        for key, value in product.dict().items():
            setattr(product_to_update, key, value)
        self.db.commit()
        return product_to_update

    def delete_product(self, product_id: int):
        """
        Deletes a product by its ID.

        Args:
            product_id (int): The ID of the product to delete.
        """
        product_to_delete = self.get_product(product_id)
        self.db.delete(product_to_delete)
        self.db.commit()
        return {"message": "Product deleted successfully"}
