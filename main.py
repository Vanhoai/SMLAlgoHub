from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from firebase_admin import initialize_app, credentials
from contextlib import asynccontextmanager

from server.rabbitmq_connection import rabbitmq_connection
from server.adapters.primary.v1.routes import router as v1_routers

import cloudinary
from server.adapters.shared.middlewares.rate_limit_middleware import RateLimitingMiddleware
from server.adapters.shared.middlewares.tracing_middleware import TracingMiddleware
from server.core.configs import configs
from server.core.exceptions import ExceptionHandler

cred = credentials.Certificate({ \
        "type": "service_account", \
        "project_id": configs.FIREBASE_PROJECT_ID, \
        "private_key_id": configs.PRIVATE_KEY_ID, \
        "private_key": configs.FIREBASE_PRIVATE_KEY.replace('\\n', '\n'), \
        "client_email": configs.FIREBASE_CLIENT_EMAIL, \
        "client_id": configs.FIREBASE_CLIENT_ID, \
        "auth_uri": configs.FIREBASE_AUTH_URI, \
        "token_uri": configs.FIREBASE_TOKEN_URI, \
        "auth_provider_x509_cert_url": configs.AUTH_PROVIDER_X509_CERT_URL, \
        "client_x509_cert_url": configs.CLIENT_X509_CERT_URL, \
        "universe_domain": "googleapis.com"
    })

initialize_app(credential=cred)

config = cloudinary.config(
    cloud_name=configs.CLOUDINARY_NAME,
    api_key=configs.CLOUDINARY_API_KEY,
    api_secret=configs.CLOUDINARY_API_SECRET,
    secure=True
)

@asynccontextmanager
async def lifespan(_: FastAPI):
    await rabbitmq_connection.connect()
    yield
    await rabbitmq_connection.disconnect()

# init app
app = FastAPI(lifespan=lifespan)

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in configs.CORS_ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TracingMiddleware)
app.add_middleware(RateLimitingMiddleware)

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
