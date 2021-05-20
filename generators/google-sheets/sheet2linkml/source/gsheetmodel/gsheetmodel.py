import pygsheets

from sheet2linkml.model import ModelElement
from sheet2linkml.source.gsheetmodel.entity import Entity, Worksheet
from linkml_model.meta import SchemaDefinition
from datetime import datetime
import re
import logging


class GSheetModel(ModelElement):
    """
    A GSheetModel represents a single, coherent model represented as a series of worksheets
    in Google Sheets. This representation is currently being developed by all the CCDH workstreams,
    and so it needs to be flexible enough to be modified extensively on the fly.

    If we ever extend sheet2linkml beyond Google Sheets, we should create a top-level Model
    class that generically represents a single, coherent model, and then make GSheetModel a
    subclass of that. But that's for another day.
    """

    """ The Google API scopes that are necessary to query this sheet. """
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.metadata.readonly",
    ]

    def __init__(self, google_sheet_oath2_credentials: str, google_sheet_id: str):
        """
        Create a new Google Sheet Model. This will create a model that uses the specified
        Google Sheet as an input.

        Note that creating a GSheetModel will kick off the Google Sheets authentication
        process, which will ask you to visit a website, log in with a Google account, and
        then to enter the provided code into this Python script. See
        https://pygsheets.readthedocs.io/en/stable/authorization.html for information on
        creating and downloading OAuth2 credentials from the Google Developers Console.
        Once you authenticate yourself, this script will create a file with your
        authentication token in your working directory, so you will not need to log in
        again from the same working directory.

        :param google_sheet_oath2_credentials: A file containing OAuth2 credential files.
        :param google_sheet_id: The Google Sheet ID containing the model.
        """

        self.client = pygsheets.authorize(
            client_secret=google_sheet_oath2_credentials, scopes=self.SCOPES
        )
        self.sheet = self.client.open_by_key(google_sheet_id)

    def worksheets(self) -> list[Worksheet]:
        """
        A list of worksheets available in this model.

        We identify a worksheet containing entities based on having 'Status' as the first column header title.

        :return: A list of entities available in this model.
        """

        def is_sheet_entity(worksheet: pygsheets.worksheet):
            """Identify worksheets containing entities, i.e. those that have 'Status' in cell A1."""
            return worksheet.get_value("A1") == "Status"

        def is_sheet_included(worksheet: pygsheets.worksheet):
            """
            Check if a sheet should be excluded. Eventually we should check whether A2 = 'included',
            but for now we just check to see if the title starts with 'x-'.
            """
            return not worksheet.title.startswith("x-")

        # Identify entity worksheets among the list of all worksheets in this Google Sheets document.
        worksheets = self.sheet.worksheets()
        entity_worksheets = filter(
            is_sheet_entity, filter(is_sheet_included, worksheets)
        )
        return [Worksheet(self, worksheet) for worksheet in entity_worksheets]

    def entities(self) -> list[Entity]:
        """
        :return: The list of entities in this model.
        """
        result = []
        for worksheet in self.worksheets():
            result.extend(worksheet.entities)
        return result

    def __str__(self) -> str:
        """
        :return: A string representation of this Google Sheet model.
        """

        return f'{self.__class__.__name__} with an underlying Google Sheet titled "{self.sheet.title}" containing {len(self.sheet.worksheets())} worksheets'

    @property
    def name(self) -> str:
        """
        :return: The name of this model.
        """
        return self.sheet.title

    def get_filename(self) -> str:
        """
        Return this Google Sheet model as a filename, which we calculate by making the Google Sheet title filesystem-safe.

        :return: A filename that could be used for this model.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        filename = str(self.sheet.title).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", filename)

    def to_markdown(self) -> str:
        """
        :return: A Markdown representation of this Google Sheet model.
        """

        return f"[{self.sheet.title}]({self.sheet.url})"

    def as_linkml(self, root_uri) -> SchemaDefinition:
        """
        Return this Google Sheet model as a LinkML SchemaDefinition.

        :param root_uri: The base URI to use for terms defined in this model.
        :return: A LinkML SchemaDefinition for the model described by this Google Sheet.
        """

        logging.info(f"Generating LinkML for {self}")

        # Set up general metadata.
        schema: SchemaDefinition = SchemaDefinition(name="CRDC-H", id=f"{root_uri}")
        schema.version = "v0"  # TODO: Replace with a version.
        schema.license = "https://creativecommons.org/publicdomain/zero/1.0/"
        schema.prefixes = {
            "linkml": "https://w3id.org/linkml/",
            "ccdh": f"{root_uri}/",
        }
        # TODO: See if we can get by without.
        # schema.imports = ['datatypes', 'prefixes']
        schema.imports = [
            'linkml:types'
        ]

        schema.default_prefix = "ccdh"
        schema.notes.append(f"derived from {self.to_markdown()}")
        schema.generation_date = datetime.now().isoformat()

        # Generate all the entities.
        schema.classes = {entity.name: entity.as_linkml(root_uri) for entity in self.entities()}

        return schema
