from functools import lru_cache
from py2neo import Graph
from pathlib import Path
from pydantic import BaseSettings

ROOT_DIR = Path(__file__).parent.parent


def neo4j_graph() -> Graph:
    settings: Settings = get_settings()
    return Graph(settings.neo4j_bolt_uri, auth=(settings.neo4j_username, settings.neo4j_password))


class Settings(BaseSettings):
    app_name: str = 'TCCM API'
    neo4j_username: str
    neo4j_password: str
    neo4j_bolt_uri: str
    cdm_google_sheet_id: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


CDM_GOOGLE_SHEET_ID = get_settings().cdm_google_sheet_id
