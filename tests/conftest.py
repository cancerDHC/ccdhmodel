import pytest
from pathlib import Path


@pytest.fixture(scope='session')
def yaml_files():
    files = list(Path(__file__).parent.parent.joinpath('model').glob(r'*.yaml'))
    return {p.name: str(p) for p in files if p.is_file()}
