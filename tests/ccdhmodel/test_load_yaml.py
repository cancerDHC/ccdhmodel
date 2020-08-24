import pytest
from pathlib import Path
from biolinkml.utils.schemaloader import SchemaLoader


def test_load_specimen(yaml_files, caplog):
    yaml_file = yaml_files['specimen.yaml']
    loader = SchemaLoader(yaml_file, logger=caplog)
    assert loader.schema.name == 'Speciman'
    assert 'ADM:Sample' in loader.schema.name.mappings
    assert len(loader.schema.classes) == 1
