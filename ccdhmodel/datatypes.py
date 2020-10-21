# Auto generated from datatypes.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-10-21 12:51
# Schema: datatypes
#
# id: https://example.org/ccdh/model/datatypes
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
TYPES = CurieNamespace('types', 'https://example.org/ccdh/datatypes/')
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

slots.identifier__value = Slot(uri=TYPES.value, name="identifier__value", curie=TYPES.curie('value'),
                      model_uri=TYPES.identifier__value, domain=None, range=Optional[Union[str, Literal]])

slots.identifier__system = Slot(uri=TYPES.system, name="identifier__system", curie=TYPES.curie('system'),
                      model_uri=TYPES.identifier__system, domain=None, range=Optional[Union[str, Literal]])

slots.identifier__type = Slot(uri=TYPES.type, name="identifier__type", curie=TYPES.curie('type'),
                      model_uri=TYPES.identifier__type, domain=None, range=Optional[Union[dict, Coding]])

slots.quantity__value = Slot(uri=TYPES.value, name="quantity__value", curie=TYPES.curie('value'),
                      model_uri=TYPES.quantity__value, domain=None, range=Optional[Union[str, Literal]])

slots.quantity__unit = Slot(uri=TYPES.unit, name="quantity__unit", curie=TYPES.curie('unit'),
                      model_uri=TYPES.quantity__unit, domain=None, range=Optional[Union[dict, Coding]])

slots.quantity__comparator = Slot(uri=TYPES.comparator, name="quantity__comparator", curie=TYPES.curie('comparator'),
                      model_uri=TYPES.quantity__comparator, domain=None, range=Optional[Union[dict, Coding]])

slots.coding__code = Slot(uri=TYPES.code, name="coding__code", curie=TYPES.curie('code'),
                      model_uri=TYPES.coding__code, domain=None, range=Optional[Union[str, Literal]])

slots.coding__display = Slot(uri=TYPES.display, name="coding__display", curie=TYPES.curie('display'),
                      model_uri=TYPES.coding__display, domain=None, range=Optional[Union[str, Literal]])

slots.coding__system = Slot(uri=TYPES.system, name="coding__system", curie=TYPES.curie('system'),
                      model_uri=TYPES.coding__system, domain=None, range=Optional[Union[str, Url]])

slots.coding__version = Slot(uri=TYPES.version, name="coding__version", curie=TYPES.curie('version'),
                      model_uri=TYPES.coding__version, domain=None, range=Optional[Union[str, Literal]])
