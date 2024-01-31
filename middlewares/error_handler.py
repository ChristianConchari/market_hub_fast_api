from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        """
        Middleware to handle exceptions and return a JSON response with the error message.

        Args:
            request (Request): The incoming request.
            call_next (Callable): The next middleware or endpoint to call.

        Returns:
            Response | JSONResponse: The response to be returned.

        Raises:
            Exception: If an exception occurs during the execution of the middleware or endpoint.
        """
        try:
            return await call_next(request)
        
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"error": str(e)}
            )