from motor.motor_asyncio import AsyncIOMotorClient
from server.core.configs import configs

client = AsyncIOMotorClient(configs.MONGO_URI).MLAlgoHub  # type: ignore[attr-defined]
