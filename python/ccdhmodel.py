# Auto generated from ccdhmodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-11 18:19
# Schema: CRDC-H
#
# id: https://example.org/ccdh
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CCDH = CurieNamespace('ccdh', 'https://example.org/ccdh/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CCDH


# Types

# Class references



@dataclass
class CDM.Specimen(YAMLRoot):
    """
    Any material taken as a sample from a biological entity (living or dead), or from a physical object or the
    environment. Specimens are usually collected as an example of their kind, often for use in some investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.Specimen"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.Specimen"
    class_name: ClassVar[str] = "CDM.Specimen"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.Specimen

    id: Optional[str] = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    specimen_type: Optional[str] = None
    analyte_type: Optional[str] = None
    associated_project: Optional[str] = None
    provided_by: Optional[str] = None
    source_material_type: Optional[str] = None
    parent_specimen: Optional[Union[str, List[str]]] = empty_list()
    source_patient: Optional[str] = None
    source_model_system: Optional[str] = None
    condition_status_at_collection: Optional[str] = None
    related_diagnosis: Optional[Union[str, List[str]]] = empty_list()
    creation_activity: Optional[str] = None
    processing_activity: Optional[Union[str, List[str]]] = empty_list()
    storage_activity: Optional[str] = None
    transport_activity: Optional[str] = None
    contained_in: Optional[str] = None
    dimensional_measure: Optional[str] = None
    quantity_measure: Optional[Union[str, List[str]]] = empty_list()
    quality_measure: Optional[Union[str, List[str]]] = empty_list()
    cellular_composition_type: Optional[str] = None
    cellular_composition_measure: Optional[Union[str, List[str]]] = empty_list()
    tissue_composition_measure: Optional[Union[str, List[str]]] = empty_list()
    general_tissue_morphology: Optional[str] = None
    specific_tissue_morphology: Optional[str] = None
    morphology_pathologically_confirmed: Optional[str] = None
    related_document: Optional[Union[str, List[str]]] = empty_list()
    related_specimen: Optional[Union[str, List[str]]] = empty_list()
    derived_product: Optional[Union[str, List[str]]] = empty_list()
    qualification_status_flag: Optional[str] = None
    reference_status_flag: Optional[str] = None
    matched_normal_flag: Optional[Union[str, List[str]]] = empty_list()
    selected_normal_flag: Optional[str] = None
    paired_specimen_genotype_match_flag: Optional[str] = None
    section_location: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.specimen_type is not None and not isinstance(self.specimen_type, str):
            self.specimen_type = str(self.specimen_type)

        if self.analyte_type is not None and not isinstance(self.analyte_type, str):
            self.analyte_type = str(self.analyte_type)

        if self.associated_project is not None and not isinstance(self.associated_project, str):
            self.associated_project = str(self.associated_project)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        if self.source_material_type is not None and not isinstance(self.source_material_type, str):
            self.source_material_type = str(self.source_material_type)

        if self.parent_specimen is None:
            self.parent_specimen = []
        if not isinstance(self.parent_specimen, list):
            self.parent_specimen = [self.parent_specimen]
        self.parent_specimen = [v if isinstance(v, str) else str(v) for v in self.parent_specimen]

        if self.source_patient is not None and not isinstance(self.source_patient, str):
            self.source_patient = str(self.source_patient)

        if self.source_model_system is not None and not isinstance(self.source_model_system, str):
            self.source_model_system = str(self.source_model_system)

        if self.condition_status_at_collection is not None and not isinstance(self.condition_status_at_collection, str):
            self.condition_status_at_collection = str(self.condition_status_at_collection)

        if self.related_diagnosis is None:
            self.related_diagnosis = []
        if not isinstance(self.related_diagnosis, list):
            self.related_diagnosis = [self.related_diagnosis]
        self.related_diagnosis = [v if isinstance(v, str) else str(v) for v in self.related_diagnosis]

        if self.creation_activity is not None and not isinstance(self.creation_activity, str):
            self.creation_activity = str(self.creation_activity)

        if self.processing_activity is None:
            self.processing_activity = []
        if not isinstance(self.processing_activity, list):
            self.processing_activity = [self.processing_activity]
        self.processing_activity = [v if isinstance(v, str) else str(v) for v in self.processing_activity]

        if self.storage_activity is not None and not isinstance(self.storage_activity, str):
            self.storage_activity = str(self.storage_activity)

        if self.transport_activity is not None and not isinstance(self.transport_activity, str):
            self.transport_activity = str(self.transport_activity)

        if self.contained_in is not None and not isinstance(self.contained_in, str):
            self.contained_in = str(self.contained_in)

        if self.dimensional_measure is not None and not isinstance(self.dimensional_measure, str):
            self.dimensional_measure = str(self.dimensional_measure)

        if self.quantity_measure is None:
            self.quantity_measure = []
        if not isinstance(self.quantity_measure, list):
            self.quantity_measure = [self.quantity_measure]
        self.quantity_measure = [v if isinstance(v, str) else str(v) for v in self.quantity_measure]

        if self.quality_measure is None:
            self.quality_measure = []
        if not isinstance(self.quality_measure, list):
            self.quality_measure = [self.quality_measure]
        self.quality_measure = [v if isinstance(v, str) else str(v) for v in self.quality_measure]

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, str):
            self.cellular_composition_type = str(self.cellular_composition_type)

        if self.cellular_composition_measure is None:
            self.cellular_composition_measure = []
        if not isinstance(self.cellular_composition_measure, list):
            self.cellular_composition_measure = [self.cellular_composition_measure]
        self.cellular_composition_measure = [v if isinstance(v, str) else str(v) for v in self.cellular_composition_measure]

        if self.tissue_composition_measure is None:
            self.tissue_composition_measure = []
        if not isinstance(self.tissue_composition_measure, list):
            self.tissue_composition_measure = [self.tissue_composition_measure]
        self.tissue_composition_measure = [v if isinstance(v, str) else str(v) for v in self.tissue_composition_measure]

        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, str):
            self.general_tissue_morphology = str(self.general_tissue_morphology)

        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, str):
            self.specific_tissue_morphology = str(self.specific_tissue_morphology)

        if self.morphology_pathologically_confirmed is not None and not isinstance(self.morphology_pathologically_confirmed, str):
            self.morphology_pathologically_confirmed = str(self.morphology_pathologically_confirmed)

        if self.related_document is None:
            self.related_document = []
        if not isinstance(self.related_document, list):
            self.related_document = [self.related_document]
        self.related_document = [v if isinstance(v, str) else str(v) for v in self.related_document]

        if self.related_specimen is None:
            self.related_specimen = []
        if not isinstance(self.related_specimen, list):
            self.related_specimen = [self.related_specimen]
        self.related_specimen = [v if isinstance(v, str) else str(v) for v in self.related_specimen]

        if self.derived_product is None:
            self.derived_product = []
        if not isinstance(self.derived_product, list):
            self.derived_product = [self.derived_product]
        self.derived_product = [v if isinstance(v, str) else str(v) for v in self.derived_product]

        if self.qualification_status_flag is not None and not isinstance(self.qualification_status_flag, str):
            self.qualification_status_flag = str(self.qualification_status_flag)

        if self.reference_status_flag is not None and not isinstance(self.reference_status_flag, str):
            self.reference_status_flag = str(self.reference_status_flag)

        if self.matched_normal_flag is None:
            self.matched_normal_flag = []
        if not isinstance(self.matched_normal_flag, list):
            self.matched_normal_flag = [self.matched_normal_flag]
        self.matched_normal_flag = [v if isinstance(v, str) else str(v) for v in self.matched_normal_flag]

        if self.selected_normal_flag is not None and not isinstance(self.selected_normal_flag, str):
            self.selected_normal_flag = str(self.selected_normal_flag)

        if self.paired_specimen_genotype_match_flag is not None and not isinstance(self.paired_specimen_genotype_match_flag, str):
            self.paired_specimen_genotype_match_flag = str(self.paired_specimen_genotype_match_flag)

        if self.section_location is not None and not isinstance(self.section_location, str):
            self.section_location = str(self.section_location)

        super().__post_init__(**kwargs)


@dataclass
class CDM.Report(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.Report"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.Report"
    class_name: ClassVar[str] = "CDM.Report"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.Report

    id: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            self.id = []
        if not isinstance(self.id, list):
            self.id = [self.id]
        self.id = [v if isinstance(v, str) else str(v) for v in self.id]

        super().__post_init__(**kwargs)


@dataclass
class CDM.SpecimenCreationActivity(YAMLRoot):
    """
    The process of creating a specimen through observing and/or removing material from an biological source or natural
    setting (e.g. from a person, animal, cell line, or environmental material), or through derivation from an existing
    specimen (e.g. through portioning or aliquoting). This activity represents the entire process up to the point
    where the specimen is physically modified, stored, or transported.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.SpecimenCreationActivity"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.SpecimenCreationActivity"
    class_name: ClassVar[str] = "CDM.SpecimenCreationActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.SpecimenCreationActivity

    id: Optional[str] = None
    activity_type: Optional[str] = None
    date_started: Optional[str] = None
    date_ended: Optional[str] = None
    performed_by: Optional[str] = None
    method_type: Optional[str] = None
    collection_site: Optional[str] = None
    input_specimen: Optional[Union[str, List[str]]] = empty_list()
    quantity_collected: Optional[str] = None
    execution_condition: Optional[Union[str, List[str]]] = empty_list()
    collected_during_visit: Optional[str] = None
    relative_timing: Optional[Union[str, List[str]]] = empty_list()
    relative_order: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.activity_type is not None and not isinstance(self.activity_type, str):
            self.activity_type = str(self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, str):
            self.date_started = str(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, str):
            self.date_ended = str(self.date_ended)

        if self.performed_by is not None and not isinstance(self.performed_by, str):
            self.performed_by = str(self.performed_by)

        if self.method_type is not None and not isinstance(self.method_type, str):
            self.method_type = str(self.method_type)

        if self.collection_site is not None and not isinstance(self.collection_site, str):
            self.collection_site = str(self.collection_site)

        if self.input_specimen is None:
            self.input_specimen = []
        if not isinstance(self.input_specimen, list):
            self.input_specimen = [self.input_specimen]
        self.input_specimen = [v if isinstance(v, str) else str(v) for v in self.input_specimen]

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, str):
            self.quantity_collected = str(self.quantity_collected)

        if self.execution_condition is None:
            self.execution_condition = []
        if not isinstance(self.execution_condition, list):
            self.execution_condition = [self.execution_condition]
        self.execution_condition = [v if isinstance(v, str) else str(v) for v in self.execution_condition]

        if self.collected_during_visit is not None and not isinstance(self.collected_during_visit, str):
            self.collected_during_visit = str(self.collected_during_visit)

        if self.relative_timing is None:
            self.relative_timing = []
        if not isinstance(self.relative_timing, list):
            self.relative_timing = [self.relative_timing]
        self.relative_timing = [v if isinstance(v, str) else str(v) for v in self.relative_timing]

        if self.relative_order is not None and not isinstance(self.relative_order, str):
            self.relative_order = str(self.relative_order)

        super().__post_init__(**kwargs)


@dataclass
class CDM.SpecimenProcessingActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.SpecimenProcessingActivity"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.SpecimenProcessingActivity"
    class_name: ClassVar[str] = "CDM.SpecimenProcessingActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.SpecimenProcessingActivity

    duration: Optional[Union[str, List[str]]] = empty_list()
    performed_by: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.duration is None:
            self.duration = []
        if not isinstance(self.duration, list):
            self.duration = [self.duration]
        self.duration = [v if isinstance(v, str) else str(v) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, str):
            self.performed_by = str(self.performed_by)

        super().__post_init__(**kwargs)


@dataclass
class CDM.SpecimenStorageActivity(YAMLRoot):
    """
    A vessel in which a specimen is held or attached - to store or as a substrate for growth (e.g. a cell culture
    dish) or analysis (e.g. a microscope slide or 96-well plate)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.SpecimenStorageActivity"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.SpecimenStorageActivity"
    class_name: ClassVar[str] = "CDM.SpecimenStorageActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.SpecimenStorageActivity

    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CDM.SpecimenTransportActivity(YAMLRoot):
    """
    An activity through which a specimen is transported between locations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.SpecimenTransportActivity"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.SpecimenTransportActivity"
    class_name: ClassVar[str] = "CDM.SpecimenTransportActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.SpecimenTransportActivity

    id: Optional[str] = None
    date_started: Optional[str] = None
    date_ended: Optional[str] = None
    transport_destination: Optional[str] = None
    execution_conditions: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.date_started is not None and not isinstance(self.date_started, str):
            self.date_started = str(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, str):
            self.date_ended = str(self.date_ended)

        if self.transport_destination is not None and not isinstance(self.transport_destination, str):
            self.transport_destination = str(self.transport_destination)

        if self.execution_conditions is None:
            self.execution_conditions = []
        if not isinstance(self.execution_conditions, list):
            self.execution_conditions = [self.execution_conditions]
        self.execution_conditions = [v if isinstance(v, str) else str(v) for v in self.execution_conditions]

        super().__post_init__(**kwargs)


@dataclass
class CDM.SpecimenContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.SpecimenContainer"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.SpecimenContainer"
    class_name: ClassVar[str] = "CDM.SpecimenContainer"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.SpecimenContainer

    container_type: Optional[Union[str, List[str]]] = empty_list()
    container_number: Optional[Union[str, List[str]]] = empty_list()
    additive: Optional[Union[str, List[str]]] = empty_list()
    parent_container: Optional[Union[str, List[str]]] = empty_list()
    charge_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.container_type is None:
            self.container_type = []
        if not isinstance(self.container_type, list):
            self.container_type = [self.container_type]
        self.container_type = [v if isinstance(v, str) else str(v) for v in self.container_type]

        if self.container_number is None:
            self.container_number = []
        if not isinstance(self.container_number, list):
            self.container_number = [self.container_number]
        self.container_number = [v if isinstance(v, str) else str(v) for v in self.container_number]

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, str) else str(v) for v in self.additive]

        if self.parent_container is None:
            self.parent_container = []
        if not isinstance(self.parent_container, list):
            self.parent_container = [self.parent_container]
        self.parent_container = [v if isinstance(v, str) else str(v) for v in self.parent_container]

        if self.charge_type is not None and not isinstance(self.charge_type, str):
            self.charge_type = str(self.charge_type)

        super().__post_init__(**kwargs)


@dataclass
class CDM.BiologicallyDerivedProduct(YAMLRoot):
    """
    A living organism, or a metabolocally active biological system such as a cell culture, tissue culture, or organoid
    that is maintained or propagated in vitro.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.BiologicallyDerivedProduct"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.BiologicallyDerivedProduct"
    class_name: ClassVar[str] = "CDM.BiologicallyDerivedProduct"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.BiologicallyDerivedProduct

    id: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    passage_number: Optional[Union[str, List[str]]] = empty_list()
    growth_rate: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.passage_number is None:
            self.passage_number = []
        if not isinstance(self.passage_number, list):
            self.passage_number = [self.passage_number]
        self.passage_number = [v if isinstance(v, str) else str(v) for v in self.passage_number]

        if self.growth_rate is None:
            self.growth_rate = []
        if not isinstance(self.growth_rate, list):
            self.growth_rate = [self.growth_rate]
        self.growth_rate = [v if isinstance(v, str) else str(v) for v in self.growth_rate]

        super().__post_init__(**kwargs)


@dataclass
class CDM.Patient(YAMLRoot):
    """
    Demographics and other administrative information about an individual or animal receiving care or other
    health-related services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.Patient"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.Patient"
    class_name: ClassVar[str] = "CDM.Patient"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.Patient

    id: str = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    given_name: Optional[str] = None
    taxon: Optional[str] = None
    adverse_events: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.given_name is not None and not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.adverse_events is None:
            self.adverse_events = []
        if not isinstance(self.adverse_events, list):
            self.adverse_events = [self.adverse_events]
        self.adverse_events = [v if isinstance(v, str) else str(v) for v in self.adverse_events]

        super().__post_init__(**kwargs)


@dataclass
class CDM.ResearchSubject(YAMLRoot):
    """
    A research subject is the entity of interest in a research study, typically a human being or an animal, but can
    also be a device, group of humans or animals,
    or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the
    subject’s privacy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.ResearchSubject"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.ResearchSubject"
    class_name: ClassVar[str] = "CDM.ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.ResearchSubject

    id: str = None
    associated_patient: str = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    primary_disease_type: Optional[str] = None
    primary_disease_site: Optional[str] = None
    qualification_status_flag: Optional[str] = None
    associated_project: Optional[Union[str, List[str]]] = empty_list()
    member_of_cohort: Optional[Union[str, List[str]]] = empty_list()
    member_of_study: Optional[Union[str, List[str]]] = empty_list()
    index_timepoint: Optional[str] = None
    reference_status_flag: Optional[str] = None
    processed_at: Optional[str] = None
    originating_site: Optional[str] = None
    study_progress: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.associated_patient is None:
            raise ValueError("associated_patient must be supplied")
        if not isinstance(self.associated_patient, str):
            self.associated_patient = str(self.associated_patient)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.primary_disease_type is not None and not isinstance(self.primary_disease_type, str):
            self.primary_disease_type = str(self.primary_disease_type)

        if self.primary_disease_site is not None and not isinstance(self.primary_disease_site, str):
            self.primary_disease_site = str(self.primary_disease_site)

        if self.qualification_status_flag is not None and not isinstance(self.qualification_status_flag, str):
            self.qualification_status_flag = str(self.qualification_status_flag)

        if self.associated_project is None:
            self.associated_project = []
        if not isinstance(self.associated_project, list):
            self.associated_project = [self.associated_project]
        self.associated_project = [v if isinstance(v, str) else str(v) for v in self.associated_project]

        if self.member_of_cohort is None:
            self.member_of_cohort = []
        if not isinstance(self.member_of_cohort, list):
            self.member_of_cohort = [self.member_of_cohort]
        self.member_of_cohort = [v if isinstance(v, str) else str(v) for v in self.member_of_cohort]

        if self.member_of_study is None:
            self.member_of_study = []
        if not isinstance(self.member_of_study, list):
            self.member_of_study = [self.member_of_study]
        self.member_of_study = [v if isinstance(v, str) else str(v) for v in self.member_of_study]

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, str):
            self.index_timepoint = str(self.index_timepoint)

        if self.reference_status_flag is not None and not isinstance(self.reference_status_flag, str):
            self.reference_status_flag = str(self.reference_status_flag)

        if self.processed_at is not None and not isinstance(self.processed_at, str):
            self.processed_at = str(self.processed_at)

        if self.originating_site is not None and not isinstance(self.originating_site, str):
            self.originating_site = str(self.originating_site)

        if self.study_progress is None:
            self.study_progress = []
        if not isinstance(self.study_progress, list):
            self.study_progress = [self.study_progress]
        self.study_progress = [v if isinstance(v, str) else str(v) for v in self.study_progress]

        super().__post_init__(**kwargs)


@dataclass
class CDM.ResearchProject(YAMLRoot):
    """
    A process where a researcher or organization plans and then executes a series of steps intended to increase the
    field of healthcare-related knowledge.
    This includes studies of safety, efficacy, comparative effectiveness and other information about medications,
    devices, therapies and other interventional
    and investigative techniques. A ResearchProject involves the gathering of information about human or animal
    subjects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.ResearchProject"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.ResearchProject"
    class_name: ClassVar[str] = "CDM.ResearchProject"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.ResearchProject

    research_project_type: str = None
    id: Optional[str] = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[str] = None
    name_shortened: Optional[str] = None
    description: Optional[str] = None
    description_shortened: Optional[str] = None
    sponsor: Optional[Union[str, List[str]]] = empty_list()
    date_started: Optional[str] = None
    date_ended: Optional[str] = None
    primary_anatomic_site: Optional[Union[str, List[str]]] = empty_list()
    url: Optional[Union[str, List[str]]] = empty_list()
    part_of: Optional[Union[str, List[str]]] = empty_list()
    date_iacuc_approval: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.research_project_type is None:
            raise ValueError("research_project_type must be supplied")
        if not isinstance(self.research_project_type, str):
            self.research_project_type = str(self.research_project_type)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.name_shortened is not None and not isinstance(self.name_shortened, str):
            self.name_shortened = str(self.name_shortened)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.description_shortened is not None and not isinstance(self.description_shortened, str):
            self.description_shortened = str(self.description_shortened)

        if self.sponsor is None:
            self.sponsor = []
        if not isinstance(self.sponsor, list):
            self.sponsor = [self.sponsor]
        self.sponsor = [v if isinstance(v, str) else str(v) for v in self.sponsor]

        if self.date_started is not None and not isinstance(self.date_started, str):
            self.date_started = str(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, str):
            self.date_ended = str(self.date_ended)

        if self.primary_anatomic_site is None:
            self.primary_anatomic_site = []
        if not isinstance(self.primary_anatomic_site, list):
            self.primary_anatomic_site = [self.primary_anatomic_site]
        self.primary_anatomic_site = [v if isinstance(v, str) else str(v) for v in self.primary_anatomic_site]

        if self.url is None:
            self.url = []
        if not isinstance(self.url, list):
            self.url = [self.url]
        self.url = [v if isinstance(v, str) else str(v) for v in self.url]

        if self.part_of is None:
            self.part_of = []
        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of]
        self.part_of = [v if isinstance(v, str) else str(v) for v in self.part_of]

        if self.date_iacuc_approval is not None and not isinstance(self.date_iacuc_approval, str):
            self.date_iacuc_approval = str(self.date_iacuc_approval)

        super().__post_init__(**kwargs)


@dataclass
class CDM.Organization(YAMLRoot):
    """
    A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or
    an institute within a university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.Organization"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.Organization"
    class_name: ClassVar[str] = "CDM.Organization"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.Organization

    id: str = None
    name: str = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    alias: Optional[str] = None
    organization_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.name is None:
            raise ValueError("name must be supplied")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.organization_type is not None and not isinstance(self.organization_type, str):
            self.organization_type = str(self.organization_type)

        super().__post_init__(**kwargs)


@dataclass
class CDM.Exposure(YAMLRoot):
    """
    Contact between an agent and a target. A state of contact or close proximity to a medicinal product, chemical,
    pathogen, radioisotope or other substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH["CDM.Exposure"]
    class_class_curie: ClassVar[str] = "ccdh:CDM.Exposure"
    class_name: ClassVar[str] = "CDM.Exposure"
    class_model_uri: ClassVar[URIRef] = CCDH.CDM.Exposure

    id: str = None
    identifier: Optional[Union[str, List[str]]] = empty_list()
    tobacco_use: Optional[str] = None
    alcohol_use: Optional[str] = None
    environmental: Optional[Union[str, List[str]]] = empty_list()
    related_patient: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if self.tobacco_use is not None and not isinstance(self.tobacco_use, str):
            self.tobacco_use = str(self.tobacco_use)

        if self.alcohol_use is not None and not isinstance(self.alcohol_use, str):
            self.alcohol_use = str(self.alcohol_use)

        if self.environmental is None:
            self.environmental = []
        if not isinstance(self.environmental, list):
            self.environmental = [self.environmental]
        self.environmental = [v if isinstance(v, str) else str(v) for v in self.environmental]

        if self.related_patient is not None and not isinstance(self.related_patient, str):
            self.related_patient = str(self.related_patient)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.cDM.Specimen__id = Slot(uri=CCDH.id, name="cDM.Specimen__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.Specimen__id'], domain=None, range=Optional[str])

slots.cDM.Specimen__identifier = Slot(uri=CCDH.identifier, name="cDM.Specimen__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.Specimen__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__description = Slot(uri=CCDH.description, name="cDM.Specimen__description", curie=CCDH.curie('description'),
                   model_uri=CCDH['cDM.Specimen__description'], domain=None, range=Optional[str])

slots.cDM.Specimen__specimen_type = Slot(uri=CCDH.specimen_type, name="cDM.Specimen__specimen_type", curie=CCDH.curie('specimen_type'),
                   model_uri=CCDH['cDM.Specimen__specimen_type'], domain=None, range=Optional[str])

slots.cDM.Specimen__analyte_type = Slot(uri=CCDH.analyte_type, name="cDM.Specimen__analyte_type", curie=CCDH.curie('analyte_type'),
                   model_uri=CCDH['cDM.Specimen__analyte_type'], domain=None, range=Optional[str])

slots.cDM.Specimen__associated_project = Slot(uri=CCDH.associated_project, name="cDM.Specimen__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH['cDM.Specimen__associated_project'], domain=None, range=Optional[str])

slots.cDM.Specimen__provided_by = Slot(uri=CCDH.provided_by, name="cDM.Specimen__provided_by", curie=CCDH.curie('provided_by'),
                   model_uri=CCDH['cDM.Specimen__provided_by'], domain=None, range=Optional[str])

slots.cDM.Specimen__source_material_type = Slot(uri=CCDH.source_material_type, name="cDM.Specimen__source_material_type", curie=CCDH.curie('source_material_type'),
                   model_uri=CCDH['cDM.Specimen__source_material_type'], domain=None, range=Optional[str])

slots.cDM.Specimen__parent_specimen = Slot(uri=CCDH.parent_specimen, name="cDM.Specimen__parent_specimen", curie=CCDH.curie('parent_specimen'),
                   model_uri=CCDH['cDM.Specimen__parent_specimen'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__source_patient = Slot(uri=CCDH.source_patient, name="cDM.Specimen__source_patient", curie=CCDH.curie('source_patient'),
                   model_uri=CCDH['cDM.Specimen__source_patient'], domain=None, range=Optional[str])

slots.cDM.Specimen__source_model_system = Slot(uri=CCDH.source_model_system, name="cDM.Specimen__source_model_system", curie=CCDH.curie('source_model_system'),
                   model_uri=CCDH['cDM.Specimen__source_model_system'], domain=None, range=Optional[str])

slots.cDM.Specimen__condition_status_at_collection = Slot(uri=CCDH.condition_status_at_collection, name="cDM.Specimen__condition_status_at_collection", curie=CCDH.curie('condition_status_at_collection'),
                   model_uri=CCDH['cDM.Specimen__condition_status_at_collection'], domain=None, range=Optional[str])

slots.cDM.Specimen__related_diagnosis = Slot(uri=CCDH.related_diagnosis, name="cDM.Specimen__related_diagnosis", curie=CCDH.curie('related_diagnosis'),
                   model_uri=CCDH['cDM.Specimen__related_diagnosis'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__creation_activity = Slot(uri=CCDH.creation_activity, name="cDM.Specimen__creation_activity", curie=CCDH.curie('creation_activity'),
                   model_uri=CCDH['cDM.Specimen__creation_activity'], domain=None, range=Optional[str])

slots.cDM.Specimen__processing_activity = Slot(uri=CCDH.processing_activity, name="cDM.Specimen__processing_activity", curie=CCDH.curie('processing_activity'),
                   model_uri=CCDH['cDM.Specimen__processing_activity'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__storage_activity = Slot(uri=CCDH.storage_activity, name="cDM.Specimen__storage_activity", curie=CCDH.curie('storage_activity'),
                   model_uri=CCDH['cDM.Specimen__storage_activity'], domain=None, range=Optional[str])

slots.cDM.Specimen__transport_activity = Slot(uri=CCDH.transport_activity, name="cDM.Specimen__transport_activity", curie=CCDH.curie('transport_activity'),
                   model_uri=CCDH['cDM.Specimen__transport_activity'], domain=None, range=Optional[str])

slots.cDM.Specimen__contained_in = Slot(uri=CCDH.contained_in, name="cDM.Specimen__contained_in", curie=CCDH.curie('contained_in'),
                   model_uri=CCDH['cDM.Specimen__contained_in'], domain=None, range=Optional[str])

slots.cDM.Specimen__dimensional_measure = Slot(uri=CCDH.dimensional_measure, name="cDM.Specimen__dimensional_measure", curie=CCDH.curie('dimensional_measure'),
                   model_uri=CCDH['cDM.Specimen__dimensional_measure'], domain=None, range=Optional[str])

slots.cDM.Specimen__quantity_measure = Slot(uri=CCDH.quantity_measure, name="cDM.Specimen__quantity_measure", curie=CCDH.curie('quantity_measure'),
                   model_uri=CCDH['cDM.Specimen__quantity_measure'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__quality_measure = Slot(uri=CCDH.quality_measure, name="cDM.Specimen__quality_measure", curie=CCDH.curie('quality_measure'),
                   model_uri=CCDH['cDM.Specimen__quality_measure'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__cellular_composition_type = Slot(uri=CCDH.cellular_composition_type, name="cDM.Specimen__cellular_composition_type", curie=CCDH.curie('cellular_composition_type'),
                   model_uri=CCDH['cDM.Specimen__cellular_composition_type'], domain=None, range=Optional[str])

slots.cDM.Specimen__cellular_composition_measure = Slot(uri=CCDH.cellular_composition_measure, name="cDM.Specimen__cellular_composition_measure", curie=CCDH.curie('cellular_composition_measure'),
                   model_uri=CCDH['cDM.Specimen__cellular_composition_measure'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__tissue_composition_measure = Slot(uri=CCDH.tissue_composition_measure, name="cDM.Specimen__tissue_composition_measure", curie=CCDH.curie('tissue_composition_measure'),
                   model_uri=CCDH['cDM.Specimen__tissue_composition_measure'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="cDM.Specimen__general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                   model_uri=CCDH['cDM.Specimen__general_tissue_morphology'], domain=None, range=Optional[str])

slots.cDM.Specimen__specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="cDM.Specimen__specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                   model_uri=CCDH['cDM.Specimen__specific_tissue_morphology'], domain=None, range=Optional[str])

slots.cDM.Specimen__morphology_pathologically_confirmed = Slot(uri=CCDH.morphology_pathologically_confirmed, name="cDM.Specimen__morphology_pathologically_confirmed", curie=CCDH.curie('morphology_pathologically_confirmed'),
                   model_uri=CCDH['cDM.Specimen__morphology_pathologically_confirmed'], domain=None, range=Optional[str])

slots.cDM.Specimen__related_document = Slot(uri=CCDH.related_document, name="cDM.Specimen__related_document", curie=CCDH.curie('related_document'),
                   model_uri=CCDH['cDM.Specimen__related_document'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__related_specimen = Slot(uri=CCDH.related_specimen, name="cDM.Specimen__related_specimen", curie=CCDH.curie('related_specimen'),
                   model_uri=CCDH['cDM.Specimen__related_specimen'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__derived_product = Slot(uri=CCDH.derived_product, name="cDM.Specimen__derived_product", curie=CCDH.curie('derived_product'),
                   model_uri=CCDH['cDM.Specimen__derived_product'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__qualification_status_flag = Slot(uri=CCDH.qualification_status_flag, name="cDM.Specimen__qualification_status_flag", curie=CCDH.curie('qualification_status_flag'),
                   model_uri=CCDH['cDM.Specimen__qualification_status_flag'], domain=None, range=Optional[str])

slots.cDM.Specimen__reference_status_flag = Slot(uri=CCDH.reference_status_flag, name="cDM.Specimen__reference_status_flag", curie=CCDH.curie('reference_status_flag'),
                   model_uri=CCDH['cDM.Specimen__reference_status_flag'], domain=None, range=Optional[str])

slots.cDM.Specimen__matched_normal_flag = Slot(uri=CCDH.matched_normal_flag, name="cDM.Specimen__matched_normal_flag", curie=CCDH.curie('matched_normal_flag'),
                   model_uri=CCDH['cDM.Specimen__matched_normal_flag'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Specimen__selected_normal_flag = Slot(uri=CCDH.selected_normal_flag, name="cDM.Specimen__selected_normal_flag", curie=CCDH.curie('selected_normal_flag'),
                   model_uri=CCDH['cDM.Specimen__selected_normal_flag'], domain=None, range=Optional[str])

slots.cDM.Specimen__paired_specimen_genotype_match_flag = Slot(uri=CCDH.paired_specimen_genotype_match_flag, name="cDM.Specimen__paired_specimen_genotype_match_flag", curie=CCDH.curie('paired_specimen_genotype_match_flag'),
                   model_uri=CCDH['cDM.Specimen__paired_specimen_genotype_match_flag'], domain=None, range=Optional[str])

slots.cDM.Specimen__section_location = Slot(uri=CCDH.section_location, name="cDM.Specimen__section_location", curie=CCDH.curie('section_location'),
                   model_uri=CCDH['cDM.Specimen__section_location'], domain=None, range=Optional[str])

slots.cDM.Report__id = Slot(uri=CCDH.id, name="cDM.Report__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.Report__id'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenCreationActivity__id = Slot(uri=CCDH.id, name="cDM.SpecimenCreationActivity__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__id'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__activity_type = Slot(uri=CCDH.activity_type, name="cDM.SpecimenCreationActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__activity_type'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__date_started = Slot(uri=CCDH.date_started, name="cDM.SpecimenCreationActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__date_started'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__date_ended = Slot(uri=CCDH.date_ended, name="cDM.SpecimenCreationActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__date_ended'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__performed_by = Slot(uri=CCDH.performed_by, name="cDM.SpecimenCreationActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__performed_by'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__method_type = Slot(uri=CCDH.method_type, name="cDM.SpecimenCreationActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__method_type'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__collection_site = Slot(uri=CCDH.collection_site, name="cDM.SpecimenCreationActivity__collection_site", curie=CCDH.curie('collection_site'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__collection_site'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__input_specimen = Slot(uri=CCDH.input_specimen, name="cDM.SpecimenCreationActivity__input_specimen", curie=CCDH.curie('input_specimen'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__input_specimen'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenCreationActivity__quantity_collected = Slot(uri=CCDH.quantity_collected, name="cDM.SpecimenCreationActivity__quantity_collected", curie=CCDH.curie('quantity_collected'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__quantity_collected'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__execution_condition = Slot(uri=CCDH.execution_condition, name="cDM.SpecimenCreationActivity__execution_condition", curie=CCDH.curie('execution_condition'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__execution_condition'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenCreationActivity__collected_during_visit = Slot(uri=CCDH.collected_during_visit, name="cDM.SpecimenCreationActivity__collected_during_visit", curie=CCDH.curie('collected_during_visit'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__collected_during_visit'], domain=None, range=Optional[str])

slots.cDM.SpecimenCreationActivity__relative_timing = Slot(uri=CCDH.relative_timing, name="cDM.SpecimenCreationActivity__relative_timing", curie=CCDH.curie('relative_timing'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__relative_timing'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenCreationActivity__relative_order = Slot(uri=CCDH.relative_order, name="cDM.SpecimenCreationActivity__relative_order", curie=CCDH.curie('relative_order'),
                   model_uri=CCDH['cDM.SpecimenCreationActivity__relative_order'], domain=None, range=Optional[str])

slots.cDM.SpecimenProcessingActivity__duration = Slot(uri=CCDH.duration, name="cDM.SpecimenProcessingActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH['cDM.SpecimenProcessingActivity__duration'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenProcessingActivity__performed_by = Slot(uri=CCDH.performed_by, name="cDM.SpecimenProcessingActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH['cDM.SpecimenProcessingActivity__performed_by'], domain=None, range=Optional[str])

slots.cDM.SpecimenStorageActivity__id = Slot(uri=CCDH.id, name="cDM.SpecimenStorageActivity__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.SpecimenStorageActivity__id'], domain=None, range=Optional[str])

slots.cDM.SpecimenTransportActivity__id = Slot(uri=CCDH.id, name="cDM.SpecimenTransportActivity__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.SpecimenTransportActivity__id'], domain=None, range=Optional[str])

slots.cDM.SpecimenTransportActivity__date_started = Slot(uri=CCDH.date_started, name="cDM.SpecimenTransportActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH['cDM.SpecimenTransportActivity__date_started'], domain=None, range=Optional[str])

slots.cDM.SpecimenTransportActivity__date_ended = Slot(uri=CCDH.date_ended, name="cDM.SpecimenTransportActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH['cDM.SpecimenTransportActivity__date_ended'], domain=None, range=Optional[str])

slots.cDM.SpecimenTransportActivity__transport_destination = Slot(uri=CCDH.transport_destination, name="cDM.SpecimenTransportActivity__transport_destination", curie=CCDH.curie('transport_destination'),
                   model_uri=CCDH['cDM.SpecimenTransportActivity__transport_destination'], domain=None, range=Optional[str])

slots.cDM.SpecimenTransportActivity__execution_conditions = Slot(uri=CCDH.execution_conditions, name="cDM.SpecimenTransportActivity__execution_conditions", curie=CCDH.curie('execution_conditions'),
                   model_uri=CCDH['cDM.SpecimenTransportActivity__execution_conditions'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenContainer__container_type = Slot(uri=CCDH.container_type, name="cDM.SpecimenContainer__container_type", curie=CCDH.curie('container_type'),
                   model_uri=CCDH['cDM.SpecimenContainer__container_type'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenContainer__container_number = Slot(uri=CCDH.container_number, name="cDM.SpecimenContainer__container_number", curie=CCDH.curie('container_number'),
                   model_uri=CCDH['cDM.SpecimenContainer__container_number'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenContainer__additive = Slot(uri=CCDH.additive, name="cDM.SpecimenContainer__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH['cDM.SpecimenContainer__additive'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenContainer__parent_container = Slot(uri=CCDH.parent_container, name="cDM.SpecimenContainer__parent_container", curie=CCDH.curie('parent_container'),
                   model_uri=CCDH['cDM.SpecimenContainer__parent_container'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.SpecimenContainer__charge_type = Slot(uri=CCDH.charge_type, name="cDM.SpecimenContainer__charge_type", curie=CCDH.curie('charge_type'),
                   model_uri=CCDH['cDM.SpecimenContainer__charge_type'], domain=None, range=Optional[str])

slots.cDM.BiologicallyDerivedProduct__id = Slot(uri=CCDH.id, name="cDM.BiologicallyDerivedProduct__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.BiologicallyDerivedProduct__id'], domain=None, range=Optional[str])

slots.cDM.BiologicallyDerivedProduct__description = Slot(uri=CCDH.description, name="cDM.BiologicallyDerivedProduct__description", curie=CCDH.curie('description'),
                   model_uri=CCDH['cDM.BiologicallyDerivedProduct__description'], domain=None, range=Optional[str])

slots.cDM.BiologicallyDerivedProduct__type = Slot(uri=CCDH.type, name="cDM.BiologicallyDerivedProduct__type", curie=CCDH.curie('type'),
                   model_uri=CCDH['cDM.BiologicallyDerivedProduct__type'], domain=None, range=Optional[str])

slots.cDM.BiologicallyDerivedProduct__passage_number = Slot(uri=CCDH.passage_number, name="cDM.BiologicallyDerivedProduct__passage_number", curie=CCDH.curie('passage_number'),
                   model_uri=CCDH['cDM.BiologicallyDerivedProduct__passage_number'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.BiologicallyDerivedProduct__growth_rate = Slot(uri=CCDH.growth_rate, name="cDM.BiologicallyDerivedProduct__growth_rate", curie=CCDH.curie('growth_rate'),
                   model_uri=CCDH['cDM.BiologicallyDerivedProduct__growth_rate'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Patient__id = Slot(uri=CCDH.id, name="cDM.Patient__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.Patient__id'], domain=None, range=str)

slots.cDM.Patient__identifier = Slot(uri=CCDH.identifier, name="cDM.Patient__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.Patient__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Patient__given_name = Slot(uri=CCDH.given_name, name="cDM.Patient__given_name", curie=CCDH.curie('given_name'),
                   model_uri=CCDH['cDM.Patient__given_name'], domain=None, range=Optional[str])

slots.cDM.Patient__taxon = Slot(uri=CCDH.taxon, name="cDM.Patient__taxon", curie=CCDH.curie('taxon'),
                   model_uri=CCDH['cDM.Patient__taxon'], domain=None, range=Optional[str])

slots.cDM.Patient__adverse_events = Slot(uri=CCDH.adverse_events, name="cDM.Patient__adverse_events", curie=CCDH.curie('adverse_events'),
                   model_uri=CCDH['cDM.Patient__adverse_events'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__id = Slot(uri=CCDH.id, name="cDM.ResearchSubject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.ResearchSubject__id'], domain=None, range=str)

slots.cDM.ResearchSubject__identifier = Slot(uri=CCDH.identifier, name="cDM.ResearchSubject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.ResearchSubject__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__description = Slot(uri=CCDH.description, name="cDM.ResearchSubject__description", curie=CCDH.curie('description'),
                   model_uri=CCDH['cDM.ResearchSubject__description'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__primary_disease_type = Slot(uri=CCDH.primary_disease_type, name="cDM.ResearchSubject__primary_disease_type", curie=CCDH.curie('primary_disease_type'),
                   model_uri=CCDH['cDM.ResearchSubject__primary_disease_type'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__primary_disease_site = Slot(uri=CCDH.primary_disease_site, name="cDM.ResearchSubject__primary_disease_site", curie=CCDH.curie('primary_disease_site'),
                   model_uri=CCDH['cDM.ResearchSubject__primary_disease_site'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__qualification_status_flag = Slot(uri=CCDH.qualification_status_flag, name="cDM.ResearchSubject__qualification_status_flag", curie=CCDH.curie('qualification_status_flag'),
                   model_uri=CCDH['cDM.ResearchSubject__qualification_status_flag'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__associated_project = Slot(uri=CCDH.associated_project, name="cDM.ResearchSubject__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH['cDM.ResearchSubject__associated_project'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__member_of_cohort = Slot(uri=CCDH.member_of_cohort, name="cDM.ResearchSubject__member_of_cohort", curie=CCDH.curie('member_of_cohort'),
                   model_uri=CCDH['cDM.ResearchSubject__member_of_cohort'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__member_of_study = Slot(uri=CCDH.member_of_study, name="cDM.ResearchSubject__member_of_study", curie=CCDH.curie('member_of_study'),
                   model_uri=CCDH['cDM.ResearchSubject__member_of_study'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__index_timepoint = Slot(uri=CCDH.index_timepoint, name="cDM.ResearchSubject__index_timepoint", curie=CCDH.curie('index_timepoint'),
                   model_uri=CCDH['cDM.ResearchSubject__index_timepoint'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__reference_status_flag = Slot(uri=CCDH.reference_status_flag, name="cDM.ResearchSubject__reference_status_flag", curie=CCDH.curie('reference_status_flag'),
                   model_uri=CCDH['cDM.ResearchSubject__reference_status_flag'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__processed_at = Slot(uri=CCDH.processed_at, name="cDM.ResearchSubject__processed_at", curie=CCDH.curie('processed_at'),
                   model_uri=CCDH['cDM.ResearchSubject__processed_at'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__originating_site = Slot(uri=CCDH.originating_site, name="cDM.ResearchSubject__originating_site", curie=CCDH.curie('originating_site'),
                   model_uri=CCDH['cDM.ResearchSubject__originating_site'], domain=None, range=Optional[str])

slots.cDM.ResearchSubject__study_progress = Slot(uri=CCDH.study_progress, name="cDM.ResearchSubject__study_progress", curie=CCDH.curie('study_progress'),
                   model_uri=CCDH['cDM.ResearchSubject__study_progress'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchSubject__associated_patient = Slot(uri=CCDH.associated_patient, name="cDM.ResearchSubject__associated_patient", curie=CCDH.curie('associated_patient'),
                   model_uri=CCDH['cDM.ResearchSubject__associated_patient'], domain=None, range=str)

slots.cDM.ResearchProject__id = Slot(uri=CCDH.id, name="cDM.ResearchProject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.ResearchProject__id'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__identifier = Slot(uri=CCDH.identifier, name="cDM.ResearchProject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.ResearchProject__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchProject__name = Slot(uri=CCDH.name, name="cDM.ResearchProject__name", curie=CCDH.curie('name'),
                   model_uri=CCDH['cDM.ResearchProject__name'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__name_shortened = Slot(uri=CCDH.name_shortened, name="cDM.ResearchProject__name_shortened", curie=CCDH.curie('name_shortened'),
                   model_uri=CCDH['cDM.ResearchProject__name_shortened'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__description = Slot(uri=CCDH.description, name="cDM.ResearchProject__description", curie=CCDH.curie('description'),
                   model_uri=CCDH['cDM.ResearchProject__description'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__description_shortened = Slot(uri=CCDH.description_shortened, name="cDM.ResearchProject__description_shortened", curie=CCDH.curie('description_shortened'),
                   model_uri=CCDH['cDM.ResearchProject__description_shortened'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__sponsor = Slot(uri=CCDH.sponsor, name="cDM.ResearchProject__sponsor", curie=CCDH.curie('sponsor'),
                   model_uri=CCDH['cDM.ResearchProject__sponsor'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchProject__date_started = Slot(uri=CCDH.date_started, name="cDM.ResearchProject__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH['cDM.ResearchProject__date_started'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__date_ended = Slot(uri=CCDH.date_ended, name="cDM.ResearchProject__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH['cDM.ResearchProject__date_ended'], domain=None, range=Optional[str])

slots.cDM.ResearchProject__primary_anatomic_site = Slot(uri=CCDH.primary_anatomic_site, name="cDM.ResearchProject__primary_anatomic_site", curie=CCDH.curie('primary_anatomic_site'),
                   model_uri=CCDH['cDM.ResearchProject__primary_anatomic_site'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchProject__url = Slot(uri=CCDH.url, name="cDM.ResearchProject__url", curie=CCDH.curie('url'),
                   model_uri=CCDH['cDM.ResearchProject__url'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchProject__part_of = Slot(uri=CCDH.part_of, name="cDM.ResearchProject__part_of", curie=CCDH.curie('part_of'),
                   model_uri=CCDH['cDM.ResearchProject__part_of'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.ResearchProject__research_project_type = Slot(uri=CCDH.research_project_type, name="cDM.ResearchProject__research_project_type", curie=CCDH.curie('research_project_type'),
                   model_uri=CCDH['cDM.ResearchProject__research_project_type'], domain=None, range=str)

slots.cDM.ResearchProject__date_iacuc_approval = Slot(uri=CCDH.date_iacuc_approval, name="cDM.ResearchProject__date_iacuc_approval", curie=CCDH.curie('date_iacuc_approval'),
                   model_uri=CCDH['cDM.ResearchProject__date_iacuc_approval'], domain=None, range=Optional[str])

slots.cDM.Organization__id = Slot(uri=CCDH.id, name="cDM.Organization__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.Organization__id'], domain=None, range=str)

slots.cDM.Organization__identifier = Slot(uri=CCDH.identifier, name="cDM.Organization__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.Organization__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Organization__name = Slot(uri=CCDH.name, name="cDM.Organization__name", curie=CCDH.curie('name'),
                   model_uri=CCDH['cDM.Organization__name'], domain=None, range=str)

slots.cDM.Organization__alias = Slot(uri=CCDH.alias, name="cDM.Organization__alias", curie=CCDH.curie('alias'),
                   model_uri=CCDH['cDM.Organization__alias'], domain=None, range=Optional[str])

slots.cDM.Organization__organization_type = Slot(uri=CCDH.organization_type, name="cDM.Organization__organization_type", curie=CCDH.curie('organization_type'),
                   model_uri=CCDH['cDM.Organization__organization_type'], domain=None, range=Optional[str])

slots.cDM.Exposure__id = Slot(uri=CCDH.id, name="cDM.Exposure__id", curie=CCDH.curie('id'),
                   model_uri=CCDH['cDM.Exposure__id'], domain=None, range=str)

slots.cDM.Exposure__identifier = Slot(uri=CCDH.identifier, name="cDM.Exposure__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH['cDM.Exposure__identifier'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Exposure__tobacco_use = Slot(uri=CCDH.tobacco_use, name="cDM.Exposure__tobacco_use", curie=CCDH.curie('tobacco_use'),
                   model_uri=CCDH['cDM.Exposure__tobacco_use'], domain=None, range=Optional[str])

slots.cDM.Exposure__alcohol_use = Slot(uri=CCDH.alcohol_use, name="cDM.Exposure__alcohol_use", curie=CCDH.curie('alcohol_use'),
                   model_uri=CCDH['cDM.Exposure__alcohol_use'], domain=None, range=Optional[str])

slots.cDM.Exposure__environmental = Slot(uri=CCDH.environmental, name="cDM.Exposure__environmental", curie=CCDH.curie('environmental'),
                   model_uri=CCDH['cDM.Exposure__environmental'], domain=None, range=Optional[Union[str, List[str]]])

slots.cDM.Exposure__related_patient = Slot(uri=CCDH.related_patient, name="cDM.Exposure__related_patient", curie=CCDH.curie('related_patient'),
                   model_uri=CCDH['cDM.Exposure__related_patient'], domain=None, range=Optional[str])
