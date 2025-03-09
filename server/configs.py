import os
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Configs(BaseSettings):
    MODE: str = os.getenv("MODE", "DEV")
    API_VERSION: str = os.getenv("API_VERSION", "v1")
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

configs = Configs()