from pydantic_settings import BaseSettings

from server.core.configs.cors_config import CorsConfig
from server.core.configs.server_config import ServerConfig


class ApplicationConfig(BaseSettings):
    """
    Application settings
    """

    APP_NAME: str = "PyFAPI"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = (
        "Python FastAPI mongodb app for Enterprise usage with best practices, tools, and more."
    )
    APP_URL: str = "http://localhost:8000"
    APP_DEBUG: bool = True

    class Config:
        # env_prefix = "APP_"
        env_file = ".env.dev"
        env_file_encoding = "utf-8"
        case_sensitive = True


app_config = ApplicationConfig()
cors_config = CorsConfig()
server_config = ServerConfig()
