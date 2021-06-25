import pygsheets

from sheet2linkml.model import ModelElement
from sheet2linkml.source.gsheetmodel.mappings import Mappings
from sheet2linkml.source.gsheetmodel.entity import Entity, EntityWorksheet, Attribute
from sheet2linkml.source.gsheetmodel.enum import EnumWorksheet, Enum
from sheet2linkml.source.gsheetmodel.datatype import Datatype, DatatypeWorksheet
from sheet2linkml.terminologies.service import TerminologyService
from linkml_model.meta import SchemaDefinition
from functools import cached_property, cache
from datetime import datetime, timezone
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

        # TODO: at some point, we should read the version number from the Google Sheets document... somehow.
        self.release_version = None

        # Set a `development version`. This is initially None, but if set, we add this to the metadata we emit.
        self.development_version = None

        # Set the 'last_updated' time to now.
        # TODO: we should be able to get this from the Google Sheet, in RFC 3339 format, but this apparently
        # requires a different scope than what we currently use.
        # return self.sheet.updated
        self.last_updated = datetime.now(timezone.utc).isoformat()

        # Set the terminology_service to None, indicating that terminology services shouldn't be used.
        self.terminology_service = None

    @property
    def version(self):
        """
        Return the version of this GSheetModel.
        """

        # TODO: We should read this from the Google Sheet.
        if self.release_version:
            return self.release_version
        else:
            return self.development_version

    @staticmethod
    def is_sheet_normative(worksheet: pygsheets.worksheet):
        """
        Check if a sheet is an informative sheet that does not contain any model information.
        There are three types of such sheets:
            - O_* tabs are useful tabs that have other non Entity content (exclude)
            - X_* tabs are tabs that might be deletable (exclude)
            - R_* tabs can be created to hold some sort of reference material that should not be changed. (exclude)
        """

        result = not (
            worksheet.title.startswith("O_")
            or worksheet.title.startswith("X_")
            or worksheet.title.startswith("R_")
        )

        return result

    @cache
    def entity_worksheets(self) -> list[EntityWorksheet]:
        """
        A list of worksheets available in this model.

        We identify a worksheet containing entities based on its column header.

        :return: A list of entities available in this model.
        """

        # Identify entity worksheets among the list of all worksheets in this Google Sheets document.
        worksheets = self.sheet.worksheets()

        tests_and_errors = {
            "excluded by sheet type": GSheetModel.is_sheet_normative,
            "not an entity worksheet": EntityWorksheet.is_sheet_entity,
        }

        entity_worksheets = list()
        for worksheet in worksheets:
            flag_skip = False
            for test_name, error in tests_and_errors.items():
                if not error(worksheet):
                    logging.debug(f"Skipping worksheet {worksheet.title}: {test_name}")
                    flag_skip = True
                    break

            if not flag_skip:
                entity_worksheets.append(worksheet)

        return [
            EntityWorksheet(
                self, worksheet, terminology_service=self.terminology_service
            )
            for worksheet in entity_worksheets
        ]

    @cache
    def entities(self) -> list[Entity]:
        """
        :return: The list of entities in this model.
        """
        result = []
        for worksheet in self.entity_worksheets():
            result.extend(worksheet.entities)
        return result

    def datatype_worksheets(self) -> list[DatatypeWorksheet]:
        """
        A list of datatype worksheets available in this model.

        We only have a single datatype worksheet: 'Primitives'. So we just return that.

        :return: A list of datatype worksheets available in this model.
        """

        return [DatatypeWorksheet(self, self.sheet.worksheet("title", "Primitives"))]

    def datatypes(self) -> list[Datatype]:
        """
        :return: The list of Datatypes in this model.
        """
        result = []
        for worksheet in self.datatype_worksheets():
            result.extend(worksheet.datatypes)
        return result

    def enum_worksheets(self) -> list[EnumWorksheet]:
        """
        A list of enum worksheets available in this model.

        We only have a single enum worksheet: 'O_CCDH Enums'. So we just return that.
        """
        return [EnumWorksheet(self, self.sheet.worksheet("title", "O_CCDH Enums"))]

    def enums_from_worksheets(self) -> list[Enum]:
        """
        A list of enums available from worksheets in this model.
        """
        result = []
        for worksheet in self.enum_worksheets():
            result.extend(worksheet.enums)
        return result

    @cached_property
    def mappings(self) -> list[Mappings.Mapping]:
        """Return a list of all the mappings in this LinkML document."""
        mappings = [
            mapping
            for datatype in self.datatypes()
            for mapping in datatype.mappings.mappings
        ]
        mappings.extend(
            mapping
            for entity in self.entities()
            for mapping in entity.mappings_including_attributes
        )
        mappings.extend(
            mapping
            for enum in self.enums_from_worksheets()
            for mapping in enum.mappings_including_values
        )
        return mappings

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

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this model.
        """
        return self.sheet.url

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
        schema.prefixes = {
            "linkml": "https://w3id.org/linkml/",
            "ccdh": f"{root_uri}/",
            "NCIT": "http://purl.obolibrary.org/obo/NCIT_",
            "GDC": "http://example.org/gdc/",
            "PDC": "http://example.org/pdc/",
            "ICDC": "http://example.org/icdc/",
            "HTAN": "http://example.org/htan/",
        }
        # TODO: See if we can get by without.
        # schema.imports = ['datatypes', 'prefixes']
        schema.imports = ["linkml:types"]
        schema.default_prefix = "ccdh"

        schema.license = "https://creativecommons.org/publicdomain/zero/1.0/"
        schema.notes.append(f"Derived from {self.to_markdown()}")
        schema.generation_date = self.last_updated

        schema.version = self.version

        # Generate all the datatypes.
        schema.types = {
            datatype.name: datatype.as_linkml(root_uri) for datatype in self.datatypes()
        }

        # Generate all the entities.
        schema.classes = {
            entity.name: entity.as_linkml(root_uri) for entity in self.entities()
        }

        # Load enums from the attributes themselves -- this will look things up in the terminology service.
        schema.enums = {
            Enum.fix_enum_name(attribute.full_name): attribute.as_linkml_enum()
            for entity in self.entities()
            for attribute in entity.attributes
            if attribute.as_linkml_enum() is not None
        }

        # Add enums from the enum worksheets in this Google Doc.
        enum_worksheets = self.enum_worksheets()
        for enum_worksheet in enum_worksheets:
            for enum in enum_worksheet.enums:
                schema.enums[enum.fixed_name] = enum.as_linkml(root_uri)

        # At this point, classes might refer to types that haven't been defined
        # yet. So, for fields that refer to other classes in this model, we need to
        # go through and:
        #   - Warn the user about the missing type
        #   - Replace the type with 'Entity' for now.
        valid_types = (
            set(schema.types.keys())
            .union(set(schema.classes.keys()))
            .union(set(schema.enums.keys()))
        )

        def fix_type_name(entity, dict, propName):
            value = dict[propName]
            if value is not None and value not in valid_types:
                logging.warning(
                    f"Entity {entity}'s {propName} refers to type {value}, which is not defined."
                )
                dict[propName] = "Entity"

        for entity in schema.classes.values():
            fix_type_name(entity.name, entity, "is_a")
            for attrName in entity.attributes:
                attr = entity.attributes[attrName]
                fix_type_name(f"{entity.name}.{attrName}", attr, "range")

        return schema

    def use_terminology_service(self, terminology_service: TerminologyService):
        """
        Activate terminology lookups using the specified base_url (e.g. https://terminology.ccdh.io/enumerations/CRDC-H.Specimen.analyte_type?value_only=false)
        """
        self.terminology_service = terminology_service
