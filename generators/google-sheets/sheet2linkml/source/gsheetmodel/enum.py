import logging
import re
from functools import cached_property

from linkml_model import SchemaDefinition
from linkml_model.meta import EnumDefinition, PermissibleValue
from pygsheets import worksheet

from sheet2linkml.model import ModelElement
from sheet2linkml.source.gsheetmodel.mappings import MappingRelations, Mappings


class Enum(ModelElement):
    """
    An enum represents an enumeration stored in a single worksheet in a Google Sheet spreadsheet.
    """

    def __init__(self, model, sheet: worksheet, name: str, rows: list[dict[str, str]]):
        """
        Create an enum based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this enum is a part of.
        :param sheet: A Google Sheet worksheet describing this enum.
        :param name: The name of this enum.
        :param rows: The rows in the spreadsheet describing this enum (as dictionaries of str -> str).
        """

        self.model = model
        self.worksheet = sheet
        self.enum_name = name
        self.rows = rows

    @property
    def value_rows(self) -> list[dict[str, str]]:
        """
        Returns this enum as a list of value rows.

        A value row is one where the COL_ENUM_NAME row is not empty.

        :return: A list of named rows in this sheet.
        """
        return [
            row
            for row in self.rows
            if row.get(EnumWorksheet.COL_VALUE_NAME) is not None
        ]

    @property
    def values(self) -> list:
        return [EnumValue(self.model, self, row) for row in self.value_rows]

    @property
    def enum_row(self) -> dict[str, str]:
        """
        Returns the "enum row" -- the single row in the spreadsheet that represents this
        enum itself. Writes errors in the logs if more than one "enum row" is found (only the
        first will be used).

        :return: A dictionary representing a row in the spreadsheet that represents this enum.
        """

        # Find all entity rows
        enum_rows = [
            row for row in self.rows if row.get(EnumWorksheet.COL_VALUE_NAME) is None
        ]

        # Report an error if no rows were found.
        if not enum_rows:
            # raise RuntimeError(f'Entity does not have an entity row: {self}')
            logging.error(f"Enum contains no enum row: {self}")
            return dict()

        # Report an error if more than one row was found.
        if len(enum_rows) > 1:
            logging.error(
                f'Enum contains more than one "enum row", only the first one will be used: {self}'
            )
            for row in enum_rows:
                logging.error(f" - Found enum row: {row}")

        return enum_rows[0]

    def __str__(self):
        """
        :return: A text description of this enum.
        """

        return f'{self.__class__.__name__} named {self.name} from worksheet "{self.worksheet.title}" containing {len(self.value_rows)} values'

    @property
    def name(self) -> str:
        """
        :return: A name for this enum.
        """
        return (self.enum_name or "(unnamed enum)").strip()

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this enum.
        """
        return f"CRDC-H.{self.enum_name}"

    @property
    def fixed_name(self):
        """
        :return: The name of this enum, modified to fit the format we use for other enums.
        """
        return Enum.fix_enum_name(self.full_name)

    @staticmethod
    def fix_enum_name(enum_name: str):
        """
        Transform enum names so that they can be accessed from Python.
        Ideally, these transformations should be done in the LinkML
        library somewhere, but for now, we can do that here.
        """

        # The hyphen in 'CRDC-H' doesn't work properly.
        fixed_name = re.sub(r"^CRDC-H\.", "CCDH.", enum_name)

        # The '.'s in the name also mess up the generated Python code.
        # But we might as well replace everything that isn't alphanumeric.
        fixed_name = re.sub(r"\W", "_", fixed_name).strip("_")

        # All enumerations should be prefixed with `enum_` for clarity.
        return f"enum_{fixed_name}"

    def get_filename(self) -> str:
        """
        Return this entity as a filename, which we calculate by making the enum name safe for file systems.

        :return: A filename that can be used for this enum.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.name).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", name)

    def to_markdown(self) -> str:
        """
        Returns a reference to this enum in Markdown. We include the name, worksheet name and worksheet URL.

        :return: A Markdown representation of this entity.
        """

        return f"[{self.name} in sheet {self.worksheet.title}]({self.worksheet.url})"

    @cached_property
    def mappings(self) -> Mappings:
        """
        Returns the list of mappings for this enum.
        """
        mappings = Mappings(self)
        mappings.add_mappings(
            self.enum_row.get("Source Entity"), MappingRelations.SKOS_RELATED_MATCH
        )
        mappings.add_mappings(
            self.enum_row.get("Source Attribute (Name)"),
            MappingRelations.SKOS_RELATED_MATCH,
        )
        mappings.add_mappings(
            self.enum_row.get("Source Attribute (Values)"),
            MappingRelations.SKOS_RELATED_MATCH,
        )
        return mappings

    @property
    def mappings_including_values(self) -> list[Mappings.Mapping]:
        """
        Returns the list of all mappings of this enum as well as all of its values.
        """
        mappings = list(self.mappings.mappings)
        for attr in self.values:
            mappings.extend(attr.mappings.mappings)
        return mappings

    def as_linkml(self, root_uri) -> EnumDefinition:
        """
        Returns a LinkML EnumDefinition describing this entity, including attributes.

        :param root_uri: The root URI to use for this enum.
        :return: A LinkML EnumDefinition describing this enum.
        """
        logging.info(f"Generating LinkML for {self}")

        # Basic metadata
        enum = EnumDefinition(
            name=self.fixed_name,
            description=(self.enum_row.get(EnumWorksheet.COL_DEFINITION) or "").strip(),
        )

        # Additional metadata

        # We add a 'derived from' note to the notes field, which might be
        # a string or a list, apparently.
        derived_from = f"Derived from {self.to_markdown()}"
        if isinstance(enum.notes, list):
            enum.notes.append(derived_from)
        elif isinstance(enum.notes, str):
            enum.notes = enum.notes + f"\n{derived_from}"
        else:
            enum.notes = derived_from

        # Add mappings
        self.mappings.set_mappings_on_element(enum)

        # Now generate LinkML for all of the values.
        enum.permissible_values = {
            str(enum_value.name): enum_value.as_linkml(root_uri)
            for enum_value in self.values
        }

        return enum


class EnumValue:
    """
    An EnumValue represents a single value within an enum.

    It is represented by a single row in a Google Sheet spreadsheet.
    """

    def __init__(self, model, enum: Enum, row: dict[str, str]):
        """
        Create an enum based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this enum is a part of.
        :param entity: The Enum that this enum value is a part of.
        :param row: The row describing this enum value (as a dictionary of str -> str).
        """

        self.model = model
        self.enum = enum
        self.row = row

    @property
    def name(self):
        """
        :return: A name for this enum value.
        """
        return (
            self.row.get(EnumWorksheet.COL_VALUE_NAME)
            or self.row.get("Name")
            or self.row.get("name")
        )

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this enum value.
        """
        return f"{self.enum.full_name}.{self.name}"

    def __str__(self):
        """
        :return: A text description of this enum value.
        """

        return f'{self.__class__.__name__} named "{self.name}" containing {len(self.row)} properties'

    @cached_property
    def mappings(self) -> Mappings:
        """
        Returns the list of mappings for this enum value.
        """
        mappings = Mappings(self)
        mappings.add_mappings(
            self.row.get("Source Entity"), MappingRelations.SKOS_RELATED_MATCH
        )
        mappings.add_mappings(
            self.row.get("Source Attribute (Name)"), MappingRelations.SKOS_RELATED_MATCH
        )
        mappings.add_mappings(
            self.row.get("Source Attribute (Values)"),
            MappingRelations.SKOS_RELATED_MATCH,
        )
        return mappings

    def as_linkml(self, root_uri) -> PermissibleValue:
        """
        Returns this attribute as a LinkML PermissibleValue.

        :param root_uri: The root URI to use for this PermissibleValue.
        :return: A LinkML PermissibleValue representing this attribute.
        """

        data = self.row

        pv = PermissibleValue(
            text=data.get(EnumWorksheet.COL_VALUE_NAME) or "",
            description=(data.get(EnumWorksheet.COL_DEFINITION) or "").strip(),
            comments=data.get("Comments"),
        )

        # Add mappings
        # TODO: LinkML doesn't actually support mappings on enum values!
        # self.mappings.set_mappings_on_element(pv)

        return pv


class EnumWorksheet(ModelElement):
    """
    A Worksheet represents a single worksheet in a GSheetModel. A single sheet usually contains
    information on a single Entity, but sometimes multiple entities may be described in a single
    Worksheet. In that case, this Worksheet will return multiple entities.
    """

    # Some column names.
    COL_STATUS = "Status"
    COL_ENUM_NAME = "Enumeration Name"
    COL_VALUE_NAME = "Value Name"
    COL_DEFINITION = "Definition"

    @staticmethod
    def is_sheet_entity(worksheet: worksheet):
        """Identify worksheets containing enums, i.e. those that have:
        - COL_STATUS in cell A1, and
        - COL_ENUM_NAME in cell B1, and
        - COL_VALUE_NAME in cell C1, and
        - COL_DEFINITION in cell D1
        """
        return worksheet.get_values("A1", "D1") == [
            [
                EnumWorksheet.COL_STATUS,
                EnumWorksheet.COL_ENUM_NAME,
                EnumWorksheet.COL_VALUE_NAME,
                EnumWorksheet.COL_DEFINITION,
            ]
        ]

    def __init__(self, model, sheet: worksheet):
        """
        Create a worksheet based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this worksheet is a part of.
        :param sheet: A Google Sheet worksheet describing this worksheet.
        """

        self.model = model
        self.worksheet = sheet

    @property
    def rows(self) -> list[dict]:
        """
        Returns this EnumWorksheet as a list of rows. We use the header row to create these dictionaries.

        :return: A list of the rows in this sheet.
        """
        return self.worksheet.get_all_records(empty_value=None)

    @property
    def included_rows(self) -> list[dict]:
        """
        Returns this entity as a list of included rows.

        An included row is one whose COL_STATUS is set to 'include'.

        :return: A list of included rows in this sheet.
        """
        return [
            row
            for row in self.rows
            if row.get(EnumWorksheet.COL_STATUS, "") == "include"
        ]

    @property
    def enum_names(self) -> list[str]:
        """
        Return a list of all the entity names in this worksheet.

        :return: A list of all the entity names in this worksheet.
        """

        return [
            (row.get(EnumWorksheet.COL_ENUM_NAME) or "") for row in self.included_rows()
        ]

    @property
    def enums_as_included_rows(self) -> dict[str, list[dict]]:
        """
        Group the list of rows based on having identical COL_ENUM_NAME values.

        :return: A dict with keys of COL_ENUM_NAME values and values of included rows having that value.
        """

        result = dict()

        for row in self.included_rows:
            enum_name = row.get(EnumWorksheet.COL_ENUM_NAME) or ""
            if not (enum_name in result):
                result[enum_name] = list()

            result[enum_name].append(row)

        # The Google Sheet might indicate that the enum row (the row without a value name) should be excluded.
        # If any other rows have been included for this entity, however, they would be used to define the entity,
        # even though the intention was to exclude that entity. In order to prevent this, we will check for any included
        # rows that don't have an entity row -- such groups will be filtered out here.
        filtered = dict()

        for name, rows in result.items():
            if any(row.get(EnumWorksheet.COL_VALUE_NAME) is None for row in rows):
                filtered[name] = rows
            else:
                logging.warning(
                    f"- Ignoring enum {name} in worksheet {self.name} as it does not have an enum row."
                )

        return filtered

    @property
    def grouped_entities(self) -> dict[str, Enum]:
        """
        Return a list of enums in this worksheet, grouped into a dict by enum name.

        :return: A dict with keys of COL_ENTITY_NAME values and values of Enum objects.
        """

        return {
            k: Enum(self.model, self.worksheet, k, v)
            for k, v in self.enums_as_included_rows.items()
        }

    @property
    def enums(self) -> list[Enum]:
        """
        Return a list of enums in this worksheet.

        :return: A list of Enum objects.
        """

        return list(self.grouped_entities.values())

    @property
    def name(self) -> str:
        """
        :return: A name for this worksheet.
        """
        return self.worksheet.title

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this worksheet.
        """
        return self.worksheet.url

    def get_filename(self) -> str:
        """
        Return this worksheet as a filename, which we calculate by making the entity name safe.

        :return: A filename that could be used for this entity.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.worksheet.title).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", name)

    def to_markdown(self) -> str:
        """
        :return: A Markdown representation of this entity.
        """

        return f"[{self.worksheet.title}]({self.worksheet.url})"

    def as_linkml(self, root_uri) -> list[SchemaDefinition]:
        """
        Return all LinkML SchemaDefinitions in this worksheet. We do this by converting each
        Entity into its LinkML SchemaDefinition.

        :param root_uri: The root URI to use for this worksheet.
        :return: A list of LinkML SchemaDefinitions representing entities in this worksheet.
        """
        return [enum.as_linkml(root_uri) for enum in self.enums.values()]
