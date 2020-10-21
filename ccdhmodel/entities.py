# Auto generated from entities.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-10-20 19:52
# Schema: CCDH
#
# id: https://ccdh.org/model/MVPv0
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
from datatypes import Coding, Identifier, Literal, Quantity
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ADM = CurieNamespace('ADM', 'https://ccdh.org/models/ADM/')
FHIR = CurieNamespace('FHIR', 'http://hl7.org/fhir/')
GDC = CurieNamespace('GDC', 'http://fill.me.in/GDC')
HTAN = CurieNamespace('HTAN', 'http://fill.me.in/ICDC')
ICDC = CurieNamespace('ICDC', 'http://fill.me.in/ICDC')
PDC = CurieNamespace('PDC', 'http://fill.me.in/PDC')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CCDH = CurieNamespace('ccdh', 'https://ccdh.example.org/ccdh/')
DEFAULT_ = CCDH


# Types

# Class references
class EntityId(extended_str):
    pass


class SpecimenId(Literal):
    pass


class PatientId(EntityId):
    pass


class ResearchSubjectId(Literal):
    pass


class ProjectId(Literal):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Entity
    class_class_curie: ClassVar[str] = "ccdh:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CCDH.Entity

    id: Union[str, EntityId]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Specimen(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Specimen
    class_class_curie: ClassVar[str] = "ccdh:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CCDH.Specimen

    id: Union[str, SpecimenId] = None
    associated_project: Optional[Union[dict, "Project"]] = None
    identifier: List[Union[dict, Identifier]] = empty_list()
    specimen_type: Optional[Union[dict, Coding]] = None
    analyte_type: Optional[Union[dict, Coding]] = None
    derived_from_specimen: Dict[Union[str, SpecimenId], Union[dict, "Specimen"]] = empty_dict()
    derived_from_subject: Optional[Union[dict, "Patient"]] = None
    source_material_type: Optional[Union[dict, Coding]] = None
    cellular_composition: Optional[Union[dict, Coding]] = None
    general_tissue_morphology: Optional[Union[dict, Coding]] = None
    specific_tissue_morphology: Optional[Union[dict, Coding]] = None
    current_weight: List[Union[dict, Quantity]] = empty_list()
    current_volume: List[Union[dict, Quantity]] = empty_list()
    analyte_concentration: Optional[Union[dict, Quantity]] = None
    analyte_concentration_method: Optional[Union[dict, Coding]] = None
    matched_normal_flag: List[Union[dict, Coding]] = empty_list()
    qualification_status_flag: Optional[Union[dict, Coding]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SpecimenId):
            self.id = SpecimenId(self.id)
        if self.associated_project is not None and not isinstance(self.associated_project, Project):
            self.associated_project = Project(self.associated_project)
        self.identifier = [Identifier(*e) for e in self.identifier.items()] if isinstance(self.identifier, dict) \
                           else [v if isinstance(v, Identifier) else Identifier(**v)
                                 for v in ([self.identifier] if isinstance(self.identifier, str) else self.identifier)]
        if self.specimen_type is not None and not isinstance(self.specimen_type, Coding):
            self.specimen_type = Coding(**self.specimen_type)
        if self.analyte_type is not None and not isinstance(self.analyte_type, Coding):
            self.analyte_type = Coding(**self.analyte_type)
        for k, v in self.derived_from_specimen.items():
            if not isinstance(v, Specimen):
                self.derived_from_specimen[k] = Specimen(id=k, **({} if v is None else v))
        if self.derived_from_subject is not None and not isinstance(self.derived_from_subject, Patient):
            self.derived_from_subject = Patient(self.derived_from_subject)
        if self.source_material_type is not None and not isinstance(self.source_material_type, Coding):
            self.source_material_type = Coding(**self.source_material_type)
        if self.cellular_composition is not None and not isinstance(self.cellular_composition, Coding):
            self.cellular_composition = Coding(**self.cellular_composition)
        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, Coding):
            self.general_tissue_morphology = Coding(**self.general_tissue_morphology)
        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, Coding):
            self.specific_tissue_morphology = Coding(**self.specific_tissue_morphology)
        self.current_weight = [Quantity(*e) for e in self.current_weight.items()] if isinstance(self.current_weight, dict) \
                               else [v if isinstance(v, Quantity) else Quantity(**v)
                                     for v in ([self.current_weight] if isinstance(self.current_weight, str) else self.current_weight)]
        self.current_volume = [Quantity(*e) for e in self.current_volume.items()] if isinstance(self.current_volume, dict) \
                               else [v if isinstance(v, Quantity) else Quantity(**v)
                                     for v in ([self.current_volume] if isinstance(self.current_volume, str) else self.current_volume)]
        if self.analyte_concentration is not None and not isinstance(self.analyte_concentration, Quantity):
            self.analyte_concentration = Quantity(**self.analyte_concentration)
        if self.analyte_concentration_method is not None and not isinstance(self.analyte_concentration_method, Coding):
            self.analyte_concentration_method = Coding(**self.analyte_concentration_method)
        self.matched_normal_flag = [Coding(*e) for e in self.matched_normal_flag.items()] if isinstance(self.matched_normal_flag, dict) \
                                    else [v if isinstance(v, Coding) else Coding(**v)
                                          for v in ([self.matched_normal_flag] if isinstance(self.matched_normal_flag, str) else self.matched_normal_flag)]
        if self.qualification_status_flag is not None and not isinstance(self.qualification_status_flag, Coding):
            self.qualification_status_flag = Coding(**self.qualification_status_flag)
        super().__post_init__(**kwargs)


@dataclass
class Patient(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Patient
    class_class_curie: ClassVar[str] = "ccdh:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = CCDH.Patient

    id: Union[str, PatientId] = None
    taxon: Optional[Union[dict, Coding]] = None
    associated_project: Dict[Union[str, ProjectId], Union[dict, "Project"]] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PatientId):
            self.id = PatientId(self.id)
        if self.taxon is not None and not isinstance(self.taxon, Coding):
            self.taxon = Coding(**self.taxon)
        for k, v in self.associated_project.items():
            if not isinstance(v, Project):
                self.associated_project[k] = Project(id=k, **({} if v is None else v))
        super().__post_init__(**kwargs)


@dataclass
class ResearchSubject(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ResearchSubject
    class_class_curie: ClassVar[str] = "ccdh:ResearchSubject"
    class_name: ClassVar[str] = "ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CCDH.ResearchSubject

    id: Union[str, ResearchSubjectId] = None
    identifier: List[Union[dict, Identifier]] = empty_list()
    primary_disease_type: Optional[Union[dict, Coding]] = None
    primary_disease_site: Optional[Union[dict, Coding]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ResearchSubjectId):
            self.id = ResearchSubjectId(self.id)
        self.identifier = [Identifier(*e) for e in self.identifier.items()] if isinstance(self.identifier, dict) \
                           else [v if isinstance(v, Identifier) else Identifier(**v)
                                 for v in ([self.identifier] if isinstance(self.identifier, str) else self.identifier)]
        if self.primary_disease_type is not None and not isinstance(self.primary_disease_type, Coding):
            self.primary_disease_type = Coding(**self.primary_disease_type)
        if self.primary_disease_site is not None and not isinstance(self.primary_disease_site, Coding):
            self.primary_disease_site = Coding(**self.primary_disease_site)
        super().__post_init__(**kwargs)


@dataclass
class Project(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Project
    class_class_curie: ClassVar[str] = "ccdh:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CCDH.Project

    id: Union[str, ProjectId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=CCDH.id, name="id", curie=CCDH.curie('id'),
                      model_uri=CCDH.id, domain=None, range=URIRef)

slots.associated_project = Slot(uri=CCDH.associated_project, name="associated_project", curie=CCDH.curie('associated_project'),
                      model_uri=CCDH.associated_project, domain=None, range=Optional[Union[dict, Project]], mappings = [ADM["Sample.project_id"], ADM["Sample.gdc_project_id"], ADM["Portion.project_id"], ADM["Aliquot.project_id"], ADM["Analyte.project_id"], GDC["Sample.project_id"], GDC["Portion.project_id"], GDC["Aliquot.project_id"], GDC["Analyte.project_id"], PDC["Sample.gdc_project_id"]])

slots.identifier = Slot(uri=CCDH.identifier, name="identifier", curie=CCDH.curie('identifier'),
                      model_uri=CCDH.identifier, domain=None, range=List[Union[dict, Identifier]], mappings = [ADM["Sample.sample_submitter_id"], ADM["Sample.gdc_sample_id"], ADM["Portion.submitter_id"], ADM["Analyte.analyte_submitter_id"], GDC["Sample.submitter_id"], GDC["Analyte.submitter_id"], PDC["Sample.sample_submitter_id"], PDC["Analyte.analyte_submitter_id"]])

slots.specimen_type = Slot(uri=CCDH.specimen_type, name="specimen_type", curie=CCDH.curie('specimen_type'),
                      model_uri=CCDH.specimen_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ICDC["Biospecimen.BIOSPECIMEN_TYPE"]])

slots.analyte_type = Slot(uri=CCDH.analyte_type, name="analyte_type", curie=CCDH.curie('analyte_type'),
                      model_uri=CCDH.analyte_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.analyte_type"], ADM["Aliquot.analyte_type_id"], ADM["Analyte.analyte_type"], ADM["Analyte.analyte_type_id"], GDC["Aliquot.analyte_type"], GDC["Aliquot.analyte_type_id"], GDC["Analyte.analyte_type"], GDC["Analyte.analyte_type_id"], PDC["Aliquot.analyte_type"], PDC["Aliquot.analyte_type_id"], PDC["Analyte.analyte_type"], PDC["Analyte.analyte_type_id"], ICDC["Biosepcimen.ANALYTE_TYPE"]])

slots.derived_from_specimen = Slot(uri=CCDH.derived_from_specimen, name="derived_from_specimen", curie=CCDH.curie('derived_from_specimen'),
                      model_uri=CCDH.derived_from_specimen, domain=None, range=Dict[Union[str, SpecimenId], Union[dict, Specimen]], mappings = [ADM["Sample.derived_from_sample"], ADM["Portion.derived_from"], ADM["Aliquot.derived_from_analyte"], ADM["Aliquot.derived_from_sample"], ADM["Analyte.derived_from_portion"], ADM["Analyte.derived_from_sample"], GDC["Sample.derived_from"], GDC["Aliquot.derived_from"], GDC["Aliquot.derived_from"], GDC["Analyte.derived_from"], GDC["Analyte.derived_from"], GDC["Portion.derived_from"], PDC["Aliquot.Sample"], PDC["Analyte.Portion"], PDC["Analyte.Sample"], PDC["Portion.Sample"], ICDC["Biospecimen.HTAN_PARENT_ID"]])

slots.derived_from_subject = Slot(uri=CCDH.derived_from_subject, name="derived_from_subject", curie=CCDH.curie('derived_from_subject'),
                      model_uri=CCDH.derived_from_subject, domain=None, range=Optional[Union[dict, Patient]], mappings = [ADM["Sample.derived_from_case"], PDC["Sample.Case"], GDC["Sample.derived_from"], ICDC["Sample.of_case"], ICDC["Biospecimen.HTAN_PARENT_ID"]])

slots.source_material_type = Slot(uri=CCDH.source_material_type, name="source_material_type", curie=CCDH.curie('source_material_type'),
                      model_uri=CCDH.source_material_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.sample_type"], ADM["Sample.sample_type_id"], GDC["Sample.sample_type"], GDC["Sample.sample_type_id"], PDC["Sample.sample_type"], PDC["Sample.sample_type_id"], ICDC["Sample.sample_type"], ICDC["Biospecimen.BIOSPECIMEN_TYPE"]])

slots.cellular_composition = Slot(uri=CCDH.cellular_composition, name="cellular_composition", curie=CCDH.curie('cellular_composition'),
                      model_uri=CCDH.cellular_composition, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.composition"], GDC["Sample.composition"], PDC["Sample.composition"]])

slots.general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                      model_uri=CCDH.general_tissue_morphology, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tissue_type"], GDC["Sample.tissue_type"], PDC["Sample.tissue_type"], ICDC["Sample.general_sample_pathology"]])

slots.specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                      model_uri=CCDH.specific_tissue_morphology, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tumor_code"], ADM["Sample.tumor_code_id"], ADM["Sample.preinvasive_morphology"], GDC["Sample.tumor_code"], GDC["Sample.tumor_code_id"], PDC["Sample.tumor_code"], PDC["Sample.tumor_code_id"], ICDC["Sample.specific_sample_pathology"], ICDC["Biospecimen.MORPHOLOGY_CODE"], ICDC["Biospecimen.PREINVASIVE_MORPHOLOGY"]])

slots.current_weight = Slot(uri=CCDH.current_weight, name="current_weight", curie=CCDH.curie('current_weight'),
                      model_uri=CCDH.current_weight, domain=None, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.current_weight"], ADM["Portion.weight"], ADM["Aliquot.quantity"], ADM["Aliquot.amount"], ADM["Analyte.analyte_quantity"], ADM["Analyte.amount"], GDC["Sample.current_weight"], GDC["Aliquot.amount"], GDC["Portion.weight"], GDC["Aliquot.aliquot_quantity"], GDC["Analyte.amount"], GDC["Analyte.analyte_quantity"], PDC["Sample.current_weight"], PDC["Aliquot.amount"], PDC["Portion.weight"], PDC["Aliquot.aliquot_quantity"], PDC["Analyte.amount"], PDC["Analyte.analyte_quantity"], ICDC["Biospecimen.PORTION_WEIGHT"]])

slots.current_volume = Slot(uri=CCDH.current_volume, name="current_volume", curie=CCDH.curie('current_volume'),
                      model_uri=CCDH.current_volume, domain=None, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.total_volume"], ADM["Aliquot.volume"], ADM["Analyte.analyte_volume"], ADM["Aliquot.amount"], ADM["Analyte.amount"], GDC["Aliquot.aliquot_volume"], GDC["Aliquot.amount"], GDC["Analyte.amount"], GDC["Analyte.analyte_volume"], PDC["Aliquot.aliquot_volume"], PDC["Aliquot.amount"], PDC["Analyte.amount"], PDC["Analyte.analyte_volume"], ICDC["Biospecimen.TOTAL_VOLUME"]])

slots.analyte_concentration = Slot(uri=CCDH.analyte_concentration, name="analyte_concentration", curie=CCDH.curie('analyte_concentration'),
                      model_uri=CCDH.analyte_concentration, domain=None, range=Optional[Union[dict, Quantity]], mappings = [ADM["Aliquot.concentration"], ADM["Analyte.concentration"], GDC["Aliquot.concentration"], GDC["Analyte.concentration"], PDC["Aliquot.concentration"], PDC["Analyte.concentration"]])

slots.analyte_concentration_method = Slot(uri=CCDH.analyte_concentration_method, name="analyte_concentration_method", curie=CCDH.curie('analyte_concentration_method'),
                      model_uri=CCDH.analyte_concentration_method, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Analyte.spectrophotometer_method"], GDC["Analyte.spectrophotometer_method"], PDC["Analyte.spectrophotometer_method"]])

slots.matched_normal_flag = Slot(uri=CCDH.matched_normal_flag, name="matched_normal_flag", curie=CCDH.curie('matched_normal_flag'),
                      model_uri=CCDH.matched_normal_flag, domain=None, range=List[Union[dict, Coding]], mappings = [ADM["Aliquot.no_matched_normal_targeted_sequencing"], ADM["Aliquot.no_matched_normal_wgs"], ADM["Aliquot.no_matched_normal_wxs"], GDC["Aliquot.no_matched_normal_targeted_sequencing"], GDC["Aliquot.no_matched_normal_wgs"], GDC["Aliquot.no_matched_normal_wxs"]])

slots.qualification_status_flag = Slot(uri=CCDH.qualification_status_flag, name="qualification_status_flag", curie=CCDH.curie('qualification_status_flag'),
                      model_uri=CCDH.qualification_status_flag, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.status"], PDC["Aliquot.status"]])

slots.taxon = Slot(uri=CCDH.taxon, name="taxon", curie=CCDH.curie('taxon'),
                      model_uri=CCDH.taxon, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.taxon"], PDC["Case.taxon"]])

slots.primary_disease_type = Slot(uri=CCDH.primary_disease_type, name="primary_disease_type", curie=CCDH.curie('primary_disease_type'),
                      model_uri=CCDH.primary_disease_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.disease_type"], GDC["Case.disease_type"], PDC["Case.disease_type"]])

slots.primary_disease_site = Slot(uri=CCDH.primary_disease_site, name="primary_disease_site", curie=CCDH.curie('primary_disease_site'),
                      model_uri=CCDH.primary_disease_site, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.primary_site"], GDC["Case.primary_site"], PDC["Case.primary_site"]])

slots.value = Slot(uri=CCDH.value, name="value", curie=CCDH.curie('value'),
                      model_uri=CCDH.value, domain=None, range=Optional[Union[str, Literal]])

slots.system = Slot(uri=CCDH.system, name="system", curie=CCDH.curie('system'),
                      model_uri=CCDH.system, domain=None, range=Optional[Union[str, Literal]])

slots.type = Slot(uri=CCDH.type, name="type", curie=CCDH.curie('type'),
                      model_uri=CCDH.type, domain=None, range=Optional[Union[dict, Coding]])

slots.unit = Slot(uri=CCDH.unit, name="unit", curie=CCDH.curie('unit'),
                      model_uri=CCDH.unit, domain=None, range=Optional[Union[dict, Coding]])

slots.comparator = Slot(uri=CCDH.comparator, name="comparator", curie=CCDH.curie('comparator'),
                      model_uri=CCDH.comparator, domain=None, range=Optional[Union[dict, Coding]])

slots.code = Slot(uri=CCDH.code, name="code", curie=CCDH.curie('code'),
                      model_uri=CCDH.code, domain=None, range=Optional[Union[str, Literal]])

slots.display = Slot(uri=CCDH.display, name="display", curie=CCDH.curie('display'),
                      model_uri=CCDH.display, domain=None, range=Optional[Union[str, Literal]])

slots.version = Slot(uri=CCDH.version, name="version", curie=CCDH.curie('version'),
                      model_uri=CCDH.version, domain=None, range=Optional[Union[str, Literal]])

slots.Specimen_associated_project = Slot(uri=CCDH.associated_project, name="Specimen_associated_project", curie=CCDH.curie('associated_project'),
                      model_uri=CCDH.Specimen_associated_project, domain=Specimen, range=Optional[Union[dict, "Project"]], mappings = [ADM["Sample.project_id"], ADM["Sample.gdc_project_id"], ADM["Portion.project_id"], ADM["Aliquot.project_id"], ADM["Analyte.project_id"], GDC["Sample.project_id"], GDC["Portion.project_id"], GDC["Aliquot.project_id"], GDC["Analyte.project_id"], PDC["Sample.gdc_project_id"]])

slots.Specimen_id = Slot(uri=CCDH.id, name="Specimen_id", curie=CCDH.curie('id'),
                      model_uri=CCDH.Specimen_id, domain=Specimen, range=Union[str, SpecimenId], mappings = [ADM["Sample.sample_id"], ADM["Portion.portion_id"], ADM["Aliquot.aliquot_id"], ADM["Analyte.analyte_id"], GDC["Aliquot.id"], GDC["Analyte.id"], GDC["Portion.id"], GDC["Sample.id"], PDC["Aliquot.aliquot_id"], PDC["Analyte.analyte_id"], PDC["Portion.portion_id"], PDC["Sample.sample_id"], ICDC["Sample.sample_id"], ICDC["Biospecimen.HTAN_BIOSPECIMEN_ID"], FHIR["Specimen.id"]])

slots.Specimen_identifier = Slot(uri=CCDH.identifier, name="Specimen_identifier", curie=CCDH.curie('identifier'),
                      model_uri=CCDH.Specimen_identifier, domain=Specimen, range=List[Union[dict, Identifier]], mappings = [ADM["Sample.sample_submitter_id"], ADM["Sample.gdc_sample_id"], ADM["Portion.submitter_id"], ADM["Analyte.analyte_submitter_id"], GDC["Sample.submitter_id"], GDC["Analyte.submitter_id"], PDC["Sample.sample_submitter_id"], PDC["Analyte.analyte_submitter_id"]])

slots.Specimen_specimen_type = Slot(uri=CCDH.specimen_type, name="Specimen_specimen_type", curie=CCDH.curie('specimen_type'),
                      model_uri=CCDH.Specimen_specimen_type, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ICDC["Biospecimen.BIOSPECIMEN_TYPE"]])

slots.Specimen_analyte_type = Slot(uri=CCDH.analyte_type, name="Specimen_analyte_type", curie=CCDH.curie('analyte_type'),
                      model_uri=CCDH.Specimen_analyte_type, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.analyte_type"], ADM["Aliquot.analyte_type_id"], ADM["Analyte.analyte_type"], ADM["Analyte.analyte_type_id"], GDC["Aliquot.analyte_type"], GDC["Aliquot.analyte_type_id"], GDC["Analyte.analyte_type"], GDC["Analyte.analyte_type_id"], PDC["Aliquot.analyte_type"], PDC["Aliquot.analyte_type_id"], PDC["Analyte.analyte_type"], PDC["Analyte.analyte_type_id"], ICDC["Biosepcimen.ANALYTE_TYPE"]])

slots.Specimen_derived_from_specimen = Slot(uri=CCDH.derived_from_specimen, name="Specimen_derived_from_specimen", curie=CCDH.curie('derived_from_specimen'),
                      model_uri=CCDH.Specimen_derived_from_specimen, domain=Specimen, range=Dict[Union[str, SpecimenId], Union[dict, "Specimen"]], mappings = [ADM["Sample.derived_from_sample"], ADM["Portion.derived_from"], ADM["Aliquot.derived_from_analyte"], ADM["Aliquot.derived_from_sample"], ADM["Analyte.derived_from_portion"], ADM["Analyte.derived_from_sample"], GDC["Sample.derived_from"], GDC["Aliquot.derived_from"], GDC["Aliquot.derived_from"], GDC["Analyte.derived_from"], GDC["Analyte.derived_from"], GDC["Portion.derived_from"], PDC["Aliquot.Sample"], PDC["Analyte.Portion"], PDC["Analyte.Sample"], PDC["Portion.Sample"], ICDC["Biospecimen.HTAN_PARENT_ID"]])

slots.Specimen_derived_from_subject = Slot(uri=CCDH.derived_from_subject, name="Specimen_derived_from_subject", curie=CCDH.curie('derived_from_subject'),
                      model_uri=CCDH.Specimen_derived_from_subject, domain=Specimen, range=Optional[Union[dict, "Patient"]], mappings = [ADM["Sample.derived_from_case"], PDC["Sample.Case"], GDC["Sample.derived_from"], ICDC["Sample.of_case"], ICDC["Biospecimen.HTAN_PARENT_ID"]])

slots.Specimen_source_material_type = Slot(uri=CCDH.source_material_type, name="Specimen_source_material_type", curie=CCDH.curie('source_material_type'),
                      model_uri=CCDH.Specimen_source_material_type, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.sample_type"], ADM["Sample.sample_type_id"], GDC["Sample.sample_type"], GDC["Sample.sample_type_id"], PDC["Sample.sample_type"], PDC["Sample.sample_type_id"], ICDC["Sample.sample_type"], ICDC["Biospecimen.BIOSPECIMEN_TYPE"]])

slots.Specimen_cellular_composition = Slot(uri=CCDH.cellular_composition, name="Specimen_cellular_composition", curie=CCDH.curie('cellular_composition'),
                      model_uri=CCDH.Specimen_cellular_composition, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.composition"], GDC["Sample.composition"], PDC["Sample.composition"]])

slots.Specimen_general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="Specimen_general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                      model_uri=CCDH.Specimen_general_tissue_morphology, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tissue_type"], GDC["Sample.tissue_type"], PDC["Sample.tissue_type"], ICDC["Sample.general_sample_pathology"]])

slots.Specimen_specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="Specimen_specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                      model_uri=CCDH.Specimen_specific_tissue_morphology, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tumor_code"], ADM["Sample.tumor_code_id"], ADM["Sample.preinvasive_morphology"], GDC["Sample.tumor_code"], GDC["Sample.tumor_code_id"], PDC["Sample.tumor_code"], PDC["Sample.tumor_code_id"], ICDC["Sample.specific_sample_pathology"], ICDC["Biospecimen.MORPHOLOGY_CODE"], ICDC["Biospecimen.PREINVASIVE_MORPHOLOGY"]])

slots.Specimen_current_weight = Slot(uri=CCDH.current_weight, name="Specimen_current_weight", curie=CCDH.curie('current_weight'),
                      model_uri=CCDH.Specimen_current_weight, domain=Specimen, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.current_weight"], ADM["Portion.weight"], ADM["Aliquot.quantity"], ADM["Aliquot.amount"], ADM["Analyte.analyte_quantity"], ADM["Analyte.amount"], GDC["Sample.current_weight"], GDC["Aliquot.amount"], GDC["Portion.weight"], GDC["Aliquot.aliquot_quantity"], GDC["Analyte.amount"], GDC["Analyte.analyte_quantity"], PDC["Sample.current_weight"], PDC["Aliquot.amount"], PDC["Portion.weight"], PDC["Aliquot.aliquot_quantity"], PDC["Analyte.amount"], PDC["Analyte.analyte_quantity"], ICDC["Biospecimen.PORTION_WEIGHT"]])

slots.Specimen_current_volume = Slot(uri=CCDH.current_volume, name="Specimen_current_volume", curie=CCDH.curie('current_volume'),
                      model_uri=CCDH.Specimen_current_volume, domain=Specimen, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.total_volume"], ADM["Aliquot.volume"], ADM["Analyte.analyte_volume"], ADM["Aliquot.amount"], ADM["Analyte.amount"], GDC["Aliquot.aliquot_volume"], GDC["Aliquot.amount"], GDC["Analyte.amount"], GDC["Analyte.analyte_volume"], PDC["Aliquot.aliquot_volume"], PDC["Aliquot.amount"], PDC["Analyte.amount"], PDC["Analyte.analyte_volume"], ICDC["Biospecimen.TOTAL_VOLUME"]])

slots.Specimen_analyte_concentration = Slot(uri=CCDH.analyte_concentration, name="Specimen_analyte_concentration", curie=CCDH.curie('analyte_concentration'),
                      model_uri=CCDH.Specimen_analyte_concentration, domain=Specimen, range=Optional[Union[dict, Quantity]], mappings = [ADM["Aliquot.concentration"], ADM["Analyte.concentration"], GDC["Aliquot.concentration"], GDC["Analyte.concentration"], PDC["Aliquot.concentration"], PDC["Analyte.concentration"]])

slots.Specimen_analyte_concentration_method = Slot(uri=CCDH.analyte_concentration_method, name="Specimen_analyte_concentration_method", curie=CCDH.curie('analyte_concentration_method'),
                      model_uri=CCDH.Specimen_analyte_concentration_method, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Analyte.spectrophotometer_method"], GDC["Analyte.spectrophotometer_method"], PDC["Analyte.spectrophotometer_method"]])

slots.Specimen_matched_normal_flag = Slot(uri=CCDH.matched_normal_flag, name="Specimen_matched_normal_flag", curie=CCDH.curie('matched_normal_flag'),
                      model_uri=CCDH.Specimen_matched_normal_flag, domain=Specimen, range=List[Union[dict, Coding]], mappings = [ADM["Aliquot.no_matched_normal_targeted_sequencing"], ADM["Aliquot.no_matched_normal_wgs"], ADM["Aliquot.no_matched_normal_wxs"], GDC["Aliquot.no_matched_normal_targeted_sequencing"], GDC["Aliquot.no_matched_normal_wgs"], GDC["Aliquot.no_matched_normal_wxs"]])

slots.Specimen_qualification_status_flag = Slot(uri=CCDH.qualification_status_flag, name="Specimen_qualification_status_flag", curie=CCDH.curie('qualification_status_flag'),
                      model_uri=CCDH.Specimen_qualification_status_flag, domain=Specimen, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.status"], PDC["Aliquot.status"]])

slots.Patient_taxon = Slot(uri=CCDH.taxon, name="Patient_taxon", curie=CCDH.curie('taxon'),
                      model_uri=CCDH.Patient_taxon, domain=Patient, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.taxon"], PDC["Case.taxon"]])

slots.Patient_associated_project = Slot(uri=CCDH.associated_project, name="Patient_associated_project", curie=CCDH.curie('associated_project'),
                      model_uri=CCDH.Patient_associated_project, domain=Patient, range=Dict[Union[str, ProjectId], Union[dict, "Project"]], mappings = [ADM["Case.member_of_project"], ADM["Case.project_id"], GDC["Case.member_of"], GDC["Case.project_id"], PDC["Case.Project"]])

slots.ResearchSubject_id = Slot(uri=CCDH.id, name="ResearchSubject_id", curie=CCDH.curie('id'),
                      model_uri=CCDH.ResearchSubject_id, domain=ResearchSubject, range=Union[str, ResearchSubjectId], mappings = [ADM["Case.case_id"], FHIR["ResearchSubject.id"]])

slots.ResearchSubject_identifier = Slot(uri=CCDH.identifier, name="ResearchSubject_identifier", curie=CCDH.curie('identifier'),
                      model_uri=CCDH.ResearchSubject_identifier, domain=ResearchSubject, range=List[Union[dict, Identifier]], mappings = [ADM["Case.external_case_id"], ADM["Case.case_submitter_id"], GDC["Case.id"], GDC["Case.submitter_id"], PDC["Case.external_case_id"], PDC["Case.case_submitter_id"]])

slots.ResearchSubject_primary_disease_type = Slot(uri=CCDH.primary_disease_type, name="ResearchSubject_primary_disease_type", curie=CCDH.curie('primary_disease_type'),
                      model_uri=CCDH.ResearchSubject_primary_disease_type, domain=ResearchSubject, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.disease_type"], GDC["Case.disease_type"], PDC["Case.disease_type"]])

slots.ResearchSubject_primary_disease_site = Slot(uri=CCDH.primary_disease_site, name="ResearchSubject_primary_disease_site", curie=CCDH.curie('primary_disease_site'),
                      model_uri=CCDH.ResearchSubject_primary_disease_site, domain=ResearchSubject, range=Optional[Union[dict, Coding]], mappings = [ADM["Case.primary_site"], GDC["Case.primary_site"], PDC["Case.primary_site"]])

slots.Project_id = Slot(uri=CCDH.id, name="Project_id", curie=CCDH.curie('id'),
                      model_uri=CCDH.Project_id, domain=Project, range=Union[str, ProjectId], mappings = [ADM["Project.project_id"], GDC["Project.id"], PDC["Project.project_id"]])
