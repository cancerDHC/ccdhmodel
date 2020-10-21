# Auto generated from datatypes.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-10-20 22:34
# Schema: datatypes
#
# id: https://ccdh.example.org/model/datatypes
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TYPES = CurieNamespace('types', 'https://ccdh.example.org/datatypes/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TYPES


# Types
class Literal(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "literal"
    type_model_uri = TYPES.Literal


class Url(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "url"
    type_model_uri = TYPES.Url


# Class references



@dataclass
class Identifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Identifier
    class_class_curie: ClassVar[str] = "types:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = TYPES.Identifier

    value: Optional[Union[str, Literal]] = None
    system: Optional[Union[str, Literal]] = None
    type: Optional[Union[dict, "Coding"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, Literal):
            self.value = Literal(self.value)
        if self.system is not None and not isinstance(self.system, Literal):
            self.system = Literal(self.system)
        if self.type is not None and not isinstance(self.type, Coding):
            self.type = Coding(**self.type)
        super().__post_init__(**kwargs)


@dataclass
class Quantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Quantity
    class_class_curie: ClassVar[str] = "types:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = TYPES.Quantity

    value: Optional[Union[str, Literal]] = None
    unit: Optional[Union[dict, "Coding"]] = None
    comparator: Optional[Union[dict, "Coding"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, Literal):
            self.value = Literal(self.value)
        if self.unit is not None and not isinstance(self.unit, Coding):
            self.unit = Coding(**self.unit)
        if self.comparator is not None and not isinstance(self.comparator, Coding):
            self.comparator = Coding(**self.comparator)
        super().__post_init__(**kwargs)


@dataclass
class Coding(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Coding
    class_class_curie: ClassVar[str] = "types:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = TYPES.Coding

    code: Optional[Union[str, Literal]] = None
    display: Optional[Union[str, Literal]] = None
    system: Optional[Union[str, Url]] = None
    version: Optional[Union[str, Literal]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.code is not None and not isinstance(self.code, Literal):
            self.code = Literal(self.code)
        if self.display is not None and not isinstance(self.display, Literal):
            self.display = Literal(self.display)
        if self.system is not None and not isinstance(self.system, Url):
            self.system = Url(self.system)
        if self.version is not None and not isinstance(self.version, Literal):
            self.version = Literal(self.version)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.value = Slot(uri=TYPES.value, name="value", curie=TYPES.curie('value'),
                      model_uri=TYPES.value, domain=None, range=Optional[Union[str, Literal]])

slots.system = Slot(uri=TYPES.system, name="system", curie=TYPES.curie('system'),
                      model_uri=TYPES.system, domain=None, range=Optional[Union[str, Literal]])

slots.type = Slot(uri=TYPES.type, name="type", curie=TYPES.curie('type'),
                      model_uri=TYPES.type, domain=None, range=Optional[Union[dict, Coding]])

slots.unit = Slot(uri=TYPES.unit, name="unit", curie=TYPES.curie('unit'),
                      model_uri=TYPES.unit, domain=None, range=Optional[Union[dict, Coding]])

slots.comparator = Slot(uri=TYPES.comparator, name="comparator", curie=TYPES.curie('comparator'),
                      model_uri=TYPES.comparator, domain=None, range=Optional[Union[dict, Coding]])

slots.code = Slot(uri=TYPES.code, name="code", curie=TYPES.curie('code'),
                      model_uri=TYPES.code, domain=None, range=Optional[Union[str, Literal]])

slots.display = Slot(uri=TYPES.display, name="display", curie=TYPES.curie('display'),
                      model_uri=TYPES.display, domain=None, range=Optional[Union[str, Literal]])

slots.version = Slot(uri=TYPES.version, name="version", curie=TYPES.curie('version'),
                      model_uri=TYPES.version, domain=None, range=Optional[Union[str, Literal]])

slots.Identifier_value = Slot(uri=TYPES.value, name="Identifier_value", curie=TYPES.curie('value'),
                      model_uri=TYPES.Identifier_value, domain=Identifier, range=Optional[Union[str, Literal]])

slots.Identifier_system = Slot(uri=TYPES.system, name="Identifier_system", curie=TYPES.curie('system'),
                      model_uri=TYPES.Identifier_system, domain=Identifier, range=Optional[Union[str, Literal]])

slots.Identifier_type = Slot(uri=TYPES.type, name="Identifier_type", curie=TYPES.curie('type'),
                      model_uri=TYPES.Identifier_type, domain=Identifier, range=Optional[Union[dict, "Coding"]])

slots.Quantity_value = Slot(uri=TYPES.value, name="Quantity_value", curie=TYPES.curie('value'),
                      model_uri=TYPES.Quantity_value, domain=Quantity, range=Optional[Union[str, Literal]])

slots.Quantity_unit = Slot(uri=TYPES.unit, name="Quantity_unit", curie=TYPES.curie('unit'),
                      model_uri=TYPES.Quantity_unit, domain=Quantity, range=Optional[Union[dict, "Coding"]])

slots.Quantity_comparator = Slot(uri=TYPES.comparator, name="Quantity_comparator", curie=TYPES.curie('comparator'),
                      model_uri=TYPES.Quantity_comparator, domain=Quantity, range=Optional[Union[dict, "Coding"]])

slots.Coding_code = Slot(uri=TYPES.code, name="Coding_code", curie=TYPES.curie('code'),
                      model_uri=TYPES.Coding_code, domain=Coding, range=Optional[Union[str, Literal]])

slots.Coding_display = Slot(uri=TYPES.display, name="Coding_display", curie=TYPES.curie('display'),
                      model_uri=TYPES.Coding_display, domain=Coding, range=Optional[Union[str, Literal]])

slots.Coding_system = Slot(uri=TYPES.system, name="Coding_system", curie=TYPES.curie('system'),
                      model_uri=TYPES.Coding_system, domain=Coding, range=Optional[Union[str, Url]])

slots.Coding_version = Slot(uri=TYPES.version, name="Coding_version", curie=TYPES.curie('version'),
                      model_uri=TYPES.Coding_version, domain=Coding, range=Optional[Union[str, Literal]])
