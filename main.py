from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.adapters.primary.v1.routes import router as v1_routers

from server.adapters.shared.middlewares.tracing_middleware import TracingMiddleware
from server.database import MLAlgoHubDatabase
from server.di import singleton

from server.core.configs import app_config, cors_config


@singleton
class MLAlgoHubServer:
    def __init__(self):

        # set default app
        self.app = FastAPI()

        # set database and container
        self.database = MLAlgoHubDatabase()

        # middlewares
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in cors_config.ALLOWED_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.add_middleware(TracingMiddleware)

        # routes
        self.app.include_router(v1_routers, prefix="/api/v1")

    def run(self):
        print("Application running on http://localhost:8000")


server = MLAlgoHubServer()
app = server.app
server.run()
