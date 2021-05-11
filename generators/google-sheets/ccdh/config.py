from functools import lru_cache
from pathlib import Path
from pydantic import BaseSettings

ROOT_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    app_name: str = 'Google Sheets LinkML generator for CRDC-H model'
    cdm_google_sheet_id: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


CDM_GOOGLE_SHEET_ID = get_settings().cdm_google_sheet_id
