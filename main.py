from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from server.adapters.primary.v1.routes import router as v1_routers

import cloudinary
from server.adapters.shared.middlewares.tracing_middleware import TracingMiddleware
from server.core.configs import configs
from server.core.exceptions import ExceptionHandler

config = cloudinary.config(
    cloud_name=configs.CLOUDINARY_NAME,
    api_key=configs.CLOUDINARY_API_KEY,
    api_secret=configs.CLOUDINARY_API_SECRET,
    secure=True
)

# init app
app = FastAPI()

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in configs.CORS_ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TracingMiddleware)

# routes
app.include_router(v1_routers, prefix="/api/v1")

# exception
@app.exception_handler(ExceptionHandler)
async def exception_handler(request: Request, exc: ExceptionHandler):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "message": exc.msg,
        },
        headers={"X-Error": f"{status.HTTP_200_OK}.{exc.code}"},
        media_type="application/json",
        # write log here
    )
