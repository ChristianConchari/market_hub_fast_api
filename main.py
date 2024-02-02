from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

from routers.product import product_router
from routers.user import user_router

app = FastAPI()
app.title = "Market Hub API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(product_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=['home'])
def message():
    """
    Returns a welcome message.
    """
    return HTMLResponse(content="<h1>Welcome to the Market Hub API</h1>", status_code=200)
