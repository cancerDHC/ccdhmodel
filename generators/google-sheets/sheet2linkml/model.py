from abc import ABC, abstractmethod
from linkml_model.meta import SchemaDefinition


class ModelElement(ABC):
    """
    A Model Element represents a model element that can be convert into a LinkML model.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        :return: A name for this model element.
        """
        pass

    @property
    @abstractmethod
    def full_name(self) -> str:
        """
        :return: The full name of this model element.
        """
        pass

    @abstractmethod
    def get_filename(self) -> str:
        """
        :return: This model element as a string.
        """
        pass

    @abstractmethod
    def get_filename(self) -> str:
        """
        :return: This model element as a string.
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
