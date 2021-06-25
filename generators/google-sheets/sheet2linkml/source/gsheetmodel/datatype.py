from sheet2linkml.model import ModelElement
from sheet2linkml.source.gsheetmodel.mappings import Mappings, MappingRelations
from pygsheets import worksheet
from linkml_model.meta import TypeDefinition
import logging
import re


class Datatype(ModelElement):
    """
    A datatype defined in the CRDC-H model. This is definitionally the primitive types, since
    the complex types are defined as entities. However, if there is some need for complex datatypes
    that are not entities, we'll probably implement that here as well.

    The way our model works, we define our own primitive types as well as mappings to the LinkML types along with
    other types. Since those are mapped to types in all the output formats (Python, JSON Schema, etc.), eventually
    everything should get mapped to right types everywhere..
    """

    def __init__(self, model, sheet: worksheet, name: str, rows: list[dict[str, str]]):
        """
        Create a datatype based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this entity is a part of.
        :param sheet: A Google Sheet worksheet describing this entity.
        :param name: The name of this datatype.
        :param rows: The rows in the spreadsheet describing this datatype (as dictionaries of str -> str).
                     For primitives, this should only be a single row.
        """

        self.model = model
        self.worksheet = sheet
        self.datatype_name = name
        self.rows = rows

    @property
    def datatype_row(self):
        if len(self.rows) == 0:
            raise RuntimeError(f"Unexpected lack of rows for {self}")

        if len(self.rows) > 1:
            logging.error(
                f"Expected exactly one row for {self} but found {len(self.rows)} rows, using first row: {self.rows[0]}"
            )

        return self.rows[0]

    def __str__(self):
        """
        :return: A text description of this datatype.
        """

        return f'{self.__class__.__name__} named {self.name} from worksheet "{self.worksheet.title}" containing {len(self.rows)} rows'

    @property
    def name(self) -> str:
        """
        The name of this datatype. To differentiate it from the LinkML base types, we add `ccdh_` as a prefix.

        :return: A name for this datatype.
        """
        return f"ccdh_{self.datatype_name}"

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this datatype.
        """
        return f"CRDC-H.{self.name}"

    def get_filename(self) -> str:
        """
        Return this datatype as a filename, which we calculate by making the datatype name safe for file systems.

        :return: A filename that can be used for this datatype.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.name).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", name)

    def to_markdown(self) -> str:
        """
        Returns a reference to this entity in Markdown. We include the name, worksheet name and worksheet URL.

        :return: A Markdown representation of this datatype.
        """

        return f"[{self.name} in sheet {self.worksheet.title}]({self.worksheet.url})"

    @property
    def linkml_type_mappings(self):
        mapping_rows = list(
            filter(
                lambda r: r is not None,
                [row.get(DatatypeWorksheet.COL_EXTERNAL_MAPPINGS) for row in self.rows],
            )
        )
        if len(mapping_rows) > 0:
            mapping_string = "\n".join(mapping_rows)
        else:
            mapping_string = ""

        # TODO: parse all external mappings and include them.
        linkml_matches = re.findall(
            r"LINKML:(\w+)\W", mapping_string, flags=re.IGNORECASE
        )
        return linkml_matches

    @property
    def mappings(self) -> Mappings:
        """
        Returns the list of mappings for this datatype.
        """
        mappings = Mappings(self)
        mappings.add_mappings(
            self.datatype_row.get("External Mapping"),
            MappingRelations.SKOS_RELATED_MATCH,
        )
        return mappings

    def as_linkml(self, root_uri) -> TypeDefinition:
        """
        Returns a LinkML TypeDefinition describing this datatype.

        :param root_uri: The root URI to use for this datatype.
        :return: A LinkML TypeDefinition describing this datatype.
        """
        logging.info(f"Generating LinkML for {self}")

        # Basic metadata
        first_typeof = (self.linkml_type_mappings or ["string"])[0]
        typ: TypeDefinition = TypeDefinition(
            name=self.name,
            description=(self.datatype_row.get("Description") or "").strip(),
            typeof=first_typeof.lower(),
        )

        # Additional metadata

        # We add a 'derived from' note to the notes field, which might be
        # a string or a list, apparently.
        derived_from = f"Derived from {self.to_markdown()}"
        if isinstance(typ.notes, list):
            typ.notes.append(derived_from)
        elif isinstance(typ.notes, str):
            typ.notes = typ.notes + f"\n{derived_from}"
        else:
            typ.notes = derived_from

        # Add mappings.
        self.mappings.set_mappings_on_element(typ)

        return typ


class DatatypeWorksheet(ModelElement):
    """
    A Worksheet represents a single worksheet in a GSheetModel. DatatypeWorksheets contain one or
    (more likely) more than one datatype definitions.
    """

    # Some column names.
    COL_STATUS = "Status"
    COL_DATATYPE_NAME = "Entity"
    COL_DESCRIPTION = "Description"
    COL_EXTERNAL_MAPPINGS = "External Mappings"

    def is_sheet_datatype(worksheet: worksheet):
        """
        Identify worksheets containing datatypes, i.e. those that have:
            - COL_STATUS in cell A1, and
            - COL_DATATYPE_NAME in cell B1, and
            - COL_DESCRIPTION in cell C1.
        """
        return worksheet.get_values("A1", "C1") == [
            [
                DatatypeWorksheet.COL_STATUS,
                DatatypeWorksheet.COL_DATATYPE_NAME,
                DatatypeWorksheet.COL_DESCRIPTION,
            ]
        ]

    def __init__(self, model, sheet: worksheet):
        """
        Create a datatype worksheet based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this worksheet is a part of.
        :param sheet: A Google Sheet worksheet describing this worksheet.
        """

        self.model = model
        self.worksheet = sheet

    @property
    def rows(self) -> list[dict]:
        """
        Returns this datatype worksheet as a list of rows. We use the header row to create these dictionaries.

        :return: A list of the rows in this sheet.
        """
        return self.worksheet.get_all_records(empty_value=None)

    @property
    def included_rows(self) -> list[dict]:
        """
        Returns this datatype worksheet as a list of included rows.

        An included row is one whose COL_STATUS is set to 'include'.

        :return: A list of included rows in this sheet.
        """
        return [
            row
            for row in self.rows
            if row.get(DatatypeWorksheet.COL_STATUS, "") == "include"
        ]

    @property
    def datatype_names(self) -> list[str]:
        """
        Return a list of all the datatype names in this worksheet.

        :return: A list of all the datatype names in this worksheet.
        """

        return [
            (row.get(DatatypeWorksheet.COL_DATATYPE_NAME) or "")
            for row in self.included_rows()
        ]

    @property
    def datatypes_as_included_rows(self) -> dict[str, list[dict]]:
        """
        Group the list of rows based on having identical COL_DATATYPE_NAME values.

        :return: A dict with keys of COL_DATATYPE_NAME values and values of included rows having that value.
        """

        result = dict()

        for row in self.included_rows:
            datatype_name = row.get(DatatypeWorksheet.COL_DATATYPE_NAME) or ""
            if not (datatype_name in result):
                result[datatype_name] = list()

            result[datatype_name].append(row)

        return result

    @property
    def grouped_datatypes(self) -> dict[str, Datatype]:
        """
        Return a list of datatypes in this file, grouped into a dict by key name.

        :return: A dict with keys of COL_ENTITY_NAME values and values of Datatype objects.
        """

        return {
            k: Datatype(self.model, self.worksheet, k, v)
            for k, v in self.datatypes_as_included_rows.items()
        }

    @property
    def datatypes(self) -> list[Datatype]:
        """
        Return a list of datatypes in this worksheet.

        :return: A list of Datatype objects.
        """

        return list(self.grouped_datatypes.values())

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
        Return this worksheet as a filename, which we calculate by making the datatype name safe.

        :return: A filename that could be used for this datatype.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.worksheet.title).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", name)

    def to_markdown(self) -> str:
        """
        :return: A Markdown representation of this datatype.
        """

        return f"[{self.worksheet.title}]({self.worksheet.url})"

    def as_linkml(self, root_uri) -> list[TypeDefinition]:
        """
        Return all LinkML TypeDefinitions in this worksheet. We do this by converting each
        Datatype into its LinkML TypeDefinition.

        :param root_uri: The root URI to use for this worksheet.
        :return: A list of LinkML TypeDefinitions representing entities in this worksheet.
        """
        return [datatype.as_linkml(root_uri) for datatype in self.datatypes.values()]
