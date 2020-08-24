# Auto generated from specimen.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-24 13:36
# Schema: Specimen
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
from biolinkml.utils.metamodelcore import Bool
from datatypes import Coding, Identifier, Literal, Quantity
from entities import BiologicallyDerivedProduct, BodyStructure, ConditionDiagnosis, DataContainer, DocumentReference, Entity, Id, Organization, PatientOrBiologicallyDerivedMaterial, Project, Relationship, SpecimenContainer, SpecimenCreationActivity, SpecimenProcessingActivity, SpecimenStorageActivity, SpecimenTransportActvity
from includes.types import Boolean, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ADM = CurieNamespace('ADM', 'https://ccdh.org/models/ADM/')
GDC = CurieNamespace('GDC', 'http://fill.me.in/GDC')
HTAN = CurieNamespace('HTAN', 'http://fill.me.in/ICDC')
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
    specimen_type: Optional[Union[dict, Coding]] = None
    analyte_type: Optional[Union[dict, Coding]] = None
    associated_project: Optional[Union[dict, Project]] = None
    provided_by: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[dict, Coding]] = None
    derived_from_specimen: Dict[Union[str, SpecimenId], Union[dict, "Specimen"]] = empty_dict()
    derived_from_subject: Optional[Union[dict, PatientOrBiologicallyDerivedMaterial]] = None
    subject_diagnosis: Dict[Union[str, ConditionDiagnosisId], Union[dict, ConditionDiagnosis]] = empty_dict()
    creation: Optional[Union[dict, SpecimenCreationActivity]] = None
    processing: List[Union[dict, SpecimenProcessingActivity]] = empty_list()
    storage: Optional[Union[dict, SpecimenStorageActivity]] = None
    transport: Optional[Union[dict, SpecimenTransportActvity]] = None
    contained_in: Optional[Union[dict, SpecimenContainer]] = None
    current_weight: List[Union[dict, Quantity]] = empty_list()
    volume: List[Union[dict, Quantity]] = empty_list()
    dimensional_measure: Optional[Union[dict, DataContainer]] = None
    analyte_concentration: Optional[Union[dict, Quantity]] = None
    analyte_concentration_method: Optional[Union[dict, Coding]] = None
    cellular_composition: Optional[Union[dict, Coding]] = None
    compositional_measure: Optional[Union[dict, DataContainer]] = None
    specimen_quality_measure: List[Union[dict, DataContainer]] = empty_list()
    general_tissue_morphology: Optional[Union[dict, Coding]] = None
    specific_tissue_morphology: Optional[Union[dict, Coding]] = None
    morphology_pathologically_confirmed: Optional[Bool] = None
    related_document: Dict[Union[str, DocumentReferenceId], Union[dict, DocumentReference]] = empty_dict()
    related_specimen: List[Union[dict, Relationship]] = empty_list()
    derived_product: List[Union[dict, BiologicallyDerivedProduct]] = empty_list()
    qualification_status_flag: Optional[Union[dict, Coding]] = None
    reference_status_flag: Optional[Bool] = None
    matched_normal_flag: List[Union[dict, Coding]] = empty_list()
    selected_normal_flag: Optional[Union[dict, Coding]] = None
    paired_specimen_genotype_match_flag: Optional[Union[dict, Coding]] = None
    source_body_structure: List[Union[dict, BodyStructure]] = empty_list()
    distance_from_paired_specimen: Optional[Union[str, Literal]] = None

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
        if self.specimen_type is not None and not isinstance(self.specimen_type, Coding):
            self.specimen_type = Coding()
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
        for k, v in self.subject_diagnosis.items():
            if not isinstance(v, ConditionDiagnosis):
                self.subject_diagnosis[k] = ConditionDiagnosis(id=k, **({} if v is None else v))
        if self.creation is not None and not isinstance(self.creation, SpecimenCreationActivity):
            self.creation = SpecimenCreationActivity()
        self.processing = [SpecimenProcessingActivity(*e) for e in self.processing.items()] if isinstance(self.processing, dict) \
                           else [v if isinstance(v, SpecimenProcessingActivity) else SpecimenProcessingActivity(**v)
                                 for v in ([self.processing] if isinstance(self.processing, str) else self.processing)]
        if self.storage is not None and not isinstance(self.storage, SpecimenStorageActivity):
            self.storage = SpecimenStorageActivity()
        if self.transport is not None and not isinstance(self.transport, SpecimenTransportActvity):
            self.transport = SpecimenTransportActvity()
        if self.contained_in is not None and not isinstance(self.contained_in, SpecimenContainer):
            self.contained_in = SpecimenContainer()
        self.current_weight = [Quantity(*e) for e in self.current_weight.items()] if isinstance(self.current_weight, dict) \
                               else [v if isinstance(v, Quantity) else Quantity(**v)
                                     for v in ([self.current_weight] if isinstance(self.current_weight, str) else self.current_weight)]
        self.volume = [Quantity(*e) for e in self.volume.items()] if isinstance(self.volume, dict) \
                       else [v if isinstance(v, Quantity) else Quantity(**v)
                             for v in ([self.volume] if isinstance(self.volume, str) else self.volume)]
        if self.dimensional_measure is not None and not isinstance(self.dimensional_measure, DataContainer):
            self.dimensional_measure = DataContainer()
        if self.analyte_concentration is not None and not isinstance(self.analyte_concentration, Quantity):
            self.analyte_concentration = Quantity()
        if self.analyte_concentration_method is not None and not isinstance(self.analyte_concentration_method, Coding):
            self.analyte_concentration_method = Coding()
        if self.cellular_composition is not None and not isinstance(self.cellular_composition, Coding):
            self.cellular_composition = Coding()
        if self.compositional_measure is not None and not isinstance(self.compositional_measure, DataContainer):
            self.compositional_measure = DataContainer()
        self.specimen_quality_measure = [DataContainer(*e) for e in self.specimen_quality_measure.items()] if isinstance(self.specimen_quality_measure, dict) \
                                         else [v if isinstance(v, DataContainer) else DataContainer(**v)
                                               for v in ([self.specimen_quality_measure] if isinstance(self.specimen_quality_measure, str) else self.specimen_quality_measure)]
        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, Coding):
            self.general_tissue_morphology = Coding()
        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, Coding):
            self.specific_tissue_morphology = Coding()
        for k, v in self.related_document.items():
            if not isinstance(v, DocumentReference):
                self.related_document[k] = DocumentReference(id=k, **({} if v is None else v))
        self.related_specimen = [Relationship(*e) for e in self.related_specimen.items()] if isinstance(self.related_specimen, dict) \
                                 else [v if isinstance(v, Relationship) else Relationship(**v)
                                       for v in ([self.related_specimen] if isinstance(self.related_specimen, str) else self.related_specimen)]
        self.derived_product = [BiologicallyDerivedProduct(*e) for e in self.derived_product.items()] if isinstance(self.derived_product, dict) \
                                else [v if isinstance(v, BiologicallyDerivedProduct) else BiologicallyDerivedProduct(**v)
                                      for v in ([self.derived_product] if isinstance(self.derived_product, str) else self.derived_product)]
        if self.qualification_status_flag is not None and not isinstance(self.qualification_status_flag, Coding):
            self.qualification_status_flag = Coding()
        self.matched_normal_flag = [Coding(*e) for e in self.matched_normal_flag.items()] if isinstance(self.matched_normal_flag, dict) \
                                    else [v if isinstance(v, Coding) else Coding(**v)
                                          for v in ([self.matched_normal_flag] if isinstance(self.matched_normal_flag, str) else self.matched_normal_flag)]
        if self.selected_normal_flag is not None and not isinstance(self.selected_normal_flag, Coding):
            self.selected_normal_flag = Coding()
        if self.paired_specimen_genotype_match_flag is not None and not isinstance(self.paired_specimen_genotype_match_flag, Coding):
            self.paired_specimen_genotype_match_flag = Coding()
        self.source_body_structure = [BodyStructure(*e) for e in self.source_body_structure.items()] if isinstance(self.source_body_structure, dict) \
                                      else [v if isinstance(v, BodyStructure) else BodyStructure(**v)
                                            for v in ([self.source_body_structure] if isinstance(self.source_body_structure, str) else self.source_body_structure)]
        if self.distance_from_paired_specimen is not None and not isinstance(self.distance_from_paired_specimen, Literal):
            self.distance_from_paired_specimen = Literal(self.distance_from_paired_specimen)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.identifier = Slot(uri=SPECIMEN.identifier, name="identifier", curie=SPECIMEN.curie('identifier'),
                      model_uri=SPECIMEN.identifier, domain=None, range=List[Union[dict, Identifier]], mappings = [ADM["Sample.sample_submitter_id"], ADM["Sample.gdc_sample_id"], ADM["Portion.submitter_id"], ADM["Analyte.analyte_submitter_id"], GDC["Sample.submitter_id"], GDC["Analyte.submitter_id"], PDC["Sample.sample_submitter_id"], PDC["Analyte.analyte_submitter_id"]])

slots.description = Slot(uri=SPECIMEN.description, name="description", curie=SPECIMEN.curie('description'),
                      model_uri=SPECIMEN.description, domain=None, range=Optional[Union[str, Literal]], mappings = [ADM["Sample.comment"], ICDC["Sample.comment"]])

slots.specimen_type = Slot(uri=SPECIMEN.specimen_type, name="specimen_type", curie=SPECIMEN.curie('specimen_type'),
                      model_uri=SPECIMEN.specimen_type, domain=None, range=Optional[Union[dict, Coding]])

slots.analyte_type = Slot(uri=SPECIMEN.analyte_type, name="analyte_type", curie=SPECIMEN.curie('analyte_type'),
                      model_uri=SPECIMEN.analyte_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.analyte_type"], ADM["Aliquot.analyte_type_id"], ADM["Analyte.analyte_type"], ADM["Analyte.analyte_type_id"], GDC["Aliquot.analyte_type"], GDC["Aliquot.analyte_type_id"], PDC["Aliquot.analyte_type"], PDC["Aliquot.analyte_type_id"], ICDC["Biosepcimen.ANALYTE_TYPE"]])

slots.associated_project = Slot(uri=SPECIMEN.associated_project, name="associated_project", curie=SPECIMEN.curie('associated_project'),
                      model_uri=SPECIMEN.associated_project, domain=None, range=Optional[Union[dict, Project]], mappings = [ADM["Sample.project_id"], ADM["Sample.gdc_project_id"], ADM["Portion.project_id"], ADM["Aliquot.project_id"], ADM["Analyte.project_id"], GDC["Sample.project_id"], GDC["Portion.project_id"], GDC["Aliquot.project_id"], GDC["Analyte.project_id"], PDC["Sample.gdc_project_id"]])

slots.provided_by = Slot(uri=SPECIMEN.provided_by, name="provided_by", curie=SPECIMEN.curie('provided_by'),
                      model_uri=SPECIMEN.provided_by, domain=None, range=Optional[Union[dict, Organization]], mappings = [ADM["Aliquot.source_center"], GDC["Aliquot.source_center"]])

slots.source_material_type = Slot(uri=SPECIMEN.source_material_type, name="source_material_type", curie=SPECIMEN.curie('source_material_type'),
                      model_uri=SPECIMEN.source_material_type, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.sample_type"], ADM["Sample.sample_type_id"], GDC["Sample.sample_type"], GDC["Sample.sample_type_id"], PDC["Sample.sample_type"], PDC["Sample.sample_type_id"], ICDC["Sample.sample_type"], ICDC["Biospecimen.BIOSPECIMEN_TYPE"]])

slots.derived_from_specimen = Slot(uri=SPECIMEN.derived_from_specimen, name="derived_from_specimen", curie=SPECIMEN.curie('derived_from_specimen'),
                      model_uri=SPECIMEN.derived_from_specimen, domain=None, range=Dict[Union[str, SpecimenId], Union[dict, Specimen]], mappings = [ADM["Sample.derived_from_sample"], ADM["Portion.derived_from"], ADM["Aliquot.derived_from_analyte"], ADM["Aliquot.derived_from_sample"], ADM["Analyte.derived_from_portion"], ADM["Analyte.derived_from_sample"], GDC["Sample.derived_from"], GDC["Aliquot.derived_from"], GDC["Aliquot.derived_from"], GDC["Analyte.derived_from"], GDC["Analyte.derived_from"], GDC["Portion.derived_from"], PDC["Aliquot.Sample"], PDC["Analyte.Portion"], PDC["Analyte.Sample"], PDC["Portion.Sample"]])

slots.derived_from_subject = Slot(uri=SPECIMEN.derived_from_subject, name="derived_from_subject", curie=SPECIMEN.curie('derived_from_subject'),
                      model_uri=SPECIMEN.derived_from_subject, domain=None, range=Optional[Union[dict, PatientOrBiologicallyDerivedMaterial]], mappings = [ADM["Sample.derived_from_case"], PDC["Sample.Case"], GDC["Sample.derived_from"], ICDC["Sample.of_case"], ICDC["Biospecimen.HTAN_PARENT_ID"]])

slots.subject_diagnosis = Slot(uri=SPECIMEN.subject_diagnosis, name="subject_diagnosis", curie=SPECIMEN.curie('subject_diagnosis'),
                      model_uri=SPECIMEN.subject_diagnosis, domain=None, range=Dict[Union[str, ConditionDiagnosisId], Union[dict, ConditionDiagnosis]], mappings = [ADM["Sample.tumor_descriptor"], GDC["Sample.tumor_descriptor"], PDC["Sample.tumor_descriptor"], ICDC["Biospecimen.TUMOR_TISSUE_TYPE"], ICDC["Sample.tumor_sample_origin"]])

slots.creation = Slot(uri=SPECIMEN.creation, name="creation", curie=SPECIMEN.curie('creation'),
                      model_uri=SPECIMEN.creation, domain=None, range=Optional[Union[dict, SpecimenCreationActivity]])

slots.processing = Slot(uri=SPECIMEN.processing, name="processing", curie=SPECIMEN.curie('processing'),
                      model_uri=SPECIMEN.processing, domain=None, range=List[Union[dict, SpecimenProcessingActivity]])

slots.storage = Slot(uri=SPECIMEN.storage, name="storage", curie=SPECIMEN.curie('storage'),
                      model_uri=SPECIMEN.storage, domain=None, range=Optional[Union[dict, SpecimenStorageActivity]])

slots.transport = Slot(uri=SPECIMEN.transport, name="transport", curie=SPECIMEN.curie('transport'),
                      model_uri=SPECIMEN.transport, domain=None, range=Optional[Union[dict, SpecimenTransportActvity]])

slots.contained_in = Slot(uri=SPECIMEN.contained_in, name="contained_in", curie=SPECIMEN.curie('contained_in'),
                      model_uri=SPECIMEN.contained_in, domain=None, range=Optional[Union[dict, SpecimenContainer]], mappings = [ADM["Analyte.well_number"], ADM["Sample.collection_media"], GDC["Analyte.well_number"], PDC["Analyte.well_number"], ICDC["Biospecimen.COLLECTION_MEDIA"]])

slots.current_weight = Slot(uri=SPECIMEN.current_weight, name="current_weight", curie=SPECIMEN.curie('current_weight'),
                      model_uri=SPECIMEN.current_weight, domain=None, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.current_weight"], ADM["Portion.weight"], ADM["Aliquot.quantity"], ADM["Aliquot.amount"], ADM["Analyte.analyte_quantity"], ADM["Analyte.amount"], GDC["Sample.current_weight"], GDC["Aliquot.amount"], GDC["Portion.weight"], GDC["Aliquot.aliquot_quantity"], GDC["Analyte.amount"], GDC["Analyte.analyte_quantity"], PDC["Sample.current_weight"], PDC["Aliquot.amount"], PDC["Portion.weight"], PDC["Aliquot.aliquot_quantity"], PDC["Analyte.amount"], PDC["Analyte.analyte_quantity"], ICDC["Biospecimen.PORTION_WEIGHT"]])

slots.volume = Slot(uri=SPECIMEN.volume, name="volume", curie=SPECIMEN.curie('volume'),
                      model_uri=SPECIMEN.volume, domain=None, range=List[Union[dict, Quantity]], mappings = [ADM["Sample.total_volume"], ADM["Aliquot.volume"], ADM["Analyte.analyte_volume"], ADM["Aliquot.amount"], ADM["Analyte.amount"], GDC["Aliquot.aliquot_volume"], GDC["Analyte.amount"], GDC["Aliquot.amount"], PDC["Aliquot.aliquot_volume"], PDC["Analyte.amount"], PDC["Aliquot.amount"], ICDC["Biospecimen.TOTAL_VOLUME"]])

slots.dimensional_measure = Slot(uri=SPECIMEN.dimensional_measure, name="dimensional_measure", curie=SPECIMEN.curie('dimensional_measure'),
                      model_uri=SPECIMEN.dimensional_measure, domain=None, range=Optional[Union[dict, DataContainer]], mappings = [ADM["Sample.length_of_tumor"], ADM["Sample.width_of_tumor"], ADM["Sample.longest_dimension"], ADM["Sample.shortest_dimension"], ADM["Sample.intermediate_dimension"], ADM["Sample.total_tissue_area"], ADM["Portion.section_thickness_value"], GDC["Sample.longest_dimension"], GDC["Sample.shortest_dimension"], GDC["Sample.intermediate_dimension"], PDC["Sample.longest_dimension"], PDC["Sample.shortest_dimension"], PDC["Sample.intermediate_dimension"], ICDC["Sample.length_of_tumor"], ICDC["Sample.width_of_tumor"], ICDC["Sample.total_tissue_area"], ICDC["Biospecimen.SECTION_THICKNESS_VALUE"]])

slots.analyte_concentration = Slot(uri=SPECIMEN.analyte_concentration, name="analyte_concentration", curie=SPECIMEN.curie('analyte_concentration'),
                      model_uri=SPECIMEN.analyte_concentration, domain=None, range=Optional[Union[dict, Quantity]], mappings = [ADM["Aliquot.concentration"], ADM["Analyte.concentration"], GDC["Aliquot.concentration"], PDC["Aliquot.concentration"]])

slots.analyte_concentration_method = Slot(uri=SPECIMEN.analyte_concentration_method, name="analyte_concentration_method", curie=SPECIMEN.curie('analyte_concentration_method'),
                      model_uri=SPECIMEN.analyte_concentration_method, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Analyte.spectrophotometer_method"], GDC["Analyte.spectrophotometer_method"], PDC["Analyte.spectrophotometer_method"]])

slots.cellular_composition = Slot(uri=SPECIMEN.cellular_composition, name="cellular_composition", curie=SPECIMEN.curie('cellular_composition'),
                      model_uri=SPECIMEN.cellular_composition, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.composition"], GDC["Sample.composition"], PDC["Sample.composition"]])

slots.compositional_measure = Slot(uri=SPECIMEN.compositional_measure, name="compositional_measure", curie=SPECIMEN.curie('compositional_measure'),
                      model_uri=SPECIMEN.compositional_measure, domain=None, range=Optional[Union[dict, DataContainer]], mappings = [ADM["Sample.non_tumor_tissue_area"], ADM["Sample.tumor_tissue_area"], ADM["Sample.percentage_tumor"], ADM["Sample.percentage_stroma"], ADM["Sample.analysis_area"], ADM["Sample.analysis_area_percentage_stroma"], ADM["Sample.analysis_area_percentage_tumor"], ADM["Sample.analysis_area_percentage_glass"], ADM["Sample.analysis_area_percentage_pigmented_tumor"], ICDC["Sample.non_tumor_tissue_area"], ICDC["Sample.tumor_tissue_area"], ICDC["Sample.percentage_tumor"], ICDC["Sample.percentage_stroma"], ICDC["Sample.analysis_area"], ICDC["Sample.analysis_area_percentage_stroma"], ICDC["Sample.analysis_area_percentage_tumor"], ICDC["Sample.analysis_area_percentage_glass"], ICDC["Sample.analysis_area_percentage_pigmented_tumor"]])

slots.specimen_quality_measure = Slot(uri=SPECIMEN.specimen_quality_measure, name="specimen_quality_measure", curie=SPECIMEN.curie('specimen_quality_measure'),
                      model_uri=SPECIMEN.specimen_quality_measure, domain=None, range=List[Union[dict, DataContainer]], mappings = [ADM["Analyte.a260_a280_ratio"], ADM["Analyte.ribosomal_rna_28s_16s_ratio"], GDC["Analyte.a260_a280_ratio"], GDC["Analyte.ribosomal_rna_28s_16s_ratio"], PDC["Analyte.a260_a280_ratio"], PDC["Analyte.ribosomal_rna_28s_16s_ratio"]])

slots.general_tissue_morphology = Slot(uri=SPECIMEN.general_tissue_morphology, name="general_tissue_morphology", curie=SPECIMEN.curie('general_tissue_morphology'),
                      model_uri=SPECIMEN.general_tissue_morphology, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tissue_type"], GDC["Sample.tissue_type"], PDC["Sample.tissue_type"], ICDC["Sample.general_sample_pathology"]])

slots.specific_tissue_morphology = Slot(uri=SPECIMEN.specific_tissue_morphology, name="specific_tissue_morphology", curie=SPECIMEN.curie('specific_tissue_morphology'),
                      model_uri=SPECIMEN.specific_tissue_morphology, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Sample.tumor_code"], ADM["Sample.tumor_code_id"], ADM["Sample.preinvasive_morphology"], GDC["Sample.tumor_code"], GDC["Sample.tumor_code_id"], PDC["Sample.tumor_code"], PDC["Sample.tumor_code_id"], ICDC["Sample.specific_sample_pathology"], ICDC["Biospecimen.MORPHOLOGY_CODE"], ICDC["Biospecimen.PREINVASIVE_MORPHOLOGY"]])

slots.morphology_pathologically_confirmed = Slot(uri=SPECIMEN.morphology_pathologically_confirmed, name="morphology_pathologically_confirmed", curie=SPECIMEN.curie('morphology_pathologically_confirmed'),
                      model_uri=SPECIMEN.morphology_pathologically_confirmed, domain=None, range=Optional[Bool], mappings = [ADM["Sample.diagnosis_pathologically_confirmed"], GDC["Sample.diagnosis_pathologically_confirmed"], PDC["Sample.diagnosis_pathologically_confirmed"]])

slots.related_document = Slot(uri=SPECIMEN.related_document, name="related_document", curie=SPECIMEN.curie('related_document'),
                      model_uri=SPECIMEN.related_document, domain=None, range=Dict[Union[str, DocumentReferenceId], Union[dict, DocumentReference]], mappings = [ADM["Sample.catalog_reference"], ADM["Sample.distributor_reference"], ADM["Sample.pathology_report_uuid"], ADM["Sample.protocol_id"], GDC["Sample.catalog_reference"], GDC["Sample.distributor_reference"], GDC["Sample.pathology_report_uuid"], PDC["Sample.catalog_reference"], PDC["Sample.distributor_reference"], PDC["Sample.pathology_report_uuid"]])

slots.related_specimen = Slot(uri=SPECIMEN.related_specimen, name="related_specimen", curie=SPECIMEN.curie('related_specimen'),
                      model_uri=SPECIMEN.related_specimen, domain=None, range=List[Union[dict, Relationship]], mappings = [ADM["Sample.next"], ADM["Sample.adjacent_biospecimen"], ICDC["Sample.next"], ICDC["Biospecimen.ADJACENT_BIOSPECIMEN_ID"]])

slots.derived_product = Slot(uri=SPECIMEN.derived_product, name="derived_product", curie=SPECIMEN.curie('derived_product'),
                      model_uri=SPECIMEN.derived_product, domain=None, range=List[Union[dict, BiologicallyDerivedProduct]], mappings = [ADM["Sample.passage_number"], ADM["Sample.growth_rate"], GDC["Sample.passage_count"], GDC["Sample.growth_rate"], PDC["Sample.passage_count"], PDC["Sample.growth_rate"]])

slots.qualification_status_flag = Slot(uri=SPECIMEN.qualification_status_flag, name="qualification_status_flag", curie=SPECIMEN.curie('qualification_status_flag'),
                      model_uri=SPECIMEN.qualification_status_flag, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.status"], PDC["Aliquot.status"]])

slots.reference_status_flag = Slot(uri=SPECIMEN.reference_status_flag, name="reference_status_flag", curie=SPECIMEN.curie('reference_status_flag'),
                      model_uri=SPECIMEN.reference_status_flag, domain=None, range=Optional[Bool], mappings = [ADM["Aliquot.aliquot_is_ref"], PDC["Aliquot.aliquot_is_ref"]])

slots.matched_normal_flag = Slot(uri=SPECIMEN.matched_normal_flag, name="matched_normal_flag", curie=SPECIMEN.curie('matched_normal_flag'),
                      model_uri=SPECIMEN.matched_normal_flag, domain=None, range=List[Union[dict, Coding]], mappings = [ADM["Aliquot.no_matched_normal_targeted_sequencing"], ADM["Aliquot.no_matched_normal_wgs"], ADM["Aliquot.no_matched_normal_wxs"], GDC["Aliquot.no_matched_normal_targeted_sequencing"], GDC["Aliquot.no_matched_normal_wgs"], GDC["Aliquot.no_matched_normal_wxs"]])

slots.selected_normal_flag = Slot(uri=SPECIMEN.selected_normal_flag, name="selected_normal_flag", curie=SPECIMEN.curie('selected_normal_flag'),
                      model_uri=SPECIMEN.selected_normal_flag, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Aliquot.selected_normal_low_pass_wgs"], ADM["Aliquot.selected_normal_targeted_sequencing"], ADM["Aliquot.selected_normal_wgs"], ADM["Aliquot.selected_normal_wxs"], GDC["Aliquot.selected_normal_low_pass_wgs"], GDC["Aliquot.selected_normal_targeted_sequencing"], GDC["Aliquot.selected_normal_wgs"], GDC["Aliquot.selected_normal_wxs"]])

slots.paired_specimen_genotype_match_flag = Slot(uri=SPECIMEN.paired_specimen_genotype_match_flag, name="paired_specimen_genotype_match_flag", curie=SPECIMEN.curie('paired_specimen_genotype_match_flag'),
                      model_uri=SPECIMEN.paired_specimen_genotype_match_flag, domain=None, range=Optional[Union[dict, Coding]], mappings = [ADM["Analyte.normal_tumor_genotype_snp_match"], GDC["Analyte.normal_tumor_genotype_snp_match"], PDC["Analyte.normal_tumor_genotype_snp_match"]])

slots.source_body_structure = Slot(uri=SPECIMEN.source_body_structure, name="source_body_structure", curie=SPECIMEN.curie('source_body_structure'),
                      model_uri=SPECIMEN.source_body_structure, domain=None, range=List[Union[dict, BodyStructure]])

slots.distance_from_paired_specimen = Slot(uri=SPECIMEN.distance_from_paired_specimen, name="distance_from_paired_specimen", curie=SPECIMEN.curie('distance_from_paired_specimen'),
                      model_uri=SPECIMEN.distance_from_paired_specimen, domain=None, range=Optional[Union[str, Literal]], mappings = [ADM["Sample.distance_normal_to_tumor"]])

slots.Specimen_id = Slot(uri=SPECIMEN.id, name="Specimen_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Specimen_id, domain=Specimen, range=Union[str, SpecimenId])

slots.Specimen_identifier = Slot(uri=SPECIMEN.identifier, name="Specimen_identifier", curie=SPECIMEN.curie('identifier'),
                      model_uri=SPECIMEN.Specimen_identifier, domain=Specimen, range=List[Union[dict, Identifier]])

slots.Specimen_description = Slot(uri=SPECIMEN.description, name="Specimen_description", curie=SPECIMEN.curie('description'),
                      model_uri=SPECIMEN.Specimen_description, domain=Specimen, range=Optional[Union[str, Literal]])

slots.Specimen_specimen_type = Slot(uri=SPECIMEN.specimen_type, name="Specimen_specimen_type", curie=SPECIMEN.curie('specimen_type'),
                      model_uri=SPECIMEN.Specimen_specimen_type, domain=Specimen, range=Optional[Union[dict, Coding]])

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

slots.Specimen_subject_diagnosis = Slot(uri=SPECIMEN.subject_diagnosis, name="Specimen_subject_diagnosis", curie=SPECIMEN.curie('subject_diagnosis'),
                      model_uri=SPECIMEN.Specimen_subject_diagnosis, domain=Specimen, range=Dict[Union[str, ConditionDiagnosisId], Union[dict, ConditionDiagnosis]])

slots.Specimen_creation = Slot(uri=SPECIMEN.creation, name="Specimen_creation", curie=SPECIMEN.curie('creation'),
                      model_uri=SPECIMEN.Specimen_creation, domain=Specimen, range=Optional[Union[dict, SpecimenCreationActivity]])

slots.Specimen_processing = Slot(uri=SPECIMEN.processing, name="Specimen_processing", curie=SPECIMEN.curie('processing'),
                      model_uri=SPECIMEN.Specimen_processing, domain=Specimen, range=List[Union[dict, SpecimenProcessingActivity]])

slots.Specimen_storage = Slot(uri=SPECIMEN.storage, name="Specimen_storage", curie=SPECIMEN.curie('storage'),
                      model_uri=SPECIMEN.Specimen_storage, domain=Specimen, range=Optional[Union[dict, SpecimenStorageActivity]])

slots.Specimen_transport = Slot(uri=SPECIMEN.transport, name="Specimen_transport", curie=SPECIMEN.curie('transport'),
                      model_uri=SPECIMEN.Specimen_transport, domain=Specimen, range=Optional[Union[dict, SpecimenTransportActvity]])

slots.Specimen_contained_in = Slot(uri=SPECIMEN.contained_in, name="Specimen_contained_in", curie=SPECIMEN.curie('contained_in'),
                      model_uri=SPECIMEN.Specimen_contained_in, domain=Specimen, range=Optional[Union[dict, SpecimenContainer]])

slots.Specimen_current_weight = Slot(uri=SPECIMEN.current_weight, name="Specimen_current_weight", curie=SPECIMEN.curie('current_weight'),
                      model_uri=SPECIMEN.Specimen_current_weight, domain=Specimen, range=List[Union[dict, Quantity]])

slots.Specimen_volume = Slot(uri=SPECIMEN.volume, name="Specimen_volume", curie=SPECIMEN.curie('volume'),
                      model_uri=SPECIMEN.Specimen_volume, domain=Specimen, range=List[Union[dict, Quantity]])

slots.Specimen_dimensional_measure = Slot(uri=SPECIMEN.dimensional_measure, name="Specimen_dimensional_measure", curie=SPECIMEN.curie('dimensional_measure'),
                      model_uri=SPECIMEN.Specimen_dimensional_measure, domain=Specimen, range=Optional[Union[dict, DataContainer]])

slots.Specimen_analyte_concentration = Slot(uri=SPECIMEN.analyte_concentration, name="Specimen_analyte_concentration", curie=SPECIMEN.curie('analyte_concentration'),
                      model_uri=SPECIMEN.Specimen_analyte_concentration, domain=Specimen, range=Optional[Union[dict, Quantity]])

slots.Specimen_analyte_concentration_method = Slot(uri=SPECIMEN.analyte_concentration_method, name="Specimen_analyte_concentration_method", curie=SPECIMEN.curie('analyte_concentration_method'),
                      model_uri=SPECIMEN.Specimen_analyte_concentration_method, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_cellular_composition = Slot(uri=SPECIMEN.cellular_composition, name="Specimen_cellular_composition", curie=SPECIMEN.curie('cellular_composition'),
                      model_uri=SPECIMEN.Specimen_cellular_composition, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_compositional_measure = Slot(uri=SPECIMEN.compositional_measure, name="Specimen_compositional_measure", curie=SPECIMEN.curie('compositional_measure'),
                      model_uri=SPECIMEN.Specimen_compositional_measure, domain=Specimen, range=Optional[Union[dict, DataContainer]])

slots.Specimen_specimen_quality_measure = Slot(uri=SPECIMEN.specimen_quality_measure, name="Specimen_specimen_quality_measure", curie=SPECIMEN.curie('specimen_quality_measure'),
                      model_uri=SPECIMEN.Specimen_specimen_quality_measure, domain=Specimen, range=List[Union[dict, DataContainer]])

slots.Specimen_general_tissue_morphology = Slot(uri=SPECIMEN.general_tissue_morphology, name="Specimen_general_tissue_morphology", curie=SPECIMEN.curie('general_tissue_morphology'),
                      model_uri=SPECIMEN.Specimen_general_tissue_morphology, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_specific_tissue_morphology = Slot(uri=SPECIMEN.specific_tissue_morphology, name="Specimen_specific_tissue_morphology", curie=SPECIMEN.curie('specific_tissue_morphology'),
                      model_uri=SPECIMEN.Specimen_specific_tissue_morphology, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_morphology_pathologically_confirmed = Slot(uri=SPECIMEN.morphology_pathologically_confirmed, name="Specimen_morphology_pathologically_confirmed", curie=SPECIMEN.curie('morphology_pathologically_confirmed'),
                      model_uri=SPECIMEN.Specimen_morphology_pathologically_confirmed, domain=Specimen, range=Optional[Bool])

slots.Specimen_related_document = Slot(uri=SPECIMEN.related_document, name="Specimen_related_document", curie=SPECIMEN.curie('related_document'),
                      model_uri=SPECIMEN.Specimen_related_document, domain=Specimen, range=Dict[Union[str, DocumentReferenceId], Union[dict, DocumentReference]])

slots.Specimen_related_specimen = Slot(uri=SPECIMEN.related_specimen, name="Specimen_related_specimen", curie=SPECIMEN.curie('related_specimen'),
                      model_uri=SPECIMEN.Specimen_related_specimen, domain=Specimen, range=List[Union[dict, Relationship]])

slots.Specimen_derived_product = Slot(uri=SPECIMEN.derived_product, name="Specimen_derived_product", curie=SPECIMEN.curie('derived_product'),
                      model_uri=SPECIMEN.Specimen_derived_product, domain=Specimen, range=List[Union[dict, BiologicallyDerivedProduct]])

slots.Specimen_qualification_status_flag = Slot(uri=SPECIMEN.qualification_status_flag, name="Specimen_qualification_status_flag", curie=SPECIMEN.curie('qualification_status_flag'),
                      model_uri=SPECIMEN.Specimen_qualification_status_flag, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_reference_status_flag = Slot(uri=SPECIMEN.reference_status_flag, name="Specimen_reference_status_flag", curie=SPECIMEN.curie('reference_status_flag'),
                      model_uri=SPECIMEN.Specimen_reference_status_flag, domain=Specimen, range=Optional[Bool])

slots.Specimen_matched_normal_flag = Slot(uri=SPECIMEN.matched_normal_flag, name="Specimen_matched_normal_flag", curie=SPECIMEN.curie('matched_normal_flag'),
                      model_uri=SPECIMEN.Specimen_matched_normal_flag, domain=Specimen, range=List[Union[dict, Coding]])

slots.Specimen_selected_normal_flag = Slot(uri=SPECIMEN.selected_normal_flag, name="Specimen_selected_normal_flag", curie=SPECIMEN.curie('selected_normal_flag'),
                      model_uri=SPECIMEN.Specimen_selected_normal_flag, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_paired_specimen_genotype_match_flag = Slot(uri=SPECIMEN.paired_specimen_genotype_match_flag, name="Specimen_paired_specimen_genotype_match_flag", curie=SPECIMEN.curie('paired_specimen_genotype_match_flag'),
                      model_uri=SPECIMEN.Specimen_paired_specimen_genotype_match_flag, domain=Specimen, range=Optional[Union[dict, Coding]])

slots.Specimen_source_body_structure = Slot(uri=SPECIMEN.source_body_structure, name="Specimen_source_body_structure", curie=SPECIMEN.curie('source_body_structure'),
                      model_uri=SPECIMEN.Specimen_source_body_structure, domain=Specimen, range=List[Union[dict, BodyStructure]])

slots.Specimen_distance_from_paired_specimen = Slot(uri=SPECIMEN.distance_from_paired_specimen, name="Specimen_distance_from_paired_specimen", curie=SPECIMEN.curie('distance_from_paired_specimen'),
                      model_uri=SPECIMEN.Specimen_distance_from_paired_specimen, domain=Specimen, range=Optional[Union[str, Literal]])
