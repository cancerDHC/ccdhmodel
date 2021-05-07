from sheet2linkml.source.gsheetmodel.attribute import Attribute
from pygsheets import worksheet


class Entity:
    """
    An entity represents a class of data that we need to model.

    It is represented by a single worksheet in a Google Sheet spreadsheet.
    """

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
    def names(self):
        """
        Returns the names of this entity. We can determine this by finding all
        unique values in the 'CDM Entity' column in this sheet.

        :return: The set of all the names of this entity.
        """
        return set(map(lambda row: row.get('CDM Entity'), self.rows))

    @property
    def attributes(self):
        """
        :return: A list of all the attributes in this entity.
        """

        return [Attribute(self.model, self, dct) for dct in self.rows]

    def __str__(self):
        """
        :return: A text description of this entity.
        """

        return f'{self.__class__.__name__} named {self.names} containing {len(self.attributes)} attributes'