from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.adapters.primary.v1.routes import router as v1_routers
from server.containers import JudgerContainer
from server.database import JudgerDatabase
from server.configs import configs
from server.di import singleton

@singleton
class MLAlgoHubServer:
    def __init__(self):

        # set default app
        self.app = FastAPI()

        # set database and container
        self.container = JudgerContainer()
        self.database = JudgerDatabase()

        # cors
        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        @self.app.get("/")
        async def root():
            return {
                "statusCode": 200,
                "message": "Application Running !!!"
            }
        
        self.app.include_router(v1_routers, prefix="/api/v1")

server = MLAlgoHubServer()
app = server.app
database = server.container