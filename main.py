from fastapi import FastAPI, Body, Path, Query, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional, List
from fastapi.security import HTTPBearer

from jwt_manager import create_token, validate_token

from models.product import Product
from models.user import User

from utils.utils import find_product_by_id

from data.products_data import products
from data.users_data import users

app = FastAPI()
app.title = "Market Hub API"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        print(data)
        if data['email'] not in [item['email'] for item in users]:
            raise HTTPException(status_code=403, detail="Invalid credentials")

@app.get("/", tags=['home'])
def message():
    return HTMLResponse("<h1>Welcome to my API</h1>")

@app.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    for item in users:
        if item['email'] == user.email and item['password'] == user.password and item['userName'] == user.userName:
            print(item)
            token: str = create_token(user.dict())
            return JSONResponse(content={"token": token}, status_code=200)
        
    return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)

@app.get("/products", tags=['products'], response_model=List[Product], status_code=200)
def get_products() -> List[Product]:
    return JSONResponse(content=products, status_code=200)

@app.get("/products/{id}", tags=['products'], response_model=Product, status_code=200)
def get_product(id: int = Path(ge=1, le=2000)) -> Product:
    for item in products:
        if item['id'] == id:
            return JSONResponse(content=item, status_code=200)
    return JSONResponse(content={"message": "Product not found"}, status_code=404)

@app.get("/products/", tags=['products'], response_model=List[Product], status_code=200)
def get_products_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Product]:
    result = [ item for item in products if item['category'] == category ]

    if len(result) == 0:
        return JSONResponse(content={"message": "No products found"}, status_code=404)
    else:
        return JSONResponse(content=result, status_code=200)
        

@app.post("/products", tags=['products'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_product(product: Product) -> dict:
    new_id = products[-1]['id'] + 1
    product.id = new_id
    products.append(product.dict())
    return JSONResponse(content={"message": "Product created successfully"}, status_code=201)

@app.put("/products/{id}", tags=['products'], dependencies=[Depends(JWTBearer())])
def update_product(id: int, product: Product):
    product.id = id
    item = find_product_by_id(id, products)
    if not item:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)

    for field, value in product.dict().items():
        item[field] = value

    return JSONResponse(content={
        "message": "Product updated successfully", 
        "data": item
    }, status_code=200)


@app.delete("/products/{id}", tags=['products'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_product(id: int) -> dict:
    deleted_product = [item for item in products if item['id'] == id]
    
    if deleted_product:
        products.remove(deleted_product[0])
        return JSONResponse(content={
            "message": "Product deleted successfully", 
        }, status_code=200)
        
    return JSONResponse(content={"message": "Product not found"}, status_code=404)
