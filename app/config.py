from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Movie Collection API"
    debug: bool = True
    database_url: str = "sqlite:///./movies.db"
    secret_key: str = "default-secret-key"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

# Ensure data directory exists for Docker volume
data_dir = Path("./data")
data_dir.mkdir(exist_ok=True)