"""
sheet2linkml.py
A script for converting Google Sheets to a LinkML model.
"""

import sys
import os
import logging
import logging.config
from sheet2linkml import config
from sheet2linkml.source.gsheetmodel.gsheetmodel import GSheetModel
from linkml.utils.yamlutils import as_yaml
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
    default=os.path.join(sys.path[0], "logging.ini")
)
def main(filter_entity, logging_config):
    # Display INFO log entry and up.
    logging.config.fileConfig(logging_config)

    # Read in Google API credentials.
    google_api_credentials = config.Settings().google_api_credentials
    google_sheet_id = config.Settings().cdm_google_sheet_id

    # Arbitrarily set a CRDC-H root URI.
    crdch_root = "https://example.org/ccdh"

    # Load the Google Sheet model.
    model = GSheetModel(google_api_credentials, google_sheet_id)
    logging.info(f"Google Sheet loaded: {model}")


    if filter_entity:
        click.echo(f"Filtering to entity {filter_entity}.")

        # Only extract a single entity.
        selected_entities = [
            entity for entity in model.entities() if filter_entity == entity.name
        ]
        for entity in selected_entities:
            filename = f"output/{entity.get_filename()}.yaml"
            with open(filename, "w") as f:
                f.write(as_yaml(entity.as_linkml(crdch_root)))
    else:
        # Convert the entire model into YAML.
        filename = f"output/{model.get_filename()}.yaml"
        with open(filename, "w") as f:
            f.write(as_yaml(model.as_linkml(crdch_root)))


if __name__ == "__main__":
    main()
