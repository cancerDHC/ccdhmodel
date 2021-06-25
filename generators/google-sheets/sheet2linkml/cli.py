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
from sheet2linkml import config
from sheet2linkml.source.gsheetmodel.gsheetmodel import GSheetModel
from sheet2linkml.source.gsheetmodel.mappings import Mappings
from sheet2linkml.terminologies.tccm.api import TCCMService
from linkml.utils import yamlutils
import click


@click.command()
@click.option(
    "--filter-entity",
    type=str,
    help="The name of a single entity that you would like to extract.",
)
@click.option(
    "--logging-config",
    type=str,
    help="A logging configuration file.",
    default=os.path.join(sys.path[0], "logging.ini"),
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
def main(filter_entity, logging_config, write_mappings, include_terminologies):
    # Display INFO log entry and up.
    logging.config.fileConfig(logging_config)

    # Read in Google API credentials.
    google_api_credentials = config.Settings().google_api_credentials
    google_sheet_id = config.Settings().cdm_google_sheet_id

    # Arbitrarily set a CRDC-H root URI.
    crdch_root = "https://example.org/ccdh"

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
            filename = f"output/{entity.get_filename()}.yaml"
            logging.info(f"Writing entity {entity.name} to {filename}")
            with open(filename, "w") as f:
                f.write(yamlutils.as_yaml(entity.as_linkml(crdch_root)))

            if write_mappings:
                mappings.extend(entity.mappings.mappings)

        Mappings.write_to_file(mappings, filename=write_mappings, model=model)

    else:
        # Convert the entire model into YAML.
        filename = f"output/{model.get_filename()}.yaml"
        logging.info(f"Writing model {model.name} to {filename}")
        with open(filename, "w") as f:
            f.write(yamlutils.as_yaml(model.as_linkml(crdch_root)))

        if write_mappings:
            Mappings.write_to_file(model.mappings, filename=write_mappings, model=model)


if __name__ == "__main__":
    main()
