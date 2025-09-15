"""
Utilities for loading and handling configuration files.
"""

import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict, YamlConfigSettingsSource
from utils.logging_utils import setup_logger

logger = setup_logger(
    log_file=__file__,
    log_to_console=False,
    file_mode="a",
)


class Settings(BaseSettings):
    """
    Application configuration container that loads required credentials and metadata
    from env, .env, YAML, or secrets files.
    """

    # .env
    GH_PAT: str = Field(...)
    WSL_PASS: str = Field(...)

    # .yaml
    APP_NAME: str = Field(...)
    APP_VERSION: str = Field(...)

    PATH_LOGS: str = Field(...)
    PATH_DATA_ROOT: str = Field(...)
    PATH_ASSETS_ROOT: str = Field(...)
    PATH_MODELS_ROOT: str = Field(...)
    PATH_OUTPUT_ROOT: str = Field(...)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,  # kwargs passed directly to Settings()
            env_settings,  # Environment variables
            dotenv_settings,  # .env file
            YamlConfigSettingsSource(
                settings_cls,
                yaml_file=Path("config/config.yaml"),
                yaml_file_encoding="utf-8",
            ),  # YAML file
            file_secret_settings,  # Secrets from files
        )


def get_settings() -> Settings:
    """
    Constructs and returns a validated Settings object that centralizes configuration
    for the application.
    Returns:
        Settings: A validated Settings instance containing application configuration.
    """

    logger.info("Loading application settings.")
    return Settings()  # type: ignore


def main():
    """Entry Point for the Program."""
    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module.\n")
    # Usage

    settings = get_settings()

    print(settings.APP_NAME)  # From config.yaml
    print(settings.APP_VERSION)  # From config.yaml
    print(settings.GH_PAT)  # From .env


if __name__ == "__main__":
    main()
