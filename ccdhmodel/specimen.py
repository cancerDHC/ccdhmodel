# Auto generated from specimen.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-19 10:25
# Schema: specimen
#
# id: https://ccdh.org/model/specimen
# description: Any material sample taken from a biological entity (living or dead), or taken from a physical
#              object or the environment. (Adapted from FHIR) Specimens are usually collected as an example of
#              their kind, often for use in some investigation.
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
from datatypes import Literal
from entities import Entity, Id, Organization
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
SPECIMEN = CurieNamespace('specimen', 'https://ccdh.org/specimen/')
DEFAULT_ = SPECIMEN


# Types

# Class references
class SpecimenId(Literal):
    pass


@dataclass
class Specimen(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPECIMEN.Specimen
    class_class_curie: ClassVar[str] = "specimen:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = SPECIMEN.Specimen

    id: Union[str, SpecimenId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SpecimenId):
            self.id = SpecimenId(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.Specimen_id = Slot(uri=SPECIMEN.id, name="Specimen_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Specimen_id, domain=Specimen, range=Union[str, SpecimenId])

slots.Organization_id = Slot(uri=SPECIMEN.id, name="Organization_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Organization_id, domain=Organization, range=Union[str, OrganizationId])
