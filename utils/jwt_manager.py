from jwt import encode, decode, InvalidTokenError
import os

MARKET_HUB_SECRET_KEY = os.getenv("MARKET_HUB_SECRET_KEY")

def create_token(data: dict):
    token: str = encode(payload=data, key=MARKET_HUB_SECRET_KEY, algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    try:
        data: dict = decode(token, key=MARKET_HUB_SECRET_KEY, algorithms="HS256")
        return data
    except InvalidTokenError:
        return {"message": "Invalid token"}