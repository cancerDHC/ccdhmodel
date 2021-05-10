from sheet2linkml.source.gsheetmodel.attribute import Attribute
from pygsheets import worksheet


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
    def attributes(self):
        """
        :return: A list of all the attributes in this entity.
        """

        return [Attribute(self.model, self, dct) for dct in self.included_named_rows]

    def __str__(self):
        """
        :return: A text description of this entity.
        """

        return f'{self.__class__.__name__} named {self.names} from worksheet "{self.worksheet.title}" containing {len(self.included_named_rows)} included, named rows'
