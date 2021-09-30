import json
import os.path
import unittest
from assertpy import assert_that, fail
import jsonschema

MODEL_PATH = 'crdch_model'


class ValidateArtifacts(unittest.TestCase):
    """
    This is a series of tests for validating that artifacts have been generated correctly.
    """

    def test_validate_json_schema(self):
        json_schema_file_path = os.path.join(MODEL_PATH, 'json_schema', 'crdch_model.schema.json')
        assert_that(json_schema_file_path).exists().is_file()

        with open(json_schema_file_path) as f:
            try:
                json_schema = json.load(f)
            except json.JSONDecodeError as e:
                fail(f'JSON Schema {json_schema_file_path} is not a valid JSON document: {e}')

            assert_that(json_schema).is_not_empty()

            try:
                jsonschema.Draft202012Validator.check_schema(json_schema)
            except jsonschema.exceptions.SchemaError as e:
                fail(f'JSON Schema {json_schema_file_path} is not a valid JSON Schema: {e}')

