from abc import ABC, abstractmethod
from linkml_model.meta import SchemaDefinition


class Model(ABC):
    """
    A Model represents a class that can be convert into a YAML model.
    """

    @abstractmethod
    def get_filename(self) -> str:
        """
        Return this model element as a string.
        """
        pass

    @abstractmethod
    def to_markdown(self) -> str:
        """
        :return: A Markdown reference to this model.
        """
        pass

    @abstractmethod
    def as_linkml(self, root_uri) -> SchemaDefinition:
        """
        Return this model element as a LinkML SchemaDefinition.

        :param root_uri: The base URI to use for terms defined in this model.
        :return: A LinkML SchemaDefinition for the model described by this Google Sheet.
        """
        pass
