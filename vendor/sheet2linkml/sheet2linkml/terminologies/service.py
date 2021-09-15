from abc import ABC, abstractmethod


class TerminologyService(ABC):
    """
    A TerminologyService is a base class for all terminology services. These will usually be APIs, but in some
    cases might read enumerations from local resources (such as a Google Sheet worksheet).
    """

    @abstractmethod
    def get_enum_values_for_field(self, field_name):
        """
        Get the enumerated values for a particular field.

        In the interests of time, this currently returns a custom Python nested dict structure. In future versions,
        this will return a list of permissible values or another structured output.

        :param field_name: The name of the field. Should be in the format "Model Name.Entity Name.Attribute Name",
            such as `CRDC-H.Specimen.analyte_type`.
        """

        pass
