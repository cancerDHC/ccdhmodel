import json
import os.path
import unittest
from assertpy import assert_that

MODEL_PATH = 'crdch_model'


class ValidateArtifacts(unittest.TestCase):
    """
    This is a series of tests for validating that artifacts have been generated correctly.
    """

    def test_validate_json_schema(self):
        json_schema_file_path = os.path.join(MODEL_PATH, 'json_schema', 'crdch_model.schema.json')
        assert_that(json_schema_file_path).exists().is_file()

        with open(json_schema_file_path) as f:
            json_schema = json.load(f)
            assert_that(json_schema).is_not_empty()


