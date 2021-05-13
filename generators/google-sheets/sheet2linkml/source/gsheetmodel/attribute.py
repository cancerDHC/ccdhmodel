from linkml_model.meta import SlotDefinition
import re


class Attribute:
    """
    An attribute represents a single property within an entity.

    It is represented by a single row in a Google Sheet spreadsheet.
    """

    # Some column names.
    COL_ATTRIBUTE_NAME = "CDM Attribute Name"
    COL_CARDINALITY = "Cardinality"

    def __init__(self, model, entity, row: dict[str, str]):
        """
        Create an entity based on a GSheetModel and a Google Sheet worksheet.

        :param model: The GSheetModel that this attribute is a part of.
        :param entity: The Entity that this attribute is a part of.
        :param row: The row describing this attribute (as a dictionary of str -> str).
        """

        self.model = model
        self.entity = entity
        self.row = row

    @property
    def name(self):
        """
        :return: A name for this attribute.
        """
        return (
            self.row.get("CDM Attribute Name")
            or self.row.get("Name")
            or self.row.get("name")
        )

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

        cardinality = self.row.get(Attribute.COL_CARDINALITY)
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

    def as_linkml(self, root_uri) -> SlotDefinition:
        """
        Returns this attribute as a LinkML SlotDefinition.

        :param root_uri: The root URI to use for this SlotDefinition.
        :return: A LinkML SlotDefinition representing this attribute.
        """

        data = self.row
        min_count, max_count = self.counts()

        slot: SlotDefinition = SlotDefinition(
            name=data[Attribute.COL_ATTRIBUTE_NAME],
            description=data.get("Description"),
            comments=data.get("Comments"),
            notes=data.get("Developer Notes"),
            required=(min_count > 0),
            multivalued=(max_count is None or max_count > 1),
        )

        cardinality = data.get(Attribute.COL_CARDINALITY)
        if cardinality:
            slot.notes.append(f"Cardinality: {cardinality}")

        # TODO: Add slot.range.

        return slot
