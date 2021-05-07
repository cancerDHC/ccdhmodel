class Attribute:
    """
    An attribute represents a single property within an entity.

    It is represented by a single row in a Google Sheet spreadsheet.
    """

    def __init__(self, model, entity, row: dict):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this attribute is a part of.
        :param entity: The Entity that this attribute is a part of.
        """

        self.model = model
        self.entity = entity
        self.data = row

    @property
    def name(self):
        return self.data.get('CDM Attribute Name') or self.data.get('Name') or self.data.get('name')

    def __str__(self):
        """
        :return: A text description of this row.
        """

        return f'{self.__class__.__name__} named "{self.name}" containing {len(self.data)} properties'
