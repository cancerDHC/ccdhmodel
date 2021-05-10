"""
sheet2linkml.py
A script for converting Google Sheets to a LinkML model.
"""

import logging
from sheet2linkml import config
from sheet2linkml.source.gsheetmodel.gsheetmodel import GSheetModel
import click


@click.command()
def main():
    google_api_credentials = config.Settings().google_api_credentials
    google_sheet_id = config.Settings().cdm_google_sheet_id

    model = GSheetModel(google_api_credentials, google_sheet_id)
    click.echo(f'Google Sheet loaded: {model}')

    entities = model.entities()
    for entity in entities:
        click.echo(f'Creating entity {entity}')
        entityName = list(entity.names)[0]
        if len(entity.names) > 1:
            logging.warning(f'Entity has more than one name! Name "{entityName}" will be used, but please fix this in the Google Sheet.')
        for attribute in entity.attributes:
            click.echo(f'   - Found attribute {attribute}')


if __name__ == "__main__":
    main()
