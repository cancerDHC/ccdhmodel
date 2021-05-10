from sheet2linkml.model import Model
from sheet2linkml.source.gsheetmodel.attribute import Attribute
from pygsheets import worksheet
from linkml_model.meta import SchemaDefinition, SlotDefinition, ElementName, ClassDefinition, ClassDefinitionName, TypeDefinitionName, TypeDefinition
import logging
import re


class Entity(Model):
    """
    An entity represents a class of data that we need to model.

    It is represented by a single worksheet in a Google Sheet spreadsheet.
    """

    COL_ATTRIBUTE_NAME = 'CDM Attribute Name'

    def __init__(self, model, sheet: worksheet, name, rows):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this entity is a part of.
        :param worksheet: A Google Sheet worksheet describing this entity.
        """

        self.model = model
        self.worksheet = sheet
        self.name = name
        self.rows = rows

    @property
    def attribute_rows(self) -> list[dict]:
        """
        Returns this entity as a list of named rows.

        A named row is one where the COL_ATTRIBUTE_NAME row is not empty.

        :return: A list of named rows in this sheet.
        """
        return [row for row in self.rows if row.get(Entity.COL_ATTRIBUTE_NAME) is not None]

    @property
    def attributes(self):
        """
        :return: A list of all the attributes in this entity.
        """

        return [Attribute(self.model, self, dct) for dct in self.attribute_rows]

    @property
    def entity_row(self) -> dict:
        """
        Returns the "entity row" -- the row in the spreadsheet that represents this entity itself.
        This is the (single) row without an attribute name.

        :return: A dictionary representing a row in the spreadsheet that represents this entity.
        """

        entity_rows = [row for row in self.rows if row.get(Entity.COL_ATTRIBUTE_NAME) is None]
        if not entity_rows:
            # raise RuntimeError(f'Entity does not have an entity row: {self}')
            logging.warn(f'Entity contains no entity row: {self}')
            return dict()

        if len(entity_rows) > 1:
            logging.warn(f'Entity contains more than one "entity row", only the first one will be used: {self}')
            for row in entity_rows:
                logging.warn(f' - Found entity row: {row}')

        return entity_rows[0]

    def __str__(self):
        """
        :return: A text description of this entity.
        """

        return f'{self.__class__.__name__} named {self.name} from worksheet "{self.worksheet.title}" containing {len(self.attribute_rows)} attributes'

    def get_filename(self) -> str:
        """
        Return this entity as a filename, which we calculate by making the entity name safe for

        :return: A filename that could be used for this entity.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.name).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', name)

    def to_markdown(self) -> str:
        """
        :return: A Markdown representation of this entity.
        """

        return f'[{self.name} in sheet {self.worksheet.title}]({self.worksheet.url})'

    def as_linkml(self, root_uri) -> SchemaDefinition:
        """
        Return this entity as a LinkML SchemaDefinition.

        :param root_uri:
        :return:
        """

        logging.info(f'Generating LinkML for {self}')

        unprefixed_name = re.sub('^CDM\.', '', self.get_filename())

        # Basic metadata
        schema: SchemaDefinition = SchemaDefinition(
            name=unprefixed_name,
            id=f'{root_uri}/entity/{unprefixed_name}',
            title=self.name,
            version='v0', # TODO: Replace with a version.
            license='https://creativecommons.org/publicdomain/zero/1.0/',
            prefixes={
                'linkml': 'https://w3id.org/biolink/linkml/',
                'ccdh': f'{root_uri}/'
            },
            see_also=self.worksheet.url,

            description=self.entity_row.get('Description'),
            comments=self.entity_row.get('Comments'),
            notes=self.entity_row.get('Developer Notes')
        )

        # Additional metadata

        # We add a 'derived from' note to the notes field, which might be
        # a string or a list, apparently.
        derived_from = f'Derived from {self.to_markdown()}'
        if isinstance(schema.notes, list):
            schema.notes.append(derived_from)
        elif isinstance(schema.notes, str):
            schema.notes = schema.notes + f'\n{derived_from}'
        else:
            schema.notes = derived_from

        # TODO: See if we can get by without.
        # schema.imports = ['datatypes', 'prefixes']

        # TODO: Add mappings (https://linkml.github.io/linkml-model/docs/mappings/)

        # Now generate LinkML for all of the attributes.

        schema.slots = [attribute.as_linkml(root_uri) for attribute in self.attributes]

        return schema


class Worksheet(Model):
    """
    A Worksheet represents a single worksheet in a GSheetModel. A single sheet usually contains
    information on a single Entity, but this is not always the case. In those cases, you should
    access the Worksheet and use that to get the list of entities.
    """

    # Some column names.
    COL_STATUS = 'Status'
    COL_ENTITY_NAME = 'CDM Entity'

    def __init__(self, model, sheet: worksheet):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this entity is a part of.
        :param worksheet: A Google Sheet worksheet describing this entity.
        """

        self.model = model
        self.worksheet = sheet

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
        return [row for row in self.rows if row.get(Worksheet.COL_STATUS, '') == 'include']

    @property
    def entity_names(self) -> list[str]:
        """
        Return a list of all the entity names in this worksheet.

        :return: A list of all the entity names in this worksheet.
        """

        return [row[Worksheet.COL_ENTITY_NAME] for row in self.included_rows()]

    @property
    def entities_as_included_rows(self) -> dict[str, list[dict]]:
        """
        Group the list of rows based on having identical COL_ENTITY_NAME values.

        :return: A dict with keys of COL_ENTITY_NAME values and values of included rows having that value.
        """

        result = dict()

        for row in self.included_rows:
            col_name = row[Worksheet.COL_ENTITY_NAME]
            if not (col_name in result):
                result[col_name] = list()

            result[col_name].append(row)

        return result

    @property
    def grouped_entities(self) -> dict[str, Entity]:
        """
        Return a list of entities in this file, grouped into a dict by key name.

        :return: A dict with keys of COL_ENTITY_NAME values and values of Entity objects.
        """

        return {k: Entity(self.model, self.worksheet, k, v) for k, v in self.entities_as_included_rows.items()}

    @property
    def entities(self) -> dict[str, Entity]:
        """
        Return a list of entities in this file.

        :return: A list of Entity objects.
        """

        return list(self.grouped_entities.values())

    def get_filename(self) -> str:
        """
        Return this worksheet as a filename, which we calculate by making the entity name safe.

        :return: A filename that could be used for this entity.
        """

        # Taken from https://stackoverflow.com/a/46801075/27310
        name = str(self.worksheet.title).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', name)

    def to_markdown(self) -> str:
        """
        :return: A Markdown representation of this entity.
        """

        return f'[{self.worksheet.title}]({self.worksheet.url})'

    def as_linkml(self, root_uri) -> list[SchemaDefinition]:
        return [entity.as_linkml(root_uri) for entity in self.entities.values()]
