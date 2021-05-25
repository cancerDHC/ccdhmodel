# Auto generated from ccdhmodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-25 03:29
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
from linkml.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime
from linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CCDH = CurieNamespace('ccdh', 'https://example.org/ccdh/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CCDH


# Types
class CcdhString(String):
    """ A sequence of Unicode characters.  There are no limits on the number of characters in the string. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ccdh_string"
    type_model_uri = CCDH.CcdhString


class CcdhInteger(Integer):
    """ An integer number.  This data type is based on the decimal type, but the fractional component is not allowed.  There are no restrictions on the size of the integer.
 """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "ccdh_integer"
    type_model_uri = CCDH.CcdhInteger


class CcdhDecimal(Decimal):
    """ A rational number that has a decimal representation.  This data type does not restrict the size or precision of the number. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "ccdh_decimal"
    type_model_uri = CCDH.CcdhDecimal


class CcdhBoolean(Boolean):
    """ Value representing either “true” or “false”.  Permissible values (case-sensitive) = “true”, “false”, “1”, “0”. """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "ccdh_boolean"
    type_model_uri = CCDH.CcdhBoolean


class CcdhDateTime(Datetime):
    """ A date and time string specified using a specialized concatenation of the date and time data types, in the general format YYYY-MM-DDThh:mm:ss+zz:zz.   """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "ccdh_dateTime"
    type_model_uri = CCDH.CcdhDateTime


class CcdhCurie(Uriorcurie):
    """  A compact URI (CURIE), which is a bipartite identifier of the form prefix:reference, in which the prefix is a convenient abbreviation of a URI.  It is expressed in the format “prefix:reference”. When a mapping of prefix to base URI is provided (external to this data type), a CURIE may be mapped to a URI. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ccdh_curie"
    type_model_uri = CCDH.CcdhCurie


class CcdhCode(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ccdh_code"
    type_model_uri = CCDH.CcdhCode


# Class references



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

    id: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BodySite(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BodySite
    class_class_curie: ClassVar[str] = "ccdh:BodySite"
    class_name: ClassVar[str] = "BodySite"
    class_model_uri: ClassVar[URIRef] = CCDH.BodySite

    site: Union[dict, "CodeableConcept"] = None
    qualifier: Optional[Union[Union[dict, "CodeableConcept"], List[Union[dict, "CodeableConcept"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.site is None:
            raise ValueError("site must be supplied")
        if not isinstance(self.site, CodeableConcept):
            self.site = CodeableConcept(**self.site)

        if self.qualifier is None:
            self.qualifier = []
        if not isinstance(self.qualifier, list):
            self.qualifier = [self.qualifier]
        self.qualifier = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.qualifier]

        super().__post_init__(**kwargs)


@dataclass
class BiologicallyDerivedProduct(Entity):
    """
    A living organism, or a metabolocally active biological system such as a cell culture, tissue culture, or organoid
    that is maintained or propagated in vitro.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedProduct
    class_class_curie: ClassVar[str] = "ccdh:BiologicallyDerivedProduct"
    class_name: ClassVar[str] = "BiologicallyDerivedProduct"
    class_model_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedProduct

    id: Optional[Union[str, CcdhString]] = None
    description: Optional[Union[str, CcdhString]] = None
    product_type: Optional[Union[dict, "CodeableConcept"]] = None
    passage_number: Optional[Union[Union[int, CcdhInteger], List[Union[int, CcdhInteger]]]] = empty_list()
    growth_rate: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.product_type is not None and not isinstance(self.product_type, CodeableConcept):
            self.product_type = CodeableConcept(**self.product_type)

        if self.passage_number is None:
            self.passage_number = []
        if not isinstance(self.passage_number, list):
            self.passage_number = [self.passage_number]
        self.passage_number = [v if isinstance(v, CcdhInteger) else CcdhInteger(v) for v in self.passage_number]

        if self.growth_rate is None:
            self.growth_rate = []
        if not isinstance(self.growth_rate, list):
            self.growth_rate = [self.growth_rate]
        self.growth_rate = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.growth_rate]

        super().__post_init__(**kwargs)


@dataclass
class CancerGrade(Entity):
    """
    A structured object to hold related data items about the grade of cancer (e.g. overall, primary gleason, secondary
    gleason, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerGrade
    class_class_curie: ClassVar[str] = "ccdh:CancerGrade"
    class_name: ClassVar[str] = "CancerGrade"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerGrade

    method_type: Optional[Union[dict, "CodeableConcept"]] = None
    observations: Optional[Union[Union[dict, "CancerGrade"], List[Union[dict, "CancerGrade"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**self.method_type)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self.observations = [v if isinstance(v, CancerGrade) else CancerGrade(**v) for v in self.observations]

        super().__post_init__(**kwargs)


@dataclass
class CancerStage(Entity):
    """
    A data structure with key (observation_type) and value (valueCodeableConcept) attributes that represents a single
    cancer staging observation, such as the Clinical Metastasis (M) component of a clinical TNM staging.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerStage
    class_class_curie: ClassVar[str] = "ccdh:CancerStage"
    class_name: ClassVar[str] = "CancerStage"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerStage

    observation_type: Union[dict, "CodeableConcept"] = None
    valueCodeableConcept: Optional[Union[dict, "CodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**self.observation_type)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CodeableConcept):
            self.valueCodeableConcept = CodeableConcept(**self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class CancerStageSet(Entity):
    """
    A structured object to hold related data items about the staging of cancer (e.g. overall, T, N, and M components
    of a Cancer Staging observation).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerStageSet
    class_class_curie: ClassVar[str] = "ccdh:CancerStageSet"
    class_name: ClassVar[str] = "CancerStageSet"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerStageSet

    method_type: Optional[Union[dict, "CodeableConcept"]] = None
    observations: Optional[Union[Union[dict, CancerStage], List[Union[dict, CancerStage]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**self.method_type)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self._normalize_inlined_slot(slot_name="observations", slot_type=CancerStage, key_name="observation_type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class CodeableConcept(Entity):
    """
    A representation of a concept that may be defined by or mapped to one or more codes in code systems
    (terminologies, ontologies, dictionaries, code sets, etc) - but may also be defined by the provision of text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CodeableConcept
    class_class_curie: ClassVar[str] = "ccdh:CodeableConcept"
    class_name: ClassVar[str] = "CodeableConcept"
    class_model_uri: ClassVar[URIRef] = CCDH.CodeableConcept

    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    text: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.coding is None:
            self.coding = []
        if not isinstance(self.coding, list):
            self.coding = [self.coding]
        self._normalize_inlined_slot(slot_name="coding", slot_type=Coding, key_name="code", inlined_as_list=True, keyed=False)

        if self.text is not None and not isinstance(self.text, CcdhString):
            self.text = CcdhString(self.text)

        super().__post_init__(**kwargs)


@dataclass
class Coding(Entity):
    """
    A structured representation of a coded/enumerated data value, that includes additional metadata about the code and
    code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Coding
    class_class_curie: ClassVar[str] = "ccdh:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = CCDH.Coding

    code: Union[str, CcdhString] = None
    system: Union[str, CcdhString] = None
    label: Optional[Union[str, CcdhString]] = None
    systemURL: Optional[Union[str, CcdhString]] = None
    systemVersion: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.code is None:
            raise ValueError("code must be supplied")
        if not isinstance(self.code, CcdhString):
            self.code = CcdhString(self.code)

        if self.system is None:
            raise ValueError("system must be supplied")
        if not isinstance(self.system, CcdhString):
            self.system = CcdhString(self.system)

        if self.label is not None and not isinstance(self.label, CcdhString):
            self.label = CcdhString(self.label)

        if self.systemURL is not None and not isinstance(self.systemURL, CcdhString):
            self.systemURL = CcdhString(self.systemURL)

        if self.systemVersion is not None and not isinstance(self.systemVersion, CcdhString):
            self.systemVersion = CcdhString(self.systemVersion)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenContainer(Entity):
    """
    A vessel in which a specimen is held or attached - to store or as a substrate for growth (e.g. a cell culture
    dish) or analysis (e.g. a microscope slide or 96-well plate)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenContainer
    class_class_curie: ClassVar[str] = "ccdh:SpecimenContainer"
    class_name: ClassVar[str] = "SpecimenContainer"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenContainer

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    container_type: Optional[Union[dict, CodeableConcept]] = None
    container_number: Optional[Union[str, CcdhString]] = None
    additive: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    parent_container: Optional[Union[Union[dict, "SpecimenContainer"], List[Union[dict, "SpecimenContainer"]]]] = empty_list()
    charge_type: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.container_type is not None and not isinstance(self.container_type, CodeableConcept):
            self.container_type = CodeableConcept(**self.container_type)

        if self.container_number is not None and not isinstance(self.container_number, CcdhString):
            self.container_number = CcdhString(self.container_number)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Entity) else Entity(**v) for v in self.additive]

        if self.parent_container is None:
            self.parent_container = []
        if not isinstance(self.parent_container, list):
            self.parent_container = [self.parent_container]
        self.parent_container = [v if isinstance(v, SpecimenContainer) else SpecimenContainer(**v) for v in self.parent_container]

        if self.charge_type is not None and not isinstance(self.charge_type, CodeableConcept):
            self.charge_type = CodeableConcept(**self.charge_type)

        super().__post_init__(**kwargs)


@dataclass
class Diagnosis(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Diagnosis
    class_class_curie: ClassVar[str] = "ccdh:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = CCDH.Diagnosis

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    age_at_diagnosis: Optional[Union[dict, "Quantity"]] = None
    year_at_diagnosis: Optional[Union[int, CcdhInteger]] = None
    condition: Optional[Union[dict, CodeableConcept]] = None
    primary_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    metastatic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    stage: Optional[Union[Union[dict, CancerStageSet], List[Union[dict, CancerStageSet]]]] = empty_list()
    grade: Optional[Union[Union[dict, CancerGrade], List[Union[dict, CancerGrade]]]] = empty_list()
    morphology: Optional[Union[dict, CodeableConcept]] = None
    disease_status: Optional[Union[dict, CodeableConcept]] = None
    prior_diagnosis: Optional[Union[dict, "Diagnosis"]] = None
    method_of_diagnosis: Optional[Union[dict, CodeableConcept]] = None
    related_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.age_at_diagnosis is not None and not isinstance(self.age_at_diagnosis, Quantity):
            self.age_at_diagnosis = Quantity(**self.age_at_diagnosis)

        if self.year_at_diagnosis is not None and not isinstance(self.year_at_diagnosis, CcdhInteger):
            self.year_at_diagnosis = CcdhInteger(self.year_at_diagnosis)

        if self.condition is not None and not isinstance(self.condition, CodeableConcept):
            self.condition = CodeableConcept(**self.condition)

        if self.primary_site is None:
            self.primary_site = []
        if not isinstance(self.primary_site, list):
            self.primary_site = [self.primary_site]
        self._normalize_inlined_slot(slot_name="primary_site", slot_type=BodySite, key_name="site", inlined_as_list=True, keyed=False)

        if self.metastatic_site is None:
            self.metastatic_site = []
        if not isinstance(self.metastatic_site, list):
            self.metastatic_site = [self.metastatic_site]
        self._normalize_inlined_slot(slot_name="metastatic_site", slot_type=BodySite, key_name="site", inlined_as_list=True, keyed=False)

        if self.stage is None:
            self.stage = []
        if not isinstance(self.stage, list):
            self.stage = [self.stage]
        self.stage = [v if isinstance(v, CancerStageSet) else CancerStageSet(**v) for v in self.stage]

        if self.grade is None:
            self.grade = []
        if not isinstance(self.grade, list):
            self.grade = [self.grade]
        self.grade = [v if isinstance(v, CancerGrade) else CancerGrade(**v) for v in self.grade]

        if self.morphology is not None and not isinstance(self.morphology, CodeableConcept):
            self.morphology = CodeableConcept(**self.morphology)

        if self.disease_status is not None and not isinstance(self.disease_status, CodeableConcept):
            self.disease_status = CodeableConcept(**self.disease_status)

        if self.prior_diagnosis is not None and not isinstance(self.prior_diagnosis, Diagnosis):
            self.prior_diagnosis = Diagnosis(**self.prior_diagnosis)

        if self.method_of_diagnosis is not None and not isinstance(self.method_of_diagnosis, CodeableConcept):
            self.method_of_diagnosis = CodeableConcept(**self.method_of_diagnosis)

        if self.related_specimen is None:
            self.related_specimen = []
        if not isinstance(self.related_specimen, list):
            self.related_specimen = [self.related_specimen]
        self.related_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.related_specimen]

        super().__post_init__(**kwargs)


@dataclass
class Document(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Document
    class_class_curie: ClassVar[str] = "ccdh:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = CCDH.Document

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    document_type: Optional[Union[dict, CodeableConcept]] = None
    description: Optional[Union[str, CcdhString]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    url: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.document_type is not None and not isinstance(self.document_type, CodeableConcept):
            self.document_type = CodeableConcept(**self.document_type)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity(**self.focus)

        if self.url is None:
            self.url = []
        if not isinstance(self.url, list):
            self.url = [self.url]
        self.url = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.url]

        super().__post_init__(**kwargs)


@dataclass
class Exposure(Entity):
    """
    Contact between an agent and a target. A state of contact or close proximity to a medicinal product, chemical,
    pathogen, radioisotope or other substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Exposure
    class_class_curie: ClassVar[str] = "ccdh:Exposure"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = CCDH.Exposure

    id: Union[str, CcdhString] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    tobacco_use: Optional[Union[dict, Entity]] = None
    alcohol_use: Optional[Union[dict, Entity]] = None
    environmental: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()
    related_patient: Optional[Union[dict, "Subject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.tobacco_use is not None and not isinstance(self.tobacco_use, Entity):
            self.tobacco_use = Entity(**self.tobacco_use)

        if self.alcohol_use is not None and not isinstance(self.alcohol_use, Entity):
            self.alcohol_use = Entity(**self.alcohol_use)

        if self.environmental is None:
            self.environmental = []
        if not isinstance(self.environmental, list):
            self.environmental = [self.environmental]
        self._normalize_inlined_slot(slot_name="environmental", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

        if self.related_patient is not None and not isinstance(self.related_patient, Subject):
            self.related_patient = Subject(**self.related_patient)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(Entity):
    """
    An Identifier is associated with a unique object or entity within a given system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Identifier
    class_class_curie: ClassVar[str] = "ccdh:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CCDH.Identifier

    value: Union[str, CcdhString] = None
    system: Optional[Union[str, CcdhString]] = None
    type: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is None:
            raise ValueError("value must be supplied")
        if not isinstance(self.value, CcdhString):
            self.value = CcdhString(self.value)

        if self.system is not None and not isinstance(self.system, CcdhString):
            self.system = CcdhString(self.system)

        if self.type is not None and not isinstance(self.type, CodeableConcept):
            self.type = CodeableConcept(**self.type)

        super().__post_init__(**kwargs)


@dataclass
class Observation(Entity):
    """
    A structured object that describes a single data item about an entity, as generated through a point-in-time
    observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Observation
    class_class_curie: ClassVar[str] = "ccdh:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = CCDH.Observation

    id: Union[str, CcdhString] = None
    category: Union[dict, CodeableConcept] = None
    observation_type: Union[dict, CodeableConcept] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    patient: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[Decimal, CcdhDecimal]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[Decimal, CcdhDecimal]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        if not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**self.category)

        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**self.observation_type)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.method_type]

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.patient is not None and not isinstance(self.patient, Subject):
            self.patient = Subject(**self.patient)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity(**self.valueEntity)

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhDecimal):
            self.valueInteger = CcdhDecimal(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDecimal):
            self.valueDateTime = CcdhDecimal(self.valueDateTime)

        super().__post_init__(**kwargs)


@dataclass
class Organization(Entity):
    """
    A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or
    an institute within a university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Organization
    class_class_curie: ClassVar[str] = "ccdh:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = CCDH.Organization

    id: Union[str, CcdhString] = None
    name: Union[str, CcdhString] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    alias: Optional[Union[str, CcdhString]] = None
    organization_type: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.name is None:
            raise ValueError("name must be supplied")
        if not isinstance(self.name, CcdhString):
            self.name = CcdhString(self.name)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.alias is not None and not isinstance(self.alias, CcdhString):
            self.alias = CcdhString(self.alias)

        if self.organization_type is not None and not isinstance(self.organization_type, CcdhString):
            self.organization_type = CcdhString(self.organization_type)

        super().__post_init__(**kwargs)


@dataclass
class Quantity(Entity):
    """
    A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including
    a value and unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Quantity
    class_class_curie: ClassVar[str] = "ccdh:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = CCDH.Quantity

    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueCodeableConcept: Optional[Union[dict, CodeableConcept]] = None
    unitCode: Optional[Union[dict, Coding]] = None
    unit: Optional[Union[str, CcdhString]] = None
    comparator: Optional[Union[dict, Coding]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CodeableConcept):
            self.valueCodeableConcept = CodeableConcept(**self.valueCodeableConcept)

        if self.unitCode is not None and not isinstance(self.unitCode, Coding):
            self.unitCode = Coding(**self.unitCode)

        if self.unit is not None and not isinstance(self.unit, CcdhString):
            self.unit = CcdhString(self.unit)

        if self.comparator is not None and not isinstance(self.comparator, Coding):
            self.comparator = Coding(**self.comparator)

        super().__post_init__(**kwargs)


@dataclass
class ResearchProject(Entity):
    """
    A process where a researcher or organization plans and then executes a series of steps intended to increase the
    field of healthcare-related knowledge.
    This includes studies of safety, efficacy, comparative effectiveness and other information about medications,
    devices, therapies and other interventional
    and investigative techniques. A ResearchProject involves the gathering of information about human or animal
    subjects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ResearchProject
    class_class_curie: ClassVar[str] = "ccdh:ResearchProject"
    class_name: ClassVar[str] = "ResearchProject"
    class_model_uri: ClassVar[URIRef] = CCDH.ResearchProject

    research_project_type: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CcdhString]] = None
    name_shortened: Optional[Union[str, CcdhString]] = None
    description: Optional[Union[str, CcdhString]] = None
    description_shortened: Optional[Union[str, CcdhString]] = None
    sponsor: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    primary_anatomic_site: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    url: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ResearchProject"], List[Union[dict, "ResearchProject"]]]] = empty_list()
    date_iacuc_approval: Optional[Union[str, CcdhDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.research_project_type is None:
            raise ValueError("research_project_type must be supplied")
        if not isinstance(self.research_project_type, CodeableConcept):
            self.research_project_type = CodeableConcept(**self.research_project_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.name is not None and not isinstance(self.name, CcdhString):
            self.name = CcdhString(self.name)

        if self.name_shortened is not None and not isinstance(self.name_shortened, CcdhString):
            self.name_shortened = CcdhString(self.name_shortened)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.description_shortened is not None and not isinstance(self.description_shortened, CcdhString):
            self.description_shortened = CcdhString(self.description_shortened)

        if self.sponsor is None:
            self.sponsor = []
        if not isinstance(self.sponsor, list):
            self.sponsor = [self.sponsor]
        self.sponsor = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.sponsor]

        if self.date_started is not None and not isinstance(self.date_started, CcdhDateTime):
            self.date_started = CcdhDateTime(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, CcdhDateTime):
            self.date_ended = CcdhDateTime(self.date_ended)

        if self.primary_anatomic_site is None:
            self.primary_anatomic_site = []
        if not isinstance(self.primary_anatomic_site, list):
            self.primary_anatomic_site = [self.primary_anatomic_site]
        self.primary_anatomic_site = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.primary_anatomic_site]

        if self.url is None:
            self.url = []
        if not isinstance(self.url, list):
            self.url = [self.url]
        self.url = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.url]

        if self.part_of is None:
            self.part_of = []
        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of]
        self._normalize_inlined_slot(slot_name="part_of", slot_type=ResearchProject, key_name="research_project_type", inlined_as_list=True, keyed=False)

        if self.date_iacuc_approval is not None and not isinstance(self.date_iacuc_approval, CcdhDateTime):
            self.date_iacuc_approval = CcdhDateTime(self.date_iacuc_approval)

        super().__post_init__(**kwargs)


@dataclass
class ResearchSubject(Entity):
    """
    A research subject is the entity of interest in a research study, typically a human being or an animal, but can
    also be a device, group of humans or animals,
    or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the
    subject’s privacy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ResearchSubject
    class_class_curie: ClassVar[str] = "ccdh:ResearchSubject"
    class_name: ClassVar[str] = "ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CCDH.ResearchSubject

    id: Union[str, CcdhString] = None
    associated_subject: Union[dict, "Subject"] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    description: Optional[Union[str, CcdhString]] = None
    member_of_research_project: Optional[Union[Union[dict, ResearchProject], List[Union[dict, ResearchProject]]]] = empty_list()
    age_at_enrollment: Optional[Union[dict, Quantity]] = None
    primary_diagnosis_condition: Optional[Union[dict, CodeableConcept]] = None
    primary_diagnosis_site: Optional[Union[dict, CodeableConcept]] = None
    primary_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    comorbid_diagnoses: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    index_timepoint: Optional[Union[dict, CodeableConcept]] = None
    originating_site: Optional[Union[dict, Organization]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.associated_subject is None:
            raise ValueError("associated_subject must be supplied")
        if not isinstance(self.associated_subject, Subject):
            self.associated_subject = Subject(**self.associated_subject)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.member_of_research_project is None:
            self.member_of_research_project = []
        if not isinstance(self.member_of_research_project, list):
            self.member_of_research_project = [self.member_of_research_project]
        self._normalize_inlined_slot(slot_name="member_of_research_project", slot_type=ResearchProject, key_name="research_project_type", inlined_as_list=True, keyed=False)

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, Quantity):
            self.age_at_enrollment = Quantity(**self.age_at_enrollment)

        if self.primary_diagnosis_condition is not None and not isinstance(self.primary_diagnosis_condition, CodeableConcept):
            self.primary_diagnosis_condition = CodeableConcept(**self.primary_diagnosis_condition)

        if self.primary_diagnosis_site is not None and not isinstance(self.primary_diagnosis_site, CodeableConcept):
            self.primary_diagnosis_site = CodeableConcept(**self.primary_diagnosis_site)

        if self.primary_diagnosis is None:
            self.primary_diagnosis = []
        if not isinstance(self.primary_diagnosis, list):
            self.primary_diagnosis = [self.primary_diagnosis]
        self.primary_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.primary_diagnosis]

        if self.comorbid_diagnoses is None:
            self.comorbid_diagnoses = []
        if not isinstance(self.comorbid_diagnoses, list):
            self.comorbid_diagnoses = [self.comorbid_diagnoses]
        self.comorbid_diagnoses = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.comorbid_diagnoses]

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, CodeableConcept):
            self.index_timepoint = CodeableConcept(**self.index_timepoint)

        if self.originating_site is not None and not isinstance(self.originating_site, Organization):
            self.originating_site = Organization(**self.originating_site)

        super().__post_init__(**kwargs)


@dataclass
class Specimen(Entity):
    """
    Any material taken as a sample from a biological entity (living or dead), or from a physical object or the
    environment. Specimens are usually collected as an example of their kind, often for use in some investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Specimen
    class_class_curie: ClassVar[str] = "ccdh:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CCDH.Specimen

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    description: Optional[Union[str, CcdhString]] = None
    specimen_type: Optional[Union[dict, CodeableConcept]] = None
    analyte_type: Optional[Union[dict, CodeableConcept]] = None
    associated_project: Optional[Union[dict, ResearchProject]] = None
    data_provider: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[dict, CodeableConcept]] = None
    parent_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    source_subject: Optional[Union[dict, "Subject"]] = None
    source_model_system: Optional[Union[dict, Entity]] = None
    condition_status_at_collection: Optional[Union[dict, CodeableConcept]] = None
    creation_activity: Optional[Union[dict, "SpecimenCreationActivity"]] = None
    processing_activity: Optional[Union[Union[dict, "SpecimenProcessingActivity"], List[Union[dict, "SpecimenProcessingActivity"]]]] = empty_list()
    storage_activity: Optional[Union[dict, "SpecimenStorageActivity"]] = None
    transport_activity: Optional[Union[dict, "SpecimenTransportActivity"]] = None
    contained_in: Optional[Union[dict, SpecimenContainer]] = None
    dimensional_measure: Optional[Union[dict, Entity]] = None
    quantity_measure: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    quality_measure: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    cellular_composition_type: Optional[Union[dict, CodeableConcept]] = None
    cellular_composition_measure: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    tissue_composition_measure: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    general_tissue_morphology: Optional[Union[dict, CodeableConcept]] = None
    specific_tissue_morphology: Optional[Union[dict, CodeableConcept]] = None
    preinvasive_tissue_morphology: Optional[Union[dict, CodeableConcept]] = None
    morphology_pathologically_confirmed: Optional[Union[bool, CcdhBoolean]] = None
    morphology_assessor_role: Optional[Union[dict, CodeableConcept]] = None
    morphlogy_assessment_method: Optional[Union[dict, CodeableConcept]] = None
    degree_of_dysplasia: Optional[Union[dict, CodeableConcept]] = None
    dysplasia_fraction: Optional[Union[str, CcdhString]] = None
    related_document: Optional[Union[Union[dict, Document], List[Union[dict, Document]]]] = empty_list()
    section_location: Optional[Union[dict, CodeableConcept]] = None
    derived_product: Optional[Union[Union[dict, BiologicallyDerivedProduct], List[Union[dict, BiologicallyDerivedProduct]]]] = empty_list()
    distance_from_paired_specimen: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.specimen_type is not None and not isinstance(self.specimen_type, CodeableConcept):
            self.specimen_type = CodeableConcept(**self.specimen_type)

        if self.analyte_type is not None and not isinstance(self.analyte_type, CodeableConcept):
            self.analyte_type = CodeableConcept(**self.analyte_type)

        if self.associated_project is not None and not isinstance(self.associated_project, ResearchProject):
            self.associated_project = ResearchProject(**self.associated_project)

        if self.data_provider is not None and not isinstance(self.data_provider, Organization):
            self.data_provider = Organization(**self.data_provider)

        if self.source_material_type is not None and not isinstance(self.source_material_type, CodeableConcept):
            self.source_material_type = CodeableConcept(**self.source_material_type)

        if self.parent_specimen is None:
            self.parent_specimen = []
        if not isinstance(self.parent_specimen, list):
            self.parent_specimen = [self.parent_specimen]
        self.parent_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.parent_specimen]

        if self.source_subject is not None and not isinstance(self.source_subject, Subject):
            self.source_subject = Subject(**self.source_subject)

        if self.source_model_system is not None and not isinstance(self.source_model_system, Entity):
            self.source_model_system = Entity(**self.source_model_system)

        if self.condition_status_at_collection is not None and not isinstance(self.condition_status_at_collection, CodeableConcept):
            self.condition_status_at_collection = CodeableConcept(**self.condition_status_at_collection)

        if self.creation_activity is not None and not isinstance(self.creation_activity, SpecimenCreationActivity):
            self.creation_activity = SpecimenCreationActivity(**self.creation_activity)

        if self.processing_activity is None:
            self.processing_activity = []
        if not isinstance(self.processing_activity, list):
            self.processing_activity = [self.processing_activity]
        self.processing_activity = [v if isinstance(v, SpecimenProcessingActivity) else SpecimenProcessingActivity(**v) for v in self.processing_activity]

        if self.storage_activity is not None and not isinstance(self.storage_activity, SpecimenStorageActivity):
            self.storage_activity = SpecimenStorageActivity(**self.storage_activity)

        if self.transport_activity is not None and not isinstance(self.transport_activity, SpecimenTransportActivity):
            self.transport_activity = SpecimenTransportActivity(**self.transport_activity)

        if self.contained_in is not None and not isinstance(self.contained_in, SpecimenContainer):
            self.contained_in = SpecimenContainer(**self.contained_in)

        if self.dimensional_measure is not None and not isinstance(self.dimensional_measure, Entity):
            self.dimensional_measure = Entity(**self.dimensional_measure)

        if self.quantity_measure is None:
            self.quantity_measure = []
        if not isinstance(self.quantity_measure, list):
            self.quantity_measure = [self.quantity_measure]
        self.quantity_measure = [v if isinstance(v, Entity) else Entity(**v) for v in self.quantity_measure]

        if self.quality_measure is None:
            self.quality_measure = []
        if not isinstance(self.quality_measure, list):
            self.quality_measure = [self.quality_measure]
        self.quality_measure = [v if isinstance(v, Entity) else Entity(**v) for v in self.quality_measure]

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, CodeableConcept):
            self.cellular_composition_type = CodeableConcept(**self.cellular_composition_type)

        if self.cellular_composition_measure is None:
            self.cellular_composition_measure = []
        if not isinstance(self.cellular_composition_measure, list):
            self.cellular_composition_measure = [self.cellular_composition_measure]
        self.cellular_composition_measure = [v if isinstance(v, Entity) else Entity(**v) for v in self.cellular_composition_measure]

        if self.tissue_composition_measure is None:
            self.tissue_composition_measure = []
        if not isinstance(self.tissue_composition_measure, list):
            self.tissue_composition_measure = [self.tissue_composition_measure]
        self.tissue_composition_measure = [v if isinstance(v, Entity) else Entity(**v) for v in self.tissue_composition_measure]

        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, CodeableConcept):
            self.general_tissue_morphology = CodeableConcept(**self.general_tissue_morphology)

        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, CodeableConcept):
            self.specific_tissue_morphology = CodeableConcept(**self.specific_tissue_morphology)

        if self.preinvasive_tissue_morphology is not None and not isinstance(self.preinvasive_tissue_morphology, CodeableConcept):
            self.preinvasive_tissue_morphology = CodeableConcept(**self.preinvasive_tissue_morphology)

        if self.morphology_pathologically_confirmed is not None and not isinstance(self.morphology_pathologically_confirmed, CcdhBoolean):
            self.morphology_pathologically_confirmed = CcdhBoolean(self.morphology_pathologically_confirmed)

        if self.morphology_assessor_role is not None and not isinstance(self.morphology_assessor_role, CodeableConcept):
            self.morphology_assessor_role = CodeableConcept(**self.morphology_assessor_role)

        if self.morphlogy_assessment_method is not None and not isinstance(self.morphlogy_assessment_method, CodeableConcept):
            self.morphlogy_assessment_method = CodeableConcept(**self.morphlogy_assessment_method)

        if self.degree_of_dysplasia is not None and not isinstance(self.degree_of_dysplasia, CodeableConcept):
            self.degree_of_dysplasia = CodeableConcept(**self.degree_of_dysplasia)

        if self.dysplasia_fraction is not None and not isinstance(self.dysplasia_fraction, CcdhString):
            self.dysplasia_fraction = CcdhString(self.dysplasia_fraction)

        if self.related_document is None:
            self.related_document = []
        if not isinstance(self.related_document, list):
            self.related_document = [self.related_document]
        self.related_document = [v if isinstance(v, Document) else Document(**v) for v in self.related_document]

        if self.section_location is not None and not isinstance(self.section_location, CodeableConcept):
            self.section_location = CodeableConcept(**self.section_location)

        if self.derived_product is None:
            self.derived_product = []
        if not isinstance(self.derived_product, list):
            self.derived_product = [self.derived_product]
        self.derived_product = [v if isinstance(v, BiologicallyDerivedProduct) else BiologicallyDerivedProduct(**v) for v in self.derived_product]

        if self.distance_from_paired_specimen is not None and not isinstance(self.distance_from_paired_specimen, Quantity):
            self.distance_from_paired_specimen = Quantity(**self.distance_from_paired_specimen)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenCreationActivity(Entity):
    """
    The process of creating a specimen through observing and/or removing material from an biological source or natural
    setting (e.g. from a person, animal, cell line, or environmental material), or through derivation from an existing
    specimen (e.g. through portioning or aliquoting). This activity represents the entire process up to the point
    where the specimen is physically modified, stored, or transported.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenCreationActivity"
    class_name: ClassVar[str] = "SpecimenCreationActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity

    activity_type: Optional[Union[dict, CodeableConcept]] = None
    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    collection_method_type: Optional[Union[dict, CodeableConcept]] = None
    derivation_method_type: Optional[Union[dict, CodeableConcept]] = None
    additive: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    collection_site: Optional[Union[dict, BodySite]] = None
    input_specimen: Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]] = empty_list()
    quantity_collected: Optional[Union[dict, Quantity]] = None
    execution_condition: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    specimen_order: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CodeableConcept):
            self.activity_type = CodeableConcept(**self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, CcdhDateTime):
            self.date_started = CcdhDateTime(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, CcdhDateTime):
            self.date_ended = CcdhDateTime(self.date_ended)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.collection_method_type is not None and not isinstance(self.collection_method_type, CodeableConcept):
            self.collection_method_type = CodeableConcept(**self.collection_method_type)

        if self.derivation_method_type is not None and not isinstance(self.derivation_method_type, CodeableConcept):
            self.derivation_method_type = CodeableConcept(**self.derivation_method_type)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Entity) else Entity(**v) for v in self.additive]

        if self.collection_site is not None and not isinstance(self.collection_site, BodySite):
            self.collection_site = BodySite(**self.collection_site)

        if self.input_specimen is None:
            self.input_specimen = []
        if not isinstance(self.input_specimen, list):
            self.input_specimen = [self.input_specimen]
        self.input_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.input_specimen]

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, Quantity):
            self.quantity_collected = Quantity(**self.quantity_collected)

        if self.execution_condition is None:
            self.execution_condition = []
        if not isinstance(self.execution_condition, list):
            self.execution_condition = [self.execution_condition]
        self.execution_condition = [v if isinstance(v, Entity) else Entity(**v) for v in self.execution_condition]

        if self.specimen_order is not None and not isinstance(self.specimen_order, CcdhString):
            self.specimen_order = CcdhString(self.specimen_order)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenProcessingActivity(Entity):
    """
    An activity that modifies the physical structure, composition, or state of a specimen. Unlike SpecimenCreation,
    SpecimenProcessing activities do not result in the generation of new entities - they take a single specimen as
    input, and output that same specimen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenProcessingActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenProcessingActivity"
    class_name: ClassVar[str] = "SpecimenProcessingActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenProcessingActivity

    activity_type: Optional[Union[dict, CodeableConcept]] = None
    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    duration: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    additive: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    device: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    executionConditions: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CodeableConcept):
            self.activity_type = CodeableConcept(**self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, CcdhDateTime):
            self.date_started = CcdhDateTime(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, CcdhDateTime):
            self.date_ended = CcdhDateTime(self.date_ended)

        if self.duration is None:
            self.duration = []
        if not isinstance(self.duration, list):
            self.duration = [self.duration]
        self.duration = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**self.method_type)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Entity) else Entity(**v) for v in self.additive]

        if self.device is None:
            self.device = []
        if not isinstance(self.device, list):
            self.device = [self.device]
        self.device = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.device]

        if self.executionConditions is None:
            self.executionConditions = []
        if not isinstance(self.executionConditions, list):
            self.executionConditions = [self.executionConditions]
        self.executionConditions = [v if isinstance(v, Entity) else Entity(**v) for v in self.executionConditions]

        super().__post_init__(**kwargs)


@dataclass
class SpecimenStorageActivity(Entity):
    """
    An activity in which a specimen is stored or maintained in a particular location, container, or state. Unlike
    'processing' activities, storage does not alter the
    intrinsic physical nature of a specimen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenStorageActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenStorageActivity"
    class_name: ClassVar[str] = "SpecimenStorageActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenStorageActivity

    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    container: Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, CcdhDateTime):
            self.date_started = CcdhDateTime(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, CcdhDateTime):
            self.date_ended = CcdhDateTime(self.date_ended)

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**self.method_type)

        if self.container is None:
            self.container = []
        if not isinstance(self.container, list):
            self.container = [self.container]
        self.container = [v if isinstance(v, SpecimenContainer) else SpecimenContainer(**v) for v in self.container]

        super().__post_init__(**kwargs)


@dataclass
class SpecimenTransportActivity(Entity):
    """
    An activity through which a specimen is transported between locations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenTransportActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenTransportActivity"
    class_name: ClassVar[str] = "SpecimenTransportActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenTransportActivity

    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    transport_destination: Optional[Union[dict, Organization]] = None
    execution_conditions: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, CcdhDateTime):
            self.date_started = CcdhDateTime(self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, CcdhDateTime):
            self.date_ended = CcdhDateTime(self.date_ended)

        if self.transport_destination is not None and not isinstance(self.transport_destination, Organization):
            self.transport_destination = Organization(**self.transport_destination)

        if self.execution_conditions is None:
            self.execution_conditions = []
        if not isinstance(self.execution_conditions, list):
            self.execution_conditions = [self.execution_conditions]
        self.execution_conditions = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.execution_conditions]

        super().__post_init__(**kwargs)


@dataclass
class Subject(Entity):
    """
    Demographics and other administrative information about an individual or animal receiving care or other
    health-related services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Subject
    class_class_curie: ClassVar[str] = "ccdh:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CCDH.Subject

    id: Union[str, CcdhString] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    species: Optional[Union[dict, CodeableConcept]] = None
    breed: Optional[Union[dict, CodeableConcept]] = None
    sex: Optional[Union[dict, CodeableConcept]] = None
    ethnicity: Optional[Union[dict, CodeableConcept]] = None
    race: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    year_of_birth: Optional[Union[int, CcdhInteger]] = None
    vital_status: Optional[Union[dict, CodeableConcept]] = None
    age_at_death: Optional[Union[dict, Quantity]] = None
    year_of_death: Optional[Union[int, CcdhInteger]] = None
    cause_of_death: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.species is not None and not isinstance(self.species, CodeableConcept):
            self.species = CodeableConcept(**self.species)

        if self.breed is not None and not isinstance(self.breed, CodeableConcept):
            self.breed = CodeableConcept(**self.breed)

        if self.sex is not None and not isinstance(self.sex, CodeableConcept):
            self.sex = CodeableConcept(**self.sex)

        if self.ethnicity is not None and not isinstance(self.ethnicity, CodeableConcept):
            self.ethnicity = CodeableConcept(**self.ethnicity)

        if self.race is None:
            self.race = []
        if not isinstance(self.race, list):
            self.race = [self.race]
        self.race = [v if isinstance(v, CodeableConcept) else CodeableConcept(**v) for v in self.race]

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, CcdhInteger):
            self.year_of_birth = CcdhInteger(self.year_of_birth)

        if self.vital_status is not None and not isinstance(self.vital_status, CodeableConcept):
            self.vital_status = CodeableConcept(**self.vital_status)

        if self.age_at_death is not None and not isinstance(self.age_at_death, Quantity):
            self.age_at_death = Quantity(**self.age_at_death)

        if self.year_of_death is not None and not isinstance(self.year_of_death, CcdhInteger):
            self.year_of_death = CcdhInteger(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, CodeableConcept):
            self.cause_of_death = CodeableConcept(**self.cause_of_death)

        super().__post_init__(**kwargs)


@dataclass
class TimePoint(Entity):
    """
    A structured representation of a single point in time that allows direct/explicit declaration as a dateTime, or
    specification in terms of offset from a defiend index.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.TimePoint
    class_class_curie: ClassVar[str] = "ccdh:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = CCDH.TimePoint

    dateTime: Optional[Union[str, CcdhDateTime]] = None
    indexDate: Optional[Union[str, CcdhDateTime]] = None
    indexEventType: Optional[Union[dict, CodeableConcept]] = None
    offsetFromIndex_indexOffset: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dateTime is not None and not isinstance(self.dateTime, CcdhDateTime):
            self.dateTime = CcdhDateTime(self.dateTime)

        if self.indexDate is not None and not isinstance(self.indexDate, CcdhDateTime):
            self.indexDate = CcdhDateTime(self.indexDate)

        if self.indexEventType is not None and not isinstance(self.indexEventType, CodeableConcept):
            self.indexEventType = CodeableConcept(**self.indexEventType)

        if self.offsetFromIndex_indexOffset is not None and not isinstance(self.offsetFromIndex_indexOffset, Quantity):
            self.offsetFromIndex_indexOffset = Quantity(**self.offsetFromIndex_indexOffset)

        super().__post_init__(**kwargs)


@dataclass
class TimePeriod(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.TimePeriod
    class_class_curie: ClassVar[str] = "ccdh:TimePeriod"
    class_name: ClassVar[str] = "TimePeriod"
    class_model_uri: ClassVar[URIRef] = CCDH.TimePeriod

    periodStart_start: Optional[Union[dict, TimePoint]] = None
    periodEnd_end: Optional[Union[dict, TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.periodStart_start is not None and not isinstance(self.periodStart_start, TimePoint):
            self.periodStart_start = TimePoint(**self.periodStart_start)

        if self.periodEnd_end is not None and not isinstance(self.periodEnd_end, TimePoint):
            self.periodEnd_end = TimePoint(**self.periodEnd_end)

        super().__post_init__(**kwargs)


@dataclass
class Treatment(Entity):
    """
    Represent medication administration or other treatment types.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Treatment
    class_class_curie: ClassVar[str] = "ccdh:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = CCDH.Treatment

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    regimen: Optional[Union[str, CcdhString]] = None
    type: Optional[Union[dict, CodeableConcept]] = None
    therapeutic_agent: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    start_date: Optional[Union[dict, TimePoint]] = None
    end_date: Optional[Union[dict, TimePoint]] = None
    end_reason: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    anatomic_site: Optional[Union[dict, BodySite]] = None
    effect: Optional[Union[str, CcdhString]] = None
    intent: Optional[Union[str, CcdhString]] = None
    outcome: Optional[Union[str, CcdhString]] = None
    diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    number_of_cycles: Optional[Union[int, CcdhInteger]] = None
    concurrent_treatment_type: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    concurrent_treatment: Optional[Union[Union[dict, "Treatment"], List[Union[dict, "Treatment"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.regimen is not None and not isinstance(self.regimen, CcdhString):
            self.regimen = CcdhString(self.regimen)

        if self.type is not None and not isinstance(self.type, CodeableConcept):
            self.type = CodeableConcept(**self.type)

        if self.therapeutic_agent is None:
            self.therapeutic_agent = []
        if not isinstance(self.therapeutic_agent, list):
            self.therapeutic_agent = [self.therapeutic_agent]
        self.therapeutic_agent = [v if isinstance(v, Entity) else Entity(**v) for v in self.therapeutic_agent]

        if self.start_date is not None and not isinstance(self.start_date, TimePoint):
            self.start_date = TimePoint(**self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, TimePoint):
            self.end_date = TimePoint(**self.end_date)

        if self.end_reason is None:
            self.end_reason = []
        if not isinstance(self.end_reason, list):
            self.end_reason = [self.end_reason]
        self.end_reason = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.end_reason]

        if self.anatomic_site is not None and not isinstance(self.anatomic_site, BodySite):
            self.anatomic_site = BodySite(**self.anatomic_site)

        if self.effect is not None and not isinstance(self.effect, CcdhString):
            self.effect = CcdhString(self.effect)

        if self.intent is not None and not isinstance(self.intent, CcdhString):
            self.intent = CcdhString(self.intent)

        if self.outcome is not None and not isinstance(self.outcome, CcdhString):
            self.outcome = CcdhString(self.outcome)

        if self.diagnosis is None:
            self.diagnosis = []
        if not isinstance(self.diagnosis, list):
            self.diagnosis = [self.diagnosis]
        self.diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.diagnosis]

        if self.number_of_cycles is not None and not isinstance(self.number_of_cycles, CcdhInteger):
            self.number_of_cycles = CcdhInteger(self.number_of_cycles)

        if self.concurrent_treatment_type is None:
            self.concurrent_treatment_type = []
        if not isinstance(self.concurrent_treatment_type, list):
            self.concurrent_treatment_type = [self.concurrent_treatment_type]
        self.concurrent_treatment_type = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.concurrent_treatment_type]

        if self.concurrent_treatment is None:
            self.concurrent_treatment = []
        if not isinstance(self.concurrent_treatment, list):
            self.concurrent_treatment = [self.concurrent_treatment]
        self.concurrent_treatment = [v if isinstance(v, Treatment) else Treatment(**v) for v in self.concurrent_treatment]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.bodySite__site = Slot(uri=CCDH.site, name="bodySite__site", curie=CCDH.curie('site'),
                   model_uri=CCDH.bodySite__site, domain=None, range=Union[dict, CodeableConcept])

slots.bodySite__qualifier = Slot(uri=CCDH.qualifier, name="bodySite__qualifier", curie=CCDH.curie('qualifier'),
                   model_uri=CCDH.bodySite__qualifier, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.biologicallyDerivedProduct__id = Slot(uri=CCDH.id, name="biologicallyDerivedProduct__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.biologicallyDerivedProduct__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicallyDerivedProduct__description = Slot(uri=CCDH.description, name="biologicallyDerivedProduct__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.biologicallyDerivedProduct__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicallyDerivedProduct__product_type = Slot(uri=CCDH.product_type, name="biologicallyDerivedProduct__product_type", curie=CCDH.curie('product_type'),
                   model_uri=CCDH.biologicallyDerivedProduct__product_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.biologicallyDerivedProduct__passage_number = Slot(uri=CCDH.passage_number, name="biologicallyDerivedProduct__passage_number", curie=CCDH.curie('passage_number'),
                   model_uri=CCDH.biologicallyDerivedProduct__passage_number, domain=None, range=Optional[Union[Union[int, CcdhInteger], List[Union[int, CcdhInteger]]]])

slots.biologicallyDerivedProduct__growth_rate = Slot(uri=CCDH.growth_rate, name="biologicallyDerivedProduct__growth_rate", curie=CCDH.curie('growth_rate'),
                   model_uri=CCDH.biologicallyDerivedProduct__growth_rate, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.cancerGrade__method_type = Slot(uri=CCDH.method_type, name="cancerGrade__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGrade__method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.cancerGrade__observations = Slot(uri=CCDH.observations, name="cancerGrade__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerGrade__observations, domain=None, range=Optional[Union[Union[dict, CancerGrade], List[Union[dict, CancerGrade]]]])

slots.cancerStage__observation_type = Slot(uri=CCDH.observation_type, name="cancerStage__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerStage__observation_type, domain=None, range=Union[dict, CodeableConcept])

slots.cancerStage__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="cancerStage__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.cancerStage__valueCodeableConcept, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.cancerStageSet__method_type = Slot(uri=CCDH.method_type, name="cancerStageSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageSet__method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.cancerStageSet__observations = Slot(uri=CCDH.observations, name="cancerStageSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerStageSet__observations, domain=None, range=Optional[Union[Union[dict, CancerStage], List[Union[dict, CancerStage]]]])

slots.codeableConcept__coding = Slot(uri=CCDH.coding, name="codeableConcept__coding", curie=CCDH.curie('coding'),
                   model_uri=CCDH.codeableConcept__coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.codeableConcept__text = Slot(uri=CCDH.text, name="codeableConcept__text", curie=CCDH.curie('text'),
                   model_uri=CCDH.codeableConcept__text, domain=None, range=Optional[Union[str, CcdhString]])

slots.coding__code = Slot(uri=CCDH.code, name="coding__code", curie=CCDH.curie('code'),
                   model_uri=CCDH.coding__code, domain=None, range=Union[str, CcdhString])

slots.coding__system = Slot(uri=CCDH.system, name="coding__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.coding__system, domain=None, range=Union[str, CcdhString])

slots.coding__label = Slot(uri=CCDH.label, name="coding__label", curie=CCDH.curie('label'),
                   model_uri=CCDH.coding__label, domain=None, range=Optional[Union[str, CcdhString]])

slots.coding__systemURL = Slot(uri=CCDH.systemURL, name="coding__systemURL", curie=CCDH.curie('systemURL'),
                   model_uri=CCDH.coding__systemURL, domain=None, range=Optional[Union[str, CcdhString]])

slots.coding__systemVersion = Slot(uri=CCDH.systemVersion, name="coding__systemVersion", curie=CCDH.curie('systemVersion'),
                   model_uri=CCDH.coding__systemVersion, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__id = Slot(uri=CCDH.id, name="specimenContainer__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenContainer__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__identifier = Slot(uri=CCDH.identifier, name="specimenContainer__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.specimenContainer__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.specimenContainer__container_type = Slot(uri=CCDH.container_type, name="specimenContainer__container_type", curie=CCDH.curie('container_type'),
                   model_uri=CCDH.specimenContainer__container_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenContainer__container_number = Slot(uri=CCDH.container_number, name="specimenContainer__container_number", curie=CCDH.curie('container_number'),
                   model_uri=CCDH.specimenContainer__container_number, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__additive = Slot(uri=CCDH.additive, name="specimenContainer__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenContainer__additive, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenContainer__parent_container = Slot(uri=CCDH.parent_container, name="specimenContainer__parent_container", curie=CCDH.curie('parent_container'),
                   model_uri=CCDH.specimenContainer__parent_container, domain=None, range=Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]])

slots.specimenContainer__charge_type = Slot(uri=CCDH.charge_type, name="specimenContainer__charge_type", curie=CCDH.curie('charge_type'),
                   model_uri=CCDH.specimenContainer__charge_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.diagnosis__id = Slot(uri=CCDH.id, name="diagnosis__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.diagnosis__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.diagnosis__identifier = Slot(uri=CCDH.identifier, name="diagnosis__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.diagnosis__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.diagnosis__age_at_diagnosis = Slot(uri=CCDH.age_at_diagnosis, name="diagnosis__age_at_diagnosis", curie=CCDH.curie('age_at_diagnosis'),
                   model_uri=CCDH.diagnosis__age_at_diagnosis, domain=None, range=Optional[Union[dict, Quantity]])

slots.diagnosis__year_at_diagnosis = Slot(uri=CCDH.year_at_diagnosis, name="diagnosis__year_at_diagnosis", curie=CCDH.curie('year_at_diagnosis'),
                   model_uri=CCDH.diagnosis__year_at_diagnosis, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.diagnosis__condition = Slot(uri=CCDH.condition, name="diagnosis__condition", curie=CCDH.curie('condition'),
                   model_uri=CCDH.diagnosis__condition, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.diagnosis__primary_site = Slot(uri=CCDH.primary_site, name="diagnosis__primary_site", curie=CCDH.curie('primary_site'),
                   model_uri=CCDH.diagnosis__primary_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__metastatic_site = Slot(uri=CCDH.metastatic_site, name="diagnosis__metastatic_site", curie=CCDH.curie('metastatic_site'),
                   model_uri=CCDH.diagnosis__metastatic_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__stage = Slot(uri=CCDH.stage, name="diagnosis__stage", curie=CCDH.curie('stage'),
                   model_uri=CCDH.diagnosis__stage, domain=None, range=Optional[Union[Union[dict, CancerStageSet], List[Union[dict, CancerStageSet]]]])

slots.diagnosis__grade = Slot(uri=CCDH.grade, name="diagnosis__grade", curie=CCDH.curie('grade'),
                   model_uri=CCDH.diagnosis__grade, domain=None, range=Optional[Union[Union[dict, CancerGrade], List[Union[dict, CancerGrade]]]])

slots.diagnosis__morphology = Slot(uri=CCDH.morphology, name="diagnosis__morphology", curie=CCDH.curie('morphology'),
                   model_uri=CCDH.diagnosis__morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.diagnosis__disease_status = Slot(uri=CCDH.disease_status, name="diagnosis__disease_status", curie=CCDH.curie('disease_status'),
                   model_uri=CCDH.diagnosis__disease_status, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.diagnosis__prior_diagnosis = Slot(uri=CCDH.prior_diagnosis, name="diagnosis__prior_diagnosis", curie=CCDH.curie('prior_diagnosis'),
                   model_uri=CCDH.diagnosis__prior_diagnosis, domain=None, range=Optional[Union[dict, Diagnosis]])

slots.diagnosis__method_of_diagnosis = Slot(uri=CCDH.method_of_diagnosis, name="diagnosis__method_of_diagnosis", curie=CCDH.curie('method_of_diagnosis'),
                   model_uri=CCDH.diagnosis__method_of_diagnosis, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.diagnosis__related_specimen = Slot(uri=CCDH.related_specimen, name="diagnosis__related_specimen", curie=CCDH.curie('related_specimen'),
                   model_uri=CCDH.diagnosis__related_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.document__id = Slot(uri=CCDH.id, name="document__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.document__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.document__identifier = Slot(uri=CCDH.identifier, name="document__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.document__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.document__document_type = Slot(uri=CCDH.document_type, name="document__document_type", curie=CCDH.curie('document_type'),
                   model_uri=CCDH.document__document_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.document__description = Slot(uri=CCDH.description, name="document__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.document__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.document__focus = Slot(uri=CCDH.focus, name="document__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.document__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.document__url = Slot(uri=CCDH.url, name="document__url", curie=CCDH.curie('url'),
                   model_uri=CCDH.document__url, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.entity__id = Slot(uri=CCDH.id, name="entity__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.entity__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.exposure__id = Slot(uri=CCDH.id, name="exposure__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.exposure__id, domain=None, range=Union[str, CcdhString])

slots.exposure__identifier = Slot(uri=CCDH.identifier, name="exposure__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.exposure__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.exposure__tobacco_use = Slot(uri=CCDH.tobacco_use, name="exposure__tobacco_use", curie=CCDH.curie('tobacco_use'),
                   model_uri=CCDH.exposure__tobacco_use, domain=None, range=Optional[Union[dict, Entity]])

slots.exposure__alcohol_use = Slot(uri=CCDH.alcohol_use, name="exposure__alcohol_use", curie=CCDH.curie('alcohol_use'),
                   model_uri=CCDH.exposure__alcohol_use, domain=None, range=Optional[Union[dict, Entity]])

slots.exposure__environmental = Slot(uri=CCDH.environmental, name="exposure__environmental", curie=CCDH.curie('environmental'),
                   model_uri=CCDH.exposure__environmental, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.exposure__related_patient = Slot(uri=CCDH.related_patient, name="exposure__related_patient", curie=CCDH.curie('related_patient'),
                   model_uri=CCDH.exposure__related_patient, domain=None, range=Optional[Union[dict, Subject]])

slots.identifier__value = Slot(uri=CCDH.value, name="identifier__value", curie=CCDH.curie('value'),
                   model_uri=CCDH.identifier__value, domain=None, range=Union[str, CcdhString])

slots.identifier__system = Slot(uri=CCDH.system, name="identifier__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.identifier__system, domain=None, range=Optional[Union[str, CcdhString]])

slots.identifier__type = Slot(uri=CCDH.type, name="identifier__type", curie=CCDH.curie('type'),
                   model_uri=CCDH.identifier__type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.observation__id = Slot(uri=CCDH.id, name="observation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.observation__id, domain=None, range=Union[str, CcdhString])

slots.observation__category = Slot(uri=CCDH.category, name="observation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.observation__category, domain=None, range=Union[dict, CodeableConcept])

slots.observation__observation_type = Slot(uri=CCDH.observation_type, name="observation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.observation__observation_type, domain=None, range=Union[dict, CodeableConcept])

slots.observation__method_type = Slot(uri=CCDH.method_type, name="observation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.observation__method_type, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.observation__focus = Slot(uri=CCDH.focus, name="observation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.observation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.observation__patient = Slot(uri=CCDH.patient, name="observation__patient", curie=CCDH.curie('patient'),
                   model_uri=CCDH.observation__patient, domain=None, range=Optional[Union[dict, Subject]])

slots.observation__performed_by = Slot(uri=CCDH.performed_by, name="observation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.observation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.observation__valueEntity = Slot(uri=CCDH.valueEntity, name="observation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.observation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.observation__valueString = Slot(uri=CCDH.valueString, name="observation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.observation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.observation__valueInteger = Slot(uri=CCDH.valueInteger, name="observation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.observation__valueInteger, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.observation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="observation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.observation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.observation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="observation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.observation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.observation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="observation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.observation__valueDateTime, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.organization__id = Slot(uri=CCDH.id, name="organization__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.organization__id, domain=None, range=Union[str, CcdhString])

slots.organization__identifier = Slot(uri=CCDH.identifier, name="organization__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.organization__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.organization__name = Slot(uri=CCDH.name, name="organization__name", curie=CCDH.curie('name'),
                   model_uri=CCDH.organization__name, domain=None, range=Union[str, CcdhString])

slots.organization__alias = Slot(uri=CCDH.alias, name="organization__alias", curie=CCDH.curie('alias'),
                   model_uri=CCDH.organization__alias, domain=None, range=Optional[Union[str, CcdhString]])

slots.organization__organization_type = Slot(uri=CCDH.organization_type, name="organization__organization_type", curie=CCDH.curie('organization_type'),
                   model_uri=CCDH.organization__organization_type, domain=None, range=Optional[Union[str, CcdhString]])

slots.quantity__valueDecimal = Slot(uri=CCDH.valueDecimal, name="quantity__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.quantity__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.quantity__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="quantity__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.quantity__valueCodeableConcept, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.quantity__unitCode = Slot(uri=CCDH.unitCode, name="quantity__unitCode", curie=CCDH.curie('unitCode'),
                   model_uri=CCDH.quantity__unitCode, domain=None, range=Optional[Union[dict, Coding]])

slots.quantity__unit = Slot(uri=CCDH.unit, name="quantity__unit", curie=CCDH.curie('unit'),
                   model_uri=CCDH.quantity__unit, domain=None, range=Optional[Union[str, CcdhString]])

slots.quantity__comparator = Slot(uri=CCDH.comparator, name="quantity__comparator", curie=CCDH.curie('comparator'),
                   model_uri=CCDH.quantity__comparator, domain=None, range=Optional[Union[dict, Coding]])

slots.researchProject__id = Slot(uri=CCDH.id, name="researchProject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.researchProject__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchProject__identifier = Slot(uri=CCDH.identifier, name="researchProject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.researchProject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.researchProject__name = Slot(uri=CCDH.name, name="researchProject__name", curie=CCDH.curie('name'),
                   model_uri=CCDH.researchProject__name, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchProject__name_shortened = Slot(uri=CCDH.name_shortened, name="researchProject__name_shortened", curie=CCDH.curie('name_shortened'),
                   model_uri=CCDH.researchProject__name_shortened, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchProject__description = Slot(uri=CCDH.description, name="researchProject__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.researchProject__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchProject__description_shortened = Slot(uri=CCDH.description_shortened, name="researchProject__description_shortened", curie=CCDH.curie('description_shortened'),
                   model_uri=CCDH.researchProject__description_shortened, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchProject__sponsor = Slot(uri=CCDH.sponsor, name="researchProject__sponsor", curie=CCDH.curie('sponsor'),
                   model_uri=CCDH.researchProject__sponsor, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.researchProject__date_started = Slot(uri=CCDH.date_started, name="researchProject__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.researchProject__date_started, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.researchProject__date_ended = Slot(uri=CCDH.date_ended, name="researchProject__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.researchProject__date_ended, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.researchProject__primary_anatomic_site = Slot(uri=CCDH.primary_anatomic_site, name="researchProject__primary_anatomic_site", curie=CCDH.curie('primary_anatomic_site'),
                   model_uri=CCDH.researchProject__primary_anatomic_site, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.researchProject__url = Slot(uri=CCDH.url, name="researchProject__url", curie=CCDH.curie('url'),
                   model_uri=CCDH.researchProject__url, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.researchProject__part_of = Slot(uri=CCDH.part_of, name="researchProject__part_of", curie=CCDH.curie('part_of'),
                   model_uri=CCDH.researchProject__part_of, domain=None, range=Optional[Union[Union[dict, ResearchProject], List[Union[dict, ResearchProject]]]])

slots.researchProject__research_project_type = Slot(uri=CCDH.research_project_type, name="researchProject__research_project_type", curie=CCDH.curie('research_project_type'),
                   model_uri=CCDH.researchProject__research_project_type, domain=None, range=Union[dict, CodeableConcept])

slots.researchProject__date_iacuc_approval = Slot(uri=CCDH.date_iacuc_approval, name="researchProject__date_iacuc_approval", curie=CCDH.curie('date_iacuc_approval'),
                   model_uri=CCDH.researchProject__date_iacuc_approval, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.researchSubject__id = Slot(uri=CCDH.id, name="researchSubject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.researchSubject__id, domain=None, range=Union[str, CcdhString])

slots.researchSubject__identifier = Slot(uri=CCDH.identifier, name="researchSubject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.researchSubject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.researchSubject__description = Slot(uri=CCDH.description, name="researchSubject__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.researchSubject__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchSubject__member_of_research_project = Slot(uri=CCDH.member_of_research_project, name="researchSubject__member_of_research_project", curie=CCDH.curie('member_of_research_project'),
                   model_uri=CCDH.researchSubject__member_of_research_project, domain=None, range=Optional[Union[Union[dict, ResearchProject], List[Union[dict, ResearchProject]]]])

slots.researchSubject__age_at_enrollment = Slot(uri=CCDH.age_at_enrollment, name="researchSubject__age_at_enrollment", curie=CCDH.curie('age_at_enrollment'),
                   model_uri=CCDH.researchSubject__age_at_enrollment, domain=None, range=Optional[Union[dict, Quantity]])

slots.researchSubject__primary_diagnosis_condition = Slot(uri=CCDH.primary_diagnosis_condition, name="researchSubject__primary_diagnosis_condition", curie=CCDH.curie('primary_diagnosis_condition'),
                   model_uri=CCDH.researchSubject__primary_diagnosis_condition, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__primary_diagnosis_site = Slot(uri=CCDH.primary_diagnosis_site, name="researchSubject__primary_diagnosis_site", curie=CCDH.curie('primary_diagnosis_site'),
                   model_uri=CCDH.researchSubject__primary_diagnosis_site, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__primary_diagnosis = Slot(uri=CCDH.primary_diagnosis, name="researchSubject__primary_diagnosis", curie=CCDH.curie('primary_diagnosis'),
                   model_uri=CCDH.researchSubject__primary_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__comorbid_diagnoses = Slot(uri=CCDH.comorbid_diagnoses, name="researchSubject__comorbid_diagnoses", curie=CCDH.curie('comorbid_diagnoses'),
                   model_uri=CCDH.researchSubject__comorbid_diagnoses, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__index_timepoint = Slot(uri=CCDH.index_timepoint, name="researchSubject__index_timepoint", curie=CCDH.curie('index_timepoint'),
                   model_uri=CCDH.researchSubject__index_timepoint, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.researchSubject__originating_site = Slot(uri=CCDH.originating_site, name="researchSubject__originating_site", curie=CCDH.curie('originating_site'),
                   model_uri=CCDH.researchSubject__originating_site, domain=None, range=Optional[Union[dict, Organization]])

slots.researchSubject__associated_subject = Slot(uri=CCDH.associated_subject, name="researchSubject__associated_subject", curie=CCDH.curie('associated_subject'),
                   model_uri=CCDH.researchSubject__associated_subject, domain=None, range=Union[dict, Subject])

slots.specimen__id = Slot(uri=CCDH.id, name="specimen__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimen__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimen__identifier = Slot(uri=CCDH.identifier, name="specimen__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.specimen__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.specimen__description = Slot(uri=CCDH.description, name="specimen__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.specimen__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimen__specimen_type = Slot(uri=CCDH.specimen_type, name="specimen__specimen_type", curie=CCDH.curie('specimen_type'),
                   model_uri=CCDH.specimen__specimen_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__analyte_type = Slot(uri=CCDH.analyte_type, name="specimen__analyte_type", curie=CCDH.curie('analyte_type'),
                   model_uri=CCDH.specimen__analyte_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__associated_project = Slot(uri=CCDH.associated_project, name="specimen__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH.specimen__associated_project, domain=None, range=Optional[Union[dict, ResearchProject]])

slots.specimen__data_provider = Slot(uri=CCDH.data_provider, name="specimen__data_provider", curie=CCDH.curie('data_provider'),
                   model_uri=CCDH.specimen__data_provider, domain=None, range=Optional[Union[dict, Organization]])

slots.specimen__source_material_type = Slot(uri=CCDH.source_material_type, name="specimen__source_material_type", curie=CCDH.curie('source_material_type'),
                   model_uri=CCDH.specimen__source_material_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__parent_specimen = Slot(uri=CCDH.parent_specimen, name="specimen__parent_specimen", curie=CCDH.curie('parent_specimen'),
                   model_uri=CCDH.specimen__parent_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.specimen__source_subject = Slot(uri=CCDH.source_subject, name="specimen__source_subject", curie=CCDH.curie('source_subject'),
                   model_uri=CCDH.specimen__source_subject, domain=None, range=Optional[Union[dict, Subject]])

slots.specimen__source_model_system = Slot(uri=CCDH.source_model_system, name="specimen__source_model_system", curie=CCDH.curie('source_model_system'),
                   model_uri=CCDH.specimen__source_model_system, domain=None, range=Optional[Union[dict, Entity]])

slots.specimen__condition_status_at_collection = Slot(uri=CCDH.condition_status_at_collection, name="specimen__condition_status_at_collection", curie=CCDH.curie('condition_status_at_collection'),
                   model_uri=CCDH.specimen__condition_status_at_collection, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__creation_activity = Slot(uri=CCDH.creation_activity, name="specimen__creation_activity", curie=CCDH.curie('creation_activity'),
                   model_uri=CCDH.specimen__creation_activity, domain=None, range=Optional[Union[dict, SpecimenCreationActivity]])

slots.specimen__processing_activity = Slot(uri=CCDH.processing_activity, name="specimen__processing_activity", curie=CCDH.curie('processing_activity'),
                   model_uri=CCDH.specimen__processing_activity, domain=None, range=Optional[Union[Union[dict, SpecimenProcessingActivity], List[Union[dict, SpecimenProcessingActivity]]]])

slots.specimen__storage_activity = Slot(uri=CCDH.storage_activity, name="specimen__storage_activity", curie=CCDH.curie('storage_activity'),
                   model_uri=CCDH.specimen__storage_activity, domain=None, range=Optional[Union[dict, SpecimenStorageActivity]])

slots.specimen__transport_activity = Slot(uri=CCDH.transport_activity, name="specimen__transport_activity", curie=CCDH.curie('transport_activity'),
                   model_uri=CCDH.specimen__transport_activity, domain=None, range=Optional[Union[dict, SpecimenTransportActivity]])

slots.specimen__contained_in = Slot(uri=CCDH.contained_in, name="specimen__contained_in", curie=CCDH.curie('contained_in'),
                   model_uri=CCDH.specimen__contained_in, domain=None, range=Optional[Union[dict, SpecimenContainer]])

slots.specimen__dimensional_measure = Slot(uri=CCDH.dimensional_measure, name="specimen__dimensional_measure", curie=CCDH.curie('dimensional_measure'),
                   model_uri=CCDH.specimen__dimensional_measure, domain=None, range=Optional[Union[dict, Entity]])

slots.specimen__quantity_measure = Slot(uri=CCDH.quantity_measure, name="specimen__quantity_measure", curie=CCDH.curie('quantity_measure'),
                   model_uri=CCDH.specimen__quantity_measure, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimen__quality_measure = Slot(uri=CCDH.quality_measure, name="specimen__quality_measure", curie=CCDH.curie('quality_measure'),
                   model_uri=CCDH.specimen__quality_measure, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimen__cellular_composition_type = Slot(uri=CCDH.cellular_composition_type, name="specimen__cellular_composition_type", curie=CCDH.curie('cellular_composition_type'),
                   model_uri=CCDH.specimen__cellular_composition_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__cellular_composition_measure = Slot(uri=CCDH.cellular_composition_measure, name="specimen__cellular_composition_measure", curie=CCDH.curie('cellular_composition_measure'),
                   model_uri=CCDH.specimen__cellular_composition_measure, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimen__tissue_composition_measure = Slot(uri=CCDH.tissue_composition_measure, name="specimen__tissue_composition_measure", curie=CCDH.curie('tissue_composition_measure'),
                   model_uri=CCDH.specimen__tissue_composition_measure, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimen__general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="specimen__general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                   model_uri=CCDH.specimen__general_tissue_morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="specimen__specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                   model_uri=CCDH.specimen__specific_tissue_morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__preinvasive_tissue_morphology = Slot(uri=CCDH.preinvasive_tissue_morphology, name="specimen__preinvasive_tissue_morphology", curie=CCDH.curie('preinvasive_tissue_morphology'),
                   model_uri=CCDH.specimen__preinvasive_tissue_morphology, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__morphology_pathologically_confirmed = Slot(uri=CCDH.morphology_pathologically_confirmed, name="specimen__morphology_pathologically_confirmed", curie=CCDH.curie('morphology_pathologically_confirmed'),
                   model_uri=CCDH.specimen__morphology_pathologically_confirmed, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.specimen__morphology_assessor_role = Slot(uri=CCDH.morphology_assessor_role, name="specimen__morphology_assessor_role", curie=CCDH.curie('morphology_assessor_role'),
                   model_uri=CCDH.specimen__morphology_assessor_role, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__morphlogy_assessment_method = Slot(uri=CCDH.morphlogy_assessment_method, name="specimen__morphlogy_assessment_method", curie=CCDH.curie('morphlogy_assessment_method'),
                   model_uri=CCDH.specimen__morphlogy_assessment_method, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__degree_of_dysplasia = Slot(uri=CCDH.degree_of_dysplasia, name="specimen__degree_of_dysplasia", curie=CCDH.curie('degree_of_dysplasia'),
                   model_uri=CCDH.specimen__degree_of_dysplasia, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__dysplasia_fraction = Slot(uri=CCDH.dysplasia_fraction, name="specimen__dysplasia_fraction", curie=CCDH.curie('dysplasia_fraction'),
                   model_uri=CCDH.specimen__dysplasia_fraction, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimen__related_document = Slot(uri=CCDH.related_document, name="specimen__related_document", curie=CCDH.curie('related_document'),
                   model_uri=CCDH.specimen__related_document, domain=None, range=Optional[Union[Union[dict, Document], List[Union[dict, Document]]]])

slots.specimen__section_location = Slot(uri=CCDH.section_location, name="specimen__section_location", curie=CCDH.curie('section_location'),
                   model_uri=CCDH.specimen__section_location, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimen__derived_product = Slot(uri=CCDH.derived_product, name="specimen__derived_product", curie=CCDH.curie('derived_product'),
                   model_uri=CCDH.specimen__derived_product, domain=None, range=Optional[Union[Union[dict, BiologicallyDerivedProduct], List[Union[dict, BiologicallyDerivedProduct]]]])

slots.specimen__distance_from_paired_specimen = Slot(uri=CCDH.distance_from_paired_specimen, name="specimen__distance_from_paired_specimen", curie=CCDH.curie('distance_from_paired_specimen'),
                   model_uri=CCDH.specimen__distance_from_paired_specimen, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenCreationActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenCreationActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenCreationActivity__activity_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenCreationActivity__date_started = Slot(uri=CCDH.date_started, name="specimenCreationActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenCreationActivity__date_started, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenCreationActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenCreationActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenCreationActivity__date_ended, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenCreationActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenCreationActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenCreationActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenCreationActivity__collection_method_type = Slot(uri=CCDH.collection_method_type, name="specimenCreationActivity__collection_method_type", curie=CCDH.curie('collection_method_type'),
                   model_uri=CCDH.specimenCreationActivity__collection_method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenCreationActivity__derivation_method_type = Slot(uri=CCDH.derivation_method_type, name="specimenCreationActivity__derivation_method_type", curie=CCDH.curie('derivation_method_type'),
                   model_uri=CCDH.specimenCreationActivity__derivation_method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenCreationActivity__additive = Slot(uri=CCDH.additive, name="specimenCreationActivity__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenCreationActivity__additive, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenCreationActivity__collection_site = Slot(uri=CCDH.collection_site, name="specimenCreationActivity__collection_site", curie=CCDH.curie('collection_site'),
                   model_uri=CCDH.specimenCreationActivity__collection_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.specimenCreationActivity__input_specimen = Slot(uri=CCDH.input_specimen, name="specimenCreationActivity__input_specimen", curie=CCDH.curie('input_specimen'),
                   model_uri=CCDH.specimenCreationActivity__input_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.specimenCreationActivity__quantity_collected = Slot(uri=CCDH.quantity_collected, name="specimenCreationActivity__quantity_collected", curie=CCDH.curie('quantity_collected'),
                   model_uri=CCDH.specimenCreationActivity__quantity_collected, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenCreationActivity__execution_condition = Slot(uri=CCDH.execution_condition, name="specimenCreationActivity__execution_condition", curie=CCDH.curie('execution_condition'),
                   model_uri=CCDH.specimenCreationActivity__execution_condition, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenCreationActivity__specimen_order = Slot(uri=CCDH.specimen_order, name="specimenCreationActivity__specimen_order", curie=CCDH.curie('specimen_order'),
                   model_uri=CCDH.specimenCreationActivity__specimen_order, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenProcessingActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenProcessingActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenProcessingActivity__activity_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenProcessingActivity__date_started = Slot(uri=CCDH.date_started, name="specimenProcessingActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenProcessingActivity__date_started, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenProcessingActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenProcessingActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenProcessingActivity__date_ended, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenProcessingActivity__duration = Slot(uri=CCDH.duration, name="specimenProcessingActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH.specimenProcessingActivity__duration, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.specimenProcessingActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenProcessingActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenProcessingActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenProcessingActivity__method_type = Slot(uri=CCDH.method_type, name="specimenProcessingActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenProcessingActivity__method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenProcessingActivity__additive = Slot(uri=CCDH.additive, name="specimenProcessingActivity__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenProcessingActivity__additive, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenProcessingActivity__device = Slot(uri=CCDH.device, name="specimenProcessingActivity__device", curie=CCDH.curie('device'),
                   model_uri=CCDH.specimenProcessingActivity__device, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.specimenProcessingActivity__executionConditions = Slot(uri=CCDH.executionConditions, name="specimenProcessingActivity__executionConditions", curie=CCDH.curie('executionConditions'),
                   model_uri=CCDH.specimenProcessingActivity__executionConditions, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenStorageActivity__date_started = Slot(uri=CCDH.date_started, name="specimenStorageActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenStorageActivity__date_started, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenStorageActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenStorageActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenStorageActivity__date_ended, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenStorageActivity__method_type = Slot(uri=CCDH.method_type, name="specimenStorageActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenStorageActivity__method_type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.specimenStorageActivity__container = Slot(uri=CCDH.container, name="specimenStorageActivity__container", curie=CCDH.curie('container'),
                   model_uri=CCDH.specimenStorageActivity__container, domain=None, range=Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]])

slots.specimenTransportActivity__date_started = Slot(uri=CCDH.date_started, name="specimenTransportActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenTransportActivity__date_started, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenTransportActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenTransportActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenTransportActivity__date_ended, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenTransportActivity__transport_destination = Slot(uri=CCDH.transport_destination, name="specimenTransportActivity__transport_destination", curie=CCDH.curie('transport_destination'),
                   model_uri=CCDH.specimenTransportActivity__transport_destination, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenTransportActivity__execution_conditions = Slot(uri=CCDH.execution_conditions, name="specimenTransportActivity__execution_conditions", curie=CCDH.curie('execution_conditions'),
                   model_uri=CCDH.specimenTransportActivity__execution_conditions, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.subject__id = Slot(uri=CCDH.id, name="subject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.subject__id, domain=None, range=Union[str, CcdhString])

slots.subject__identifier = Slot(uri=CCDH.identifier, name="subject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.subject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.subject__species = Slot(uri=CCDH.species, name="subject__species", curie=CCDH.curie('species'),
                   model_uri=CCDH.subject__species, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.subject__breed = Slot(uri=CCDH.breed, name="subject__breed", curie=CCDH.curie('breed'),
                   model_uri=CCDH.subject__breed, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.subject__sex = Slot(uri=CCDH.sex, name="subject__sex", curie=CCDH.curie('sex'),
                   model_uri=CCDH.subject__sex, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.subject__ethnicity = Slot(uri=CCDH.ethnicity, name="subject__ethnicity", curie=CCDH.curie('ethnicity'),
                   model_uri=CCDH.subject__ethnicity, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.subject__race = Slot(uri=CCDH.race, name="subject__race", curie=CCDH.curie('race'),
                   model_uri=CCDH.subject__race, domain=None, range=Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]])

slots.subject__year_of_birth = Slot(uri=CCDH.year_of_birth, name="subject__year_of_birth", curie=CCDH.curie('year_of_birth'),
                   model_uri=CCDH.subject__year_of_birth, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__vital_status = Slot(uri=CCDH.vital_status, name="subject__vital_status", curie=CCDH.curie('vital_status'),
                   model_uri=CCDH.subject__vital_status, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.subject__age_at_death = Slot(uri=CCDH.age_at_death, name="subject__age_at_death", curie=CCDH.curie('age_at_death'),
                   model_uri=CCDH.subject__age_at_death, domain=None, range=Optional[Union[dict, Quantity]])

slots.subject__year_of_death = Slot(uri=CCDH.year_of_death, name="subject__year_of_death", curie=CCDH.curie('year_of_death'),
                   model_uri=CCDH.subject__year_of_death, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__cause_of_death = Slot(uri=CCDH.cause_of_death, name="subject__cause_of_death", curie=CCDH.curie('cause_of_death'),
                   model_uri=CCDH.subject__cause_of_death, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.timePoint__dateTime = Slot(uri=CCDH.dateTime, name="timePoint__dateTime", curie=CCDH.curie('dateTime'),
                   model_uri=CCDH.timePoint__dateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__indexDate = Slot(uri=CCDH.indexDate, name="timePoint__indexDate", curie=CCDH.curie('indexDate'),
                   model_uri=CCDH.timePoint__indexDate, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__indexEventType = Slot(uri=CCDH.indexEventType, name="timePoint__indexEventType", curie=CCDH.curie('indexEventType'),
                   model_uri=CCDH.timePoint__indexEventType, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.timePoint__offsetFromIndex_indexOffset = Slot(uri=CCDH.offsetFromIndex_indexOffset, name="timePoint__offsetFromIndex_indexOffset", curie=CCDH.curie('offsetFromIndex_indexOffset'),
                   model_uri=CCDH.timePoint__offsetFromIndex_indexOffset, domain=None, range=Optional[Union[dict, Quantity]])

slots.timePeriod__periodStart_start = Slot(uri=CCDH.periodStart_start, name="timePeriod__periodStart_start", curie=CCDH.curie('periodStart_start'),
                   model_uri=CCDH.timePeriod__periodStart_start, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePeriod__periodEnd_end = Slot(uri=CCDH.periodEnd_end, name="timePeriod__periodEnd_end", curie=CCDH.curie('periodEnd_end'),
                   model_uri=CCDH.timePeriod__periodEnd_end, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__id = Slot(uri=CCDH.id, name="treatment__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.treatment__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__identifier = Slot(uri=CCDH.identifier, name="treatment__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.treatment__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.treatment__regimen = Slot(uri=CCDH.regimen, name="treatment__regimen", curie=CCDH.curie('regimen'),
                   model_uri=CCDH.treatment__regimen, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__type = Slot(uri=CCDH.type, name="treatment__type", curie=CCDH.curie('type'),
                   model_uri=CCDH.treatment__type, domain=None, range=Optional[Union[dict, CodeableConcept]])

slots.treatment__therapeutic_agent = Slot(uri=CCDH.therapeutic_agent, name="treatment__therapeutic_agent", curie=CCDH.curie('therapeutic_agent'),
                   model_uri=CCDH.treatment__therapeutic_agent, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.treatment__start_date = Slot(uri=CCDH.start_date, name="treatment__start_date", curie=CCDH.curie('start_date'),
                   model_uri=CCDH.treatment__start_date, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__end_date = Slot(uri=CCDH.end_date, name="treatment__end_date", curie=CCDH.curie('end_date'),
                   model_uri=CCDH.treatment__end_date, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__end_reason = Slot(uri=CCDH.end_reason, name="treatment__end_reason", curie=CCDH.curie('end_reason'),
                   model_uri=CCDH.treatment__end_reason, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.treatment__anatomic_site = Slot(uri=CCDH.anatomic_site, name="treatment__anatomic_site", curie=CCDH.curie('anatomic_site'),
                   model_uri=CCDH.treatment__anatomic_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.treatment__effect = Slot(uri=CCDH.effect, name="treatment__effect", curie=CCDH.curie('effect'),
                   model_uri=CCDH.treatment__effect, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__intent = Slot(uri=CCDH.intent, name="treatment__intent", curie=CCDH.curie('intent'),
                   model_uri=CCDH.treatment__intent, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__outcome = Slot(uri=CCDH.outcome, name="treatment__outcome", curie=CCDH.curie('outcome'),
                   model_uri=CCDH.treatment__outcome, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__diagnosis = Slot(uri=CCDH.diagnosis, name="treatment__diagnosis", curie=CCDH.curie('diagnosis'),
                   model_uri=CCDH.treatment__diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.treatment__number_of_cycles = Slot(uri=CCDH.number_of_cycles, name="treatment__number_of_cycles", curie=CCDH.curie('number_of_cycles'),
                   model_uri=CCDH.treatment__number_of_cycles, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.treatment__concurrent_treatment_type = Slot(uri=CCDH.concurrent_treatment_type, name="treatment__concurrent_treatment_type", curie=CCDH.curie('concurrent_treatment_type'),
                   model_uri=CCDH.treatment__concurrent_treatment_type, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.treatment__concurrent_treatment = Slot(uri=CCDH.concurrent_treatment, name="treatment__concurrent_treatment", curie=CCDH.curie('concurrent_treatment'),
                   model_uri=CCDH.treatment__concurrent_treatment, domain=None, range=Optional[Union[Union[dict, Treatment], List[Union[dict, Treatment]]]])
