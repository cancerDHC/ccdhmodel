"""
sheet2linkml.py
A script for converting Google Sheets to a LinkML model.
"""

import logging
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
def main(filter_entity):
    google_api_credentials = config.Settings().google_api_credentials
    google_sheet_id = config.Settings().cdm_google_sheet_id

    crdch_root = "https://example.org/ccdh"

    model = GSheetModel(google_api_credentials, google_sheet_id)
    click.echo(f"Google Sheet loaded: {model}")

    logging.basicConfig(level=logging.INFO)

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
