import time
from loguru import logger
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class ProcessTimeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, some_attribute: str):
        super().__init__(app)
        self.some_attribute = some_attribute

    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()

        client_ip = request.client.host if request.client else "Unknown"
        method = request.method
        url = str(request.url)
        user_agent = request.headers.get("User-Agent", "Unknown")

        logger.info(f"📌 [Request] IP: {client_ip}, Method: {method}, URL: {url}, User-Agent: {user_agent}")

        response = await call_next(request)
        process_time = time.perf_counter() - start_time

        logger.info(f"✅ [Response] URL: {url}, Process Time: {process_time:.4f}s")

        response.headers["X-Process-Time"] = str(process_time)
        return response