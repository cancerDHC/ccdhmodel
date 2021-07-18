from linkml_model import SchemaDefinition

from functools import cached_property
from sheet2linkml.terminologies.service import TerminologyService
from sheet2linkml.model import ModelElement
from sheet2linkml.source.gsheetmodel.mappings import Mappings, MappingRelations
from sheet2linkml.source.gsheetmodel.enum import Enum
from pygsheets import worksheet
from linkml_model.meta import (
    ClassDefinition,
    SlotDefinition,
    EnumDefinition,
    PermissibleValue,
    Example,
)
import logging
import re
import urllib.parse


class Entity(ModelElement):
    """
    An entity represents a class of data that we need to model.

    It is represented by a single worksheet in a Google Sheet spreadsheet.
    """

    def __init__(
        self,
        model,
        sheet: worksheet,
        name: str,
        rows: list[dict[str, str]],
        terminology_service: TerminologyService,
    ):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this entity is a part of.
        :param sheet: A Google Sheet worksheet describing this entity.
        :param name: The name of this entity.
        :param rows: The rows in the spreadsheet describing this entity (as dictionaries of str -> str).
        :param terminology_service: The TerminologyService to access the codesets we use.
        """

        self.model = model
        self.worksheet = sheet
        self.entity_name = name
        self.rows = rows
        self.terminology_service = terminology_service

    @property
    def attribute_rows(self) -> list[dict[str, str]]:
        """
        Returns this entity as a list of attribute rows.

        An attribute row is one where the COL_ATTRIBUTE_NAME row is not empty.

        :return: A list of named rows in this sheet.
        """
        return [
            row
            for row in self.rows
            if row.get(EntityWorksheet.COL_ATTRIBUTE_NAME) is not None
        ]

    @cached_property
    def attributes(self):
        """
        Returns a list of attributes in this entity. We construct this by wrapping the
        attribute rows with Attribute().

        :return: A list of all the attributes in this entity.
        """

        return [
            Attribute(
                self.model, self, dct, terminology_service=self.terminology_service
            )
            for dct in self.attribute_rows
        ]

    @property
    def entity_row(self) -> dict[str, str]:
        """
        Returns the "entity row" -- the single row in the spreadsheet that represents this
        entity itself. Writes errors in the logs if more than one "entity row" is found (only the
        first will be used).

        :return: A dictionary representing a row in the spreadsheet that represents this entity.
        """

        # Find all entity rows
        entity_rows = [
            row
            for row in self.rows
            if row.get(EntityWorksheet.COL_ATTRIBUTE_NAME) is None
        ]

        # Report an error if no rows were found.
        if not entity_rows:
            # raise RuntimeError(f'Entity does not have an entity row: {self}')
            logging.error(f"Entity contains no entity row: {self}")
            return dict()

        # Report an error if more than one row was found.
        if len(entity_rows) > 1:
            logging.error(
                f'Entity contains more than one "entity row", only the first one will be used: {self}'
            )
            for row in entity_rows:
                logging.error(f" - Found entity row: {row}")

        return entity_rows[0]

    def __str__(self):
        """
        :return: A text description of this entity.
        """

        return f'{self.__class__.__name__} named {self.name} from worksheet "{self.worksheet.title}" containing {len(self.attribute_rows)} attributes'

    @property
    def name(self) -> str:
        """
        :return: A name for this entity.
        """
        return (self.entity_name or "(unnamed entity)").strip()

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this entity.
        """
        return f"CRDC-H.{self.entity_name}"

    def get_filename(self) -> str:
        """
        Return this entity as a filename, which we calculate by making the entity name safe for file systems.

        :return: A filename that can be used for this entity.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.name).strip().replace(" ", "_")
        return re.sub(r"(?u)[^-\w.]", "", name)

    def to_markdown(self) -> str:
        """
        Returns a reference to this entity in Markdown. We include the name, worksheet name and worksheet URL.

        :return: A Markdown representation of this entity.
        """

        return f"[{self.name} in sheet {self.worksheet.title}]({self.worksheet.url})"

    @cached_property
    def mappings(self) -> Mappings:
        """
        Returns the list of mappings for this entity.
        """
        mappings = Mappings(self)
        mappings.add_mappings(
            self.entity_row.get("Source Mapping"), MappingRelations.SKOS_EXACT_MATCH
        )
        mappings.add_mappings(
            self.entity_row.get("Indirect Source Mapping"),
            MappingRelations.SKOS_CLOSE_MATCH,
        )
        return mappings

    @property
    def mappings_including_attributes(self) -> list[Mappings.Mapping]:
        """
        Returns the list of all mappings of this entity as well as all of its attributes.
        """
        mappings = list(self.mappings.mappings)
        for attr in self.attributes:
            mappings.extend(attr.mappings.mappings)
        return mappings

    def as_linkml(self, root_uri) -> ClassDefinition:
        """
        Returns a LinkML ClassDefinition describing this entity, including attributes.

        :param root_uri: The root URI to use for this entity.
        :return: A LinkML ClassDefinition describing this entity.
        """
        logging.info(f"Generating LinkML for {self}")

        # Basic metadata
        cls: ClassDefinition = ClassDefinition(
            name=self.name,
            description=(self.entity_row.get("Description") or "").strip(),
            comments=self.entity_row.get("Comments"),
        )

        if self.name != "Entity":
            cls.is_a = "Entity"

        # Additional metadata

        # We add a 'derived from' note to the notes field, which might be
        # a string or a list, apparently.
        derived_from = f"Derived from {self.to_markdown()}"
        if isinstance(cls.notes, list):
            cls.notes.append(derived_from)
        elif isinstance(cls.notes, str):
            cls.notes = cls.notes + f"\n{derived_from}"
        else:
            cls.notes = derived_from

        # Add mappings
        self.mappings.set_mappings_on_element(cls)

        # Now generate LinkML for all of the attributes.
        cls.attributes = {
            attribute.name: attribute.as_linkml(root_uri)
            for attribute in self.attributes
        }

        return cls


class Attribute:
    """
    An attribute represents a single property within an entity.

    It is represented by a single row in a Google Sheet spreadsheet.
    """

    def __init__(
        self,
        model,
        entity,
        row: dict[str, str],
        terminology_service: TerminologyService,
    ):
        """
        Create an attribute based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this attribute is a part of.
        :param entity: The Entity that this attribute is a part of.
        :param row: The row describing this attribute (as a dictionary of str -> str).
        :param terminology_service: The TerminologyService to use for accessing codeset information.
        """

        self.model = model
        self.entity = entity
        self.row = row
        self.terminology_service = terminology_service

    @property
    def name(self):
        """
        :return: A name for this attribute.
        """
        return (
            self.row.get(EntityWorksheet.COL_ATTRIBUTE_NAME)
            or self.row.get("Name")
            or self.row.get("name")
        )

    @property
    def full_name(self) -> str:
        """
        :return: The full name of this attribute.
        """
        return f"{self.entity.full_name}.{self.name}"

    def __str__(self):
        """
        :return: A text description of this row.
        """

        return f'{self.__class__.__name__} named "{self.name}" containing {len(self.row)} properties'

    def counts(self) -> (int, int):
        """
        Returns the minimum and maximum cardinality, determined by parsing the Cardinality column.
        If the string is `?..m`, this indicates that there is no maximum cardinality -- which we
        report by returning None instead of the maximum cardinality.

        :return: The minimum and maximum cardinality by reading the 'Cardinality' column.
        """

        # A default cardinality to return if none can be parsed.
        default = 0, None

        cardinality = self.row.get(EntityWorksheet.COL_CARDINALITY)
        if not cardinality:
            return default

        # We currently use `1..m` to indicate that there is no maximum cardinality.
        # We might eventually need to support `1..*` as well.
        m = re.compile("^(\\d+)\\.\\.(\\d+|m)$").match(str(cardinality))
        if not m:
            return default

        min_count = int(m.group(1))
        max_count = None
        if (
            m.group(2) != "m"
        ):  # We use '..m' to indicate that there is no maximum value.
            max_count = int(m.group(2))

        return min_count, max_count

    @cached_property
    def mappings(self) -> Mappings:
        """
        Returns the list of mappings for this attribute.
        """
        mappings = Mappings(self)
        mappings.add_mappings(
            self.row.get("Source Mapping"), MappingRelations.SKOS_EXACT_MATCH
        )
        mappings.add_mappings(
            self.row.get("Indirect Source Mapping"), MappingRelations.SKOS_CLOSE_MATCH
        )
        return mappings

    @property
    def range(self):
        """
        Return the range of this attribute.
        """

        attribute_range = "string"  # Default to linkml:string.
        if EntityWorksheet.COL_TYPE in self.row:
            attribute_range = self.row.get(EntityWorksheet.COL_TYPE) or "string"

            # For primitive types, we need to add `ccdh_` to the start of the type name.
            if attribute_range[0].islower():
                attribute_range = f"ccdh_{attribute_range}"

        return attribute_range

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

        return fixed_name

    def as_linkml_enum(self) -> EnumDefinition:
        """
        If this is an attribute with an enumeration of possible values,
        this method will return this enumeration as a LinkML EnumDefinition.
        """
        if not self.terminology_service:
            return None

        if self.range != EntityWorksheet.ENTITY_CODEABLE_CONCEPT:
            return None

        # Look up enumerations on the Terminology Service.
        enum_info = self.terminology_service.get_enum_values_for_field(self.full_name)
        permissible_values = {}
        for pv in enum_info.get("permissible_values", []):
            text = pv.get("text")
            if text in permissible_values.keys():
                logging.warning(
                    f"In field '{self.full_name}', found duplicate permissible value text: {text} was previously assigned to {permissible_values[text]}, but will now be replaced with {pv}"
                )

            permissible_values[str(text)] = PermissibleValue(
                text=text, description=pv.get("description"), meaning=pv.get("meaning")
            )

        return EnumDefinition(
            name=Enum.fix_enum_name(self.full_name),
            code_set=f"https://terminology.ccdh.io/enumerations/{urllib.parse.quote_plus(self.full_name)}",
            code_set_version=enum_info.get("last_updated", ""),
            comments=f'Name according to TCCM: "{enum_info.get("name", "")}"',
            description=enum_info.get("description"),
            permissible_values=list(permissible_values.values()),
        )

    def as_linkml(self, root_uri) -> SlotDefinition:
        """
        Returns this attribute as a LinkML SlotDefinition.

        :param root_uri: The root URI to use for this SlotDefinition.
        :return: A LinkML SlotDefinition representing this attribute.
        """

        data = self.row
        min_count, max_count = self.counts()

        # Set up some complex fields.
        examples = re.split(
            r"\s*[\r\n\|]\s*", (data.get("Example Values") or "").strip()
        )
        if len(examples) == 0:
            examples = []
        else:
            examples = [Example(value=example) for example in examples]

        attribute_range = self.range
        # For CodeableConcepts, we currently replace it with an enumeration.
        # In future versions, we will instead constrain the CodeableConcept's codes in some way.
        if self.terminology_service and attribute_range == "CodeableConcept":
            # Logically, we should be able to set `attribute_range` to the EnumDefinition.
            # But LinkML doesn't support that yet. So instead, we'll refer to the enum definition
            # here and enter it elsewhere in the YAML file.
            attribute_range = Enum.fix_enum_name(self.full_name)

        slot: SlotDefinition = SlotDefinition(
            name=data.get(EntityWorksheet.COL_ATTRIBUTE_NAME) or "",
            description=(data.get("Description") or "").strip(),
            examples=examples,
            comments=data.get("Comments"),
            # notes=data.get("Developer Notes"),
            required=(min_count > 0),
            multivalued=(max_count is None or max_count > 1),
            domain=self.entity.name,
            range=attribute_range,
        )

        # Multivalued fields need to be inlined as a list.
        # (Eventually, we might want to inline some of these as dicts, but not yet.)
        if max_count is None or max_count > 1:
            # Except for enumerated fields.
            if self.range != EntityWorksheet.ENTITY_CODEABLE_CONCEPT:
                slot.inlined_as_list = True

        cardinality = data.get(EntityWorksheet.COL_CARDINALITY)
        if cardinality:
            slot.notes.append(f"Cardinality: {cardinality}")

        # Add mappings
        self.mappings.set_mappings_on_element(slot)

        return slot


class EntityWorksheet(ModelElement):
    """
    A Worksheet represents a single worksheet in a GSheetModel. A single sheet usually contains
    information on a single Entity, but sometimes multiple entities may be described in a single
    Worksheet. In that case, this Worksheet will return multiple entities.
    """

    # Some column names.
    COL_STATUS = "Status"
    COL_ENTITY_NAME = "Entity"
    COL_ATTRIBUTE_NAME = "Attribute"
    COL_CARDINALITY = "Cardinality"
    COL_TYPE = "Type"

    # Some entity names.
    ENTITY_CODEABLE_CONCEPT = "CodeableConcept"

    @staticmethod
    def is_sheet_entity(worksheet: worksheet):
        """Identify worksheets containing entities, i.e. those that have:
        - COL_STATUS in cell A1, and
        - COL_ENTITY_NAME in cell B1, and
        - COL_ATTRIBUTE_NAME in cell C1.
        """
        return worksheet.get_values("A1", "C1") == [
            [
                EntityWorksheet.COL_STATUS,
                EntityWorksheet.COL_ENTITY_NAME,
                EntityWorksheet.COL_ATTRIBUTE_NAME,
            ]
        ]

    def __init__(
        self, model, sheet: worksheet, terminology_service: TerminologyService
    ):
        """
        Create a worksheet based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this worksheet is a part of.
        :param sheet: A Google Sheet worksheet describing this worksheet.
        """

        self.model = model
        self.worksheet = sheet
        self.terminology_service = terminology_service

    @property
    def rows(self) -> list[dict]:
        """
        Returns this entity as a list of rows. We use the header row to create these dictionaries.

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
            if row.get(EntityWorksheet.COL_STATUS, "") == "include"
        ]

    @property
    def entity_names(self) -> list[str]:
        """
        Return a list of all the entity names in this worksheet.

        :return: A list of all the entity names in this worksheet.
        """

        return [
            (row.get(EntityWorksheet.COL_ENTITY_NAME) or "")
            for row in self.included_rows()
        ]

    @property
    def entities_as_included_rows(self) -> dict[str, list[dict]]:
        """
        Group the list of rows based on having identical COL_ENTITY_NAME values.

        :return: A dict with keys of COL_ENTITY_NAME values and values of included rows having that value.
        """

        result = dict()

        for row in self.included_rows:
            entity_name = row.get(EntityWorksheet.COL_ENTITY_NAME) or ""
            if not (entity_name in result):
                result[entity_name] = list()

            result[entity_name].append(row)

        # The Google Sheet might indicate that the entity row (the row without an attribute name) should be excluded.
        # If any other rows have been included for this entity, however, they would be used to define the entity,
        # even though the intention was to exclude that entity. In order to prevent this, we will check for any included
        # rows that don't have an entity row -- such groups will be filtered out here.
        filtered = dict()

        for name, rows in result.items():
            if any(row.get(EntityWorksheet.COL_ATTRIBUTE_NAME) is None for row in rows):
                filtered[name] = rows
            else:
                logging.warning(
                    f"- Ignoring entity {name} in worksheet {self.name} as it does not have an entity row."
                )

        # Make sure that we only have a single entity name in this Worksheet -- the name of the sheet itself.
        entity_names = list(filtered.keys())
        if not (len(entity_names) == 1 and entity_names[0] == self.name):
            logging.warning(
                f"Expected entity worksheet {self.name} to contain a single entity, but found {len(entity_names)}: {', '.join(entity_names)}"
            )

        return filtered

    @property
    def grouped_entities(self) -> dict[str, Entity]:
        """
        Return a list of entities in this file, grouped into a dict by key name.

        :return: A dict with keys of COL_ENTITY_NAME values and values of Entity objects.
        """

        return {
            k: Entity(
                self.model,
                self.worksheet,
                k,
                v,
                terminology_service=self.terminology_service,
            )
            for k, v in self.entities_as_included_rows.items()
        }

    @property
    def entities(self) -> list[Entity]:
        """
        Return a list of entities in this file.

        :return: A list of Entity objects.
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
        return [entity.as_linkml(root_uri) for entity in self.entities.values()]
