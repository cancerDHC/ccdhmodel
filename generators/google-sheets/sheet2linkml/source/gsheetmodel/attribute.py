from linkml_model.meta import SchemaDefinition, SlotDefinition, ElementName, ClassDefinition, ClassDefinitionName, TypeDefinitionName, TypeDefinition


class Attribute:
    """
    An attribute represents a single property within an entity.

    It is represented by a single row in a Google Sheet spreadsheet.
    """

    COL_ATTRIBUTE_NAME = 'CDM Attribute Name'

    def __init__(self, model, entity, row: dict):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this attribute is a part of.
        :param entity: The Entity that this attribute is a part of.
        """

        self.model = model
        self.entity = entity
        self.row = row

    @property
    def name(self):
        return self.row.get('CDM Attribute Name') or self.row.get('Name') or self.row.get('name')

    def __str__(self):
        """
        :return: A text description of this row.
        """

        return f'{self.__class__.__name__} named "{self.name}" containing {len(self.row)} properties'

    def as_linkml(self, root_uri) -> SlotDefinition:
        """
        Returns this attribute as a LinkML SlotDefinition.

        :param root_uri: The root URI to use for this SlotDefinition.
        :return: A LinkML SlotDefinition representing this attribute.
        """

        data = self.row

        slot: SlotDefinition = SlotDefinition(
            name=data[Attribute.COL_ATTRIBUTE_NAME],
            description=data.get('Description'),
            comments=data.get('Comments'),
            notes=data.get('Developer Notes')
        )

        return slot
