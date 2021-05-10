from sheet2linkml.source.gsheetmodel.attribute import Attribute
from pygsheets import worksheet
from linkml_model.meta import SchemaDefinition, SlotDefinition, ElementName, ClassDefinition, ClassDefinitionName, TypeDefinitionName, TypeDefinition
import logging
import re


class Entity:
    """
    An entity represents a class of data that we need to model.

    It is represented by a single worksheet in a Google Sheet spreadsheet.
    """

    # Some column names.
    COL_STATUS = 'Status'
    COL_ENTITY_NAME = 'CDM Entity'
    COL_ATTRIBUTE_NAME = 'CDM Attribute Name'

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
    def named_rows(self) -> list[dict]:
        """
        Returns this entity as a list of named rows.

        A named row is one where the COL_ATTRIBUTE_NAME row is not empty.

        :return: A list of named rows in this sheet.
        """
        return [row for row in self.rows if row.get(Entity.COL_ATTRIBUTE_NAME) is not None]

    @property
    def included_named_rows(self) -> list[dict]:
        """
        Returns this entity as a list of named, included rows.

        A named, included row is one where a name is set and a

        :return: A list of named, included rows in this sheet.
        """
        return [row for row in self.named_rows if row.get(Entity.COL_STATUS, '') == 'include']

    @property
    def names(self) -> set:
        """
        Returns the names of this entity. We can determine this by finding all
        unique values in the 'CDM Entity' column in this sheet.

        :return: The set of all the names of this entity.
        """
        names_from_rows = set(row.get('CDM Entity') for row in self.included_named_rows)

        if names_from_rows:
            return names_from_rows

        return {f'(based on a Google Worksheet entitled "{self.worksheet.title}")'}

    @property
    def name(self) -> str:
        entity_name = list(self.names)[0]
        if len(self.names) > 1:
            logging.warning(f'Entity has more than one name: {self.names}! ' +
                            'Name "{entity_name}" will be used, but please fix this in the Google Sheet.')

        return entity_name

    @property
    def attributes(self):
        """
        :return: A list of all the attributes in this entity.
        """

        return [Attribute(self.model, self, dct) for dct in self.included_named_rows]

    def __str__(self):
        """
        :return: A text description of this entity.
        """

        return f'{self.__class__.__name__} named {self.name} from worksheet "{self.worksheet.title}" containing {len(self.included_named_rows)} included, named rows'

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

        return f'[{self.worksheet.title}]({self.worksheet.url})'

    def as_linkml(self, root_uri) -> SchemaDefinition:
        """
        Return this entity as a LinkML SchemaDefinition.

        :param root_uri:
        :return:
        """

        logging.info(f'Generating LinkML for {self}')

        unprefixed_name = re.sub('^CDM\.', '', self.get_filename())

        schema: SchemaDefinition = SchemaDefinition(
            name=unprefixed_name,
            id=f'{root_uri}/entity/{unprefixed_name}',
            title=self.name)
        schema.version = 'v0'   # TODO: Replace with a version.
        schema.license = 'https://creativecommons.org/publicdomain/zero/1.0/'
        schema.prefixes = {
            'linkml': 'https://w3id.org/biolink/linkml/',
            'ccdh': f'{root_uri}/'
        }
        # TODO: See if we can get by without.
        # schema.imports = ['datatypes', 'prefixes']

        schema.notes.append(f'derived from {self.to_markdown()}')
        return schema
