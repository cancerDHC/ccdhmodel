from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings

ROOT_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    app_name: str = "Google Sheets LinkML generator for CRDC-H model"
    cdm_google_sheet_id: str
    google_api_credentials: str = "google_api_credentials.json"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
