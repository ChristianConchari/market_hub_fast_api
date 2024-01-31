"""
This module contains the implementation of the user router, which handles the
user authentication and login functionality.
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

from data.users_data import users

user_router = APIRouter()

@user_router.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    """
    Logs in a user and returns a token.

    Args:
        user (User): The user object containing email, password, and userName.

    Returns:
        dict: A dictionary containing the token.

    """
    for item in users:
        if (item['userName'] == user.userName) and (item['email'] == user.email) and (item['password'] == user.password):
            token: str = create_token(user.dict())
            return JSONResponse(content={"token": token}, status_code=200)
