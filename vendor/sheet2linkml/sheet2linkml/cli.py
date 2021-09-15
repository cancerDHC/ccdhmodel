"""
sheet2linkml.py
A script for converting Google Sheets to a LinkML model.
"""

import sys
import os
import re
import subprocess
import logging
import logging.config
import click
from linkml_runtime.dumpers import yaml_dumper
from dotenv import load_dotenv

from sheet2linkml.source.gsheetmodel.gsheetmodel import GSheetModel
from sheet2linkml.source.gsheetmodel.mappings import Mappings
from sheet2linkml.terminologies.tccm.api import TCCMService

@click.command()
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    default='model.yaml',
    help="The file that the generated LinkML model should be written to.",
)
@click.option(
    "--filter-entity",
    type=str,
    help="The name of a single entity that you would like to extract.",
)
@click.option(
    "--logging-config",
    type=str,
    help="A logging configuration file.",
    default='logging.ini',
)
@click.option(
    "--write-mappings",
    type=click.Path(exists=False),
    help="A file to write out mappings to.",
)
@click.option(
    "--include-terminologies/--skip-terminologies",
    default=True,
    help="Controls whether we use the CCDH Terminology Service to add enumerated values for attributes.",
)
def main(output, filter_entity, logging_config, write_mappings, include_terminologies):
    # Display INFO log entry and up.
    logging.config.fileConfig(logging_config)

    # Load environemental variables from `.env` if one is present.
    load_dotenv()

    # Read in Google API credentials.
    google_api_credentials = os.getenv('GOOGLE_API_CREDENTIALS', 'google_api_credentials.json')
    google_sheet_id = os.getenv('CDM_GOOGLE_SHEET_ID')

    # Arbitrarily set a CRDC-H root URI.
    crdch_root = "https://example.org/crdch"

    # Load the Google Sheet model and add the development version number.
    model = GSheetModel(google_api_credentials, google_sheet_id)
    if include_terminologies:
        model.use_terminology_service(TCCMService("https://terminology.ccdh.io"))
    logging.info(f"Google Sheet loaded: {model}")

    # Determine the development version number. We can get this from git-describe.
    git_describe_result = subprocess.run(
        ["git", "describe", "--long", "--dirty"], capture_output=True
    )
    if git_describe_result.returncode == 0:
        model.development_version = re.sub(
            "[^a-zA-Z0-9.\\-]", "_", git_describe_result.stdout.decode("utf8").strip()
        )

    # Setup output filename.
    output_filename = click.format_filename(output)

    # We have two operating modes:
    # 1. If a `--filter-entity "<Entity Name>"` is specified on the command line,
    #    we generate `output/<Entity Name>.yaml` for that entity alone.
    # 2. Otherwise, we generate `output/<Model Name>.yaml` for the entire model.
    if filter_entity:
        # Only extract a single entity.
        logging.info(f"Filtering to entity {filter_entity}.")
        selected_entities = [
            entity for entity in model.entities() if filter_entity == entity.name
        ]

        if not selected_entities:
            logging.error(
                f"Could not find any entities named {filter_entity}. Please use one of:"
            )
            for entity in model.entities():
                logging.error(f" - {entity.name}")
            exit(1)

        mappings = list()

        for entity in selected_entities:
            logging.info(f"Writing entity {entity.name} to {output_filename}")
            yaml_dumper.dump(entity.as_linkml(crdch_root), output_filename)

            if write_mappings:
                mappings.extend(entity.mappings.mappings)

        Mappings.write_to_file(mappings, filename=write_mappings, model=model)

    else:
        # Convert the entire model into YAML.
        logging.info(f"Writing model {model.name} to {output_filename}")
        yaml_dumper.dump(model.as_linkml(crdch_root), output_filename)

        if write_mappings:
            Mappings.write_to_file(model.mappings, filename=write_mappings, model=model)


if __name__ == "__main__":
    main()
