from pydantic_settings import BaseSettings, SettingsConfigDict

from server.core.types import string


class Configs(BaseSettings):
    # App
    MODE: string

    # Database
    MONGO_URI: string

    # storage
    CLOUDINARY_NAME: string
    CLOUDINARY_API_KEY: string
    CLOUDINARY_API_SECRET: string

    # Cors
    CORS_ALLOWED_ORIGINS: string
    MAX_AGE: int = 3600

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    model_config = SettingsConfigDict(env_file=".env", extra="forbid")

configs = Configs()
