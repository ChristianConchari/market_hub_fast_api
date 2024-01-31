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
