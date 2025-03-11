from pydantic_settings import BaseSettings, SettingsConfigDict

from server.core.types import string


class Configs(BaseSettings):
    # App
    MODE: string

    # Database
    MONGO_URI: string

    # Cors
    CORS_ALLOWED_ORIGINS: string
    MAX_AGE: int = 3600

    model_config = SettingsConfigDict(env_file=".env", extra="forbid")


configs = Configs()
