# add docstring
"""
This module contains the implementation of the JWTBearer class, which is a
middleware for JWT Bearer authentication.

This class extends the HTTPBearer class and provides the implementation for
validating JWT tokens in the Authorization header of the request.
"""
import logging
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    """
    Middleware class for JWT Bearer authentication.

    Attributes:
        None

    Methods:
        __call__(self, request: Request): Validates the JWT token and checks
            if the user is authenticated.

    Raises:
        HTTPException: If the token is invalid or expired, or if the user
            credentials are invalid.

    Returns:
        None
    """
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if not data or 'email' not in data:
            raise HTTPException(status_code=403, detail="Invalid token or expired")
        if data['email'] != "admin@admin.com": #TODO: Avoid hardcoding the email
            raise HTTPException(status_code=403, detail="Invalid credentials")
        logging.info("User %s has authenticated successfully", data['email'])
