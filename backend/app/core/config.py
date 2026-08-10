"""
SheetPilot

Capability : CORE-001
Module     : Configuration
Version    : 0.1.0
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Global application configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --------------------
    # Application
    # --------------------

    app_name: str = Field(default="SheetPilot")

    app_version: str = Field(default="0.1.0")

    environment: str = Field(default="development")

    debug: bool = Field(default=True)

    log_level: str = Field(default="INFO")

    # --------------------
    # AI
    # --------------------

    default_ai_provider: str = Field(default="openai")

    openai_api_key: str = ""

    google_api_key: str = ""

    # --------------------
    # Database
    # --------------------

    database_url: str = "sqlite:///memory/sheetpilot.db"

    # --------------------
    # Repository
    # --------------------

    project_root: str = ""

    # --------------------
    # UI
    # --------------------

    theme: str = "dark"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()
