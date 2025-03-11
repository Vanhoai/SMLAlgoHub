from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from server.adapters.primary.v1.routes import router as v1_routers

from server.adapters.shared.middlewares.tracing_middleware import TracingMiddleware
from server.database import MLAlgoHubDatabase
from server.core.configs import configs
from server.core.exceptions import ExceptionHandler

from server.domain.entities.account_entity import AccountEntity
from server.domain.entities.tag_entity import TagEntity


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    app.db = AsyncIOMotorClient(configs.MONGO_URI).MLAlgoHub  # type: ignore[attr-defined]
    await init_beanie(app.db, document_models=[AccountEntity, TagEntity])  # type: ignore[arg-type,attr-defined]
    print("Connected to database ✅")
    yield
    print("Shutdown complete ✅")


# init app
app = FastAPI(lifespan=lifespan)

# set database and container
database = MLAlgoHubDatabase()

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
