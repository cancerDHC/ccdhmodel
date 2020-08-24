# Auto generated from specimen.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-24 13:05
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
from datatypes import Coding, Identifier, Literal
from entities import Entity, Id, Organization, PatientOrBiologicallyDerivedMaterial, Project
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ADM = CurieNamespace('ADM', 'https://ccdh.org/models/ADM/')
FHIR = CurieNamespace('FHIR', 'http://hl7.org/fhir/')
GDC = CurieNamespace('GDC', 'http://fill.me.in/GDC')
ICDC = CurieNamespace('ICDC', 'http://fill.me.in/ICDC')
PDC = CurieNamespace('PDC', 'http://fill.me.in/PDC')
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
    identifier: List[Union[dict, Identifier]] = empty_list()
    description: Optional[Union[str, Literal]] = None
    specimen_type: List[Union[dict, Coding]] = empty_list()
    analyte_type: Optional[Union[dict, Coding]] = None
    associated_project: Optional[Union[dict, Project]] = None
    provided_by: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[dict, Coding]] = None
    derived_from_specimen: Dict[Union[str, SpecimenId], Union[dict, "Specimen"]] = empty_dict()
    derived_from_subject: Optional[Union[dict, PatientOrBiologicallyDerivedMaterial]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SpecimenId):
            self.id = SpecimenId(self.id)
        self.identifier = [Identifier(*e) for e in self.identifier.items()] if isinstance(self.identifier, dict) \
                           else [v if isinstance(v, Identifier) else Identifier(**v)
                                 for v in ([self.identifier] if isinstance(self.identifier, str) else self.identifier)]
        if self.description is not None and not isinstance(self.description, Literal):
            self.description = Literal(self.description)
        self.specimen_type = [Coding(*e) for e in self.specimen_type.items()] if isinstance(self.specimen_type, dict) \
                              else [v if isinstance(v, Coding) else Coding(**v)
                                    for v in ([self.specimen_type] if isinstance(self.specimen_type, str) else self.specimen_type)]
        if self.analyte_type is not None and not isinstance(self.analyte_type, Coding):
            self.analyte_type = Coding()
        if self.associated_project is not None and not isinstance(self.associated_project, Project):
            self.associated_project = Project(**self.associated_project)
        if self.provided_by is not None and not isinstance(self.provided_by, Organization):
            self.provided_by = Organization(**self.provided_by)
        if self.source_material_type is not None and not isinstance(self.source_material_type, Coding):
            self.source_material_type = Coding()
        for k, v in self.derived_from_specimen.items():
            if not isinstance(v, Specimen):
                self.derived_from_specimen[k] = Specimen(id=k, **({} if v is None else v))
        if self.derived_from_subject is not None and not isinstance(self.derived_from_subject, PatientOrBiologicallyDerivedMaterial):
            self.derived_from_subject = PatientOrBiologicallyDerivedMaterial()
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.identifier = Slot(uri=SPECIMEN.identifier, name="identifier", curie=SPECIMEN.curie('identifier'),
                      model_uri=SPECIMEN.identifier, domain=None, range=List[Union[dict, Identifier]], mappings = [ADM["Sample.sample_submitter_id"], ADM["Sample.gdc_sample_id"], ADM["Portion.submitter_id"], ADM["Analyte.analyte_submitter_id"], GDC["Sample.submitter_id"], GDC["Analyte.submitter_id"], PDC["Sample.sample_submitter_id"], PDC["Analyte.analyte_submitter_id"], FHIR["Specimen.identifier"]])

slots.description = Slot(uri=SPECIMEN.description, name="description", curie=SPECIMEN.curie('description'),
                      model_uri=SPECIMEN.description, domain=None, range=Optional[Union[str, Literal]], mappings = [ADM["Sample.comment"], ICDC["Sample.comment"], FHIR["specimen.note"]])

slots.specimen_type = Slot(uri=SPECIMEN.specimen_type, name="specimen_type", curie=SPECIMEN.curie('specimen_type'),
                      model_uri=SPECIMEN.specimen_type, domain=None, range=List[Union[dict, Coding]])

slots.analyte_type = Slot(uri=SPECIMEN.analyte_type, name="analyte_type", curie=SPECIMEN.curie('analyte_type'),
                      model_uri=SPECIMEN.analyte_type, domain=None, range=Optional[Union[dict, Coding]])

slots.associated_project = Slot(uri=SPECIMEN.associated_project, name="associated_project", curie=SPECIMEN.curie('associated_project'),
                      model_uri=SPECIMEN.associated_project, domain=None, range=Optional[Union[dict, Project]])

slots.provided_by = Slot(uri=SPECIMEN.provided_by, name="provided_by", curie=SPECIMEN.curie('provided_by'),
                      model_uri=SPECIMEN.provided_by, domain=None, range=Optional[Union[dict, Organization]])

slots.source_material_type = Slot(uri=SPECIMEN.source_material_type, name="source_material_type", curie=SPECIMEN.curie('source_material_type'),
                      model_uri=SPECIMEN.source_material_type, domain=None, range=Optional[Union[dict, Coding]])

slots.derived_from_specimen = Slot(uri=SPECIMEN.derived_from_specimen, name="derived_from_specimen", curie=SPECIMEN.curie('derived_from_specimen'),
                      model_uri=SPECIMEN.derived_from_specimen, domain=None, range=Dict[Union[str, SpecimenId], Union[dict, Specimen]])

slots.derived_from_subject = Slot(uri=SPECIMEN.derived_from_subject, name="derived_from_subject", curie=SPECIMEN.curie('derived_from_subject'),
                      model_uri=SPECIMEN.derived_from_subject, domain=None, range=Optional[Union[dict, PatientOrBiologicallyDerivedMaterial]])

slots.Specimen_id = Slot(uri=SPECIMEN.id, name="Specimen_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Specimen_id, domain=Specimen, range=Union[str, SpecimenId])

slots.Specimen_identifier = Slot(uri=SPECIMEN.identifier, name="Specimen_identifier", curie=SPECIMEN.curie('identifier'),
                      model_uri=SPECIMEN.Specimen_identifier, domain=Specimen, range=List[Union[dict, Identifier]])

slots.Specimen_description = Slot(uri=SPECIMEN.description, name="Specimen_description", curie=SPECIMEN.curie('description'),
                      model_uri=SPECIMEN.Specimen_description, domain=Specimen, range=Optional[Union[str, Literal]])

slots.Specimen_specimen_type = Slot(uri=SPECIMEN.specimen_type, name="Specimen_specimen_type", curie=SPECIMEN.curie('specimen_type'),
                      model_uri=SPECIMEN.Specimen_specimen_type, domain=Specimen, range=List[Union[dict, Coding]])

slots.Specimen_analyte_type = Slot(uri=SPECIMEN.analyte_type, name="Specimen_analyte_type", curie=SPECIMEN.curie('analyte_type'),
                      model_uri=SPECIMEN.Specimen_analyte_type, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_associated_project = Slot(uri=SPECIMEN.associated_project, name="Specimen_associated_project", curie=SPECIMEN.curie('associated_project'),
                      model_uri=SPECIMEN.Specimen_associated_project, domain=Specimen, range=Optional[Union[dict, Project]])

slots.Specimen_provided_by = Slot(uri=SPECIMEN.provided_by, name="Specimen_provided_by", curie=SPECIMEN.curie('provided_by'),
                      model_uri=SPECIMEN.Specimen_provided_by, domain=Specimen, range=Optional[Union[dict, Organization]])

slots.Specimen_source_material_type = Slot(uri=SPECIMEN.source_material_type, name="Specimen_source_material_type", curie=SPECIMEN.curie('source_material_type'),
                      model_uri=SPECIMEN.Specimen_source_material_type, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_derived_from_specimen = Slot(uri=SPECIMEN.derived_from_specimen, name="Specimen_derived_from_specimen", curie=SPECIMEN.curie('derived_from_specimen'),
                      model_uri=SPECIMEN.Specimen_derived_from_specimen, domain=Specimen, range=Dict[Union[str, SpecimenId], Union[dict, "Specimen"]])

slots.Specimen_derived_from_subject = Slot(uri=SPECIMEN.derived_from_subject, name="Specimen_derived_from_subject", curie=SPECIMEN.curie('derived_from_subject'),
                      model_uri=SPECIMEN.Specimen_derived_from_subject, domain=Specimen, range=Optional[Union[dict, PatientOrBiologicallyDerivedMaterial]])
