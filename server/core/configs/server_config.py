# Server - API configuration
from pydantic_settings import BaseSettings

from server.core.types import string


class ServerConfig(BaseSettings):
    """
    Server configuration settings

    Attributes:
    -----------
    HOST: str
        Hostname to bind the server to
    PORT: int
        Port number to bind the server to
    DEBUG: bool
        Enable debug mode
    RELOAD: bool
        Enable auto-reload
    WORKERS: int
        Number of worker processes to spawn
    API_VERSION: str
        Base path for the API endpoints in the server like /api/v1 or /api/v2 etc.
    """

    HOST: string = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = True
    WORKERS: int = 1

    class Config:
        env_prefix = "SERVER_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
