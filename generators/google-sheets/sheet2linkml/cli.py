"""
sheet2linkml.py
A script for converting Google Sheets to a LinkML model.
"""

from sheet2linkml import config
from sheet2linkml.source.gsheetmodel.gsheetmodel import GSheetModel
import click


@click.command()
def main():
    click.echo('Loading settings.')
    google_api_credentials = config.Settings().google_api_credentials
    google_sheet_id = config.Settings().cdm_google_sheet_id

    model = GSheetModel(google_api_credentials, google_sheet_id)
    click.echo(f'Google Sheet loaded: {model}')

    entities = model.entities()
    for entity in entities:
        click.echo(f' - Found entity {entity}')

if __name__ == "__main__":
    main()