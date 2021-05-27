# Auto generated from ccdhmodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-27 11:48
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
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
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

    site: Union[str, "EnumCRDC-H.BodySite.site"] = None
    qualifier: Optional[Union[Union[str, "EnumCRDC-H.BodySite.qualifier"], List[Union[str, "EnumCRDC-H.BodySite.qualifier"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.site is None:
            raise ValueError("site must be supplied")
        if not isinstance(self.site, EnumCRDC-H.BodySite.site):
            self.site = EnumCRDC-H.BodySite.site(self.site)

        if self.qualifier is None:
            self.qualifier = []
        if not isinstance(self.qualifier, list):
            self.qualifier = [self.qualifier]
        self.qualifier = [v if isinstance(v, EnumCRDC-H.BodySite.qualifier) else EnumCRDC-H.BodySite.qualifier(v) for v in self.qualifier]

        super().__post_init__(**kwargs)


@dataclass
class BiologicProduct(Entity):
    """
    A living organism, or a metabolocally active biological system such as a cell culture, tissue culture, or organoid
    that is maintained or propagated in vitro.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BiologicProduct
    class_class_curie: ClassVar[str] = "ccdh:BiologicProduct"
    class_name: ClassVar[str] = "BiologicProduct"
    class_model_uri: ClassVar[URIRef] = CCDH.BiologicProduct

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    description: Optional[Union[str, CcdhString]] = None
    product_type: Optional[Union[str, "EnumCRDC-H.BiologicProduct.productType"]] = None
    passage_number: Optional[Union[Union[int, CcdhInteger], List[Union[int, CcdhInteger]]]] = empty_list()
    growth_rate: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()

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

        if self.product_type is not None and not isinstance(self.product_type, EnumCRDC-H.BiologicProduct.productType):
            self.product_type = EnumCRDC-H.BiologicProduct.productType(self.product_type)

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
class CancerGradeObservation(Entity):
    """
    A data structure with key (observation_type) and value (valueCodeableConcept) attributes that represents a single
    cancer grade observation, such as ...
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation
    class_class_curie: ClassVar[str] = "ccdh:CancerGradeObservation"
    class_name: ClassVar[str] = "CancerGradeObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation

    observation_type: Union[str, "EnumCRDC-H.CancerGradeObservation.observationType"] = None
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.CancerGradeObservation.observationType):
            self.observation_type = EnumCRDC-H.CancerGradeObservation.observationType(self.observation_type)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.CancerGradeObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.CancerGradeObservation.valueCodeableConcept(self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class CancerGradeObservationSet(Entity):
    """
    A structured object to hold related data items about the grade of cancer (e.g. overall, primary gleason, secondary
    gleason, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerGradeObservationSet
    class_class_curie: ClassVar[str] = "ccdh:CancerGradeObservationSet"
    class_name: ClassVar[str] = "CancerGradeObservationSet"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerGradeObservationSet

    method_type: Optional[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"]] = None
    observations: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.CancerGradeObservationSet.methodType):
            self.method_type = EnumCRDC-H.CancerGradeObservationSet.methodType(self.method_type)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self.observations = [v if isinstance(v, Entity) else Entity(**v) for v in self.observations]

        super().__post_init__(**kwargs)


@dataclass
class CancerStageObservation(Entity):
    """
    A data structure with key (observation_type) and value (valueCodeableConcept) attributes that represents a single
    cancer staging observation, such as the Clinical Metastasis (M) component of a clinical TNM staging.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerStageObservation
    class_class_curie: ClassVar[str] = "ccdh:CancerStageObservation"
    class_name: ClassVar[str] = "CancerStageObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerStageObservation

    observation_type: Union[str, "EnumCRDC-H.CancerStageObservation.observationType"] = None
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.CancerStageObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.CancerStageObservation.observationType):
            self.observation_type = EnumCRDC-H.CancerStageObservation.observationType(self.observation_type)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.CancerStageObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.CancerStageObservation.valueCodeableConcept(self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class CancerStageObservationSet(Entity):
    """
    A structured object to hold related data items about the staging of cancer (e.g. overall, T, N, and M components
    of a Cancer Staging observation).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerStageObservationSet
    class_class_curie: ClassVar[str] = "ccdh:CancerStageObservationSet"
    class_name: ClassVar[str] = "CancerStageObservationSet"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerStageObservationSet

    category: Union[str, "EnumCRDC-H.CancerStageObservationSet.category"] = None
    method_type: Optional[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"]] = None
    observations: Optional[Union[Union[dict, CancerStageObservation], List[Union[dict, CancerStageObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.category is None:
            raise ValueError("category must be supplied")
        if not isinstance(self.category, EnumCRDC-H.CancerStageObservationSet.category):
            self.category = EnumCRDC-H.CancerStageObservationSet.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.CancerStageObservationSet.methodType):
            self.method_type = EnumCRDC-H.CancerStageObservationSet.methodType(self.method_type)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self._normalize_inlined_slot(slot_name="observations", slot_type=CancerStageObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

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
    condition: Optional[Union[str, "EnumCRDC-H.Diagnosis.condition"]] = None
    primary_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    metastatic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    stage: Optional[Union[Union[dict, CancerStageObservationSet], List[Union[dict, CancerStageObservationSet]]]] = empty_list()
    grade: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    morphology: Optional[Union[str, "EnumCRDC-H.Diagnosis.morphology"]] = None
    disease_status: Optional[Union[str, "EnumCRDC-H.Diagnosis.diseaseStatus"]] = None
    prior_diagnosis: Optional[Union[dict, "Diagnosis"]] = None
    method_of_diagnosis: Optional[Union[str, "EnumCRDC-H.Diagnosis.methodOfDiagnosis"]] = None
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

        if self.condition is not None and not isinstance(self.condition, EnumCRDC-H.Diagnosis.condition):
            self.condition = EnumCRDC-H.Diagnosis.condition(self.condition)

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
        self._normalize_inlined_slot(slot_name="stage", slot_type=CancerStageObservationSet, key_name="category", inlined_as_list=True, keyed=False)

        if self.grade is None:
            self.grade = []
        if not isinstance(self.grade, list):
            self.grade = [self.grade]
        self.grade = [v if isinstance(v, Entity) else Entity(**v) for v in self.grade]

        if self.morphology is not None and not isinstance(self.morphology, EnumCRDC-H.Diagnosis.morphology):
            self.morphology = EnumCRDC-H.Diagnosis.morphology(self.morphology)

        if self.disease_status is not None and not isinstance(self.disease_status, EnumCRDC-H.Diagnosis.diseaseStatus):
            self.disease_status = EnumCRDC-H.Diagnosis.diseaseStatus(self.disease_status)

        if self.prior_diagnosis is not None and not isinstance(self.prior_diagnosis, Diagnosis):
            self.prior_diagnosis = Diagnosis(**self.prior_diagnosis)

        if self.method_of_diagnosis is not None and not isinstance(self.method_of_diagnosis, EnumCRDC-H.Diagnosis.methodOfDiagnosis):
            self.method_of_diagnosis = EnumCRDC-H.Diagnosis.methodOfDiagnosis(self.method_of_diagnosis)

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
    document_type: Optional[Union[str, "EnumCRDC-H.Document.documentType"]] = None
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

        if self.document_type is not None and not isinstance(self.document_type, EnumCRDC-H.Document.documentType):
            self.document_type = EnumCRDC-H.Document.documentType(self.document_type)

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
    tobacco_use: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    alcohol_use: Optional[Union[dict, Entity]] = None
    environmental: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None

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

        if self.tobacco_use is None:
            self.tobacco_use = []
        if not isinstance(self.tobacco_use, list):
            self.tobacco_use = [self.tobacco_use]
        self.tobacco_use = [v if isinstance(v, Entity) else Entity(**v) for v in self.tobacco_use]

        if self.alcohol_use is not None and not isinstance(self.alcohol_use, Entity):
            self.alcohol_use = Entity(**self.alcohol_use)

        if self.environmental is None:
            self.environmental = []
        if not isinstance(self.environmental, list):
            self.environmental = [self.environmental]
        self._normalize_inlined_slot(slot_name="environmental", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

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
    type: Optional[Union[str, "EnumCRDC-H.Identifier.type"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is None:
            raise ValueError("value must be supplied")
        if not isinstance(self.value, CcdhString):
            self.value = CcdhString(self.value)

        if self.system is not None and not isinstance(self.system, CcdhString):
            self.system = CcdhString(self.system)

        if self.type is not None and not isinstance(self.type, EnumCRDC-H.Identifier.type):
            self.type = EnumCRDC-H.Identifier.type(self.type)

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
    category: Union[str, "EnumCRDC-H.Observation.category"] = None
    observation_type: Union[str, "EnumCRDC-H.Observation.observationType"] = None
    method_type: Optional[Union[Union[str, "EnumCRDC-H.Observation.methodType"], List[Union[str, "EnumCRDC-H.Observation.methodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[Decimal, CcdhDecimal]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, "Quantity"]] = None
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.Observation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        if not isinstance(self.category, EnumCRDC-H.Observation.category):
            self.category = EnumCRDC-H.Observation.category(self.category)

        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.Observation.observationType):
            self.observation_type = EnumCRDC-H.Observation.observationType(self.observation_type)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, EnumCRDC-H.Observation.methodType) else EnumCRDC-H.Observation.methodType(v) for v in self.method_type]

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

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

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.Observation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.Observation.valueCodeableConcept(self.valueCodeableConcept)

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
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CcdhString]] = None
    alias: Optional[Union[str, CcdhString]] = None
    organization_type: Optional[Union[str, CcdhString]] = None

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

        if self.name is not None and not isinstance(self.name, CcdhString):
            self.name = CcdhString(self.name)

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
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.Quantity.valueCodeableConcept"]] = None
    unitCode: Optional[Union[dict, Coding]] = None
    unit: Optional[Union[str, CcdhString]] = None
    comparator: Optional[Union[dict, Coding]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.Quantity.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.Quantity.valueCodeableConcept(self.valueCodeableConcept)

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

    research_project_type: Union[str, "EnumCRDC-H.ResearchProject.researchProjectType"] = None
    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CcdhString]] = None
    name_shortened: Optional[Union[str, CcdhString]] = None
    description: Optional[Union[str, CcdhString]] = None
    description_shortened: Optional[Union[str, CcdhString]] = None
    sponsor: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    primary_anatomic_site: Optional[Union[Union[str, "EnumCRDC-H.ResearchProject.primaryAnatomicSite"], List[Union[str, "EnumCRDC-H.ResearchProject.primaryAnatomicSite"]]]] = empty_list()
    url: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ResearchProject"], List[Union[dict, "ResearchProject"]]]] = empty_list()
    date_iacuc_approval: Optional[Union[str, CcdhDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.research_project_type is None:
            raise ValueError("research_project_type must be supplied")
        if not isinstance(self.research_project_type, EnumCRDC-H.ResearchProject.researchProjectType):
            self.research_project_type = EnumCRDC-H.ResearchProject.researchProjectType(self.research_project_type)

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
        self.primary_anatomic_site = [v if isinstance(v, EnumCRDC-H.ResearchProject.primaryAnatomicSite) else EnumCRDC-H.ResearchProject.primaryAnatomicSite(v) for v in self.primary_anatomic_site]

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
    member_of_research_project: Optional[Union[dict, ResearchProject]] = None
    age_at_enrollment: Optional[Union[dict, Quantity]] = None
    primary_diagnosis_condition: Optional[Union[str, "EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition"]] = None
    primary_diagnosis_site: Optional[Union[str, "EnumCRDC-H.ResearchSubject.primaryDiagnosisSite"]] = None
    primary_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    comorbid_diagnoses: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    index_timepoint: Optional[Union[str, "EnumCRDC-H.ResearchSubject.indexTimepoint"]] = None
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

        if self.member_of_research_project is not None and not isinstance(self.member_of_research_project, ResearchProject):
            self.member_of_research_project = ResearchProject(**self.member_of_research_project)

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, Quantity):
            self.age_at_enrollment = Quantity(**self.age_at_enrollment)

        if self.primary_diagnosis_condition is not None and not isinstance(self.primary_diagnosis_condition, EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition):
            self.primary_diagnosis_condition = EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition(self.primary_diagnosis_condition)

        if self.primary_diagnosis_site is not None and not isinstance(self.primary_diagnosis_site, EnumCRDC-H.ResearchSubject.primaryDiagnosisSite):
            self.primary_diagnosis_site = EnumCRDC-H.ResearchSubject.primaryDiagnosisSite(self.primary_diagnosis_site)

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

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, EnumCRDC-H.ResearchSubject.indexTimepoint):
            self.index_timepoint = EnumCRDC-H.ResearchSubject.indexTimepoint(self.index_timepoint)

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
    specimen_type: Optional[Union[str, "EnumCRDC-H.Specimen.specimenType"]] = None
    analyte_type: Optional[Union[str, "EnumCRDC-H.Specimen.analyteType"]] = None
    associated_project: Optional[Union[dict, ResearchProject]] = None
    data_provider: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[str, "EnumCRDC-H.Specimen.sourceMaterialType"]] = None
    parent_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    source_subject: Optional[Union[dict, "Subject"]] = None
    source_model_system: Optional[Union[dict, Entity]] = None
    tumor_status_at_collection: Optional[Union[str, "EnumCRDC-H.Specimen.tumorStatusAtCollection"]] = None
    creation_activity: Optional[Union[dict, "SpecimenCreationActivity"]] = None
    processing_activity: Optional[Union[Union[dict, "SpecimenProcessingActivity"], List[Union[dict, "SpecimenProcessingActivity"]]]] = empty_list()
    storage_activity: Optional[Union[dict, "SpecimenStorageActivity"]] = None
    transport_activity: Optional[Union[dict, "SpecimenTransportActivity"]] = None
    contained_in: Optional[Union[dict, "SpecimenContainer"]] = None
    dimensional_measure: Optional[Union[dict, Entity]] = None
    quantity_measure: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    quality_measure: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    cellular_composition_type: Optional[Union[str, "EnumCRDC-H.Specimen.cellularCompositionType"]] = None
    histological_composition_measure: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    general_tissue_morphology: Optional[Union[str, "EnumCRDC-H.Specimen.generalTissueMorphology"]] = None
    specific_tissue_morphology: Optional[Union[str, "EnumCRDC-H.Specimen.specificTissueMorphology"]] = None
    preinvasive_tissue_morphology: Optional[Union[str, "EnumCRDC-H.Specimen.preinvasiveTissueMorphology"]] = None
    morphology_pathologically_confirmed: Optional[Union[bool, CcdhBoolean]] = None
    morphology_assessor_role: Optional[Union[str, "EnumCRDC-H.Specimen.morphologyAssessorRole"]] = None
    morphlogy_assessment_method: Optional[Union[str, "EnumCRDC-H.Specimen.morphlogyAssessmentMethod"]] = None
    degree_of_dysplasia: Optional[Union[str, "EnumCRDC-H.Specimen.degreeOfDysplasia"]] = None
    dysplasia_fraction: Optional[Union[str, CcdhString]] = None
    related_document: Optional[Union[Union[dict, Document], List[Union[dict, Document]]]] = empty_list()
    section_location: Optional[Union[str, "EnumCRDC-H.Specimen.sectionLocation"]] = None
    derived_product: Optional[Union[Union[dict, BiologicProduct], List[Union[dict, BiologicProduct]]]] = empty_list()
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

        if self.specimen_type is not None and not isinstance(self.specimen_type, EnumCRDC-H.Specimen.specimenType):
            self.specimen_type = EnumCRDC-H.Specimen.specimenType(self.specimen_type)

        if self.analyte_type is not None and not isinstance(self.analyte_type, EnumCRDC-H.Specimen.analyteType):
            self.analyte_type = EnumCRDC-H.Specimen.analyteType(self.analyte_type)

        if self.associated_project is not None and not isinstance(self.associated_project, ResearchProject):
            self.associated_project = ResearchProject(**self.associated_project)

        if self.data_provider is not None and not isinstance(self.data_provider, Organization):
            self.data_provider = Organization(**self.data_provider)

        if self.source_material_type is not None and not isinstance(self.source_material_type, EnumCRDC-H.Specimen.sourceMaterialType):
            self.source_material_type = EnumCRDC-H.Specimen.sourceMaterialType(self.source_material_type)

        if self.parent_specimen is None:
            self.parent_specimen = []
        if not isinstance(self.parent_specimen, list):
            self.parent_specimen = [self.parent_specimen]
        self.parent_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.parent_specimen]

        if self.source_subject is not None and not isinstance(self.source_subject, Subject):
            self.source_subject = Subject(**self.source_subject)

        if self.source_model_system is not None and not isinstance(self.source_model_system, Entity):
            self.source_model_system = Entity(**self.source_model_system)

        if self.tumor_status_at_collection is not None and not isinstance(self.tumor_status_at_collection, EnumCRDC-H.Specimen.tumorStatusAtCollection):
            self.tumor_status_at_collection = EnumCRDC-H.Specimen.tumorStatusAtCollection(self.tumor_status_at_collection)

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
        self._normalize_inlined_slot(slot_name="quantity_measure", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

        if self.quality_measure is None:
            self.quality_measure = []
        if not isinstance(self.quality_measure, list):
            self.quality_measure = [self.quality_measure]
        self._normalize_inlined_slot(slot_name="quality_measure", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, EnumCRDC-H.Specimen.cellularCompositionType):
            self.cellular_composition_type = EnumCRDC-H.Specimen.cellularCompositionType(self.cellular_composition_type)

        if self.histological_composition_measure is None:
            self.histological_composition_measure = []
        if not isinstance(self.histological_composition_measure, list):
            self.histological_composition_measure = [self.histological_composition_measure]
        self._normalize_inlined_slot(slot_name="histological_composition_measure", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, EnumCRDC-H.Specimen.generalTissueMorphology):
            self.general_tissue_morphology = EnumCRDC-H.Specimen.generalTissueMorphology(self.general_tissue_morphology)

        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, EnumCRDC-H.Specimen.specificTissueMorphology):
            self.specific_tissue_morphology = EnumCRDC-H.Specimen.specificTissueMorphology(self.specific_tissue_morphology)

        if self.preinvasive_tissue_morphology is not None and not isinstance(self.preinvasive_tissue_morphology, EnumCRDC-H.Specimen.preinvasiveTissueMorphology):
            self.preinvasive_tissue_morphology = EnumCRDC-H.Specimen.preinvasiveTissueMorphology(self.preinvasive_tissue_morphology)

        if self.morphology_pathologically_confirmed is not None and not isinstance(self.morphology_pathologically_confirmed, CcdhBoolean):
            self.morphology_pathologically_confirmed = CcdhBoolean(self.morphology_pathologically_confirmed)

        if self.morphology_assessor_role is not None and not isinstance(self.morphology_assessor_role, EnumCRDC-H.Specimen.morphologyAssessorRole):
            self.morphology_assessor_role = EnumCRDC-H.Specimen.morphologyAssessorRole(self.morphology_assessor_role)

        if self.morphlogy_assessment_method is not None and not isinstance(self.morphlogy_assessment_method, EnumCRDC-H.Specimen.morphlogyAssessmentMethod):
            self.morphlogy_assessment_method = EnumCRDC-H.Specimen.morphlogyAssessmentMethod(self.morphlogy_assessment_method)

        if self.degree_of_dysplasia is not None and not isinstance(self.degree_of_dysplasia, EnumCRDC-H.Specimen.degreeOfDysplasia):
            self.degree_of_dysplasia = EnumCRDC-H.Specimen.degreeOfDysplasia(self.degree_of_dysplasia)

        if self.dysplasia_fraction is not None and not isinstance(self.dysplasia_fraction, CcdhString):
            self.dysplasia_fraction = CcdhString(self.dysplasia_fraction)

        if self.related_document is None:
            self.related_document = []
        if not isinstance(self.related_document, list):
            self.related_document = [self.related_document]
        self.related_document = [v if isinstance(v, Document) else Document(**v) for v in self.related_document]

        if self.section_location is not None and not isinstance(self.section_location, EnumCRDC-H.Specimen.sectionLocation):
            self.section_location = EnumCRDC-H.Specimen.sectionLocation(self.section_location)

        if self.derived_product is None:
            self.derived_product = []
        if not isinstance(self.derived_product, list):
            self.derived_product = [self.derived_product]
        self.derived_product = [v if isinstance(v, BiologicProduct) else BiologicProduct(**v) for v in self.derived_product]

        if self.distance_from_paired_specimen is not None and not isinstance(self.distance_from_paired_specimen, Quantity):
            self.distance_from_paired_specimen = Quantity(**self.distance_from_paired_specimen)

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
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    container_type: Optional[Union[str, "EnumCRDC-H.SpecimenContainer.containerType"]] = None
    container_number: Optional[Union[str, CcdhString]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    parent_container: Optional[Union[Union[dict, "SpecimenContainer"], List[Union[dict, "SpecimenContainer"]]]] = empty_list()
    charge_type: Optional[Union[str, "EnumCRDC-H.SpecimenContainer.chargeType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.container_type is not None and not isinstance(self.container_type, EnumCRDC-H.SpecimenContainer.containerType):
            self.container_type = EnumCRDC-H.SpecimenContainer.containerType(self.container_type)

        if self.container_number is not None and not isinstance(self.container_number, CcdhString):
            self.container_number = CcdhString(self.container_number)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Substance) else Substance(**v) for v in self.additive]

        if self.parent_container is None:
            self.parent_container = []
        if not isinstance(self.parent_container, list):
            self.parent_container = [self.parent_container]
        self.parent_container = [v if isinstance(v, SpecimenContainer) else SpecimenContainer(**v) for v in self.parent_container]

        if self.charge_type is not None and not isinstance(self.charge_type, EnumCRDC-H.SpecimenContainer.chargeType):
            self.charge_type = EnumCRDC-H.SpecimenContainer.chargeType(self.charge_type)

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

    activity_type: Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.activityType"]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    collection_method_type: Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.collectionMethodType"]] = None
    derivation_method_type: Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.derivationMethodType"]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    collection_site: Optional[Union[dict, BodySite]] = None
    input_specimen: Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]] = empty_list()
    quantity_collected: Optional[Union[dict, Quantity]] = None
    execution_observation: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    specimen_order: Optional[Union[str, CcdhString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, EnumCRDC-H.SpecimenCreationActivity.activityType):
            self.activity_type = EnumCRDC-H.SpecimenCreationActivity.activityType(self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.collection_method_type is not None and not isinstance(self.collection_method_type, EnumCRDC-H.SpecimenCreationActivity.collectionMethodType):
            self.collection_method_type = EnumCRDC-H.SpecimenCreationActivity.collectionMethodType(self.collection_method_type)

        if self.derivation_method_type is not None and not isinstance(self.derivation_method_type, EnumCRDC-H.SpecimenCreationActivity.derivationMethodType):
            self.derivation_method_type = EnumCRDC-H.SpecimenCreationActivity.derivationMethodType(self.derivation_method_type)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Substance) else Substance(**v) for v in self.additive]

        if self.collection_site is not None and not isinstance(self.collection_site, BodySite):
            self.collection_site = BodySite(**self.collection_site)

        if self.input_specimen is None:
            self.input_specimen = []
        if not isinstance(self.input_specimen, list):
            self.input_specimen = [self.input_specimen]
        self.input_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.input_specimen]

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, Quantity):
            self.quantity_collected = Quantity(**self.quantity_collected)

        if self.execution_observation is None:
            self.execution_observation = []
        if not isinstance(self.execution_observation, list):
            self.execution_observation = [self.execution_observation]
        self._normalize_inlined_slot(slot_name="execution_observation", slot_type=Observation, key_name="id", inlined_as_list=True, keyed=False)

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

    activity_type: Optional[Union[str, "EnumCRDC-H.SpecimenProcessingActivity.activityType"]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.SpecimenProcessingActivity.methodType"]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    execution_observation: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, EnumCRDC-H.SpecimenProcessingActivity.activityType):
            self.activity_type = EnumCRDC-H.SpecimenProcessingActivity.activityType(self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.duration is None:
            self.duration = []
        if not isinstance(self.duration, list):
            self.duration = [self.duration]
        self.duration = [v if isinstance(v, Entity) else Entity(**v) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.SpecimenProcessingActivity.methodType):
            self.method_type = EnumCRDC-H.SpecimenProcessingActivity.methodType(self.method_type)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Substance) else Substance(**v) for v in self.additive]

        if self.execution_observation is None:
            self.execution_observation = []
        if not isinstance(self.execution_observation, list):
            self.execution_observation = [self.execution_observation]
        self.execution_observation = [v if isinstance(v, Entity) else Entity(**v) for v in self.execution_observation]

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

    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[dict, Quantity]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.SpecimenStorageActivity.methodType"]] = None
    container: Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.duration is not None and not isinstance(self.duration, Quantity):
            self.duration = Quantity(**self.duration)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.SpecimenStorageActivity.methodType):
            self.method_type = EnumCRDC-H.SpecimenStorageActivity.methodType(self.method_type)

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

    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    transport_origin: Optional[Union[dict, Organization]] = None
    transport_destination: Optional[Union[dict, Organization]] = None
    execution_observation: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    execution_conditions: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.duration is None:
            self.duration = []
        if not isinstance(self.duration, list):
            self.duration = [self.duration]
        self.duration = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.transport_origin is not None and not isinstance(self.transport_origin, Organization):
            self.transport_origin = Organization(**self.transport_origin)

        if self.transport_destination is not None and not isinstance(self.transport_destination, Organization):
            self.transport_destination = Organization(**self.transport_destination)

        if self.execution_observation is None:
            self.execution_observation = []
        if not isinstance(self.execution_observation, list):
            self.execution_observation = [self.execution_observation]
        self.execution_observation = [v if isinstance(v, Entity) else Entity(**v) for v in self.execution_observation]

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
    species: Optional[Union[str, "EnumCRDC-H.Subject.species"]] = None
    breed: Optional[Union[str, "EnumCRDC-H.Subject.breed"]] = None
    sex: Optional[Union[str, "EnumCRDC-H.Subject.sex"]] = None
    ethnicity: Optional[Union[str, "EnumCRDC-H.Subject.ethnicity"]] = None
    race: Optional[Union[Union[str, "EnumCRDC-H.Subject.race"], List[Union[str, "EnumCRDC-H.Subject.race"]]]] = empty_list()
    year_of_birth: Optional[Union[int, CcdhInteger]] = None
    vital_status: Optional[Union[str, "EnumCRDC-H.Subject.vitalStatus"]] = None
    age_at_death: Optional[Union[dict, Quantity]] = None
    year_of_death: Optional[Union[int, CcdhInteger]] = None
    cause_of_death: Optional[Union[str, "EnumCRDC-H.Subject.causeOfDeath"]] = None

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

        if self.species is not None and not isinstance(self.species, EnumCRDC-H.Subject.species):
            self.species = EnumCRDC-H.Subject.species(self.species)

        if self.breed is not None and not isinstance(self.breed, EnumCRDC-H.Subject.breed):
            self.breed = EnumCRDC-H.Subject.breed(self.breed)

        if self.sex is not None and not isinstance(self.sex, EnumCRDC-H.Subject.sex):
            self.sex = EnumCRDC-H.Subject.sex(self.sex)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EnumCRDC-H.Subject.ethnicity):
            self.ethnicity = EnumCRDC-H.Subject.ethnicity(self.ethnicity)

        if self.race is None:
            self.race = []
        if not isinstance(self.race, list):
            self.race = [self.race]
        self.race = [v if isinstance(v, EnumCRDC-H.Subject.race) else EnumCRDC-H.Subject.race(v) for v in self.race]

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, CcdhInteger):
            self.year_of_birth = CcdhInteger(self.year_of_birth)

        if self.vital_status is not None and not isinstance(self.vital_status, EnumCRDC-H.Subject.vitalStatus):
            self.vital_status = EnumCRDC-H.Subject.vitalStatus(self.vital_status)

        if self.age_at_death is not None and not isinstance(self.age_at_death, Quantity):
            self.age_at_death = Quantity(**self.age_at_death)

        if self.year_of_death is not None and not isinstance(self.year_of_death, CcdhInteger):
            self.year_of_death = CcdhInteger(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, EnumCRDC-H.Subject.causeOfDeath):
            self.cause_of_death = EnumCRDC-H.Subject.causeOfDeath(self.cause_of_death)

        super().__post_init__(**kwargs)


@dataclass
class Substance(Entity):
    """
    A type of material substance, or instance thereof, as used in a particular application. May include information
    about the role the substance played in a particular application.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Substance
    class_class_curie: ClassVar[str] = "ccdh:Substance"
    class_name: ClassVar[str] = "Substance"
    class_model_uri: ClassVar[URIRef] = CCDH.Substance

    substance_type: Optional[Union[str, "EnumCRDC-H.Substance.substanceType"]] = None
    role: Optional[Union[Union[str, "EnumCRDC-H.Substance.role"], List[Union[str, "EnumCRDC-H.Substance.role"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.substance_type is not None and not isinstance(self.substance_type, EnumCRDC-H.Substance.substanceType):
            self.substance_type = EnumCRDC-H.Substance.substanceType(self.substance_type)

        if self.role is None:
            self.role = []
        if not isinstance(self.role, list):
            self.role = [self.role]
        self.role = [v if isinstance(v, EnumCRDC-H.Substance.role) else EnumCRDC-H.Substance.role(v) for v in self.role]

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
    indexEventType: Optional[Union[str, "EnumCRDC-H.TimePoint.indexEventType"]] = None
    offsetFromIndex: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dateTime is not None and not isinstance(self.dateTime, CcdhDateTime):
            self.dateTime = CcdhDateTime(self.dateTime)

        if self.indexDate is not None and not isinstance(self.indexDate, CcdhDateTime):
            self.indexDate = CcdhDateTime(self.indexDate)

        if self.indexEventType is not None and not isinstance(self.indexEventType, EnumCRDC-H.TimePoint.indexEventType):
            self.indexEventType = EnumCRDC-H.TimePoint.indexEventType(self.indexEventType)

        if self.offsetFromIndex is not None and not isinstance(self.offsetFromIndex, Quantity):
            self.offsetFromIndex = Quantity(**self.offsetFromIndex)

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
    type: Optional[Union[str, "EnumCRDC-H.Treatment.type"]] = None
    therapeutic_agent: Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]] = empty_list()
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

        if self.type is not None and not isinstance(self.type, EnumCRDC-H.Treatment.type):
            self.type = EnumCRDC-H.Treatment.type(self.type)

        if self.therapeutic_agent is None:
            self.therapeutic_agent = []
        if not isinstance(self.therapeutic_agent, list):
            self.therapeutic_agent = [self.therapeutic_agent]
        self.therapeutic_agent = [v if isinstance(v, Substance) else Substance(**v) for v in self.therapeutic_agent]

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
class EnumCRDC-H.BodySite.site(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite site
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BodySite.site",
        description="Autogenerated Enumeration for CRDC-H BodySite site",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.154272+00:00",
    )

class EnumCRDC-H.BodySite.qualifier(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite qualifier
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BodySite.qualifier",
        description="Autogenerated Enumeration for CRDC-H BodySite qualifier",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.349541+00:00",
    )

class EnumCRDC-H.BiologicProduct.productType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BiologicProduct product_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BiologicProduct.productType",
        description="Autogenerated Enumeration for CRDC-H BiologicProduct product_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.498021+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation observation_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.644138+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.794118+00:00",
    )

class EnumCRDC-H.CancerGradeObservationSet.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservationSet method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservationSet.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:42.944468+00:00",
    )

class EnumCRDC-H.CancerStageObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation observation_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:43.091737+00:00",
    )

class EnumCRDC-H.CancerStageObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-27T15:46:43.241295+00:00",
    )

class EnumCRDC-H.CancerStageObservationSet.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservationSet category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservationSet.category",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservationSet category",
        code_set=None,
        code_set_version="2021-05-27T15:46:43.401800+00:00",
    )

class EnumCRDC-H.CancerStageObservationSet.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservationSet method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservationSet.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:43.562096+00:00",
    )

class EnumCRDC-H.Diagnosis.condition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis condition
    """
    Carcinofibroma = PermissibleValue(text="Carcinofibroma",
                                                   description="Carcinofibroma")
    Esthesioneurocytoma = PermissibleValue(text="Esthesioneurocytoma",
                                                             description="Esthesioneurocytoma")
    Osteofibroma = PermissibleValue(text="Osteofibroma",
                                               description="Osteofibroma")
    Sympathicoblastoma = PermissibleValue(text="Sympathicoblastoma",
                                                           description="Sympathicoblastoma")
    C155863 = PermissibleValue(text="C155863",
                                     description="Poorly Differentiated Neuroendocrine Lesion",
                                     meaning=NCIT.C155863)
    C155861 = PermissibleValue(text="C155861",
                                     description="Well Differentiated Neuroendocrine Lesion",
                                     meaning=NCIT.C155861)
    C127915 = PermissibleValue(text="C127915",
                                     description="Cervical Adenocarcinoma Admixed with Neuroendocrine Carcinoma",
                                     meaning=NCIT.C127915)
    C7364 = PermissibleValue(text="C7364",
                                 description="Diffuse Intraductal Papillomatosis",
                                 meaning=NCIT.C7364)
    C40194 = PermissibleValue(text="C40194",
                                   description="Cervical Squamotransitional Carcinoma",
                                   meaning=NCIT.C40194)
    C39912 = PermissibleValue(text="C39912",
                                   description="Testicular Mixed Germ Cell-Sex Cord-Stromal Tumor, Unclassified",
                                   meaning=NCIT.C39912)
    C47848 = PermissibleValue(text="C47848",
                                   description="Breast Carcinoma with Osseous Metaplasia",
                                   meaning=NCIT.C47848)
    C97049 = PermissibleValue(text="C97049",
                                   description="Invasive Breast Lobular Carcinoma, Alveolar Variant",
                                   meaning=NCIT.C97049)
    C97052 = PermissibleValue(text="C97052",
                                   description="Invasive Breast Lobular Carcinoma, Solid Variant",
                                   meaning=NCIT.C97052)
    C97051 = PermissibleValue(text="C97051",
                                   description="Invasive Breast Lobular Carcinoma, Pleomorphic Variant",
                                   meaning=NCIT.C97051)
    C173720 = PermissibleValue(text="C173720",
                                     description="Odontogenic Carcinoma",
                                     meaning=NCIT.C173720)
    C173738 = PermissibleValue(text="C173738",
                                     description="Odontogenic Sarcoma",
                                     meaning=NCIT.C173738)
    C173739 = PermissibleValue(text="C173739",
                                     description="Ameloblastic Fibrodentinosarcoma",
                                     meaning=NCIT.C173739)
    C121789 = PermissibleValue(text="C121789",
                                     description="Malignant Phosphaturic Mesenchymal Tumor",
                                     meaning=NCIT.C121789)
    C121797 = PermissibleValue(text="C121797",
                                     description="Undifferentiated Spindle Cell Sarcoma",
                                     meaning=NCIT.C121797)
    C121802 = PermissibleValue(text="C121802",
                                     description="Undifferentiated Epithelioid Sarcoma",
                                     meaning=NCIT.C121802)
    C121655 = PermissibleValue(text="C121655",
                                     description="Sclerosing Rhabdomyosarcoma",
                                     meaning=NCIT.C121655)
    C154494 = PermissibleValue(text="C154494",
                                     description="MiT Family Translocation-Associated Renal Cell Carcinoma",
                                     meaning=NCIT.C154494)
    C129443 = PermissibleValue(text="C129443",
                                     description="Medulloblastoma, SHH-Activated, TP53-Wildtype",
                                     meaning=NCIT.C129443)
    C129445 = PermissibleValue(text="C129445",
                                     description="Medulloblastoma, Non-WNT/Non-SHH, Group 3",
                                     meaning=NCIT.C129445)
    C129293 = PermissibleValue(text="C129293",
                                     description="Epithelioid Glioblastoma",
                                     meaning=NCIT.C129293)
    C129446 = PermissibleValue(text="C129446",
                                     description="Medulloblastoma, Non-WNT/Non-SHH, Group 4",
                                     meaning=NCIT.C129446)
    C127907 = PermissibleValue(text="C127907",
                                     description="Endocervical Adenocarcinoma, Usual Type",
                                     meaning=NCIT.C127907)
    C45202 = PermissibleValue(text="C45202",
                                   description="Low Grade Fibromyxoid Sarcoma",
                                   meaning=NCIT.C45202)
    C40017 = PermissibleValue(text="C40017",
                                   description="Rete Ovarii Adenocarcinoma",
                                   meaning=NCIT.C40017)
    C40203 = PermissibleValue(text="C40203",
                                   description="Cervical Mucinous Adenocarcinoma, Intestinal-Type",
                                   meaning=NCIT.C40203)
    C39827 = PermissibleValue(text="C39827",
                                   description="Infiltrating Bladder Urothelial Carcinoma, Clear Cell Variant",
                                   meaning=NCIT.C39827)
    C39820 = PermissibleValue(text="C39820",
                                   description="Infiltrating Bladder Urothelial Carcinoma, Microcystic Variant",
                                   meaning=NCIT.C39820)
    C39818 = PermissibleValue(text="C39818",
                                   description="Infiltrating Bladder Urothelial Carcinoma with Trophoblastic Differentiation",
                                   meaning=NCIT.C39818)
    C39819 = PermissibleValue(text="C39819",
                                   description="Infiltrating Bladder Urothelial Carcinoma, Nested Variant",
                                   meaning=NCIT.C39819)
    C54039 = PermissibleValue(text="C54039",
                                   description="Classic Medulloblastoma",
                                   meaning=NCIT.C54039)
    C47847 = PermissibleValue(text="C47847",
                                   description="Breast Carcinoma with Chondroid Metaplasia",
                                   meaning=NCIT.C47847)
    C27846 = PermissibleValue(text="C27846",
                                   description="Villoglandular Endometrial Endometrioid Adenocarcinoma",
                                   meaning=NCIT.C27846)
    C142827 = PermissibleValue(text="C142827",
                                     description="Pulmonary Myxoid Sarcoma with EWSR1-CREB1 Translocation",
                                     meaning=NCIT.C142827)
    C121786 = PermissibleValue(text="C121786",
                                     description="Mixed Tumor, Not Otherwise Specified",
                                     meaning=NCIT.C121786)
    C129424 = PermissibleValue(text="C129424",
                                     description="Diffuse Leptomeningeal Glioneuronal Tumor",
                                     meaning=NCIT.C129424)
    C7572 = PermissibleValue(text="C7572",
                                 description="Kidney Medullary Carcinoma",
                                 meaning=NCIT.C7572)
    C6870 = PermissibleValue(text="C6870",
                                 description="Breast Solid Papillary Carcinoma",
                                 meaning=NCIT.C6870)
    C40208 = PermissibleValue(text="C40208",
                                   description="Cervical Villoglandular Adenocarcinoma",
                                   meaning=NCIT.C40208)
    C40362 = PermissibleValue(text="C40362",
                                   description="Low Grade Breast Adenosquamous Carcinoma",
                                   meaning=NCIT.C40362)
    C40440 = PermissibleValue(text="C40440",
                                   description="Ovarian Small Cell Carcinoma, Pulmonary-Type",
                                   meaning=NCIT.C40440)
    C39828 = PermissibleValue(text="C39828",
                                   description="Infiltrating Bladder Urothelial Carcinoma, Lipid-Rich Variant",
                                   meaning=NCIT.C39828)
    C49027 = PermissibleValue(text="C49027",
                                   description="Sclerosing Epithelioid Fibrosarcoma",
                                   meaning=NCIT.C49027)
    C9502 = PermissibleValue(text="C9502",
                                 description="Myolipoma",
                                 meaning=NCIT.C9502)
    C96878 = PermissibleValue(text="C96878",
                                   description="Gallbladder Intracholecystic Papillary (Tubular) Neoplasm with Intermediate Grade Intraepithelial Neoplasia",
                                   meaning=NCIT.C96878)
    C27260 = PermissibleValue(text="C27260",
                                   description="Dendritic Cell Tumor, Not Otherwise Specified",
                                   meaning=NCIT.C27260)
    C121799 = PermissibleValue(text="C121799",
                                     description="Undifferentiated Round Cell Sarcoma",
                                     meaning=NCIT.C121799)
    C129271 = PermissibleValue(text="C129271",
                                     description="Diffuse Astrocytoma, IDH-Mutant",
                                     meaning=NCIT.C129271)
    C129318 = PermissibleValue(text="C129318",
                                     description="Oligodendroglioma, IDH-Mutant and 1p/19q-Codeleted",
                                     meaning=NCIT.C129318)
    C129321 = PermissibleValue(text="C129321",
                                     description="Anaplastic Oligodendroglioma, IDH-Mutant and 1p/19q-Codeleted",
                                     meaning=NCIT.C129321)
    C129291 = PermissibleValue(text="C129291",
                                     description="Anaplastic Astrocytoma, IDH-Wildtype",
                                     meaning=NCIT.C129291)
    C129528 = PermissibleValue(text="C129528",
                                     description="Central Nervous System Solitary Fibrous Tumor/Hemangiopericytoma, Grade 2",
                                     meaning=NCIT.C129528)
    C129274 = PermissibleValue(text="C129274",
                                     description="Diffuse Astrocytoma, IDH-Wildtype",
                                     meaning=NCIT.C129274)
    C129290 = PermissibleValue(text="C129290",
                                     description="Anaplastic Astrocytoma, IDH-Mutant",
                                     meaning=NCIT.C129290)
    C129327 = PermissibleValue(text="C129327",
                                     description="Anaplastic Pleomorphic Xanthoastrocytoma",
                                     meaning=NCIT.C129327)
    C66925 = PermissibleValue(text="C66925",
                                   description="Enteroglucagonoma",
                                   meaning=NCIT.C66925)
    C8972 = PermissibleValue(text="C8972",
                                 description="Uterine Corpus Undifferentiated Sarcoma",
                                 meaning=NCIT.C8972)
    C9019 = PermissibleValue(text="C9019",
                                 description="Acute Myeloid Leukemia with t(16;16)(p13.1;q22); CBFB-MYH11",
                                 meaning=NCIT.C9019)
    C5568 = PermissibleValue(text="C5568",
                                 description="Skin Nodulo-Ulcerative Basal Cell Carcinoma",
                                 meaning=NCIT.C5568)
    C4375 = PermissibleValue(text="C4375",
                                 description="Nesidioblastosis",
                                 meaning=NCIT.C4375)
    C45194 = PermissibleValue(text="C45194",
                                   description="Primary Cutaneous Diffuse Large B-Cell Lymphoma, Leg Type",
                                   meaning=NCIT.C45194)
    C40439 = PermissibleValue(text="C40439",
                                   description="Ovarian Small Cell Carcinoma, Hypercalcemic Type",
                                   meaning=NCIT.C40439)
    C39750 = PermissibleValue(text="C39750",
                                   description="Glioblastoma, IDH-Wildtype",
                                   meaning=NCIT.C39750)
    C6530 = PermissibleValue(text="C6530",
                                 description="Malignant Pericytic Neoplasm",
                                 meaning=NCIT.C6530)
    C62192 = PermissibleValue(text="C62192",
                                   description="Salivary Gland Intraductal Carcinoma",
                                   meaning=NCIT.C62192)
    C36310 = PermissibleValue(text="C36310",
                                   description="Secondary Carcinoma",
                                   meaning=NCIT.C36310)
    C35382 = PermissibleValue(text="C35382",
                                   description="True Histiocytic Lymphoma",
                                   meaning=NCIT.C35382)
    C176979 = PermissibleValue(text="C176979",
                                     description="Lipoma-Like Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                     meaning=NCIT.C176979)
    C126303 = PermissibleValue(text="C126303",
                                     description="Tubulocystic Renal Cell Carcinoma",
                                     meaning=NCIT.C126303)
    C129527 = PermissibleValue(text="C129527",
                                     description="Central Nervous System Solitary Fibrous Tumor/Hemangiopericytoma, Grade 3",
                                     meaning=NCIT.C129527)
    C6910 = PermissibleValue(text="C6910",
                                 description="Melanotic Psammomatous Malignant Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C6910)
    C7167 = PermissibleValue(text="C7167",
                                 description="Myelodysplastic Syndrome with Excess Blasts-1",
                                 meaning=NCIT.C7167)
    C6879 = PermissibleValue(text="C6879",
                                 description="Pancreatic Mixed Ductal-Neuroendocrine Carcinoma",
                                 meaning=NCIT.C6879)
    C4230 = PermissibleValue(text="C4230",
                                 description="Optic Disc Melanocytoma",
                                 meaning=NCIT.C4230)
    C45339 = PermissibleValue(text="C45339",
                                   description="Primary Cutaneous CD8-Positive Aggressive Epidermotropic Cytotoxic T-Cell Lymphoma",
                                   meaning=NCIT.C45339)
    C5317 = PermissibleValue(text="C5317",
                                 description="Meningeal Melanoma",
                                 meaning=NCIT.C5317)
    C9379 = PermissibleValue(text="C9379",
                                 description="Combined Lung Small Cell Carcinoma and Lung Adenocarcinoma",
                                 meaning=NCIT.C9379)
    C27426 = PermissibleValue(text="C27426",
                                   description="High Grade Esophageal Squamous Intraepithelial Neoplasia",
                                   meaning=NCIT.C27426)
    C9018 = PermissibleValue(text="C9018",
                                 description="Acute Myeloid Leukemia with inv(16)(p13.1q22); CBFB-MYH11",
                                 meaning=NCIT.C9018)
    C7267 = PermissibleValue(text="C7267",
                                 description="Combined Lung Large Cell Neuroendocrine Carcinoma",
                                 meaning=NCIT.C7267)
    C5530 = PermissibleValue(text="C5530",
                                 description="Prostate Acinar Adenocarcinoma, Sarcomatoid Variant",
                                 meaning=NCIT.C5530)
    C39816 = PermissibleValue(text="C39816",
                                   description="Infiltrating Bladder Urothelial Carcinoma with Squamous Differentiation",
                                   meaning=NCIT.C39816)
    C39807 = PermissibleValue(text="C39807",
                                   description="Mucinous Tubular and Spindle Cell Carcinoma of the Kidney",
                                   meaning=NCIT.C39807)
    C94537 = PermissibleValue(text="C94537",
                                   description="Spindle Cell Oncocytoma",
                                   meaning=NCIT.C94537)
    C5904 = PermissibleValue(text="C5904",
                                 description="Salivary Duct Carcinoma",
                                 meaning=NCIT.C5904)
    C95506 = PermissibleValue(text="C95506",
                                   description="Pancreatic Intraductal Tubulopapillary Neoplasm",
                                   meaning=NCIT.C95506)
    C3751 = PermissibleValue(text="C3751",
                                 description="Smooth Muscle Neoplasm",
                                 meaning=NCIT.C3751)
    C142825 = PermissibleValue(text="C142825",
                                     description="Pulmonary Artery Intimal Sarcoma",
                                     meaning=NCIT.C142825)
    C27258 = PermissibleValue(text="C27258",
                                   description="Malignant Lymphoma, Non-Cleaved Cell Type",
                                   meaning=NCIT.C27258)
    C8563 = PermissibleValue(text="C8563",
                                 description="Undifferentiated High Grade Pleomorphic Sarcoma of Bone",
                                 meaning=NCIT.C8563)
    C6290 = PermissibleValue(text="C6290",
                                 description="Endometrial Endometrioid Adenocarcinoma, Variant with Squamous Differentiation",
                                 meaning=NCIT.C6290)
    C7159 = PermissibleValue(text="C7159",
                                 description="Subepidermal Nodular Fibrosis",
                                 meaning=NCIT.C7159)
    C27270 = PermissibleValue(text="C27270",
                                   description="Hodgkin's Disease, Nodular Sclerosis, Lymphocyte Predominance",
                                   meaning=NCIT.C27270)
    C27098 = PermissibleValue(text="C27098",
                                   description="Hodgkin's Disease, Nodular Sclerosis, Mixed Cellularity",
                                   meaning=NCIT.C27098)
    C27821 = PermissibleValue(text="C27821",
                                   description="Malignant Lymphoma, Convoluted",
                                   meaning=NCIT.C27821)
    C3005 = PermissibleValue(text="C3005",
                                 description="Tumor Embolism",
                                 meaning=NCIT.C3005)
    C122585 = PermissibleValue(text="C122585",
                                     description="Borderline Ovarian Serous Tumor-Micropapillary Variant/Non-Invasive Low Grade Ovarian Serous Carcinoma",
                                     meaning=NCIT.C122585)
    C136716 = PermissibleValue(text="C136716",
                                     description="Lung Non-Mucinous Adenocarcinoma In Situ",
                                     meaning=NCIT.C136716)
    C136717 = PermissibleValue(text="C136717",
                                     description="Lung Mucinous Adenocarcinoma In Situ",
                                     meaning=NCIT.C136717)
    C127905 = PermissibleValue(text="C127905",
                                     description="Cervical Mucinous Adenocarcinoma, Gastric Type",
                                     meaning=NCIT.C127905)
    C7680 = PermissibleValue(text="C7680",
                                 description="Adenocarcinoma In Situ in a Polyp",
                                 meaning=NCIT.C7680)
    C7681 = PermissibleValue(text="C7681",
                                 description="Carcinoma In Situ in a Polyp",
                                 meaning=NCIT.C7681)
    C9010 = PermissibleValue(text="C9010",
                                 description="Mixed Teratoma and Seminoma",
                                 meaning=NCIT.C9010)
    C9014 = PermissibleValue(text="C9014",
                                 description="Cystic Teratoma",
                                 meaning=NCIT.C9014)
    C9012 = PermissibleValue(text="C9012",
                                 description="Adult Cystic Teratoma",
                                 meaning=NCIT.C9012)
    C8994 = PermissibleValue(text="C8994",
                                 description="Malignant Lymphoma Centroblastic, Follicular",
                                 meaning=NCIT.C8994)
    C8979 = PermissibleValue(text="C8979",
                                 description="Mucinous Cystadenofibroma",
                                 meaning=NCIT.C8979)
    C6880 = PermissibleValue(text="C6880",
                                 description="Glandular Papilloma",
                                 meaning=NCIT.C6880)
    C45733 = PermissibleValue(text="C45733",
                                   description="Malignant Mediastinal Germ Cell Tumor with Associated Hematologic Malignancy",
                                   meaning=NCIT.C45733)
    C35725 = PermissibleValue(text="C35725",
                                   description="Grade II Neuroendocrine Carcinoma",
                                   meaning=NCIT.C35725)
    C34774 = PermissibleValue(text="C34774",
                                   description="Chronic Monocytic Leukemia",
                                   meaning=NCIT.C34774)
    C27823 = PermissibleValue(text="C27823",
                                   description="Malignant Lymphoma, Large Cell Type",
                                   meaning=NCIT.C27823)
    C27352 = PermissibleValue(text="C27352",
                                   description="Peripheral T-Cell Lymphoma, Large Cell",
                                   meaning=NCIT.C27352)
    C27822 = PermissibleValue(text="C27822",
                                   description="Diffuse Malignant Lymphoma",
                                   meaning=NCIT.C27822)
    C27288 = PermissibleValue(text="C27288",
                                   description="Ovarian Endometrioid Cystadenofibroma",
                                   meaning=NCIT.C27288)
    C27799 = PermissibleValue(text="C27799",
                                   description="Pre-Pre-B Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27799)
    C27099 = PermissibleValue(text="C27099",
                                   description="Malignant Lymphoma, Histiocytic, Diffuse",
                                   meaning=NCIT.C27099)
    C27808 = PermissibleValue(text="C27808",
                                   description="Hodgkin's Disease, Nodular Sclerosis, Lymphocyte Depletion",
                                   meaning=NCIT.C27808)
    C3356 = PermissibleValue(text="C3356",
                                 description="Solitary Reticulohistiocytoma",
                                 meaning=NCIT.C3356)
    C121774 = PermissibleValue(text="C121774",
                                     description="Malignant Ossifying Fibromyxoid Tumor",
                                     meaning=NCIT.C121774)
    C150701 = PermissibleValue(text="C150701",
                                     description="Langerhans Cell Histiocytosis, Monostotic",
                                     meaning=NCIT.C150701)
    C150702 = PermissibleValue(text="C150702",
                                     description="Langerhans Cell Histiocytosis, Polyostotic",
                                     meaning=NCIT.C150702)
    C37272 = PermissibleValue(text="C37272",
                                   description="Vulvar Intraepithelial Neoplasia, Differentiated Type",
                                   meaning=NCIT.C37272)
    C7685 = PermissibleValue(text="C7685",
                                 description="Adenocarcinoma with Cartilaginous Metaplasia",
                                 meaning=NCIT.C7685)
    C7679 = PermissibleValue(text="C7679",
                                 description="Adenocarcinoma In Situ in Tubular Adenoma",
                                 meaning=NCIT.C7679)
    C7677 = PermissibleValue(text="C7677",
                                 description="Adenocarcinoma in Tubular Adenoma",
                                 meaning=NCIT.C7677)
    C7684 = PermissibleValue(text="C7684",
                                 description="Adenocarcinoma with Osseous Metaplasia",
                                 meaning=NCIT.C7684)
    C7603 = PermissibleValue(text="C7603",
                                 description="Regressing Nevus",
                                 meaning=NCIT.C7603)
    C7567 = PermissibleValue(text="C7567",
                                 description="Clear Cell Hidradenoma",
                                 meaning=NCIT.C7567)
    C8986 = PermissibleValue(text="C8986",
                                 description="Papillary Adenofibroma",
                                 meaning=NCIT.C8986)
    C8985 = PermissibleValue(text="C8985",
                                 description="Cystadenofibroma",
                                 meaning=NCIT.C8985)
    C8988 = PermissibleValue(text="C8988",
                                 description="Clear Cell Cystadenofibroma",
                                 meaning=NCIT.C8988)
    C8461 = PermissibleValue(text="C8461",
                                 description="Tibial Adamantinoma",
                                 meaning=NCIT.C8461)
    C7204 = PermissibleValue(text="C7204",
                                 description="T-Zone Variant Peripheral T-Cell Lymphoma",
                                 meaning=NCIT.C7204)
    C7449 = PermissibleValue(text="C7449",
                                 description="Infiltrating Angiolipoma",
                                 meaning=NCIT.C7449)
    C7452 = PermissibleValue(text="C7452",
                                 description="Odontogenic Myxofibroma",
                                 meaning=NCIT.C7452)
    C7451 = PermissibleValue(text="C7451",
                                 description="Infiltrating Lipoma",
                                 meaning=NCIT.C7451)
    C7176 = PermissibleValue(text="C7176",
                                 description="Aleukemic Chronic Lymphocytic Leukemia",
                                 meaning=NCIT.C7176)
    C6907 = PermissibleValue(text="C6907",
                                 description="Metaplastic Meningioma",
                                 meaning=NCIT.C6907)
    C6895 = PermissibleValue(text="C6895",
                                 description="Atypical Polypoid Adenomyoma",
                                 meaning=NCIT.C6895)
    C43342 = PermissibleValue(text="C43342",
                                   description="Apocrine Hidrocystoma",
                                   meaning=NCIT.C43342)
    C4339 = PermissibleValue(text="C4339",
                                 description="Multifocal Lymphomatous Polyposis",
                                 meaning=NCIT.C4339)
    C54000 = PermissibleValue(text="C54000",
                                   description="Gastrointestinal Stromal Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C54000)
    C3892 = PermissibleValue(text="C3892",
                                 description="Mu Heavy Chain Disease",
                                 meaning=NCIT.C3892)
    C4718 = PermissibleValue(text="C4718",
                                 description="Secretory Meningioma",
                                 meaning=NCIT.C4718)
    C4721 = PermissibleValue(text="C4721",
                                 description="Microcystic Meningioma",
                                 meaning=NCIT.C4721)
    C4713 = PermissibleValue(text="C4713",
                                 description="Cellular Ependymoma",
                                 meaning=NCIT.C4713)
    C4714 = PermissibleValue(text="C4714",
                                 description="Clear Cell Ependymoma",
                                 meaning=NCIT.C4714)
    C4720 = PermissibleValue(text="C4720",
                                 description="Lymphoplasmacyte-Rich Meningioma",
                                 meaning=NCIT.C4720)
    C92625 = PermissibleValue(text="C92625",
                                   description="Anaplastic Medulloblastoma",
                                   meaning=NCIT.C92625)
    C97053 = PermissibleValue(text="C97053",
                                   description="Invasive Breast Lobular Carcinoma, Tubulolobular Variant",
                                   meaning=NCIT.C97053)
    C35794 = PermissibleValue(text="C35794",
                                   description="Pagetoid Reticulosis",
                                   meaning=NCIT.C35794)
    C27257 = PermissibleValue(text="C27257",
                                   description="Cellular Angiofibroma",
                                   meaning=NCIT.C27257)
    C27256 = PermissibleValue(text="C27256",
                                   description="Giant Cell Angiofibroma",
                                   meaning=NCIT.C27256)
    C27290 = PermissibleValue(text="C27290",
                                   description="L1 Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27290)
    C27547 = PermissibleValue(text="C27547",
                                   description="Fibrosarcomatous Dermatofibrosarcoma Protuberans",
                                   meaning=NCIT.C27547)
    C3203 = PermissibleValue(text="C3203",
                                 description="Acquired Progressive Lymphangioma",
                                 meaning=NCIT.C3203)
    C173928 = PermissibleValue(text="C173928",
                                     description="Periapical Cemento-Osseous Dysplasia",
                                     meaning=NCIT.C173928)
    C156122 = PermissibleValue(text="C156122",
                                     description="Thyroid Gland Follicular Carcinoma, Encapsulated Angioinvasive",
                                     meaning=NCIT.C156122)
    C129499 = PermissibleValue(text="C129499",
                                     description="Embryonal Tumor with Multilayered Rosettes, Not Otherwise Specified",
                                     meaning=NCIT.C129499)
    C129431 = PermissibleValue(text="C129431",
                                     description="Rosette-Forming Glioneuronal Tumor",
                                     meaning=NCIT.C129431)
    C129501 = PermissibleValue(text="C129501",
                                     description="Central Nervous System Embryonal Tumor with Rhabdoid Features",
                                     meaning=NCIT.C129501)
    C7682 = PermissibleValue(text="C7682",
                                 description="Carcinoma in a Polyp",
                                 meaning=NCIT.C7682)
    C7643 = PermissibleValue(text="C7643",
                                 description="Alkylating Agent-Related Myelodysplastic Syndrome",
                                 meaning=NCIT.C7643)
    C7565 = PermissibleValue(text="C7565",
                                 description="Eccrine Hidrocystoma",
                                 meaning=NCIT.C7565)
    C7642 = PermissibleValue(text="C7642",
                                 description="Epipodophyllotoxin-Related Myelodysplastic Syndrome",
                                 meaning=NCIT.C7642)
    C80308 = PermissibleValue(text="C80308",
                                   description="Splenic B-Cell Lymphoma/Leukemia, Unclassifiable",
                                   meaning=NCIT.C80308)
    C80309 = PermissibleValue(text="C80309",
                                   description="Splenic Diffuse Red Pulp Small B-Cell Lymphoma",
                                   meaning=NCIT.C80309)
    C9004 = PermissibleValue(text="C9004",
                                 description="Benign Adrenal Cortex Neoplasm",
                                 meaning=NCIT.C9004)
    C6909 = PermissibleValue(text="C6909",
                                 description="Rhabdoid Meningioma",
                                 meaning=NCIT.C6909)
    C6911 = PermissibleValue(text="C6911",
                                 description="Intraneural Perineurioma",
                                 meaning=NCIT.C6911)
    C6916 = PermissibleValue(text="C6916",
                                 description="Anaplastic Lymphoma",
                                 meaning=NCIT.C6916)
    C6967 = PermissibleValue(text="C6967",
                                 description="Pineal Parenchymal Tumor of Intermediate Differentiation",
                                 meaning=NCIT.C6967)
    C6912 = PermissibleValue(text="C6912",
                                 description="Soft Tissue Perineurioma",
                                 meaning=NCIT.C6912)
    C6908 = PermissibleValue(text="C6908",
                                 description="Chordoid Meningioma",
                                 meaning=NCIT.C6908)
    C6903 = PermissibleValue(text="C6903",
                                 description="Tanycytic Ependymoma",
                                 meaning=NCIT.C6903)
    C6877 = PermissibleValue(text="C6877",
                                 description="Grade III Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C6877)
    C4470 = PermissibleValue(text="C4470",
                                 description="Perifollicular Fibroma",
                                 meaning=NCIT.C4470)
    C43352 = PermissibleValue(text="C43352",
                                   description="Turban Tumor",
                                   meaning=NCIT.C43352)
    C65191 = PermissibleValue(text="C65191",
                                   description="Malignant Enteroglucagonoma",
                                   meaning=NCIT.C65191)
    C65184 = PermissibleValue(text="C65184",
                                   description="Islet Cell Adenoma",
                                   meaning=NCIT.C65184)
    C3819 = PermissibleValue(text="C3819",
                                 description="Primary Amyloidosis",
                                 meaning=NCIT.C3819)
    C92555 = PermissibleValue(text="C92555",
                                   description="Extraventricular Neurocytoma",
                                   meaning=NCIT.C92555)
    C9359 = PermissibleValue(text="C9359",
                                 description="Skin Pigmented Basal Cell Carcinoma",
                                 meaning=NCIT.C9359)
    C35558 = PermissibleValue(text="C35558",
                                   description="Tall Cell Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C35558)
    C3713 = PermissibleValue(text="C3713",
                                 description="Papillomatosis",
                                 meaning=NCIT.C3713)
    C27510 = PermissibleValue(text="C27510",
                                   description="Kaposiform Hemangioendothelioma",
                                   meaning=NCIT.C27510)
    C27541 = PermissibleValue(text="C27541",
                                   description="Skin Micronodular Basal Cell Carcinoma",
                                   meaning=NCIT.C27541)
    C3074 = PermissibleValue(text="C3074",
                                 description="Hairy Nevus",
                                 meaning=NCIT.C3074)
    C3218 = PermissibleValue(text="C3218",
                                 description="Diffuse Cutaneous Mastocytosis",
                                 meaning=NCIT.C3218)
    C126449 = PermissibleValue(text="C126449",
                                     description="Serous Tubal Intraepithelial Carcinoma",
                                     meaning=NCIT.C126449)
    C129530 = PermissibleValue(text="C129530",
                                     description="Central Nervous System Solitary Fibrous Tumor/Hemangiopericytoma, Grade 1",
                                     meaning=NCIT.C129530)
    C7072 = PermissibleValue(text="C7072",
                                 description="Oncocytic Neoplasm",
                                 meaning=NCIT.C7072)
    C46068 = PermissibleValue(text="C46068",
                                   description="Thyroid Gland Hurthle (Oncocytic) Cell Neoplasm",
                                   meaning=NCIT.C46068)
    C7690 = PermissibleValue(text="C7690",
                                 description="Breast Ductal Carcinoma In Situ and Lobular Carcinoma",
                                 meaning=NCIT.C7690)
    C7660 = PermissibleValue(text="C7660",
                                 description="Grade II Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C7660)
    C81767 = PermissibleValue(text="C81767",
                                   description="Indeterminate Dendritic Cell Tumor",
                                   meaning=NCIT.C81767)
    C80289 = PermissibleValue(text="C80289",
                                   description="Diffuse Large B-Cell Lymphoma Associated with Chronic Inflammation",
                                   meaning=NCIT.C80289)
    C9013 = PermissibleValue(text="C9013",
                                 description="Adult Teratoma",
                                 meaning=NCIT.C9013)
    C7442 = PermissibleValue(text="C7442",
                                 description="Benign Myoepithelioma",
                                 meaning=NCIT.C7442)
    C7162 = PermissibleValue(text="C7162",
                                 description="Primary Cutaneous Lymphoma",
                                 meaning=NCIT.C7162)
    C43333 = PermissibleValue(text="C43333",
                                   description="Spindle-Cell Predominant Trichodiscoma",
                                   meaning=NCIT.C43333)
    C4258 = PermissibleValue(text="C4258",
                                 description="Pleomorphic Rhabdomyosarcoma",
                                 meaning=NCIT.C4258)
    C40090 = PermissibleValue(text="C40090",
                                   description="Ovarian Seromucinous Carcinoma",
                                   meaning=NCIT.C40090)
    C6489 = PermissibleValue(text="C6489",
                                 description="Extraabdominal Fibromatosis",
                                 meaning=NCIT.C6489)
    C54345 = PermissibleValue(text="C54345",
                                   description="Sinonasal Oncocytic Papilloma",
                                   meaning=NCIT.C54345)
    C4982 = PermissibleValue(text="C4982",
                                 description="Aleukemic Leukemia",
                                 meaning=NCIT.C4982)
    C27807 = PermissibleValue(text="C27807",
                                   description="Nodular Sclerosis Classic Hodgkin Lymphoma, Syncytial Variant",
                                   meaning=NCIT.C27807)
    C27683 = PermissibleValue(text="C27683",
                                   description="Human Papillomavirus-Related Squamous Cell Carcinoma",
                                   meaning=NCIT.C27683)
    C2858 = PermissibleValue(text="C2858",
                                 description="Adrenal Cortex Neoplasm",
                                 meaning=NCIT.C2858)
    C126998 = PermissibleValue(text="C126998",
                                     description="Uterine Corpus High Grade Endometrial Stromal Sarcoma",
                                     meaning=NCIT.C126998)
    C89476 = PermissibleValue(text="C89476",
                                   description="Stage 0 Vaginal Cancer AJCC v7",
                                   meaning=NCIT.C89476)
    C67457 = PermissibleValue(text="C67457",
                                   description="Pancreatic Beta Cell Adenoma",
                                   meaning=NCIT.C67457)
    C7351 = PermissibleValue(text="C7351",
                                 description="Grade II Squamous Intraepithelial Neoplasia",
                                 meaning=NCIT.C7351)
    C6936 = PermissibleValue(text="C6936",
                                 description="Deep "Aggressive" Angiomyxoma",
                                 meaning=NCIT.C6936)
    C6969 = PermissibleValue(text="C6969",
                                 description="Plexiform Schwannoma",
                                 meaning=NCIT.C6969)
    C7138 = PermissibleValue(text="C7138",
                                 description="Solitary Mastocytoma of the Skin",
                                 meaning=NCIT.C7138)
    C6883 = PermissibleValue(text="C6883",
                                 description="Pancreatic Mucinous-Cystic Neoplasm with Intermediate Grade Dysplasia",
                                 meaning=NCIT.C6883)
    C6507 = PermissibleValue(text="C6507",
                                 description="Sclerosing Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                 meaning=NCIT.C6507)
    C6508 = PermissibleValue(text="C6508",
                                 description="Inflammatory Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                 meaning=NCIT.C6508)
    C53953 = PermissibleValue(text="C53953",
                                   description="Osteoblastic Osteosarcoma",
                                   meaning=NCIT.C53953)
    C4724 = PermissibleValue(text="C4724",
                                 description="Cellular Schwannoma",
                                 meaning=NCIT.C4724)
    C9497 = PermissibleValue(text="C9497",
                                 description="Medulloblastoma with Melanotic Differentiation",
                                 meaning=NCIT.C9497)
    C3721 = PermissibleValue(text="C3721",
                                 description="Lymphomatoid Papulosis",
                                 meaning=NCIT.C3721)
    C27427 = PermissibleValue(text="C27427",
                                   description="Low Grade Esophageal Squamous Intraepithelial Neoplasia",
                                   meaning=NCIT.C27427)
    C27425 = PermissibleValue(text="C27425",
                                   description="Esophageal High Grade Intraepithelial Neoplasia",
                                   meaning=NCIT.C27425)
    C27428 = PermissibleValue(text="C27428",
                                   description="Low Grade Esophageal Glandular Intraepithelial Neoplasia",
                                   meaning=NCIT.C27428)
    C3007 = PermissibleValue(text="C3007",
                                 description="Enchondroma",
                                 meaning=NCIT.C3007)
    C7695 = PermissibleValue(text="C7695",
                                 description="Primary Peritoneal Serous Papillary Adenocarcinoma",
                                 meaning=NCIT.C7695)
    C6747 = PermissibleValue(text="C6747",
                                 description="Desmoplastic Mesothelioma",
                                 meaning=NCIT.C6747)
    C8997 = PermissibleValue(text="C8997",
                                 description="Blastoma",
                                 meaning=NCIT.C8997)
    C7492 = PermissibleValue(text="C7492",
                                 description="Ameloblastic Carcinoma",
                                 meaning=NCIT.C7492)
    C7097 = PermissibleValue(text="C7097",
                                 description="Mixed Epithelial and Mesenchymal Hepatoblastoma",
                                 meaning=NCIT.C7097)
    C6917 = PermissibleValue(text="C6917",
                                 description="Atypical Burkitt/Burkitt-Like Lymphoma",
                                 meaning=NCIT.C6917)
    C7136 = PermissibleValue(text="C7136",
                                 description="Extracutaneous Mastocytoma",
                                 meaning=NCIT.C7136)
    C4346 = PermissibleValue(text="C4346",
                                 description="Skin Basal Cell Carcinoma with Sebaceous Differentiation",
                                 meaning=NCIT.C4346)
    C5407 = PermissibleValue(text="C5407",
                                 description="Medulloblastoma with Extensive Nodularity",
                                 meaning=NCIT.C5407)
    C27813 = PermissibleValue(text="C27813",
                                   description="Bile Duct Adenocarcinoma",
                                   meaning=NCIT.C27813)
    C27429 = PermissibleValue(text="C27429",
                                   description="High Grade Esophageal Glandular Intraepithelial Neoplasia",
                                   meaning=NCIT.C27429)
    C142823 = PermissibleValue(text="C142823",
                                     description="Congenital Peribronchial Myofibroblastic Tumor",
                                     meaning=NCIT.C142823)
    C123160 = PermissibleValue(text="C123160",
                                     description="Lepidic Predominant Adenocarcinoma",
                                     meaning=NCIT.C123160)
    C137839 = PermissibleValue(text="C137839",
                                     description="Breast Pleomorphic Lobular Carcinoma In Situ",
                                     meaning=NCIT.C137839)
    C5138 = PermissibleValue(text="C5138",
                                 description="Breast Ductal Carcinoma In Situ, Cribriform Pattern",
                                 meaning=NCIT.C5138)
    C7689 = PermissibleValue(text="C7689",
                                 description="Invasive Breast Ductal Carcinoma and Lobular Carcinoma In Situ",
                                 meaning=NCIT.C7689)
    C7727 = PermissibleValue(text="C7727",
                                 description="Light Chain Deposition Disease",
                                 meaning=NCIT.C7727)
    C4474 = PermissibleValue(text="C4474",
                                 description="Benign Mixed Tumor of the Skin",
                                 meaning=NCIT.C4474)
    C40152 = PermissibleValue(text="C40152",
                                   description="Serous Endometrial Intraepithelial Carcinoma",
                                   meaning=NCIT.C40152)
    C39842 = PermissibleValue(text="C39842",
                                   description="Bladder Urachal Carcinoma",
                                   meaning=NCIT.C39842)
    C4810 = PermissibleValue(text="C4810",
                                 description="Malignant Sweat Gland Neoplasm",
                                 meaning=NCIT.C4810)
    C4738 = PermissibleValue(text="C4738",
                                 description="Desmoplastic Infantile Ganglioglioma",
                                 meaning=NCIT.C4738)
    C4751 = PermissibleValue(text="C4751",
                                 description="Pigmented Spindle Cell Nevus",
                                 meaning=NCIT.C4751)
    C96807 = PermissibleValue(text="C96807",
                                   description="Bile Duct Intraductal Papillary Neoplasm, Low Grade",
                                   meaning=NCIT.C96807)
    C96809 = PermissibleValue(text="C96809",
                                   description="Bile Duct Intraductal Papillary Neoplasm, High Grade",
                                   meaning=NCIT.C96809)
    C27038 = PermissibleValue(text="C27038",
                                   description="Hypereosinophilic Syndrome",
                                   meaning=NCIT.C27038)
    C3070 = PermissibleValue(text="C3070",
                                 description="Granulosa Cell Tumor",
                                 meaning=NCIT.C3070)
    C3153 = PermissibleValue(text="C3153",
                                 description="Krukenberg Tumor",
                                 meaning=NCIT.C3153)
    C176980 = PermissibleValue(text="C176980",
                                     description="Superficial Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                     meaning=NCIT.C176980)
    C82403 = PermissibleValue(text="C82403",
                                   description="Acute Myeloid Leukemia with t(9;11)(p21.3;q23.3); MLLT3-MLL",
                                   meaning=NCIT.C82403)
    C82616 = PermissibleValue(text="C82616",
                                   description="Myelodysplastic/Myeloproliferative Neoplasm with Ring Sideroblasts and Thrombocytosis",
                                   meaning=NCIT.C82616)
    C82596 = PermissibleValue(text="C82596",
                                   description="Refractory Cytopenia of Childhood",
                                   meaning=NCIT.C82596)
    C7812 = PermissibleValue(text="C7812",
                                 description="Solitary Plasmacytoma of Bone",
                                 meaning=NCIT.C7812)
    C8648 = PermissibleValue(text="C8648",
                                 description="Myelodysplastic Syndrome, Unclassifiable",
                                 meaning=NCIT.C8648)
    C7168 = PermissibleValue(text="C7168",
                                 description="Myelodysplastic Syndrome with Excess Blasts-2",
                                 meaning=NCIT.C7168)
    C49025 = PermissibleValue(text="C49025",
                                   description="Myxoinflammatory Fibroblastic Sarcoma",
                                   meaning=NCIT.C49025)
    C4871 = PermissibleValue(text="C4871",
                                 description="Complete Hydatidiform Mole",
                                 meaning=NCIT.C4871)
    C4879 = PermissibleValue(text="C4879",
                                 description="Benign Sweat Gland Neoplasm",
                                 meaning=NCIT.C4879)
    C9285 = PermissibleValue(text="C9285",
                                 description="Aggressive Systemic Mastocytosis",
                                 meaning=NCIT.C9285)
    C3433 = PermissibleValue(text="C3433",
                                 description="Urticaria Pigmentosa/Maculopapular Cutaneous Mastocytosis",
                                 meaning=NCIT.C3433)
    C27182 = PermissibleValue(text="C27182",
                                   description="Skin Sclerosing/Morphoeic Basal Cell Carcinoma",
                                   meaning=NCIT.C27182)
    C4868 = PermissibleValue(text="C4868",
                                 description="Placental Hemangioma",
                                 meaning=NCIT.C4868)
    C7930 = PermissibleValue(text="C7930",
                                 description="Lymphomatoid Granulomatosis",
                                 meaning=NCIT.C7930)
    C6959 = PermissibleValue(text="C6959",
                                 description="Anaplastic Oligoastrocytoma",
                                 meaning=NCIT.C6959)
    C6968 = PermissibleValue(text="C6968",
                                 description="Supratentorial Embryonal Tumor, Not Otherwise Specified",
                                 meaning=NCIT.C6968)
    C7137 = PermissibleValue(text="C7137",
                                 description="Cutaneous Mastocytosis",
                                 meaning=NCIT.C7137)
    C7192 = PermissibleValue(text="C7192",
                                 description="Grade 3b Follicular Lymphoma",
                                 meaning=NCIT.C7192)
    C4327 = PermissibleValue(text="C4327",
                                 description="Central Nervous System Medulloepithelioma",
                                 meaning=NCIT.C4327)
    C4615 = PermissibleValue(text="C4615",
                                 description="Benign Skin Appendage Neoplasm",
                                 meaning=NCIT.C4615)
    C4748 = PermissibleValue(text="C4748",
                                 description="Malignant Melanotic Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C4748)
    C96877 = PermissibleValue(text="C96877",
                                   description="Gallbladder Intracholecystic Papillary Neoplasm, Low Grade",
                                   meaning=NCIT.C96877)
    C35815 = PermissibleValue(text="C35815",
                                   description="Granulocytic Sarcoma",
                                   meaning=NCIT.C35815)
    C8312 = PermissibleValue(text="C8312",
                                 description="Leptomeningeal Sarcoma",
                                 meaning=NCIT.C8312)
    C67493 = PermissibleValue(text="C67493",
                                   description="High-Grade Biliary Intraepithelial Neoplasia",
                                   meaning=NCIT.C67493)
    C4030 = PermissibleValue(text="C4030",
                                 description="Urothelial Carcinoma",
                                 meaning=NCIT.C4030)
    C4862 = PermissibleValue(text="C4862",
                                 description="Ovarian Sex Cord-Stromal Tumor",
                                 meaning=NCIT.C4862)
    C5160 = PermissibleValue(text="C5160",
                                 description="Breast Mixed Ductal and Lobular Carcinoma",
                                 meaning=NCIT.C5160)
    C27261 = PermissibleValue(text="C27261",
                                   description="Pre T-ALL",
                                   meaning=NCIT.C27261)
    C8694 = PermissibleValue(text="C8694",
                                 description="T Lymphoblastic Leukemia/Lymphoma",
                                 meaning=NCIT.C8694)
    C7152 = PermissibleValue(text="C7152",
                                 description="Erythroleukemia",
                                 meaning=NCIT.C7152)
    C3276 = PermissibleValue(text="C3276",
                                 description="Vestibular Schwannoma",
                                 meaning=NCIT.C3276)
    C8590 = PermissibleValue(text="C8590",
                                 description="Lymphocyte Predominant Type Hodgkin's Disease",
                                 meaning=NCIT.C8590)
    C167335 = PermissibleValue(text="C167335",
                                     description="Glioblastoma, IDH-Mutant",
                                     meaning=NCIT.C167335)
    C35727 = PermissibleValue(text="C35727",
                                   description="Grade I Neuroendocrine Carcinoma",
                                   meaning=NCIT.C35727)
    C3176 = PermissibleValue(text="C3176",
                                 description="Philadelphia-Negative Myelogenous Leukemia",
                                 meaning=NCIT.C3176)
    C150703 = PermissibleValue(text="C150703",
                                     description="Langerhans Cell Histiocytosis, Disseminated",
                                     meaning=NCIT.C150703)
    C129442 = PermissibleValue(text="C129442",
                                     description="Medulloblastoma, SHH-Activated, TP53-Mutant",
                                     meaning=NCIT.C129442)
    C129351 = PermissibleValue(text="C129351",
                                     description="Ependymoma, RELA Fusion-Positive",
                                     meaning=NCIT.C129351)
    C9235 = PermissibleValue(text="C9235",
                                 description="Systemic Mastocytosis",
                                 meaning=NCIT.C9235)
    C4630 = PermissibleValue(text="C4630",
                                 description="Low Grade Cervical Intraepithelial Neoplasia",
                                 meaning=NCIT.C4630)
    C37869 = PermissibleValue(text="C37869",
                                   description="B-Cell Lymphoma, Unclassifiable, with Features Intermediate between Diffuse Large B-Cell Lymphoma and Classic Hodgkin Lymphoma",
                                   meaning=NCIT.C37869)
    C66746 = PermissibleValue(text="C66746",
                                   description="Benign Thymoma",
                                   meaning=NCIT.C66746)
    C7380 = PermissibleValue(text="C7380",
                                 description="Thyroid Gland Papillary and Follicular Carcinoma",
                                 meaning=NCIT.C7380)
    C7438 = PermissibleValue(text="C7438",
                                 description="Infiltrating Papillary Adenocarcinoma",
                                 meaning=NCIT.C7438)
    C4338 = PermissibleValue(text="C4338",
                                 description="Diffuse Centroblastic-Centrocytic Lymphoma",
                                 meaning=NCIT.C4338)
    C4180 = PermissibleValue(text="C4180",
                                 description="Papillary Serous Cystadenoma",
                                 meaning=NCIT.C4180)
    C53677 = PermissibleValue(text="C53677",
                                   description="Intimal Sarcoma",
                                   meaning=NCIT.C53677)
    C95914 = PermissibleValue(text="C95914",
                                   description="Ampullary Noninvasive Pancreatobiliary Papillary Neoplasm with Low Grade Dysplasia",
                                   meaning=NCIT.C95914)
    C164250 = PermissibleValue(text="C164250",
                                     description="Human Papillomavirus-Negative Squamous Cell Carcinoma",
                                     meaning=NCIT.C164250)
    C162848 = PermissibleValue(text="C162848",
                                     description="Digital Papillary Adenoma",
                                     meaning=NCIT.C162848)
    C27824 = PermissibleValue(text="C27824",
                                   description="Reticulosarcoma",
                                   meaning=NCIT.C27824)
    C27820 = PermissibleValue(text="C27820",
                                   description="Mature T-ALL",
                                   meaning=NCIT.C27820)
    C82433 = PermissibleValue(text="C82433",
                                   description="Acute Myeloid Leukemia with Mutated CEBPA",
                                   meaning=NCIT.C82433)
    C80281 = PermissibleValue(text="C80281",
                                   description="EBV-Positive Diffuse Large B-Cell Lymphoma, Not Otherwise Specified",
                                   meaning=NCIT.C80281)
    C9022 = PermissibleValue(text="C9022",
                                 description="Childhood Astrocytic Tumor",
                                 meaning=NCIT.C9022)
    C3494 = PermissibleValue(text="C3494",
                                 description="Lung Papillary Adenoma",
                                 meaning=NCIT.C3494)
    C66764 = PermissibleValue(text="C66764",
                                   description="Fascial Fibroma",
                                   meaning=NCIT.C66764)
    C66953 = PermissibleValue(text="C66953",
                                   description="Mucinous Adenocarcinoma, Endocervical Type",
                                   meaning=NCIT.C66953)
    C41245 = PermissibleValue(text="C41245",
                                   description="Pancreatic Non-Invasive Mucinous Cystadenocarcinoma",
                                   meaning=NCIT.C41245)
    C4179 = PermissibleValue(text="C4179",
                                 description="Papillary Cystic Neoplasm",
                                 meaning=NCIT.C4179)
    C40081 = PermissibleValue(text="C40081",
                                   description="Borderline Ovarian Clear Cell Adenofibroma",
                                   meaning=NCIT.C40081)
    C6492 = PermissibleValue(text="C6492",
                                 description="Deep Fibrous Histiocytoma",
                                 meaning=NCIT.C6492)
    C65196 = PermissibleValue(text="C65196",
                                   description="Carcinoid Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C65196)
    C65189 = PermissibleValue(text="C65189",
                                   description="Malignant Vipoma",
                                   meaning=NCIT.C65189)
    C94759 = PermissibleValue(text="C94759",
                                   description="Functioning Endocrine Neoplasm",
                                   meaning=NCIT.C94759)
    C27798 = PermissibleValue(text="C27798",
                                   description="Pre-B Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27798)
    C80291 = PermissibleValue(text="C80291",
                                   description="High Grade B-Cell Lymphoma, Not Otherwise Specified",
                                   meaning=NCIT.C80291)
    C3466 = PermissibleValue(text="C3466",
                                 description="T-Cell Non-Hodgkin Lymphoma",
                                 meaning=NCIT.C3466)
    C7568 = PermissibleValue(text="C7568",
                                 description="Nodular Hidradenoma",
                                 meaning=NCIT.C7568)
    C82594 = PermissibleValue(text="C82594",
                                   description="Refractory Thrombocytopenia",
                                   meaning=NCIT.C82594)
    C82593 = PermissibleValue(text="C82593",
                                   description="Refractory Neutropenia",
                                   meaning=NCIT.C82593)
    C66754 = PermissibleValue(text="C66754",
                                   description="Small Congenital Melanocytic Nevus",
                                   meaning=NCIT.C66754)
    C84276 = PermissibleValue(text="C84276",
                                   description="Myeloid/Lymphoid Neoplasms with PDGFRB Rearrangement",
                                   meaning=NCIT.C84276)
    C7315 = PermissibleValue(text="C7315",
                                 description="Borderline Ovarian Serous Surface Papillary Tumor",
                                 meaning=NCIT.C7315)
    C6958 = PermissibleValue(text="C6958",
                                 description="Astrocytic Tumor",
                                 meaning=NCIT.C6958)
    C6932 = PermissibleValue(text="C6932",
                                 description="Solitary Plasmacytoma",
                                 meaning=NCIT.C6932)
    C4311 = PermissibleValue(text="C4311",
                                 description="Ghost Cell Odontogenic Carcinoma",
                                 meaning=NCIT.C4311)
    C4343 = PermissibleValue(text="C4343",
                                 description="Aleukemic Lymphoid Leukemia",
                                 meaning=NCIT.C4343)
    C39812 = PermissibleValue(text="C39812",
                                   description="Metanephric Adenofibroma",
                                   meaning=NCIT.C39812)
    C26919 = PermissibleValue(text="C26919",
                                   description="Lymphosarcoma",
                                   meaning=NCIT.C26919)
    C27825 = PermissibleValue(text="C27825",
                                   description="Mucin-Producing Carcinoma",
                                   meaning=NCIT.C27825)
    C121792 = PermissibleValue(text="C121792",
                                     description="Malignant PEComa",
                                     meaning=NCIT.C121792)
    C129309 = PermissibleValue(text="C129309",
                                     description="Diffuse Midline Glioma, H3 K27M-Mutant",
                                     meaning=NCIT.C129309)
    C66756 = PermissibleValue(text="C66756",
                                   description="Mixed Epithelioid and Spindle Cell Melanoma",
                                   meaning=NCIT.C66756)
    C9150 = PermissibleValue(text="C9150",
                                 description="Botryoid-Type Embryonal Rhabdomyosarcoma",
                                 meaning=NCIT.C9150)
    C7183 = PermissibleValue(text="C7183",
                                 description="Polymorphic Post-Transplant Lymphoproliferative Disorder",
                                 meaning=NCIT.C7183)
    C7171 = PermissibleValue(text="C7171",
                                 description="Acute Monoblastic Leukemia",
                                 meaning=NCIT.C7171)
    C4182 = PermissibleValue(text="C4182",
                                 description="Serous Surface Papillary Carcinoma",
                                 meaning=NCIT.C4182)
    C45366 = PermissibleValue(text="C45366",
                                   description="Primary Cutaneous CD4-Positive Small/Medium T-Cell Lymphoproliferative Disorder",
                                   meaning=NCIT.C45366)
    C4073 = PermissibleValue(text="C4073",
                                 description="Meningeal Sarcoma",
                                 meaning=NCIT.C4073)
    C5143 = PermissibleValue(text="C5143",
                                 description="Malignant Breast Adenomyoepithelioma",
                                 meaning=NCIT.C5143)
    C95493 = PermissibleValue(text="C95493",
                                   description="Pancreatic Mucinous-Cystic Neoplasm, High Grade",
                                   meaning=NCIT.C95493)
    C164205 = PermissibleValue(text="C164205",
                                     description="Biphenotypic Sinonasal Sarcoma",
                                     meaning=NCIT.C164205)
    C36255 = PermissibleValue(text="C36255",
                                   description="Secondary Neoplasm",
                                   meaning=NCIT.C36255)
    C36084 = PermissibleValue(text="C36084",
                                   description="Invasive Breast Micropapillary Carcinoma",
                                   meaning=NCIT.C36084)
    C27281 = PermissibleValue(text="C27281",
                                   description="L2 Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27281)
    C27483 = PermissibleValue(text="C27483",
                                   description="Lipoblastoma",
                                   meaning=NCIT.C27483)
    C3083 = PermissibleValue(text="C3083",
                                 description="Gamma Heavy Chain Disease",
                                 meaning=NCIT.C3083)
    C6882 = PermissibleValue(text="C6882",
                                 description="Micropapillary Serous Carcinoma",
                                 meaning=NCIT.C6882)
    C4300 = PermissibleValue(text="C4300",
                                 description="Benign Hemangiopericytoma",
                                 meaning=NCIT.C4300)
    C6556 = PermissibleValue(text="C6556",
                                 description="Degenerated Schwannoma",
                                 meaning=NCIT.C6556)
    C3709 = PermissibleValue(text="C3709",
                                 description="Epithelial Neoplasm",
                                 meaning=NCIT.C3709)
    C27940 = PermissibleValue(text="C27940",
                                   description="Gastrointestinal Autonomic Nerve Tumor",
                                   meaning=NCIT.C27940)
    C8252 = PermissibleValue(text="C8252",
                                 description="Therapy-Related Acute Myeloid Leukemia",
                                 meaning=NCIT.C8252)
    C9298 = PermissibleValue(text="C9298",
                                 description="Acute Undifferentiated Leukemia",
                                 meaning=NCIT.C9298)
    C6871 = PermissibleValue(text="C6871",
                                 description="Sinonasal Inverted Papilloma",
                                 meaning=NCIT.C6871)
    C4037 = PermissibleValue(text="C4037",
                                 description="Acute Myeloid Leukemia Arising from Previous Myelodysplastic Syndrome",
                                 meaning=NCIT.C4037)
    C5264 = PermissibleValue(text="C5264",
                                 description="Bronchial Mucosa-Associated Lymphoid Tissue Lymphoma",
                                 meaning=NCIT.C5264)
    C27754 = PermissibleValue(text="C27754",
                                   description="Alkylating Agent-Related Acute Myeloid Leukemia",
                                   meaning=NCIT.C27754)
    C3087 = PermissibleValue(text="C3087",
                                 description="Hemangiopericytoma",
                                 meaning=NCIT.C3087)
    C157575 = PermissibleValue(text="C157575",
                                     description="Anal Intraepithelial Neoplasia 3",
                                     meaning=NCIT.C157575)
    C39591 = PermissibleValue(text="C39591",
                                   description="Chronic Lymphoproliferative Disorder of NK-Cells",
                                   meaning=NCIT.C39591)
    C7612 = PermissibleValue(text="C7612",
                                 description="Malignant Thymoma",
                                 meaning=NCIT.C7612)
    C7570 = PermissibleValue(text="C7570",
                                 description="Melanocytic Nevus",
                                 meaning=NCIT.C7570)
    C4301 = PermissibleValue(text="C4301",
                                 description="Malignant Hemangiopericytoma",
                                 meaning=NCIT.C4301)
    C45843 = PermissibleValue(text="C45843",
                                   description="Pancreatic Mixed Adenoneuroendocrine Carcinoma",
                                   meaning=NCIT.C45843)
    C9289 = PermissibleValue(text="C9289",
                                 description="Acute Myeloid Leukemia with Multilineage Dysplasia",
                                 meaning=NCIT.C9289)
    C45837 = PermissibleValue(text="C45837",
                                   description="Non-Functioning Pancreatic Neuroendocrine Tumor",
                                   meaning=NCIT.C45837)
    C9020 = PermissibleValue(text="C9020",
                                 description="Acute Myelomonocytic Leukemia with Abnormal Eosinophils",
                                 meaning=NCIT.C9020)
    C7205 = PermissibleValue(text="C7205",
                                 description="Lymphoepithelioid Variant Peripheral T-Cell Lymphoma",
                                 meaning=NCIT.C7205)
    C6923 = PermissibleValue(text="C6923",
                                 description="Acute Bilineal Leukemia",
                                 meaning=NCIT.C6923)
    C48314 = PermissibleValue(text="C48314",
                                   description="Benign Paraganglioma",
                                   meaning=NCIT.C48314)
    C9284 = PermissibleValue(text="C9284",
                                 description="Systemic Mastocytosis with an Associated Hematological Neoplasm",
                                 meaning=NCIT.C9284)
    C164145 = PermissibleValue(text="C164145",
                                     description="Hodgkin's Sarcoma",
                                     meaning=NCIT.C164145)
    C6920 = PermissibleValue(text="C6920",
                                 description="Hand-Schuller-Christian Disease",
                                 meaning=NCIT.C6920)
    C4193 = PermissibleValue(text="C4193",
                                 description="Thyroid Gland Medullary Carcinoma with Amyloid Stroma",
                                 meaning=NCIT.C4193)
    C2977 = PermissibleValue(text="C2977",
                                 description="Phyllodes Tumor",
                                 meaning=NCIT.C2977)
    C162973 = PermissibleValue(text="C162973",
                                     description="Non-Invasive Cribriform Carcinoma",
                                     meaning=NCIT.C162973)
    C8868 = PermissibleValue(text="C8868",
                                 description="B Lymphoblastic Lymphoma",
                                 meaning=NCIT.C8868)
    C9327 = PermissibleValue(text="C9327",
                                 description="Malignant Adrenal Cortex Neoplasm",
                                 meaning=NCIT.C9327)
    C9295 = PermissibleValue(text="C9295",
                                 description="Mast Cell Neoplasm",
                                 meaning=NCIT.C9295)
    C4233 = PermissibleValue(text="C4233",
                                 description="Precancerous Melanosis",
                                 meaning=NCIT.C4233)
    C3486 = PermissibleValue(text="C3486",
                                 description="Epithelioid Cell Type Gastrointestinal Stromal Tumor",
                                 meaning=NCIT.C3486)
    C36122 = PermissibleValue(text="C36122",
                                   description="Benign Cellular Infiltrate",
                                   meaning=NCIT.C36122)
    C7855 = PermissibleValue(text="C7855",
                                 description="Stage 0 Vaginal Cancer AJCC v6",
                                 meaning=NCIT.C7855)
    C8863 = PermissibleValue(text="C8863",
                                 description="Nodal Marginal Zone Lymphoma",
                                 meaning=NCIT.C8863)
    C7230 = PermissibleValue(text="C7230",
                                 description="Primary Cutaneous Marginal Zone Lymphoma of Mucosa-Associated Lymphoid Tissue",
                                 meaning=NCIT.C7230)
    C3160 = PermissibleValue(text="C3160",
                                 description="Letterer-Siwe Disease",
                                 meaning=NCIT.C3160)
    C7662 = PermissibleValue(text="C7662",
                                 description="High Grade Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C7662)
    C66815 = PermissibleValue(text="C66815",
                                   description="Diffuse Retinoblastoma",
                                   meaning=NCIT.C66815)
    C66779 = PermissibleValue(text="C66779",
                                   description="Benign Hemangioendothelioma",
                                   meaning=NCIT.C66779)
    C66772 = PermissibleValue(text="C66772",
                                   description="Benign Stromal Tumor",
                                   meaning=NCIT.C66772)
    C67090 = PermissibleValue(text="C67090",
                                   description="Serous Adenofibroma",
                                   meaning=NCIT.C67090)
    C66778 = PermissibleValue(text="C66778",
                                   description="Malignant Trophoblastic Teratoma",
                                   meaning=NCIT.C66778)
    C66803 = PermissibleValue(text="C66803",
                                   description="Cerebellar Sarcoma",
                                   meaning=NCIT.C66803)
    C8978 = PermissibleValue(text="C8978",
                                 description="Mucinous Adenofibroma",
                                 meaning=NCIT.C8978)
    C7363 = PermissibleValue(text="C7363",
                                 description="Intraductal Papillomatosis",
                                 meaning=NCIT.C7363)
    C7468 = PermissibleValue(text="C7468",
                                 description="Struma Ovarii",
                                 meaning=NCIT.C7468)
    C4309 = PermissibleValue(text="C4309",
                                 description="Complex Odontoma",
                                 meaning=NCIT.C4309)
    C4211 = PermissibleValue(text="C4211",
                                 description="Ovarian Sertoli Cell Tumor with Lipid Storage",
                                 meaning=NCIT.C4211)
    C39974 = PermissibleValue(text="C39974",
                                   description="Ovarian Sertoli-Leydig Cell Tumor with Retiform Elements",
                                   meaning=NCIT.C39974)
    C65182 = PermissibleValue(text="C65182",
                                   description="Micropapillary Transitional Cell Carcinoma",
                                   meaning=NCIT.C65182)
    C65198 = PermissibleValue(text="C65198",
                                   description="Glandular Papillomatosis",
                                   meaning=NCIT.C65198)
    C46095 = PermissibleValue(text="C46095",
                                   description="Solid/Trabecular Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C46095)
    C96485 = PermissibleValue(text="C96485",
                                   description="Colorectal Serrated Adenocarcinoma",
                                   meaning=NCIT.C96485)
    C92624 = PermissibleValue(text="C92624",
                                   description="Papillary Tumor of the Pineal Region",
                                   meaning=NCIT.C92624)
    C95913 = PermissibleValue(text="C95913",
                                   description="Ampullary Noninvasive Papillary Neoplasm, Pancreatobiliary Type",
                                   meaning=NCIT.C95913)
    C95963 = PermissibleValue(text="C95963",
                                   description="Ampulla of Vater Pancreatobiliary Type Adenocarcinoma",
                                   meaning=NCIT.C95963)
    C3686 = PermissibleValue(text="C3686",
                                 description="Salivary Gland Monomorphic Adenoma",
                                 meaning=NCIT.C3686)
    C3711 = PermissibleValue(text="C3711",
                                 description="Compound Odontoma",
                                 meaning=NCIT.C3711)
    C27797 = PermissibleValue(text="C27797",
                                   description="Common Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27797)
    C2874 = PermissibleValue(text="C2874",
                                 description="Angiokeratoma",
                                 meaning=NCIT.C2874)
    C3190 = PermissibleValue(text="C3190",
                                 description="Linitis Plastica",
                                 meaning=NCIT.C3190)
    C129444 = PermissibleValue(text="C129444",
                                     description="Medulloblastoma, Non-WNT/Non-SHH",
                                     meaning=NCIT.C129444)
    C96414 = PermissibleValue(text="C96414",
                                   description="Serrated Lesions and Polyps",
                                   meaning=NCIT.C96414)
    C27814 = PermissibleValue(text="C27814",
                                   description="Bile Duct Carcinoma",
                                   meaning=NCIT.C27814)
    C3016 = PermissibleValue(text="C3016",
                                 description="Eosinophilic Granuloma",
                                 meaning=NCIT.C3016)
    C8376 = PermissibleValue(text="C8376",
                                 description="Adenocarcinoma In Situ in Villous Adenoma",
                                 meaning=NCIT.C8376)
    C80338 = PermissibleValue(text="C80338",
                                   description="B Lymphoblastic Leukemia/Lymphoma with Hypodiploidy",
                                   meaning=NCIT.C80338)
    C66811 = PermissibleValue(text="C66811",
                                   description="Spongioneuroblastoma",
                                   meaning=NCIT.C66811)
    C67156 = PermissibleValue(text="C67156",
                                   description="Olfactory Neurocytoma",
                                   meaning=NCIT.C67156)
    C66796 = PermissibleValue(text="C66796",
                                   description="Aggressive Osteoblastoma",
                                   meaning=NCIT.C66796)
    C66951 = PermissibleValue(text="C66951",
                                   description="Adenocarcinoma, Endocervical Type",
                                   meaning=NCIT.C66951)
    C66717 = PermissibleValue(text="C66717",
                                   description="Metastatic Signet Ring Cell Carcinoma",
                                   meaning=NCIT.C66717)
    C66816 = PermissibleValue(text="C66816",
                                   description="Spontaneously Regressed Retinoblastoma",
                                   meaning=NCIT.C66816)
    C66718 = PermissibleValue(text="C66718",
                                   description="Medullary Carcinoma, Not Otherwise Specified",
                                   meaning=NCIT.C66718)
    C66763 = PermissibleValue(text="C66763",
                                   description="Periosteal Fibrosarcoma",
                                   meaning=NCIT.C66763)
    C66752 = PermissibleValue(text="C66752",
                                   description="Clear Cell Neoplasm",
                                   meaning=NCIT.C66752)
    C66771 = PermissibleValue(text="C66771",
                                   description="Angiomyosarcoma",
                                   meaning=NCIT.C66771)
    C66804 = PermissibleValue(text="C66804",
                                   description="Ganglioneuromatosis",
                                   meaning=NCIT.C66804)
    C66800 = PermissibleValue(text="C66800",
                                   description="Ameloblastic Fibrodentinoma",
                                   meaning=NCIT.C66800)
    C66813 = PermissibleValue(text="C66813",
                                   description="Differentiated Retinoblastoma",
                                   meaning=NCIT.C66813)
    C66817 = PermissibleValue(text="C66817",
                                   description="Hemangioblastic Meningioma",
                                   meaning=NCIT.C66817)
    C66799 = PermissibleValue(text="C66799",
                                   description="Metastasizing Chondroblastoma",
                                   meaning=NCIT.C66799)
    C66814 = PermissibleValue(text="C66814",
                                   description="Undifferentiated Retinoblastoma",
                                   meaning=NCIT.C66814)
    C66903 = PermissibleValue(text="C66903",
                                   description="Skin Metatypical Carcinoma",
                                   meaning=NCIT.C66903)
    C67092 = PermissibleValue(text="C67092",
                                   description="Ovarian Serous Adenocarcinofibroma",
                                   meaning=NCIT.C67092)
    C66757 = PermissibleValue(text="C66757",
                                   description="Epithelioid Cell Nevus",
                                   meaning=NCIT.C66757)
    C66765 = PermissibleValue(text="C66765",
                                   description="Fascial Fibrosarcoma",
                                   meaning=NCIT.C66765)
    C66761 = PermissibleValue(text="C66761",
                                   description="Periosteal Fibroma",
                                   meaning=NCIT.C66761)
    C66802 = PermissibleValue(text="C66802",
                                   description="Oligodendroblastoma",
                                   meaning=NCIT.C66802)
    C67155 = PermissibleValue(text="C67155",
                                   description="Olfactory Neurogenic Tumor",
                                   meaning=NCIT.C67155)
    C8987 = PermissibleValue(text="C8987",
                                 description="Clear Cell Adenofibroma",
                                 meaning=NCIT.C8987)
    C9009 = PermissibleValue(text="C9009",
                                 description="Squamous Papillomatosis",
                                 meaning=NCIT.C9009)
    C84275 = PermissibleValue(text="C84275",
                                   description="Myeloid/Lymphoid Neoplasms with PDGFRA Rearrangement",
                                   meaning=NCIT.C84275)
    C7501 = PermissibleValue(text="C7501",
                                 description="Odontogenic Myxoma",
                                 meaning=NCIT.C7501)
    C7559 = PermissibleValue(text="C7559",
                                 description="Atypical Adenoma",
                                 meaning=NCIT.C7559)
    C7450 = PermissibleValue(text="C7450",
                                 description="Intramuscular Lipoma",
                                 meaning=NCIT.C7450)
    C6902 = PermissibleValue(text="C6902",
                                 description="Chondroid Chordoma",
                                 meaning=NCIT.C6902)
    C6892 = PermissibleValue(text="C6892",
                                 description="Cellular Fibroma",
                                 meaning=NCIT.C6892)
    C4315 = PermissibleValue(text="C4315",
                                 description="Peripheral Odontogenic Fibroma",
                                 meaning=NCIT.C4315)
    C4319 = PermissibleValue(text="C4319",
                                 description="Papillary Ependymoma",
                                 meaning=NCIT.C4319)
    C4324 = PermissibleValue(text="C4324",
                                 description="Astroblastoma",
                                 meaning=NCIT.C4324)
    C4328 = PermissibleValue(text="C4328",
                                 description="Pacinian Neurofibroma",
                                 meaning=NCIT.C4328)
    C4332 = PermissibleValue(text="C4332",
                                 description="Angiomatous Meningioma",
                                 meaning=NCIT.C4332)
    C4320 = PermissibleValue(text="C4320",
                                 description="Protoplasmic Astrocytoma",
                                 meaning=NCIT.C4320)
    C4331 = PermissibleValue(text="C4331",
                                 description="Psammomatous Meningioma",
                                 meaning=NCIT.C4331)
    C4125 = PermissibleValue(text="C4125",
                                 description="Superficial Spreading Adenocarcinoma",
                                 meaning=NCIT.C4125)
    C4136 = PermissibleValue(text="C4136",
                                 description="Adenocarcinoma in Multiple Adenomatous Polyps",
                                 meaning=NCIT.C4136)
    C4101 = PermissibleValue(text="C4101",
                                 description="Verrucous Papilloma",
                                 meaning=NCIT.C4101)
    C4141 = PermissibleValue(text="C4141",
                                 description="Adenocarcinoma in Villous Adenoma",
                                 meaning=NCIT.C4141)
    C4168 = PermissibleValue(text="C4168",
                                 description="Apocrine Adenoma",
                                 meaning=NCIT.C4168)
    C4142 = PermissibleValue(text="C4142",
                                 description="Villous Adenocarcinoma",
                                 meaning=NCIT.C4142)
    C4158 = PermissibleValue(text="C4158",
                                 description="Mixed Cell Adenocarcinoma",
                                 meaning=NCIT.C4158)
    C4157 = PermissibleValue(text="C4157",
                                 description="Mixed Cell Adenoma",
                                 meaning=NCIT.C4157)
    C4112 = PermissibleValue(text="C4112",
                                 description="Trichofolliculoma",
                                 meaning=NCIT.C4112)
    C4145 = PermissibleValue(text="C4145",
                                 description="Adenocarcinoma in Tubulovillous Adenoma",
                                 meaning=NCIT.C4145)
    C4144 = PermissibleValue(text="C4144",
                                 description="Adenocarcinoma In Situ in Tubulovillous Adenoma",
                                 meaning=NCIT.C4144)
    C4104 = PermissibleValue(text="C4104",
                                 description="Metastatic Squamous Cell Carcinoma",
                                 meaning=NCIT.C4104)
    C4181 = PermissibleValue(text="C4181",
                                 description="Serous Surface Papilloma",
                                 meaning=NCIT.C4181)
    C4184 = PermissibleValue(text="C4184",
                                 description="Papillary Mucinous Cystadenoma",
                                 meaning=NCIT.C4184)
    C4134 = PermissibleValue(text="C4134",
                                 description="Adenocarcinoma in Adenomatous Polyposis Coli",
                                 meaning=NCIT.C4134)
    C4173 = PermissibleValue(text="C4173",
                                 description="Papillary Eccrine Adenoma",
                                 meaning=NCIT.C4173)
    C4210 = PermissibleValue(text="C4210",
                                 description="Poorly Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                 meaning=NCIT.C4210)
    C4209 = PermissibleValue(text="C4209",
                                 description="Well Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                 meaning=NCIT.C4209)
    C4223 = PermissibleValue(text="C4223",
                                 description="Glomangiomyoma",
                                 meaning=NCIT.C4223)
    C4291 = PermissibleValue(text="C4291",
                                 description="Malignant Struma Ovarii",
                                 meaning=NCIT.C4291)
    C4262 = PermissibleValue(text="C4262",
                                 description="Endometrial Stromal Nodule",
                                 meaning=NCIT.C4262)
    C4253 = PermissibleValue(text="C4253",
                                 description="Mixed Liposarcoma",
                                 meaning=NCIT.C4253)
    C4256 = PermissibleValue(text="C4256",
                                 description="Cellular Leiomyoma",
                                 meaning=NCIT.C4256)
    C4260 = PermissibleValue(text="C4260",
                                 description="Fetal Rhabdomyoma",
                                 meaning=NCIT.C4260)
    C4226 = PermissibleValue(text="C4226",
                                 description="Balloon Cell Nevus",
                                 meaning=NCIT.C4226)
    C4243 = PermissibleValue(text="C4243",
                                 description="Sarcomatosis",
                                 meaning=NCIT.C4243)
    C39954 = PermissibleValue(text="C39954",
                                   description="Brenner Tumor",
                                   meaning=NCIT.C39954)
    C39981 = PermissibleValue(text="C39981",
                                   description="Malignant Ovarian Steroid Cell Tumor",
                                   meaning=NCIT.C39981)
    C40315 = PermissibleValue(text="C40315",
                                   description="Pilomyxoid Astrocytoma",
                                   meaning=NCIT.C40315)
    C40077 = PermissibleValue(text="C40077",
                                   description="Malignant Ovarian Clear Cell Tumor",
                                   meaning=NCIT.C40077)
    C4094 = PermissibleValue(text="C4094",
                                 description="Pleomorphic Carcinoma",
                                 meaning=NCIT.C4094)
    C39944 = PermissibleValue(text="C39944",
                                   description="Testicular Large Cell Calcifying Sertoli Cell Tumor",
                                   meaning=NCIT.C39944)
    C39973 = PermissibleValue(text="C39973",
                                   description="Poorly Differentiated Ovarian Sertoli-Leydig Cell Tumor, Variant with Heterologous Elements",
                                   meaning=NCIT.C39973)
    C40028 = PermissibleValue(text="C40028",
                                   description="Borderline Ovarian Serous Adenofibroma",
                                   meaning=NCIT.C40028)
    C39740 = PermissibleValue(text="C39740",
                                   description="Lung Inflammatory Myofibroblastic Tumor",
                                   meaning=NCIT.C39740)
    C6475 = PermissibleValue(text="C6475",
                                 description="Clear Cell Chondrosarcoma",
                                 meaning=NCIT.C6475)
    C6503 = PermissibleValue(text="C6503",
                                 description="Chondroid Lipoma",
                                 meaning=NCIT.C6503)
    C6517 = PermissibleValue(text="C6517",
                                 description="Genital Rhabdomyoma",
                                 meaning=NCIT.C6517)
    C65161 = PermissibleValue(text="C65161",
                                   description="Polygonal Cell Carcinoma",
                                   meaning=NCIT.C65161)
    C65160 = PermissibleValue(text="C65160",
                                   description="Giant Cell and Spindle Cell Carcinoma",
                                   meaning=NCIT.C65160)
    C65204 = PermissibleValue(text="C65204",
                                   description="Papillary Mucinous Cystadenocarcinoma",
                                   meaning=NCIT.C65204)
    C65195 = PermissibleValue(text="C65195",
                                   description="Carcinoma Simplex",
                                   meaning=NCIT.C65195)
    C65179 = PermissibleValue(text="C65179",
                                   description="Squamous Cell Carcinoma with Horn Formation",
                                   meaning=NCIT.C65179)
    C65178 = PermissibleValue(text="C65178",
                                   description="Microinvasive Squamous Cell Carcinoma",
                                   meaning=NCIT.C65178)
    C6509 = PermissibleValue(text="C6509",
                                 description="Fibroblastic Liposarcoma",
                                 meaning=NCIT.C6509)
    C65165 = PermissibleValue(text="C65165",
                                   description="Inverted Squamous Cell Papilloma",
                                   meaning=NCIT.C65165)
    C65159 = PermissibleValue(text="C65159",
                                   description="Glassy Cell Carcinoma",
                                   meaning=NCIT.C65159)
    C65203 = PermissibleValue(text="C65203",
                                   description="Clear Cell Papillary Cystadenoma",
                                   meaning=NCIT.C65203)
    C65154 = PermissibleValue(text="C65154",
                                   description="Malignant Tumor, Small Cell Type",
                                   meaning=NCIT.C65154)
    C53316 = PermissibleValue(text="C53316",
                                   description="Cavernous Lymphangioma",
                                   meaning=NCIT.C53316)
    C53686 = PermissibleValue(text="C53686",
                                   description="Atypical Choroid Plexus Papilloma",
                                   meaning=NCIT.C53686)
    C5419 = PermissibleValue(text="C5419",
                                 description="Gliofibroma",
                                 meaning=NCIT.C5419)
    C49016 = PermissibleValue(text="C49016",
                                   description="Angiomyofibroblastoma",
                                   meaning=NCIT.C49016)
    C49012 = PermissibleValue(text="C49012",
                                   description="Myofibroblastoma",
                                   meaning=NCIT.C49012)
    C4973 = PermissibleValue(text="C4973",
                                 description="Perineurioma",
                                 meaning=NCIT.C4973)
    C3830 = PermissibleValue(text="C3830",
                                 description="Chondromyxoid Fibroma",
                                 meaning=NCIT.C3830)
    C4717 = PermissibleValue(text="C4717",
                                 description="Anaplastic Ganglioglioma",
                                 meaning=NCIT.C4717)
    C92554 = PermissibleValue(text="C92554",
                                   description="Papillary Glioneuronal Tumor",
                                   meaning=NCIT.C92554)
    C3700 = PermissibleValue(text="C3700",
                                 description="Epithelioid Leiomyosarcoma",
                                 meaning=NCIT.C3700)
    C3701 = PermissibleValue(text="C3701",
                                 description="Myxoid Leiomyosarcoma",
                                 meaning=NCIT.C3701)
    C3685 = PermissibleValue(text="C3685",
                                 description="Microcystic Adenoma",
                                 meaning=NCIT.C3685)
    C3688 = PermissibleValue(text="C3688",
                                 description="Trabecular Adenoma",
                                 meaning=NCIT.C3688)
    C35259 = PermissibleValue(text="C35259",
                                   description="Chondromatosis",
                                   meaning=NCIT.C35259)
    C35837 = PermissibleValue(text="C35837",
                                   description="Salivary Gland Sialoblastoma",
                                   meaning=NCIT.C35837)
    C3763 = PermissibleValue(text="C3763",
                                 description="Pulmonary Adenomatosis",
                                 meaning=NCIT.C3763)
    C3748 = PermissibleValue(text="C3748",
                                 description="Leiomyomatosis",
                                 meaning=NCIT.C3748)
    C3737 = PermissibleValue(text="C3737",
                                 description="Mesenchymal Chondrosarcoma",
                                 meaning=NCIT.C3737)
    C27816 = PermissibleValue(text="C27816",
                                   description="Pigmented Nevus",
                                   meaning=NCIT.C27816)
    C27265 = PermissibleValue(text="C27265",
                                   description="Malignant Lymphoma, Large Cell, Cleaved",
                                   meaning=NCIT.C27265)
    C27369 = PermissibleValue(text="C27369",
                                   description="Adult Pleomorphic Rhabdomyosarcoma",
                                   meaning=NCIT.C27369)
    C27031 = PermissibleValue(text="C27031",
                                   description="Pancreatic Neuroendocrine Neoplasm",
                                   meaning=NCIT.C27031)
    C27535 = PermissibleValue(text="C27535",
                                   description="Skin Adenoid Basal Cell Carcinoma",
                                   meaning=NCIT.C27535)
    C173735 = PermissibleValue(text="C173735",
                                     description="Odontogenic Carcinosarcoma",
                                     meaning=NCIT.C173735)
    C129440 = PermissibleValue(text="C129440",
                                     description="Medulloblastoma, WNT-Activated",
                                     meaning=NCIT.C129440)
    C7683 = PermissibleValue(text="C7683",
                                 description="Adenocarcinoma with Cartilaginous and Osseous Metaplasia",
                                 meaning=NCIT.C7683)
    C80341 = PermissibleValue(text="C80341",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(1;19)(q23;p13.3); E2A-PBX1 (TCF3-PBX1)",
                                   meaning=NCIT.C80341)
    C80335 = PermissibleValue(text="C80335",
                                   description="B Lymphoblastic Leukemia/Lymphoma with Hyperdiploidy",
                                   meaning=NCIT.C80335)
    C66841 = PermissibleValue(text="C66841",
                                   description="Melanotic Neurofibroma",
                                   meaning=NCIT.C66841)
    C66775 = PermissibleValue(text="C66775",
                                   description="Borderline Ovarian Mucinous Adenofibroma",
                                   meaning=NCIT.C66775)
    C66812 = PermissibleValue(text="C66812",
                                   description="Retinocytoma",
                                   meaning=NCIT.C66812)
    C66755 = PermissibleValue(text="C66755",
                                   description="Proliferative Nodules in Congenital Melanocytic Nevus",
                                   meaning=NCIT.C66755)
    C66809 = PermissibleValue(text="C66809",
                                   description="Ciliary Body Benign Teratoid Medulloepithelioma",
                                   meaning=NCIT.C66809)
    C66808 = PermissibleValue(text="C66808",
                                   description="Medulloepithelioma Not Otherwise Specified",
                                   meaning=NCIT.C66808)
    C66749 = PermissibleValue(text="C66749",
                                   description="Ovarian Stromal Tumor with Minor Sex Cord Elements",
                                   meaning=NCIT.C66749)
    C66792 = PermissibleValue(text="C66792",
                                   description="Hemolymphangioma",
                                   meaning=NCIT.C66792)
    C66810 = PermissibleValue(text="C66810",
                                   description="Ciliary Body Teratoid Medulloepithelioma",
                                   meaning=NCIT.C66810)
    C66774 = PermissibleValue(text="C66774",
                                   description="Ossifying Renal Tumor of Infancy",
                                   meaning=NCIT.C66774)
    C66750 = PermissibleValue(text="C66750",
                                   description="Adult Type Granulosa Cell Tumor",
                                   meaning=NCIT.C66750)
    C8970 = PermissibleValue(text="C8970",
                                 description="Periosteal Osteosarcoma",
                                 meaning=NCIT.C8970)
    C7195 = PermissibleValue(text="C7195",
                                 description="Primary Cutaneous CD30-Positive T-Cell Lymphoproliferative Disorder",
                                 meaning=NCIT.C7195)
    C6581 = PermissibleValue(text="C6581",
                                 description="Parachordoma",
                                 meaning=NCIT.C6581)
    C7503 = PermissibleValue(text="C7503",
                                 description="Borderline Phyllodes Tumor",
                                 meaning=NCIT.C7503)
    C7457 = PermissibleValue(text="C7457",
                                 description="Capillary Hemangioma",
                                 meaning=NCIT.C7457)
    C6934 = PermissibleValue(text="C6934",
                                 description="Gangliocytoma",
                                 meaning=NCIT.C6934)
    C7052 = PermissibleValue(text="C7052",
                                 description="Myofibroma",
                                 meaning=NCIT.C7052)
    C7112 = PermissibleValue(text="C7112",
                                 description="Squamous Odontogenic Tumor",
                                 meaning=NCIT.C7112)
    C6899 = PermissibleValue(text="C6899",
                                 description="Breast Adenomyoepithelioma",
                                 meaning=NCIT.C6899)
    C6904 = PermissibleValue(text="C6904",
                                 description="Large Cell Medulloblastoma",
                                 meaning=NCIT.C6904)
    C4308 = PermissibleValue(text="C4308",
                                 description="Cementoblastoma",
                                 meaning=NCIT.C4308)
    C4397 = PermissibleValue(text="C4397",
                                 description="Carcinoma ex Pleomorphic Adenoma",
                                 meaning=NCIT.C4397)
    C43565 = PermissibleValue(text="C43565",
                                   description="Appendix Tubular Carcinoid",
                                   meaning=NCIT.C43565)
    C4316 = PermissibleValue(text="C4316",
                                 description="Ameloblastic Fibroma",
                                 meaning=NCIT.C4316)
    C4155 = PermissibleValue(text="C4155",
                                 description="Parathyroid Gland Water-Clear Cell Adenoma",
                                 meaning=NCIT.C4155)
    C4110 = PermissibleValue(text="C4110",
                                 description="Intraepidermal Epithelioma of Jadassohn",
                                 meaning=NCIT.C4110)
    C4201 = PermissibleValue(text="C4201",
                                 description="Adenocarcinoma with Spindle Cell Metaplasia",
                                 meaning=NCIT.C4201)
    C4254 = PermissibleValue(text="C4254",
                                 description="Spindle Cell Lipoma",
                                 meaning=NCIT.C4254)
    C4245 = PermissibleValue(text="C4245",
                                 description="Elastofibroma",
                                 meaning=NCIT.C4245)
    C4229 = PermissibleValue(text="C4229",
                                 description="Neuronevus",
                                 meaning=NCIT.C4229)
    C4219 = PermissibleValue(text="C4219",
                                 description="Malignant Extra-Adrenal Paraganglioma",
                                 meaning=NCIT.C4219)
    C4222 = PermissibleValue(text="C4222",
                                 description="Glomangioma",
                                 meaning=NCIT.C4222)
    C4288 = PermissibleValue(text="C4288",
                                 description="Intermediate Immature Teratoma",
                                 meaning=NCIT.C4288)
    C4252 = PermissibleValue(text="C4252",
                                 description="Round Cell Liposarcoma",
                                 meaning=NCIT.C4252)
    C45602 = PermissibleValue(text="C45602",
                                   description="Lung Mixed Squamous Cell and Glandular Papilloma",
                                   meaning=NCIT.C45602)
    C40223 = PermissibleValue(text="C40223",
                                   description="Uterine Corpus Low Grade Endometrial Stromal Sarcoma",
                                   meaning=NCIT.C40223)
    C40034 = PermissibleValue(text="C40034",
                                   description="Ovarian Mucinous Adenocarcinofibroma",
                                   meaning=NCIT.C40034)
    C40970 = PermissibleValue(text="C40970",
                                   description="Angiocentric Immunoproliferative Lesion",
                                   meaning=NCIT.C40970)
    C39972 = PermissibleValue(text="C39972",
                                   description="Moderately Differentiated Ovarian Sertoli-Leydig Cell Tumor, Variant with Heterologous Elements",
                                   meaning=NCIT.C39972)
    C39968 = PermissibleValue(text="C39968",
                                   description="Moderately Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                   meaning=NCIT.C39968)
    C40060 = PermissibleValue(text="C40060",
                                   description="Ovarian Endometrioid Adenocarcinofibroma",
                                   meaning=NCIT.C40060)
    C40079 = PermissibleValue(text="C40079",
                                   description="Ovarian Clear Cell Adenocarcinofibroma",
                                   meaning=NCIT.C40079)
    C3904 = PermissibleValue(text="C3904",
                                 description="Papillary Meningioma",
                                 meaning=NCIT.C3904)
    C65200 = PermissibleValue(text="C65200",
                                   description="Thyroid Gland Follicular Carcinoma, Minimally Invasive",
                                   meaning=NCIT.C65200)
    C65180 = PermissibleValue(text="C65180",
                                   description="Squamous Cell Carcinoma, Clear Cell Type",
                                   meaning=NCIT.C65180)
    C63622 = PermissibleValue(text="C63622",
                                   description="Undifferentiated Carcinoma with Osteoclast-Like Giant Cells",
                                   meaning=NCIT.C63622)
    C53595 = PermissibleValue(text="C53595",
                                   description="Ectopic Hamartomatous Thymoma",
                                   meaning=NCIT.C53595)
    C54664 = PermissibleValue(text="C54664",
                                   description="Hidradenocarcinoma",
                                   meaning=NCIT.C54664)
    C53958 = PermissibleValue(text="C53958",
                                   description="High Grade Surface Osteosarcoma",
                                   meaning=NCIT.C53958)
    C62282 = PermissibleValue(text="C62282",
                                   description="Skin Nodular Basal Cell Carcinoma",
                                   meaning=NCIT.C62282)
    C48876 = PermissibleValue(text="C48876",
                                   description="Dedifferentiated Chordoma",
                                   meaning=NCIT.C48876)
    C4722 = PermissibleValue(text="C4722",
                                 description="Clear Cell Meningioma",
                                 meaning=NCIT.C4722)
    C4723 = PermissibleValue(text="C4723",
                                 description="Atypical Meningioma",
                                 meaning=NCIT.C4723)
    C9473 = PermissibleValue(text="C9473",
                                 description="Lactating Adenoma",
                                 meaning=NCIT.C9473)
    C95514 = PermissibleValue(text="C95514",
                                   description="Pancreatic Intraductal Papillary Mucinous Neoplasm, Oncocytic-Type",
                                   meaning=NCIT.C95514)
    C3706 = PermissibleValue(text="C3706",
                                 description="Medullomyoblastoma with Myogenic Differentiation",
                                 meaning=NCIT.C3706)
    C3699 = PermissibleValue(text="C3699",
                                 description="Intramuscular Hemangioma",
                                 meaning=NCIT.C3699)
    C3703 = PermissibleValue(text="C3703",
                                 description="Pleomorphic Lipoma",
                                 meaning=NCIT.C3703)
    C3760 = PermissibleValue(text="C3760",
                                 description="Hidrocystoma",
                                 meaning=NCIT.C3760)
    C3761 = PermissibleValue(text="C3761",
                                 description="Syringoma",
                                 meaning=NCIT.C3761)
    C3779 = PermissibleValue(text="C3779",
                                 description="Giant Cell Carcinoma",
                                 meaning=NCIT.C3779)
    C3275 = PermissibleValue(text="C3275",
                                 description="Neuroma",
                                 meaning=NCIT.C3275)
    C3254 = PermissibleValue(text="C3254",
                                 description="Angiomyxoma",
                                 meaning=NCIT.C3254)
    C27273 = PermissibleValue(text="C27273",
                                   description="Poroma",
                                   meaning=NCIT.C27273)
    C27848 = PermissibleValue(text="C27848",
                                   description="Endometrial Endometrioid Adenocarcinoma, Ciliated Variant",
                                   meaning=NCIT.C27848)
    C27839 = PermissibleValue(text="C27839",
                                   description="Endometrial Endometrioid Adenocarcinoma, Secretory Variant",
                                   meaning=NCIT.C27839)
    C2860 = PermissibleValue(text="C2860",
                                 description="Adrenal Rest Tumor",
                                 meaning=NCIT.C2860)
    C3204 = PermissibleValue(text="C3204",
                                 description="Lymphangioleiomyoma",
                                 meaning=NCIT.C3204)
    C3082 = PermissibleValue(text="C3082",
                                 description="Heavy Chain Disease",
                                 meaning=NCIT.C3082)
    C173927 = PermissibleValue(text="C173927",
                                     description="Cemento-Osseous Dysplasia",
                                     meaning=NCIT.C173927)
    C126594 = PermissibleValue(text="C126594",
                                     description="Follicular Variant Thyroid Gland Papillary Carcinoma",
                                     meaning=NCIT.C126594)
    C129319 = PermissibleValue(text="C129319",
                                     description="Oligodendroglioma, Not Otherwise Specified",
                                     meaning=NCIT.C129319)
    C82431 = PermissibleValue(text="C82431",
                                   description="Acute Myeloid Leukemia with Mutated NPM1",
                                   meaning=NCIT.C82431)
    C4174 = PermissibleValue(text="C4174",
                                 description="Sebaceous Adenoma",
                                 meaning=NCIT.C4174)
    C27856 = PermissibleValue(text="C27856",
                                   description="Diffuse Large B-Cell Lymphoma Arising in HHV8-Positive Multicentric Castleman Disease",
                                   meaning=NCIT.C27856)
    C81758 = PermissibleValue(text="C81758",
                                   description="Fibroblastic Reticular Cell Tumor",
                                   meaning=NCIT.C81758)
    C82212 = PermissibleValue(text="C82212",
                                   description="Mixed Phenotype Acute Leukemia, B/Myeloid, Not Otherwise Specified",
                                   meaning=NCIT.C82212)
    C82192 = PermissibleValue(text="C82192",
                                   description="Mixed Phenotype Acute Leukemia with t(9;22)(q34.1;q11.2); BCR-ABL1",
                                   meaning=NCIT.C82192)
    C82213 = PermissibleValue(text="C82213",
                                   description="Mixed Phenotype Acute Leukemia, T/Myeloid, Not Otherwise Specified",
                                   meaning=NCIT.C82213)
    C80334 = PermissibleValue(text="C80334",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(12;21)(p13.2;q22.1); ETV6-RUNX1",
                                   meaning=NCIT.C80334)
    C80340 = PermissibleValue(text="C80340",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(5;14)(q31.1;q32.3); IL3-IGH",
                                   meaning=NCIT.C80340)
    C80326 = PermissibleValue(text="C80326",
                                   description="B Lymphoblastic Leukemia/Lymphoma, Not Otherwise Specified",
                                   meaning=NCIT.C80326)
    C80331 = PermissibleValue(text="C80331",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(9;22)(q34.1;q11.2); BCR-ABL1",
                                   meaning=NCIT.C80331)
    C80332 = PermissibleValue(text="C80332",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(v;11q23.3); MLL Rearranged",
                                   meaning=NCIT.C80332)
    C66933 = PermissibleValue(text="C66933",
                                   description="Breast Ductal Carcinoma In Situ, Solid Type",
                                   meaning=NCIT.C66933)
    C66719 = PermissibleValue(text="C66719",
                                   description="Breast Atypical Medullary Carcinoma",
                                   meaning=NCIT.C66719)
    C66807 = PermissibleValue(text="C66807",
                                   description="Ciliary Body Benign Medulloepithelioma",
                                   meaning=NCIT.C66807)
    C6876 = PermissibleValue(text="C6876",
                                 description="Lung Large Cell Carcinoma with Rhabdoid Phenotype",
                                 meaning=NCIT.C6876)
    C6781 = PermissibleValue(text="C6781",
                                 description="Stromal Neoplasm",
                                 meaning=NCIT.C6781)
    C5728 = PermissibleValue(text="C5728",
                                 description="Solid Pseudopapillary Carcinoma of the Pancreas",
                                 meaning=NCIT.C5728)
    C4299 = PermissibleValue(text="C4299",
                                 description="Verrucous Hemangioma",
                                 meaning=NCIT.C4299)
    C4323 = PermissibleValue(text="C4323",
                                 description="Pleomorphic Xanthoastrocytoma",
                                 meaning=NCIT.C4323)
    C4325 = PermissibleValue(text="C4325",
                                 description="Giant Cell Glioblastoma",
                                 meaning=NCIT.C4325)
    C4318 = PermissibleValue(text="C4318",
                                 description="Gliomatosis Cerebri",
                                 meaning=NCIT.C4318)
    C4169 = PermissibleValue(text="C4169",
                                 description="Apocrine Carcinoma",
                                 meaning=NCIT.C4169)
    C4135 = PermissibleValue(text="C4135",
                                 description="Multiple Adenomatous Polyps",
                                 meaning=NCIT.C4135)
    C4116 = PermissibleValue(text="C4116",
                                 description="Stage 0 Transitional Cell Carcinoma",
                                 meaning=NCIT.C4116)
    C4153 = PermissibleValue(text="C4153",
                                 description="Glycogen-Rich Carcinoma",
                                 meaning=NCIT.C4153)
    C4108 = PermissibleValue(text="C4108",
                                 description="Superficial Multifocal Basal Cell Carcinoma",
                                 meaning=NCIT.C4108)
    C4123 = PermissibleValue(text="C4123",
                                 description="Adenocarcinoma In Situ",
                                 meaning=NCIT.C4123)
    C4178 = PermissibleValue(text="C4178",
                                 description="Borderline Papillary Cystadenoma",
                                 meaning=NCIT.C4178)
    C4199 = PermissibleValue(text="C4199",
                                 description="Epithelial-Myoepithelial Carcinoma",
                                 meaning=NCIT.C4199)
    C4188 = PermissibleValue(text="C4188",
                                 description="Comedocarcinoma",
                                 meaning=NCIT.C4188)
    C4148 = PermissibleValue(text="C4148",
                                 description="Pituitary Gland Mixed Acidophil-Basophil Adenoma",
                                 meaning=NCIT.C4148)
    C4152 = PermissibleValue(text="C4152",
                                 description="Lipid-Rich Carcinoma",
                                 meaning=NCIT.C4152)
    C4137 = PermissibleValue(text="C4137",
                                 description="Solid Carcinoma",
                                 meaning=NCIT.C4137)
    C4239 = PermissibleValue(text="C4239",
                                 description="Type B Spindle Cell Melanoma",
                                 meaning=NCIT.C4239)
    C4238 = PermissibleValue(text="C4238",
                                 description="Type A Spindle Cell Melanoma",
                                 meaning=NCIT.C4238)
    C4265 = PermissibleValue(text="C4265",
                                 description="Pancreatoblastoma",
                                 meaning=NCIT.C4265)
    C4241 = PermissibleValue(text="C4241",
                                 description="Cellular Blue Nevus",
                                 meaning=NCIT.C4241)
    C4296 = PermissibleValue(text="C4296",
                                 description="Venous Hemangioma",
                                 meaning=NCIT.C4296)
    C4208 = PermissibleValue(text="C4208",
                                 description="Ovarian Sex Cord Tumor with Annular Tubules",
                                 meaning=NCIT.C4208)
    C4217 = PermissibleValue(text="C4217",
                                 description="Parasympathetic Paraganglioma",
                                 meaning=NCIT.C4217)
    C40177 = PermissibleValue(text="C40177",
                                   description="Uterine Corpus Smooth Muscle Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C40177)
    C4074 = PermissibleValue(text="C4074",
                                 description="Centroblastic Lymphoma",
                                 meaning=NCIT.C4074)
    C6476 = PermissibleValue(text="C6476",
                                 description="Dedifferentiated Chondrosarcoma",
                                 meaning=NCIT.C6476)
    C6493 = PermissibleValue(text="C6493",
                                 description="Plexiform Fibrohistiocytic Tumor",
                                 meaning=NCIT.C6493)
    C65193 = PermissibleValue(text="C65193",
                                   description="Flat Adenoma",
                                   meaning=NCIT.C65193)
    C6494 = PermissibleValue(text="C6494",
                                 description="Angiomatoid Fibrous Histiocytoma",
                                 meaning=NCIT.C6494)
    C5979 = PermissibleValue(text="C5979",
                                 description="Salivary Gland Canalicular Adenoma",
                                 meaning=NCIT.C5979)
    C5325 = PermissibleValue(text="C5325",
                                 description="Intestinal Gangliocytic Paraganglioma",
                                 meaning=NCIT.C5325)
    C48622 = PermissibleValue(text="C48622",
                                   description="Mucosal Lentiginous Melanoma",
                                   meaning=NCIT.C48622)
    C2974 = PermissibleValue(text="C2974",
                                 description="Papillary Cystadenoma",
                                 meaning=NCIT.C2974)
    C2927 = PermissibleValue(text="C2927",
                                 description="Papillary Carcinoma",
                                 meaning=NCIT.C2927)
    C9303 = PermissibleValue(text="C9303",
                                 description="Mastocytoma",
                                 meaning=NCIT.C9303)
    C92552 = PermissibleValue(text="C92552",
                                   description="Angiocentric Glioma",
                                   meaning=NCIT.C92552)
    C3705 = PermissibleValue(text="C3705",
                                 description="Pleomorphic Liposarcoma",
                                 meaning=NCIT.C3705)
    C35765 = PermissibleValue(text="C35765",
                                   description="Histiocytoma",
                                   meaning=NCIT.C35765)
    C3757 = PermissibleValue(text="C3757",
                                 description="Placental-Site Gestational Trophoblastic Tumor",
                                 meaning=NCIT.C3757)
    C3297 = PermissibleValue(text="C3297",
                                 description="Osteoid Osteoma",
                                 meaning=NCIT.C3297)
    C27722 = PermissibleValue(text="C27722",
                                   description="Therapy-Related Myelodysplastic Syndrome",
                                   meaning=NCIT.C27722)
    C27092 = PermissibleValue(text="C27092",
                                   description="Small Cell Carcinoma, Fusiform Cell Type",
                                   meaning=NCIT.C27092)
    C3060 = PermissibleValue(text="C3060",
                                 description="Glomus Tumor",
                                 meaning=NCIT.C3060)
    C3086 = PermissibleValue(text="C3086",
                                 description="Cavernous Hemangioma",
                                 meaning=NCIT.C3086)
    C12917 = PermissibleValue(text="C12917",
                                   description="Malignant Cell",
                                   meaning=NCIT.C12917)
    C7203 = PermissibleValue(text="C7203",
                                 description="Blastic Plasmacytoid Dendritic Cell Neoplasm",
                                 meaning=NCIT.C7203)
    C6919 = PermissibleValue(text="C6919",
                                 description="T Lymphoblastic Lymphoma",
                                 meaning=NCIT.C6919)
    C82203 = PermissibleValue(text="C82203",
                                   description="Mixed Phenotype Acute Leukemia with t(v;11q23.3); MLL Rearranged",
                                   meaning=NCIT.C82203)
    C80374 = PermissibleValue(text="C80374",
                                   description="Systemic EBV-Positive T-Cell Lymphoma of Childhood",
                                   meaning=NCIT.C80374)
    C66776 = PermissibleValue(text="C66776",
                                   description="Gonadal Polyembryoma",
                                   meaning=NCIT.C66776)
    C66753 = PermissibleValue(text="C66753",
                                   description="Malignant Melanoma in Precancerous Melanosis",
                                   meaning=NCIT.C66753)
    C66991 = PermissibleValue(text="C66991",
                                   description="Mixed Testicular Sex Cord-Stromal Tumor",
                                   meaning=NCIT.C66991)
    C8984 = PermissibleValue(text="C8984",
                                 description="Female Reproductive System Adenofibroma",
                                 meaning=NCIT.C8984)
    C8419 = PermissibleValue(text="C8419",
                                 description="Dysplastic Cerebellar Gangliocytoma",
                                 meaning=NCIT.C8419)
    C7225 = PermissibleValue(text="C7225",
                                 description="ALK-Positive Large B-Cell Lymphoma",
                                 meaning=NCIT.C7225)
    C6577 = PermissibleValue(text="C6577",
                                 description="Myxoma",
                                 meaning=NCIT.C6577)
    C6582 = PermissibleValue(text="C6582",
                                 description="Ossifying Fibromyxoid Tumor",
                                 meaning=NCIT.C6582)
    C7504 = PermissibleValue(text="C7504",
                                 description="Adult Cystic Nephroma",
                                 meaning=NCIT.C7504)
    C7440 = PermissibleValue(text="C7440",
                                 description="Papilloma",
                                 meaning=NCIT.C7440)
    C6921 = PermissibleValue(text="C6921",
                                 description="Langerhans Cell Sarcoma",
                                 meaning=NCIT.C6921)
    C6926 = PermissibleValue(text="C6926",
                                 description="Stromal Sarcoma",
                                 meaning=NCIT.C6926)
    C6900 = PermissibleValue(text="C6900",
                                 description="Epithelioid Trophoblastic Tumor",
                                 meaning=NCIT.C6900)
    C6891 = PermissibleValue(text="C6891",
                                 description="Meningeal Melanomatosis",
                                 meaning=NCIT.C6891)
    C6894 = PermissibleValue(text="C6894",
                                 description="Malignant Solitary Fibrous Tumor",
                                 meaning=NCIT.C6894)
    C6890 = PermissibleValue(text="C6890",
                                 description="Meningeal Melanocytosis",
                                 meaning=NCIT.C6890)
    C4334 = PermissibleValue(text="C4334",
                                 description="Meningeal Sarcomatosis",
                                 meaning=NCIT.C4334)
    C43625 = PermissibleValue(text="C43625",
                                   description="Pleomorphic Hepatocellular Carcinoma",
                                   meaning=NCIT.C43625)
    C4165 = PermissibleValue(text="C4165",
                                 description="Adrenal Cortex Clear Cell Adenoma",
                                 meaning=NCIT.C4165)
    C41251 = PermissibleValue(text="C41251",
                                   description="Pancreatic Intraductal Papillary-Mucinous Neoplasm, High Grade",
                                   meaning=NCIT.C41251)
    C4121 = PermissibleValue(text="C4121",
                                 description="Basaloid Carcinoma",
                                 meaning=NCIT.C4121)
    C4120 = PermissibleValue(text="C4120",
                                 description="Sarcomatoid Transitional Cell Carcinoma",
                                 meaning=NCIT.C4120)
    C4151 = PermissibleValue(text="C4151",
                                 description="Clear Cell Adenoma",
                                 meaning=NCIT.C4151)
    C4163 = PermissibleValue(text="C4163",
                                 description="Adrenal Cortex Compact Cell Adenoma",
                                 meaning=NCIT.C4163)
    C4149 = PermissibleValue(text="C4149",
                                 description="Pituitary Gland Mixed Acidophil-Basophil Carcinoma",
                                 meaning=NCIT.C4149)
    C4167 = PermissibleValue(text="C4167",
                                 description="Adrenal Cortex Mixed Cell Adenoma",
                                 meaning=NCIT.C4167)
    C4166 = PermissibleValue(text="C4166",
                                 description="Adrenal Cortex Glomerulosa Cell Adenoma",
                                 meaning=NCIT.C4166)
    C4279 = PermissibleValue(text="C4279",
                                 description="Biphasic Synovial Sarcoma",
                                 meaning=NCIT.C4279)
    C4267 = PermissibleValue(text="C4267",
                                 description="Benign Mesenchymoma",
                                 meaning=NCIT.C4267)
    C4228 = PermissibleValue(text="C4228",
                                 description="Regressing Melanoma",
                                 meaning=NCIT.C4228)
    C4203 = PermissibleValue(text="C4203",
                                 description="Ovarian Luteinized Thecoma",
                                 meaning=NCIT.C4203)
    C4249 = PermissibleValue(text="C4249",
                                 description="Fibrolipoma",
                                 meaning=NCIT.C4249)
    C4234 = PermissibleValue(text="C4234",
                                 description="Giant Congenital Nevus",
                                 meaning=NCIT.C4234)
    C65190 = PermissibleValue(text="C65190",
                                   description="Malignant Somatostatinoma",
                                   meaning=NCIT.C65190)
    C6519 = PermissibleValue(text="C6519",
                                 description="Spindle Cell Rhabdomyosarcoma",
                                 meaning=NCIT.C6519)
    C65151 = PermissibleValue(text="C65151",
                                   description="Non-Small Cell Carcinoma",
                                   meaning=NCIT.C65151)
    C5950 = PermissibleValue(text="C5950",
                                 description="Salivary Gland Basal Cell Adenoma",
                                 meaning=NCIT.C5950)
    C53459 = PermissibleValue(text="C53459",
                                   description="Chondroma",
                                   meaning=NCIT.C53459)
    C54244 = PermissibleValue(text="C54244",
                                   description="Basaloid Squamous Cell Carcinoma",
                                   meaning=NCIT.C54244)
    C54319 = PermissibleValue(text="C54319",
                                   description="Calcifying Cystic Odontogenic Tumor",
                                   meaning=NCIT.C54319)
    C49107 = PermissibleValue(text="C49107",
                                   description="Giant Cell Tumor of Soft Tissue",
                                   meaning=NCIT.C49107)
    C5117 = PermissibleValue(text="C5117",
                                 description="Spiradenocarcinoma",
                                 meaning=NCIT.C5117)
    C4700 = PermissibleValue(text="C4700",
                                 description="Giant Cell Fibroblastoma",
                                 meaning=NCIT.C4700)
    C3693 = PermissibleValue(text="C3693",
                                 description="Carcinomatosis",
                                 meaning=NCIT.C3693)
    C3678 = PermissibleValue(text="C3678",
                                 description="Salivary Gland Basal Cell Adenocarcinoma",
                                 meaning=NCIT.C3678)
    C35830 = PermissibleValue(text="C35830",
                                   description="Columnar Cell Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C35830)
    C3726 = PermissibleValue(text="C3726",
                                 description="Adenomyoma",
                                 meaning=NCIT.C3726)
    C3746 = PermissibleValue(text="C3746",
                                 description="Small Cell Sarcoma",
                                 meaning=NCIT.C3746)
    C3296 = PermissibleValue(text="C3296",
                                 description="Osteoma",
                                 meaning=NCIT.C3296)
    C3255 = PermissibleValue(text="C3255",
                                 description="Myxosarcoma",
                                 meaning=NCIT.C3255)
    C3482 = PermissibleValue(text="C3482",
                                 description="Metastatic Carcinoma",
                                 meaning=NCIT.C3482)
    C2879 = PermissibleValue(text="C2879",
                                 description="Neoplasm of the Diffuse Neuroendocrine System",
                                 meaning=NCIT.C2879)
    C3041 = PermissibleValue(text="C3041",
                                 description="Fibroma",
                                 meaning=NCIT.C3041)
    C3072 = PermissibleValue(text="C3072",
                                 description="Ovarian Gynandroblastoma",
                                 meaning=NCIT.C3072)
    C121793 = PermissibleValue(text="C121793",
                                     description="Undifferentiated/Unclassified Sarcoma",
                                     meaning=NCIT.C121793)
    C128847 = PermissibleValue(text="C128847",
                                     description="Lung Micropapillary Adenocarcinoma",
                                     meaning=NCIT.C128847)
    C4522 = PermissibleValue(text="C4522",
                                 description="Stage 0 Vulvar Cancer AJCC v6",
                                 meaning=NCIT.C4522)
    C51302 = PermissibleValue(text="C51302",
                                   description="Hereditary Leiomyomatosis and Renal Cell Carcinoma",
                                   meaning=NCIT.C51302)
    C9245 = PermissibleValue(text="C9245",
                                 description="Invasive Breast Carcinoma",
                                 meaning=NCIT.C9245)
    C9301 = PermissibleValue(text="C9301",
                                 description="Central Nervous System Lymphoma",
                                 meaning=NCIT.C9301)
    C7602 = PermissibleValue(text="C7602",
                                 description="Halo Nevus",
                                 meaning=NCIT.C7602)
    C66748 = PermissibleValue(text="C66748",
                                   description="Unclassified Testicular Sex Cord-Stromal Tumor",
                                   meaning=NCIT.C66748)
    C84277 = PermissibleValue(text="C84277",
                                   description="Myeloid/Lymphoid Neoplasms with FGFR1 Rearrangement",
                                   meaning=NCIT.C84277)
    C7217 = PermissibleValue(text="C7217",
                                 description="Primary Cutaneous Follicle Center Lymphoma",
                                 meaning=NCIT.C7217)
    C7224 = PermissibleValue(text="C7224",
                                 description="Plasmablastic Lymphoma",
                                 meaning=NCIT.C7224)
    C7399 = PermissibleValue(text="C7399",
                                 description="Villous Adenoma",
                                 meaning=NCIT.C7399)
    C6918 = PermissibleValue(text="C6918",
                                 description="Subcutaneous Panniculitis-Like T-Cell Lymphoma",
                                 meaning=NCIT.C6918)
    C7017 = PermissibleValue(text="C7017",
                                 description="Granular Cell Tumor of the Sellar Region",
                                 meaning=NCIT.C7017)
    C6881 = PermissibleValue(text="C6881",
                                 description="Bile Duct Intraductal Papillary Neoplasm",
                                 meaning=NCIT.C6881)
    C6885 = PermissibleValue(text="C6885",
                                 description="Thymoma Type AB",
                                 meaning=NCIT.C6885)
    C5727 = PermissibleValue(text="C5727",
                                 description="Pancreatic Acinar Cell Cystadenocarcinoma",
                                 meaning=NCIT.C5727)
    C4272 = PermissibleValue(text="C4272",
                                 description="Breast Pericanalicular Fibroadenoma",
                                 meaning=NCIT.C4272)
    C4237 = PermissibleValue(text="C4237",
                                 description="Spindle Cell Melanoma",
                                 meaning=NCIT.C4237)
    C4271 = PermissibleValue(text="C4271",
                                 description="Breast Intracanalicular Fibroadenoma",
                                 meaning=NCIT.C4271)
    C4204 = PermissibleValue(text="C4204",
                                 description="Ovarian Sclerosing Stromal Tumor",
                                 meaning=NCIT.C4204)
    C4207 = PermissibleValue(text="C4207",
                                 description="Juvenile Type Granulosa Cell Tumor",
                                 meaning=NCIT.C4207)
    C4236 = PermissibleValue(text="C4236",
                                 description="Epithelioid Cell Melanoma",
                                 meaning=NCIT.C4236)
    C4273 = PermissibleValue(text="C4273",
                                 description="Breast Giant Fibroadenoma",
                                 meaning=NCIT.C4273)
    C4276 = PermissibleValue(text="C4276",
                                 description="Breast Juvenile Fibroadenoma",
                                 meaning=NCIT.C4276)
    C4099 = PermissibleValue(text="C4099",
                                 description="Small Cell Intermediate Cell Carcinoma",
                                 meaning=NCIT.C4099)
    C6481 = PermissibleValue(text="C6481",
                                 description="Inflammatory Myofibroblastic Tumor",
                                 meaning=NCIT.C6481)
    C6496 = PermissibleValue(text="C6496",
                                 description="Myxofibrosarcoma",
                                 meaning=NCIT.C6496)
    C49024 = PermissibleValue(text="C49024",
                                   description="Low Grade Myofibroblastic Sarcoma",
                                   meaning=NCIT.C49024)
    C2971 = PermissibleValue(text="C2971",
                                 description="Cystadenocarcinoma",
                                 meaning=NCIT.C2971)
    C5100 = PermissibleValue(text="C5100",
                                 description="Renomedullary Interstitial Cell Tumor",
                                 meaning=NCIT.C5100)
    C46004 = PermissibleValue(text="C46004",
                                   description="Thyroid Gland Papillary Microcarcinoma",
                                   meaning=NCIT.C46004)
    C4753 = PermissibleValue(text="C4753",
                                 description="B-Cell Prolymphocytic Leukemia",
                                 meaning=NCIT.C4753)
    C4662 = PermissibleValue(text="C4662",
                                 description="Meningeal Melanocytoma",
                                 meaning=NCIT.C4662)
    C9505 = PermissibleValue(text="C9505",
                                 description="Dysembryoplastic Neuroepithelial Tumor",
                                 meaning=NCIT.C9505)
    C3697 = PermissibleValue(text="C3697",
                                 description="Myxopapillary Ependymoma",
                                 meaning=NCIT.C3697)
    C3704 = PermissibleValue(text="C3704",
                                 description="Dedifferentiated Liposarcoma",
                                 meaning=NCIT.C3704)
    C3736 = PermissibleValue(text="C3736",
                                 description="Adrenal Gland Myelolipoma",
                                 meaning=NCIT.C3736)
    C3733 = PermissibleValue(text="C3733",
                                 description="Angiolipoma",
                                 meaning=NCIT.C3733)
    C2853 = PermissibleValue(text="C2853",
                                 description="Papillary Adenocarcinoma",
                                 meaning=NCIT.C2853)
    C6042 = PermissibleValue(text="C6042",
                                 description="Thyroid Gland Hurthle Cell Adenoma",
                                 meaning=NCIT.C6042)
    C4050 = PermissibleValue(text="C4050",
                                 description="Oligoastrocytoma",
                                 meaning=NCIT.C4050)
    C5398 = PermissibleValue(text="C5398",
                                 description="Central Nervous System Embryonal Tumor, Not Otherwise Specified",
                                 meaning=NCIT.C5398)
    C8377 = PermissibleValue(text="C8377",
                                 description="Papillary Serous Cystadenocarcinoma",
                                 meaning=NCIT.C8377)
    C7401 = PermissibleValue(text="C7401",
                                 description="Hairy Cell Leukemia Variant",
                                 meaning=NCIT.C7401)
    C6888 = PermissibleValue(text="C6888",
                                 description="Thymoma Type B2",
                                 meaning=NCIT.C6888)
    C4313 = PermissibleValue(text="C4313",
                                 description="Ameloblastoma",
                                 meaning=NCIT.C4313)
    C4130 = PermissibleValue(text="C4130",
                                 description="Bile Duct Mucinous Cystic Neoplasm with an Associated Invasive Carcinoma",
                                 meaning=NCIT.C4130)
    C4113 = PermissibleValue(text="C4113",
                                 description="Trichilemmoma",
                                 meaning=NCIT.C4113)
    C4129 = PermissibleValue(text="C4129",
                                 description="Bile Duct Mucinous Cystic Neoplasm",
                                 meaning=NCIT.C4129)
    C4133 = PermissibleValue(text="C4133",
                                 description="Tubular Adenoma",
                                 meaning=NCIT.C4133)
    C4124 = PermissibleValue(text="C4124",
                                 description="Metastatic Adenocarcinoma",
                                 meaning=NCIT.C4124)
    C4242 = PermissibleValue(text="C4242",
                                 description="Benign Soft Tissue Neoplasm",
                                 meaning=NCIT.C4242)
    C42598 = PermissibleValue(text="C42598",
                                   description="Low Grade Appendix Mucinous Neoplasm",
                                   meaning=NCIT.C42598)
    C45340 = PermissibleValue(text="C45340",
                                   description="Primary Cutaneous Gamma-Delta T-Cell Lymphoma",
                                   meaning=NCIT.C45340)
    C3902 = PermissibleValue(text="C3902",
                                 description="Telangiectatic Osteosarcoma",
                                 meaning=NCIT.C3902)
    C53998 = PermissibleValue(text="C53998",
                                   description="Benign Gastrointestinal Stromal Tumor",
                                   meaning=NCIT.C53998)
    C54297 = PermissibleValue(text="C54297",
                                   description="Metastasizing Ameloblastoma",
                                   meaning=NCIT.C54297)
    C4752 = PermissibleValue(text="C4752",
                                 description="T-Cell Prolymphocytic Leukemia",
                                 meaning=NCIT.C4752)
    C46093 = PermissibleValue(text="C46093",
                                   description="Oncocytic Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C46093)
    C9476 = PermissibleValue(text="C9476",
                                 description="Desmoplastic Infantile Astrocytoma",
                                 meaning=NCIT.C9476)
    C9286 = PermissibleValue(text="C9286",
                                 description="Indolent Systemic Mastocytosis",
                                 meaning=NCIT.C9286)
    C35702 = PermissibleValue(text="C35702",
                                   description="Salivary Gland Polymorphous Adenocarcinoma",
                                   meaning=NCIT.C35702)
    C3780 = PermissibleValue(text="C3780",
                                 description="Large Cell Carcinoma",
                                 meaning=NCIT.C3780)
    C3734 = PermissibleValue(text="C3734",
                                 description="Angiomyolipoma",
                                 meaning=NCIT.C3734)
    C3309 = PermissibleValue(text="C3309",
                                 description="Extra-Adrenal Paraganglioma",
                                 meaning=NCIT.C3309)
    C2855 = PermissibleValue(text="C2855",
                                 description="Adenoma",
                                 meaning=NCIT.C2855)
    C121619 = PermissibleValue(text="C121619",
                                     description="Nongerminomatous Germ Cell Tumor",
                                     meaning=NCIT.C121619)
    C7950 = PermissibleValue(text="C7950",
                                 description="Invasive Breast Lobular Carcinoma",
                                 meaning=NCIT.C7950)
    C3708 = PermissibleValue(text="C3708",
                                 description="Germ Cell Tumor",
                                 meaning=NCIT.C3708)
    C9015 = PermissibleValue(text="C9015",
                                 description="Mature Teratoma",
                                 meaning=NCIT.C9015)
    C67107 = PermissibleValue(text="C67107",
                                   description="Benign Teratoma",
                                   meaning=NCIT.C67107)
    C7191 = PermissibleValue(text="C7191",
                                 description="Grade 3a Follicular Lymphoma",
                                 meaning=NCIT.C7191)
    C7151 = PermissibleValue(text="C7151",
                                 description="Monoclonal Immunoglobulin Deposition Disease",
                                 meaning=NCIT.C7151)
    C6875 = PermissibleValue(text="C6875",
                                 description="Large Cell Neuroendocrine Carcinoma",
                                 meaning=NCIT.C6875)
    C4457 = PermissibleValue(text="C4457",
                                 description="Pleural Solitary Fibrous Tumor",
                                 meaning=NCIT.C4457)
    C43627 = PermissibleValue(text="C43627",
                                   description="Sarcomatoid Hepatocellular Carcinoma",
                                   meaning=NCIT.C43627)
    C4278 = PermissibleValue(text="C4278",
                                 description="Epithelial Synovial Sarcoma",
                                 meaning=NCIT.C4278)
    C4205 = PermissibleValue(text="C4205",
                                 description="Malignant Granulosa Cell Tumor",
                                 meaning=NCIT.C4205)
    C45754 = PermissibleValue(text="C45754",
                                   description="Cystic Tumor of the Atrioventricular Node",
                                   meaning=NCIT.C45754)
    C6469 = PermissibleValue(text="C6469",
                                 description="Osteosarcoma Arising in Paget Disease of Bone",
                                 meaning=NCIT.C6469)
    C65187 = PermissibleValue(text="C65187",
                                   description="Malignant Pancreatic Glucagonoma",
                                   meaning=NCIT.C65187)
    C54317 = PermissibleValue(text="C54317",
                                   description="Odontoameloblastoma",
                                   meaning=NCIT.C54317)
    C4882 = PermissibleValue(text="C4882",
                                 description="Benign Muscle Neoplasm",
                                 meaning=NCIT.C4882)
    C94524 = PermissibleValue(text="C94524",
                                   description="Pituicytoma",
                                   meaning=NCIT.C94524)
    C3696 = PermissibleValue(text="C3696",
                                 description="Subependymal Giant Cell Astrocytoma",
                                 meaning=NCIT.C3696)
    C3302 = PermissibleValue(text="C3302",
                                 description="Extramammary Paget Disease",
                                 meaning=NCIT.C3302)
    C3287 = PermissibleValue(text="C3287",
                                 description="Odontoma",
                                 meaning=NCIT.C3287)
    C27255 = PermissibleValue(text="C27255",
                                   description="Eccrine Carcinoma",
                                   meaning=NCIT.C27255)
    C27005 = PermissibleValue(text="C27005",
                                   description="Spindle Cell Sarcoma",
                                   meaning=NCIT.C27005)
    C3358 = PermissibleValue(text="C3358",
                                 description="Rhabdomyoma",
                                 meaning=NCIT.C3358)
    C3398 = PermissibleValue(text="C3398",
                                 description="Sweat Gland Neoplasm",
                                 meaning=NCIT.C3398)
    C2857 = PermissibleValue(text="C2857",
                                 description="Pituitary Gland Chromophobe Adenoma",
                                 meaning=NCIT.C2857)
    C4035 = PermissibleValue(text="C4035",
                                 description="Thyroid Gland Papillary Carcinoma",
                                 meaning=NCIT.C4035)
    C8574 = PermissibleValue(text="C8574",
                                 description="Myelodysplastic Syndrome with Multilineage Dysplasia",
                                 meaning=NCIT.C8574)
    C8971 = PermissibleValue(text="C8971",
                                 description="Embryonal Rhabdomyosarcoma",
                                 meaning=NCIT.C8971)
    C5754 = PermissibleValue(text="C5754",
                                 description="Clear Cell Hepatocellular Carcinoma",
                                 meaning=NCIT.C5754)
    C7362 = PermissibleValue(text="C7362",
                                 description="Breast Scirrhous Carcinoma",
                                 meaning=NCIT.C7362)
    C7560 = PermissibleValue(text="C7560",
                                 description="Sweat Gland Adenoma",
                                 meaning=NCIT.C7560)
    C6970 = PermissibleValue(text="C6970",
                                 description="Melanotic Schwannoma",
                                 meaning=NCIT.C6970)
    C43356 = PermissibleValue(text="C43356",
                                   description="Syringofibroadenoma",
                                   meaning=NCIT.C43356)
    C4140 = PermissibleValue(text="C4140",
                                 description="Alveolar Adenoma",
                                 meaning=NCIT.C4140)
    C4225 = PermissibleValue(text="C4225",
                                 description="Cutaneous Nodular Melanoma",
                                 meaning=NCIT.C4225)
    C4232 = PermissibleValue(text="C4232",
                                 description="Melanoma in Junctional Nevus",
                                 meaning=NCIT.C4232)
    C4270 = PermissibleValue(text="C4270",
                                 description="Malignant Ovarian Brenner Tumor",
                                 meaning=NCIT.C4270)
    C45509 = PermissibleValue(text="C45509",
                                   description="Lung Fetal Adenocarcinoma",
                                   meaning=NCIT.C45509)
    C45327 = PermissibleValue(text="C45327",
                                   description="Hydroa Vacciniforme-Like Lymphoproliferative Disorder",
                                   meaning=NCIT.C45327)
    C4090 = PermissibleValue(text="C4090",
                                 description="Malignant Giant Cell Neoplasm",
                                 meaning=NCIT.C4090)
    C65186 = PermissibleValue(text="C65186",
                                   description="Malignant Pancreatic Insulinoma",
                                   meaning=NCIT.C65186)
    C4726 = PermissibleValue(text="C4726",
                                 description="Adamantinomatous Craniopharyngioma",
                                 meaning=NCIT.C4726)
    C8025 = PermissibleValue(text="C8025",
                                 description="Malignant Mixed Tumor of the Salivary Gland",
                                 meaning=NCIT.C8025)
    C121932 = PermissibleValue(text="C121932",
                                     description="Giant Cell Tumor of Bone",
                                     meaning=NCIT.C121932)
    C156034 = PermissibleValue(text="C156034",
                                     description="Encapsulated Variant Thyroid Gland Papillary Carcinoma",
                                     meaning=NCIT.C156034)
    C40407 = PermissibleValue(text="C40407",
                                   description="Kidney Wilms Tumor",
                                   meaning=NCIT.C40407)
    C3903 = PermissibleValue(text="C3903",
                                 description="Mixed Glioma",
                                 meaning=NCIT.C3903)
    C8336 = PermissibleValue(text="C8336",
                                 description="High Grade Squamous Intraepithelial Neoplasia",
                                 meaning=NCIT.C8336)
    C80307 = PermissibleValue(text="C80307",
                                   description="Waldenstrom Macroglobulinemia",
                                   meaning=NCIT.C80307)
    C8647 = PermissibleValue(text="C8647",
                                 description="Aggressive NK-Cell Leukemia",
                                 meaning=NCIT.C8647)
    C6846 = PermissibleValue(text="C6846",
                                 description="Thyroid Gland Hyalinizing Trabecular Tumor",
                                 meaning=NCIT.C6846)
    C4487 = PermissibleValue(text="C4487",
                                 description="Tufted Angioma",
                                 meaning=NCIT.C4487)
    C4306 = PermissibleValue(text="C4306",
                                 description="Benign Odontogenic Neoplasm",
                                 meaning=NCIT.C4306)
    C4227 = PermissibleValue(text="C4227",
                                 description="Balloon Cell Melanoma",
                                 meaning=NCIT.C4227)
    C4022 = PermissibleValue(text="C4022",
                                 description="Acral Lentiginous Melanoma",
                                 meaning=NCIT.C4022)
    C4019 = PermissibleValue(text="C4019",
                                 description="Breast Paget Disease and Intraductal Carcinoma",
                                 meaning=NCIT.C4019)
    C6557 = PermissibleValue(text="C6557",
                                 description="Schwannomatosis",
                                 meaning=NCIT.C6557)
    C9349 = PermissibleValue(text="C9349",
                                 description="Plasmacytoma",
                                 meaning=NCIT.C9349)
    C27254 = PermissibleValue(text="C27254",
                                   description="Papillary Eccrine Carcinoma",
                                   meaning=NCIT.C27254)
    C27534 = PermissibleValue(text="C27534",
                                   description="Digital Papillary Adenocarcinoma",
                                   meaning=NCIT.C27534)
    C2872 = PermissibleValue(text="C2872",
                                 description="Refractory Anemia",
                                 meaning=NCIT.C2872)
    C3181 = PermissibleValue(text="C3181",
                                 description="Prolymphocytic Leukemia",
                                 meaning=NCIT.C3181)
    C3169 = PermissibleValue(text="C3169",
                                 description="Mast Cell Leukemia",
                                 meaning=NCIT.C3169)
    C3188 = PermissibleValue(text="C3188",
                                 description="Leydig Cell Tumor",
                                 meaning=NCIT.C3188)
    C3049 = PermissibleValue(text="C3049",
                                 description="Ganglioneuroma",
                                 meaning=NCIT.C3049)
    C45508 = PermissibleValue(text="C45508",
                                   description="Lung Adenocarcinoma, Mixed Subtype",
                                   meaning=NCIT.C45508)
    C40069 = PermissibleValue(text="C40069",
                                   description="Borderline Ovarian Endometrioid Adenofibroma",
                                   meaning=NCIT.C40069)
    C27266 = PermissibleValue(text="C27266",
                                   description="Malignant Lymphoma, Non-Cleaved, Diffuse",
                                   meaning=NCIT.C27266)
    C82427 = PermissibleValue(text="C82427",
                                   description="Acute Myeloid Leukemia (Megakaryoblastic) with t(1;22)(p13.3;q13.1); RBM15-MKL1",
                                   meaning=NCIT.C82427)
    C8255 = PermissibleValue(text="C8255",
                                 description="Anal Canal Cloacogenic Carcinoma",
                                 meaning=NCIT.C8255)
    C82426 = PermissibleValue(text="C82426",
                                   description="Acute Myeloid Leukemia with inv(3) (q21.3;q26.2) or t(3;3) (q21.3;q26.2); GATA2, MECOM",
                                   meaning=NCIT.C82426)
    C7542 = PermissibleValue(text="C7542",
                                 description="Askin Tumor",
                                 meaning=NCIT.C7542)
    C6860 = PermissibleValue(text="C6860",
                                 description="Primary Cutaneous Anaplastic Large Cell Lymphoma",
                                 meaning=NCIT.C6860)
    C4154 = PermissibleValue(text="C4154",
                                 description="Parathyroid Gland Chief Cell Adenoma",
                                 meaning=NCIT.C4154)
    C4293 = PermissibleValue(text="C4293",
                                 description="Partial Hydatidiform Mole",
                                 meaning=NCIT.C4293)
    C45716 = PermissibleValue(text="C45716",
                                   description="NUT Carcinoma",
                                   meaning=NCIT.C45716)
    C4812 = PermissibleValue(text="C4812",
                                 description="Malignant Odontogenic Neoplasm",
                                 meaning=NCIT.C4812)
    C3802 = PermissibleValue(text="C3802",
                                 description="Amelanotic Melanoma",
                                 meaning=NCIT.C3802)
    C4673 = PermissibleValue(text="C4673",
                                 description="Acute Biphenotypic Leukemia",
                                 meaning=NCIT.C4673)
    C4725 = PermissibleValue(text="C4725",
                                 description="Papillary Craniopharyngioma",
                                 meaning=NCIT.C4725)
    C4737 = PermissibleValue(text="C4737",
                                 description="Enteropathy-Associated T-Cell Lymphoma",
                                 meaning=NCIT.C4737)
    C36077 = PermissibleValue(text="C36077",
                                   description="Hilar Cholangiocarcinoma",
                                   meaning=NCIT.C36077)
    C3749 = PermissibleValue(text="C3749",
                                 description="Alveolar Rhabdomyosarcoma",
                                 meaning=NCIT.C3749)
    C3272 = PermissibleValue(text="C3272",
                                 description="Neurofibroma",
                                 meaning=NCIT.C3272)
    C34448 = PermissibleValue(text="C34448",
                                   description="Carcinosarcoma",
                                   meaning=NCIT.C34448)
    C27096 = PermissibleValue(text="C27096",
                                   description="Liver Embryonal Sarcoma",
                                   meaning=NCIT.C27096)
    C27912 = PermissibleValue(text="C27912",
                                   description="Therapy-Related Myeloid Neoplasm",
                                   meaning=NCIT.C27912)
    C3179 = PermissibleValue(text="C3179",
                                 description="Chronic Neutrophilic Leukemia",
                                 meaning=NCIT.C3179)
    C6914 = PermissibleValue(text="C6914",
                                 description="Hodgkin's Granuloma",
                                 meaning=NCIT.C6914)
    C65181 = PermissibleValue(text="C65181",
                                   description="Non-Invasive Papillary Transitional Cell Carcinoma",
                                   meaning=NCIT.C65181)
    C173820 = PermissibleValue(text="C173820",
                                     description="Ossifying Fibroma",
                                     meaning=NCIT.C173820)
    C157718 = PermissibleValue(text="C157718",
                                     description="Acquired Cystic Disease-Associated Renal Cell Carcinoma",
                                     meaning=NCIT.C157718)
    C129447 = PermissibleValue(text="C129447",
                                     description="Medulloblastoma, Not Otherwise Specified",
                                     meaning=NCIT.C129447)
    C3273 = PermissibleValue(text="C3273",
                                 description="Neurofibromatosis Type 1",
                                 meaning=NCIT.C3273)
    C3059 = PermissibleValue(text="C3059",
                                 description="Glioma",
                                 meaning=NCIT.C3059)
    C82339 = PermissibleValue(text="C82339",
                                   description="Transient Abnormal Myelopoiesis Associated with Down Syndrome",
                                   meaning=NCIT.C82339)
    C7318 = PermissibleValue(text="C7318",
                                 description="Acute Monoblastic and Monocytic Leukemia",
                                 meaning=NCIT.C7318)
    C43223 = PermissibleValue(text="C43223",
                                   description="Myeloid Leukemia Associated with Down Syndrome",
                                   meaning=NCIT.C43223)
    C4326 = PermissibleValue(text="C4326",
                                 description="Anaplastic Oligodendroglioma",
                                 meaning=NCIT.C4326)
    C4240 = PermissibleValue(text="C4240",
                                 description="Melanoma Arising from Blue Nevus",
                                 meaning=NCIT.C4240)
    C40345 = PermissibleValue(text="C40345",
                                   description="Testicular Germ Cell Neoplasia In Situ",
                                   meaning=NCIT.C40345)
    C26749 = PermissibleValue(text="C26749",
                                   description="VIP-Producing Neuroendocrine Tumor",
                                   meaning=NCIT.C26749)
    C3698 = PermissibleValue(text="C3698",
                                 description="Choroid Plexus Papilloma",
                                 meaning=NCIT.C3698)
    C3744 = PermissibleValue(text="C3744",
                                 description="Breast Fibroadenoma",
                                 meaning=NCIT.C3744)
    C3790 = PermissibleValue(text="C3790",
                                 description="Ganglioneuroblastoma",
                                 meaning=NCIT.C3790)
    C3775 = PermissibleValue(text="C3775",
                                 description="Adnexal Carcinoma",
                                 meaning=NCIT.C3775)
    C27502 = PermissibleValue(text="C27502",
                                   description="Extraskeletal Myxoid Chondrosarcoma",
                                   meaning=NCIT.C27502)
    C3164 = PermissibleValue(text="C3164",
                                 description="Acute Basophilic Leukemia",
                                 meaning=NCIT.C3164)
    C66751 = PermissibleValue(text="C66751",
                                   description="Granulosa Cell-Theca Cell Tumor",
                                   meaning=NCIT.C66751)
    C66801 = PermissibleValue(text="C66801",
                                   description="Polar Spongioblastoma",
                                   meaning=NCIT.C66801)
    C66745 = PermissibleValue(text="C66745",
                                   description="Adenocarcinoma with Neuroendocrine Differentiation",
                                   meaning=NCIT.C66745)
    C66777 = PermissibleValue(text="C66777",
                                   description="Choriocarcinoma Combined with Other Germ Cell Elements",
                                   meaning=NCIT.C66777)
    C66759 = PermissibleValue(text="C66759",
                                   description="Giant Cell Sarcoma",
                                   meaning=NCIT.C66759)
    C65163 = PermissibleValue(text="C65163",
                                   description="Papillary Carcinoma In Situ",
                                   meaning=NCIT.C65163)
    C65176 = PermissibleValue(text="C65176",
                                   description="Squamous Cell Carcinoma In Situ with Questionable Stromal Invasion",
                                   meaning=NCIT.C65176)
    C53457 = PermissibleValue(text="C53457",
                                   description="Multiple Osteochondromas",
                                   meaning=NCIT.C53457)
    C95458 = PermissibleValue(text="C95458",
                                   description="Pancreatic Mixed Acinar-Ductal Carcinoma",
                                   meaning=NCIT.C95458)
    C3463 = PermissibleValue(text="C3463",
                                 description="Diffuse Mixed Cell Lymphoma",
                                 meaning=NCIT.C3463)
    C27379 = PermissibleValue(text="C27379",
                                   description="Mucin-Producing Adenocarcinoma",
                                   meaning=NCIT.C27379)
    C27095 = PermissibleValue(text="C27095",
                                   description="Nonpigmented Nevus",
                                   meaning=NCIT.C27095)
    C3405 = PermissibleValue(text="C3405",
                                 description="Thecoma",
                                 meaning=NCIT.C3405)
    C3233 = PermissibleValue(text="C3233",
                                 description="Mesenchymoma",
                                 meaning=NCIT.C3233)
    C12922 = PermissibleValue(text="C12922",
                                   description="Neoplastic Cell",
                                   meaning=NCIT.C12922)
    C6088 = PermissibleValue(text="C6088",
                                 description="Ceruminous Adenoma",
                                 meaning=NCIT.C6088)
    C6040 = PermissibleValue(text="C6040",
                                 description="Poorly Differentiated Thyroid Gland Carcinoma",
                                 meaning=NCIT.C6040)
    C6915 = PermissibleValue(text="C6915",
                                 description="Primary Effusion Lymphoma",
                                 meaning=NCIT.C6915)
    C4049 = PermissibleValue(text="C4049",
                                 description="Anaplastic Ependymoma",
                                 meaning=NCIT.C4049)
    C4883 = PermissibleValue(text="C4883",
                                 description="Malignant Muscle Neoplasm",
                                 meaning=NCIT.C4883)
    C27753 = PermissibleValue(text="C27753",
                                   description="Acute Myeloid Leukemia Not Otherwise Specified",
                                   meaning=NCIT.C27753)
    C43331 = PermissibleValue(text="C43331",
                                   description="Fibrofolliculoma",
                                   meaning=NCIT.C43331)
    C4310 = PermissibleValue(text="C4310",
                                 description="Adenomatoid Odontogenic Tumor",
                                 meaning=NCIT.C4310)
    C4122 = PermissibleValue(text="C4122",
                                 description="Papillary Transitional Cell Carcinoma",
                                 meaning=NCIT.C4122)
    C4156 = PermissibleValue(text="C4156",
                                 description="Water-Clear Cell Adenocarcinoma",
                                 meaning=NCIT.C4156)
    C4202 = PermissibleValue(text="C4202",
                                 description="Adenocarcinoma with Apocrine Metaplasia",
                                 meaning=NCIT.C4202)
    C65164 = PermissibleValue(text="C65164",
                                   description="Non-Invasive Papillary Squamous Cell Carcinoma",
                                   meaning=NCIT.C65164)
    C65175 = PermissibleValue(text="C65175",
                                   description="Non-Keratinizing Small Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C65175)
    C65194 = PermissibleValue(text="C65194",
                                   description="Gastric Parietal Cell Adenocarcinoma",
                                   meaning=NCIT.C65194)
    C3842 = PermissibleValue(text="C3842",
                                 description="Urothelial Papilloma",
                                 meaning=NCIT.C3842)
    C9498 = PermissibleValue(text="C9498",
                                 description="Melanocytoma",
                                 meaning=NCIT.C9498)
    C26956 = PermissibleValue(text="C26956",
                                   description="Hodgkin's Paragranuloma",
                                   meaning=NCIT.C26956)
    C37212 = PermissibleValue(text="C37212",
                                   description="Solid Pseudopapillary Neoplasm of the Pancreas",
                                   meaning=NCIT.C37212)
    C3791 = PermissibleValue(text="C3791",
                                 description="Central Neurocytoma",
                                 meaning=NCIT.C3791)
    C136709 = PermissibleValue(text="C136709",
                                     description="Invasive Lung Mucinous Adenocarcinoma",
                                     meaning=NCIT.C136709)
    C7268 = PermissibleValue(text="C7268",
                                 description="Minimally Invasive Lung Mucinous Adenocarcinoma",
                                 meaning=NCIT.C7268)
    C7600 = PermissibleValue(text="C7600",
                                 description="Acute Myeloid Leukemia with Myelodysplasia-Related Changes",
                                 meaning=NCIT.C7600)
    C8300 = PermissibleValue(text="C8300",
                                 description="Desmoplastic Small Round Cell Tumor",
                                 meaning=NCIT.C8300)
    C7951 = PermissibleValue(text="C7951",
                                 description="Breast Paget Disease with Invasive Ductal Carcinoma",
                                 meaning=NCIT.C7951)
    C8975 = PermissibleValue(text="C8975",
                                 description="Malignant Mixed Mesodermal (Mullerian) Tumor",
                                 meaning=NCIT.C8975)
    C6975 = PermissibleValue(text="C6975",
                                 description="Papillary Renal Cell Carcinoma",
                                 meaning=NCIT.C6975)
    C5669 = PermissibleValue(text="C5669",
                                 description="Pleuropulmonary Blastoma",
                                 meaning=NCIT.C5669)
    C4212 = PermissibleValue(text="C4212",
                                 description="Benign Leydig Cell Tumor",
                                 meaning=NCIT.C4212)
    C4290 = PermissibleValue(text="C4290",
                                 description="Mixed Germ Cell Tumor",
                                 meaning=NCIT.C4290)
    C2947 = PermissibleValue(text="C2947",
                                 description="Chordoma",
                                 meaning=NCIT.C2947)
    C3753 = PermissibleValue(text="C3753",
                                 description="Germinoma",
                                 meaning=NCIT.C3753)
    C2880 = PermissibleValue(text="C2880",
                                 description="Ovarian Sertoli-Leydig Cell Tumor",
                                 meaning=NCIT.C2880)
    C3043 = PermissibleValue(text="C3043",
                                 description="Fibrosarcoma",
                                 meaning=NCIT.C3043)
    C7661 = PermissibleValue(text="C7661",
                                 description="Low Grade Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C7661)
    C7563 = PermissibleValue(text="C7563",
                                 description="Hidradenoma",
                                 meaning=NCIT.C7563)
    C66950 = PermissibleValue(text="C66950",
                                   description="Hepatoid Adenocarcinoma",
                                   meaning=NCIT.C66950)
    C7357 = PermissibleValue(text="C7357",
                                 description="Periosteal Chondrosarcoma",
                                 meaning=NCIT.C7357)
    C7439 = PermissibleValue(text="C7439",
                                 description="Breast Papillary Ductal Carcinoma In Situ with Invasion",
                                 meaning=NCIT.C7439)
    C7018 = PermissibleValue(text="C7018",
                                 description="Nerve Sheath Myxoma",
                                 meaning=NCIT.C7018)
    C5609 = PermissibleValue(text="C5609",
                                 description="Anal Glands Adenocarcinoma",
                                 meaning=NCIT.C5609)
    C5560 = PermissibleValue(text="C5560",
                                 description="Porocarcinoma",
                                 meaning=NCIT.C5560)
    C4302 = PermissibleValue(text="C4302",
                                 description="Periosteal Chondroma",
                                 meaning=NCIT.C4302)
    C4317 = PermissibleValue(text="C4317",
                                 description="Ameloblastic Fibrosarcoma",
                                 meaning=NCIT.C4317)
    C4321 = PermissibleValue(text="C4321",
                                 description="Gemistocytic Astrocytoma",
                                 meaning=NCIT.C4321)
    C4330 = PermissibleValue(text="C4330",
                                 description="Fibrous Meningioma",
                                 meaning=NCIT.C4330)
    C4171 = PermissibleValue(text="C4171",
                                 description="Hidradenoma Papilliferum",
                                 meaning=NCIT.C4171)
    C4251 = PermissibleValue(text="C4251",
                                 description="Fibromyxolipoma",
                                 meaning=NCIT.C4251)
    C4292 = PermissibleValue(text="C4292",
                                 description="Strumal Carcinoid",
                                 meaning=NCIT.C4292)
    C4235 = PermissibleValue(text="C4235",
                                 description="Melanoma Arising in Giant Congenital Nevus",
                                 meaning=NCIT.C4235)
    C4263 = PermissibleValue(text="C4263",
                                 description="Low Grade Endometrioid Stromal Sarcoma",
                                 meaning=NCIT.C4263)
    C4255 = PermissibleValue(text="C4255",
                                 description="Lipoblastomatosis",
                                 meaning=NCIT.C4255)
    C45512 = PermissibleValue(text="C45512",
                                   description="Lung Colloid Adenocarcinoma",
                                   meaning=NCIT.C45512)
    C65153 = PermissibleValue(text="C65153",
                                   description="Malignant Neoplasm, Uncertain Whether Primary or Metastatic",
                                   meaning=NCIT.C65153)
    C3804 = PermissibleValue(text="C3804",
                                 description="Dermal Nevus",
                                 meaning=NCIT.C3804)
    C3681 = PermissibleValue(text="C3681",
                                 description="Granular Cell Carcinoma",
                                 meaning=NCIT.C3681)
    C3680 = PermissibleValue(text="C3680",
                                 description="Cribriform Carcinoma",
                                 meaning=NCIT.C3680)
    C3707 = PermissibleValue(text="C3707",
                                 description="Meningiomatosis",
                                 meaning=NCIT.C3707)
    C3784 = PermissibleValue(text="C3784",
                                 description="Basal Cell Neoplasm",
                                 meaning=NCIT.C3784)
    C27884 = PermissibleValue(text="C27884",
                                   description="Bladder Papillary Urothelial Neoplasm of Low Malignant Potential",
                                   meaning=NCIT.C27884)
    C82423 = PermissibleValue(text="C82423",
                                   description="Acute Myeloid Leukemia with t(6;9) (p23;q34.1); DEK-NUP214",
                                   meaning=NCIT.C82423)
    C6966 = PermissibleValue(text="C6966",
                                 description="Pineocytoma",
                                 meaning=NCIT.C6966)
    C3694 = PermissibleValue(text="C3694",
                                 description="Dysplastic Nevus",
                                 meaning=NCIT.C3694)
    C3750 = PermissibleValue(text="C3750",
                                 description="Alveolar Soft Part Sarcoma",
                                 meaning=NCIT.C3750)
    C3740 = PermissibleValue(text="C3740",
                                 description="Desmoplastic Fibroma",
                                 meaning=NCIT.C3740)
    C27780 = PermissibleValue(text="C27780",
                                   description="Myelodysplastic/Myeloproliferative Neoplasm, Unclassifiable",
                                   meaning=NCIT.C27780)
    C8381 = PermissibleValue(text="C8381",
                                 description="Florid Cemento-Osseous Dysplasia",
                                 meaning=NCIT.C8381)
    C66845 = PermissibleValue(text="C66845",
                                   description="Malignant Peripheral Nerve Sheath Tumor with Perineurial Differentiation",
                                   meaning=NCIT.C66845)
    C67012 = PermissibleValue(text="C67012",
                                   description="Benign Sertoli Cell Tumor",
                                   meaning=NCIT.C67012)
    C8602 = PermissibleValue(text="C8602",
                                 description="Pleomorphic Adenoma",
                                 meaning=NCIT.C8602)
    C7202 = PermissibleValue(text="C7202",
                                 description="Malignant Histiocytosis",
                                 meaning=NCIT.C7202)
    C7165 = PermissibleValue(text="C7165",
                                 description="Grade 1 Nodular Sclerosis Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C7165)
    C6889 = PermissibleValue(text="C6889",
                                 description="Malignant Type B2 Thymoma",
                                 meaning=NCIT.C6889)
    C6905 = PermissibleValue(text="C6905",
                                 description="Cerebellar Liponeurocytoma",
                                 meaning=NCIT.C6905)
    C6886 = PermissibleValue(text="C6886",
                                 description="Malignant Type AB Thymoma",
                                 meaning=NCIT.C6886)
    C4333 = PermissibleValue(text="C4333",
                                 description="Transitional Meningioma",
                                 meaning=NCIT.C4333)
    C4160 = PermissibleValue(text="C4160",
                                 description="Thyroid Gland Microfollicular Adenoma",
                                 meaning=NCIT.C4160)
    C4177 = PermissibleValue(text="C4177",
                                 description="Borderline Serous Cystadenoma",
                                 meaning=NCIT.C4177)
    C4170 = PermissibleValue(text="C4170",
                                 description="Spiradenoma",
                                 meaning=NCIT.C4170)
    C4176 = PermissibleValue(text="C4176",
                                 description="Ceruminous Adenocarcinoma",
                                 meaning=NCIT.C4176)
    C4298 = PermissibleValue(text="C4298",
                                 description="Epithelioid Hemangioma",
                                 meaning=NCIT.C4298)
    C4277 = PermissibleValue(text="C4277",
                                 description="Spindle Cell Synovial Sarcoma",
                                 meaning=NCIT.C4277)
    C4282 = PermissibleValue(text="C4282",
                                 description="Biphasic Mesothelioma",
                                 meaning=NCIT.C4282)
    C4274 = PermissibleValue(text="C4274",
                                 description="Benign Phyllodes Tumor",
                                 meaning=NCIT.C4274)
    C4023 = PermissibleValue(text="C4023",
                                 description="Small Cell Osteosarcoma",
                                 meaning=NCIT.C4023)
    C4068 = PermissibleValue(text="C4068",
                                 description="Trabecular Adenocarcinoma",
                                 meaning=NCIT.C4068)
    C39921 = PermissibleValue(text="C39921",
                                   description="Testicular Spermatocytic Tumor",
                                   meaning=NCIT.C39921)
    C40080 = PermissibleValue(text="C40080",
                                   description="Borderline Ovarian Clear Cell Tumor",
                                   meaning=NCIT.C40080)
    C39920 = PermissibleValue(text="C39920",
                                   description="Testicular Seminoma with High Mitotic Index",
                                   meaning=NCIT.C39920)
    C65192 = PermissibleValue(text="C65192",
                                   description="Tubular Adenocarcinoma",
                                   meaning=NCIT.C65192)
    C3803 = PermissibleValue(text="C3803",
                                 description="Blue Nevus",
                                 meaning=NCIT.C3803)
    C9430 = PermissibleValue(text="C9430",
                                 description="Pigmented Dermatofibrosarcoma Protuberans",
                                 meaning=NCIT.C9430)
    C96830 = PermissibleValue(text="C96830",
                                   description="Calcifying Nested Stromal-Epithelial Tumor of the Liver",
                                   meaning=NCIT.C96830)
    C3765 = PermissibleValue(text="C3765",
                                 description="Multicystic Mesothelioma",
                                 meaning=NCIT.C3765)
    C3778 = PermissibleValue(text="C3778",
                                 description="Serous Cystadenocarcinoma",
                                 meaning=NCIT.C3778)
    C27094 = PermissibleValue(text="C27094",
                                   description="Cylindroma",
                                   meaning=NCIT.C27094)
    C4131 = PermissibleValue(text="C4131",
                                 description="Fibrolamellar Carcinoma",
                                 meaning=NCIT.C4131)
    C4001 = PermissibleValue(text="C4001",
                                 description="Breast Inflammatory Carcinoma",
                                 meaning=NCIT.C4001)
    C9477 = PermissibleValue(text="C9477",
                                 description="Anaplastic Astrocytoma",
                                 meaning=NCIT.C9477)
    C3308 = PermissibleValue(text="C3308",
                                 description="Paraganglioma",
                                 meaning=NCIT.C3308)
    C27790 = PermissibleValue(text="C27790",
                                   description="Penile Carcinoma In Situ",
                                   meaning=NCIT.C27790)
    C67171 = PermissibleValue(text="C67171",
                                   description="Nodular Sclerosis Classic Hodgkin Lymphoma, Cellular Phase",
                                   meaning=NCIT.C67171)
    C8969 = PermissibleValue(text="C8969",
                                 description="Parosteal Osteosarcoma",
                                 meaning=NCIT.C8969)
    C6780 = PermissibleValue(text="C6780",
                                 description="Pituitary Gland Acidophil Adenoma",
                                 meaning=NCIT.C6780)
    C4159 = PermissibleValue(text="C4159",
                                 description="Lipoadenoma",
                                 meaning=NCIT.C4159)
    C4294 = PermissibleValue(text="C4294",
                                 description="Benign Mesonephroma",
                                 meaning=NCIT.C4294)
    C4268 = PermissibleValue(text="C4268",
                                 description="Malignant Mesenchymoma",
                                 meaning=NCIT.C4268)
    C40392 = PermissibleValue(text="C40392",
                                   description="Myoepithelial Tumor",
                                   meaning=NCIT.C40392)
    C3901 = PermissibleValue(text="C3901",
                                 description="Compound Nevus",
                                 meaning=NCIT.C3901)
    C6454 = PermissibleValue(text="C6454",
                                 description="Thymoma Type A",
                                 meaning=NCIT.C6454)
    C4754 = PermissibleValue(text="C4754",
                                 description="Spindle Cell Hemangioma",
                                 meaning=NCIT.C4754)
    C3801 = PermissibleValue(text="C3801",
                                 description="Hemangioblastoma",
                                 meaning=NCIT.C3801)
    C3777 = PermissibleValue(text="C3777",
                                 description="Papillary Cystadenocarcinoma",
                                 meaning=NCIT.C3777)
    C27729 = PermissibleValue(text="C27729",
                                   description="Thyroid Gland Well-Differentiated Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C27729)
    C27949 = PermissibleValue(text="C27949",
                                   description="Metaplastic Carcinoma",
                                   meaning=NCIT.C27949)
    C3084 = PermissibleValue(text="C3084",
                                 description="Hemangioendothelioma",
                                 meaning=NCIT.C3084)
    C3157 = PermissibleValue(text="C3157",
                                 description="Leiomyoma",
                                 meaning=NCIT.C3157)
    C8991 = PermissibleValue(text="C8991",
                                 description="Malignant Mastocytosis",
                                 meaning=NCIT.C8991)
    C7526 = PermissibleValue(text="C7526",
                                 description="Papillary Intralymphatic Angioendothelioma",
                                 meaning=NCIT.C7526)
    C7166 = PermissibleValue(text="C7166",
                                 description="Grade 2 Nodular Sclerosis Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C7166)
    C43372 = PermissibleValue(text="C43372",
                                   description="Lentigo Maligna",
                                   meaning=NCIT.C43372)
    C4322 = PermissibleValue(text="C4322",
                                 description="Fibrillary Astrocytoma",
                                 meaning=NCIT.C4322)
    C4161 = PermissibleValue(text="C4161",
                                 description="Thyroid Gland Macrofollicular Adenoma",
                                 meaning=NCIT.C4161)
    C4192 = PermissibleValue(text="C4192",
                                 description="Nipple Adenoma",
                                 meaning=NCIT.C4192)
    C4275 = PermissibleValue(text="C4275",
                                 description="Malignant Phyllodes Tumor",
                                 meaning=NCIT.C4275)
    C65188 = PermissibleValue(text="C65188",
                                   description="Malignant Gastrinoma",
                                   meaning=NCIT.C65188)
    C4915 = PermissibleValue(text="C4915",
                                 description="Embryonal Tumor with Multilayered Rosettes, C19MC-Altered",
                                 meaning=NCIT.C4915)
    C2972 = PermissibleValue(text="C2972",
                                 description="Cystadenoma",
                                 meaning=NCIT.C2972)
    C4716 = PermissibleValue(text="C4716",
                                 description="Ectomesenchymoma",
                                 meaning=NCIT.C4716)
    C9308 = PermissibleValue(text="C9308",
                                 description="Lymphoproliferative Disorder",
                                 meaning=NCIT.C9308)
    C37257 = PermissibleValue(text="C37257",
                                   description="Desmoplastic Melanoma",
                                   meaning=NCIT.C37257)
    C3754 = PermissibleValue(text="C3754",
                                 description="Gonadoblastoma",
                                 meaning=NCIT.C3754)
    C3774 = PermissibleValue(text="C3774",
                                 description="Signet Ring Cell Carcinoma",
                                 meaning=NCIT.C3774)
    C3286 = PermissibleValue(text="C3286",
                                 description="Odontogenic Neoplasm",
                                 meaning=NCIT.C3286)
    C3474 = PermissibleValue(text="C3474",
                                 description="Granular Cell Tumor",
                                 meaning=NCIT.C3474)
    C27091 = PermissibleValue(text="C27091",
                                   description="Malignant Spindle Cell Neoplasm",
                                   meaning=NCIT.C27091)
    C27080 = PermissibleValue(text="C27080",
                                   description="Refractory Anemia with Excess Blasts in Transformation",
                                   meaning=NCIT.C27080)
    C9152 = PermissibleValue(text="C9152",
                                 description="Low-CSD Melanoma",
                                 meaning=NCIT.C9152)
    C9119 = PermissibleValue(text="C9119",
                                 description="Breast Medullary Carcinoma",
                                 meaning=NCIT.C9119)
    C6569 = PermissibleValue(text="C6569",
                                 description="Congenital Mesoblastic Nephroma",
                                 meaning=NCIT.C6569)
    C27720 = PermissibleValue(text="C27720",
                                   description="Pancreatic Neuroendocrine Tumor",
                                   meaning=NCIT.C27720)
    C2996 = PermissibleValue(text="C2996",
                                 description="Dysgerminoma",
                                 meaning=NCIT.C2996)
    C7985 = PermissibleValue(text="C7985",
                                 description="Epithelioid Mesothelioma",
                                 meaning=NCIT.C7985)
    C9151 = PermissibleValue(text="C9151",
                                 description="Lentigo Maligna Melanoma",
                                 meaning=NCIT.C9151)
    C4314 = PermissibleValue(text="C4314",
                                 description="Odontogenic Fibroma",
                                 meaning=NCIT.C4314)
    C4162 = PermissibleValue(text="C4162",
                                 description="Juxtaglomerular Cell Tumor",
                                 meaning=NCIT.C4162)
    C4115 = PermissibleValue(text="C4115",
                                 description="Transitional Cell Papilloma",
                                 meaning=NCIT.C4115)
    C4002 = PermissibleValue(text="C4002",
                                 description="Extraosseous Plasmacytoma",
                                 meaning=NCIT.C4002)
    C54301 = PermissibleValue(text="C54301",
                                   description="Calcifying Epithelial Odontogenic Tumor",
                                   meaning=NCIT.C54301)
    C9281 = PermissibleValue(text="C9281",
                                 description="Follicular Dendritic Cell Sarcoma",
                                 meaning=NCIT.C9281)
    C3756 = PermissibleValue(text="C3756",
                                 description="Mixed Embryonal Carcinoma and Teratoma",
                                 meaning=NCIT.C3756)
    C3742 = PermissibleValue(text="C3742",
                                 description="Myofibromatosis",
                                 meaning=NCIT.C3742)
    C3796 = PermissibleValue(text="C3796",
                                 description="Gliosarcoma",
                                 meaning=NCIT.C3796)
    C37194 = PermissibleValue(text="C37194",
                                   description="Anaplastic Large Cell Lymphoma, ALK-Negative",
                                   meaning=NCIT.C37194)
    C3483 = PermissibleValue(text="C3483",
                                 description="Chronic Leukemia",
                                 meaning=NCIT.C3483)
    C27388 = PermissibleValue(text="C27388",
                                   description="Scirrhous Hepatocellular Carcinoma",
                                   meaning=NCIT.C27388)
    C27781 = PermissibleValue(text="C27781",
                                   description="Myxoid Liposarcoma",
                                   meaning=NCIT.C27781)
    C2856 = PermissibleValue(text="C2856",
                                 description="Pituitary Gland Basophil Adenoma",
                                 meaning=NCIT.C2856)
    C4822 = PermissibleValue(text="C4822",
                                 description="Malignant Glioma",
                                 meaning=NCIT.C4822)
    C3829 = PermissibleValue(text="C3829",
                                 description="Benign Synovial Neoplasm",
                                 meaning=NCIT.C3829)
    C7644 = PermissibleValue(text="C7644",
                                 description="Adamantinoma",
                                 meaning=NCIT.C7644)
    C6727 = PermissibleValue(text="C6727",
                                 description="Neurofibromatosis",
                                 meaning=NCIT.C6727)
    C6645 = PermissibleValue(text="C6645",
                                 description="Infantile Hemangioma",
                                 meaning=NCIT.C6645)
    C6938 = PermissibleValue(text="C6938",
                                 description="Sweat Gland Carcinoma",
                                 meaning=NCIT.C6938)
    C5592 = PermissibleValue(text="C5592",
                                 description="Chordoid Glioma of the Third Ventricle",
                                 meaning=NCIT.C5592)
    C4200 = PermissibleValue(text="C4200",
                                 description="Adenocarcinoma with Squamous Metaplasia",
                                 meaning=NCIT.C4200)
    C4102 = PermissibleValue(text="C4102",
                                 description="Papillary Squamous Cell Carcinoma",
                                 meaning=NCIT.C4102)
    C4286 = PermissibleValue(text="C4286",
                                 description="Immature Teratoma",
                                 meaning=NCIT.C4286)
    C4214 = PermissibleValue(text="C4214",
                                 description="Ovarian Hilus Cell Tumor",
                                 meaning=NCIT.C4214)
    C4051 = PermissibleValue(text="C4051",
                                 description="Anaplastic (Malignant) Meningioma",
                                 meaning=NCIT.C4051)
    C54287 = PermissibleValue(text="C54287",
                                   description="Sinonasal Non-Keratinizing Squamous Cell Carcinoma",
                                   meaning=NCIT.C54287)
    C53999 = PermissibleValue(text="C53999",
                                   description="Malignant Gastrointestinal Stromal Tumor",
                                   meaning=NCIT.C53999)
    C3714 = PermissibleValue(text="C3714",
                                 description="Epithelioid Sarcoma",
                                 meaning=NCIT.C3714)
    C3732 = PermissibleValue(text="C3732",
                                 description="Pulmonary Blastoma",
                                 meaning=NCIT.C3732)
    C3764 = PermissibleValue(text="C3764",
                                 description="Adenomatous Polyp",
                                 meaning=NCIT.C3764)
    C9306 = PermissibleValue(text="C9306",
                                 description="Soft Tissue Sarcoma",
                                 meaning=NCIT.C9306)
    C3329 = PermissibleValue(text="C3329",
                                 description="Pituitary Gland Adenoma",
                                 meaning=NCIT.C3329)
    C8459 = PermissibleValue(text="C8459",
                                 description="Hepatosplenic T-Cell Lymphoma",
                                 meaning=NCIT.C8459)
    C4246 = PermissibleValue(text="C4246",
                                 description="Atypical Fibroxanthoma",
                                 meaning=NCIT.C4246)
    C4047 = PermissibleValue(text="C4047",
                                 description="Pilocytic Astrocytoma",
                                 meaning=NCIT.C4047)
    C6561 = PermissibleValue(text="C6561",
                                 description="Epithelioid Malignant Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C6561)
    C47857 = PermissibleValue(text="C47857",
                                   description="Breast Paget Disease",
                                   meaning=NCIT.C47857)
    C9282 = PermissibleValue(text="C9282",
                                 description="Interdigitating Dendritic Cell Sarcoma",
                                 meaning=NCIT.C9282)
    C3642 = PermissibleValue(text="C3642",
                                 description="Grade III Prostatic Intraepithelial Neoplasia",
                                 meaning=NCIT.C3642)
    C3725 = PermissibleValue(text="C3725",
                                 description="Lymphangioleiomyomatosis",
                                 meaning=NCIT.C3725)
    C3710 = PermissibleValue(text="C3710",
                                 description="Ameloblastic Fibro-Odontoma",
                                 meaning=NCIT.C3710)
    C3797 = PermissibleValue(text="C3797",
                                 description="Plexiform Neurofibroma",
                                 meaning=NCIT.C3797)
    C27349 = PermissibleValue(text="C27349",
                                   description="Histiocytic Sarcoma",
                                   meaning=NCIT.C27349)
    C27893 = PermissibleValue(text="C27893",
                                   description="Sarcomatoid Renal Cell Carcinoma",
                                   meaning=NCIT.C27893)
    C3061 = PermissibleValue(text="C3061",
                                 description="Jugulotympanic Paraganglioma",
                                 meaning=NCIT.C3061)
    C126598 = PermissibleValue(text="C126598",
                                     description="Thyroid Gland Noninvasive Follicular Neoplasm with Papillary-Like Nuclear Features",
                                     meaning=NCIT.C126598)
    C9309 = PermissibleValue(text="C9309",
                                 description="Seminoma",
                                 meaning=NCIT.C9309)
    C7580 = PermissibleValue(text="C7580",
                                 description="Skin Appendage Adenoma",
                                 meaning=NCIT.C7580)
    C7596 = PermissibleValue(text="C7596",
                                 description="Malignant Myoepithelioma",
                                 meaning=NCIT.C7596)
    C8422 = PermissibleValue(text="C8422",
                                 description="Cemento-Ossifying Fibroma",
                                 meaning=NCIT.C8422)
    C4336 = PermissibleValue(text="C4336",
                                 description="Malignant Granular Cell Tumor",
                                 meaning=NCIT.C4336)
    C4186 = PermissibleValue(text="C4186",
                                 description="Borderline Papillary Mucinous Cystadenoma",
                                 meaning=NCIT.C4186)
    C4244 = PermissibleValue(text="C4244",
                                 description="Infantile Fibrosarcoma",
                                 meaning=NCIT.C4244)
    C4036 = PermissibleValue(text="C4036",
                                 description="Myelodysplastic Syndrome with Ring Sideroblasts",
                                 meaning=NCIT.C4036)
    C6535 = PermissibleValue(text="C6535",
                                 description="Malignant Tenosynovial Giant Cell Tumor",
                                 meaning=NCIT.C6535)
    C62571 = PermissibleValue(text="C62571",
                                   description="Bowen Disease of the Skin",
                                   meaning=NCIT.C62571)
    C2922 = PermissibleValue(text="C2922",
                                 description="Skin Basosquamous Cell Carcinoma",
                                 meaning=NCIT.C2922)
    C9474 = PermissibleValue(text="C9474",
                                 description="Adenosarcoma",
                                 meaning=NCIT.C9474)
    C95598 = PermissibleValue(text="C95598",
                                   description="Pancreatic Insulinoma",
                                   meaning=NCIT.C95598)
    C65173 = PermissibleValue(text="C65173",
                                   description="Non-Keratinizing Large Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C65173)
    C95915 = PermissibleValue(text="C95915",
                                   description="Ampullary Noninvasive Pancreatobiliary Papillary Neoplasm with High Grade Dysplasia",
                                   meaning=NCIT.C95915)
    C7634 = PermissibleValue(text="C7634",
                                 description="Solitary Fibrous Tumor",
                                 meaning=NCIT.C7634)
    C7467 = PermissibleValue(text="C7467",
                                 description="Pure Erythroid Leukemia",
                                 meaning=NCIT.C7467)
    C7173 = PermissibleValue(text="C7173",
                                 description="Diffuse Astrocytoma",
                                 meaning=NCIT.C7173)
    C4020 = PermissibleValue(text="C4020",
                                 description="Fibroblastic Osteosarcoma",
                                 meaning=NCIT.C4020)
    C3771 = PermissibleValue(text="C3771",
                                 description="Breast Lobular Carcinoma",
                                 meaning=NCIT.C3771)
    C3799 = PermissibleValue(text="C3799",
                                 description="Angiofibroma",
                                 meaning=NCIT.C3799)
    C3294 = PermissibleValue(text="C3294",
                                 description="Osteoblastoma",
                                 meaning=NCIT.C3294)
    C7678 = PermissibleValue(text="C7678",
                                 description="Adenocarcinoma In Situ in Adenomatous Polyp",
                                 meaning=NCIT.C7678)
    C4436 = PermissibleValue(text="C4436",
                                 description="Cholangiocarcinoma",
                                 meaning=NCIT.C4436)
    C4536 = PermissibleValue(text="C4536",
                                 description="Pituitary Gland Carcinoma",
                                 meaning=NCIT.C4536)
    C3328 = PermissibleValue(text="C3328",
                                 description="Pineal Region Neoplasm",
                                 meaning=NCIT.C3328)
    C8335 = PermissibleValue(text="C8335",
                                 description="Low Grade Squamous Intraepithelial Neoplasia",
                                 meaning=NCIT.C8335)
    C4213 = PermissibleValue(text="C4213",
                                 description="Malignant Leydig Cell Tumor",
                                 meaning=NCIT.C4213)
    C4683 = PermissibleValue(text="C4683",
                                 description="Dermatofibrosarcoma Protuberans",
                                 meaning=NCIT.C4683)
    C9287 = PermissibleValue(text="C9287",
                                 description="Acute Myeloid Leukemia with inv(16)(p13.1q22) or t(16;16)(p13.1;q22); CBFB-MYH11",
                                 meaning=NCIT.C9287)
    C2882 = PermissibleValue(text="C2882",
                                 description="Arteriovenous Malformation/Hemangioma",
                                 meaning=NCIT.C2882)
    C3192 = PermissibleValue(text="C3192",
                                 description="Lipoma",
                                 meaning=NCIT.C3192)
    C80280 = PermissibleValue(text="C80280",
                                   description="Diffuse Large B-Cell Lymphoma, Not Otherwise Specified",
                                   meaning=NCIT.C80280)
    C66850 = PermissibleValue(text="C66850",
                                   description="Follicular Variant Thyroid Gland Papillary Carcinoma, Encapsulated Subtype with Invasion",
                                   meaning=NCIT.C66850)
    C4329 = PermissibleValue(text="C4329",
                                 description="Meningothelial Meningioma",
                                 meaning=NCIT.C4329)
    C4105 = PermissibleValue(text="C4105",
                                 description="Keratinizing Squamous Cell Carcinoma",
                                 meaning=NCIT.C4105)
    C46105 = PermissibleValue(text="C46105",
                                   description="Thyroid Gland Spindle Cell Tumor with Thymus-Like Differentiation",
                                   meaning=NCIT.C46105)
    C6929 = PermissibleValue(text="C6929",
                                 description="Malignant Ovarian Thecoma",
                                 meaning=NCIT.C6929)
    C4456 = PermissibleValue(text="C4456",
                                 description="Malignant Mesothelioma",
                                 meaning=NCIT.C4456)
    C4195 = PermissibleValue(text="C4195",
                                 description="Breast Ductal Carcinoma In Situ and Lobular Carcinoma In Situ",
                                 meaning=NCIT.C4195)
    C5139 = PermissibleValue(text="C5139",
                                 description="Breast Micropapillary Ductal Carcinoma In Situ",
                                 meaning=NCIT.C5139)
    C3158 = PermissibleValue(text="C3158",
                                 description="Leiomyosarcoma",
                                 meaning=NCIT.C3158)
    C3411 = PermissibleValue(text="C3411",
                                 description="Thymoma",
                                 meaning=NCIT.C3411)
    C3345 = PermissibleValue(text="C3345",
                                 description="Pseudomyxoma Peritonei",
                                 meaning=NCIT.C3345)
    C3379 = PermissibleValue(text="C3379",
                                 description="Somatostatin-Producing Neuroendocrine Tumor",
                                 meaning=NCIT.C3379)
    C3110 = PermissibleValue(text="C3110",
                                 description="Hydatidiform Mole",
                                 meaning=NCIT.C3110)
    C3202 = PermissibleValue(text="C3202",
                                 description="Ovarian Stromal Luteoma",
                                 meaning=NCIT.C3202)
    C43326 = PermissibleValue(text="C43326",
                                   description="Trichilemmal Carcinoma",
                                   meaning=NCIT.C43326)
    C4127 = PermissibleValue(text="C4127",
                                 description="Diffuse Type Adenocarcinoma",
                                 meaning=NCIT.C4127)
    C4117 = PermissibleValue(text="C4117",
                                 description="Sinonasal Papilloma",
                                 meaning=NCIT.C4117)
    C4072 = PermissibleValue(text="C4072",
                                 description="Mesonephric Adenocarcinoma",
                                 meaning=NCIT.C4072)
    C2945 = PermissibleValue(text="C2945",
                                 description="Chondroblastoma",
                                 meaning=NCIT.C2945)
    C46106 = PermissibleValue(text="C46106",
                                   description="Intrathyroid Thymic Carcinoma",
                                   meaning=NCIT.C46106)
    C3759 = PermissibleValue(text="C3759",
                                 description="Oncocytic Adenoma",
                                 meaning=NCIT.C3759)
    C3783 = PermissibleValue(text="C3783",
                                 description="Serous Cystadenoma",
                                 meaning=NCIT.C3783)
    C7569 = PermissibleValue(text="C7569",
                                 description="Thymic Carcinoma",
                                 meaning=NCIT.C7569)
    C8973 = PermissibleValue(text="C8973",
                                 description="Endometrioid Stromal Sarcoma",
                                 meaning=NCIT.C8973)
    C4438 = PermissibleValue(text="C4438",
                                 description="Liver Angiosarcoma",
                                 meaning=NCIT.C4438)
    C40310 = PermissibleValue(text="C40310",
                                   description="Sebaceous Carcinoma",
                                   meaning=NCIT.C40310)
    C2930 = PermissibleValue(text="C2930",
                                 description="Transitional Cell Carcinoma",
                                 meaning=NCIT.C2930)
    C3745 = PermissibleValue(text="C3745",
                                 description="Clear Cell Sarcoma of Soft Tissue",
                                 meaning=NCIT.C3745)
    C7581 = PermissibleValue(text="C7581",
                                 description="Microcystic Adnexal Carcinoma",
                                 meaning=NCIT.C7581)
    C7999 = PermissibleValue(text="C7999",
                                 description="Malignant Type A Thymoma",
                                 meaning=NCIT.C7999)
    C5726 = PermissibleValue(text="C5726",
                                 description="Pancreatic Intraductal Papillary-Mucinous Neoplasm with an Associated Invasive Carcinoma",
                                 meaning=NCIT.C5726)
    C4197 = PermissibleValue(text="C4197",
                                 description="Acinar Cell Neoplasm",
                                 meaning=NCIT.C4197)
    C4126 = PermissibleValue(text="C4126",
                                 description="Intestinal-Type Adenocarcinoma",
                                 meaning=NCIT.C4126)
    C4150 = PermissibleValue(text="C4150",
                                 description="Basophilic Adenocarcinoma",
                                 meaning=NCIT.C4150)
    C3788 = PermissibleValue(text="C3788",
                                 description="Ganglioglioma",
                                 meaning=NCIT.C3788)
    C173740 = PermissibleValue(text="C173740",
                                     description="Ameloblastic Fibroodontosarcoma",
                                     meaning=NCIT.C173740)
    C2852 = PermissibleValue(text="C2852",
                                 description="Adenocarcinoma",
                                 meaning=NCIT.C2852)
    C8380 = PermissibleValue(text="C8380",
                                 description="Undifferentiated Pleomorphic Sarcoma with Osteoclast-Like Giant Cells",
                                 meaning=NCIT.C8380)
    C3776 = PermissibleValue(text="C3776",
                                 description="Mucinous Cystadenocarcinoma",
                                 meaning=NCIT.C3776)
    C3747 = PermissibleValue(text="C3747",
                                 description="Angioleiomyoma",
                                 meaning=NCIT.C3747)
    C3183 = PermissibleValue(text="C3183",
                                 description="T Acute Lymphoblastic Leukemia",
                                 meaning=NCIT.C3183)
    C60781 = PermissibleValue(text="C60781",
                                   description="Astrocytoma",
                                   meaning=NCIT.C60781)
    C4017 = PermissibleValue(text="C4017",
                                 description="Breast Ductal Carcinoma",
                                 meaning=NCIT.C4017)
    C6432 = PermissibleValue(text="C6432",
                                 description="Multiple Endocrine Neoplasia",
                                 meaning=NCIT.C6432)
    C2942 = PermissibleValue(text="C2942",
                                 description="Bile Duct Adenoma",
                                 meaning=NCIT.C2942)
    C4663 = PermissibleValue(text="C4663",
                                 description="Splenic Marginal Zone Lymphoma",
                                 meaning=NCIT.C4663)
    C3752 = PermissibleValue(text="C3752",
                                 description="Embryonal Carcinoma",
                                 meaning=NCIT.C3752)
    C3403 = PermissibleValue(text="C3403",
                                 description="Teratoma",
                                 meaning=NCIT.C3403)
    C6939 = PermissibleValue(text="C6939",
                                 description="Breast Ductal Carcinoma In Situ and Invasive Lobular Carcinoma",
                                 meaning=NCIT.C6939)
    C4172 = PermissibleValue(text="C4172",
                                 description="Syringocystadenoma Papilliferum",
                                 meaning=NCIT.C4172)
    C38458 = PermissibleValue(text="C38458",
                                   description="Traditional Serrated Adenoma",
                                   meaning=NCIT.C38458)
    C9348 = PermissibleValue(text="C9348",
                                 description="Mast Cell Sarcoma",
                                 meaning=NCIT.C9348)
    C3769 = PermissibleValue(text="C3769",
                                 description="Endometrioid Adenocarcinoma",
                                 meaning=NCIT.C3769)
    C3868 = PermissibleValue(text="C3868",
                                 description="Gastrointestinal Stromal Tumor",
                                 meaning=NCIT.C3868)
    C66760 = PermissibleValue(text="C66760",
                                   description="Fibromyxoid Tumor",
                                   meaning=NCIT.C66760)
    C4164 = PermissibleValue(text="C4164",
                                 description="Pigmented Adrenal Cortex Adenoma",
                                 meaning=NCIT.C4164)
    C4106 = PermissibleValue(text="C4106",
                                 description="Pseudoglandular Squamous Cell Carcinoma",
                                 meaning=NCIT.C4106)
    C4216 = PermissibleValue(text="C4216",
                                 description="Sympathetic Paraganglioma",
                                 meaning=NCIT.C4216)
    C4289 = PermissibleValue(text="C4289",
                                 description="Teratoma with Somatic-Type Malignancy",
                                 meaning=NCIT.C4289)
    C4021 = PermissibleValue(text="C4021",
                                 description="Chondroblastic Osteosarcoma",
                                 meaning=NCIT.C4021)
    C54300 = PermissibleValue(text="C54300",
                                   description="Clear Cell Odontogenic Carcinoma",
                                   meaning=NCIT.C54300)
    C4956 = PermissibleValue(text="C4956",
                                 description="Desmoplastic/Nodular Medulloblastoma",
                                 meaning=NCIT.C4956)
    C2854 = PermissibleValue(text="C2854",
                                 description="Warthin Tumor",
                                 meaning=NCIT.C2854)
    C9003 = PermissibleValue(text="C9003",
                                 description="Adrenal Cortex Adenoma",
                                 meaning=NCIT.C9003)
    C3863 = PermissibleValue(text="C3863",
                                 description="Breast Intraductal Papilloma",
                                 meaning=NCIT.C3863)
    C9459 = PermissibleValue(text="C9459",
                                 description="Borderline Ovarian Brenner Tumor/Atypical Proliferative Ovarian Brenner Tumor",
                                 meaning=NCIT.C9459)
    C9341 = PermissibleValue(text="C9341",
                                 description="Peripheral Primitive Neuroectodermal Tumor",
                                 meaning=NCIT.C9341)
    C3467 = PermissibleValue(text="C3467",
                                 description="Primary Cutaneous T-Cell Non-Hodgkin Lymphoma",
                                 meaning=NCIT.C3467)
    C95406 = PermissibleValue(text="C95406",
                                   description="Digestive System Mixed Adenoneuroendocrine Carcinoma",
                                   meaning=NCIT.C95406)
    C3724 = PermissibleValue(text="C3724",
                                 description="Cystic Hygroma",
                                 meaning=NCIT.C3724)
    C3194 = PermissibleValue(text="C3194",
                                 description="Liposarcoma",
                                 meaning=NCIT.C3194)
    C2928 = PermissibleValue(text="C2928",
                                 description="Scirrhous Adenocarcinoma",
                                 meaning=NCIT.C2928)
    C3794 = PermissibleValue(text="C3794",
                                 description="Sex Cord-Stromal Tumor",
                                 meaning=NCIT.C3794)
    C3180 = PermissibleValue(text="C3180",
                                 description="Plasma Cell Leukemia",
                                 meaning=NCIT.C3180)
    C8559 = PermissibleValue(text="C8559",
                                 description="Malignant Paraganglioma",
                                 meaning=NCIT.C8559)
    C9011 = PermissibleValue(text="C9011",
                                 description="Dermoid Cyst",
                                 meaning=NCIT.C9011)
    C4304 = PermissibleValue(text="C4304",
                                 description="Malignancy in Giant Cell Tumor of Bone",
                                 meaning=NCIT.C4304)
    C4196 = PermissibleValue(text="C4196",
                                 description="Acinar Cell Adenoma",
                                 meaning=NCIT.C4196)
    C4107 = PermissibleValue(text="C4107",
                                 description="Nasopharyngeal-Type Undifferentiated Carcinoma",
                                 meaning=NCIT.C4107)
    C4295 = PermissibleValue(text="C4295",
                                 description="Mesonephric Neoplasm",
                                 meaning=NCIT.C4295)
    C54323 = PermissibleValue(text="C54323",
                                   description="Dentinogenic Ghost Cell Tumor",
                                   meaning=NCIT.C54323)
    C2932 = PermissibleValue(text="C2932",
                                 description="Carotid Body Paraganglioma",
                                 meaning=NCIT.C2932)
    C27084 = PermissibleValue(text="C27084",
                                   description="Spindle Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C27084)
    C3342 = PermissibleValue(text="C3342",
                                 description="Lactotroph Adenoma",
                                 meaning=NCIT.C3342)
    C4665 = PermissibleValue(text="C4665",
                                 description="Plasma Cell Neoplasm",
                                 meaning=NCIT.C4665)
    C9182 = PermissibleValue(text="C9182",
                                 description="Desmoid Fibromatosis",
                                 meaning=NCIT.C9182)
    C4183 = PermissibleValue(text="C4183",
                                 description="Borderline Papillary Serous Cystadenoma",
                                 meaning=NCIT.C4183)
    C3808 = PermissibleValue(text="C3808",
                                 description="Rhabdoid Tumor",
                                 meaning=NCIT.C3808)
    C3234 = PermissibleValue(text="C3234",
                                 description="Mesothelioma",
                                 meaning=NCIT.C3234)
    C3050 = PermissibleValue(text="C3050",
                                 description="Gastrin-Producing Neuroendocrine Tumor",
                                 meaning=NCIT.C3050)
    C7676 = PermissibleValue(text="C7676",
                                 description="Adenocarcinoma in Adenomatous Polyp",
                                 meaning=NCIT.C7676)
    C8460 = PermissibleValue(text="C8460",
                                 description="Acute Myeloid Leukemia with Minimal Differentiation",
                                 meaning=NCIT.C8460)
    C7541 = PermissibleValue(text="C7541",
                                 description="Retinoblastoma",
                                 meaning=NCIT.C7541)
    C4264 = PermissibleValue(text="C4264",
                                 description="Clear Cell Sarcoma of the Kidney",
                                 meaning=NCIT.C4264)
    C3249 = PermissibleValue(text="C3249",
                                 description="Acute Myeloid Leukemia without Maturation",
                                 meaning=NCIT.C3249)
    C4218 = PermissibleValue(text="C4218",
                                 description="Aorticopulmonary Paraganglioma",
                                 meaning=NCIT.C4218)
    C4727 = PermissibleValue(text="C4727",
                                 description="Post-Transplant Lymphoproliferative Disorder",
                                 meaning=NCIT.C4727)
    C72074 = PermissibleValue(text="C72074",
                                   description="Atypical Carcinoid Tumor",
                                   meaning=NCIT.C72074)
    C27539 = PermissibleValue(text="C27539",
                                   description="Skin Infiltrating Basal Cell Carcinoma",
                                   meaning=NCIT.C27539)
    C3502 = PermissibleValue(text="C3502",
                                 description="Thyroid Gland Follicular Adenoma",
                                 meaning=NCIT.C3502)
    C3795 = PermissibleValue(text="C3795",
                                 description="Subependymoma",
                                 meaning=NCIT.C3795)
    C3758 = PermissibleValue(text="C3758",
                                 description="Hepatocellular Adenoma",
                                 meaning=NCIT.C3758)
    C27132 = PermissibleValue(text="C27132",
                                   description="Trichoblastoma",
                                   meaning=NCIT.C27132)
    C3402 = PermissibleValue(text="C3402",
                                 description="Tenosynovial Giant Cell Tumor",
                                 meaning=NCIT.C3402)
    C7270 = PermissibleValue(text="C7270",
                                 description="Mixed Mucinous and Non-Mucinous Bronchioloalveolar Carcinoma",
                                 meaning=NCIT.C7270)
    C4118 = PermissibleValue(text="C4118",
                                 description="Inverted Transitional Cell Papilloma",
                                 meaning=NCIT.C4118)
    C45655 = PermissibleValue(text="C45655",
                                   description="Sarcomatoid Mesothelioma",
                                   meaning=NCIT.C45655)
    C3250 = PermissibleValue(text="C3250",
                                 description="Acute Myeloid Leukemia with Maturation",
                                 meaning=NCIT.C3250)
    C7368 = PermissibleValue(text="C7368",
                                 description="Pilomatricoma",
                                 meaning=NCIT.C7368)
    C3828 = PermissibleValue(text="C3828",
                                 description="Combined Hepatocellular Carcinoma and Cholangiocarcinoma",
                                 meaning=NCIT.C3828)
    C3702 = PermissibleValue(text="C3702",
                                 description="Hibernoma",
                                 meaning=NCIT.C3702)
    C3205 = PermissibleValue(text="C3205",
                                 description="Lymphangiosarcoma",
                                 meaning=NCIT.C3205)
    C4147 = PermissibleValue(text="C4147",
                                 description="Pituitary Gland Acidophil Carcinoma",
                                 meaning=NCIT.C4147)
    C27253 = PermissibleValue(text="C27253",
                                   description="Metanephric Adenoma",
                                   meaning=NCIT.C27253)
    C3519 = PermissibleValue(text="C3519",
                                 description="Atypical Chronic Myeloid Leukemia, BCR-ABL1 Negative",
                                 meaning=NCIT.C3519)
    C4143 = PermissibleValue(text="C4143",
                                 description="Tubulovillous Adenoma",
                                 meaning=NCIT.C4143)
    C4257 = PermissibleValue(text="C4257",
                                 description="Bizarre Leiomyoma",
                                 meaning=NCIT.C4257)
    C3772 = PermissibleValue(text="C3772",
                                 description="Mucoepidermoid Carcinoma",
                                 meaning=NCIT.C3772)
    C4220 = PermissibleValue(text="C4220",
                                 description="Malignant Adrenal Gland Pheochromocytoma",
                                 meaning=NCIT.C4220)
    C7402 = PermissibleValue(text="C7402",
                                 description="Hairy Cell Leukemia",
                                 meaning=NCIT.C7402)
    C4231 = PermissibleValue(text="C4231",
                                 description="Junctional Nevus",
                                 meaning=NCIT.C4231)
    C3996 = PermissibleValue(text="C3996",
                                 description="Monoclonal Gammopathy of Undetermined Significance",
                                 meaning=NCIT.C3996)
    C3712 = PermissibleValue(text="C3712",
                                 description="Squamous Cell Papilloma",
                                 meaning=NCIT.C3712)
    C3766 = PermissibleValue(text="C3766",
                                 description="Clear Cell Adenocarcinoma",
                                 meaning=NCIT.C3766)
    C7645 = PermissibleValue(text="C7645",
                                 description="Breast Intracystic Papillary Carcinoma",
                                 meaning=NCIT.C7645)
    C3295 = PermissibleValue(text="C3295",
                                 description="Osteochondroma",
                                 meaning=NCIT.C3295)
    C3461 = PermissibleValue(text="C3461",
                                 description="Immunoblastic Lymphoma",
                                 meaning=NCIT.C3461)
    C174129 = PermissibleValue(text="C174129",
                                     description="Acute Myeloid Leukemia with MLL Rearrangement",
                                     meaning=NCIT.C174129)
    C6906 = PermissibleValue(text="C6906",
                                 description="Atypical Teratoid/Rhabdoid Tumor",
                                 meaning=NCIT.C6906)
    C4563 = PermissibleValue(text="C4563",
                                 description="Chronic Eosinophilic Leukemia, Not Otherwise Specified",
                                 meaning=NCIT.C4563)
    C2946 = PermissibleValue(text="C2946",
                                 description="Chondrosarcoma",
                                 meaning=NCIT.C2946)
    C9344 = PermissibleValue(text="C9344",
                                 description="Pineoblastoma",
                                 meaning=NCIT.C9344)
    C9137 = PermissibleValue(text="C9137",
                                 description="Combined Lung Small Cell Carcinoma",
                                 meaning=NCIT.C9137)
    C6887 = PermissibleValue(text="C6887",
                                 description="Thymoma Type B1",
                                 meaning=NCIT.C6887)
    C4335 = PermissibleValue(text="C4335",
                                 description="Malignant Triton Tumor",
                                 meaning=NCIT.C4335)
    C4114 = PermissibleValue(text="C4114",
                                 description="Pilomatrical Carcinoma",
                                 meaning=NCIT.C4114)
    C6474 = PermissibleValue(text="C6474",
                                 description="Low Grade Central Osteosarcoma",
                                 meaning=NCIT.C6474)
    C9496 = PermissibleValue(text="C9496",
                                 description="T-Cell/Histiocyte-Rich Large B-Cell Lymphoma",
                                 meaning=NCIT.C9496)
    C37193 = PermissibleValue(text="C37193",
                                   description="Anaplastic Large Cell Lymphoma, ALK-Positive",
                                   meaning=NCIT.C37193)
    C3800 = PermissibleValue(text="C3800",
                                 description="Epithelioid Hemangioendothelioma",
                                 meaning=NCIT.C3800)
    C8644 = PermissibleValue(text="C8644",
                                 description="B Acute Lymphoblastic Leukemia",
                                 meaning=NCIT.C8644)
    C3727 = PermissibleValue(text="C3727",
                                 description="Adenosquamous Carcinoma",
                                 meaning=NCIT.C3727)
    C3230 = PermissibleValue(text="C3230",
                                 description="Meningioma",
                                 meaning=NCIT.C3230)
    C6801 = PermissibleValue(text="C6801",
                                 description="Skin Fibrous Histiocytoma",
                                 meaning=NCIT.C6801)
    C2970 = PermissibleValue(text="C2970",
                                 description="Adenoid Cystic Carcinoma",
                                 meaning=NCIT.C2970)
    C3717 = PermissibleValue(text="C3717",
                                 description="Melanotic Neuroectodermal Tumor",
                                 meaning=NCIT.C3717)
    C6194 = PermissibleValue(text="C6194",
                                 description="Collecting Duct Carcinoma",
                                 meaning=NCIT.C6194)
    C3400 = PermissibleValue(text="C3400",
                                 description="Synovial Sarcoma",
                                 meaning=NCIT.C3400)
    C7427 = PermissibleValue(text="C7427",
                                 description="Diffuse Sclerosing Variant Thyroid Gland Papillary Carcinoma",
                                 meaning=NCIT.C7427)
    C3739 = PermissibleValue(text="C3739",
                                 description="Fibrous Histiocytoma",
                                 meaning=NCIT.C3739)
    C27125 = PermissibleValue(text="C27125",
                                   description="Proliferating Trichilemmal Tumor",
                                   meaning=NCIT.C27125)
    C2948 = PermissibleValue(text="C2948",
                                 description="Choriocarcinoma",
                                 meaning=NCIT.C2948)
    C3326 = PermissibleValue(text="C3326",
                                 description="Adrenal Gland Pheochromocytoma",
                                 meaning=NCIT.C3326)
    C3262 = PermissibleValue(text="C3262",
                                 description="Neoplasm",
                                 meaning=NCIT.C3262)
    C4215 = PermissibleValue(text="C4215",
                                 description="Ovarian Steroid Cell Tumor",
                                 meaning=NCIT.C4215)
    C3261 = PermissibleValue(text="C3261",
                                 description="Metastatic Neoplasm",
                                 meaning=NCIT.C3261)
    C7506 = PermissibleValue(text="C7506",
                                 description="Myelodysplastic Syndrome with Excess Blasts",
                                 meaning=NCIT.C7506)
    C27287 = PermissibleValue(text="C27287",
                                   description="Ovarian Endometrioid Adenofibroma",
                                   meaning=NCIT.C27287)
    C9233 = PermissibleValue(text="C9233",
                                 description="Juvenile Myelomonocytic Leukemia",
                                 meaning=NCIT.C9233)
    C4344 = PermissibleValue(text="C4344",
                                 description="Acute Panmyelosis with Myelofibrosis",
                                 meaning=NCIT.C4344)
    C4341 = PermissibleValue(text="C4341",
                                 description="Marginal Zone Lymphoma",
                                 meaning=NCIT.C4341)
    C65162 = PermissibleValue(text="C65162",
                                   description="Tumorlet",
                                   meaning=NCIT.C65162)
    C9128 = PermissibleValue(text="C9128",
                                 description="Philadelphia Chromosome Positive, BCR-ABL1 Positive Chronic Myelogenous Leukemia",
                                 meaning=NCIT.C9128)
    C6867 = PermissibleValue(text="C6867",
                                 description="Myelodysplastic Syndrome with Isolated del(5q)",
                                 meaning=NCIT.C6867)
    C3741 = PermissibleValue(text="C3741",
                                 description="Abdominal (Mesenteric) Fibromatosis",
                                 meaning=NCIT.C3741)
    C7996 = PermissibleValue(text="C7996",
                                 description="Malignant Type B1 Thymoma",
                                 meaning=NCIT.C7996)
    C7269 = PermissibleValue(text="C7269",
                                 description="Minimally Invasive Lung Non-Mucinous Adenocarcinoma",
                                 meaning=NCIT.C7269)
    C3879 = PermissibleValue(text="C3879",
                                 description="Thyroid Gland Medullary Carcinoma",
                                 meaning=NCIT.C3879)
    C7949 = PermissibleValue(text="C7949",
                                 description="Breast Ductal Carcinoma In Situ, High Grade",
                                 meaning=NCIT.C7949)
    C7463 = PermissibleValue(text="C7463",
                                 description="Acute Myelomonocytic Leukemia",
                                 meaning=NCIT.C7463)
    C3336 = PermissibleValue(text="C3336",
                                 description="Polycythemia Vera",
                                 meaning=NCIT.C3336)
    C3366 = PermissibleValue(text="C3366",
                                 description="Sezary Syndrome",
                                 meaning=NCIT.C3366)
    C3184 = PermissibleValue(text="C3184",
                                 description="Adult T-Cell Leukemia/Lymphoma",
                                 meaning=NCIT.C3184)
    C7688 = PermissibleValue(text="C7688",
                                 description="Invasive Breast Ductal Carcinoma and Lobular Carcinoma",
                                 meaning=NCIT.C7688)
    C46104 = PermissibleValue(text="C46104",
                                   description="Thyroid Gland Mixed Medullary and Follicular Cell Carcinoma",
                                   meaning=NCIT.C46104)
    C9325 = PermissibleValue(text="C9325",
                                 description="Adrenal Cortex Carcinoma",
                                 meaning=NCIT.C9325)
    C4018 = PermissibleValue(text="C4018",
                                 description="Breast Lobular Carcinoma In Situ",
                                 meaning=NCIT.C4018)
    C67006 = PermissibleValue(text="C67006",
                                   description="Malignant Sertoli Cell Tumor",
                                   meaning=NCIT.C67006)
    C4109 = PermissibleValue(text="C4109",
                                 description="Skin Fibroepithelial Basal Cell Carcinoma",
                                 meaning=NCIT.C4109)
    C4000 = PermissibleValue(text="C4000",
                                 description="Stage 0 Cervical Cancer AJCC v6",
                                 meaning=NCIT.C4000)
    C3212 = PermissibleValue(text="C3212",
                                 description="Lymphoplasmacytic Lymphoma",
                                 meaning=NCIT.C3212)
    C8965 = PermissibleValue(text="C8965",
                                 description="Lymphangioma",
                                 meaning=NCIT.C8965)
    C3785 = PermissibleValue(text="C3785",
                                 description="Intraductal Papilloma",
                                 meaning=NCIT.C3785)
    C9118 = PermissibleValue(text="C9118",
                                 description="Sarcoma",
                                 meaning=NCIT.C9118)
    C3267 = PermissibleValue(text="C3267",
                                 description="Wilms Tumor",
                                 meaning=NCIT.C3267)
    C3017 = PermissibleValue(text="C3017",
                                 description="Ependymoma",
                                 meaning=NCIT.C3017)
    C4342 = PermissibleValue(text="C4342",
                                 description="Intravascular Large B-Cell Lymphoma",
                                 meaning=NCIT.C4342)
    C4287 = PermissibleValue(text="C4287",
                                 description="Malignant Teratoma",
                                 meaning=NCIT.C4287)
    C4715 = PermissibleValue(text="C4715",
                                 description="Choroid Plexus Carcinoma",
                                 meaning=NCIT.C4715)
    C7400 = PermissibleValue(text="C7400",
                                 description="Burkitt Leukemia",
                                 meaning=NCIT.C7400)
    C3269 = PermissibleValue(text="C3269",
                                 description="Schwannoma",
                                 meaning=NCIT.C3269)
    C4247 = PermissibleValue(text="C4247",
                                 description="Undifferentiated Pleomorphic Sarcoma",
                                 meaning=NCIT.C4247)
    C2964 = PermissibleValue(text="C2964",
                                 description="Craniopharyngioma",
                                 meaning=NCIT.C2964)
    C3768 = PermissibleValue(text="C3768",
                                 description="Acinar Cell Carcinoma",
                                 meaning=NCIT.C3768)
    C3730 = PermissibleValue(text="C3730",
                                 description="Mixed Mesodermal (Mullerian) Tumor",
                                 meaning=NCIT.C3730)
    C9280 = PermissibleValue(text="C9280",
                                 description="Primary Mediastinal (Thymic) Large B-Cell Lymphoma",
                                 meaning=NCIT.C9280)
    C3085 = PermissibleValue(text="C3085",
                                 description="Hemangioma",
                                 meaning=NCIT.C3085)
    C3781 = PermissibleValue(text="C3781",
                                 description="Verrucous Carcinoma",
                                 meaning=NCIT.C3781)
    C9231 = PermissibleValue(text="C9231",
                                 description="Merkel Cell Carcinoma",
                                 meaning=NCIT.C9231)
    C3898 = PermissibleValue(text="C3898",
                                 description="Extranodal Marginal Zone Lymphoma of Mucosa-Associated Lymphoid Tissue",
                                 meaning=NCIT.C3898)
    C3692 = PermissibleValue(text="C3692",
                                 description="Undifferentiated Carcinoma",
                                 meaning=NCIT.C3692)
    C3224 = PermissibleValue(text="C3224",
                                 description="Melanoma",
                                 meaning=NCIT.C3224)
    C3434 = PermissibleValue(text="C3434",
                                 description="Uterine Corpus Leiomyoma",
                                 meaning=NCIT.C3434)
    C6505 = PermissibleValue(text="C6505",
                                 description="Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                 meaning=NCIT.C6505)
    C4221 = PermissibleValue(text="C4221",
                                 description="Malignant Glomus Tumor",
                                 meaning=NCIT.C4221)
    C27252 = PermissibleValue(text="C27252",
                                   description="Enterochromaffin-Like Cell Neuroendocrine Tumor G1",
                                   meaning=NCIT.C27252)
    C3728 = PermissibleValue(text="C3728",
                                 description="Hepatoblastoma",
                                 meaning=NCIT.C3728)
    C3770 = PermissibleValue(text="C3770",
                                 description="Pancreatic Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3770)
    C3107 = PermissibleValue(text="C3107",
                                 description="Langerhans Cell Histiocytosis",
                                 meaning=NCIT.C3107)
    C6985 = PermissibleValue(text="C6985",
                                 description="Invasive Hydatidiform Mole",
                                 meaning=NCIT.C6985)
    C9288 = PermissibleValue(text="C9288",
                                 description="Acute Myeloid Leukemia with t(8;21); (q22; q22.1); RUNX1-RUNX1T1",
                                 meaning=NCIT.C9288)
    C9300 = PermissibleValue(text="C9300",
                                 description="Acute Leukemia",
                                 meaning=NCIT.C9300)
    C9385 = PermissibleValue(text="C9385",
                                 description="Renal Cell Carcinoma",
                                 meaning=NCIT.C9385)
    C4092 = PermissibleValue(text="C4092",
                                 description="Benign Epithelial Neoplasm",
                                 meaning=NCIT.C4092)
    C4189 = PermissibleValue(text="C4189",
                                 description="Breast Secretory Carcinoma",
                                 meaning=NCIT.C4189)
    C4684 = PermissibleValue(text="C4684",
                                 description="Nasal Type Extranodal NK/T-Cell Lymphoma",
                                 meaning=NCIT.C4684)
    C6897 = PermissibleValue(text="C6897",
                                 description="Cystic Partially Differentiated Kidney Nephroblastoma",
                                 meaning=NCIT.C6897)
    C4817 = PermissibleValue(text="C4817",
                                 description="Ewing Sarcoma",
                                 meaning=NCIT.C4817)
    C3465 = PermissibleValue(text="C3465",
                                 description="Grade 1 Follicular Lymphoma",
                                 meaning=NCIT.C3465)
    C3359 = PermissibleValue(text="C3359",
                                 description="Rhabdomyosarcoma",
                                 meaning=NCIT.C3359)
    C3339 = PermissibleValue(text="C3339",
                                 description="Familial Adenomatous Polyposis",
                                 meaning=NCIT.C3339)
    C2973 = PermissibleValue(text="C2973",
                                 description="Mucinous Cystadenoma",
                                 meaning=NCIT.C2973)
    C3773 = PermissibleValue(text="C3773",
                                 description="Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3773)
    C3246 = PermissibleValue(text="C3246",
                                 description="Mycosis Fungoides",
                                 meaning=NCIT.C3246)
    C7983 = PermissibleValue(text="C7983",
                                 description="Borderline Ovarian Endometrioid Tumor/Atypical Proliferative Ovarian Endometrioid Tumor",
                                 meaning=NCIT.C7983)
    C9145 = PermissibleValue(text="C9145",
                                 description="Osteosarcoma",
                                 meaning=NCIT.C9145)
    C4194 = PermissibleValue(text="C4194",
                                 description="Invasive Breast Carcinoma of No Special Type",
                                 meaning=NCIT.C4194)
    C3178 = PermissibleValue(text="C3178",
                                 description="Chronic Myelomonocytic Leukemia",
                                 meaning=NCIT.C3178)
    C27004 = PermissibleValue(text="C27004",
                                   description="Sarcomatoid Carcinoma",
                                   meaning=NCIT.C27004)
    C3270 = PermissibleValue(text="C3270",
                                 description="Neuroblastoma",
                                 meaning=NCIT.C3270)
    C3679 = PermissibleValue(text="C3679",
                                 description="Oncocytic Adenocarcinoma",
                                 meaning=NCIT.C3679)
    C3677 = PermissibleValue(text="C3677",
                                 description="Benign Neoplasm",
                                 meaning=NCIT.C3677)
    C39976 = PermissibleValue(text="C39976",
                                   description="Sertoli Cell Tumor",
                                   meaning=NCIT.C39976)
    C8423 = PermissibleValue(text="C8423",
                                 description="Stage 0 Cutaneous Melanoma AJCC v6 and v7",
                                 meaning=NCIT.C8423)
    C2916 = PermissibleValue(text="C2916",
                                 description="Carcinoma",
                                 meaning=NCIT.C2916)
    C6913 = PermissibleValue(text="C6913",
                                 description="Lymphocyte-Rich Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C6913)
    C27007 = PermissibleValue(text="C27007",
                                   description="Spitz Nevus",
                                   meaning=NCIT.C27007)
    C27093 = PermissibleValue(text="C27093",
                                   description="Stage 0 Squamous Cell Carcinoma",
                                   meaning=NCIT.C27093)
    C4190 = PermissibleValue(text="C4190",
                                 description="Breast Papillary Ductal Carcinoma In Situ",
                                 meaning=NCIT.C4190)
    C2929 = PermissibleValue(text="C2929",
                                 description="Squamous Cell Carcinoma",
                                 meaning=NCIT.C2929)
    C3460 = PermissibleValue(text="C3460",
                                 description="Grade 3 Follicular Lymphoma",
                                 meaning=NCIT.C3460)
    C3088 = PermissibleValue(text="C3088",
                                 description="Angiosarcoma",
                                 meaning=NCIT.C3088)
    C4340 = PermissibleValue(text="C4340",
                                 description="Peripheral T-Cell Lymphoma, Not Otherwise Specified",
                                 meaning=NCIT.C4340)
    C3520 = PermissibleValue(text="C3520",
                                 description="Myeloid Sarcoma",
                                 meaning=NCIT.C3520)
    C4345 = PermissibleValue(text="C4345",
                                 description="Myeloproliferative Neoplasm",
                                 meaning=NCIT.C4345)
    C3011 = PermissibleValue(text="C3011",
                                 description="Yolk Sac Tumor",
                                 meaning=NCIT.C3011)
    C35870 = PermissibleValue(text="C35870",
                                   description="Conventional Osteosarcoma",
                                   meaning=NCIT.C35870)
    C3789 = PermissibleValue(text="C3789",
                                 description="Olfactory Neuroblastoma",
                                 meaning=NCIT.C3789)
    C3407 = PermissibleValue(text="C3407",
                                 description="Essential Thrombocythemia",
                                 meaning=NCIT.C3407)
    C3170 = PermissibleValue(text="C3170",
                                 description="Acute Megakaryoblastic Leukemia",
                                 meaning=NCIT.C3170)
    C4146 = PermissibleValue(text="C4146",
                                 description="Chromophobe Renal Cell Carcinoma",
                                 meaning=NCIT.C4146)
    C8968 = PermissibleValue(text="C8968",
                                 description="Grade 2 Follicular Lymphoma",
                                 meaning=NCIT.C8968)
    C3132 = PermissibleValue(text="C3132",
                                 description="Alpha Heavy Chain Disease",
                                 meaning=NCIT.C3132)
    C3182 = PermissibleValue(text="C3182",
                                 description="Acute Promyelocytic Leukemia with PML-RARA",
                                 meaning=NCIT.C3182)
    C3716 = PermissibleValue(text="C3716",
                                 description="Primitive Neuroectodermal Tumor",
                                 meaning=NCIT.C3716)
    C2915 = PermissibleValue(text="C2915",
                                 description="Carcinoid Tumor",
                                 meaning=NCIT.C2915)
    C3099 = PermissibleValue(text="C3099",
                                 description="Hepatocellular Carcinoma",
                                 meaning=NCIT.C3099)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C3211 = PermissibleValue(text="C3211",
                                 description="Non-Hodgkin Lymphoma",
                                 meaning=NCIT.C3211)
    C4867 = PermissibleValue(text="C4867",
                                 description="Malignant Soft Tissue Neoplasm",
                                 meaning=NCIT.C4867)
    C9305 = PermissibleValue(text="C9305",
                                 description="Malignant Neoplasm",
                                 meaning=NCIT.C9305)
    C9357 = PermissibleValue(text="C9357",
                                 description="Hodgkin Lymphoma",
                                 meaning=NCIT.C9357)
    C3161 = PermissibleValue(text="C3161",
                                 description="Leukemia",
                                 meaning=NCIT.C3161)
    C3167 = PermissibleValue(text="C3167",
                                 description="Acute Lymphoblastic Leukemia",
                                 meaning=NCIT.C3167)
    C3172 = PermissibleValue(text="C3172",
                                 description="Myeloid Leukemia",
                                 meaning=NCIT.C3172)
    C3209 = PermissibleValue(text="C3209",
                                 description="Follicular Lymphoma",
                                 meaning=NCIT.C3209)
    C9283 = PermissibleValue(text="C9283",
                                 description="Lymphocyte-Depleted Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C9283)
    C3518 = PermissibleValue(text="C3518",
                                 description="Nodular Sclerosis Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C3518)
    C7539 = PermissibleValue(text="C7539",
                                 description="Lymphoid Leukemia",
                                 meaning=NCIT.C7539)
    C2912 = PermissibleValue(text="C2912",
                                 description="Burkitt Lymphoma",
                                 meaning=NCIT.C2912)
    C7258 = PermissibleValue(text="C7258",
                                 description="Nodular Lymphocyte Predominant Hodgkin Lymphoma",
                                 meaning=NCIT.C7258)
    C3208 = PermissibleValue(text="C3208",
                                 description="Lymphoma",
                                 meaning=NCIT.C3208)
    C3058 = PermissibleValue(text="C3058",
                                 description="Glioblastoma",
                                 meaning=NCIT.C3058)
    C3798 = PermissibleValue(text="C3798",
                                 description="Malignant Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C3798)
    C3247 = PermissibleValue(text="C3247",
                                 description="Myelodysplastic Syndrome",
                                 meaning=NCIT.C3247)
    C4861 = PermissibleValue(text="C4861",
                                 description="Acute Monocytic Leukemia",
                                 meaning=NCIT.C4861)
    C2921 = PermissibleValue(text="C2921",
                                 description="Skin Basal Cell Carcinoma",
                                 meaning=NCIT.C2921)
    C156767 = PermissibleValue(text="C156767",
                                     description="Basal Cell Carcinoma",
                                     meaning=NCIT.C156767)
    C3171 = PermissibleValue(text="C3171",
                                 description="Acute Myeloid Leukemia",
                                 meaning=NCIT.C3171)
    C3174 = PermissibleValue(text="C3174",
                                 description="Chronic Myelogenous Leukemia, BCR-ABL1 Positive",
                                 meaning=NCIT.C3174)
    C26712 = PermissibleValue(text="C26712",
                                   description="Mucinous Adenocarcinoma",
                                   meaning=NCIT.C26712)
    C2923 = PermissibleValue(text="C2923",
                                 description="Minimally Invasive Lung Adenocarcinoma",
                                 meaning=NCIT.C2923)
    C3242 = PermissibleValue(text="C3242",
                                 description="Plasma Cell Myeloma",
                                 meaning=NCIT.C3242)
    C9360 = PermissibleValue(text="C9360",
                                 description="Lymphoblastic Lymphoma",
                                 meaning=NCIT.C9360)
    C8851 = PermissibleValue(text="C8851",
                                 description="Diffuse Large B-Cell Lymphoma",
                                 meaning=NCIT.C8851)
    C2924 = PermissibleValue(text="C2924",
                                 description="Breast Ductal Carcinoma In Situ",
                                 meaning=NCIT.C2924)
    C8054 = PermissibleValue(text="C8054",
                                 description="Thyroid Gland Follicular Carcinoma",
                                 meaning=NCIT.C8054)
    C4033 = PermissibleValue(text="C4033",
                                 description="Clear Cell Renal Cell Carcinoma",
                                 meaning=NCIT.C4033)
    C8923 = PermissibleValue(text="C8923",
                                 description="Acute Erythroid Leukemia",
                                 meaning=NCIT.C8923)
    C3517 = PermissibleValue(text="C3517",
                                 description="Mixed Cellularity Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C3517)
    C7540 = PermissibleValue(text="C7540",
                                 description="Small Lymphocytic Lymphoma",
                                 meaning=NCIT.C7540)
    C7997 = PermissibleValue(text="C7997",
                                 description="Thymoma Type B3",
                                 meaning=NCIT.C7997)
    C4337 = PermissibleValue(text="C4337",
                                 description="Mantle Cell Lymphoma",
                                 meaning=NCIT.C4337)
    C2862 = PermissibleValue(text="C2862",
                                 description="Primary Myelofibrosis",
                                 meaning=NCIT.C2862)
    C65157 = PermissibleValue(text="C65157",
                                   description="Neoplasm, Uncertain Whether Benign or Malignant",
                                   meaning=NCIT.C65157)
    C3720 = PermissibleValue(text="C3720",
                                 description="Anaplastic Large Cell Lymphoma",
                                 meaning=NCIT.C3720)
    C3915 = PermissibleValue(text="C3915",
                                 description="Small Cell Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3915)
    C4139 = PermissibleValue(text="C4139",
                                 description="Combined Carcinoid and Adenocarcinoma",
                                 meaning=NCIT.C4139)
    C7528 = PermissibleValue(text="C7528",
                                 description="Angioimmunoblastic T-Cell Lymphoma",
                                 meaning=NCIT.C7528)
    C3163 = PermissibleValue(text="C3163",
                                 description="Chronic Lymphocytic Leukemia",
                                 meaning=NCIT.C3163)
    C27911 = PermissibleValue(text="C27911",
                                   description="Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma",
                                   meaning=NCIT.C27911)
    C3762 = PermissibleValue(text="C3762",
                                 description="Adenomatoid Tumor",
                                 meaning=NCIT.C3762)
    C4664 = PermissibleValue(text="C4664",
                                 description="T-Cell Large Granular Lymphocyte Leukemia",
                                 meaning=NCIT.C4664)
    C2917 = PermissibleValue(text="C2917",
                                 description="Carcinoma In Situ",
                                 meaning=NCIT.C2917)
    C9087 = PermissibleValue(text="C9087",
                                 description="Kaposi Sarcoma",
                                 meaning=NCIT.C9087)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.condition",
        description="Autogenerated Enumeration for CRDC-H Diagnosis condition",
        code_set=None,
        code_set_version="2021-05-27T15:46:43.715569+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Carcinoid tumor, argentaffin, NOS",
                PermissibleValue(text="Carcinoid tumor, argentaffin, NOS",
                                 description="Carcinoid tumor, argentaffin, NOS") )
        setattr(cls, "Infiltrating duct and colloid carcinoma",
                PermissibleValue(text="Infiltrating duct and colloid carcinoma",
                                 description="Infiltrating duct and colloid carcinoma") )
        setattr(cls, "Tubulopapillary adenocarcinoma",
                PermissibleValue(text="Tubulopapillary adenocarcinoma",
                                 description="Tubulopapillary adenocarcinoma") )
        setattr(cls, "Malignant chondroid syringoma",
                PermissibleValue(text="Malignant chondroid syringoma",
                                 description="Malignant chondroid syringoma") )
        setattr(cls, "Reticulum cell sarcoma, diffuse",
                PermissibleValue(text="Reticulum cell sarcoma, diffuse",
                                 description="Reticulum cell sarcoma, diffuse") )
        setattr(cls, "Congenital generalized fibromatosis",
                PermissibleValue(text="Congenital generalized fibromatosis",
                                 description="Congenital generalized fibromatosis") )
        setattr(cls, "Terminal duct adenocarcinoma",
                PermissibleValue(text="Terminal duct adenocarcinoma",
                                 description="Terminal duct adenocarcinoma") )
        setattr(cls, "Gastrointestinal pacemaker cell tumor",
                PermissibleValue(text="Gastrointestinal pacemaker cell tumor",
                                 description="Gastrointestinal pacemaker cell tumor") )
        setattr(cls, "Clear cell sarcoma, of tendons and aponeuroses",
                PermissibleValue(text="Clear cell sarcoma, of tendons and aponeuroses",
                                 description="Clear cell sarcoma, of tendons and aponeuroses") )
        setattr(cls, "DCIS, comedo type",
                PermissibleValue(text="DCIS, comedo type",
                                 description="DCIS, comedo type") )
        setattr(cls, "Papillotubular adenocarcinoma",
                PermissibleValue(text="Papillotubular adenocarcinoma",
                                 description="Papillotubular adenocarcinoma") )
        setattr(cls, "Atypical proliferative mucinous tumor",
                PermissibleValue(text="Atypical proliferative mucinous tumor",
                                 description="Atypical proliferative mucinous tumor") )
        setattr(cls, "Metaplastic carcinoma with chondroid differentiation",
                PermissibleValue(text="Metaplastic carcinoma with chondroid differentiation",
                                 description="Metaplastic carcinoma with chondroid differentiation") )
        setattr(cls, "Schmincke tumor",
                PermissibleValue(text="Schmincke tumor",
                                 description="Schmincke tumor") )
        setattr(cls, "Testicular stromal tumor",
                PermissibleValue(text="Testicular stromal tumor",
                                 description="Testicular stromal tumor") )
        setattr(cls, "Traditional sessile serrated adenoma",
                PermissibleValue(text="Traditional sessile serrated adenoma",
                                 description="Traditional sessile serrated adenoma") )
        setattr(cls, "Reticulosarcoma, diffuse",
                PermissibleValue(text="Reticulosarcoma, diffuse",
                                 description="Reticulosarcoma, diffuse") )
        setattr(cls, "Serous cystadenocarcinofibroma",
                PermissibleValue(text="Serous cystadenocarcinofibroma",
                                 description="Serous cystadenocarcinofibroma") )
        setattr(cls, "Invasive carcinoma of no special type",
                PermissibleValue(text="Invasive carcinoma of no special type",
                                 description="Invasive carcinoma of no special type") )
        setattr(cls, "Intraductal papillary-mucinous carcinoma, non-invasive",
                PermissibleValue(text="Intraductal papillary-mucinous carcinoma, non-invasive",
                                 description="Intraductal papillary-mucinous carcinoma, non-invasive") )
        setattr(cls, "Carcinoid, NOS, of appendix",
                PermissibleValue(text="Carcinoid, NOS, of appendix",
                                 description="Carcinoid, NOS, of appendix") )
        setattr(cls, "Argentaffinoma, NOS",
                PermissibleValue(text="Argentaffinoma, NOS",
                                 description="Argentaffinoma, NOS") )
        setattr(cls, "Endometrioid cystadenoma, NOS",
                PermissibleValue(text="Endometrioid cystadenoma, NOS",
                                 description="Endometrioid cystadenoma, NOS") )
        setattr(cls, "Anal intraepithelial neoplasia, low grade",
                PermissibleValue(text="Anal intraepithelial neoplasia, low grade",
                                 description="Anal intraepithelial neoplasia, low grade") )
        setattr(cls, "Mucinous cystadenocarcinofibroma",
                PermissibleValue(text="Mucinous cystadenocarcinofibroma",
                                 description="Mucinous cystadenocarcinofibroma") )
        setattr(cls, "Acute myloid leukemia, 11q23 abnormalities",
                PermissibleValue(text="Acute myloid leukemia, 11q23 abnormalities",
                                 description="Acute myloid leukemia, 11q23 abnormalities") )
        setattr(cls, "Enteric adenocarcinoma",
                PermissibleValue(text="Enteric adenocarcinoma",
                                 description="Enteric adenocarcinoma") )
        setattr(cls, "Plexiform fibromyxoma",
                PermissibleValue(text="Plexiform fibromyxoma",
                                 description="Plexiform fibromyxoma") )
        setattr(cls, "Hemangiopericytic meningioma",
                PermissibleValue(text="Hemangiopericytic meningioma",
                                 description="Hemangiopericytic meningioma") )
        setattr(cls, "Combined small cell-large carcinoma",
                PermissibleValue(text="Combined small cell-large carcinoma",
                                 description="Combined small cell-large carcinoma") )
        setattr(cls, "Aleukemic myelogenous leukemia",
                PermissibleValue(text="Aleukemic myelogenous leukemia",
                                 description="Aleukemic myelogenous leukemia") )
        setattr(cls, "Adenocarcinoma, cribriform comedo-type",
                PermissibleValue(text="Adenocarcinoma, cribriform comedo-type",
                                 description="Adenocarcinoma, cribriform comedo-type") )
        setattr(cls, "Mixed acinar-endocrine carcinoma",
                PermissibleValue(text="Mixed acinar-endocrine carcinoma",
                                 description="Mixed acinar-endocrine carcinoma") )
        setattr(cls, "Adenocarcinoma, pancreatobiliary type",
                PermissibleValue(text="Adenocarcinoma, pancreatobiliary type",
                                 description="Adenocarcinoma, pancreatobiliary type") )
        setattr(cls, "Transitional pineal tumor",
                PermissibleValue(text="Transitional pineal tumor",
                                 description="Transitional pineal tumor") )
        setattr(cls, "Mucocarcinoid tumor",
                PermissibleValue(text="Mucocarcinoid tumor",
                                 description="Mucocarcinoid tumor") )
        setattr(cls, "Neuroendocrine tumor, grade 1",
                PermissibleValue(text="Neuroendocrine tumor, grade 1",
                                 description="Neuroendocrine tumor, grade 1") )
        setattr(cls, "Mixed islet cell and exocrine adenocarcinoma",
                PermissibleValue(text="Mixed islet cell and exocrine adenocarcinoma",
                                 description="Mixed islet cell and exocrine adenocarcinoma") )
        setattr(cls, "Intraductal papillary-mucinous tumor with intermediate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with intermediate dysplasia",
                                 description="Intraductal papillary-mucinous tumor with intermediate dysplasia") )
        setattr(cls, "Acute myeloid leukemia, t(15:17)(g22;q11-12)",
                PermissibleValue(text="Acute myeloid leukemia, t(15:17)(g22;q11-12)",
                                 description="Acute myeloid leukemia, t(15:17)(g22;q11-12)") )
        setattr(cls, "Hepatocellular carcinoma, sarcomatoid",
                PermissibleValue(text="Hepatocellular carcinoma, sarcomatoid",
                                 description="Hepatocellular carcinoma, sarcomatoid") )
        setattr(cls, "Serotonin producing carcinoid",
                PermissibleValue(text="Serotonin producing carcinoid",
                                 description="Serotonin producing carcinoid") )
        setattr(cls, "Mixed endocrine and exocrine adenocarcinoma",
                PermissibleValue(text="Mixed endocrine and exocrine adenocarcinoma",
                                 description="Mixed endocrine and exocrine adenocarcinoma") )
        setattr(cls, "Periductal stromal tumor, low grade",
                PermissibleValue(text="Periductal stromal tumor, low grade",
                                 description="Periductal stromal tumor, low grade") )
        setattr(cls, "Nonchromaffin paraganglioma, NOS",
                PermissibleValue(text="Nonchromaffin paraganglioma, NOS",
                                 description="Nonchromaffin paraganglioma, NOS") )
        setattr(cls, "Solid carcinoma with mucin formation",
                PermissibleValue(text="Solid carcinoma with mucin formation",
                                 description="Solid carcinoma with mucin formation") )
        setattr(cls, "Infiltrating duct and mucinous carcinoma",
                PermissibleValue(text="Infiltrating duct and mucinous carcinoma",
                                 description="Infiltrating duct and mucinous carcinoma") )
        setattr(cls, "Acute progressive histiocytosis X",
                PermissibleValue(text="Acute progressive histiocytosis X",
                                 description="Acute progressive histiocytosis X") )
        setattr(cls, "MPNST with mesenchymal differentiation",
                PermissibleValue(text="MPNST with mesenchymal differentiation",
                                 description="MPNST with mesenchymal differentiation") )
        setattr(cls, "Cylindrical cell papilloma",
                PermissibleValue(text="Cylindrical cell papilloma",
                                 description="Cylindrical cell papilloma") )
        setattr(cls, "Malignant lymphoma, mixed lymphocytic-histiocytic, diffuse",
                PermissibleValue(text="Malignant lymphoma, mixed lymphocytic-histiocytic, diffuse",
                                 description="Malignant lymphoma, mixed lymphocytic-histiocytic, diffuse") )
        setattr(cls, "Ductal carcinoma in situ, comedo type",
                PermissibleValue(text="Ductal carcinoma in situ, comedo type",
                                 description="Ductal carcinoma in situ, comedo type") )
        setattr(cls, "Thymic carcinoma with adenoid cystic carcinoma-like features",
                PermissibleValue(text="Thymic carcinoma with adenoid cystic carcinoma-like features",
                                 description="Thymic carcinoma with adenoid cystic carcinoma-like features") )
        setattr(cls, "Differentiated penile intraepithelial neoplasia",
                PermissibleValue(text="Differentiated penile intraepithelial neoplasia",
                                 description="Differentiated penile intraepithelial neoplasia") )
        setattr(cls, "Malignant serous cystadenofibroma",
                PermissibleValue(text="Malignant serous cystadenofibroma",
                                 description="Malignant serous cystadenofibroma") )
        setattr(cls, "Folliculome lipidique",
                PermissibleValue(text="Folliculome lipidique",
                                 description="Folliculome lipidique") )
        setattr(cls, "Metaplastic carcinoma with other types mesenchymal differentiation",
                PermissibleValue(text="Metaplastic carcinoma with other types mesenchymal differentiation",
                                 description="Metaplastic carcinoma with other types mesenchymal differentiation") )
        setattr(cls, "Choriocarcinoma combined with teratorna",
                PermissibleValue(text="Choriocarcinoma combined with teratorna",
                                 description="Choriocarcinoma combined with teratorna") )
        setattr(cls, "Nodular hidradenoma, malignant",
                PermissibleValue(text="Nodular hidradenoma, malignant",
                                 description="Nodular hidradenoma, malignant") )
        setattr(cls, "Clear cell cystadenocarcinofibroma",
                PermissibleValue(text="Clear cell cystadenocarcinofibroma",
                                 description="Clear cell cystadenocarcinofibroma") )
        setattr(cls, "High-grade neuroendocrine carcinoma",
                PermissibleValue(text="High-grade neuroendocrine carcinoma",
                                 description="High-grade neuroendocrine carcinoma") )
        setattr(cls, "Intraductal carcinoma, clinging",
                PermissibleValue(text="Intraductal carcinoma, clinging",
                                 description="Intraductal carcinoma, clinging") )
        setattr(cls, "Malignant lymphoma, noncleaved cell, follicular, NOS",
                PermissibleValue(text="Malignant lymphoma, noncleaved cell, follicular, NOS",
                                 description="Malignant lymphoma, noncleaved cell, follicular, NOS") )
        setattr(cls, "Clear cell cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Clear cell cystadenofibroma of borderline malignancy",
                                 description="Clear cell cystadenofibroma of borderline malignancy") )
        setattr(cls, "Carcinoid tumor, NOS, of appendix",
                PermissibleValue(text="Carcinoid tumor, NOS, of appendix",
                                 description="Carcinoid tumor, NOS, of appendix") )
        setattr(cls, "Pancreatic microadenoma",
                PermissibleValue(text="Pancreatic microadenoma",
                                 description="Pancreatic microadenoma") )
        setattr(cls, "Diktyoma, benign",
                PermissibleValue(text="Diktyoma, benign",
                                 description="Diktyoma, benign") )
        setattr(cls, "Malignant lymphoma, cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, cleaved cell, NOS",
                                 description="Malignant lymphoma, cleaved cell, NOS") )
        setattr(cls, "Micropapillary adenocarcinoma",
                PermissibleValue(text="Micropapillary adenocarcinoma",
                                 description="Micropapillary adenocarcinoma") )
        setattr(cls, "Mucinous cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Mucinous cystadenofibroma of borderline malignancy",
                                 description="Mucinous cystadenofibroma of borderline malignancy") )
        setattr(cls, "Intraductal papillary-mucinous neoplasm with moderate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous neoplasm with moderate dysplasia",
                                 description="Intraductal papillary-mucinous neoplasm with moderate dysplasia") )
        setattr(cls, "Serous cystadenofibroma, NOS",
                PermissibleValue(text="Serous cystadenofibroma, NOS",
                                 description="Serous cystadenofibroma, NOS") )
        setattr(cls, "Lepidic adenocarcinoma",
                PermissibleValue(text="Lepidic adenocarcinoma",
                                 description="Lepidic adenocarcinoma") )
        setattr(cls, "Infiltrating duct and cribriform carcinoma",
                PermissibleValue(text="Infiltrating duct and cribriform carcinoma",
                                 description="Infiltrating duct and cribriform carcinoma") )
        setattr(cls, "Adamantinoma, NOS",
                PermissibleValue(text="Adamantinoma, NOS",
                                 description="Adamantinoma, NOS") )
        setattr(cls, "Intraductal papilloma with ductal carcinoma in situ",
                PermissibleValue(text="Intraductal papilloma with ductal carcinoma in situ",
                                 description="Intraductal papilloma with ductal carcinoma in situ") )
        setattr(cls, "Atypical hyperplasia/Endometrioid intraepithelial neoplasm",
                PermissibleValue(text="Atypical hyperplasia/Endometrioid intraepithelial neoplasm",
                                 description="Atypical hyperplasia/Endometrioid intraepithelial neoplasm") )
        setattr(cls, "ACTH-producing tumor",
                PermissibleValue(text="ACTH-producing tumor",
                                 description="ACTH-producing tumor") )
        setattr(cls, "Mucinous tumor, NOS, of low malignant potential",
                PermissibleValue(text="Mucinous tumor, NOS, of low malignant potential",
                                 description="Mucinous tumor, NOS, of low malignant potential") )
        setattr(cls, "Fibrous papule of nose",
                PermissibleValue(text="Fibrous papule of nose",
                                 description="Fibrous papule of nose") )
        setattr(cls, "Monstrocellular sarcoma",
                PermissibleValue(text="Monstrocellular sarcoma",
                                 description="Monstrocellular sarcoma") )
        setattr(cls, "Embryonal rhabdomyosarcoma, pleomorphic",
                PermissibleValue(text="Embryonal rhabdomyosarcoma, pleomorphic",
                                 description="Embryonal rhabdomyosarcoma, pleomorphic") )
        setattr(cls, "Mucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Mucinous cystadenoma, borderline malignancy",
                                 description="Mucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Sertoli-Leydig cell tumor, sarcomatoid",
                PermissibleValue(text="Sertoli-Leydig cell tumor, sarcomatoid",
                                 description="Sertoli-Leydig cell tumor, sarcomatoid") )
        setattr(cls, "Atypical proliferating clear cell tumor",
                PermissibleValue(text="Atypical proliferating clear cell tumor",
                                 description="Atypical proliferating clear cell tumor") )
        setattr(cls, "Urothelial carcinoma with divergent differentiation",
                PermissibleValue(text="Urothelial carcinoma with divergent differentiation",
                                 description="Urothelial carcinoma with divergent differentiation") )
        setattr(cls, "Renomedullary fibroma",
                PermissibleValue(text="Renomedullary fibroma",
                                 description="Renomedullary fibroma") )
        setattr(cls, "Large granular lymphocytosis, NOS",
                PermissibleValue(text="Large granular lymphocytosis, NOS",
                                 description="Large granular lymphocytosis, NOS") )
        setattr(cls, "Mucinous cystic neoplasm with an associated invasive carcinoma",
                PermissibleValue(text="Mucinous cystic neoplasm with an associated invasive carcinoma",
                                 description="Mucinous cystic neoplasm with an associated invasive carcinoma") )
        setattr(cls, "Follicular carcinoma, moderately differentiated",
                PermissibleValue(text="Follicular carcinoma, moderately differentiated",
                                 description="Follicular carcinoma, moderately differentiated") )
        setattr(cls, "Glucagon-like peptide-producing tumor",
                PermissibleValue(text="Glucagon-like peptide-producing tumor",
                                 description="Glucagon-like peptide-producing tumor") )
        setattr(cls, "Columnar cell papilloma",
                PermissibleValue(text="Columnar cell papilloma",
                                 description="Columnar cell papilloma") )
        setattr(cls, "Intraductal papillary-mucinous tumor with low grade dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with low grade dysplasia",
                                 description="Intraductal papillary-mucinous tumor with low grade dysplasia") )
        setattr(cls, "Pseudomucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Pseudomucinous cystadenoma, borderline malignancy",
                                 description="Pseudomucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Flat intraepithelial neoplasia, high grade",
                PermissibleValue(text="Flat intraepithelial neoplasia, high grade",
                                 description="Flat intraepithelial neoplasia, high grade") )
        setattr(cls, "Alpha cell tumor, NOS",
                PermissibleValue(text="Alpha cell tumor, NOS",
                                 description="Alpha cell tumor, NOS") )
        setattr(cls, "Malignant fibrous histiocytoma (MFH) of bone",
                PermissibleValue(text="Malignant fibrous histiocytoma (MFH) of bone",
                                 description="Malignant fibrous histiocytoma (MFH) of bone") )
        setattr(cls, "Biliary intraepithelial neoplasia, high grade",
                PermissibleValue(text="Biliary intraepithelial neoplasia, high grade",
                                 description="Biliary intraepithelial neoplasia, high grade") )
        setattr(cls, "Adenomatosis, NOS",
                PermissibleValue(text="Adenomatosis, NOS",
                                 description="Adenomatosis, NOS") )
        setattr(cls, "Mucinous cystic neoplasm with low-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with low-grade intraepithelial neoplasia",
                                 description="Mucinous cystic neoplasm with low-grade intraepithelial neoplasia") )
        setattr(cls, "Mucinous cystic tumor with intermediate dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with intermediate dysplasia",
                                 description="Mucinous cystic tumor with intermediate dysplasia") )
        setattr(cls, "Mucinous cystic neoplasm with high-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with high-grade intraepithelial neoplasia",
                                 description="Mucinous cystic neoplasm with high-grade intraepithelial neoplasia") )
        setattr(cls, "Periosteal sarcoma, NOS",
                PermissibleValue(text="Periosteal sarcoma, NOS",
                                 description="Periosteal sarcoma, NOS") )
        setattr(cls, "Nonlipid reticuloendotheliosis",
                PermissibleValue(text="Nonlipid reticuloendotheliosis",
                                 description="Nonlipid reticuloendotheliosis") )
        setattr(cls, "Splenic lymphoma with villous lymphocytes",
                PermissibleValue(text="Splenic lymphoma with villous lymphocytes",
                                 description="Splenic lymphoma with villous lymphocytes") )
        setattr(cls, "Neurotropic melanoma, malignant",
                PermissibleValue(text="Neurotropic melanoma, malignant",
                                 description="Neurotropic melanoma, malignant") )
        setattr(cls, "Intraductal tubular-papillary neoplasm, low grade",
                PermissibleValue(text="Intraductal tubular-papillary neoplasm, low grade",
                                 description="Intraductal tubular-papillary neoplasm, low grade") )
        setattr(cls, "Mucinous carcinoid",
                PermissibleValue(text="Mucinous carcinoid",
                                 description="Mucinous carcinoid") )
        setattr(cls, "Mucinous cystic tumor with an associated invasive carcinoma",
                PermissibleValue(text="Mucinous cystic tumor with an associated invasive carcinoma",
                                 description="Mucinous cystic tumor with an associated invasive carcinoma") )
        setattr(cls, "Metaplastic carcinoma with osseous differentiation",
                PermissibleValue(text="Metaplastic carcinoma with osseous differentiation",
                                 description="Metaplastic carcinoma with osseous differentiation") )
        setattr(cls, "Metastasizing leiomyoma",
                PermissibleValue(text="Metastasizing leiomyoma",
                                 description="Metastasizing leiomyoma") )
        setattr(cls, "Aleukemic myeloid leukemia",
                PermissibleValue(text="Aleukemic myeloid leukemia",
                                 description="Aleukemic myeloid leukemia") )
        setattr(cls, "Embryonal carcinoma, polyembryonal type",
                PermissibleValue(text="Embryonal carcinoma, polyembryonal type",
                                 description="Embryonal carcinoma, polyembryonal type") )
        setattr(cls, "Aleukemic granulocytic leukemia",
                PermissibleValue(text="Aleukemic granulocytic leukemia",
                                 description="Aleukemic granulocytic leukemia") )
        setattr(cls, "Intraductal papilloma with lobular carcinoma in situ",
                PermissibleValue(text="Intraductal papilloma with lobular carcinoma in situ",
                                 description="Intraductal papilloma with lobular carcinoma in situ") )
        setattr(cls, "Intraductal papillary-mucinous tumor with moderate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with moderate dysplasia",
                                 description="Intraductal papillary-mucinous tumor with moderate dysplasia") )
        setattr(cls, "Intracystic papillary tumor with high grade dysplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade dysplasia",
                                 description="Intracystic papillary tumor with high grade dysplasia") )
        setattr(cls, "Chondrosarcoma grade 2/3",
                PermissibleValue(text="Chondrosarcoma grade 2/3",
                                 description="Chondrosarcoma grade 2/3") )
        setattr(cls, "Lipid-rich Sertoli cell tumor",
                PermissibleValue(text="Lipid-rich Sertoli cell tumor",
                                 description="Lipid-rich Sertoli cell tumor") )
        setattr(cls, "Mucinous cystic neoplasm with intermediate-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with intermediate-grade intraepithelial neoplasia",
                                 description="Mucinous cystic neoplasm with intermediate-grade intraepithelial neoplasia") )
        setattr(cls, "Involuting nevus",
                PermissibleValue(text="Involuting nevus",
                                 description="Involuting nevus") )
        setattr(cls, "Endometrioid cystadenofibroma, malignant",
                PermissibleValue(text="Endometrioid cystadenofibroma, malignant",
                                 description="Endometrioid cystadenofibroma, malignant") )
        setattr(cls, "Mixed embryonal rhabdomyosarcoma and alveolar rhabdomyosarcoma",
                PermissibleValue(text="Mixed embryonal rhabdomyosarcoma and alveolar rhabdomyosarcoma",
                                 description="Mixed embryonal rhabdomyosarcoma and alveolar rhabdomyosarcoma") )
        setattr(cls, "Mesothelial papilloma",
                PermissibleValue(text="Mesothelial papilloma",
                                 description="Mesothelial papilloma") )
        setattr(cls, "Adult rhabdomyoma",
                PermissibleValue(text="Adult rhabdomyoma",
                                 description="Adult rhabdomyoma") )
        setattr(cls, "Subacute lymphatic leukemia",
                PermissibleValue(text="Subacute lymphatic leukemia",
                                 description="Subacute lymphatic leukemia") )
        setattr(cls, "Glucagonoma, NOS",
                PermissibleValue(text="Glucagonoma, NOS",
                                 description="Glucagonoma, NOS") )
        setattr(cls, "Flat intraepithelial glandular neoplasia, high grade",
                PermissibleValue(text="Flat intraepithelial glandular neoplasia, high grade",
                                 description="Flat intraepithelial glandular neoplasia, high grade") )
        setattr(cls, "Typical carcinoid",
                PermissibleValue(text="Typical carcinoid",
                                 description="Typical carcinoid") )
        setattr(cls, "Malignant lymphoma, undifferentiated cell type, NOS",
                PermissibleValue(text="Malignant lymphoma, undifferentiated cell type, NOS",
                                 description="Malignant lymphoma, undifferentiated cell type, NOS") )
        setattr(cls, "Low-grade serous carcinoma",
                PermissibleValue(text="Low-grade serous carcinoma",
                                 description="Low-grade serous carcinoma") )
        setattr(cls, "Subacute leukemia, NOS",
                PermissibleValue(text="Subacute leukemia, NOS",
                                 description="Subacute leukemia, NOS") )
        setattr(cls, "Granulosa cell tumor, sarcomatoid",
                PermissibleValue(text="Granulosa cell tumor, sarcomatoid",
                                 description="Granulosa cell tumor, sarcomatoid") )
        setattr(cls, "Argentaffinoma, malignant",
                PermissibleValue(text="Argentaffinoma, malignant",
                                 description="Argentaffinoma, malignant") )
        setattr(cls, "Malignant mucinous adenofibroma",
                PermissibleValue(text="Malignant mucinous adenofibroma",
                                 description="Malignant mucinous adenofibroma") )
        setattr(cls, "Intraductal papillary-mucinous neoplasm with low grade dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous neoplasm with low grade dysplasia",
                                 description="Intraductal papillary-mucinous neoplasm with low grade dysplasia") )
        setattr(cls, "Intratubular germ cell neoplasia",
                PermissibleValue(text="Intratubular germ cell neoplasia",
                                 description="Intratubular germ cell neoplasia") )
        setattr(cls, "Fibromatosis-like metaplastic carcinoma",
                PermissibleValue(text="Fibromatosis-like metaplastic carcinoma",
                                 description="Fibromatosis-like metaplastic carcinoma") )
        setattr(cls, "Villous papilloma",
                PermissibleValue(text="Villous papilloma",
                                 description="Villous papilloma") )
        setattr(cls, "Non-invasive low grade serous carcinoma",
                PermissibleValue(text="Non-invasive low grade serous carcinoma",
                                 description="Non-invasive low grade serous carcinoma") )
        setattr(cls, "Glycogenic rhabdomyoma",
                PermissibleValue(text="Glycogenic rhabdomyoma",
                                 description="Glycogenic rhabdomyoma") )
        setattr(cls, "Papillary adenocarcinoma, follicular variant",
                PermissibleValue(text="Papillary adenocarcinoma, follicular variant",
                                 description="Papillary adenocarcinoma, follicular variant") )
        setattr(cls, "Follicular carcinoma, encapsulated",
                PermissibleValue(text="Follicular carcinoma, encapsulated",
                                 description="Follicular carcinoma, encapsulated") )
        setattr(cls, "Well differentiated papillary mesothelioma, benign",
                PermissibleValue(text="Well differentiated papillary mesothelioma, benign",
                                 description="Well differentiated papillary mesothelioma, benign") )
        setattr(cls, "Malignant lymphoma, undifferentiated cell, non-Burkitt",
                PermissibleValue(text="Malignant lymphoma, undifferentiated cell, non-Burkitt",
                                 description="Malignant lymphoma, undifferentiated cell, non-Burkitt") )
        setattr(cls, "Mucinous cystic tumor with low grade dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with low grade dysplasia",
                                 description="Mucinous cystic tumor with low grade dysplasia") )
        setattr(cls, "Serous cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Serous cystadenofibroma of borderline malignancy",
                                 description="Serous cystadenofibroma of borderline malignancy") )
        setattr(cls, "Papillary carcinoma, encapsulated",
                PermissibleValue(text="Papillary carcinoma, encapsulated",
                                 description="Papillary carcinoma, encapsulated") )
        setattr(cls, "Solid adenocarcinoma with mucin formation",
                PermissibleValue(text="Solid adenocarcinoma with mucin formation",
                                 description="Solid adenocarcinoma with mucin formation") )
        setattr(cls, "Primary intraosseous carcinoma",
                PermissibleValue(text="Primary intraosseous carcinoma",
                                 description="Primary intraosseous carcinoma") )
        setattr(cls, "MPNST with glandular differentiation",
                PermissibleValue(text="MPNST with glandular differentiation",
                                 description="MPNST with glandular differentiation") )
        setattr(cls, "PP/PYY producing tumor",
                PermissibleValue(text="PP/PYY producing tumor",
                                 description="PP/PYY producing tumor") )
        setattr(cls, "Myelomonocytic leukemia, NOS",
                PermissibleValue(text="Myelomonocytic leukemia, NOS",
                                 description="Myelomonocytic leukemia, NOS") )
        setattr(cls, "Composite Hodgkin and non-Hodgkin lymphoma",
                PermissibleValue(text="Composite Hodgkin and non-Hodgkin lymphoma",
                                 description="Composite Hodgkin and non-Hodgkin lymphoma") )
        setattr(cls, "Follicular adenocarcinoma, moderately differentiated",
                PermissibleValue(text="Follicular adenocarcinoma, moderately differentiated",
                                 description="Follicular adenocarcinoma, moderately differentiated") )
        setattr(cls, "Primitive polar spongioblastoma",
                PermissibleValue(text="Primitive polar spongioblastoma",
                                 description="Primitive polar spongioblastoma") )
        setattr(cls, "Peripheral T-cell lymphoma, pleomorphic small cell",
                PermissibleValue(text="Peripheral T-cell lymphoma, pleomorphic small cell",
                                 description="Peripheral T-cell lymphoma, pleomorphic small cell") )
        setattr(cls, "Neuroendocrine tumor, grade 2",
                PermissibleValue(text="Neuroendocrine tumor, grade 2",
                                 description="Neuroendocrine tumor, grade 2") )
        setattr(cls, "Subacute lymphoid leukemia",
                PermissibleValue(text="Subacute lymphoid leukemia",
                                 description="Subacute lymphoid leukemia") )
        setattr(cls, "Cystic mesothelioma, benign",
                PermissibleValue(text="Cystic mesothelioma, benign",
                                 description="Cystic mesothelioma, benign") )
        setattr(cls, "Syringadenoma, NOS",
                PermissibleValue(text="Syringadenoma, NOS",
                                 description="Syringadenoma, NOS") )
        setattr(cls, "Plexiform leiomyoma",
                PermissibleValue(text="Plexiform leiomyoma",
                                 description="Plexiform leiomyoma") )
        setattr(cls, "Chronic myelomonocytic leukemia, Type 1",
                PermissibleValue(text="Chronic myelomonocytic leukemia, Type 1",
                                 description="Chronic myelomonocytic leukemia, Type 1") )
        setattr(cls, "Intracystic papillary tumor with high grade entraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade entraepithelial neoplasia",
                                 description="Intracystic papillary tumor with high grade entraepithelial neoplasia") )
        setattr(cls, "Intracystic papillary neoplasm with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary neoplasm with high grade intraepithelial neoplasia",
                                 description="Intracystic papillary neoplasm with high grade intraepithelial neoplasia") )
        setattr(cls, "High-grade serous carcinoma",
                PermissibleValue(text="High-grade serous carcinoma",
                                 description="High-grade serous carcinoma") )
        setattr(cls, "Biliary intraepithelial neoplasia, low grade",
                PermissibleValue(text="Biliary intraepithelial neoplasia, low grade",
                                 description="Biliary intraepithelial neoplasia, low grade") )
        setattr(cls, "Anaplastic large cell lymphoma, T cell and Null cell type",
                PermissibleValue(text="Anaplastic large cell lymphoma, T cell and Null cell type",
                                 description="Anaplastic large cell lymphoma, T cell and Null cell type") )
        setattr(cls, "Mixed invasive mucinous and non-mucinous adenocarcinoma",
                PermissibleValue(text="Mixed invasive mucinous and non-mucinous adenocarcinoma",
                                 description="Mixed invasive mucinous and non-mucinous adenocarcinoma") )
        setattr(cls, "Mucinous cystic neoplasm with low-grade dysplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with low-grade dysplasia",
                                 description="Mucinous cystic neoplasm with low-grade dysplasia") )
        setattr(cls, "Intravascular bronchial alveolar tumor",
                PermissibleValue(text="Intravascular bronchial alveolar tumor",
                                 description="Intravascular bronchial alveolar tumor") )
        setattr(cls, "Pancreatic peptide and pancreatic peptide-like peptide within terminal tyrosine amide producing tumor",
                PermissibleValue(text="Pancreatic peptide and pancreatic peptide-like peptide within terminal tyrosine amide producing tumor",
                                 description="Pancreatic peptide and pancreatic peptide-like peptide within terminal tyrosine amide producing tumor") )
        setattr(cls, "Malignant lymphoma, small cleaved cell, diffuse",
                PermissibleValue(text="Malignant lymphoma, small cleaved cell, diffuse",
                                 description="Malignant lymphoma, small cleaved cell, diffuse") )
        setattr(cls, "Aleukemic monocytic leukemia",
                PermissibleValue(text="Aleukemic monocytic leukemia",
                                 description="Aleukemic monocytic leukemia") )
        setattr(cls, "Subacute monocytic leukemia",
                PermissibleValue(text="Subacute monocytic leukemia",
                                 description="Subacute monocytic leukemia") )
        setattr(cls, "Intraductal papillary neoplasm with high grade dysplasia",
                PermissibleValue(text="Intraductal papillary neoplasm with high grade dysplasia",
                                 description="Intraductal papillary neoplasm with high grade dysplasia") )
        setattr(cls, "Malignant lymphoma, centrocytic",
                PermissibleValue(text="Malignant lymphoma, centrocytic",
                                 description="Malignant lymphoma, centrocytic") )
        setattr(cls, "Tubular androblastoma with lipid storage",
                PermissibleValue(text="Tubular androblastoma with lipid storage",
                                 description="Tubular androblastoma with lipid storage") )
        setattr(cls, "Carcinoma with other types mesenchymal differentiation",
                PermissibleValue(text="Carcinoma with other types mesenchymal differentiation",
                                 description="Carcinoma with other types mesenchymal differentiation") )
        setattr(cls, "Mixed pineal tumor",
                PermissibleValue(text="Mixed pineal tumor",
                                 description="Mixed pineal tumor") )
        setattr(cls, "Intracystic papillary tumor with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade intraepithelial neoplasia",
                                 description="Intracystic papillary tumor with high grade intraepithelial neoplasia") )
        setattr(cls, "Malignant lymphoma, small cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, small cleaved cell, NOS",
                                 description="Malignant lymphoma, small cleaved cell, NOS") )
        setattr(cls, "Malignant lymphoma, small cell, noncleaved, diffuse",
                PermissibleValue(text="Malignant lymphoma, small cell, noncleaved, diffuse",
                                 description="Malignant lymphoma, small cell, noncleaved, diffuse") )
        setattr(cls, "Intracystic papillary neoplasm with associated invasive carcinoma",
                PermissibleValue(text="Intracystic papillary neoplasm with associated invasive carcinoma",
                                 description="Intracystic papillary neoplasm with associated invasive carcinoma") )
        setattr(cls, "Intraductal papillary tumor with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intraductal papillary tumor with high grade intraepithelial neoplasia",
                                 description="Intraductal papillary tumor with high grade intraepithelial neoplasia") )
        setattr(cls, "Malignant lymphoma, lymphocytic, intermediate differentiation, nodular",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, intermediate differentiation, nodular",
                                 description="Malignant lymphoma, lymphocytic, intermediate differentiation, nodular") )
        setattr(cls, "Intermediate and giant congenital nevus",
                PermissibleValue(text="Intermediate and giant congenital nevus",
                                 description="Intermediate and giant congenital nevus") )
        setattr(cls, "Bronchial adenoma, carcinoid",
                PermissibleValue(text="Bronchial adenoma, carcinoid",
                                 description="Bronchial adenoma, carcinoid") )
        setattr(cls, "Cribriform comedo-type carcinoma",
                PermissibleValue(text="Cribriform comedo-type carcinoma",
                                 description="Cribriform comedo-type carcinoma") )
        setattr(cls, "Polymorphic reticulosis",
                PermissibleValue(text="Polymorphic reticulosis",
                                 description="Polymorphic reticulosis") )
        setattr(cls, "Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)",
                PermissibleValue(text="Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)",
                                 description="Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)") )
        setattr(cls, "Invasive carcinoma, NST",
                PermissibleValue(text="Invasive carcinoma, NST",
                                 description="Invasive carcinoma, NST") )
        setattr(cls, "B cell lymphoma, NOS",
                PermissibleValue(text="B cell lymphoma, NOS",
                                 description="B cell lymphoma, NOS") )
        setattr(cls, "EC cell carcinoid",
                PermissibleValue(text="EC cell carcinoid",
                                 description="EC cell carcinoid") )
        setattr(cls, "Hepatoblastoma, epithelioid",
                PermissibleValue(text="Hepatoblastoma, epithelioid",
                                 description="Hepatoblastoma, epithelioid") )
        setattr(cls, "Classical Hodgkin lymphoma, lymphocyte depletion, reticular",
                PermissibleValue(text="Classical Hodgkin lymphoma, lymphocyte depletion, reticular",
                                 description="Classical Hodgkin lymphoma, lymphocyte depletion, reticular") )
        setattr(cls, "Bronchial adenoma, cylindroid",
                PermissibleValue(text="Bronchial adenoma, cylindroid",
                                 description="Bronchial adenoma, cylindroid") )
        setattr(cls, "Mixed pineocytoma-pineoblastoma",
                PermissibleValue(text="Mixed pineocytoma-pineoblastoma",
                                 description="Mixed pineocytoma-pineoblastoma") )
        setattr(cls, "Intraductal tubular-papillary neoplasm, high grade",
                PermissibleValue(text="Intraductal tubular-papillary neoplasm, high grade",
                                 description="Intraductal tubular-papillary neoplasm, high grade") )
        setattr(cls, "Mucinous cystic tumor with high-grade dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with high-grade dysplasia",
                                 description="Mucinous cystic tumor with high-grade dysplasia") )
        setattr(cls, "Mixed type rhabdomyosarcoma",
                PermissibleValue(text="Mixed type rhabdomyosarcoma",
                                 description="Mixed type rhabdomyosarcoma") )
        setattr(cls, "Carcinoid tumor, argentaffin, malignant",
                PermissibleValue(text="Carcinoid tumor, argentaffin, malignant",
                                 description="Carcinoid tumor, argentaffin, malignant") )
        setattr(cls, "Angioblastic meningioma",
                PermissibleValue(text="Angioblastic meningioma",
                                 description="Angioblastic meningioma") )
        setattr(cls, "Intravascular leiomyomatosis",
                PermissibleValue(text="Intravascular leiomyomatosis",
                                 description="Intravascular leiomyomatosis") )
        setattr(cls, "Intraductal papillary tumor with high grade dysplasia",
                PermissibleValue(text="Intraductal papillary tumor with high grade dysplasia",
                                 description="Intraductal papillary tumor with high grade dysplasia") )
        setattr(cls, "Malignant mucinous cystadenofibroma",
                PermissibleValue(text="Malignant mucinous cystadenofibroma",
                                 description="Malignant mucinous cystadenofibroma") )
        setattr(cls, "Chronic erythremia",
                PermissibleValue(text="Chronic erythremia",
                                 description="Chronic erythremia") )
        setattr(cls, "Malignant myelosclerosis",
                PermissibleValue(text="Malignant myelosclerosis",
                                 description="Malignant myelosclerosis") )
        setattr(cls, "Infiltrating duct and tubular carcinoma",
                PermissibleValue(text="Infiltrating duct and tubular carcinoma",
                                 description="Infiltrating duct and tubular carcinoma") )
        setattr(cls, "Mucinous cystic neoplasm with intermediate-grade dysplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with intermediate-grade dysplasia",
                                 description="Mucinous cystic neoplasm with intermediate-grade dysplasia") )
        setattr(cls, "Chronic myelomonocytic leukemia, Type II",
                PermissibleValue(text="Chronic myelomonocytic leukemia, Type II",
                                 description="Chronic myelomonocytic leukemia, Type II") )
        setattr(cls, "Non-invasive mammary carcinoma",
                PermissibleValue(text="Non-invasive mammary carcinoma",
                                 description="Non-invasive mammary carcinoma") )
        setattr(cls, "Mammary carcinoma, in situ",
                PermissibleValue(text="Mammary carcinoma, in situ",
                                 description="Mammary carcinoma, in situ") )
        setattr(cls, "Malignant midline reticulosis",
                PermissibleValue(text="Malignant midline reticulosis",
                                 description="Malignant midline reticulosis") )
        setattr(cls, "Malignant lymphoma, lymphocytic, well differentiated, nodular",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, well differentiated, nodular",
                                 description="Malignant lymphoma, lymphocytic, well differentiated, nodular") )
        setattr(cls, "Inflammatory adenocarcinoma",
                PermissibleValue(text="Inflammatory adenocarcinoma",
                                 description="Inflammatory adenocarcinoma") )
        setattr(cls, "Peripheral T-cell lymphoma, pleomorphic medium and large cell",
                PermissibleValue(text="Peripheral T-cell lymphoma, pleomorphic medium and large cell",
                                 description="Peripheral T-cell lymphoma, pleomorphic medium and large cell") )
        setattr(cls, "Sertoli-Leydig cell tumor, retiform, with heterologous elements",
                PermissibleValue(text="Sertoli-Leydig cell tumor, retiform, with heterologous elements",
                                 description="Sertoli-Leydig cell tumor, retiform, with heterologous elements") )
        setattr(cls, "Intraductal carcinoma, solid type",
                PermissibleValue(text="Intraductal carcinoma, solid type",
                                 description="Intraductal carcinoma, solid type") )
        setattr(cls, "Spongioblastoma, NOS",
                PermissibleValue(text="Spongioblastoma, NOS",
                                 description="Spongioblastoma, NOS") )
        setattr(cls, "Malignant serous adenofibroma",
                PermissibleValue(text="Malignant serous adenofibroma",
                                 description="Malignant serous adenofibroma") )
        setattr(cls, "Follicular carcinoma, trabecular",
                PermissibleValue(text="Follicular carcinoma, trabecular",
                                 description="Follicular carcinoma, trabecular") )
        setattr(cls, "Subependymal astrocytoma, NOS",
                PermissibleValue(text="Subependymal astrocytoma, NOS",
                                 description="Subependymal astrocytoma, NOS") )
        setattr(cls, "NK-cell large granular lymphocytic leukemia",
                PermissibleValue(text="NK-cell large granular lymphocytic leukemia",
                                 description="NK-cell large granular lymphocytic leukemia") )
        setattr(cls, "Islet cell tumor, benign",
                PermissibleValue(text="Islet cell tumor, benign",
                                 description="Islet cell tumor, benign") )
        setattr(cls, "Refractory anemia without sideroblasts",
                PermissibleValue(text="Refractory anemia without sideroblasts",
                                 description="Refractory anemia without sideroblasts") )
        setattr(cls, "L-cell tumor",
                PermissibleValue(text="L-cell tumor",
                                 description="L-cell tumor") )
        setattr(cls, "Medullary adenocarcinoma",
                PermissibleValue(text="Medullary adenocarcinoma",
                                 description="Medullary adenocarcinoma") )
        setattr(cls, "Malignant lymphoma, lymphocytic, poorly differentiated, diffuse",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, poorly differentiated, diffuse",
                                 description="Malignant lymphoma, lymphocytic, poorly differentiated, diffuse") )
        setattr(cls, "Subacute lymphocytic leukemia",
                PermissibleValue(text="Subacute lymphocytic leukemia",
                                 description="Subacute lymphocytic leukemia") )
        setattr(cls, "Ductal carcinoma in situ, micropapillary",
                PermissibleValue(text="Ductal carcinoma in situ, micropapillary",
                                 description="Ductal carcinoma in situ, micropapillary") )
        setattr(cls, "Primary diffuse large B-cell lymphoma of the CNS",
                PermissibleValue(text="Primary diffuse large B-cell lymphoma of the CNS",
                                 description="Primary diffuse large B-cell lymphoma of the CNS") )
        setattr(cls, "Round cell sarcoma",
                PermissibleValue(text="Round cell sarcoma",
                                 description="Round cell sarcoma") )

class EnumCRDC-H.Diagnosis.morphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis morphology
    """
    C45747 = PermissibleValue(text="C45747",
                                   description="Adult Cardiac Cellular Rhabdomyoma",
                                   meaning=NCIT.C45747)
    C5241 = PermissibleValue(text="C5241",
                                 description="Mixed Germ Cell-Sex Cord-Stromal Tumor",
                                 meaning=NCIT.C5241)
    C167335 = PermissibleValue(text="C167335",
                                     description="Glioblastoma, IDH-Mutant",
                                     meaning=NCIT.C167335)
    C3176 = PermissibleValue(text="C3176",
                                 description="Philadelphia-Negative Myelogenous Leukemia",
                                 meaning=NCIT.C3176)
    C129442 = PermissibleValue(text="C129442",
                                     description="Medulloblastoma, SHH-Activated, TP53-Mutant",
                                     meaning=NCIT.C129442)
    C129351 = PermissibleValue(text="C129351",
                                     description="Ependymoma, RELA Fusion-Positive",
                                     meaning=NCIT.C129351)
    C66746 = PermissibleValue(text="C66746",
                                   description="Benign Thymoma",
                                   meaning=NCIT.C66746)
    C4180 = PermissibleValue(text="C4180",
                                 description="Papillary Serous Cystadenoma",
                                 meaning=NCIT.C4180)
    C40182 = PermissibleValue(text="C40182",
                                   description="Uterine Corpus Carcinofibroma",
                                   meaning=NCIT.C40182)
    C53677 = PermissibleValue(text="C53677",
                                   description="Intimal Sarcoma",
                                   meaning=NCIT.C53677)
    C164250 = PermissibleValue(text="C164250",
                                     description="Human Papillomavirus-Negative Squamous Cell Carcinoma",
                                     meaning=NCIT.C164250)
    C162848 = PermissibleValue(text="C162848",
                                     description="Digital Papillary Adenoma",
                                     meaning=NCIT.C162848)
    C66764 = PermissibleValue(text="C66764",
                                   description="Fascial Fibroma",
                                   meaning=NCIT.C66764)
    C66953 = PermissibleValue(text="C66953",
                                   description="Mucinous Adenocarcinoma, Endocervical Type",
                                   meaning=NCIT.C66953)
    C40173 = PermissibleValue(text="C40173",
                                   description="Benign Metastasizing Leiomyoma of the Uterine Corpus",
                                   meaning=NCIT.C40173)
    C65196 = PermissibleValue(text="C65196",
                                   description="Carcinoid Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C65196)
    C65189 = PermissibleValue(text="C65189",
                                   description="Malignant Vipoma",
                                   meaning=NCIT.C65189)
    C94759 = PermissibleValue(text="C94759",
                                   description="Functioning Endocrine Neoplasm",
                                   meaning=NCIT.C94759)
    C82594 = PermissibleValue(text="C82594",
                                   description="Refractory Thrombocytopenia",
                                   meaning=NCIT.C82594)
    C82593 = PermissibleValue(text="C82593",
                                   description="Refractory Neutropenia",
                                   meaning=NCIT.C82593)
    C79951 = PermissibleValue(text="C79951",
                                   description="Papillary Adenoma",
                                   meaning=NCIT.C79951)
    C84276 = PermissibleValue(text="C84276",
                                   description="Myeloid/Lymphoid Neoplasms with PDGFRB Rearrangement",
                                   meaning=NCIT.C84276)
    C7315 = PermissibleValue(text="C7315",
                                 description="Borderline Ovarian Serous Surface Papillary Tumor",
                                 meaning=NCIT.C7315)
    C4311 = PermissibleValue(text="C4311",
                                 description="Ghost Cell Odontogenic Carcinoma",
                                 meaning=NCIT.C4311)
    C4259 = PermissibleValue(text="C4259",
                                 description="Rhabdomyosarcoma with Mixed Embryonal and Alveolar Features",
                                 meaning=NCIT.C4259)
    C39812 = PermissibleValue(text="C39812",
                                   description="Metanephric Adenofibroma",
                                   meaning=NCIT.C39812)
    C129309 = PermissibleValue(text="C129309",
                                     description="Diffuse Midline Glioma, H3 K27M-Mutant",
                                     meaning=NCIT.C129309)
    C66756 = PermissibleValue(text="C66756",
                                   description="Mixed Epithelioid and Spindle Cell Melanoma",
                                   meaning=NCIT.C66756)
    C7183 = PermissibleValue(text="C7183",
                                 description="Polymorphic Post-Transplant Lymphoproliferative Disorder",
                                 meaning=NCIT.C7183)
    C7695 = PermissibleValue(text="C7695",
                                 description="Primary Peritoneal Serous Papillary Adenocarcinoma",
                                 meaning=NCIT.C7695)
    C5143 = PermissibleValue(text="C5143",
                                 description="Malignant Breast Adenomyoepithelioma",
                                 meaning=NCIT.C5143)
    C41245 = PermissibleValue(text="C41245",
                                   description="Pancreatic Non-Invasive Mucinous Cystadenocarcinoma",
                                   meaning=NCIT.C41245)
    C164205 = PermissibleValue(text="C164205",
                                     description="Biphenotypic Sinonasal Sarcoma",
                                     meaning=NCIT.C164205)
    C36084 = PermissibleValue(text="C36084",
                                   description="Invasive Breast Micropapillary Carcinoma",
                                   meaning=NCIT.C36084)
    C66754 = PermissibleValue(text="C66754",
                                   description="Small Congenital Melanocytic Nevus",
                                   meaning=NCIT.C66754)
    C4300 = PermissibleValue(text="C4300",
                                 description="Benign Hemangiopericytoma",
                                 meaning=NCIT.C4300)
    C95597 = PermissibleValue(text="C95597",
                                   description="Pancreatic Glucagonoma",
                                   meaning=NCIT.C95597)
    C3087 = PermissibleValue(text="C3087",
                                 description="Hemangiopericytoma",
                                 meaning=NCIT.C3087)
    C7612 = PermissibleValue(text="C7612",
                                 description="Malignant Thymoma",
                                 meaning=NCIT.C7612)
    C4301 = PermissibleValue(text="C4301",
                                 description="Malignant Hemangiopericytoma",
                                 meaning=NCIT.C4301)
    C164255 = PermissibleValue(text="C164255",
                                     description="Mixed Neuroendocrine Non-Neuroendocrine Neoplasm",
                                     meaning=NCIT.C164255)
    C48314 = PermissibleValue(text="C48314",
                                   description="Benign Paraganglioma",
                                   meaning=NCIT.C48314)
    C164145 = PermissibleValue(text="C164145",
                                     description="Hodgkin's Sarcoma",
                                     meaning=NCIT.C164145)
    C37869 = PermissibleValue(text="C37869",
                                   description="B-Cell Lymphoma, Unclassifiable, with Features Intermediate between Diffuse Large B-Cell Lymphoma and Classic Hodgkin Lymphoma",
                                   meaning=NCIT.C37869)
    C162973 = PermissibleValue(text="C162973",
                                     description="Non-Invasive Cribriform Carcinoma",
                                     meaning=NCIT.C162973)
    C8868 = PermissibleValue(text="C8868",
                                 description="B Lymphoblastic Lymphoma",
                                 meaning=NCIT.C8868)
    C4233 = PermissibleValue(text="C4233",
                                 description="Precancerous Melanosis",
                                 meaning=NCIT.C4233)
    C40164 = PermissibleValue(text="C40164",
                                   description="Uterine Corpus Epithelioid Leiomyoma",
                                   meaning=NCIT.C40164)
    C36122 = PermissibleValue(text="C36122",
                                   description="Benign Cellular Infiltrate",
                                   meaning=NCIT.C36122)
    C66815 = PermissibleValue(text="C66815",
                                   description="Diffuse Retinoblastoma",
                                   meaning=NCIT.C66815)
    C66779 = PermissibleValue(text="C66779",
                                   description="Benign Hemangioendothelioma",
                                   meaning=NCIT.C66779)
    C66772 = PermissibleValue(text="C66772",
                                   description="Benign Stromal Tumor",
                                   meaning=NCIT.C66772)
    C67090 = PermissibleValue(text="C67090",
                                   description="Serous Adenofibroma",
                                   meaning=NCIT.C67090)
    C66778 = PermissibleValue(text="C66778",
                                   description="Malignant Trophoblastic Teratoma",
                                   meaning=NCIT.C66778)
    C66803 = PermissibleValue(text="C66803",
                                   description="Cerebellar Sarcoma",
                                   meaning=NCIT.C66803)
    C8979 = PermissibleValue(text="C8979",
                                 description="Mucinous Cystadenofibroma",
                                 meaning=NCIT.C8979)
    C7363 = PermissibleValue(text="C7363",
                                 description="Intraductal Papillomatosis",
                                 meaning=NCIT.C7363)
    C7468 = PermissibleValue(text="C7468",
                                 description="Struma Ovarii",
                                 meaning=NCIT.C7468)
    C4309 = PermissibleValue(text="C4309",
                                 description="Complex Odontoma",
                                 meaning=NCIT.C4309)
    C4211 = PermissibleValue(text="C4211",
                                 description="Ovarian Sertoli Cell Tumor with Lipid Storage",
                                 meaning=NCIT.C4211)
    C39974 = PermissibleValue(text="C39974",
                                   description="Ovarian Sertoli-Leydig Cell Tumor with Retiform Elements",
                                   meaning=NCIT.C39974)
    C65182 = PermissibleValue(text="C65182",
                                   description="Micropapillary Transitional Cell Carcinoma",
                                   meaning=NCIT.C65182)
    C46095 = PermissibleValue(text="C46095",
                                   description="Solid/Trabecular Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C46095)
    C96485 = PermissibleValue(text="C96485",
                                   description="Colorectal Serrated Adenocarcinoma",
                                   meaning=NCIT.C96485)
    C92624 = PermissibleValue(text="C92624",
                                   description="Papillary Tumor of the Pineal Region",
                                   meaning=NCIT.C92624)
    C95914 = PermissibleValue(text="C95914",
                                   description="Ampullary Noninvasive Pancreatobiliary Papillary Neoplasm with Low Grade Dysplasia",
                                   meaning=NCIT.C95914)
    C95963 = PermissibleValue(text="C95963",
                                   description="Ampulla of Vater Pancreatobiliary Type Adenocarcinoma",
                                   meaning=NCIT.C95963)
    C3686 = PermissibleValue(text="C3686",
                                 description="Salivary Gland Monomorphic Adenoma",
                                 meaning=NCIT.C3686)
    C3711 = PermissibleValue(text="C3711",
                                 description="Compound Odontoma",
                                 meaning=NCIT.C3711)
    C2874 = PermissibleValue(text="C2874",
                                 description="Angiokeratoma",
                                 meaning=NCIT.C2874)
    C3190 = PermissibleValue(text="C3190",
                                 description="Linitis Plastica",
                                 meaning=NCIT.C3190)
    C129444 = PermissibleValue(text="C129444",
                                     description="Medulloblastoma, Non-WNT/Non-SHH",
                                     meaning=NCIT.C129444)
    C8376 = PermissibleValue(text="C8376",
                                 description="Adenocarcinoma In Situ in Villous Adenoma",
                                 meaning=NCIT.C8376)
    C80344 = PermissibleValue(text="C80344",
                                   description="Hyperdiploid B Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C80344)
    C66811 = PermissibleValue(text="C66811",
                                   description="Spongioneuroblastoma",
                                   meaning=NCIT.C66811)
    C67156 = PermissibleValue(text="C67156",
                                   description="Olfactory Neurocytoma",
                                   meaning=NCIT.C67156)
    C66796 = PermissibleValue(text="C66796",
                                   description="Aggressive Osteoblastoma",
                                   meaning=NCIT.C66796)
    C66951 = PermissibleValue(text="C66951",
                                   description="Adenocarcinoma, Endocervical Type",
                                   meaning=NCIT.C66951)
    C3153 = PermissibleValue(text="C3153",
                                 description="Krukenberg Tumor",
                                 meaning=NCIT.C3153)
    C66816 = PermissibleValue(text="C66816",
                                   description="Spontaneously Regressed Retinoblastoma",
                                   meaning=NCIT.C66816)
    C66718 = PermissibleValue(text="C66718",
                                   description="Medullary Carcinoma, Not Otherwise Specified",
                                   meaning=NCIT.C66718)
    C66763 = PermissibleValue(text="C66763",
                                   description="Periosteal Fibrosarcoma",
                                   meaning=NCIT.C66763)
    C66752 = PermissibleValue(text="C66752",
                                   description="Clear Cell Neoplasm",
                                   meaning=NCIT.C66752)
    C66771 = PermissibleValue(text="C66771",
                                   description="Angiomyosarcoma",
                                   meaning=NCIT.C66771)
    C66804 = PermissibleValue(text="C66804",
                                   description="Ganglioneuromatosis",
                                   meaning=NCIT.C66804)
    C66813 = PermissibleValue(text="C66813",
                                   description="Differentiated Retinoblastoma",
                                   meaning=NCIT.C66813)
    C66817 = PermissibleValue(text="C66817",
                                   description="Hemangioblastic Meningioma",
                                   meaning=NCIT.C66817)
    C66799 = PermissibleValue(text="C66799",
                                   description="Metastasizing Chondroblastoma",
                                   meaning=NCIT.C66799)
    C66814 = PermissibleValue(text="C66814",
                                   description="Undifferentiated Retinoblastoma",
                                   meaning=NCIT.C66814)
    C66903 = PermissibleValue(text="C66903",
                                   description="Skin Metatypical Carcinoma",
                                   meaning=NCIT.C66903)
    C67092 = PermissibleValue(text="C67092",
                                   description="Ovarian Serous Adenocarcinofibroma",
                                   meaning=NCIT.C67092)
    C66757 = PermissibleValue(text="C66757",
                                   description="Epithelioid Cell Nevus",
                                   meaning=NCIT.C66757)
    C66765 = PermissibleValue(text="C66765",
                                   description="Fascial Fibrosarcoma",
                                   meaning=NCIT.C66765)
    C66761 = PermissibleValue(text="C66761",
                                   description="Periosteal Fibroma",
                                   meaning=NCIT.C66761)
    C66802 = PermissibleValue(text="C66802",
                                   description="Oligodendroblastoma",
                                   meaning=NCIT.C66802)
    C67155 = PermissibleValue(text="C67155",
                                   description="Olfactory Neurogenic Tumor",
                                   meaning=NCIT.C67155)
    C8988 = PermissibleValue(text="C8988",
                                 description="Clear Cell Cystadenofibroma",
                                 meaning=NCIT.C8988)
    C3713 = PermissibleValue(text="C3713",
                                 description="Papillomatosis",
                                 meaning=NCIT.C3713)
    C84275 = PermissibleValue(text="C84275",
                                   description="Myeloid/Lymphoid Neoplasms with PDGFRA Rearrangement",
                                   meaning=NCIT.C84275)
    C7452 = PermissibleValue(text="C7452",
                                 description="Odontogenic Myxofibroma",
                                 meaning=NCIT.C7452)
    C3494 = PermissibleValue(text="C3494",
                                 description="Lung Papillary Adenoma",
                                 meaning=NCIT.C3494)
    C7449 = PermissibleValue(text="C7449",
                                 description="Infiltrating Angiolipoma",
                                 meaning=NCIT.C7449)
    C6902 = PermissibleValue(text="C6902",
                                 description="Chondroid Chordoma",
                                 meaning=NCIT.C6902)
    C6892 = PermissibleValue(text="C6892",
                                 description="Cellular Fibroma",
                                 meaning=NCIT.C6892)
    C4315 = PermissibleValue(text="C4315",
                                 description="Peripheral Odontogenic Fibroma",
                                 meaning=NCIT.C4315)
    C4319 = PermissibleValue(text="C4319",
                                 description="Papillary Ependymoma",
                                 meaning=NCIT.C4319)
    C4324 = PermissibleValue(text="C4324",
                                 description="Astroblastoma",
                                 meaning=NCIT.C4324)
    C4328 = PermissibleValue(text="C4328",
                                 description="Pacinian Neurofibroma",
                                 meaning=NCIT.C4328)
    C4332 = PermissibleValue(text="C4332",
                                 description="Angiomatous Meningioma",
                                 meaning=NCIT.C4332)
    C4320 = PermissibleValue(text="C4320",
                                 description="Protoplasmic Astrocytoma",
                                 meaning=NCIT.C4320)
    C4331 = PermissibleValue(text="C4331",
                                 description="Psammomatous Meningioma",
                                 meaning=NCIT.C4331)
    C4125 = PermissibleValue(text="C4125",
                                 description="Superficial Spreading Adenocarcinoma",
                                 meaning=NCIT.C4125)
    C4136 = PermissibleValue(text="C4136",
                                 description="Adenocarcinoma in Multiple Adenomatous Polyps",
                                 meaning=NCIT.C4136)
    C4101 = PermissibleValue(text="C4101",
                                 description="Verrucous Papilloma",
                                 meaning=NCIT.C4101)
    C4141 = PermissibleValue(text="C4141",
                                 description="Adenocarcinoma in Villous Adenoma",
                                 meaning=NCIT.C4141)
    C43342 = PermissibleValue(text="C43342",
                                   description="Apocrine Hidrocystoma",
                                   meaning=NCIT.C43342)
    C4142 = PermissibleValue(text="C4142",
                                 description="Villous Adenocarcinoma",
                                 meaning=NCIT.C4142)
    C4158 = PermissibleValue(text="C4158",
                                 description="Mixed Cell Adenocarcinoma",
                                 meaning=NCIT.C4158)
    C4157 = PermissibleValue(text="C4157",
                                 description="Mixed Cell Adenoma",
                                 meaning=NCIT.C4157)
    C4112 = PermissibleValue(text="C4112",
                                 description="Trichofolliculoma",
                                 meaning=NCIT.C4112)
    C4145 = PermissibleValue(text="C4145",
                                 description="Adenocarcinoma in Tubulovillous Adenoma",
                                 meaning=NCIT.C4145)
    C4144 = PermissibleValue(text="C4144",
                                 description="Adenocarcinoma In Situ in Tubulovillous Adenoma",
                                 meaning=NCIT.C4144)
    C4104 = PermissibleValue(text="C4104",
                                 description="Metastatic Squamous Cell Carcinoma",
                                 meaning=NCIT.C4104)
    C4181 = PermissibleValue(text="C4181",
                                 description="Serous Surface Papilloma",
                                 meaning=NCIT.C4181)
    C4184 = PermissibleValue(text="C4184",
                                 description="Papillary Mucinous Cystadenoma",
                                 meaning=NCIT.C4184)
    C4134 = PermissibleValue(text="C4134",
                                 description="Adenocarcinoma in Adenomatous Polyposis Coli",
                                 meaning=NCIT.C4134)
    C4173 = PermissibleValue(text="C4173",
                                 description="Papillary Eccrine Adenoma",
                                 meaning=NCIT.C4173)
    C4210 = PermissibleValue(text="C4210",
                                 description="Poorly Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                 meaning=NCIT.C4210)
    C4209 = PermissibleValue(text="C4209",
                                 description="Well Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                 meaning=NCIT.C4209)
    C4223 = PermissibleValue(text="C4223",
                                 description="Glomangiomyoma",
                                 meaning=NCIT.C4223)
    C4291 = PermissibleValue(text="C4291",
                                 description="Malignant Struma Ovarii",
                                 meaning=NCIT.C4291)
    C4262 = PermissibleValue(text="C4262",
                                 description="Endometrial Stromal Nodule",
                                 meaning=NCIT.C4262)
    C4253 = PermissibleValue(text="C4253",
                                 description="Mixed Liposarcoma",
                                 meaning=NCIT.C4253)
    C4256 = PermissibleValue(text="C4256",
                                 description="Cellular Leiomyoma",
                                 meaning=NCIT.C4256)
    C4260 = PermissibleValue(text="C4260",
                                 description="Fetal Rhabdomyoma",
                                 meaning=NCIT.C4260)
    C4226 = PermissibleValue(text="C4226",
                                 description="Balloon Cell Nevus",
                                 meaning=NCIT.C4226)
    C4243 = PermissibleValue(text="C4243",
                                 description="Sarcomatosis",
                                 meaning=NCIT.C4243)
    C39954 = PermissibleValue(text="C39954",
                                   description="Brenner Tumor",
                                   meaning=NCIT.C39954)
    C39981 = PermissibleValue(text="C39981",
                                   description="Malignant Ovarian Steroid Cell Tumor",
                                   meaning=NCIT.C39981)
    C40315 = PermissibleValue(text="C40315",
                                   description="Pilomyxoid Astrocytoma",
                                   meaning=NCIT.C40315)
    C40077 = PermissibleValue(text="C40077",
                                   description="Malignant Ovarian Clear Cell Tumor",
                                   meaning=NCIT.C40077)
    C4094 = PermissibleValue(text="C4094",
                                 description="Pleomorphic Carcinoma",
                                 meaning=NCIT.C4094)
    C39944 = PermissibleValue(text="C39944",
                                   description="Testicular Large Cell Calcifying Sertoli Cell Tumor",
                                   meaning=NCIT.C39944)
    C39973 = PermissibleValue(text="C39973",
                                   description="Poorly Differentiated Ovarian Sertoli-Leydig Cell Tumor, Variant with Heterologous Elements",
                                   meaning=NCIT.C39973)
    C40028 = PermissibleValue(text="C40028",
                                   description="Borderline Ovarian Serous Adenofibroma",
                                   meaning=NCIT.C40028)
    C142823 = PermissibleValue(text="C142823",
                                     description="Congenital Peribronchial Myofibroblastic Tumor",
                                     meaning=NCIT.C142823)
    C6475 = PermissibleValue(text="C6475",
                                 description="Clear Cell Chondrosarcoma",
                                 meaning=NCIT.C6475)
    C6503 = PermissibleValue(text="C6503",
                                 description="Chondroid Lipoma",
                                 meaning=NCIT.C6503)
    C6517 = PermissibleValue(text="C6517",
                                 description="Genital Rhabdomyoma",
                                 meaning=NCIT.C6517)
    C65161 = PermissibleValue(text="C65161",
                                   description="Polygonal Cell Carcinoma",
                                   meaning=NCIT.C65161)
    C65160 = PermissibleValue(text="C65160",
                                   description="Giant Cell and Spindle Cell Carcinoma",
                                   meaning=NCIT.C65160)
    C65204 = PermissibleValue(text="C65204",
                                   description="Papillary Mucinous Cystadenocarcinoma",
                                   meaning=NCIT.C65204)
    C65195 = PermissibleValue(text="C65195",
                                   description="Carcinoma Simplex",
                                   meaning=NCIT.C65195)
    C65179 = PermissibleValue(text="C65179",
                                   description="Squamous Cell Carcinoma with Horn Formation",
                                   meaning=NCIT.C65179)
    C65178 = PermissibleValue(text="C65178",
                                   description="Microinvasive Squamous Cell Carcinoma",
                                   meaning=NCIT.C65178)
    C6509 = PermissibleValue(text="C6509",
                                 description="Fibroblastic Liposarcoma",
                                 meaning=NCIT.C6509)
    C65165 = PermissibleValue(text="C65165",
                                   description="Inverted Squamous Cell Papilloma",
                                   meaning=NCIT.C65165)
    C65159 = PermissibleValue(text="C65159",
                                   description="Glassy Cell Carcinoma",
                                   meaning=NCIT.C65159)
    C65203 = PermissibleValue(text="C65203",
                                   description="Clear Cell Papillary Cystadenoma",
                                   meaning=NCIT.C65203)
    C65154 = PermissibleValue(text="C65154",
                                   description="Malignant Tumor, Small Cell Type",
                                   meaning=NCIT.C65154)
    C53316 = PermissibleValue(text="C53316",
                                   description="Cavernous Lymphangioma",
                                   meaning=NCIT.C53316)
    C53686 = PermissibleValue(text="C53686",
                                   description="Atypical Choroid Plexus Papilloma",
                                   meaning=NCIT.C53686)
    C5419 = PermissibleValue(text="C5419",
                                 description="Gliofibroma",
                                 meaning=NCIT.C5419)
    C49016 = PermissibleValue(text="C49016",
                                   description="Angiomyofibroblastoma",
                                   meaning=NCIT.C49016)
    C49012 = PermissibleValue(text="C49012",
                                   description="Myofibroblastoma",
                                   meaning=NCIT.C49012)
    C6911 = PermissibleValue(text="C6911",
                                 description="Intraneural Perineurioma",
                                 meaning=NCIT.C6911)
    C3830 = PermissibleValue(text="C3830",
                                 description="Chondromyxoid Fibroma",
                                 meaning=NCIT.C3830)
    C4717 = PermissibleValue(text="C4717",
                                 description="Anaplastic Ganglioglioma",
                                 meaning=NCIT.C4717)
    C129431 = PermissibleValue(text="C129431",
                                     description="Rosette-Forming Glioneuronal Tumor",
                                     meaning=NCIT.C129431)
    C3700 = PermissibleValue(text="C3700",
                                 description="Epithelioid Leiomyosarcoma",
                                 meaning=NCIT.C3700)
    C3701 = PermissibleValue(text="C3701",
                                 description="Myxoid Leiomyosarcoma",
                                 meaning=NCIT.C3701)
    C3685 = PermissibleValue(text="C3685",
                                 description="Microcystic Adenoma",
                                 meaning=NCIT.C3685)
    C3688 = PermissibleValue(text="C3688",
                                 description="Trabecular Adenoma",
                                 meaning=NCIT.C3688)
    C35259 = PermissibleValue(text="C35259",
                                   description="Chondromatosis",
                                   meaning=NCIT.C35259)
    C35837 = PermissibleValue(text="C35837",
                                   description="Salivary Gland Sialoblastoma",
                                   meaning=NCIT.C35837)
    C3763 = PermissibleValue(text="C3763",
                                 description="Pulmonary Adenomatosis",
                                 meaning=NCIT.C3763)
    C3748 = PermissibleValue(text="C3748",
                                 description="Leiomyomatosis",
                                 meaning=NCIT.C3748)
    C3737 = PermissibleValue(text="C3737",
                                 description="Mesenchymal Chondrosarcoma",
                                 meaning=NCIT.C3737)
    C3074 = PermissibleValue(text="C3074",
                                 description="Hairy Nevus",
                                 meaning=NCIT.C3074)
    C4258 = PermissibleValue(text="C4258",
                                 description="Pleomorphic Rhabdomyosarcoma",
                                 meaning=NCIT.C4258)
    C27031 = PermissibleValue(text="C27031",
                                   description="Pancreatic Neuroendocrine Neoplasm",
                                   meaning=NCIT.C27031)
    C27535 = PermissibleValue(text="C27535",
                                   description="Skin Adenoid Basal Cell Carcinoma",
                                   meaning=NCIT.C27535)
    C173735 = PermissibleValue(text="C173735",
                                     description="Odontogenic Carcinosarcoma",
                                     meaning=NCIT.C173735)
    C129440 = PermissibleValue(text="C129440",
                                     description="Medulloblastoma, WNT-Activated",
                                     meaning=NCIT.C129440)
    C7685 = PermissibleValue(text="C7685",
                                 description="Adenocarcinoma with Cartilaginous Metaplasia",
                                 meaning=NCIT.C7685)
    C80341 = PermissibleValue(text="C80341",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(1;19)(q23;p13.3); E2A-PBX1 (TCF3-PBX1)",
                                   meaning=NCIT.C80341)
    C80335 = PermissibleValue(text="C80335",
                                   description="B Lymphoblastic Leukemia/Lymphoma with Hyperdiploidy",
                                   meaning=NCIT.C80335)
    C66841 = PermissibleValue(text="C66841",
                                   description="Melanotic Neurofibroma",
                                   meaning=NCIT.C66841)
    C66775 = PermissibleValue(text="C66775",
                                   description="Borderline Ovarian Mucinous Adenofibroma",
                                   meaning=NCIT.C66775)
    C66812 = PermissibleValue(text="C66812",
                                   description="Retinocytoma",
                                   meaning=NCIT.C66812)
    C66755 = PermissibleValue(text="C66755",
                                   description="Proliferative Nodules in Congenital Melanocytic Nevus",
                                   meaning=NCIT.C66755)
    C66809 = PermissibleValue(text="C66809",
                                   description="Ciliary Body Benign Teratoid Medulloepithelioma",
                                   meaning=NCIT.C66809)
    C4327 = PermissibleValue(text="C4327",
                                 description="Central Nervous System Medulloepithelioma",
                                 meaning=NCIT.C4327)
    C66749 = PermissibleValue(text="C66749",
                                   description="Ovarian Stromal Tumor with Minor Sex Cord Elements",
                                   meaning=NCIT.C66749)
    C66792 = PermissibleValue(text="C66792",
                                   description="Hemolymphangioma",
                                   meaning=NCIT.C66792)
    C66810 = PermissibleValue(text="C66810",
                                   description="Ciliary Body Teratoid Medulloepithelioma",
                                   meaning=NCIT.C66810)
    C66774 = PermissibleValue(text="C66774",
                                   description="Ossifying Renal Tumor of Infancy",
                                   meaning=NCIT.C66774)
    C3070 = PermissibleValue(text="C3070",
                                 description="Granulosa Cell Tumor",
                                 meaning=NCIT.C3070)
    C8970 = PermissibleValue(text="C8970",
                                 description="Periosteal Osteosarcoma",
                                 meaning=NCIT.C8970)
    C6581 = PermissibleValue(text="C6581",
                                 description="Parachordoma",
                                 meaning=NCIT.C6581)
    C2977 = PermissibleValue(text="C2977",
                                 description="Phyllodes Tumor",
                                 meaning=NCIT.C2977)
    C6934 = PermissibleValue(text="C6934",
                                 description="Gangliocytoma",
                                 meaning=NCIT.C6934)
    C7052 = PermissibleValue(text="C7052",
                                 description="Myofibroma",
                                 meaning=NCIT.C7052)
    C7112 = PermissibleValue(text="C7112",
                                 description="Squamous Odontogenic Tumor",
                                 meaning=NCIT.C7112)
    C6899 = PermissibleValue(text="C6899",
                                 description="Breast Adenomyoepithelioma",
                                 meaning=NCIT.C6899)
    C92625 = PermissibleValue(text="C92625",
                                   description="Anaplastic Medulloblastoma",
                                   meaning=NCIT.C92625)
    C4308 = PermissibleValue(text="C4308",
                                 description="Cementoblastoma",
                                 meaning=NCIT.C4308)
    C4397 = PermissibleValue(text="C4397",
                                 description="Carcinoma ex Pleomorphic Adenoma",
                                 meaning=NCIT.C4397)
    C43565 = PermissibleValue(text="C43565",
                                   description="Appendix Tubular Carcinoid",
                                   meaning=NCIT.C43565)
    C4316 = PermissibleValue(text="C4316",
                                 description="Ameloblastic Fibroma",
                                 meaning=NCIT.C4316)
    C4155 = PermissibleValue(text="C4155",
                                 description="Parathyroid Gland Water-Clear Cell Adenoma",
                                 meaning=NCIT.C4155)
    C4110 = PermissibleValue(text="C4110",
                                 description="Intraepidermal Epithelioma of Jadassohn",
                                 meaning=NCIT.C4110)
    C4201 = PermissibleValue(text="C4201",
                                 description="Adenocarcinoma with Spindle Cell Metaplasia",
                                 meaning=NCIT.C4201)
    C4254 = PermissibleValue(text="C4254",
                                 description="Spindle Cell Lipoma",
                                 meaning=NCIT.C4254)
    C4245 = PermissibleValue(text="C4245",
                                 description="Elastofibroma",
                                 meaning=NCIT.C4245)
    C4229 = PermissibleValue(text="C4229",
                                 description="Neuronevus",
                                 meaning=NCIT.C4229)
    C4219 = PermissibleValue(text="C4219",
                                 description="Malignant Extra-Adrenal Paraganglioma",
                                 meaning=NCIT.C4219)
    C4222 = PermissibleValue(text="C4222",
                                 description="Glomangioma",
                                 meaning=NCIT.C4222)
    C4288 = PermissibleValue(text="C4288",
                                 description="Intermediate Immature Teratoma",
                                 meaning=NCIT.C4288)
    C4252 = PermissibleValue(text="C4252",
                                 description="Round Cell Liposarcoma",
                                 meaning=NCIT.C4252)
    C45602 = PermissibleValue(text="C45602",
                                   description="Lung Mixed Squamous Cell and Glandular Papilloma",
                                   meaning=NCIT.C45602)
    C40034 = PermissibleValue(text="C40034",
                                   description="Ovarian Mucinous Adenocarcinofibroma",
                                   meaning=NCIT.C40034)
    C7930 = PermissibleValue(text="C7930",
                                 description="Lymphomatoid Granulomatosis",
                                 meaning=NCIT.C7930)
    C39972 = PermissibleValue(text="C39972",
                                   description="Moderately Differentiated Ovarian Sertoli-Leydig Cell Tumor, Variant with Heterologous Elements",
                                   meaning=NCIT.C39972)
    C40060 = PermissibleValue(text="C40060",
                                   description="Ovarian Endometrioid Adenocarcinofibroma",
                                   meaning=NCIT.C40060)
    C40079 = PermissibleValue(text="C40079",
                                   description="Ovarian Clear Cell Adenocarcinofibroma",
                                   meaning=NCIT.C40079)
    C6909 = PermissibleValue(text="C6909",
                                 description="Rhabdoid Meningioma",
                                 meaning=NCIT.C6909)
    C65200 = PermissibleValue(text="C65200",
                                   description="Thyroid Gland Follicular Carcinoma, Minimally Invasive",
                                   meaning=NCIT.C65200)
    C65180 = PermissibleValue(text="C65180",
                                   description="Squamous Cell Carcinoma, Clear Cell Type",
                                   meaning=NCIT.C65180)
    C63622 = PermissibleValue(text="C63622",
                                   description="Undifferentiated Carcinoma with Osteoclast-Like Giant Cells",
                                   meaning=NCIT.C63622)
    C53595 = PermissibleValue(text="C53595",
                                   description="Ectopic Hamartomatous Thymoma",
                                   meaning=NCIT.C53595)
    C54664 = PermissibleValue(text="C54664",
                                   description="Hidradenocarcinoma",
                                   meaning=NCIT.C54664)
    C53958 = PermissibleValue(text="C53958",
                                   description="High Grade Surface Osteosarcoma",
                                   meaning=NCIT.C53958)
    C27541 = PermissibleValue(text="C27541",
                                   description="Skin Micronodular Basal Cell Carcinoma",
                                   meaning=NCIT.C27541)
    C48876 = PermissibleValue(text="C48876",
                                   description="Dedifferentiated Chordoma",
                                   meaning=NCIT.C48876)
    C6908 = PermissibleValue(text="C6908",
                                 description="Chordoid Meningioma",
                                 meaning=NCIT.C6908)
    C4723 = PermissibleValue(text="C4723",
                                 description="Atypical Meningioma",
                                 meaning=NCIT.C4723)
    C9473 = PermissibleValue(text="C9473",
                                 description="Lactating Adenoma",
                                 meaning=NCIT.C9473)
    C95514 = PermissibleValue(text="C95514",
                                   description="Pancreatic Intraductal Papillary Mucinous Neoplasm, Oncocytic-Type",
                                   meaning=NCIT.C95514)
    C3706 = PermissibleValue(text="C3706",
                                 description="Medullomyoblastoma with Myogenic Differentiation",
                                 meaning=NCIT.C3706)
    C3699 = PermissibleValue(text="C3699",
                                 description="Intramuscular Hemangioma",
                                 meaning=NCIT.C3699)
    C3703 = PermissibleValue(text="C3703",
                                 description="Pleomorphic Lipoma",
                                 meaning=NCIT.C3703)
    C7565 = PermissibleValue(text="C7565",
                                 description="Eccrine Hidrocystoma",
                                 meaning=NCIT.C7565)
    C3761 = PermissibleValue(text="C3761",
                                 description="Syringoma",
                                 meaning=NCIT.C3761)
    C3779 = PermissibleValue(text="C3779",
                                 description="Giant Cell Carcinoma",
                                 meaning=NCIT.C3779)
    C3275 = PermissibleValue(text="C3275",
                                 description="Neuroma",
                                 meaning=NCIT.C3275)
    C6936 = PermissibleValue(text="C6936",
                                 description="Deep "Aggressive" Angiomyxoma",
                                 meaning=NCIT.C6936)
    C27273 = PermissibleValue(text="C27273",
                                   description="Poroma",
                                   meaning=NCIT.C27273)
    C27848 = PermissibleValue(text="C27848",
                                   description="Endometrial Endometrioid Adenocarcinoma, Ciliated Variant",
                                   meaning=NCIT.C27848)
    C27839 = PermissibleValue(text="C27839",
                                   description="Endometrial Endometrioid Adenocarcinoma, Secretory Variant",
                                   meaning=NCIT.C27839)
    C2860 = PermissibleValue(text="C2860",
                                 description="Adrenal Rest Tumor",
                                 meaning=NCIT.C2860)
    C3204 = PermissibleValue(text="C3204",
                                 description="Lymphangioleiomyoma",
                                 meaning=NCIT.C3204)
    C173927 = PermissibleValue(text="C173927",
                                     description="Cemento-Osseous Dysplasia",
                                     meaning=NCIT.C173927)
    C7380 = PermissibleValue(text="C7380",
                                 description="Thyroid Gland Papillary and Follicular Carcinoma",
                                 meaning=NCIT.C7380)
    C129319 = PermissibleValue(text="C129319",
                                     description="Oligodendroglioma, Not Otherwise Specified",
                                     meaning=NCIT.C129319)
    C4346 = PermissibleValue(text="C4346",
                                 description="Skin Basal Cell Carcinoma with Sebaceous Differentiation",
                                 meaning=NCIT.C4346)
    C27856 = PermissibleValue(text="C27856",
                                   description="Diffuse Large B-Cell Lymphoma Arising in HHV8-Positive Multicentric Castleman Disease",
                                   meaning=NCIT.C27856)
    C81758 = PermissibleValue(text="C81758",
                                   description="Fibroblastic Reticular Cell Tumor",
                                   meaning=NCIT.C81758)
    C82212 = PermissibleValue(text="C82212",
                                   description="Mixed Phenotype Acute Leukemia, B/Myeloid, Not Otherwise Specified",
                                   meaning=NCIT.C82212)
    C82192 = PermissibleValue(text="C82192",
                                   description="Mixed Phenotype Acute Leukemia with t(9;22)(q34.1;q11.2); BCR-ABL1",
                                   meaning=NCIT.C82192)
    C82213 = PermissibleValue(text="C82213",
                                   description="Mixed Phenotype Acute Leukemia, T/Myeloid, Not Otherwise Specified",
                                   meaning=NCIT.C82213)
    C80334 = PermissibleValue(text="C80334",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(12;21)(p13.2;q22.1); ETV6-RUNX1",
                                   meaning=NCIT.C80334)
    C80340 = PermissibleValue(text="C80340",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(5;14)(q31.1;q32.3); IL3-IGH",
                                   meaning=NCIT.C80340)
    C80326 = PermissibleValue(text="C80326",
                                   description="B Lymphoblastic Leukemia/Lymphoma, Not Otherwise Specified",
                                   meaning=NCIT.C80326)
    C80331 = PermissibleValue(text="C80331",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(9;22)(q34.1;q11.2); BCR-ABL1",
                                   meaning=NCIT.C80331)
    C80332 = PermissibleValue(text="C80332",
                                   description="B Lymphoblastic Leukemia/Lymphoma with t(v;11q23.3); MLL Rearranged",
                                   meaning=NCIT.C80332)
    C66933 = PermissibleValue(text="C66933",
                                   description="Breast Ductal Carcinoma In Situ, Solid Type",
                                   meaning=NCIT.C66933)
    C66719 = PermissibleValue(text="C66719",
                                   description="Breast Atypical Medullary Carcinoma",
                                   meaning=NCIT.C66719)
    C66807 = PermissibleValue(text="C66807",
                                   description="Ciliary Body Benign Medulloepithelioma",
                                   meaning=NCIT.C66807)
    C6876 = PermissibleValue(text="C6876",
                                 description="Lung Large Cell Carcinoma with Rhabdoid Phenotype",
                                 meaning=NCIT.C6876)
    C6781 = PermissibleValue(text="C6781",
                                 description="Stromal Neoplasm",
                                 meaning=NCIT.C6781)
    C4299 = PermissibleValue(text="C4299",
                                 description="Verrucous Hemangioma",
                                 meaning=NCIT.C4299)
    C4323 = PermissibleValue(text="C4323",
                                 description="Pleomorphic Xanthoastrocytoma",
                                 meaning=NCIT.C4323)
    C4325 = PermissibleValue(text="C4325",
                                 description="Giant Cell Glioblastoma",
                                 meaning=NCIT.C4325)
    C4318 = PermissibleValue(text="C4318",
                                 description="Gliomatosis Cerebri",
                                 meaning=NCIT.C4318)
    C4169 = PermissibleValue(text="C4169",
                                 description="Apocrine Carcinoma",
                                 meaning=NCIT.C4169)
    C4135 = PermissibleValue(text="C4135",
                                 description="Multiple Adenomatous Polyps",
                                 meaning=NCIT.C4135)
    C4116 = PermissibleValue(text="C4116",
                                 description="Stage 0 Transitional Cell Carcinoma",
                                 meaning=NCIT.C4116)
    C4153 = PermissibleValue(text="C4153",
                                 description="Glycogen-Rich Carcinoma",
                                 meaning=NCIT.C4153)
    C4108 = PermissibleValue(text="C4108",
                                 description="Superficial Multifocal Basal Cell Carcinoma",
                                 meaning=NCIT.C4108)
    C4123 = PermissibleValue(text="C4123",
                                 description="Adenocarcinoma In Situ",
                                 meaning=NCIT.C4123)
    C4178 = PermissibleValue(text="C4178",
                                 description="Borderline Papillary Cystadenoma",
                                 meaning=NCIT.C4178)
    C4199 = PermissibleValue(text="C4199",
                                 description="Epithelial-Myoepithelial Carcinoma",
                                 meaning=NCIT.C4199)
    C4188 = PermissibleValue(text="C4188",
                                 description="Comedocarcinoma",
                                 meaning=NCIT.C4188)
    C4148 = PermissibleValue(text="C4148",
                                 description="Pituitary Gland Mixed Acidophil-Basophil Adenoma",
                                 meaning=NCIT.C4148)
    C4152 = PermissibleValue(text="C4152",
                                 description="Lipid-Rich Carcinoma",
                                 meaning=NCIT.C4152)
    C4137 = PermissibleValue(text="C4137",
                                 description="Solid Carcinoma",
                                 meaning=NCIT.C4137)
    C4239 = PermissibleValue(text="C4239",
                                 description="Type B Spindle Cell Melanoma",
                                 meaning=NCIT.C4239)
    C4238 = PermissibleValue(text="C4238",
                                 description="Type A Spindle Cell Melanoma",
                                 meaning=NCIT.C4238)
    C4265 = PermissibleValue(text="C4265",
                                 description="Pancreatoblastoma",
                                 meaning=NCIT.C4265)
    C4241 = PermissibleValue(text="C4241",
                                 description="Cellular Blue Nevus",
                                 meaning=NCIT.C4241)
    C4296 = PermissibleValue(text="C4296",
                                 description="Venous Hemangioma",
                                 meaning=NCIT.C4296)
    C4208 = PermissibleValue(text="C4208",
                                 description="Ovarian Sex Cord Tumor with Annular Tubules",
                                 meaning=NCIT.C4208)
    C4217 = PermissibleValue(text="C4217",
                                 description="Parasympathetic Paraganglioma",
                                 meaning=NCIT.C4217)
    C40177 = PermissibleValue(text="C40177",
                                   description="Uterine Corpus Smooth Muscle Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C40177)
    C6476 = PermissibleValue(text="C6476",
                                 description="Dedifferentiated Chondrosarcoma",
                                 meaning=NCIT.C6476)
    C6493 = PermissibleValue(text="C6493",
                                 description="Plexiform Fibrohistiocytic Tumor",
                                 meaning=NCIT.C6493)
    C65193 = PermissibleValue(text="C65193",
                                   description="Flat Adenoma",
                                   meaning=NCIT.C65193)
    C6494 = PermissibleValue(text="C6494",
                                 description="Angiomatoid Fibrous Histiocytoma",
                                 meaning=NCIT.C6494)
    C5979 = PermissibleValue(text="C5979",
                                 description="Salivary Gland Canalicular Adenoma",
                                 meaning=NCIT.C5979)
    C5325 = PermissibleValue(text="C5325",
                                 description="Intestinal Gangliocytic Paraganglioma",
                                 meaning=NCIT.C5325)
    C48622 = PermissibleValue(text="C48622",
                                   description="Mucosal Lentiginous Melanoma",
                                   meaning=NCIT.C48622)
    C2974 = PermissibleValue(text="C2974",
                                 description="Papillary Cystadenoma",
                                 meaning=NCIT.C2974)
    C2927 = PermissibleValue(text="C2927",
                                 description="Papillary Carcinoma",
                                 meaning=NCIT.C2927)
    C3218 = PermissibleValue(text="C3218",
                                 description="Diffuse Cutaneous Mastocytosis",
                                 meaning=NCIT.C3218)
    C92552 = PermissibleValue(text="C92552",
                                   description="Angiocentric Glioma",
                                   meaning=NCIT.C92552)
    C3705 = PermissibleValue(text="C3705",
                                 description="Pleomorphic Liposarcoma",
                                 meaning=NCIT.C3705)
    C3356 = PermissibleValue(text="C3356",
                                 description="Solitary Reticulohistiocytoma",
                                 meaning=NCIT.C3356)
    C3757 = PermissibleValue(text="C3757",
                                 description="Placental-Site Gestational Trophoblastic Tumor",
                                 meaning=NCIT.C3757)
    C3297 = PermissibleValue(text="C3297",
                                 description="Osteoid Osteoma",
                                 meaning=NCIT.C3297)
    C7643 = PermissibleValue(text="C7643",
                                 description="Alkylating Agent-Related Myelodysplastic Syndrome",
                                 meaning=NCIT.C7643)
    C27092 = PermissibleValue(text="C27092",
                                   description="Small Cell Carcinoma, Fusiform Cell Type",
                                   meaning=NCIT.C27092)
    C3060 = PermissibleValue(text="C3060",
                                 description="Glomus Tumor",
                                 meaning=NCIT.C3060)
    C3086 = PermissibleValue(text="C3086",
                                 description="Cavernous Hemangioma",
                                 meaning=NCIT.C3086)
    C12917 = PermissibleValue(text="C12917",
                                   description="Malignant Cell",
                                   meaning=NCIT.C12917)
    C6919 = PermissibleValue(text="C6919",
                                 description="T Lymphoblastic Lymphoma",
                                 meaning=NCIT.C6919)
    C82203 = PermissibleValue(text="C82203",
                                   description="Mixed Phenotype Acute Leukemia with t(v;11q23.3); MLL Rearranged",
                                   meaning=NCIT.C82203)
    C80374 = PermissibleValue(text="C80374",
                                   description="Systemic EBV-Positive T-Cell Lymphoma of Childhood",
                                   meaning=NCIT.C80374)
    C66776 = PermissibleValue(text="C66776",
                                   description="Gonadal Polyembryoma",
                                   meaning=NCIT.C66776)
    C66753 = PermissibleValue(text="C66753",
                                   description="Malignant Melanoma in Precancerous Melanosis",
                                   meaning=NCIT.C66753)
    C66991 = PermissibleValue(text="C66991",
                                   description="Mixed Testicular Sex Cord-Stromal Tumor",
                                   meaning=NCIT.C66991)
    C8986 = PermissibleValue(text="C8986",
                                 description="Papillary Adenofibroma",
                                 meaning=NCIT.C8986)
    C8419 = PermissibleValue(text="C8419",
                                 description="Dysplastic Cerebellar Gangliocytoma",
                                 meaning=NCIT.C8419)
    C7225 = PermissibleValue(text="C7225",
                                 description="ALK-Positive Large B-Cell Lymphoma",
                                 meaning=NCIT.C7225)
    C6577 = PermissibleValue(text="C6577",
                                 description="Myxoma",
                                 meaning=NCIT.C6577)
    C6582 = PermissibleValue(text="C6582",
                                 description="Ossifying Fibromyxoid Tumor",
                                 meaning=NCIT.C6582)
    C7504 = PermissibleValue(text="C7504",
                                 description="Adult Cystic Nephroma",
                                 meaning=NCIT.C7504)
    C7440 = PermissibleValue(text="C7440",
                                 description="Papilloma",
                                 meaning=NCIT.C7440)
    C6921 = PermissibleValue(text="C6921",
                                 description="Langerhans Cell Sarcoma",
                                 meaning=NCIT.C6921)
    C6926 = PermissibleValue(text="C6926",
                                 description="Stromal Sarcoma",
                                 meaning=NCIT.C6926)
    C6900 = PermissibleValue(text="C6900",
                                 description="Epithelioid Trophoblastic Tumor",
                                 meaning=NCIT.C6900)
    C6891 = PermissibleValue(text="C6891",
                                 description="Meningeal Melanomatosis",
                                 meaning=NCIT.C6891)
    C6894 = PermissibleValue(text="C6894",
                                 description="Malignant Solitary Fibrous Tumor",
                                 meaning=NCIT.C6894)
    C6890 = PermissibleValue(text="C6890",
                                 description="Meningeal Melanocytosis",
                                 meaning=NCIT.C6890)
    C4334 = PermissibleValue(text="C4334",
                                 description="Meningeal Sarcomatosis",
                                 meaning=NCIT.C4334)
    C43625 = PermissibleValue(text="C43625",
                                   description="Pleomorphic Hepatocellular Carcinoma",
                                   meaning=NCIT.C43625)
    C4165 = PermissibleValue(text="C4165",
                                 description="Adrenal Cortex Clear Cell Adenoma",
                                 meaning=NCIT.C4165)
    C41251 = PermissibleValue(text="C41251",
                                   description="Pancreatic Intraductal Papillary-Mucinous Neoplasm, High Grade",
                                   meaning=NCIT.C41251)
    C4121 = PermissibleValue(text="C4121",
                                 description="Basaloid Carcinoma",
                                 meaning=NCIT.C4121)
    C4120 = PermissibleValue(text="C4120",
                                 description="Sarcomatoid Transitional Cell Carcinoma",
                                 meaning=NCIT.C4120)
    C4151 = PermissibleValue(text="C4151",
                                 description="Clear Cell Adenoma",
                                 meaning=NCIT.C4151)
    C4163 = PermissibleValue(text="C4163",
                                 description="Adrenal Cortex Compact Cell Adenoma",
                                 meaning=NCIT.C4163)
    C4149 = PermissibleValue(text="C4149",
                                 description="Pituitary Gland Mixed Acidophil-Basophil Carcinoma",
                                 meaning=NCIT.C4149)
    C4167 = PermissibleValue(text="C4167",
                                 description="Adrenal Cortex Mixed Cell Adenoma",
                                 meaning=NCIT.C4167)
    C4166 = PermissibleValue(text="C4166",
                                 description="Adrenal Cortex Glomerulosa Cell Adenoma",
                                 meaning=NCIT.C4166)
    C4279 = PermissibleValue(text="C4279",
                                 description="Biphasic Synovial Sarcoma",
                                 meaning=NCIT.C4279)
    C4267 = PermissibleValue(text="C4267",
                                 description="Benign Mesenchymoma",
                                 meaning=NCIT.C4267)
    C4228 = PermissibleValue(text="C4228",
                                 description="Regressing Melanoma",
                                 meaning=NCIT.C4228)
    C4203 = PermissibleValue(text="C4203",
                                 description="Ovarian Luteinized Thecoma",
                                 meaning=NCIT.C4203)
    C4249 = PermissibleValue(text="C4249",
                                 description="Fibrolipoma",
                                 meaning=NCIT.C4249)
    C4234 = PermissibleValue(text="C4234",
                                 description="Giant Congenital Nevus",
                                 meaning=NCIT.C4234)
    C65190 = PermissibleValue(text="C65190",
                                   description="Malignant Somatostatinoma",
                                   meaning=NCIT.C65190)
    C6519 = PermissibleValue(text="C6519",
                                 description="Spindle Cell Rhabdomyosarcoma",
                                 meaning=NCIT.C6519)
    C65151 = PermissibleValue(text="C65151",
                                   description="Non-Small Cell Carcinoma",
                                   meaning=NCIT.C65151)
    C5950 = PermissibleValue(text="C5950",
                                 description="Salivary Gland Basal Cell Adenoma",
                                 meaning=NCIT.C5950)
    C3007 = PermissibleValue(text="C3007",
                                 description="Enchondroma",
                                 meaning=NCIT.C3007)
    C54244 = PermissibleValue(text="C54244",
                                   description="Basaloid Squamous Cell Carcinoma",
                                   meaning=NCIT.C54244)
    C54319 = PermissibleValue(text="C54319",
                                   description="Calcifying Cystic Odontogenic Tumor",
                                   meaning=NCIT.C54319)
    C49107 = PermissibleValue(text="C49107",
                                   description="Giant Cell Tumor of Soft Tissue",
                                   meaning=NCIT.C49107)
    C5117 = PermissibleValue(text="C5117",
                                 description="Spiradenocarcinoma",
                                 meaning=NCIT.C5117)
    C4700 = PermissibleValue(text="C4700",
                                 description="Giant Cell Fibroblastoma",
                                 meaning=NCIT.C4700)
    C3693 = PermissibleValue(text="C3693",
                                 description="Carcinomatosis",
                                 meaning=NCIT.C3693)
    C3678 = PermissibleValue(text="C3678",
                                 description="Salivary Gland Basal Cell Adenocarcinoma",
                                 meaning=NCIT.C3678)
    C35558 = PermissibleValue(text="C35558",
                                   description="Tall Cell Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C35558)
    C6895 = PermissibleValue(text="C6895",
                                 description="Atypical Polypoid Adenomyoma",
                                 meaning=NCIT.C6895)
    C3746 = PermissibleValue(text="C3746",
                                 description="Small Cell Sarcoma",
                                 meaning=NCIT.C3746)
    C3296 = PermissibleValue(text="C3296",
                                 description="Osteoma",
                                 meaning=NCIT.C3296)
    C3255 = PermissibleValue(text="C3255",
                                 description="Myxosarcoma",
                                 meaning=NCIT.C3255)
    C3482 = PermissibleValue(text="C3482",
                                 description="Metastatic Carcinoma",
                                 meaning=NCIT.C3482)
    C2879 = PermissibleValue(text="C2879",
                                 description="Neoplasm of the Diffuse Neuroendocrine System",
                                 meaning=NCIT.C2879)
    C3041 = PermissibleValue(text="C3041",
                                 description="Fibroma",
                                 meaning=NCIT.C3041)
    C3072 = PermissibleValue(text="C3072",
                                 description="Ovarian Gynandroblastoma",
                                 meaning=NCIT.C3072)
    C121793 = PermissibleValue(text="C121793",
                                     description="Undifferentiated/Unclassified Sarcoma",
                                     meaning=NCIT.C121793)
    C128847 = PermissibleValue(text="C128847",
                                     description="Lung Micropapillary Adenocarcinoma",
                                     meaning=NCIT.C128847)
    C7603 = PermissibleValue(text="C7603",
                                 description="Regressing Nevus",
                                 meaning=NCIT.C7603)
    C66748 = PermissibleValue(text="C66748",
                                   description="Unclassified Testicular Sex Cord-Stromal Tumor",
                                   meaning=NCIT.C66748)
    C84277 = PermissibleValue(text="C84277",
                                   description="Myeloid/Lymphoid Neoplasms with FGFR1 Rearrangement",
                                   meaning=NCIT.C84277)
    C7217 = PermissibleValue(text="C7217",
                                 description="Primary Cutaneous Follicle Center Lymphoma",
                                 meaning=NCIT.C7217)
    C7224 = PermissibleValue(text="C7224",
                                 description="Plasmablastic Lymphoma",
                                 meaning=NCIT.C7224)
    C7399 = PermissibleValue(text="C7399",
                                 description="Villous Adenoma",
                                 meaning=NCIT.C7399)
    C6918 = PermissibleValue(text="C6918",
                                 description="Subcutaneous Panniculitis-Like T-Cell Lymphoma",
                                 meaning=NCIT.C6918)
    C7017 = PermissibleValue(text="C7017",
                                 description="Granular Cell Tumor of the Sellar Region",
                                 meaning=NCIT.C7017)
    C65198 = PermissibleValue(text="C65198",
                                   description="Glandular Papillomatosis",
                                   meaning=NCIT.C65198)
    C6885 = PermissibleValue(text="C6885",
                                 description="Thymoma Type AB",
                                 meaning=NCIT.C6885)
    C5727 = PermissibleValue(text="C5727",
                                 description="Pancreatic Acinar Cell Cystadenocarcinoma",
                                 meaning=NCIT.C5727)
    C4272 = PermissibleValue(text="C4272",
                                 description="Breast Pericanalicular Fibroadenoma",
                                 meaning=NCIT.C4272)
    C4237 = PermissibleValue(text="C4237",
                                 description="Spindle Cell Melanoma",
                                 meaning=NCIT.C4237)
    C4271 = PermissibleValue(text="C4271",
                                 description="Breast Intracanalicular Fibroadenoma",
                                 meaning=NCIT.C4271)
    C4204 = PermissibleValue(text="C4204",
                                 description="Ovarian Sclerosing Stromal Tumor",
                                 meaning=NCIT.C4204)
    C4207 = PermissibleValue(text="C4207",
                                 description="Juvenile Type Granulosa Cell Tumor",
                                 meaning=NCIT.C4207)
    C4236 = PermissibleValue(text="C4236",
                                 description="Epithelioid Cell Melanoma",
                                 meaning=NCIT.C4236)
    C4273 = PermissibleValue(text="C4273",
                                 description="Breast Giant Fibroadenoma",
                                 meaning=NCIT.C4273)
    C4276 = PermissibleValue(text="C4276",
                                 description="Breast Juvenile Fibroadenoma",
                                 meaning=NCIT.C4276)
    C4099 = PermissibleValue(text="C4099",
                                 description="Small Cell Intermediate Cell Carcinoma",
                                 meaning=NCIT.C4099)
    C6496 = PermissibleValue(text="C6496",
                                 description="Myxofibrosarcoma",
                                 meaning=NCIT.C6496)
    C49024 = PermissibleValue(text="C49024",
                                   description="Low Grade Myofibroblastic Sarcoma",
                                   meaning=NCIT.C49024)
    C2971 = PermissibleValue(text="C2971",
                                 description="Cystadenocarcinoma",
                                 meaning=NCIT.C2971)
    C5100 = PermissibleValue(text="C5100",
                                 description="Renomedullary Interstitial Cell Tumor",
                                 meaning=NCIT.C5100)
    C46004 = PermissibleValue(text="C46004",
                                   description="Thyroid Gland Papillary Microcarcinoma",
                                   meaning=NCIT.C46004)
    C4753 = PermissibleValue(text="C4753",
                                 description="B-Cell Prolymphocytic Leukemia",
                                 meaning=NCIT.C4753)
    C4662 = PermissibleValue(text="C4662",
                                 description="Meningeal Melanocytoma",
                                 meaning=NCIT.C4662)
    C9505 = PermissibleValue(text="C9505",
                                 description="Dysembryoplastic Neuroepithelial Tumor",
                                 meaning=NCIT.C9505)
    C3697 = PermissibleValue(text="C3697",
                                 description="Myxopapillary Ependymoma",
                                 meaning=NCIT.C3697)
    C3704 = PermissibleValue(text="C3704",
                                 description="Dedifferentiated Liposarcoma",
                                 meaning=NCIT.C3704)
    C3736 = PermissibleValue(text="C3736",
                                 description="Adrenal Gland Myelolipoma",
                                 meaning=NCIT.C3736)
    C3733 = PermissibleValue(text="C3733",
                                 description="Angiolipoma",
                                 meaning=NCIT.C3733)
    C6882 = PermissibleValue(text="C6882",
                                 description="Micropapillary Serous Carcinoma",
                                 meaning=NCIT.C6882)
    C6888 = PermissibleValue(text="C6888",
                                 description="Thymoma Type B2",
                                 meaning=NCIT.C6888)
    C4313 = PermissibleValue(text="C4313",
                                 description="Ameloblastoma",
                                 meaning=NCIT.C4313)
    C4130 = PermissibleValue(text="C4130",
                                 description="Bile Duct Mucinous Cystic Neoplasm with an Associated Invasive Carcinoma",
                                 meaning=NCIT.C4130)
    C4113 = PermissibleValue(text="C4113",
                                 description="Trichilemmoma",
                                 meaning=NCIT.C4113)
    C4129 = PermissibleValue(text="C4129",
                                 description="Bile Duct Mucinous Cystic Neoplasm",
                                 meaning=NCIT.C4129)
    C4133 = PermissibleValue(text="C4133",
                                 description="Tubular Adenoma",
                                 meaning=NCIT.C4133)
    C4124 = PermissibleValue(text="C4124",
                                 description="Metastatic Adenocarcinoma",
                                 meaning=NCIT.C4124)
    C4242 = PermissibleValue(text="C4242",
                                 description="Benign Soft Tissue Neoplasm",
                                 meaning=NCIT.C4242)
    C42598 = PermissibleValue(text="C42598",
                                   description="Low Grade Appendix Mucinous Neoplasm",
                                   meaning=NCIT.C42598)
    C45340 = PermissibleValue(text="C45340",
                                   description="Primary Cutaneous Gamma-Delta T-Cell Lymphoma",
                                   meaning=NCIT.C45340)
    C3902 = PermissibleValue(text="C3902",
                                 description="Telangiectatic Osteosarcoma",
                                 meaning=NCIT.C3902)
    C53998 = PermissibleValue(text="C53998",
                                   description="Benign Gastrointestinal Stromal Tumor",
                                   meaning=NCIT.C53998)
    C54297 = PermissibleValue(text="C54297",
                                   description="Metastasizing Ameloblastoma",
                                   meaning=NCIT.C54297)
    C4752 = PermissibleValue(text="C4752",
                                 description="T-Cell Prolymphocytic Leukemia",
                                 meaning=NCIT.C4752)
    C46093 = PermissibleValue(text="C46093",
                                   description="Oncocytic Variant Thyroid Gland Papillary Carcinoma",
                                   meaning=NCIT.C46093)
    C4738 = PermissibleValue(text="C4738",
                                 description="Desmoplastic Infantile Ganglioglioma",
                                 meaning=NCIT.C4738)
    C9286 = PermissibleValue(text="C9286",
                                 description="Indolent Systemic Mastocytosis",
                                 meaning=NCIT.C9286)
    C35702 = PermissibleValue(text="C35702",
                                   description="Salivary Gland Polymorphous Adenocarcinoma",
                                   meaning=NCIT.C35702)
    C3780 = PermissibleValue(text="C3780",
                                 description="Large Cell Carcinoma",
                                 meaning=NCIT.C3780)
    C3734 = PermissibleValue(text="C3734",
                                 description="Angiomyolipoma",
                                 meaning=NCIT.C3734)
    C2855 = PermissibleValue(text="C2855",
                                 description="Adenoma",
                                 meaning=NCIT.C2855)
    C121619 = PermissibleValue(text="C121619",
                                     description="Nongerminomatous Germ Cell Tumor",
                                     meaning=NCIT.C121619)
    C9014 = PermissibleValue(text="C9014",
                                 description="Cystic Teratoma",
                                 meaning=NCIT.C9014)
    C3819 = PermissibleValue(text="C3819",
                                 description="Primary Amyloidosis",
                                 meaning=NCIT.C3819)
    C6875 = PermissibleValue(text="C6875",
                                 description="Large Cell Neuroendocrine Carcinoma",
                                 meaning=NCIT.C6875)
    C4457 = PermissibleValue(text="C4457",
                                 description="Pleural Solitary Fibrous Tumor",
                                 meaning=NCIT.C4457)
    C43627 = PermissibleValue(text="C43627",
                                   description="Sarcomatoid Hepatocellular Carcinoma",
                                   meaning=NCIT.C43627)
    C4278 = PermissibleValue(text="C4278",
                                 description="Epithelial Synovial Sarcoma",
                                 meaning=NCIT.C4278)
    C4205 = PermissibleValue(text="C4205",
                                 description="Malignant Granulosa Cell Tumor",
                                 meaning=NCIT.C4205)
    C45754 = PermissibleValue(text="C45754",
                                   description="Cystic Tumor of the Atrioventricular Node",
                                   meaning=NCIT.C45754)
    C6469 = PermissibleValue(text="C6469",
                                 description="Osteosarcoma Arising in Paget Disease of Bone",
                                 meaning=NCIT.C6469)
    C65191 = PermissibleValue(text="C65191",
                                   description="Malignant Enteroglucagonoma",
                                   meaning=NCIT.C65191)
    C54317 = PermissibleValue(text="C54317",
                                   description="Odontoameloblastoma",
                                   meaning=NCIT.C54317)
    C4882 = PermissibleValue(text="C4882",
                                 description="Benign Muscle Neoplasm",
                                 meaning=NCIT.C4882)
    C94524 = PermissibleValue(text="C94524",
                                   description="Pituicytoma",
                                   meaning=NCIT.C94524)
    C3696 = PermissibleValue(text="C3696",
                                 description="Subependymal Giant Cell Astrocytoma",
                                 meaning=NCIT.C3696)
    C3302 = PermissibleValue(text="C3302",
                                 description="Extramammary Paget Disease",
                                 meaning=NCIT.C3302)
    C3287 = PermissibleValue(text="C3287",
                                 description="Odontoma",
                                 meaning=NCIT.C3287)
    C27255 = PermissibleValue(text="C27255",
                                   description="Eccrine Carcinoma",
                                   meaning=NCIT.C27255)
    C27005 = PermissibleValue(text="C27005",
                                   description="Spindle Cell Sarcoma",
                                   meaning=NCIT.C27005)
    C3358 = PermissibleValue(text="C3358",
                                 description="Rhabdomyoma",
                                 meaning=NCIT.C3358)
    C3398 = PermissibleValue(text="C3398",
                                 description="Sweat Gland Neoplasm",
                                 meaning=NCIT.C3398)
    C2857 = PermissibleValue(text="C2857",
                                 description="Pituitary Gland Chromophobe Adenoma",
                                 meaning=NCIT.C2857)
    C82596 = PermissibleValue(text="C82596",
                                   description="Refractory Cytopenia of Childhood",
                                   meaning=NCIT.C82596)
    C9150 = PermissibleValue(text="C9150",
                                 description="Botryoid-Type Embryonal Rhabdomyosarcoma",
                                 meaning=NCIT.C9150)
    C5754 = PermissibleValue(text="C5754",
                                 description="Clear Cell Hepatocellular Carcinoma",
                                 meaning=NCIT.C5754)
    C7362 = PermissibleValue(text="C7362",
                                 description="Breast Scirrhous Carcinoma",
                                 meaning=NCIT.C7362)
    C43356 = PermissibleValue(text="C43356",
                                   description="Syringofibroadenoma",
                                   meaning=NCIT.C43356)
    C4140 = PermissibleValue(text="C4140",
                                 description="Alveolar Adenoma",
                                 meaning=NCIT.C4140)
    C4225 = PermissibleValue(text="C4225",
                                 description="Cutaneous Nodular Melanoma",
                                 meaning=NCIT.C4225)
    C4232 = PermissibleValue(text="C4232",
                                 description="Melanoma in Junctional Nevus",
                                 meaning=NCIT.C4232)
    C4270 = PermissibleValue(text="C4270",
                                 description="Malignant Ovarian Brenner Tumor",
                                 meaning=NCIT.C4270)
    C45509 = PermissibleValue(text="C45509",
                                   description="Lung Fetal Adenocarcinoma",
                                   meaning=NCIT.C45509)
    C45327 = PermissibleValue(text="C45327",
                                   description="Hydroa Vacciniforme-Like Lymphoproliferative Disorder",
                                   meaning=NCIT.C45327)
    C4090 = PermissibleValue(text="C4090",
                                 description="Malignant Giant Cell Neoplasm",
                                 meaning=NCIT.C4090)
    C65186 = PermissibleValue(text="C65186",
                                   description="Malignant Pancreatic Insulinoma",
                                   meaning=NCIT.C65186)
    C4726 = PermissibleValue(text="C4726",
                                 description="Adamantinomatous Craniopharyngioma",
                                 meaning=NCIT.C4726)
    C3729 = PermissibleValue(text="C3729",
                                 description="Malignant Mixed Neoplasm",
                                 meaning=NCIT.C3729)
    C121932 = PermissibleValue(text="C121932",
                                     description="Giant Cell Tumor of Bone",
                                     meaning=NCIT.C121932)
    C156034 = PermissibleValue(text="C156034",
                                     description="Encapsulated Variant Thyroid Gland Papillary Carcinoma",
                                     meaning=NCIT.C156034)
    C6959 = PermissibleValue(text="C6959",
                                 description="Anaplastic Oligoastrocytoma",
                                 meaning=NCIT.C6959)
    C80307 = PermissibleValue(text="C80307",
                                   description="Waldenstrom Macroglobulinemia",
                                   meaning=NCIT.C80307)
    C8647 = PermissibleValue(text="C8647",
                                 description="Aggressive NK-Cell Leukemia",
                                 meaning=NCIT.C8647)
    C6846 = PermissibleValue(text="C6846",
                                 description="Thyroid Gland Hyalinizing Trabecular Tumor",
                                 meaning=NCIT.C6846)
    C4487 = PermissibleValue(text="C4487",
                                 description="Tufted Angioma",
                                 meaning=NCIT.C4487)
    C4306 = PermissibleValue(text="C4306",
                                 description="Benign Odontogenic Neoplasm",
                                 meaning=NCIT.C4306)
    C4227 = PermissibleValue(text="C4227",
                                 description="Balloon Cell Melanoma",
                                 meaning=NCIT.C4227)
    C4022 = PermissibleValue(text="C4022",
                                 description="Acral Lentiginous Melanoma",
                                 meaning=NCIT.C4022)
    C4019 = PermissibleValue(text="C4019",
                                 description="Breast Paget Disease and Intraductal Carcinoma",
                                 meaning=NCIT.C4019)
    C6557 = PermissibleValue(text="C6557",
                                 description="Schwannomatosis",
                                 meaning=NCIT.C6557)
    C27254 = PermissibleValue(text="C27254",
                                   description="Papillary Eccrine Carcinoma",
                                   meaning=NCIT.C27254)
    C2872 = PermissibleValue(text="C2872",
                                 description="Refractory Anemia",
                                 meaning=NCIT.C2872)
    C3181 = PermissibleValue(text="C3181",
                                 description="Prolymphocytic Leukemia",
                                 meaning=NCIT.C3181)
    C3169 = PermissibleValue(text="C3169",
                                 description="Mast Cell Leukemia",
                                 meaning=NCIT.C3169)
    C3188 = PermissibleValue(text="C3188",
                                 description="Leydig Cell Tumor",
                                 meaning=NCIT.C3188)
    C3049 = PermissibleValue(text="C3049",
                                 description="Ganglioneuroma",
                                 meaning=NCIT.C3049)
    C45508 = PermissibleValue(text="C45508",
                                   description="Lung Adenocarcinoma, Mixed Subtype",
                                   meaning=NCIT.C45508)
    C40069 = PermissibleValue(text="C40069",
                                   description="Borderline Ovarian Endometrioid Adenofibroma",
                                   meaning=NCIT.C40069)
    C82427 = PermissibleValue(text="C82427",
                                   description="Acute Myeloid Leukemia (Megakaryoblastic) with t(1;22)(p13.3;q13.1); RBM15-MKL1",
                                   meaning=NCIT.C82427)
    C8255 = PermissibleValue(text="C8255",
                                 description="Anal Canal Cloacogenic Carcinoma",
                                 meaning=NCIT.C8255)
    C82426 = PermissibleValue(text="C82426",
                                   description="Acute Myeloid Leukemia with inv(3) (q21.3;q26.2) or t(3;3) (q21.3;q26.2); GATA2, MECOM",
                                   meaning=NCIT.C82426)
    C7542 = PermissibleValue(text="C7542",
                                 description="Askin Tumor",
                                 meaning=NCIT.C7542)
    C3721 = PermissibleValue(text="C3721",
                                 description="Lymphomatoid Papulosis",
                                 meaning=NCIT.C3721)
    C4154 = PermissibleValue(text="C4154",
                                 description="Parathyroid Gland Chief Cell Adenoma",
                                 meaning=NCIT.C4154)
    C4293 = PermissibleValue(text="C4293",
                                 description="Partial Hydatidiform Mole",
                                 meaning=NCIT.C4293)
    C7492 = PermissibleValue(text="C7492",
                                 description="Ameloblastic Carcinoma",
                                 meaning=NCIT.C7492)
    C3802 = PermissibleValue(text="C3802",
                                 description="Amelanotic Melanoma",
                                 meaning=NCIT.C3802)
    C6923 = PermissibleValue(text="C6923",
                                 description="Acute Bilineal Leukemia",
                                 meaning=NCIT.C6923)
    C4725 = PermissibleValue(text="C4725",
                                 description="Papillary Craniopharyngioma",
                                 meaning=NCIT.C4725)
    C150495 = PermissibleValue(text="C150495",
                                     description="Intestinal T-Cell Lymphoma",
                                     meaning=NCIT.C150495)
    C36077 = PermissibleValue(text="C36077",
                                   description="Hilar Cholangiocarcinoma",
                                   meaning=NCIT.C36077)
    C3749 = PermissibleValue(text="C3749",
                                 description="Alveolar Rhabdomyosarcoma",
                                 meaning=NCIT.C3749)
    C3272 = PermissibleValue(text="C3272",
                                 description="Neurofibroma",
                                 meaning=NCIT.C3272)
    C34448 = PermissibleValue(text="C34448",
                                   description="Carcinosarcoma",
                                   meaning=NCIT.C34448)
    C27096 = PermissibleValue(text="C27096",
                                   description="Liver Embryonal Sarcoma",
                                   meaning=NCIT.C27096)
    C8252 = PermissibleValue(text="C8252",
                                 description="Therapy-Related Acute Myeloid Leukemia",
                                 meaning=NCIT.C8252)
    C3179 = PermissibleValue(text="C3179",
                                 description="Chronic Neutrophilic Leukemia",
                                 meaning=NCIT.C3179)
    C6914 = PermissibleValue(text="C6914",
                                 description="Hodgkin's Granuloma",
                                 meaning=NCIT.C6914)
    C65181 = PermissibleValue(text="C65181",
                                   description="Non-Invasive Papillary Transitional Cell Carcinoma",
                                   meaning=NCIT.C65181)
    C173820 = PermissibleValue(text="C173820",
                                     description="Ossifying Fibroma",
                                     meaning=NCIT.C173820)
    C157718 = PermissibleValue(text="C157718",
                                     description="Acquired Cystic Disease-Associated Renal Cell Carcinoma",
                                     meaning=NCIT.C157718)
    C9497 = PermissibleValue(text="C9497",
                                 description="Medulloblastoma with Melanotic Differentiation",
                                 meaning=NCIT.C9497)
    C82339 = PermissibleValue(text="C82339",
                                   description="Transient Abnormal Myelopoiesis Associated with Down Syndrome",
                                   meaning=NCIT.C82339)
    C43223 = PermissibleValue(text="C43223",
                                   description="Myeloid Leukemia Associated with Down Syndrome",
                                   meaning=NCIT.C43223)
    C4326 = PermissibleValue(text="C4326",
                                 description="Anaplastic Oligodendroglioma",
                                 meaning=NCIT.C4326)
    C4240 = PermissibleValue(text="C4240",
                                 description="Melanoma Arising from Blue Nevus",
                                 meaning=NCIT.C4240)
    C40345 = PermissibleValue(text="C40345",
                                   description="Testicular Germ Cell Neoplasia In Situ",
                                   meaning=NCIT.C40345)
    C26749 = PermissibleValue(text="C26749",
                                   description="VIP-Producing Neuroendocrine Tumor",
                                   meaning=NCIT.C26749)
    C3698 = PermissibleValue(text="C3698",
                                 description="Choroid Plexus Papilloma",
                                 meaning=NCIT.C3698)
    C3744 = PermissibleValue(text="C3744",
                                 description="Breast Fibroadenoma",
                                 meaning=NCIT.C3744)
    C3790 = PermissibleValue(text="C3790",
                                 description="Ganglioneuroblastoma",
                                 meaning=NCIT.C3790)
    C3775 = PermissibleValue(text="C3775",
                                 description="Adnexal Carcinoma",
                                 meaning=NCIT.C3775)
    C27502 = PermissibleValue(text="C27502",
                                   description="Extraskeletal Myxoid Chondrosarcoma",
                                   meaning=NCIT.C27502)
    C3164 = PermissibleValue(text="C3164",
                                 description="Acute Basophilic Leukemia",
                                 meaning=NCIT.C3164)
    C66751 = PermissibleValue(text="C66751",
                                   description="Granulosa Cell-Theca Cell Tumor",
                                   meaning=NCIT.C66751)
    C66801 = PermissibleValue(text="C66801",
                                   description="Polar Spongioblastoma",
                                   meaning=NCIT.C66801)
    C66745 = PermissibleValue(text="C66745",
                                   description="Adenocarcinoma with Neuroendocrine Differentiation",
                                   meaning=NCIT.C66745)
    C66777 = PermissibleValue(text="C66777",
                                   description="Choriocarcinoma Combined with Other Germ Cell Elements",
                                   meaning=NCIT.C66777)
    C66759 = PermissibleValue(text="C66759",
                                   description="Giant Cell Sarcoma",
                                   meaning=NCIT.C66759)
    C65163 = PermissibleValue(text="C65163",
                                   description="Papillary Carcinoma In Situ",
                                   meaning=NCIT.C65163)
    C65176 = PermissibleValue(text="C65176",
                                   description="Squamous Cell Carcinoma In Situ with Questionable Stromal Invasion",
                                   meaning=NCIT.C65176)
    C53457 = PermissibleValue(text="C53457",
                                   description="Multiple Osteochondromas",
                                   meaning=NCIT.C53457)
    C95458 = PermissibleValue(text="C95458",
                                   description="Pancreatic Mixed Acinar-Ductal Carcinoma",
                                   meaning=NCIT.C95458)
    C4338 = PermissibleValue(text="C4338",
                                 description="Diffuse Centroblastic-Centrocytic Lymphoma",
                                 meaning=NCIT.C4338)
    C27825 = PermissibleValue(text="C27825",
                                   description="Mucin-Producing Carcinoma",
                                   meaning=NCIT.C27825)
    C27095 = PermissibleValue(text="C27095",
                                   description="Nonpigmented Nevus",
                                   meaning=NCIT.C27095)
    C3405 = PermissibleValue(text="C3405",
                                 description="Thecoma",
                                 meaning=NCIT.C3405)
    C3233 = PermissibleValue(text="C3233",
                                 description="Mesenchymoma",
                                 meaning=NCIT.C3233)
    C12922 = PermissibleValue(text="C12922",
                                   description="Neoplastic Cell",
                                   meaning=NCIT.C12922)
    C6088 = PermissibleValue(text="C6088",
                                 description="Ceruminous Adenoma",
                                 meaning=NCIT.C6088)
    C6040 = PermissibleValue(text="C6040",
                                 description="Poorly Differentiated Thyroid Gland Carcinoma",
                                 meaning=NCIT.C6040)
    C6915 = PermissibleValue(text="C6915",
                                 description="Primary Effusion Lymphoma",
                                 meaning=NCIT.C6915)
    C4883 = PermissibleValue(text="C4883",
                                 description="Malignant Muscle Neoplasm",
                                 meaning=NCIT.C4883)
    C4470 = PermissibleValue(text="C4470",
                                 description="Perifollicular Fibroma",
                                 meaning=NCIT.C4470)
    C4310 = PermissibleValue(text="C4310",
                                 description="Adenomatoid Odontogenic Tumor",
                                 meaning=NCIT.C4310)
    C4122 = PermissibleValue(text="C4122",
                                 description="Papillary Transitional Cell Carcinoma",
                                 meaning=NCIT.C4122)
    C4156 = PermissibleValue(text="C4156",
                                 description="Water-Clear Cell Adenocarcinoma",
                                 meaning=NCIT.C4156)
    C4202 = PermissibleValue(text="C4202",
                                 description="Adenocarcinoma with Apocrine Metaplasia",
                                 meaning=NCIT.C4202)
    C65164 = PermissibleValue(text="C65164",
                                   description="Non-Invasive Papillary Squamous Cell Carcinoma",
                                   meaning=NCIT.C65164)
    C65175 = PermissibleValue(text="C65175",
                                   description="Non-Keratinizing Small Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C65175)
    C65194 = PermissibleValue(text="C65194",
                                   description="Gastric Parietal Cell Adenocarcinoma",
                                   meaning=NCIT.C65194)
    C9498 = PermissibleValue(text="C9498",
                                 description="Melanocytoma",
                                 meaning=NCIT.C9498)
    C5728 = PermissibleValue(text="C5728",
                                 description="Solid Pseudopapillary Carcinoma of the Pancreas",
                                 meaning=NCIT.C5728)
    C37212 = PermissibleValue(text="C37212",
                                   description="Solid Pseudopapillary Neoplasm of the Pancreas",
                                   meaning=NCIT.C37212)
    C136709 = PermissibleValue(text="C136709",
                                     description="Invasive Lung Mucinous Adenocarcinoma",
                                     meaning=NCIT.C136709)
    C4037 = PermissibleValue(text="C4037",
                                 description="Acute Myeloid Leukemia Arising from Previous Myelodysplastic Syndrome",
                                 meaning=NCIT.C4037)
    C8300 = PermissibleValue(text="C8300",
                                 description="Desmoplastic Small Round Cell Tumor",
                                 meaning=NCIT.C8300)
    C7951 = PermissibleValue(text="C7951",
                                 description="Breast Paget Disease with Invasive Ductal Carcinoma",
                                 meaning=NCIT.C7951)
    C8975 = PermissibleValue(text="C8975",
                                 description="Malignant Mixed Mesodermal (Mullerian) Tumor",
                                 meaning=NCIT.C8975)
    C2853 = PermissibleValue(text="C2853",
                                 description="Papillary Adenocarcinoma",
                                 meaning=NCIT.C2853)
    C5669 = PermissibleValue(text="C5669",
                                 description="Pleuropulmonary Blastoma",
                                 meaning=NCIT.C5669)
    C4212 = PermissibleValue(text="C4212",
                                 description="Benign Leydig Cell Tumor",
                                 meaning=NCIT.C4212)
    C9010 = PermissibleValue(text="C9010",
                                 description="Mixed Teratoma and Seminoma",
                                 meaning=NCIT.C9010)
    C2947 = PermissibleValue(text="C2947",
                                 description="Chordoma",
                                 meaning=NCIT.C2947)
    C3708 = PermissibleValue(text="C3708",
                                 description="Germ Cell Tumor",
                                 meaning=NCIT.C3708)
    C39968 = PermissibleValue(text="C39968",
                                   description="Moderately Differentiated Ovarian Sertoli-Leydig Cell Tumor",
                                   meaning=NCIT.C39968)
    C3043 = PermissibleValue(text="C3043",
                                 description="Fibrosarcoma",
                                 meaning=NCIT.C3043)
    C7660 = PermissibleValue(text="C7660",
                                 description="Grade II Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C7660)
    C7567 = PermissibleValue(text="C7567",
                                 description="Clear Cell Hidradenoma",
                                 meaning=NCIT.C7567)
    C4879 = PermissibleValue(text="C4879",
                                 description="Benign Sweat Gland Neoplasm",
                                 meaning=NCIT.C4879)
    C66950 = PermissibleValue(text="C66950",
                                   description="Hepatoid Adenocarcinoma",
                                   meaning=NCIT.C66950)
    C7357 = PermissibleValue(text="C7357",
                                 description="Periosteal Chondrosarcoma",
                                 meaning=NCIT.C7357)
    C7438 = PermissibleValue(text="C7438",
                                 description="Infiltrating Papillary Adenocarcinoma",
                                 meaning=NCIT.C7438)
    C7018 = PermissibleValue(text="C7018",
                                 description="Nerve Sheath Myxoma",
                                 meaning=NCIT.C7018)
    C5609 = PermissibleValue(text="C5609",
                                 description="Anal Glands Adenocarcinoma",
                                 meaning=NCIT.C5609)
    C5560 = PermissibleValue(text="C5560",
                                 description="Porocarcinoma",
                                 meaning=NCIT.C5560)
    C4302 = PermissibleValue(text="C4302",
                                 description="Periosteal Chondroma",
                                 meaning=NCIT.C4302)
    C4317 = PermissibleValue(text="C4317",
                                 description="Ameloblastic Fibrosarcoma",
                                 meaning=NCIT.C4317)
    C4321 = PermissibleValue(text="C4321",
                                 description="Gemistocytic Astrocytoma",
                                 meaning=NCIT.C4321)
    C4330 = PermissibleValue(text="C4330",
                                 description="Fibrous Meningioma",
                                 meaning=NCIT.C4330)
    C4171 = PermissibleValue(text="C4171",
                                 description="Hidradenoma Papilliferum",
                                 meaning=NCIT.C4171)
    C4251 = PermissibleValue(text="C4251",
                                 description="Fibromyxolipoma",
                                 meaning=NCIT.C4251)
    C4292 = PermissibleValue(text="C4292",
                                 description="Strumal Carcinoid",
                                 meaning=NCIT.C4292)
    C4235 = PermissibleValue(text="C4235",
                                 description="Melanoma Arising in Giant Congenital Nevus",
                                 meaning=NCIT.C4235)
    C40223 = PermissibleValue(text="C40223",
                                   description="Uterine Corpus Low Grade Endometrial Stromal Sarcoma",
                                   meaning=NCIT.C40223)
    C27483 = PermissibleValue(text="C27483",
                                   description="Lipoblastoma",
                                   meaning=NCIT.C27483)
    C45512 = PermissibleValue(text="C45512",
                                   description="Lung Colloid Adenocarcinoma",
                                   meaning=NCIT.C45512)
    C65153 = PermissibleValue(text="C65153",
                                   description="Malignant Neoplasm, Uncertain Whether Primary or Metastatic",
                                   meaning=NCIT.C65153)
    C3804 = PermissibleValue(text="C3804",
                                 description="Dermal Nevus",
                                 meaning=NCIT.C3804)
    C3681 = PermissibleValue(text="C3681",
                                 description="Granular Cell Carcinoma",
                                 meaning=NCIT.C3681)
    C3680 = PermissibleValue(text="C3680",
                                 description="Cribriform Carcinoma",
                                 meaning=NCIT.C3680)
    C3707 = PermissibleValue(text="C3707",
                                 description="Meningiomatosis",
                                 meaning=NCIT.C3707)
    C3784 = PermissibleValue(text="C3784",
                                 description="Basal Cell Neoplasm",
                                 meaning=NCIT.C3784)
    C27884 = PermissibleValue(text="C27884",
                                   description="Bladder Papillary Urothelial Neoplasm of Low Malignant Potential",
                                   meaning=NCIT.C27884)
    C82423 = PermissibleValue(text="C82423",
                                   description="Acute Myeloid Leukemia with t(6;9) (p23;q34.1); DEK-NUP214",
                                   meaning=NCIT.C82423)
    C6966 = PermissibleValue(text="C6966",
                                 description="Pineocytoma",
                                 meaning=NCIT.C6966)
    C3694 = PermissibleValue(text="C3694",
                                 description="Dysplastic Nevus",
                                 meaning=NCIT.C3694)
    C3750 = PermissibleValue(text="C3750",
                                 description="Alveolar Soft Part Sarcoma",
                                 meaning=NCIT.C3750)
    C3740 = PermissibleValue(text="C3740",
                                 description="Desmoplastic Fibroma",
                                 meaning=NCIT.C3740)
    C27780 = PermissibleValue(text="C27780",
                                   description="Myelodysplastic/Myeloproliferative Neoplasm, Unclassifiable",
                                   meaning=NCIT.C27780)
    C8381 = PermissibleValue(text="C8381",
                                 description="Florid Cemento-Osseous Dysplasia",
                                 meaning=NCIT.C8381)
    C66845 = PermissibleValue(text="C66845",
                                   description="Malignant Peripheral Nerve Sheath Tumor with Perineurial Differentiation",
                                   meaning=NCIT.C66845)
    C67012 = PermissibleValue(text="C67012",
                                   description="Benign Sertoli Cell Tumor",
                                   meaning=NCIT.C67012)
    C6930 = PermissibleValue(text="C6930",
                                 description="Mixed Neoplasm",
                                 meaning=NCIT.C6930)
    C7202 = PermissibleValue(text="C7202",
                                 description="Malignant Histiocytosis",
                                 meaning=NCIT.C7202)
    C27270 = PermissibleValue(text="C27270",
                                   description="Hodgkin's Disease, Nodular Sclerosis, Lymphocyte Predominance",
                                   meaning=NCIT.C27270)
    C6889 = PermissibleValue(text="C6889",
                                 description="Malignant Type B2 Thymoma",
                                 meaning=NCIT.C6889)
    C92555 = PermissibleValue(text="C92555",
                                   description="Extraventricular Neurocytoma",
                                   meaning=NCIT.C92555)
    C6886 = PermissibleValue(text="C6886",
                                 description="Malignant Type AB Thymoma",
                                 meaning=NCIT.C6886)
    C4333 = PermissibleValue(text="C4333",
                                 description="Transitional Meningioma",
                                 meaning=NCIT.C4333)
    C4160 = PermissibleValue(text="C4160",
                                 description="Thyroid Gland Microfollicular Adenoma",
                                 meaning=NCIT.C4160)
    C4177 = PermissibleValue(text="C4177",
                                 description="Borderline Serous Cystadenoma",
                                 meaning=NCIT.C4177)
    C4170 = PermissibleValue(text="C4170",
                                 description="Spiradenoma",
                                 meaning=NCIT.C4170)
    C4176 = PermissibleValue(text="C4176",
                                 description="Ceruminous Adenocarcinoma",
                                 meaning=NCIT.C4176)
    C4298 = PermissibleValue(text="C4298",
                                 description="Epithelioid Hemangioma",
                                 meaning=NCIT.C4298)
    C4277 = PermissibleValue(text="C4277",
                                 description="Spindle Cell Synovial Sarcoma",
                                 meaning=NCIT.C4277)
    C4282 = PermissibleValue(text="C4282",
                                 description="Biphasic Mesothelioma",
                                 meaning=NCIT.C4282)
    C4274 = PermissibleValue(text="C4274",
                                 description="Benign Phyllodes Tumor",
                                 meaning=NCIT.C4274)
    C4023 = PermissibleValue(text="C4023",
                                 description="Small Cell Osteosarcoma",
                                 meaning=NCIT.C4023)
    C4068 = PermissibleValue(text="C4068",
                                 description="Trabecular Adenocarcinoma",
                                 meaning=NCIT.C4068)
    C39921 = PermissibleValue(text="C39921",
                                   description="Testicular Spermatocytic Tumor",
                                   meaning=NCIT.C39921)
    C40080 = PermissibleValue(text="C40080",
                                   description="Borderline Ovarian Clear Cell Tumor",
                                   meaning=NCIT.C40080)
    C40081 = PermissibleValue(text="C40081",
                                   description="Borderline Ovarian Clear Cell Adenofibroma",
                                   meaning=NCIT.C40081)
    C39920 = PermissibleValue(text="C39920",
                                   description="Testicular Seminoma with High Mitotic Index",
                                   meaning=NCIT.C39920)
    C65192 = PermissibleValue(text="C65192",
                                   description="Tubular Adenocarcinoma",
                                   meaning=NCIT.C65192)
    C3803 = PermissibleValue(text="C3803",
                                 description="Blue Nevus",
                                 meaning=NCIT.C3803)
    C9430 = PermissibleValue(text="C9430",
                                 description="Pigmented Dermatofibrosarcoma Protuberans",
                                 meaning=NCIT.C9430)
    C96830 = PermissibleValue(text="C96830",
                                   description="Calcifying Nested Stromal-Epithelial Tumor of the Liver",
                                   meaning=NCIT.C96830)
    C6536 = PermissibleValue(text="C6536",
                                 description="Peritoneal Multicystic Mesothelioma",
                                 meaning=NCIT.C6536)
    C3778 = PermissibleValue(text="C3778",
                                 description="Serous Cystadenocarcinoma",
                                 meaning=NCIT.C3778)
    C43352 = PermissibleValue(text="C43352",
                                   description="Turban Tumor",
                                   meaning=NCIT.C43352)
    C4131 = PermissibleValue(text="C4131",
                                 description="Fibrolamellar Carcinoma",
                                 meaning=NCIT.C4131)
    C4001 = PermissibleValue(text="C4001",
                                 description="Breast Inflammatory Carcinoma",
                                 meaning=NCIT.C4001)
    C9477 = PermissibleValue(text="C9477",
                                 description="Anaplastic Astrocytoma",
                                 meaning=NCIT.C9477)
    C3308 = PermissibleValue(text="C3308",
                                 description="Paraganglioma",
                                 meaning=NCIT.C3308)
    C27790 = PermissibleValue(text="C27790",
                                   description="Penile Carcinoma In Situ",
                                   meaning=NCIT.C27790)
    C67171 = PermissibleValue(text="C67171",
                                   description="Nodular Sclerosis Classic Hodgkin Lymphoma, Cellular Phase",
                                   meaning=NCIT.C67171)
    C8969 = PermissibleValue(text="C8969",
                                 description="Parosteal Osteosarcoma",
                                 meaning=NCIT.C8969)
    C6780 = PermissibleValue(text="C6780",
                                 description="Pituitary Gland Acidophil Adenoma",
                                 meaning=NCIT.C6780)
    C4159 = PermissibleValue(text="C4159",
                                 description="Lipoadenoma",
                                 meaning=NCIT.C4159)
    C4294 = PermissibleValue(text="C4294",
                                 description="Benign Mesonephroma",
                                 meaning=NCIT.C4294)
    C4268 = PermissibleValue(text="C4268",
                                 description="Malignant Mesenchymoma",
                                 meaning=NCIT.C4268)
    C7442 = PermissibleValue(text="C7442",
                                 description="Benign Myoepithelioma",
                                 meaning=NCIT.C7442)
    C3901 = PermissibleValue(text="C3901",
                                 description="Compound Nevus",
                                 meaning=NCIT.C3901)
    C6454 = PermissibleValue(text="C6454",
                                 description="Thymoma Type A",
                                 meaning=NCIT.C6454)
    C4754 = PermissibleValue(text="C4754",
                                 description="Spindle Cell Hemangioma",
                                 meaning=NCIT.C4754)
    C3801 = PermissibleValue(text="C3801",
                                 description="Hemangioblastoma",
                                 meaning=NCIT.C3801)
    C3777 = PermissibleValue(text="C3777",
                                 description="Papillary Cystadenocarcinoma",
                                 meaning=NCIT.C3777)
    C27729 = PermissibleValue(text="C27729",
                                   description="Thyroid Gland Well-Differentiated Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C27729)
    C27949 = PermissibleValue(text="C27949",
                                   description="Metaplastic Carcinoma",
                                   meaning=NCIT.C27949)
    C27510 = PermissibleValue(text="C27510",
                                   description="Kaposiform Hemangioendothelioma",
                                   meaning=NCIT.C27510)
    C9285 = PermissibleValue(text="C9285",
                                 description="Aggressive Systemic Mastocytosis",
                                 meaning=NCIT.C9285)
    C7526 = PermissibleValue(text="C7526",
                                 description="Papillary Intralymphatic Angioendothelioma",
                                 meaning=NCIT.C7526)
    C27808 = PermissibleValue(text="C27808",
                                   description="Hodgkin's Disease, Nodular Sclerosis, Lymphocyte Depletion",
                                   meaning=NCIT.C27808)
    C43372 = PermissibleValue(text="C43372",
                                   description="Lentigo Maligna",
                                   meaning=NCIT.C43372)
    C4322 = PermissibleValue(text="C4322",
                                 description="Fibrillary Astrocytoma",
                                 meaning=NCIT.C4322)
    C4161 = PermissibleValue(text="C4161",
                                 description="Thyroid Gland Macrofollicular Adenoma",
                                 meaning=NCIT.C4161)
    C4192 = PermissibleValue(text="C4192",
                                 description="Nipple Adenoma",
                                 meaning=NCIT.C4192)
    C4275 = PermissibleValue(text="C4275",
                                 description="Malignant Phyllodes Tumor",
                                 meaning=NCIT.C4275)
    C65188 = PermissibleValue(text="C65188",
                                   description="Malignant Gastrinoma",
                                   meaning=NCIT.C65188)
    C129499 = PermissibleValue(text="C129499",
                                     description="Embryonal Tumor with Multilayered Rosettes, Not Otherwise Specified",
                                     meaning=NCIT.C129499)
    C4049 = PermissibleValue(text="C4049",
                                 description="Anaplastic Ependymoma",
                                 meaning=NCIT.C4049)
    C2972 = PermissibleValue(text="C2972",
                                 description="Cystadenoma",
                                 meaning=NCIT.C2972)
    C4716 = PermissibleValue(text="C4716",
                                 description="Ectomesenchymoma",
                                 meaning=NCIT.C4716)
    C9308 = PermissibleValue(text="C9308",
                                 description="Lymphoproliferative Disorder",
                                 meaning=NCIT.C9308)
    C37257 = PermissibleValue(text="C37257",
                                   description="Desmoplastic Melanoma",
                                   meaning=NCIT.C37257)
    C3754 = PermissibleValue(text="C3754",
                                 description="Gonadoblastoma",
                                 meaning=NCIT.C3754)
    C3286 = PermissibleValue(text="C3286",
                                 description="Odontogenic Neoplasm",
                                 meaning=NCIT.C3286)
    C3474 = PermissibleValue(text="C3474",
                                 description="Granular Cell Tumor",
                                 meaning=NCIT.C3474)
    C27091 = PermissibleValue(text="C27091",
                                   description="Malignant Spindle Cell Neoplasm",
                                   meaning=NCIT.C27091)
    C27080 = PermissibleValue(text="C27080",
                                   description="Refractory Anemia with Excess Blasts in Transformation",
                                   meaning=NCIT.C27080)
    C9152 = PermissibleValue(text="C9152",
                                 description="Low-CSD Melanoma",
                                 meaning=NCIT.C9152)
    C9119 = PermissibleValue(text="C9119",
                                 description="Breast Medullary Carcinoma",
                                 meaning=NCIT.C9119)
    C6569 = PermissibleValue(text="C6569",
                                 description="Congenital Mesoblastic Nephroma",
                                 meaning=NCIT.C6569)
    C27720 = PermissibleValue(text="C27720",
                                   description="Pancreatic Neuroendocrine Tumor",
                                   meaning=NCIT.C27720)
    C2996 = PermissibleValue(text="C2996",
                                 description="Dysgerminoma",
                                 meaning=NCIT.C2996)
    C7985 = PermissibleValue(text="C7985",
                                 description="Epithelioid Mesothelioma",
                                 meaning=NCIT.C7985)
    C9151 = PermissibleValue(text="C9151",
                                 description="Lentigo Maligna Melanoma",
                                 meaning=NCIT.C9151)
    C4314 = PermissibleValue(text="C4314",
                                 description="Odontogenic Fibroma",
                                 meaning=NCIT.C4314)
    C4162 = PermissibleValue(text="C4162",
                                 description="Juxtaglomerular Cell Tumor",
                                 meaning=NCIT.C4162)
    C3842 = PermissibleValue(text="C3842",
                                 description="Urothelial Papilloma",
                                 meaning=NCIT.C3842)
    C4002 = PermissibleValue(text="C4002",
                                 description="Extraosseous Plasmacytoma",
                                 meaning=NCIT.C4002)
    C54301 = PermissibleValue(text="C54301",
                                   description="Calcifying Epithelial Odontogenic Tumor",
                                   meaning=NCIT.C54301)
    C9281 = PermissibleValue(text="C9281",
                                 description="Follicular Dendritic Cell Sarcoma",
                                 meaning=NCIT.C9281)
    C3756 = PermissibleValue(text="C3756",
                                 description="Mixed Embryonal Carcinoma and Teratoma",
                                 meaning=NCIT.C3756)
    C3742 = PermissibleValue(text="C3742",
                                 description="Myofibromatosis",
                                 meaning=NCIT.C3742)
    C3796 = PermissibleValue(text="C3796",
                                 description="Gliosarcoma",
                                 meaning=NCIT.C3796)
    C27388 = PermissibleValue(text="C27388",
                                   description="Scirrhous Hepatocellular Carcinoma",
                                   meaning=NCIT.C27388)
    C27781 = PermissibleValue(text="C27781",
                                   description="Myxoid Liposarcoma",
                                   meaning=NCIT.C27781)
    C2856 = PermissibleValue(text="C2856",
                                 description="Pituitary Gland Basophil Adenoma",
                                 meaning=NCIT.C2856)
    C3059 = PermissibleValue(text="C3059",
                                 description="Glioma",
                                 meaning=NCIT.C3059)
    C3829 = PermissibleValue(text="C3829",
                                 description="Benign Synovial Neoplasm",
                                 meaning=NCIT.C3829)
    C8461 = PermissibleValue(text="C8461",
                                 description="Tibial Adamantinoma",
                                 meaning=NCIT.C8461)
    C3273 = PermissibleValue(text="C3273",
                                 description="Neurofibromatosis Type 1",
                                 meaning=NCIT.C3273)
    C7457 = PermissibleValue(text="C7457",
                                 description="Capillary Hemangioma",
                                 meaning=NCIT.C7457)
    C4810 = PermissibleValue(text="C4810",
                                 description="Malignant Sweat Gland Neoplasm",
                                 meaning=NCIT.C4810)
    C5592 = PermissibleValue(text="C5592",
                                 description="Chordoid Glioma of the Third Ventricle",
                                 meaning=NCIT.C5592)
    C4200 = PermissibleValue(text="C4200",
                                 description="Adenocarcinoma with Squamous Metaplasia",
                                 meaning=NCIT.C4200)
    C4102 = PermissibleValue(text="C4102",
                                 description="Papillary Squamous Cell Carcinoma",
                                 meaning=NCIT.C4102)
    C4214 = PermissibleValue(text="C4214",
                                 description="Ovarian Hilus Cell Tumor",
                                 meaning=NCIT.C4214)
    C8312 = PermissibleValue(text="C8312",
                                 description="Leptomeningeal Sarcoma",
                                 meaning=NCIT.C8312)
    C54287 = PermissibleValue(text="C54287",
                                   description="Sinonasal Non-Keratinizing Squamous Cell Carcinoma",
                                   meaning=NCIT.C54287)
    C53999 = PermissibleValue(text="C53999",
                                   description="Malignant Gastrointestinal Stromal Tumor",
                                   meaning=NCIT.C53999)
    C3714 = PermissibleValue(text="C3714",
                                 description="Epithelioid Sarcoma",
                                 meaning=NCIT.C3714)
    C3732 = PermissibleValue(text="C3732",
                                 description="Pulmonary Blastoma",
                                 meaning=NCIT.C3732)
    C3764 = PermissibleValue(text="C3764",
                                 description="Adenomatous Polyp",
                                 meaning=NCIT.C3764)
    C3329 = PermissibleValue(text="C3329",
                                 description="Pituitary Gland Adenoma",
                                 meaning=NCIT.C3329)
    C8459 = PermissibleValue(text="C8459",
                                 description="Hepatosplenic T-Cell Lymphoma",
                                 meaning=NCIT.C8459)
    C4246 = PermissibleValue(text="C4246",
                                 description="Atypical Fibroxanthoma",
                                 meaning=NCIT.C4246)
    C9022 = PermissibleValue(text="C9022",
                                 description="Childhood Astrocytic Tumor",
                                 meaning=NCIT.C9022)
    C6561 = PermissibleValue(text="C6561",
                                 description="Epithelioid Malignant Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C6561)
    C47857 = PermissibleValue(text="C47857",
                                   description="Breast Paget Disease",
                                   meaning=NCIT.C47857)
    C81767 = PermissibleValue(text="C81767",
                                   description="Indeterminate Dendritic Cell Tumor",
                                   meaning=NCIT.C81767)
    C6877 = PermissibleValue(text="C6877",
                                 description="Grade III Glandular Intraepithelial Neoplasia",
                                 meaning=NCIT.C6877)
    C3725 = PermissibleValue(text="C3725",
                                 description="Lymphangioleiomyomatosis",
                                 meaning=NCIT.C3725)
    C3710 = PermissibleValue(text="C3710",
                                 description="Ameloblastic Fibro-Odontoma",
                                 meaning=NCIT.C3710)
    C3797 = PermissibleValue(text="C3797",
                                 description="Plexiform Neurofibroma",
                                 meaning=NCIT.C3797)
    C27349 = PermissibleValue(text="C27349",
                                   description="Histiocytic Sarcoma",
                                   meaning=NCIT.C27349)
    C27893 = PermissibleValue(text="C27893",
                                   description="Sarcomatoid Renal Cell Carcinoma",
                                   meaning=NCIT.C27893)
    C3061 = PermissibleValue(text="C3061",
                                 description="Jugulotympanic Paraganglioma",
                                 meaning=NCIT.C3061)
    C9309 = PermissibleValue(text="C9309",
                                 description="Seminoma",
                                 meaning=NCIT.C9309)
    C7580 = PermissibleValue(text="C7580",
                                 description="Skin Appendage Adenoma",
                                 meaning=NCIT.C7580)
    C7596 = PermissibleValue(text="C7596",
                                 description="Malignant Myoepithelioma",
                                 meaning=NCIT.C7596)
    C8422 = PermissibleValue(text="C8422",
                                 description="Cemento-Ossifying Fibroma",
                                 meaning=NCIT.C8422)
    C4336 = PermissibleValue(text="C4336",
                                 description="Malignant Granular Cell Tumor",
                                 meaning=NCIT.C4336)
    C4186 = PermissibleValue(text="C4186",
                                 description="Borderline Papillary Mucinous Cystadenoma",
                                 meaning=NCIT.C4186)
    C4244 = PermissibleValue(text="C4244",
                                 description="Infantile Fibrosarcoma",
                                 meaning=NCIT.C4244)
    C82616 = PermissibleValue(text="C82616",
                                   description="Myelodysplastic/Myeloproliferative Neoplasm with Ring Sideroblasts and Thrombocytosis",
                                   meaning=NCIT.C82616)
    C6535 = PermissibleValue(text="C6535",
                                 description="Malignant Tenosynovial Giant Cell Tumor",
                                 meaning=NCIT.C6535)
    C62571 = PermissibleValue(text="C62571",
                                   description="Bowen Disease of the Skin",
                                   meaning=NCIT.C62571)
    C2922 = PermissibleValue(text="C2922",
                                 description="Skin Basosquamous Cell Carcinoma",
                                 meaning=NCIT.C2922)
    C9474 = PermissibleValue(text="C9474",
                                 description="Adenosarcoma",
                                 meaning=NCIT.C9474)
    C67457 = PermissibleValue(text="C67457",
                                   description="Pancreatic Beta Cell Adenoma",
                                   meaning=NCIT.C67457)
    C65173 = PermissibleValue(text="C65173",
                                   description="Non-Keratinizing Large Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C65173)
    C95915 = PermissibleValue(text="C95915",
                                   description="Ampullary Noninvasive Pancreatobiliary Papillary Neoplasm with High Grade Dysplasia",
                                   meaning=NCIT.C95915)
    C7634 = PermissibleValue(text="C7634",
                                 description="Solitary Fibrous Tumor",
                                 meaning=NCIT.C7634)
    C4020 = PermissibleValue(text="C4020",
                                 description="Fibroblastic Osteosarcoma",
                                 meaning=NCIT.C4020)
    C7950 = PermissibleValue(text="C7950",
                                 description="Invasive Breast Lobular Carcinoma",
                                 meaning=NCIT.C7950)
    C27257 = PermissibleValue(text="C27257",
                                   description="Cellular Angiofibroma",
                                   meaning=NCIT.C27257)
    C3294 = PermissibleValue(text="C3294",
                                 description="Osteoblastoma",
                                 meaning=NCIT.C3294)
    C7680 = PermissibleValue(text="C7680",
                                 description="Adenocarcinoma In Situ in a Polyp",
                                 meaning=NCIT.C7680)
    C27813 = PermissibleValue(text="C27813",
                                   description="Bile Duct Adenocarcinoma",
                                   meaning=NCIT.C27813)
    C4536 = PermissibleValue(text="C4536",
                                 description="Pituitary Gland Carcinoma",
                                 meaning=NCIT.C4536)
    C3328 = PermissibleValue(text="C3328",
                                 description="Pineal Region Neoplasm",
                                 meaning=NCIT.C3328)
    C7351 = PermissibleValue(text="C7351",
                                 description="Grade II Squamous Intraepithelial Neoplasia",
                                 meaning=NCIT.C7351)
    C4213 = PermissibleValue(text="C4213",
                                 description="Malignant Leydig Cell Tumor",
                                 meaning=NCIT.C4213)
    C4683 = PermissibleValue(text="C4683",
                                 description="Dermatofibrosarcoma Protuberans",
                                 meaning=NCIT.C4683)
    C9020 = PermissibleValue(text="C9020",
                                 description="Acute Myelomonocytic Leukemia with Abnormal Eosinophils",
                                 meaning=NCIT.C9020)
    C2882 = PermissibleValue(text="C2882",
                                 description="Arteriovenous Malformation/Hemangioma",
                                 meaning=NCIT.C2882)
    C3192 = PermissibleValue(text="C3192",
                                 description="Lipoma",
                                 meaning=NCIT.C3192)
    C66850 = PermissibleValue(text="C66850",
                                   description="Follicular Variant Thyroid Gland Papillary Carcinoma, Encapsulated Subtype with Invasion",
                                   meaning=NCIT.C66850)
    C4329 = PermissibleValue(text="C4329",
                                 description="Meningothelial Meningioma",
                                 meaning=NCIT.C4329)
    C4105 = PermissibleValue(text="C4105",
                                 description="Keratinizing Squamous Cell Carcinoma",
                                 meaning=NCIT.C4105)
    C46105 = PermissibleValue(text="C46105",
                                   description="Thyroid Gland Spindle Cell Tumor with Thymus-Like Differentiation",
                                   meaning=NCIT.C46105)
    C6929 = PermissibleValue(text="C6929",
                                 description="Malignant Ovarian Thecoma",
                                 meaning=NCIT.C6929)
    C4195 = PermissibleValue(text="C4195",
                                 description="Breast Ductal Carcinoma In Situ and Lobular Carcinoma In Situ",
                                 meaning=NCIT.C4195)
    C5139 = PermissibleValue(text="C5139",
                                 description="Breast Micropapillary Ductal Carcinoma In Situ",
                                 meaning=NCIT.C5139)
    C3158 = PermissibleValue(text="C3158",
                                 description="Leiomyosarcoma",
                                 meaning=NCIT.C3158)
    C3411 = PermissibleValue(text="C3411",
                                 description="Thymoma",
                                 meaning=NCIT.C3411)
    C3345 = PermissibleValue(text="C3345",
                                 description="Pseudomyxoma Peritonei",
                                 meaning=NCIT.C3345)
    C3379 = PermissibleValue(text="C3379",
                                 description="Somatostatin-Producing Neuroendocrine Tumor",
                                 meaning=NCIT.C3379)
    C4871 = PermissibleValue(text="C4871",
                                 description="Complete Hydatidiform Mole",
                                 meaning=NCIT.C4871)
    C3202 = PermissibleValue(text="C3202",
                                 description="Ovarian Stromal Luteoma",
                                 meaning=NCIT.C3202)
    C43326 = PermissibleValue(text="C43326",
                                   description="Trichilemmal Carcinoma",
                                   meaning=NCIT.C43326)
    C3774 = PermissibleValue(text="C3774",
                                 description="Signet Ring Cell Carcinoma",
                                 meaning=NCIT.C3774)
    C2945 = PermissibleValue(text="C2945",
                                 description="Chondroblastoma",
                                 meaning=NCIT.C2945)
    C46106 = PermissibleValue(text="C46106",
                                   description="Intrathyroid Thymic Carcinoma",
                                   meaning=NCIT.C46106)
    C6042 = PermissibleValue(text="C6042",
                                 description="Thyroid Gland Hurthle Cell Adenoma",
                                 meaning=NCIT.C6042)
    C3783 = PermissibleValue(text="C3783",
                                 description="Serous Cystadenoma",
                                 meaning=NCIT.C3783)
    C7569 = PermissibleValue(text="C7569",
                                 description="Thymic Carcinoma",
                                 meaning=NCIT.C7569)
    C126998 = PermissibleValue(text="C126998",
                                     description="Uterine Corpus High Grade Endometrial Stromal Sarcoma",
                                     meaning=NCIT.C126998)
    C4438 = PermissibleValue(text="C4438",
                                 description="Liver Angiosarcoma",
                                 meaning=NCIT.C4438)
    C40310 = PermissibleValue(text="C40310",
                                   description="Sebaceous Carcinoma",
                                   meaning=NCIT.C40310)
    C4030 = PermissibleValue(text="C4030",
                                 description="Urothelial Carcinoma",
                                 meaning=NCIT.C4030)
    C3745 = PermissibleValue(text="C3745",
                                 description="Clear Cell Sarcoma of Soft Tissue",
                                 meaning=NCIT.C3745)
    C7581 = PermissibleValue(text="C7581",
                                 description="Microcystic Adnexal Carcinoma",
                                 meaning=NCIT.C7581)
    C7999 = PermissibleValue(text="C7999",
                                 description="Malignant Type A Thymoma",
                                 meaning=NCIT.C7999)
    C5726 = PermissibleValue(text="C5726",
                                 description="Pancreatic Intraductal Papillary-Mucinous Neoplasm with an Associated Invasive Carcinoma",
                                 meaning=NCIT.C5726)
    C4126 = PermissibleValue(text="C4126",
                                 description="Intestinal-Type Adenocarcinoma",
                                 meaning=NCIT.C4126)
    C4150 = PermissibleValue(text="C4150",
                                 description="Basophilic Adenocarcinoma",
                                 meaning=NCIT.C4150)
    C3788 = PermissibleValue(text="C3788",
                                 description="Ganglioglioma",
                                 meaning=NCIT.C3788)
    C173740 = PermissibleValue(text="C173740",
                                     description="Ameloblastic Fibroodontosarcoma",
                                     meaning=NCIT.C173740)
    C2852 = PermissibleValue(text="C2852",
                                 description="Adenocarcinoma",
                                 meaning=NCIT.C2852)
    C3776 = PermissibleValue(text="C3776",
                                 description="Mucinous Cystadenocarcinoma",
                                 meaning=NCIT.C3776)
    C3747 = PermissibleValue(text="C3747",
                                 description="Angioleiomyoma",
                                 meaning=NCIT.C3747)
    C27261 = PermissibleValue(text="C27261",
                                   description="Pre T-ALL",
                                   meaning=NCIT.C27261)
    C6958 = PermissibleValue(text="C6958",
                                 description="Astrocytic Tumor",
                                 meaning=NCIT.C6958)
    C6432 = PermissibleValue(text="C6432",
                                 description="Multiple Endocrine Neoplasia",
                                 meaning=NCIT.C6432)
    C2942 = PermissibleValue(text="C2942",
                                 description="Bile Duct Adenoma",
                                 meaning=NCIT.C2942)
    C4663 = PermissibleValue(text="C4663",
                                 description="Splenic Marginal Zone Lymphoma",
                                 meaning=NCIT.C4663)
    C3752 = PermissibleValue(text="C3752",
                                 description="Embryonal Carcinoma",
                                 meaning=NCIT.C3752)
    C3403 = PermissibleValue(text="C3403",
                                 description="Teratoma",
                                 meaning=NCIT.C3403)
    C6939 = PermissibleValue(text="C6939",
                                 description="Breast Ductal Carcinoma In Situ and Invasive Lobular Carcinoma",
                                 meaning=NCIT.C6939)
    C4172 = PermissibleValue(text="C4172",
                                 description="Syringocystadenoma Papilliferum",
                                 meaning=NCIT.C4172)
    C96414 = PermissibleValue(text="C96414",
                                   description="Serrated Lesions and Polyps",
                                   meaning=NCIT.C96414)
    C9348 = PermissibleValue(text="C9348",
                                 description="Mast Cell Sarcoma",
                                 meaning=NCIT.C9348)
    C3769 = PermissibleValue(text="C3769",
                                 description="Endometrioid Adenocarcinoma",
                                 meaning=NCIT.C3769)
    C54000 = PermissibleValue(text="C54000",
                                   description="Gastrointestinal Stromal Tumor of Uncertain Malignant Potential",
                                   meaning=NCIT.C54000)
    C66760 = PermissibleValue(text="C66760",
                                   description="Fibromyxoid Tumor",
                                   meaning=NCIT.C66760)
    C4164 = PermissibleValue(text="C4164",
                                 description="Pigmented Adrenal Cortex Adenoma",
                                 meaning=NCIT.C4164)
    C4106 = PermissibleValue(text="C4106",
                                 description="Pseudoglandular Squamous Cell Carcinoma",
                                 meaning=NCIT.C4106)
    C4289 = PermissibleValue(text="C4289",
                                 description="Teratoma with Somatic-Type Malignancy",
                                 meaning=NCIT.C4289)
    C4021 = PermissibleValue(text="C4021",
                                 description="Chondroblastic Osteosarcoma",
                                 meaning=NCIT.C4021)
    C54300 = PermissibleValue(text="C54300",
                                   description="Clear Cell Odontogenic Carcinoma",
                                   meaning=NCIT.C54300)
    C5407 = PermissibleValue(text="C5407",
                                 description="Medulloblastoma with Extensive Nodularity",
                                 meaning=NCIT.C5407)
    C2854 = PermissibleValue(text="C2854",
                                 description="Warthin Tumor",
                                 meaning=NCIT.C2854)
    C9004 = PermissibleValue(text="C9004",
                                 description="Benign Adrenal Cortex Neoplasm",
                                 meaning=NCIT.C9004)
    C3863 = PermissibleValue(text="C3863",
                                 description="Breast Intraductal Papilloma",
                                 meaning=NCIT.C3863)
    C9459 = PermissibleValue(text="C9459",
                                 description="Borderline Ovarian Brenner Tumor/Atypical Proliferative Ovarian Brenner Tumor",
                                 meaning=NCIT.C9459)
    C7162 = PermissibleValue(text="C7162",
                                 description="Primary Cutaneous Lymphoma",
                                 meaning=NCIT.C7162)
    C95406 = PermissibleValue(text="C95406",
                                   description="Digestive System Mixed Adenoneuroendocrine Carcinoma",
                                   meaning=NCIT.C95406)
    C3724 = PermissibleValue(text="C3724",
                                 description="Cystic Hygroma",
                                 meaning=NCIT.C3724)
    C3194 = PermissibleValue(text="C3194",
                                 description="Liposarcoma",
                                 meaning=NCIT.C3194)
    C2928 = PermissibleValue(text="C2928",
                                 description="Scirrhous Adenocarcinoma",
                                 meaning=NCIT.C2928)
    C4862 = PermissibleValue(text="C4862",
                                 description="Ovarian Sex Cord-Stromal Tumor",
                                 meaning=NCIT.C4862)
    C3180 = PermissibleValue(text="C3180",
                                 description="Plasma Cell Leukemia",
                                 meaning=NCIT.C3180)
    C8559 = PermissibleValue(text="C8559",
                                 description="Malignant Paraganglioma",
                                 meaning=NCIT.C8559)
    C9011 = PermissibleValue(text="C9011",
                                 description="Dermoid Cyst",
                                 meaning=NCIT.C9011)
    C8380 = PermissibleValue(text="C8380",
                                 description="Undifferentiated Pleomorphic Sarcoma with Osteoclast-Like Giant Cells",
                                 meaning=NCIT.C8380)
    C4196 = PermissibleValue(text="C4196",
                                 description="Acinar Cell Adenoma",
                                 meaning=NCIT.C4196)
    C4107 = PermissibleValue(text="C4107",
                                 description="Nasopharyngeal-Type Undifferentiated Carcinoma",
                                 meaning=NCIT.C4107)
    C4072 = PermissibleValue(text="C4072",
                                 description="Mesonephric Adenocarcinoma",
                                 meaning=NCIT.C4072)
    C54323 = PermissibleValue(text="C54323",
                                   description="Dentinogenic Ghost Cell Tumor",
                                   meaning=NCIT.C54323)
    C66800 = PermissibleValue(text="C66800",
                                   description="Ameloblastic Fibrodentinoma",
                                   meaning=NCIT.C66800)
    C3309 = PermissibleValue(text="C3309",
                                 description="Extra-Adrenal Paraganglioma",
                                 meaning=NCIT.C3309)
    C27084 = PermissibleValue(text="C27084",
                                   description="Spindle Cell Squamous Cell Carcinoma",
                                   meaning=NCIT.C27084)
    C3342 = PermissibleValue(text="C3342",
                                 description="Lactotroph Adenoma",
                                 meaning=NCIT.C3342)
    C7812 = PermissibleValue(text="C7812",
                                 description="Solitary Plasmacytoma of Bone",
                                 meaning=NCIT.C7812)
    C6489 = PermissibleValue(text="C6489",
                                 description="Extraabdominal Fibromatosis",
                                 meaning=NCIT.C6489)
    C4183 = PermissibleValue(text="C4183",
                                 description="Borderline Papillary Serous Cystadenoma",
                                 meaning=NCIT.C4183)
    C3808 = PermissibleValue(text="C3808",
                                 description="Rhabdoid Tumor",
                                 meaning=NCIT.C3808)
    C4456 = PermissibleValue(text="C4456",
                                 description="Malignant Mesothelioma",
                                 meaning=NCIT.C4456)
    C3050 = PermissibleValue(text="C3050",
                                 description="Gastrin-Producing Neuroendocrine Tumor",
                                 meaning=NCIT.C3050)
    C7677 = PermissibleValue(text="C7677",
                                 description="Adenocarcinoma in Tubular Adenoma",
                                 meaning=NCIT.C7677)
    C7541 = PermissibleValue(text="C7541",
                                 description="Retinoblastoma",
                                 meaning=NCIT.C7541)
    C4264 = PermissibleValue(text="C4264",
                                 description="Clear Cell Sarcoma of the Kidney",
                                 meaning=NCIT.C4264)
    C3249 = PermissibleValue(text="C3249",
                                 description="Acute Myeloid Leukemia without Maturation",
                                 meaning=NCIT.C3249)
    C4218 = PermissibleValue(text="C4218",
                                 description="Aorticopulmonary Paraganglioma",
                                 meaning=NCIT.C4218)
    C4727 = PermissibleValue(text="C4727",
                                 description="Post-Transplant Lymphoproliferative Disorder",
                                 meaning=NCIT.C4727)
    C35725 = PermissibleValue(text="C35725",
                                   description="Grade II Neuroendocrine Carcinoma",
                                   meaning=NCIT.C35725)
    C27182 = PermissibleValue(text="C27182",
                                   description="Skin Sclerosing/Morphoeic Basal Cell Carcinoma",
                                   meaning=NCIT.C27182)
    C3502 = PermissibleValue(text="C3502",
                                 description="Thyroid Gland Follicular Adenoma",
                                 meaning=NCIT.C3502)
    C3795 = PermissibleValue(text="C3795",
                                 description="Subependymoma",
                                 meaning=NCIT.C3795)
    C3758 = PermissibleValue(text="C3758",
                                 description="Hepatocellular Adenoma",
                                 meaning=NCIT.C3758)
    C27132 = PermissibleValue(text="C27132",
                                   description="Trichoblastoma",
                                   meaning=NCIT.C27132)
    C3402 = PermissibleValue(text="C3402",
                                 description="Tenosynovial Giant Cell Tumor",
                                 meaning=NCIT.C3402)
    C7270 = PermissibleValue(text="C7270",
                                 description="Mixed Mucinous and Non-Mucinous Bronchioloalveolar Carcinoma",
                                 meaning=NCIT.C7270)
    C54345 = PermissibleValue(text="C54345",
                                   description="Sinonasal Oncocytic Papilloma",
                                   meaning=NCIT.C54345)
    C4117 = PermissibleValue(text="C4117",
                                 description="Sinonasal Papilloma",
                                 meaning=NCIT.C4117)
    C6747 = PermissibleValue(text="C6747",
                                 description="Desmoplastic Mesothelioma",
                                 meaning=NCIT.C6747)
    C3250 = PermissibleValue(text="C3250",
                                 description="Acute Myeloid Leukemia with Maturation",
                                 meaning=NCIT.C3250)
    C7368 = PermissibleValue(text="C7368",
                                 description="Pilomatricoma",
                                 meaning=NCIT.C7368)
    C3828 = PermissibleValue(text="C3828",
                                 description="Combined Hepatocellular Carcinoma and Cholangiocarcinoma",
                                 meaning=NCIT.C3828)
    C3702 = PermissibleValue(text="C3702",
                                 description="Hibernoma",
                                 meaning=NCIT.C3702)
    C3205 = PermissibleValue(text="C3205",
                                 description="Lymphangiosarcoma",
                                 meaning=NCIT.C3205)
    C4147 = PermissibleValue(text="C4147",
                                 description="Pituitary Gland Acidophil Carcinoma",
                                 meaning=NCIT.C4147)
    C27253 = PermissibleValue(text="C27253",
                                   description="Metanephric Adenoma",
                                   meaning=NCIT.C27253)
    C4143 = PermissibleValue(text="C4143",
                                 description="Tubulovillous Adenoma",
                                 meaning=NCIT.C4143)
    C4257 = PermissibleValue(text="C4257",
                                 description="Bizarre Leiomyoma",
                                 meaning=NCIT.C4257)
    C3772 = PermissibleValue(text="C3772",
                                 description="Mucoepidermoid Carcinoma",
                                 meaning=NCIT.C3772)
    C4220 = PermissibleValue(text="C4220",
                                 description="Malignant Adrenal Gland Pheochromocytoma",
                                 meaning=NCIT.C4220)
    C7401 = PermissibleValue(text="C7401",
                                 description="Hairy Cell Leukemia Variant",
                                 meaning=NCIT.C7401)
    C4231 = PermissibleValue(text="C4231",
                                 description="Junctional Nevus",
                                 meaning=NCIT.C4231)
    C3996 = PermissibleValue(text="C3996",
                                 description="Monoclonal Gammopathy of Undetermined Significance",
                                 meaning=NCIT.C3996)
    C3712 = PermissibleValue(text="C3712",
                                 description="Squamous Cell Papilloma",
                                 meaning=NCIT.C3712)
    C3766 = PermissibleValue(text="C3766",
                                 description="Clear Cell Adenocarcinoma",
                                 meaning=NCIT.C3766)
    C7645 = PermissibleValue(text="C7645",
                                 description="Breast Intracystic Papillary Carcinoma",
                                 meaning=NCIT.C7645)
    C3295 = PermissibleValue(text="C3295",
                                 description="Osteochondroma",
                                 meaning=NCIT.C3295)
    C3461 = PermissibleValue(text="C3461",
                                 description="Immunoblastic Lymphoma",
                                 meaning=NCIT.C3461)
    C174129 = PermissibleValue(text="C174129",
                                     description="Acute Myeloid Leukemia with MLL Rearrangement",
                                     meaning=NCIT.C174129)
    C6906 = PermissibleValue(text="C6906",
                                 description="Atypical Teratoid/Rhabdoid Tumor",
                                 meaning=NCIT.C6906)
    C27038 = PermissibleValue(text="C27038",
                                   description="Hypereosinophilic Syndrome",
                                   meaning=NCIT.C27038)
    C2946 = PermissibleValue(text="C2946",
                                 description="Chondrosarcoma",
                                 meaning=NCIT.C2946)
    C6967 = PermissibleValue(text="C6967",
                                 description="Pineal Parenchymal Tumor of Intermediate Differentiation",
                                 meaning=NCIT.C6967)
    C9137 = PermissibleValue(text="C9137",
                                 description="Combined Lung Small Cell Carcinoma",
                                 meaning=NCIT.C9137)
    C6887 = PermissibleValue(text="C6887",
                                 description="Thymoma Type B1",
                                 meaning=NCIT.C6887)
    C4335 = PermissibleValue(text="C4335",
                                 description="Malignant Triton Tumor",
                                 meaning=NCIT.C4335)
    C4114 = PermissibleValue(text="C4114",
                                 description="Pilomatrical Carcinoma",
                                 meaning=NCIT.C4114)
    C6474 = PermissibleValue(text="C6474",
                                 description="Low Grade Central Osteosarcoma",
                                 meaning=NCIT.C6474)
    C9496 = PermissibleValue(text="C9496",
                                 description="T-Cell/Histiocyte-Rich Large B-Cell Lymphoma",
                                 meaning=NCIT.C9496)
    C3800 = PermissibleValue(text="C3800",
                                 description="Epithelioid Hemangioendothelioma",
                                 meaning=NCIT.C3800)
    C27799 = PermissibleValue(text="C27799",
                                   description="Pre-Pre-B Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27799)
    C3727 = PermissibleValue(text="C3727",
                                 description="Adenosquamous Carcinoma",
                                 meaning=NCIT.C3727)
    C6907 = PermissibleValue(text="C6907",
                                 description="Metaplastic Meningioma",
                                 meaning=NCIT.C6907)
    C7159 = PermissibleValue(text="C7159",
                                 description="Subepidermal Nodular Fibrosis",
                                 meaning=NCIT.C7159)
    C2970 = PermissibleValue(text="C2970",
                                 description="Adenoid Cystic Carcinoma",
                                 meaning=NCIT.C2970)
    C3717 = PermissibleValue(text="C3717",
                                 description="Melanotic Neuroectodermal Tumor",
                                 meaning=NCIT.C3717)
    C6194 = PermissibleValue(text="C6194",
                                 description="Collecting Duct Carcinoma",
                                 meaning=NCIT.C6194)
    C3400 = PermissibleValue(text="C3400",
                                 description="Synovial Sarcoma",
                                 meaning=NCIT.C3400)
    C7427 = PermissibleValue(text="C7427",
                                 description="Diffuse Sclerosing Variant Thyroid Gland Papillary Carcinoma",
                                 meaning=NCIT.C7427)
    C3739 = PermissibleValue(text="C3739",
                                 description="Fibrous Histiocytoma",
                                 meaning=NCIT.C3739)
    C27125 = PermissibleValue(text="C27125",
                                   description="Proliferating Trichilemmal Tumor",
                                   meaning=NCIT.C27125)
    C2948 = PermissibleValue(text="C2948",
                                 description="Choriocarcinoma",
                                 meaning=NCIT.C2948)
    C4216 = PermissibleValue(text="C4216",
                                 description="Sympathetic Paraganglioma",
                                 meaning=NCIT.C4216)
    C4215 = PermissibleValue(text="C4215",
                                 description="Ovarian Steroid Cell Tumor",
                                 meaning=NCIT.C4215)
    C3005 = PermissibleValue(text="C3005",
                                 description="Tumor Embolism",
                                 meaning=NCIT.C3005)
    C7506 = PermissibleValue(text="C7506",
                                 description="Myelodysplastic Syndrome with Excess Blasts",
                                 meaning=NCIT.C7506)
    C27287 = PermissibleValue(text="C27287",
                                   description="Ovarian Endometrioid Adenofibroma",
                                   meaning=NCIT.C27287)
    C27288 = PermissibleValue(text="C27288",
                                   description="Ovarian Endometrioid Cystadenofibroma",
                                   meaning=NCIT.C27288)
    C9233 = PermissibleValue(text="C9233",
                                 description="Juvenile Myelomonocytic Leukemia",
                                 meaning=NCIT.C9233)
    C4344 = PermissibleValue(text="C4344",
                                 description="Acute Panmyelosis with Myelofibrosis",
                                 meaning=NCIT.C4344)
    C65162 = PermissibleValue(text="C65162",
                                   description="Tumorlet",
                                   meaning=NCIT.C65162)
    C6867 = PermissibleValue(text="C6867",
                                 description="Myelodysplastic Syndrome with Isolated del(5q)",
                                 meaning=NCIT.C6867)
    C3741 = PermissibleValue(text="C3741",
                                 description="Abdominal (Mesenteric) Fibromatosis",
                                 meaning=NCIT.C3741)
    C7996 = PermissibleValue(text="C7996",
                                 description="Malignant Type B1 Thymoma",
                                 meaning=NCIT.C7996)
    C7269 = PermissibleValue(text="C7269",
                                 description="Minimally Invasive Lung Non-Mucinous Adenocarcinoma",
                                 meaning=NCIT.C7269)
    C4193 = PermissibleValue(text="C4193",
                                 description="Thyroid Gland Medullary Carcinoma with Amyloid Stroma",
                                 meaning=NCIT.C4193)
    C7463 = PermissibleValue(text="C7463",
                                 description="Acute Myelomonocytic Leukemia",
                                 meaning=NCIT.C7463)
    C3336 = PermissibleValue(text="C3336",
                                 description="Polycythemia Vera",
                                 meaning=NCIT.C3336)
    C3366 = PermissibleValue(text="C3366",
                                 description="Sezary Syndrome",
                                 meaning=NCIT.C3366)
    C3184 = PermissibleValue(text="C3184",
                                 description="Adult T-Cell Leukemia/Lymphoma",
                                 meaning=NCIT.C3184)
    C7690 = PermissibleValue(text="C7690",
                                 description="Breast Ductal Carcinoma In Situ and Lobular Carcinoma",
                                 meaning=NCIT.C7690)
    C7688 = PermissibleValue(text="C7688",
                                 description="Invasive Breast Ductal Carcinoma and Lobular Carcinoma",
                                 meaning=NCIT.C7688)
    C46104 = PermissibleValue(text="C46104",
                                   description="Thyroid Gland Mixed Medullary and Follicular Cell Carcinoma",
                                   meaning=NCIT.C46104)
    C9327 = PermissibleValue(text="C9327",
                                 description="Malignant Adrenal Cortex Neoplasm",
                                 meaning=NCIT.C9327)
    C4018 = PermissibleValue(text="C4018",
                                 description="Breast Lobular Carcinoma In Situ",
                                 meaning=NCIT.C4018)
    C67006 = PermissibleValue(text="C67006",
                                   description="Malignant Sertoli Cell Tumor",
                                   meaning=NCIT.C67006)
    C4109 = PermissibleValue(text="C4109",
                                 description="Skin Fibroepithelial Basal Cell Carcinoma",
                                 meaning=NCIT.C4109)
    C8965 = PermissibleValue(text="C8965",
                                 description="Lymphangioma",
                                 meaning=NCIT.C8965)
    C3203 = PermissibleValue(text="C3203",
                                 description="Acquired Progressive Lymphangioma",
                                 meaning=NCIT.C3203)
    C96807 = PermissibleValue(text="C96807",
                                   description="Bile Duct Intraductal Papillary Neoplasm, Low Grade",
                                   meaning=NCIT.C96807)
    C40407 = PermissibleValue(text="C40407",
                                   description="Kidney Wilms Tumor",
                                   meaning=NCIT.C40407)
    C4713 = PermissibleValue(text="C4713",
                                 description="Cellular Ependymoma",
                                 meaning=NCIT.C4713)
    C4342 = PermissibleValue(text="C4342",
                                 description="Intravascular Large B-Cell Lymphoma",
                                 meaning=NCIT.C4342)
    C4287 = PermissibleValue(text="C4287",
                                 description="Malignant Teratoma",
                                 meaning=NCIT.C4287)
    C4715 = PermissibleValue(text="C4715",
                                 description="Choroid Plexus Carcinoma",
                                 meaning=NCIT.C4715)
    C8644 = PermissibleValue(text="C8644",
                                 description="B Acute Lymphoblastic Leukemia",
                                 meaning=NCIT.C8644)
    C6969 = PermissibleValue(text="C6969",
                                 description="Plexiform Schwannoma",
                                 meaning=NCIT.C6969)
    C4247 = PermissibleValue(text="C4247",
                                 description="Undifferentiated Pleomorphic Sarcoma",
                                 meaning=NCIT.C4247)
    C2964 = PermissibleValue(text="C2964",
                                 description="Craniopharyngioma",
                                 meaning=NCIT.C2964)
    C4197 = PermissibleValue(text="C4197",
                                 description="Acinar Cell Neoplasm",
                                 meaning=NCIT.C4197)
    C3730 = PermissibleValue(text="C3730",
                                 description="Mixed Mesodermal (Mullerian) Tumor",
                                 meaning=NCIT.C3730)
    C9280 = PermissibleValue(text="C9280",
                                 description="Primary Mediastinal (Thymic) Large B-Cell Lymphoma",
                                 meaning=NCIT.C9280)
    C3085 = PermissibleValue(text="C3085",
                                 description="Hemangioma",
                                 meaning=NCIT.C3085)
    C3781 = PermissibleValue(text="C3781",
                                 description="Verrucous Carcinoma",
                                 meaning=NCIT.C3781)
    C9231 = PermissibleValue(text="C9231",
                                 description="Merkel Cell Carcinoma",
                                 meaning=NCIT.C9231)
    C5264 = PermissibleValue(text="C5264",
                                 description="Bronchial Mucosa-Associated Lymphoid Tissue Lymphoma",
                                 meaning=NCIT.C5264)
    C3212 = PermissibleValue(text="C3212",
                                 description="Lymphoplasmacytic Lymphoma",
                                 meaning=NCIT.C3212)
    C3692 = PermissibleValue(text="C3692",
                                 description="Undifferentiated Carcinoma",
                                 meaning=NCIT.C3692)
    C3224 = PermissibleValue(text="C3224",
                                 description="Melanoma",
                                 meaning=NCIT.C3224)
    C3157 = PermissibleValue(text="C3157",
                                 description="Leiomyoma",
                                 meaning=NCIT.C3157)
    C6507 = PermissibleValue(text="C6507",
                                 description="Sclerosing Atypical Lipomatous Tumor/Well Differentiated Liposarcoma",
                                 meaning=NCIT.C6507)
    C4221 = PermissibleValue(text="C4221",
                                 description="Malignant Glomus Tumor",
                                 meaning=NCIT.C4221)
    C27252 = PermissibleValue(text="C27252",
                                   description="Enterochromaffin-Like Cell Neuroendocrine Tumor G1",
                                   meaning=NCIT.C27252)
    C7097 = PermissibleValue(text="C7097",
                                 description="Mixed Epithelial and Mesenchymal Hepatoblastoma",
                                 meaning=NCIT.C7097)
    C3770 = PermissibleValue(text="C3770",
                                 description="Pancreatic Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3770)
    C6920 = PermissibleValue(text="C6920",
                                 description="Hand-Schuller-Christian Disease",
                                 meaning=NCIT.C6920)
    C3107 = PermissibleValue(text="C3107",
                                 description="Langerhans Cell Histiocytosis",
                                 meaning=NCIT.C3107)
    C6985 = PermissibleValue(text="C6985",
                                 description="Invasive Hydatidiform Mole",
                                 meaning=NCIT.C6985)
    C9288 = PermissibleValue(text="C9288",
                                 description="Acute Myeloid Leukemia with t(8;21); (q22; q22.1); RUNX1-RUNX1T1",
                                 meaning=NCIT.C9288)
    C9300 = PermissibleValue(text="C9300",
                                 description="Acute Leukemia",
                                 meaning=NCIT.C9300)
    C4092 = PermissibleValue(text="C4092",
                                 description="Benign Epithelial Neoplasm",
                                 meaning=NCIT.C4092)
    C4189 = PermissibleValue(text="C4189",
                                 description="Breast Secretory Carcinoma",
                                 meaning=NCIT.C4189)
    C68692 = PermissibleValue(text="C68692",
                                   description="Childhood Nasal Type Extranodal NK/T-Cell Lymphoma",
                                   meaning=NCIT.C68692)
    C6897 = PermissibleValue(text="C6897",
                                 description="Cystic Partially Differentiated Kidney Nephroblastoma",
                                 meaning=NCIT.C6897)
    C4817 = PermissibleValue(text="C4817",
                                 description="Ewing Sarcoma",
                                 meaning=NCIT.C4817)
    C3465 = PermissibleValue(text="C3465",
                                 description="Grade 1 Follicular Lymphoma",
                                 meaning=NCIT.C3465)
    C3359 = PermissibleValue(text="C3359",
                                 description="Rhabdomyosarcoma",
                                 meaning=NCIT.C3359)
    C3339 = PermissibleValue(text="C3339",
                                 description="Familial Adenomatous Polyposis",
                                 meaning=NCIT.C3339)
    C6883 = PermissibleValue(text="C6883",
                                 description="Pancreatic Mucinous-Cystic Neoplasm with Intermediate Grade Dysplasia",
                                 meaning=NCIT.C6883)
    C3773 = PermissibleValue(text="C3773",
                                 description="Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3773)
    C35794 = PermissibleValue(text="C35794",
                                   description="Pagetoid Reticulosis",
                                   meaning=NCIT.C35794)
    C7983 = PermissibleValue(text="C7983",
                                 description="Borderline Ovarian Endometrioid Tumor/Atypical Proliferative Ovarian Endometrioid Tumor",
                                 meaning=NCIT.C7983)
    C53953 = PermissibleValue(text="C53953",
                                   description="Osteoblastic Osteosarcoma",
                                   meaning=NCIT.C53953)
    C4017 = PermissibleValue(text="C4017",
                                 description="Breast Ductal Carcinoma",
                                 meaning=NCIT.C4017)
    C3178 = PermissibleValue(text="C3178",
                                 description="Chronic Myelomonocytic Leukemia",
                                 meaning=NCIT.C3178)
    C27004 = PermissibleValue(text="C27004",
                                   description="Sarcomatoid Carcinoma",
                                   meaning=NCIT.C27004)
    C3270 = PermissibleValue(text="C3270",
                                 description="Neuroblastoma",
                                 meaning=NCIT.C3270)
    C3679 = PermissibleValue(text="C3679",
                                 description="Oncocytic Adenocarcinoma",
                                 meaning=NCIT.C3679)
    C3677 = PermissibleValue(text="C3677",
                                 description="Benign Neoplasm",
                                 meaning=NCIT.C3677)
    C39976 = PermissibleValue(text="C39976",
                                   description="Sertoli Cell Tumor",
                                   meaning=NCIT.C39976)
    C8423 = PermissibleValue(text="C8423",
                                 description="Stage 0 Cutaneous Melanoma AJCC v6 and v7",
                                 meaning=NCIT.C8423)
    C2916 = PermissibleValue(text="C2916",
                                 description="Carcinoma",
                                 meaning=NCIT.C2916)
    C8590 = PermissibleValue(text="C8590",
                                 description="Lymphocyte Predominant Type Hodgkin's Disease",
                                 meaning=NCIT.C8590)
    C4751 = PermissibleValue(text="C4751",
                                 description="Pigmented Spindle Cell Nevus",
                                 meaning=NCIT.C4751)
    C157575 = PermissibleValue(text="C157575",
                                     description="Anal Intraepithelial Neoplasia 3",
                                     meaning=NCIT.C157575)
    C96809 = PermissibleValue(text="C96809",
                                   description="Bile Duct Intraductal Papillary Neoplasm, High Grade",
                                   meaning=NCIT.C96809)
    C2929 = PermissibleValue(text="C2929",
                                 description="Squamous Cell Carcinoma",
                                 meaning=NCIT.C2929)
    C8994 = PermissibleValue(text="C8994",
                                 description="Malignant Lymphoma Centroblastic, Follicular",
                                 meaning=NCIT.C8994)
    C3088 = PermissibleValue(text="C3088",
                                 description="Angiosarcoma",
                                 meaning=NCIT.C3088)
    C27352 = PermissibleValue(text="C27352",
                                   description="Peripheral T-Cell Lymphoma, Large Cell",
                                   meaning=NCIT.C27352)
    C35815 = PermissibleValue(text="C35815",
                                   description="Granulocytic Sarcoma",
                                   meaning=NCIT.C35815)
    C4345 = PermissibleValue(text="C4345",
                                 description="Myeloproliferative Neoplasm",
                                 meaning=NCIT.C4345)
    C3011 = PermissibleValue(text="C3011",
                                 description="Yolk Sac Tumor",
                                 meaning=NCIT.C3011)
    C35870 = PermissibleValue(text="C35870",
                                   description="Conventional Osteosarcoma",
                                   meaning=NCIT.C35870)
    C3789 = PermissibleValue(text="C3789",
                                 description="Olfactory Neuroblastoma",
                                 meaning=NCIT.C3789)
    C3407 = PermissibleValue(text="C3407",
                                 description="Essential Thrombocythemia",
                                 meaning=NCIT.C3407)
    C3170 = PermissibleValue(text="C3170",
                                 description="Acute Megakaryoblastic Leukemia",
                                 meaning=NCIT.C3170)
    C4146 = PermissibleValue(text="C4146",
                                 description="Chromophobe Renal Cell Carcinoma",
                                 meaning=NCIT.C4146)
    C8968 = PermissibleValue(text="C8968",
                                 description="Grade 2 Follicular Lymphoma",
                                 meaning=NCIT.C8968)
    C3132 = PermissibleValue(text="C3132",
                                 description="Alpha Heavy Chain Disease",
                                 meaning=NCIT.C3132)
    C3892 = PermissibleValue(text="C3892",
                                 description="Mu Heavy Chain Disease",
                                 meaning=NCIT.C3892)
    C3182 = PermissibleValue(text="C3182",
                                 description="Acute Promyelocytic Leukemia with PML-RARA",
                                 meaning=NCIT.C3182)
    C9341 = PermissibleValue(text="C9341",
                                 description="Peripheral Primitive Neuroectodermal Tumor",
                                 meaning=NCIT.C9341)
    C3716 = PermissibleValue(text="C3716",
                                 description="Primitive Neuroectodermal Tumor",
                                 meaning=NCIT.C3716)
    C6968 = PermissibleValue(text="C6968",
                                 description="Supratentorial Embryonal Tumor, Not Otherwise Specified",
                                 meaning=NCIT.C6968)
    C35727 = PermissibleValue(text="C35727",
                                   description="Grade I Neuroendocrine Carcinoma",
                                   meaning=NCIT.C35727)
    C2915 = PermissibleValue(text="C2915",
                                 description="Carcinoid Tumor",
                                 meaning=NCIT.C2915)
    C3099 = PermissibleValue(text="C3099",
                                 description="Hepatocellular Carcinoma",
                                 meaning=NCIT.C3099)
    C9087 = PermissibleValue(text="C9087",
                                 description="Kaposi Sarcoma",
                                 meaning=NCIT.C9087)
    C2917 = PermissibleValue(text="C2917",
                                 description="Carcinoma In Situ",
                                 meaning=NCIT.C2917)
    C4664 = PermissibleValue(text="C4664",
                                 description="T-Cell Large Granular Lymphocyte Leukemia",
                                 meaning=NCIT.C4664)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C27258 = PermissibleValue(text="C27258",
                                   description="Malignant Lymphoma, Non-Cleaved Cell Type",
                                   meaning=NCIT.C27258)
    C9306 = PermissibleValue(text="C9306",
                                 description="Soft Tissue Sarcoma",
                                 meaning=NCIT.C9306)
    C8997 = PermissibleValue(text="C8997",
                                 description="Blastoma",
                                 meaning=NCIT.C8997)
    C9357 = PermissibleValue(text="C9357",
                                 description="Hodgkin Lymphoma",
                                 meaning=NCIT.C9357)
    C4982 = PermissibleValue(text="C4982",
                                 description="Aleukemic Leukemia",
                                 meaning=NCIT.C4982)
    C27290 = PermissibleValue(text="C27290",
                                   description="L1 Acute Lymphoblastic Leukemia",
                                   meaning=NCIT.C27290)
    C34774 = PermissibleValue(text="C34774",
                                   description="Chronic Monocytic Leukemia",
                                   meaning=NCIT.C34774)
    C3209 = PermissibleValue(text="C3209",
                                 description="Follicular Lymphoma",
                                 meaning=NCIT.C3209)
    C9283 = PermissibleValue(text="C9283",
                                 description="Lymphocyte-Depleted Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C9283)
    C3518 = PermissibleValue(text="C3518",
                                 description="Nodular Sclerosis Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C3518)
    C7176 = PermissibleValue(text="C7176",
                                 description="Aleukemic Chronic Lymphocytic Leukemia",
                                 meaning=NCIT.C7176)
    C6917 = PermissibleValue(text="C6917",
                                 description="Atypical Burkitt/Burkitt-Like Lymphoma",
                                 meaning=NCIT.C6917)
    C26956 = PermissibleValue(text="C26956",
                                   description="Hodgkin's Paragranuloma",
                                   meaning=NCIT.C26956)
    C9301 = PermissibleValue(text="C9301",
                                 description="Central Nervous System Lymphoma",
                                 meaning=NCIT.C9301)
    C3058 = PermissibleValue(text="C3058",
                                 description="Glioblastoma",
                                 meaning=NCIT.C3058)
    C4748 = PermissibleValue(text="C4748",
                                 description="Malignant Melanotic Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C4748)
    C3798 = PermissibleValue(text="C3798",
                                 description="Malignant Peripheral Nerve Sheath Tumor",
                                 meaning=NCIT.C3798)
    C8648 = PermissibleValue(text="C8648",
                                 description="Myelodysplastic Syndrome, Unclassifiable",
                                 meaning=NCIT.C8648)
    C7171 = PermissibleValue(text="C7171",
                                 description="Acute Monoblastic Leukemia",
                                 meaning=NCIT.C7171)
    C9359 = PermissibleValue(text="C9359",
                                 description="Skin Pigmented Basal Cell Carcinoma",
                                 meaning=NCIT.C9359)
    C82433 = PermissibleValue(text="C82433",
                                   description="Acute Myeloid Leukemia with Mutated CEBPA",
                                   meaning=NCIT.C82433)
    C8460 = PermissibleValue(text="C8460",
                                 description="Acute Myeloid Leukemia with Minimal Differentiation",
                                 meaning=NCIT.C8460)
    C3174 = PermissibleValue(text="C3174",
                                 description="Chronic Myelogenous Leukemia, BCR-ABL1 Positive",
                                 meaning=NCIT.C3174)
    C9128 = PermissibleValue(text="C9128",
                                 description="Philadelphia Chromosome Positive, BCR-ABL1 Positive Chronic Myelogenous Leukemia",
                                 meaning=NCIT.C9128)
    C26712 = PermissibleValue(text="C26712",
                                   description="Mucinous Adenocarcinoma",
                                   meaning=NCIT.C26712)
    C2923 = PermissibleValue(text="C2923",
                                 description="Minimally Invasive Lung Adenocarcinoma",
                                 meaning=NCIT.C2923)
    C3242 = PermissibleValue(text="C3242",
                                 description="Plasma Cell Myeloma",
                                 meaning=NCIT.C3242)
    C27821 = PermissibleValue(text="C27821",
                                   description="Malignant Lymphoma, Convoluted",
                                   meaning=NCIT.C27821)
    C27823 = PermissibleValue(text="C27823",
                                   description="Malignant Lymphoma, Large Cell Type",
                                   meaning=NCIT.C27823)
    C7949 = PermissibleValue(text="C7949",
                                 description="Breast Ductal Carcinoma In Situ, High Grade",
                                 meaning=NCIT.C7949)
    C8054 = PermissibleValue(text="C8054",
                                 description="Thyroid Gland Follicular Carcinoma",
                                 meaning=NCIT.C8054)
    C9385 = PermissibleValue(text="C9385",
                                 description="Renal Cell Carcinoma",
                                 meaning=NCIT.C9385)
    C4033 = PermissibleValue(text="C4033",
                                 description="Clear Cell Renal Cell Carcinoma",
                                 meaning=NCIT.C4033)
    C7467 = PermissibleValue(text="C7467",
                                 description="Pure Erythroid Leukemia",
                                 meaning=NCIT.C7467)
    C3517 = PermissibleValue(text="C3517",
                                 description="Mixed Cellularity Classic Hodgkin Lymphoma",
                                 meaning=NCIT.C3517)
    C7540 = PermissibleValue(text="C7540",
                                 description="Small Lymphocytic Lymphoma",
                                 meaning=NCIT.C7540)
    C7997 = PermissibleValue(text="C7997",
                                 description="Thymoma Type B3",
                                 meaning=NCIT.C7997)
    C4339 = PermissibleValue(text="C4339",
                                 description="Multifocal Lymphomatous Polyposis",
                                 meaning=NCIT.C4339)
    C2862 = PermissibleValue(text="C2862",
                                 description="Primary Myelofibrosis",
                                 meaning=NCIT.C2862)
    C3262 = PermissibleValue(text="C3262",
                                 description="Neoplasm",
                                 meaning=NCIT.C3262)
    C37193 = PermissibleValue(text="C37193",
                                   description="Anaplastic Large Cell Lymphoma, ALK-Positive",
                                   meaning=NCIT.C37193)
    C3915 = PermissibleValue(text="C3915",
                                 description="Small Cell Neuroendocrine Carcinoma",
                                 meaning=NCIT.C3915)
    C4139 = PermissibleValue(text="C4139",
                                 description="Combined Carcinoid and Adenocarcinoma",
                                 meaning=NCIT.C4139)
    C7528 = PermissibleValue(text="C7528",
                                 description="Angioimmunoblastic T-Cell Lymphoma",
                                 meaning=NCIT.C7528)
    C27911 = PermissibleValue(text="C27911",
                                   description="Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma",
                                   meaning=NCIT.C27911)
    C3762 = PermissibleValue(text="C3762",
                                 description="Adenomatoid Tumor",
                                 meaning=NCIT.C3762)
    C39591 = PermissibleValue(text="C39591",
                                   description="Chronic Lymphoproliferative Disorder of NK-Cells",
                                   meaning=NCIT.C39591)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.morphology",
        description="Autogenerated Enumeration for CRDC-H Diagnosis morphology",
        code_set=None,
        code_set_version="2021-05-27T15:46:46.436149+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "8071/2",
                PermissibleValue(text="8071/2",
                                 description="8071/2") )
        setattr(cls, "8339/3",
                PermissibleValue(text="8339/3",
                                 description="8339/3") )
        setattr(cls, "8502/3",
                PermissibleValue(text="8502/3",
                                 description="8502/3") )
        setattr(cls, "9086/3",
                PermissibleValue(text="9086/3",
                                 description="9086/3") )
        setattr(cls, "8714/3",
                PermissibleValue(text="8714/3",
                                 description="8714/3") )
        setattr(cls, "8041/34",
                PermissibleValue(text="8041/34",
                                 description="8041/34") )
        setattr(cls, "8370/1",
                PermissibleValue(text="8370/1",
                                 description="8370/1") )
        setattr(cls, "8509/2",
                PermissibleValue(text="8509/2",
                                 description="8509/2") )
        setattr(cls, "8460/2",
                PermissibleValue(text="8460/2",
                                 description="8460/2") )
        setattr(cls, "8256/3",
                PermissibleValue(text="8256/3",
                                 description="8256/3") )
        setattr(cls, "8521/3",
                PermissibleValue(text="8521/3",
                                 description="8521/3") )
        setattr(cls, "8140/33",
                PermissibleValue(text="8140/33",
                                 description="8140/33") )
        setattr(cls, "9110/1",
                PermissibleValue(text="9110/1",
                                 description="9110/1") )
        setattr(cls, "8430/3",
                PermissibleValue(text="8430/3",
                                 description="8430/3") )
        setattr(cls, "8811/1",
                PermissibleValue(text="8811/1",
                                 description="8811/1") )
        setattr(cls, "8550/3",
                PermissibleValue(text="8550/3",
                                 description="8550/3") )
        setattr(cls, "8522/1",
                PermissibleValue(text="8522/1",
                                 description="8522/1") )
        setattr(cls, "8630/3",
                PermissibleValue(text="8630/3",
                                 description="8630/3") )
        setattr(cls, "8772/0",
                PermissibleValue(text="8772/0",
                                 description="8772/0") )
        setattr(cls, "8085/3",
                PermissibleValue(text="8085/3",
                                 description="8085/3") )
        setattr(cls, "9120/3",
                PermissibleValue(text="9120/3",
                                 description="9120/3") )
        setattr(cls, "8380/2",
                PermissibleValue(text="8380/2",
                                 description="8380/2") )
        setattr(cls, "8692/1",
                PermissibleValue(text="8692/1",
                                 description="8692/1") )
        setattr(cls, "8850/1",
                PermissibleValue(text="8850/1",
                                 description="8850/1") )
        setattr(cls, "8250/2",
                PermissibleValue(text="8250/2",
                                 description="8250/2") )
        setattr(cls, "8343/2",
                PermissibleValue(text="8343/2",
                                 description="8343/2") )
        setattr(cls, "9752/1",
                PermissibleValue(text="9752/1",
                                 description="9752/1") )
        setattr(cls, "9753/1",
                PermissibleValue(text="9753/1",
                                 description="9753/1") )
        setattr(cls, "8474/3",
                PermissibleValue(text="8474/3",
                                 description="8474/3") )
        setattr(cls, "9754/3",
                PermissibleValue(text="9754/3",
                                 description="9754/3") )
        setattr(cls, "8023/3",
                PermissibleValue(text="8023/3",
                                 description="8023/3") )
        setattr(cls, "8630/1",
                PermissibleValue(text="8630/1",
                                 description="8630/1") )
        setattr(cls, "8474/1",
                PermissibleValue(text="8474/1",
                                 description="8474/1") )
        setattr(cls, "8070/2",
                PermissibleValue(text="8070/2",
                                 description="8070/2") )
        setattr(cls, "9052/0",
                PermissibleValue(text="9052/0",
                                 description="9052/0") )
        setattr(cls, "8815/1",
                PermissibleValue(text="8815/1",
                                 description="8815/1") )
        setattr(cls, "8257/3",
                PermissibleValue(text="8257/3",
                                 description="8257/3") )
        setattr(cls, "8825/1",
                PermissibleValue(text="8825/1",
                                 description="8825/1") )
        setattr(cls, "8311/3",
                PermissibleValue(text="8311/3",
                                 description="8311/3") )
        setattr(cls, "8480/0",
                PermissibleValue(text="8480/0",
                                 description="8480/0") )
        setattr(cls, "8120/0",
                PermissibleValue(text="8120/0",
                                 description="8120/0") )
        setattr(cls, "8325/0",
                PermissibleValue(text="8325/0",
                                 description="8325/0") )
        setattr(cls, "8070/33",
                PermissibleValue(text="8070/33",
                                 description="8070/33") )
        setattr(cls, "8145/3",
                PermissibleValue(text="8145/3",
                                 description="8145/3") )
        setattr(cls, "8681/1",
                PermissibleValue(text="8681/1",
                                 description="8681/1") )
        setattr(cls, "9055/1",
                PermissibleValue(text="9055/1",
                                 description="9055/1") )
        setattr(cls, "8519/2",
                PermissibleValue(text="8519/2",
                                 description="8519/2") )
        setattr(cls, "8521/1",
                PermissibleValue(text="8521/1",
                                 description="8521/1") )
        setattr(cls, "8842/3",
                PermissibleValue(text="8842/3",
                                 description="8842/3") )
        setattr(cls, "8441/2",
                PermissibleValue(text="8441/2",
                                 description="8441/2") )
        setattr(cls, "9050/0",
                PermissibleValue(text="9050/0",
                                 description="9050/0") )
        setattr(cls, "8482/6",
                PermissibleValue(text="8482/6",
                                 description="8482/6") )
        setattr(cls, "8720/6",
                PermissibleValue(text="8720/6",
                                 description="8720/6") )
        setattr(cls, "9180/6",
                PermissibleValue(text="9180/6",
                                 description="9180/6") )
        setattr(cls, "8310/6",
                PermissibleValue(text="8310/6",
                                 description="8310/6") )
        setattr(cls, "8249/6",
                PermissibleValue(text="8249/6",
                                 description="8249/6") )
        setattr(cls, "8804/6",
                PermissibleValue(text="8804/6",
                                 description="8804/6") )
        setattr(cls, "8800/6",
                PermissibleValue(text="8800/6",
                                 description="8800/6") )
        setattr(cls, "8500/6",
                PermissibleValue(text="8500/6",
                                 description="8500/6") )
        setattr(cls, "8041/6",
                PermissibleValue(text="8041/6",
                                 description="8041/6") )
        setattr(cls, "8471/1",
                PermissibleValue(text="8471/1",
                                 description="8471/1") )
        setattr(cls, "8311/6",
                PermissibleValue(text="8311/6",
                                 description="8311/6") )
        setattr(cls, "8240/6",
                PermissibleValue(text="8240/6",
                                 description="8240/6") )
        setattr(cls, "8046/6",
                PermissibleValue(text="8046/6",
                                 description="8046/6") )
        setattr(cls, "8806/6",
                PermissibleValue(text="8806/6",
                                 description="8806/6") )
        setattr(cls, "8040/3",
                PermissibleValue(text="8040/3",
                                 description="8040/3") )
        setattr(cls, "8441/6",
                PermissibleValue(text="8441/6",
                                 description="8441/6") )
        setattr(cls, "8020/6",
                PermissibleValue(text="8020/6",
                                 description="8020/6") )
        setattr(cls, "9440/6",
                PermissibleValue(text="9440/6",
                                 description="9440/6") )
        setattr(cls, "8950/6",
                PermissibleValue(text="8950/6",
                                 description="8950/6") )
        setattr(cls, "8801/6",
                PermissibleValue(text="8801/6",
                                 description="8801/6") )
        setattr(cls, "8920/6",
                PermissibleValue(text="8920/6",
                                 description="8920/6") )

class EnumCRDC-H.Diagnosis.diseaseStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis disease_status
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.diseaseStatus",
        description="Autogenerated Enumeration for CRDC-H Diagnosis disease_status",
        code_set=None,
        code_set_version="2021-05-27T15:46:48.379862+00:00",
    )

class EnumCRDC-H.Diagnosis.methodOfDiagnosis(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis
    """
    C93022 = PermissibleValue(text="C93022",
                                   description="Ultrasound-Guided Biopsy",
                                   meaning=NCIT.C93022)
    C15266 = PermissibleValue(text="C15266",
                                   description="Laparotomy",
                                   meaning=NCIT.C15266)
    C16502 = PermissibleValue(text="C16502",
                                   description="Diagnostic Imaging",
                                   meaning=NCIT.C16502)
    C125006 = PermissibleValue(text="C125006",
                                     description="Pathologic Examination",
                                     meaning=NCIT.C125006)
    C16482 = PermissibleValue(text="C16482",
                                   description="Cystoscopy",
                                   meaning=NCIT.C16482)
    C16491 = PermissibleValue(text="C16491",
                                   description="Cytology",
                                   meaning=NCIT.C16491)
    C15226 = PermissibleValue(text="C15226",
                                   description="Dilation and Curettage",
                                   meaning=NCIT.C15226)
    C16969 = PermissibleValue(text="C16969",
                                   description="Laparoscopy",
                                   meaning=NCIT.C16969)
    C48601 = PermissibleValue(text="C48601",
                                   description="Enucleation",
                                   meaning=NCIT.C48601)
    C133261 = PermissibleValue(text="C133261",
                                     description="Bone Marrow Aspirate",
                                     meaning=NCIT.C133261)
    C17348 = PermissibleValue(text="C17348",
                                   description="Pap Smear",
                                   meaning=NCIT.C17348)
    C25153 = PermissibleValue(text="C25153",
                                   description="Autopsy",
                                   meaning=NCIT.C25153)
    C17369 = PermissibleValue(text="C17369",
                                   description="Imaging Technique",
                                   meaning=NCIT.C17369)
    C15385 = PermissibleValue(text="C15385",
                                   description="Excisional Biopsy",
                                   meaning=NCIT.C15385)
    C15386 = PermissibleValue(text="C15386",
                                   description="Incisional Biopsy",
                                   meaning=NCIT.C15386)
    C158758 = PermissibleValue(text="C158758",
                                     description="Resection",
                                     meaning=NCIT.C158758)
    C15749 = PermissibleValue(text="C15749",
                                   description="Tumor Debulking",
                                   meaning=NCIT.C15749)
    C15392 = PermissibleValue(text="C15392",
                                   description="Thoracentesis",
                                   meaning=NCIT.C15392)
    C15680 = PermissibleValue(text="C15680",
                                   description="Core Biopsy",
                                   meaning=NCIT.C15680)
    C15361 = PermissibleValue(text="C15361",
                                   description="Fine-Needle Aspiration",
                                   meaning=NCIT.C15361)
    C20989 = PermissibleValue(text="C20989",
                                   description="Physical Examination",
                                   meaning=NCIT.C20989)
    C17610 = PermissibleValue(text="C17610",
                                   description="Blood Sample",
                                   meaning=NCIT.C17610)
    C15189 = PermissibleValue(text="C15189",
                                   description="Biopsy",
                                   meaning=NCIT.C15189)
    C17649 = PermissibleValue(text="C17649",
                                   description="Other",
                                   meaning=NCIT.C17649)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.methodOfDiagnosis",
        description="Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis",
        code_set=None,
        code_set_version="2021-05-27T15:46:48.541019+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect",
                                 description="Not Allowed To Collect") )

class EnumCRDC-H.Document.documentType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Document document_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Document.documentType",
        description="Autogenerated Enumeration for CRDC-H Document document_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:48.746020+00:00",
    )

class EnumCRDC-H.Identifier.type(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Identifier type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Identifier.type",
        description="Autogenerated Enumeration for CRDC-H Identifier type",
        code_set=None,
        code_set_version="2021-05-27T15:46:48.950814+00:00",
    )

class EnumCRDC-H.Observation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.category",
        description="Autogenerated Enumeration for CRDC-H Observation category",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.203313+00:00",
    )

class EnumCRDC-H.Observation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.observationType",
        description="Autogenerated Enumeration for CRDC-H Observation observation_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.354908+00:00",
    )

class EnumCRDC-H.Observation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.methodType",
        description="Autogenerated Enumeration for CRDC-H Observation method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.504337+00:00",
    )

class EnumCRDC-H.Observation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.651199+00:00",
    )

class EnumCRDC-H.Quantity.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Quantity.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.797978+00:00",
    )

class EnumCRDC-H.ResearchProject.primaryAnatomicSite(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchProject primary_anatomic_site
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchProject.primaryAnatomicSite",
        description="Autogenerated Enumeration for CRDC-H ResearchProject primary_anatomic_site",
        code_set=None,
        code_set_version="2021-05-27T15:46:49.942410+00:00",
    )

class EnumCRDC-H.ResearchProject.researchProjectType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchProject research_project_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchProject.researchProjectType",
        description="Autogenerated Enumeration for CRDC-H ResearchProject research_project_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:50.084871+00:00",
    )

class EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition
    """
    Mesothelioma = PermissibleValue(text="Mesothelioma",
                                               description="Mesothelioma")
    Other = PermissibleValue(text="Other",
                                 description="Other")
    Thymoma = PermissibleValue(text="Thymoma",
                                     description="Thymoma")
    Glioblastoma = PermissibleValue(text="Glioblastoma",
                                               description="Glioblastoma")
    Osteosarcoma = PermissibleValue(text="Osteosarcoma",
                                               description="Osteosarcoma")
    Cholangiocarcinoma = PermissibleValue(text="Cholangiocarcinoma",
                                                           description="Cholangiocarcinoma")
    Sarcoma = PermissibleValue(text="Sarcoma",
                                     description="Sarcoma")
    Neuroblastoma = PermissibleValue(text="Neuroblastoma",
                                                 description="Neuroblastoma")
    C3055 = PermissibleValue(text="C3055",
                                 description="Giant Cell Tumor",
                                 meaning=NCIT.C3055)
    C7387 = PermissibleValue(text="C7387",
                                 description="Blood Vessel Neoplasm",
                                 meaning=NCIT.C7387)
    C3786 = PermissibleValue(text="C3786",
                                 description="Mesothelial Neoplasm",
                                 meaning=NCIT.C3786)
    C3743 = PermissibleValue(text="C3743",
                                 description="Fibroepithelial Neoplasm",
                                 meaning=NCIT.C3743)
    C3792 = PermissibleValue(text="C3792",
                                 description="Squamous Cell Neoplasm",
                                 meaning=NCIT.C3792)
    C4198 = PermissibleValue(text="C4198",
                                 description="Complex Epithelial Neoplasm",
                                 meaning=NCIT.C4198)
    C7056 = PermissibleValue(text="C7056",
                                 description="Mature B-Cell Non-Hodgkin Lymphoma",
                                 meaning=NCIT.C7056)
    C4248 = PermissibleValue(text="C4248",
                                 description="Lipomatous Neoplasm",
                                 meaning=NCIT.C4248)
    C4063 = PermissibleValue(text="C4063",
                                 description="Myomatous Neoplasm",
                                 meaning=NCIT.C4063)
    C3422 = PermissibleValue(text="C3422",
                                 description="Trophoblastic Tumor",
                                 meaning=NCIT.C3422)
    C3723 = PermissibleValue(text="C3723",
                                 description="Lymphatic Vessel Neoplasm",
                                 meaning=NCIT.C3723)
    C3787 = PermissibleValue(text="C3787",
                                 description="Neuroepithelial Neoplasm",
                                 meaning=NCIT.C3787)
    C4463 = PermissibleValue(text="C4463",
                                 description="Skin Appendage Neoplasm",
                                 meaning=NCIT.C4463)
    C4972 = PermissibleValue(text="C4972",
                                 description="Nerve Sheath Neoplasm",
                                 meaning=NCIT.C4972)
    C3709 = PermissibleValue(text="C3709",
                                 description="Epithelial Neoplasm",
                                 meaning=NCIT.C3709)
    C9295 = PermissibleValue(text="C9295",
                                 description="Mast Cell Neoplasm",
                                 meaning=NCIT.C9295)
    C9343 = PermissibleValue(text="C9343",
                                 description="Bone Neoplasm",
                                 meaning=NCIT.C9343)
    C3468 = PermissibleValue(text="C3468",
                                 description="Mature T-Cell and NK-Cell Non-Hodgkin Lymphoma",
                                 meaning=NCIT.C3468)
    C3708 = PermissibleValue(text="C3708",
                                 description="Germ Cell Tumor",
                                 meaning=NCIT.C3708)
    C3059 = PermissibleValue(text="C3059",
                                 description="Glioma",
                                 meaning=NCIT.C3059)
    C3784 = PermissibleValue(text="C3784",
                                 description="Basal Cell Neoplasm",
                                 meaning=NCIT.C3784)
    C3286 = PermissibleValue(text="C3286",
                                 description="Odontogenic Neoplasm",
                                 meaning=NCIT.C3286)
    C3411 = PermissibleValue(text="C3411",
                                 description="Thymoma",
                                 meaning=NCIT.C3411)
    C4197 = PermissibleValue(text="C4197",
                                 description="Acinar Cell Neoplasm",
                                 meaning=NCIT.C4197)
    C4295 = PermissibleValue(text="C4295",
                                 description="Mesonephric Neoplasm",
                                 meaning=NCIT.C4295)
    C4665 = PermissibleValue(text="C4665",
                                 description="Plasma Cell Neoplasm",
                                 meaning=NCIT.C4665)
    C3230 = PermissibleValue(text="C3230",
                                 description="Meningioma",
                                 meaning=NCIT.C3230)
    C3262 = PermissibleValue(text="C3262",
                                 description="Neoplasm",
                                 meaning=NCIT.C3262)
    C4345 = PermissibleValue(text="C4345",
                                 description="Myeloproliferative Neoplasm",
                                 meaning=NCIT.C4345)
    C48660 = PermissibleValue(text="C48660",
                                   description="Not Applicable",
                                   meaning=NCIT.C48660)
    C9360 = PermissibleValue(text="C9360",
                                 description="Lymphoblastic Lymphoma",
                                 meaning=NCIT.C9360)
    C3247 = PermissibleValue(text="C3247",
                                 description="Myelodysplastic Syndrome",
                                 meaning=NCIT.C3247)
    C3208 = PermissibleValue(text="C3208",
                                 description="Lymphoma",
                                 meaning=NCIT.C3208)
    C7539 = PermissibleValue(text="C7539",
                                 description="Lymphoid Leukemia",
                                 meaning=NCIT.C7539)
    C3172 = PermissibleValue(text="C3172",
                                 description="Myeloid Leukemia",
                                 meaning=NCIT.C3172)
    C3161 = PermissibleValue(text="C3161",
                                 description="Leukemia",
                                 meaning=NCIT.C3161)
    C9357 = PermissibleValue(text="C9357",
                                 description="Hodgkin Lymphoma",
                                 meaning=NCIT.C9357)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition",
        code_set=None,
        code_set_version="2021-05-27T15:46:50.234412+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Transitional Cell Papillomas and Carcinomas",
                PermissibleValue(text="Transitional Cell Papillomas and Carcinomas",
                                 description="Transitional Cell Papillomas and Carcinomas") )
        setattr(cls, "Prostate Adenocarcinoma",
                PermissibleValue(text="Prostate Adenocarcinoma",
                                 description="Prostate Adenocarcinoma") )
        setattr(cls, "Osseous and Chondromatous Neoplasms",
                PermissibleValue(text="Osseous and Chondromatous Neoplasms",
                                 description="Osseous and Chondromatous Neoplasms") )
        setattr(cls, "Uterine Corpus Endometrial Carcinoma",
                PermissibleValue(text="Uterine Corpus Endometrial Carcinoma",
                                 description="Uterine Corpus Endometrial Carcinoma") )
        setattr(cls, "Testicular Germ Cell Tumors",
                PermissibleValue(text="Testicular Germ Cell Tumors",
                                 description="Testicular Germ Cell Tumors") )
        setattr(cls, "HIV+ Tumor Molecular Characterization Project - Cervical Cancer",
                PermissibleValue(text="HIV+ Tumor Molecular Characterization Project - Cervical Cancer",
                                 description="HIV+ Tumor Molecular Characterization Project - Cervical Cancer") )
        setattr(cls, "Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma",
                PermissibleValue(text="Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma",
                                 description="Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma") )
        setattr(cls, "Kidney Renal Clear Cell Carcinoma",
                PermissibleValue(text="Kidney Renal Clear Cell Carcinoma",
                                 description="Kidney Renal Clear Cell Carcinoma") )
        setattr(cls, "Breast Invasive Carcinoma",
                PermissibleValue(text="Breast Invasive Carcinoma",
                                 description="Breast Invasive Carcinoma") )
        setattr(cls, "Uterine Carcinosarcoma",
                PermissibleValue(text="Uterine Carcinosarcoma",
                                 description="Uterine Carcinosarcoma") )
        setattr(cls, "Clear Cell Renal Cell Carcinoma",
                PermissibleValue(text="Clear Cell Renal Cell Carcinoma",
                                 description="Clear Cell Renal Cell Carcinoma") )
        setattr(cls, "Skin Cutaneous Melanoma",
                PermissibleValue(text="Skin Cutaneous Melanoma",
                                 description="Skin Cutaneous Melanoma") )
        setattr(cls, "Oral Squamous Cell Carcinoma",
                PermissibleValue(text="Oral Squamous Cell Carcinoma",
                                 description="Oral Squamous Cell Carcinoma") )
        setattr(cls, "Adrenocortical Carcinoma",
                PermissibleValue(text="Adrenocortical Carcinoma",
                                 description="Adrenocortical Carcinoma") )
        setattr(cls, "Head and Neck Squamous Cell Carcinoma",
                PermissibleValue(text="Head and Neck Squamous Cell Carcinoma",
                                 description="Head and Neck Squamous Cell Carcinoma") )
        setattr(cls, "Rectum Adenocarcinoma",
                PermissibleValue(text="Rectum Adenocarcinoma",
                                 description="Rectum Adenocarcinoma") )
        setattr(cls, "Chronic Lymphocytic Leukemia",
                PermissibleValue(text="Chronic Lymphocytic Leukemia",
                                 description="Chronic Lymphocytic Leukemia") )
        setattr(cls, "Mucoepidermoid Neoplasms",
                PermissibleValue(text="Mucoepidermoid Neoplasms",
                                 description="Mucoepidermoid Neoplasms") )
        setattr(cls, "Uveal Melanoma",
                PermissibleValue(text="Uveal Melanoma",
                                 description="Uveal Melanoma") )
        setattr(cls, "Clear Cell Sarcoma of the Kidney",
                PermissibleValue(text="Clear Cell Sarcoma of the Kidney",
                                 description="Clear Cell Sarcoma of the Kidney") )
        setattr(cls, "Stomach Adenocarcinoma",
                PermissibleValue(text="Stomach Adenocarcinoma",
                                 description="Stomach Adenocarcinoma") )
        setattr(cls, "Other Leukemias",
                PermissibleValue(text="Other Leukemias",
                                 description="Other Leukemias") )
        setattr(cls, "Synovial-like Neoplasms",
                PermissibleValue(text="Synovial-like Neoplasms",
                                 description="Synovial-like Neoplasms") )
        setattr(cls, "Pediatric/AYA Brain Tumors",
                PermissibleValue(text="Pediatric/AYA Brain Tumors",
                                 description="Pediatric/AYA Brain Tumors") )
        setattr(cls, "Rhabdoid Tumor",
                PermissibleValue(text="Rhabdoid Tumor",
                                 description="Rhabdoid Tumor") )
        setattr(cls, "Early Onset Gastric Cancer",
                PermissibleValue(text="Early Onset Gastric Cancer",
                                 description="Early Onset Gastric Cancer") )
        setattr(cls, "Neoplasms of Histiocytes and Accessory Lymphoid Cells",
                PermissibleValue(text="Neoplasms of Histiocytes and Accessory Lymphoid Cells",
                                 description="Neoplasms of Histiocytes and Accessory Lymphoid Cells") )
        setattr(cls, "Acute Lymphoblastic Leukemia",
                PermissibleValue(text="Acute Lymphoblastic Leukemia",
                                 description="Acute Lymphoblastic Leukemia") )
        setattr(cls, "Acute Myeloid Leukemia",
                PermissibleValue(text="Acute Myeloid Leukemia",
                                 description="Acute Myeloid Leukemia") )
        setattr(cls, "Bladder Urothelial Carcinoma",
                PermissibleValue(text="Bladder Urothelial Carcinoma",
                                 description="Bladder Urothelial Carcinoma") )
        setattr(cls, "Papillary Renal Cell Carcinoma",
                PermissibleValue(text="Papillary Renal Cell Carcinoma",
                                 description="Papillary Renal Cell Carcinoma") )
        setattr(cls, "Pheochromocytoma and Paraganglioma",
                PermissibleValue(text="Pheochromocytoma and Paraganglioma",
                                 description="Pheochromocytoma and Paraganglioma") )
        setattr(cls, "Nevi and Melanomas",
                PermissibleValue(text="Nevi and Melanomas",
                                 description="Nevi and Melanomas") )
        setattr(cls, "Lung Squamous Cell Carcinoma",
                PermissibleValue(text="Lung Squamous Cell Carcinoma",
                                 description="Lung Squamous Cell Carcinoma") )
        setattr(cls, "Ductal and Lobular Neoplasms",
                PermissibleValue(text="Ductal and Lobular Neoplasms",
                                 description="Ductal and Lobular Neoplasms") )
        setattr(cls, "Esophageal Carcinoma",
                PermissibleValue(text="Esophageal Carcinoma",
                                 description="Esophageal Carcinoma") )
        setattr(cls, "Lung Adenocarcinoma",
                PermissibleValue(text="Lung Adenocarcinoma",
                                 description="Lung Adenocarcinoma") )
        setattr(cls, "Myxomatous Neoplasms",
                PermissibleValue(text="Myxomatous Neoplasms",
                                 description="Myxomatous Neoplasms") )
        setattr(cls, "Fibromatous Neoplasms",
                PermissibleValue(text="Fibromatous Neoplasms",
                                 description="Fibromatous Neoplasms") )
        setattr(cls, "Soft Tissue Tumors and Sarcomas, NOS",
                PermissibleValue(text="Soft Tissue Tumors and Sarcomas, NOS",
                                 description="Soft Tissue Tumors and Sarcomas, NOS") )
        setattr(cls, "Kidney Chromophobe",
                PermissibleValue(text="Kidney Chromophobe",
                                 description="Kidney Chromophobe") )
        setattr(cls, "Thyroid Carcinoma",
                PermissibleValue(text="Thyroid Carcinoma",
                                 description="Thyroid Carcinoma") )
        setattr(cls, "Granular Cell Tumors and Alveolar Soft Part Sarcomas",
                PermissibleValue(text="Granular Cell Tumors and Alveolar Soft Part Sarcomas",
                                 description="Granular Cell Tumors and Alveolar Soft Part Sarcomas") )
        setattr(cls, "Brain Lower Grade Glioma",
                PermissibleValue(text="Brain Lower Grade Glioma",
                                 description="Brain Lower Grade Glioma") )
        setattr(cls, "Lymphoid Neoplasm Diffuse Large B-cell Lymphoma",
                PermissibleValue(text="Lymphoid Neoplasm Diffuse Large B-cell Lymphoma",
                                 description="Lymphoid Neoplasm Diffuse Large B-cell Lymphoma") )
        setattr(cls, "Immunoproliferative Diseases",
                PermissibleValue(text="Immunoproliferative Diseases",
                                 description="Immunoproliferative Diseases") )
        setattr(cls, "Ovarian Serous Cystadenocarcinoma",
                PermissibleValue(text="Ovarian Serous Cystadenocarcinoma",
                                 description="Ovarian Serous Cystadenocarcinoma") )
        setattr(cls, "Burkitt Lymphoma",
                PermissibleValue(text="Burkitt Lymphoma",
                                 description="Burkitt Lymphoma") )
        setattr(cls, "Other Hematologic Disorders",
                PermissibleValue(text="Other Hematologic Disorders",
                                 description="Other Hematologic Disorders") )
        setattr(cls, "Cystic, Mucinous and Serous Neoplasms",
                PermissibleValue(text="Cystic, Mucinous and Serous Neoplasms",
                                 description="Cystic, Mucinous and Serous Neoplasms") )
        setattr(cls, "Paragangliomas and Glomus Tumors",
                PermissibleValue(text="Paragangliomas and Glomus Tumors",
                                 description="Paragangliomas and Glomus Tumors") )
        setattr(cls, "Hepatocellular Carcinoma",
                PermissibleValue(text="Hepatocellular Carcinoma",
                                 description="Hepatocellular Carcinoma") )
        setattr(cls, "Colon Adenocarcinoma",
                PermissibleValue(text="Colon Adenocarcinoma",
                                 description="Colon Adenocarcinoma") )
        setattr(cls, "High-Risk Wilms Tumor",
                PermissibleValue(text="High-Risk Wilms Tumor",
                                 description="High-Risk Wilms Tumor") )
        setattr(cls, "Liver Hepatocellular Carcinoma",
                PermissibleValue(text="Liver Hepatocellular Carcinoma",
                                 description="Liver Hepatocellular Carcinoma") )
        setattr(cls, "Kidney Renal Papillary Cell Carcinoma",
                PermissibleValue(text="Kidney Renal Papillary Cell Carcinoma",
                                 description="Kidney Renal Papillary Cell Carcinoma") )
        setattr(cls, "Specialized Gonadal Neoplasms",
                PermissibleValue(text="Specialized Gonadal Neoplasms",
                                 description="Specialized Gonadal Neoplasms") )
        setattr(cls, "Chromophobe Renal Cell Carcinoma",
                PermissibleValue(text="Chromophobe Renal Cell Carcinoma",
                                 description="Chromophobe Renal Cell Carcinoma") )
        setattr(cls, "Complex Mixed and Stromal Neoplasms",
                PermissibleValue(text="Complex Mixed and Stromal Neoplasms",
                                 description="Complex Mixed and Stromal Neoplasms") )
        setattr(cls, "Glioblastoma Multiforme",
                PermissibleValue(text="Glioblastoma Multiforme",
                                 description="Glioblastoma Multiforme") )
        setattr(cls, "Pancreatic Adenocarcinoma",
                PermissibleValue(text="Pancreatic Adenocarcinoma",
                                 description="Pancreatic Adenocarcinoma") )
        setattr(cls, "Miscellaneous Tumors",
                PermissibleValue(text="Miscellaneous Tumors",
                                 description="Miscellaneous Tumors") )
        setattr(cls, "Multiple Myeloma",
                PermissibleValue(text="Multiple Myeloma",
                                 description="Multiple Myeloma") )
        setattr(cls, "HIV+ Tumor Molecular Characterization Project - Lung Cancer",
                PermissibleValue(text="HIV+ Tumor Molecular Characterization Project - Lung Cancer",
                                 description="HIV+ Tumor Molecular Characterization Project - Lung Cancer") )
        setattr(cls, "Adenomas and Adenocarcinomas",
                PermissibleValue(text="Adenomas and Adenocarcinomas",
                                 description="Adenomas and Adenocarcinomas") )
        setattr(cls, "Pancreatic Ductal Adenocarcinoma",
                PermissibleValue(text="Pancreatic Ductal Adenocarcinoma",
                                 description="Pancreatic Ductal Adenocarcinoma") )

class EnumCRDC-H.ResearchSubject.primaryDiagnosisSite(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_site
    """
    Thyroid = PermissibleValue(text="Thyroid",
                                     description="Thyroid")
    Colorectal = PermissibleValue(text="Colorectal",
                                           description="Colorectal")
    Lung = PermissibleValue(text="Lung",
                               description="Lung")
    Cervix = PermissibleValue(text="Cervix",
                                   description="Cervix")
    Uterus = PermissibleValue(text="Uterus",
                                   description="Uterus")
    Pleura = PermissibleValue(text="Pleura",
                                   description="Pleura")
    Blood = PermissibleValue(text="Blood",
                                 description="Blood")
    Liver = PermissibleValue(text="Liver",
                                 description="Liver")
    Eye = PermissibleValue(text="Eye",
                             description="Eye")
    Bone = PermissibleValue(text="Bone",
                               description="Bone")
    Prostate = PermissibleValue(text="Prostate",
                                       description="Prostate")
    C156712 = PermissibleValue(text="C156712",
                                     description="Peritoneum and Retroperitoneum",
                                     meaning=NCIT.C156712)
    C164038 = PermissibleValue(text="C164038",
                                     description="Limb Skeletal System",
                                     meaning=NCIT.C164038)
    C148335 = PermissibleValue(text="C148335",
                                     description="Other and Ill Defined Digestive Organs ICD-O-3",
                                     meaning=NCIT.C148335)
    C148345 = PermissibleValue(text="C148345",
                                     description="Other and Unspecified Urinary Organs ICD-O-3",
                                     meaning=NCIT.C148345)
    C148340 = PermissibleValue(text="C148340",
                                     description="Other and Unspecified Major Salivary Glands ICD-O-3",
                                     meaning=NCIT.C148340)
    C148346 = PermissibleValue(text="C148346",
                                     description="Other Endocrine Glands and Related Structures ICD-O-3",
                                     meaning=NCIT.C148346)
    C148337 = PermissibleValue(text="C148337",
                                     description="Other and Ill-Defined Sites in Lip, Oral Cavity and Pharynx ICD-O-3",
                                     meaning=NCIT.C148337)
    C148336 = PermissibleValue(text="C148336",
                                     description="Other and Ill-Defined Sites ICD-O-3",
                                     meaning=NCIT.C148336)
    C148342 = PermissibleValue(text="C148342",
                                     description="Other and Unspecified Parts of Biliary Tract ICD-O-3",
                                     meaning=NCIT.C148342)
    C148343 = PermissibleValue(text="C148343",
                                     description="Other and Unspecified Parts of Mouth ICD-O-3",
                                     meaning=NCIT.C148343)
    C148344 = PermissibleValue(text="C148344",
                                     description="Other and Unspecified Parts of Tongue ICD-O-3",
                                     meaning=NCIT.C148344)
    C92218 = PermissibleValue(text="C92218",
                                   description="Lung/Bronchus",
                                   meaning=NCIT.C92218)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C12470 = PermissibleValue(text="C12470",
                                   description="Skin",
                                   meaning=NCIT.C12470)
    C12415 = PermissibleValue(text="C12415",
                                   description="Kidney",
                                   meaning=NCIT.C12415)
    C12246 = PermissibleValue(text="C12246",
                                   description="Hypopharynx",
                                   meaning=NCIT.C12246)
    C12745 = PermissibleValue(text="C12745",
                                   description="Lymph Node",
                                   meaning=NCIT.C12745)
    C12666 = PermissibleValue(text="C12666",
                                   description="Adrenal Gland",
                                   meaning=NCIT.C12666)
    C12414 = PermissibleValue(text="C12414",
                                   description="Bladder",
                                   meaning=NCIT.C12414)
    C12439 = PermissibleValue(text="C12439",
                                   description="Brain",
                                   meaning=NCIT.C12439)
    C12386 = PermissibleValue(text="C12386",
                                   description="Small Intestine",
                                   meaning=NCIT.C12386)
    C12407 = PermissibleValue(text="C12407",
                                   description="Vagina",
                                   meaning=NCIT.C12407)
    C12404 = PermissibleValue(text="C12404",
                                   description="Ovary",
                                   meaning=NCIT.C12404)
    C12382 = PermissibleValue(text="C12382",
                                   description="Colon",
                                   meaning=NCIT.C12382)
    C12412 = PermissibleValue(text="C12412",
                                   description="Testis",
                                   meaning=NCIT.C12412)
    C12311 = PermissibleValue(text="C12311",
                                   description="Cervix Uteri",
                                   meaning=NCIT.C12311)
    C12393 = PermissibleValue(text="C12393",
                                   description="Pancreas",
                                   meaning=NCIT.C12393)
    C12389 = PermissibleValue(text="C12389",
                                   description="Esophagus",
                                   meaning=NCIT.C12389)
    C12408 = PermissibleValue(text="C12408",
                                   description="Vulva",
                                   meaning=NCIT.C12408)
    C12416 = PermissibleValue(text="C12416",
                                   description="Ureter",
                                   meaning=NCIT.C12416)
    C12405 = PermissibleValue(text="C12405",
                                   description="Uterus",
                                   meaning=NCIT.C12405)
    C12400 = PermissibleValue(text="C12400",
                                   description="Thyroid Gland",
                                   meaning=NCIT.C12400)
    C12391 = PermissibleValue(text="C12391",
                                   description="Stomach",
                                   meaning=NCIT.C12391)
    C12410 = PermissibleValue(text="C12410",
                                   description="Prostate Gland",
                                   meaning=NCIT.C12410)
    C12420 = PermissibleValue(text="C12420",
                                   description="Larynx",
                                   meaning=NCIT.C12420)
    C12433 = PermissibleValue(text="C12433",
                                   description="Thymus Gland",
                                   meaning=NCIT.C12433)
    C32677 = PermissibleValue(text="C32677",
                                   description="Gingiva",
                                   meaning=NCIT.C32677)
    C12971 = PermissibleValue(text="C12971",
                                   description="Breast",
                                   meaning=NCIT.C12971)
    C12390 = PermissibleValue(text="C12390",
                                   description="Rectum",
                                   meaning=NCIT.C12390)
    C12423 = PermissibleValue(text="C12423",
                                   description="Nasopharynx",
                                   meaning=NCIT.C12423)
    C12220 = PermissibleValue(text="C12220",
                                   description="Lip",
                                   meaning=NCIT.C12220)
    C12762 = PermissibleValue(text="C12762",
                                   description="Oropharynx",
                                   meaning=NCIT.C12762)
    C12377 = PermissibleValue(text="C12377",
                                   description="Gallbladder",
                                   meaning=NCIT.C12377)
    C12409 = PermissibleValue(text="C12409",
                                   description="Penis",
                                   meaning=NCIT.C12409)
    C12427 = PermissibleValue(text="C12427",
                                   description="Parotid Gland",
                                   meaning=NCIT.C12427)
    C54187 = PermissibleValue(text="C54187",
                                   description="Floor of Mouth",
                                   meaning=NCIT.C54187)
    C12229 = PermissibleValue(text="C12229",
                                   description="Palate",
                                   meaning=NCIT.C12229)
    C12763 = PermissibleValue(text="C12763",
                                   description="Paranasal Sinus",
                                   meaning=NCIT.C12763)
    C13272 = PermissibleValue(text="C13272",
                                   description="Placenta",
                                   meaning=NCIT.C13272)
    C54188 = PermissibleValue(text="C54188",
                                   description="Rectosigmoid Region",
                                   meaning=NCIT.C54188)
    C12316 = PermissibleValue(text="C12316",
                                   description="Corpus Uteri",
                                   meaning=NCIT.C12316)
    C12428 = PermissibleValue(text="C12428",
                                   description="Trachea",
                                   meaning=NCIT.C12428)
    C12887 = PermissibleValue(text="C12887",
                                   description="Renal Pelvis",
                                   meaning=NCIT.C12887)
    C12348 = PermissibleValue(text="C12348",
                                   description="Meninges",
                                   meaning=NCIT.C12348)
    C12228 = PermissibleValue(text="C12228",
                                   description="Base of the Tongue",
                                   meaning=NCIT.C12228)
    C148339 = PermissibleValue(text="C148339",
                                     description="Other and Unspecified Female Genital Organs ICD-O-3",
                                     meaning=NCIT.C148339)
    C148338 = PermissibleValue(text="C148338",
                                     description="Other and Ill-Defined Sites within Respiratory System and Intrathoracic Organs ICD-O-3",
                                     meaning=NCIT.C148338)
    C148341 = PermissibleValue(text="C148341",
                                     description="Other and Unspecified Male Genital Organs ICD-O-3",
                                     meaning=NCIT.C148341)
    C33439 = PermissibleValue(text="C33439",
                                   description="Pyriform Sinus",
                                   meaning=NCIT.C33439)
    C12802 = PermissibleValue(text="C12802",
                                   description="Tonsil",
                                   meaning=NCIT.C12802)

    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchSubject.primaryDiagnosisSite",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_site",
        code_set=None,
        code_set_version="2021-05-27T15:46:50.517775+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Soft Tissue",
                PermissibleValue(text="Soft Tissue",
                                 description="Soft Tissue") )
        setattr(cls, "Lymph Nodes",
                PermissibleValue(text="Lymph Nodes",
                                 description="Lymph Nodes") )
        setattr(cls, "Connective, subcutaneous and other soft tissues",
                PermissibleValue(text="Connective, subcutaneous and other soft tissues",
                                 description="Connective, subcutaneous and other soft tissues") )
        setattr(cls, "Adrenal Gland",
                PermissibleValue(text="Adrenal Gland",
                                 description="Adrenal Gland") )
        setattr(cls, "Heart, mediastinum, and pleura",
                PermissibleValue(text="Heart, mediastinum, and pleura",
                                 description="Heart, mediastinum, and pleura") )
        setattr(cls, "Spinal cord, cranial nerves, and other parts of central nervous system",
                PermissibleValue(text="Spinal cord, cranial nerves, and other parts of central nervous system",
                                 description="Spinal cord, cranial nerves, and other parts of central nervous system") )
        setattr(cls, "Bone Marrow",
                PermissibleValue(text="Bone Marrow",
                                 description="Bone Marrow") )
        setattr(cls, "Liver and intrahepatic bile ducts",
                PermissibleValue(text="Liver and intrahepatic bile ducts",
                                 description="Liver and intrahepatic bile ducts") )
        setattr(cls, "Anus and anal canal",
                PermissibleValue(text="Anus and anal canal",
                                 description="Anus and anal canal") )
        setattr(cls, "Nervous System",
                PermissibleValue(text="Nervous System",
                                 description="Nervous System") )
        setattr(cls, "Hematopoietic and reticuloendothelial systems",
                PermissibleValue(text="Hematopoietic and reticuloendothelial systems",
                                 description="Hematopoietic and reticuloendothelial systems") )
        setattr(cls, "Bones, joints and articular cartilage of other and unspecified sites",
                PermissibleValue(text="Bones, joints and articular cartilage of other and unspecified sites",
                                 description="Bones, joints and articular cartilage of other and unspecified sites") )
        setattr(cls, "Head and Neck",
                PermissibleValue(text="Head and Neck",
                                 description="Head and Neck") )
        setattr(cls, "Nasal cavity and middle ear",
                PermissibleValue(text="Nasal cavity and middle ear",
                                 description="Nasal cavity and middle ear") )
        setattr(cls, "Eye and adnexa",
                PermissibleValue(text="Eye and adnexa",
                                 description="Eye and adnexa") )
        setattr(cls, "Bile Duct",
                PermissibleValue(text="Bile Duct",
                                 description="Bile Duct") )
        setattr(cls, "Peripheral nerves and autonomic nervous system",
                PermissibleValue(text="Peripheral nerves and autonomic nervous system",
                                 description="Peripheral nerves and autonomic nervous system") )
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable",
                                 description="Not Applicable") )

class EnumCRDC-H.ResearchSubject.indexTimepoint(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint
    """
    C164024 = PermissibleValue(text="C164024",
                                     description="Sample Procurement Date",
                                     meaning=NCIT.C164024)
    C164021 = PermissibleValue(text="C164021",
                                     description="First Patient Visit Date",
                                     meaning=NCIT.C164021)
    C164023 = PermissibleValue(text="C164023",
                                     description="Initial Genomic Sequencing Date",
                                     meaning=NCIT.C164023)
    C171136 = PermissibleValue(text="C171136",
                                     description="Date of Recurrence",
                                     meaning=NCIT.C171136)
    C164339 = PermissibleValue(text="C164339",
                                     description="Date of Diagnosis",
                                     meaning=NCIT.C164339)
    C164022 = PermissibleValue(text="C164022",
                                     description="First Treatment Date",
                                     meaning=NCIT.C164022)
    C139171 = PermissibleValue(text="C139171",
                                     description="Date of First Enrollment into Study",
                                     meaning=NCIT.C139171)

    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchSubject.indexTimepoint",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint",
        code_set=None,
        code_set_version="2021-05-27T15:46:50.778269+00:00",
    )

class EnumCRDC-H.Specimen.specimenType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen specimen_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.specimenType",
        description="Autogenerated Enumeration for CRDC-H Specimen specimen_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:50.943337+00:00",
    )

class EnumCRDC-H.Specimen.analyteType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen analyte_type
    """
    H = PermissibleValue(text="H",
                         description="H")
    S = PermissibleValue(text="S",
                         description="S")
    X = PermissibleValue(text="X",
                         description="X")
    E = PermissibleValue(text="E",
                         description="E")
    Y = PermissibleValue(text="Y",
                         description="Y")
    Protein = PermissibleValue(text="Protein",
                                     description="Protein")
    C174108 = PermissibleValue(text="C174108",
                                     description="Nucleic RNA Sample",
                                     meaning=NCIT.C174108)
    C156436 = PermissibleValue(text="C156436",
                                     description="Formalin-Fixed Paraffin-Embedded RNA",
                                     meaning=NCIT.C156436)
    C156435 = PermissibleValue(text="C156435",
                                     description="Formalin-Fixed Paraffin-Embedded DNA",
                                     meaning=NCIT.C156435)
    C156437 = PermissibleValue(text="C156437",
                                     description="REPLI-g Pooled DNA",
                                     meaning=NCIT.C156437)
    C128274 = PermissibleValue(text="C128274",
                                     description="Circulating Cell-Free DNA",
                                     meaning=NCIT.C128274)
    C156439 = PermissibleValue(text="C156439",
                                     description="REPLI-g X DNA",
                                     meaning=NCIT.C156439)
    C128788 = PermissibleValue(text="C128788",
                                     description="REPLI-g Whole Genome Amplification",
                                     meaning=NCIT.C128788)
    C128787 = PermissibleValue(text="C128787",
                                     description="GenomePlex Whole Genome Amplification",
                                     meaning=NCIT.C128787)
    C812 = PermissibleValue(text="C812",
                               description="Ribonucleic Acid",
                               meaning=NCIT.C812)
    C163995 = PermissibleValue(text="C163995",
                                     description="Total RNA",
                                     meaning=NCIT.C163995)
    C449 = PermissibleValue(text="C449",
                               description="DNA",
                               meaning=NCIT.C449)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.analyteType",
        description="Autogenerated Enumeration for CRDC-H Specimen analyte_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:51.095738+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "EBV Immortalized Normal",
                PermissibleValue(text="EBV Immortalized Normal",
                                 description="EBV Immortalized Normal") )

class EnumCRDC-H.Specimen.sourceMaterialType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen source_material_type
    """
    C36118 = PermissibleValue(text="C36118",
                                   description="In Situ Lesion",
                                   meaning=NCIT.C36118)
    C172293 = PermissibleValue(text="C172293",
                                     description="Original Tumor Cell Sample",
                                     meaning=NCIT.C172293)
    C172296 = PermissibleValue(text="C172296",
                                     description="Biospecimen on a Slide",
                                     meaning=NCIT.C172296)
    C164033 = PermissibleValue(text="C164033",
                                     description="Tumor-Adjacent Normal Post Neoadjuvant Therapy Sample",
                                     meaning=NCIT.C164033)
    C172267 = PermissibleValue(text="C172267",
                                     description="Formalin-Fixed Paraffin-Embedded Tissue Sample from Recurrent Disease",
                                     meaning=NCIT.C172267)
    C172295 = PermissibleValue(text="C172295",
                                     description="Next Generation Cancer Model",
                                     meaning=NCIT.C172295)
    C156444 = PermissibleValue(text="C156444",
                                     description="Post Neoadjuvant Therapy Sample",
                                     meaning=NCIT.C156444)
    C174119 = PermissibleValue(text="C174119",
                                     description="Saliva Sample",
                                     meaning=NCIT.C174119)
    C13049 = PermissibleValue(text="C13049",
                                   description="Lymphoid Tissue",
                                   meaning=NCIT.C13049)
    C164010 = PermissibleValue(text="C164010",
                                     description="Bone Marrow-Derived Fibroblasts",
                                     meaning=NCIT.C164010)
    C172264 = PermissibleValue(text="C172264",
                                     description="Buccal Cell Sample",
                                     meaning=NCIT.C172264)
    C174118 = PermissibleValue(text="C174118",
                                     description="Mixed Adherent Cells in Suspension",
                                     meaning=NCIT.C174118)
    C156441 = PermissibleValue(text="C156441",
                                     description="Sample Derived from New Primary",
                                     meaning=NCIT.C156441)
    C156443 = PermissibleValue(text="C156443",
                                     description="Cell Line-Derived Xenograft",
                                     meaning=NCIT.C156443)
    C135727 = PermissibleValue(text="C135727",
                                     description="Liquid Biopsy",
                                     meaning=NCIT.C135727)
    C164011 = PermissibleValue(text="C164011",
                                     description="Bone Marrow-Derived Mononuclear Cells",
                                     meaning=NCIT.C164011)
    C18009 = PermissibleValue(text="C18009",
                                   description="Tumor Tissue",
                                   meaning=NCIT.C18009)
    C84513 = PermissibleValue(text="C84513",
                                   description="Whole Bone Marrow",
                                   meaning=NCIT.C84513)
    C164014 = PermissibleValue(text="C164014",
                                     description="Solid Tissue Specimen",
                                     meaning=NCIT.C164014)
    C164015 = PermissibleValue(text="C164015",
                                     description="Blood Cancer-Derived Bone Marrow Specimen",
                                     meaning=NCIT.C164015)
    C164017 = PermissibleValue(text="C164017",
                                     description="Blood Cancer-Derived Bone Marrow Specimen, Post-Treatment",
                                     meaning=NCIT.C164017)
    C156439 = PermissibleValue(text="C156439",
                                     description="REPLI-g X DNA",
                                     meaning=NCIT.C156439)
    C164030 = PermissibleValue(text="C164030",
                                     description="Blood Cancer-Derived Blood Specimen",
                                     meaning=NCIT.C164030)
    C164031 = PermissibleValue(text="C164031",
                                     description="Blood Cancer-Derived Blood Specimen, Post-Treatment",
                                     meaning=NCIT.C164031)
    C12932 = PermissibleValue(text="C12932",
                                   description="Xenograft",
                                   meaning=NCIT.C12932)
    C41067 = PermissibleValue(text="C41067",
                                   description="Whole Blood",
                                   meaning=NCIT.C41067)
    C4798 = PermissibleValue(text="C4798",
                                 description="Recurrent Neoplasm",
                                 meaning=NCIT.C4798)
    C163993 = PermissibleValue(text="C163993",
                                     description="EBV Immortalized Lymphocytes",
                                     meaning=NCIT.C163993)
    C128788 = PermissibleValue(text="C128788",
                                     description="REPLI-g Whole Genome Amplification",
                                     meaning=NCIT.C128788)
    C128787 = PermissibleValue(text="C128787",
                                     description="GenomePlex Whole Genome Amplification",
                                     meaning=NCIT.C128787)
    C156440 = PermissibleValue(text="C156440",
                                     description="Metastatic Tumor Sample",
                                     meaning=NCIT.C156440)
    C8509 = PermissibleValue(text="C8509",
                                 description="Primary Neoplasm",
                                 meaning=NCIT.C8509)
    C12530 = PermissibleValue(text="C12530",
                                   description="Granulocyte",
                                   meaning=NCIT.C12530)
    C16403 = PermissibleValue(text="C16403",
                                   description="Cell Line",
                                   meaning=NCIT.C16403)
    C812 = PermissibleValue(text="C812",
                               description="Ribonucleic Acid",
                               meaning=NCIT.C812)
    C163995 = PermissibleValue(text="C163995",
                                     description="Total RNA",
                                     meaning=NCIT.C163995)
    C156442 = PermissibleValue(text="C156442",
                                     description="Control Analyte",
                                     meaning=NCIT.C156442)
    C3331 = PermissibleValue(text="C3331",
                                 description="Pleural Effusion",
                                 meaning=NCIT.C3331)
    C449 = PermissibleValue(text="C449",
                               description="DNA",
                               meaning=NCIT.C449)
    C3677 = PermissibleValue(text="C3677",
                                 description="Benign Neoplasm",
                                 meaning=NCIT.C3677)
    C65157 = PermissibleValue(text="C65157",
                                   description="Neoplasm, Uncertain Whether Benign or Malignant",
                                   meaning=NCIT.C65157)
    C141478 = PermissibleValue(text="C141478",
                                     description="Not Allowed To Collect",
                                     meaning=NCIT.C141478)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.sourceMaterialType",
        description="Autogenerated Enumeration for CRDC-H Specimen source_material_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:51.276015+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "FFPE Scrolls",
                PermissibleValue(text="FFPE Scrolls",
                                 description="FFPE Scrolls") )
        setattr(cls, "Recurrent Blood Derived Cancer - Peripheral Blood",
                PermissibleValue(text="Recurrent Blood Derived Cancer - Peripheral Blood",
                                 description="Recurrent Blood Derived Cancer - Peripheral Blood") )
        setattr(cls, "Expanded Next Generation Cancer Model",
                PermissibleValue(text="Expanded Next Generation Cancer Model",
                                 description="Expanded Next Generation Cancer Model") )
        setattr(cls, "Primary Xenograft Tissue",
                PermissibleValue(text="Primary Xenograft Tissue",
                                 description="Primary Xenograft Tissue") )
        setattr(cls, "Normal Adjacent Tissue",
                PermissibleValue(text="Normal Adjacent Tissue",
                                 description="Normal Adjacent Tissue") )
        setattr(cls, "99",
                PermissibleValue(text="99",
                                 description="99") )
        setattr(cls, "01",
                PermissibleValue(text="01",
                                 description="01") )
        setattr(cls, "42",
                PermissibleValue(text="42",
                                 description="42") )
        setattr(cls, "15",
                PermissibleValue(text="15",
                                 description="15") )
        setattr(cls, "32",
                PermissibleValue(text="32",
                                 description="32") )
        setattr(cls, "02",
                PermissibleValue(text="02",
                                 description="02") )
        setattr(cls, "16",
                PermissibleValue(text="16",
                                 description="16") )
        setattr(cls, "85",
                PermissibleValue(text="85",
                                 description="85") )
        setattr(cls, "86",
                PermissibleValue(text="86",
                                 description="86") )
        setattr(cls, "18",
                PermissibleValue(text="18",
                                 description="18") )
        setattr(cls, "08",
                PermissibleValue(text="08",
                                 description="08") )
        setattr(cls, "12",
                PermissibleValue(text="12",
                                 description="12") )
        setattr(cls, "41",
                PermissibleValue(text="41",
                                 description="41") )
        setattr(cls, "30",
                PermissibleValue(text="30",
                                 description="30") )
        setattr(cls, "31",
                PermissibleValue(text="31",
                                 description="31") )
        setattr(cls, "17",
                PermissibleValue(text="17",
                                 description="17") )

class EnumCRDC-H.Specimen.tumorStatusAtCollection(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.tumorStatusAtCollection",
        description="Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection",
        code_set=None,
        code_set_version="2021-05-27T15:46:51.520703+00:00",
    )

class EnumCRDC-H.Specimen.cellularCompositionType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type
    """
    C156445 = PermissibleValue(text="C156445",
                                     description="Derived Cell Line",
                                     meaning=NCIT.C156445)
    C20217 = PermissibleValue(text="C20217",
                                   description="Suspension Culture",
                                   meaning=NCIT.C20217)
    C172261 = PermissibleValue(text="C172261",
                                     description="Neurosphere",
                                     meaning=NCIT.C172261)
    C172260 = PermissibleValue(text="C172260",
                                     description="Air-Liquid Interface Organoid",
                                     meaning=NCIT.C172260)
    C126974 = PermissibleValue(text="C126974",
                                     description="Sorted Cells",
                                     meaning=NCIT.C126974)
    C19315 = PermissibleValue(text="C19315",
                                   description="Primary Cell Culture",
                                   meaning=NCIT.C19315)
    C20216 = PermissibleValue(text="C20216",
                                   description="Adherent Culture",
                                   meaning=NCIT.C20216)
    C172259 = PermissibleValue(text="C172259",
                                     description="Organoid",
                                     meaning=NCIT.C172259)
    C172258 = PermissibleValue(text="C172258",
                                     description="Modified Conditionally Reprogrammed Cells",
                                     meaning=NCIT.C172258)
    C172257 = PermissibleValue(text="C172257",
                                     description="Conditionally Reprogrammed Cells",
                                     meaning=NCIT.C172257)
    C13278 = PermissibleValue(text="C13278",
                                   description="Sputum",
                                   meaning=NCIT.C13278)
    C12535 = PermissibleValue(text="C12535",
                                   description="Lymphocyte",
                                   meaning=NCIT.C12535)
    C164009 = PermissibleValue(text="C164009",
                                     description="Bone Marrow Sample",
                                     meaning=NCIT.C164009)
    C164010 = PermissibleValue(text="C164010",
                                     description="Bone Marrow-Derived Fibroblasts",
                                     meaning=NCIT.C164010)
    C172264 = PermissibleValue(text="C172264",
                                     description="Buccal Cell Sample",
                                     meaning=NCIT.C172264)
    C174118 = PermissibleValue(text="C174118",
                                     description="Mixed Adherent Cells in Suspension",
                                     meaning=NCIT.C174118)
    C12508 = PermissibleValue(text="C12508",
                                   description="Cell",
                                   meaning=NCIT.C12508)
    C84507 = PermissibleValue(text="C84507",
                                   description="Buffy Coat",
                                   meaning=NCIT.C84507)
    C13275 = PermissibleValue(text="C13275",
                                   description="Saliva",
                                   meaning=NCIT.C13275)
    C164011 = PermissibleValue(text="C164011",
                                     description="Bone Marrow-Derived Mononuclear Cells",
                                     meaning=NCIT.C164011)
    C13356 = PermissibleValue(text="C13356",
                                   description="Plasma",
                                   meaning=NCIT.C13356)
    C13325 = PermissibleValue(text="C13325",
                                   description="Serum",
                                   meaning=NCIT.C13325)
    C84513 = PermissibleValue(text="C84513",
                                   description="Whole Bone Marrow",
                                   meaning=NCIT.C84513)
    C164014 = PermissibleValue(text="C164014",
                                     description="Solid Tissue Specimen",
                                     meaning=NCIT.C164014)
    C17610 = PermissibleValue(text="C17610",
                                   description="Blood Sample",
                                   meaning=NCIT.C17610)
    C41067 = PermissibleValue(text="C41067",
                                   description="Whole Blood",
                                   meaning=NCIT.C41067)
    C163993 = PermissibleValue(text="C163993",
                                     description="EBV Immortalized Lymphocytes",
                                     meaning=NCIT.C163993)
    C12530 = PermissibleValue(text="C12530",
                                   description="Granulocyte",
                                   meaning=NCIT.C12530)
    C156442 = PermissibleValue(text="C156442",
                                     description="Control Analyte",
                                     meaning=NCIT.C156442)
    C3331 = PermissibleValue(text="C3331",
                                 description="Pleural Effusion",
                                 meaning=NCIT.C3331)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.cellularCompositionType",
        description="Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:51.665298+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect",
                                 description="Not Allowed To Collect") )

class EnumCRDC-H.Specimen.generalTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology
    """
    C119010 = PermissibleValue(text="C119010",
                                     description="Peritumoral",
                                     meaning=NCIT.C119010)
    C25401 = PermissibleValue(text="C25401",
                                   description="Abnormal",
                                   meaning=NCIT.C25401)
    C14165 = PermissibleValue(text="C14165",
                                   description="Normal",
                                   meaning=NCIT.C14165)
    C18009 = PermissibleValue(text="C18009",
                                   description="Tumor Tissue",
                                   meaning=NCIT.C18009)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.generalTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-27T15:46:51.875075+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect",
                                 description="Not Allowed To Collect") )

class EnumCRDC-H.Specimen.specificTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology
    """
    C3512 = PermissibleValue(text="C3512",
                                 description="Lung Adenocarcinoma",
                                 meaning=NCIT.C3512)
    C3493 = PermissibleValue(text="C3493",
                                 description="Lung Squamous Cell Carcinoma",
                                 meaning=NCIT.C3493)
    C7558 = PermissibleValue(text="C7558",
                                 description="Endometrial Carcinoma",
                                 meaning=NCIT.C7558)
    C4349 = PermissibleValue(text="C4349",
                                 description="Colon Adenocarcinoma",
                                 meaning=NCIT.C4349)
    C7978 = PermissibleValue(text="C7978",
                                 description="Ovarian Serous Cystadenocarcinoma",
                                 meaning=NCIT.C7978)
    C9245 = PermissibleValue(text="C9245",
                                 description="Invasive Breast Carcinoma",
                                 meaning=NCIT.C9245)
    C156442 = PermissibleValue(text="C156442",
                                     description="Control Analyte",
                                     meaning=NCIT.C156442)
    C6975 = PermissibleValue(text="C6975",
                                 description="Papillary Renal Cell Carcinoma",
                                 meaning=NCIT.C6975)
    C4033 = PermissibleValue(text="C4033",
                                 description="Clear Cell Renal Cell Carcinoma",
                                 meaning=NCIT.C4033)
    C132067 = PermissibleValue(text="C132067",
                                     description="Low Grade Glioma",
                                     meaning=NCIT.C132067)
    C7464 = PermissibleValue(text="C7464",
                                 description="Acute Leukemia of Ambiguous Lineage",
                                 meaning=NCIT.C7464)
    C9291 = PermissibleValue(text="C9291",
                                 description="Anal Carcinoma",
                                 meaning=NCIT.C9291)
    C8715 = PermissibleValue(text="C8715",
                                 description="Rhabdoid Tumor of the Kidney",
                                 meaning=NCIT.C8715)
    C3222 = PermissibleValue(text="C3222",
                                 description="Medulloblastoma",
                                 meaning=NCIT.C3222)
    C4878 = PermissibleValue(text="C4878",
                                 description="Lung Carcinoma",
                                 meaning=NCIT.C4878)
    C9039 = PermissibleValue(text="C9039",
                                 description="Cervical Carcinoma",
                                 meaning=NCIT.C9039)
    C9306 = PermissibleValue(text="C9306",
                                 description="Soft Tissue Sarcoma",
                                 meaning=NCIT.C9306)
    C4264 = PermissibleValue(text="C4264",
                                 description="Clear Cell Sarcoma of the Kidney",
                                 meaning=NCIT.C4264)
    C3267 = PermissibleValue(text="C3267",
                                 description="Wilms Tumor",
                                 meaning=NCIT.C3267)
    C3017 = PermissibleValue(text="C3017",
                                 description="Ependymoma",
                                 meaning=NCIT.C3017)
    C4817 = PermissibleValue(text="C4817",
                                 description="Ewing Sarcoma",
                                 meaning=NCIT.C4817)
    C3359 = PermissibleValue(text="C3359",
                                 description="Rhabdomyosarcoma",
                                 meaning=NCIT.C3359)
    C9145 = PermissibleValue(text="C9145",
                                 description="Osteosarcoma",
                                 meaning=NCIT.C9145)
    C3270 = PermissibleValue(text="C3270",
                                 description="Neuroblastoma",
                                 meaning=NCIT.C3270)
    C3720 = PermissibleValue(text="C3720",
                                 description="Anaplastic Large Cell Lymphoma",
                                 meaning=NCIT.C3720)
    C8851 = PermissibleValue(text="C8851",
                                 description="Diffuse Large B-Cell Lymphoma",
                                 meaning=NCIT.C8851)
    C3171 = PermissibleValue(text="C3171",
                                 description="Acute Myeloid Leukemia",
                                 meaning=NCIT.C3171)
    C3058 = PermissibleValue(text="C3058",
                                 description="Glioblastoma",
                                 meaning=NCIT.C3058)
    C2912 = PermissibleValue(text="C2912",
                                 description="Burkitt Lymphoma",
                                 meaning=NCIT.C2912)
    C3167 = PermissibleValue(text="C3167",
                                 description="Acute Lymphoblastic Leukemia",
                                 meaning=NCIT.C3167)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.specificTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.051784+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CNS, rhabdoid tumor",
                PermissibleValue(text="CNS, rhabdoid tumor",
                                 description="CNS, rhabdoid tumor") )
        setattr(cls, "Induction Failure AML (AML-IF)",
                PermissibleValue(text="Induction Failure AML (AML-IF)",
                                 description="Induction Failure AML (AML-IF)") )
        setattr(cls, "CNS, other",
                PermissibleValue(text="CNS, other",
                                 description="CNS, other") )
        setattr(cls, "Non cancerous tissue",
                PermissibleValue(text="Non cancerous tissue",
                                 description="Non cancerous tissue") )

class EnumCRDC-H.Specimen.preinvasiveTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.preinvasiveTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.277476+00:00",
    )

class EnumCRDC-H.Specimen.morphologyAssessorRole(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.morphologyAssessorRole",
        description="Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.422089+00:00",
    )

class EnumCRDC-H.Specimen.morphlogyAssessmentMethod(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.morphlogyAssessmentMethod",
        description="Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.586317+00:00",
    )

class EnumCRDC-H.Specimen.degreeOfDysplasia(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.degreeOfDysplasia",
        description="Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.734082+00:00",
    )

class EnumCRDC-H.Specimen.sectionLocation(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen section_location
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.sectionLocation",
        description="Autogenerated Enumeration for CRDC-H Specimen section_location",
        code_set=None,
        code_set_version="2021-05-27T15:46:52.878312+00:00",
    )

class EnumCRDC-H.SpecimenContainer.containerType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer container_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenContainer.containerType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer container_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.021065+00:00",
    )

class EnumCRDC-H.SpecimenContainer.chargeType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenContainer.chargeType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.166127+00:00",
    )

class EnumCRDC-H.SpecimenCreationActivity.activityType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity activity_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.activityType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity activity_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.310194+00:00",
    )

class EnumCRDC-H.SpecimenCreationActivity.collectionMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type
    """
    Yes = PermissibleValue(text="Yes",
                             description="Yes")
    No = PermissibleValue(text="No",
                           description="No")
    C91839 = PermissibleValue(text="C91839",
                                   description="Supracricoid Laryngectomy",
                                   meaning=NCIT.C91839)
    C51632 = PermissibleValue(text="C51632",
                                   description="Total Nephrectomy",
                                   meaning=NCIT.C51632)
    C164212 = PermissibleValue(text="C164212",
                                     description="Tumor Resection",
                                     meaning=NCIT.C164212)
    C163997 = PermissibleValue(text="C163997",
                                     description="Thoracoscopic Biopsy",
                                     meaning=NCIT.C163997)
    C172322 = PermissibleValue(text="C172322",
                                     description="Buccal Mucosal Resection",
                                     meaning=NCIT.C172322)
    C165183 = PermissibleValue(text="C165183",
                                     description="Laparoscopic Radical Prostatectomy with Robotics",
                                     meaning=NCIT.C165183)
    C165179 = PermissibleValue(text="C165179",
                                     description="Hand Assisted Laparoscopic Radical Nephrectomy",
                                     meaning=NCIT.C165179)
    C165186 = PermissibleValue(text="C165186",
                                     description="Open Partial Nephrectomy",
                                     meaning=NCIT.C165186)
    C165187 = PermissibleValue(text="C165187",
                                     description="Open Radical Nephrectomy",
                                     meaning=NCIT.C165187)
    C165188 = PermissibleValue(text="C165188",
                                     description="Open Radical Prostatectomy",
                                     meaning=NCIT.C165188)
    C165180 = PermissibleValue(text="C165180",
                                     description="Laparoscopic Biopsy",
                                     meaning=NCIT.C165180)
    C165181 = PermissibleValue(text="C165181",
                                     description="Laparoscopic Partial Nephrectomy",
                                     meaning=NCIT.C165181)
    C165182 = PermissibleValue(text="C165182",
                                     description="Laparoscopic Radical Nephrectomy",
                                     meaning=NCIT.C165182)
    C51910 = PermissibleValue(text="C51910",
                                   description="Superficial Parotidectomy",
                                   meaning=NCIT.C51910)
    C51781 = PermissibleValue(text="C51781",
                                   description="Total Hepatectomy",
                                   meaning=NCIT.C51781)
    C51656 = PermissibleValue(text="C51656",
                                   description="Maxillectomy",
                                   meaning=NCIT.C51656)
    C51657 = PermissibleValue(text="C51657",
                                   description="Partial Maxillectomy",
                                   meaning=NCIT.C51657)
    C94240 = PermissibleValue(text="C94240",
                                   description="Partial Laryngectomy",
                                   meaning=NCIT.C94240)
    C159342 = PermissibleValue(text="C159342",
                                     description="Ascites Drainage",
                                     meaning=NCIT.C159342)
    C160999 = PermissibleValue(text="C160999",
                                     description="Endolaryngeal Excision",
                                     meaning=NCIT.C160999)
    C160997 = PermissibleValue(text="C160997",
                                     description="Palatectomy",
                                     meaning=NCIT.C160997)
    C161002 = PermissibleValue(text="C161002",
                                     description="Deep Parotidectomy",
                                     meaning=NCIT.C161002)
    C172324 = PermissibleValue(text="C172324",
                                     description="Total Maxillectomy",
                                     meaning=NCIT.C172324)
    C172325 = PermissibleValue(text="C172325",
                                     description="Subtotal Prostatectomy",
                                     meaning=NCIT.C172325)
    C118358 = PermissibleValue(text="C118358",
                                     description="Exoresection",
                                     meaning=NCIT.C118358)
    C91840 = PermissibleValue(text="C91840",
                                   description="Transoral Laser Microsurgery",
                                   meaning=NCIT.C91840)
    C51623 = PermissibleValue(text="C51623",
                                   description="Right Colectomy",
                                   meaning=NCIT.C51623)
    C51664 = PermissibleValue(text="C51664",
                                   description="Mandibulectomy",
                                   meaning=NCIT.C51664)
    C126397 = PermissibleValue(text="C126397",
                                     description="Supracervical Hysterectomy",
                                     meaning=NCIT.C126397)
    C165178 = PermissibleValue(text="C165178",
                                     description="Endorectal Tumor Resection",
                                     meaning=NCIT.C165178)
    C51889 = PermissibleValue(text="C51889",
                                   description="Supraglottic Laryngectomy",
                                   meaning=NCIT.C51889)
    C51924 = PermissibleValue(text="C51924",
                                   description="Total Colectomy",
                                   meaning=NCIT.C51924)
    C51771 = PermissibleValue(text="C51771",
                                   description="Total Laryngectomy",
                                   meaning=NCIT.C51771)
    C51490 = PermissibleValue(text="C51490",
                                   description="Parotidectomy",
                                   meaning=NCIT.C51490)
    C51612 = PermissibleValue(text="C51612",
                                   description="Transverse Colectomy",
                                   meaning=NCIT.C51612)
    C15305 = PermissibleValue(text="C15305",
                                   description="Pneumonectomy",
                                   meaning=NCIT.C15305)
    C15310 = PermissibleValue(text="C15310",
                                   description="Paracentesis",
                                   meaning=NCIT.C15310)
    C15394 = PermissibleValue(text="C15394",
                                   description="Partial Hepatectomy",
                                   meaning=NCIT.C15394)
    C150660 = PermissibleValue(text="C150660",
                                     description="Laryngopharyngectomy",
                                     meaning=NCIT.C150660)
    C103242 = PermissibleValue(text="C103242",
                                     description="Endoscopic Mucosal Resection",
                                     meaning=NCIT.C103242)
    C165184 = PermissibleValue(text="C165184",
                                     description="Laparoscopic Radical Prostatectomy",
                                     meaning=NCIT.C165184)
    C51906 = PermissibleValue(text="C51906",
                                   description="Hemilaryngectomy",
                                   meaning=NCIT.C51906)
    C15278 = PermissibleValue(text="C15278",
                                   description="Modified Radical Mastectomy",
                                   meaning=NCIT.C15278)
    C116651 = PermissibleValue(text="C116651",
                                     description="Transurethral Resection of Bladder Tumor",
                                     meaning=NCIT.C116651)
    C113716 = PermissibleValue(text="C113716",
                                     description="Low Anterior Resection",
                                     meaning=NCIT.C113716)
    C103239 = PermissibleValue(text="C103239",
                                     description="Total Proctocolectomy",
                                     meaning=NCIT.C103239)
    C91826 = PermissibleValue(text="C91826",
                                   description="Abdominoperineal Resection",
                                   meaning=NCIT.C91826)
    C91838 = PermissibleValue(text="C91838",
                                   description="Sigmoidectomy",
                                   meaning=NCIT.C91838)
    C51787 = PermissibleValue(text="C51787",
                                   description="Omentectomy",
                                   meaning=NCIT.C51787)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17649 = PermissibleValue(text="C17649",
                                   description="Other",
                                   meaning=NCIT.C17649)
    C141478 = PermissibleValue(text="C141478",
                                     description="Not Allowed To Collect",
                                     meaning=NCIT.C141478)
    C48658 = PermissibleValue(text="C48658",
                                   description="Indeterminate",
                                   meaning=NCIT.C48658)
    C15701 = PermissibleValue(text="C15701",
                                   description="Total Hysterectomy",
                                   meaning=NCIT.C15701)
    C15189 = PermissibleValue(text="C15189",
                                   description="Biopsy",
                                   meaning=NCIT.C15189)
    C17610 = PermissibleValue(text="C17610",
                                   description="Blood Sample",
                                   meaning=NCIT.C17610)
    C15361 = PermissibleValue(text="C15361",
                                   description="Fine-Needle Aspiration",
                                   meaning=NCIT.C15361)
    C15680 = PermissibleValue(text="C15680",
                                   description="Core Biopsy",
                                   meaning=NCIT.C15680)
    C15392 = PermissibleValue(text="C15392",
                                   description="Thoracentesis",
                                   meaning=NCIT.C15392)
    C15749 = PermissibleValue(text="C15749",
                                   description="Tumor Debulking",
                                   meaning=NCIT.C15749)
    C158758 = PermissibleValue(text="C158758",
                                     description="Resection",
                                     meaning=NCIT.C158758)
    C15275 = PermissibleValue(text="C15275",
                                   description="Lymphadenectomy",
                                   meaning=NCIT.C15275)
    C15256 = PermissibleValue(text="C15256",
                                   description="Hysterectomy",
                                   meaning=NCIT.C15256)
    C15386 = PermissibleValue(text="C15386",
                                   description="Incisional Biopsy",
                                   meaning=NCIT.C15386)
    C15385 = PermissibleValue(text="C15385",
                                   description="Excisional Biopsy",
                                   meaning=NCIT.C15385)
    C15281 = PermissibleValue(text="C15281",
                                   description="Total Mastectomy",
                                   meaning=NCIT.C15281)
    C25153 = PermissibleValue(text="C25153",
                                   description="Autopsy",
                                   meaning=NCIT.C25153)
    C15399 = PermissibleValue(text="C15399",
                                   description="Radical Prostatectomy",
                                   meaning=NCIT.C15399)
    C133261 = PermissibleValue(text="C133261",
                                     description="Bone Marrow Aspirate",
                                     meaning=NCIT.C133261)
    C135727 = PermissibleValue(text="C135727",
                                     description="Liquid Biopsy",
                                     meaning=NCIT.C135727)
    C48601 = PermissibleValue(text="C48601",
                                   description="Enucleation",
                                   meaning=NCIT.C48601)
    C94470 = PermissibleValue(text="C94470",
                                   description="Radical Hysterectomy",
                                   meaning=NCIT.C94470)
    C15342 = PermissibleValue(text="C15342",
                                   description="Transplantation",
                                   meaning=NCIT.C15342)
    C15288 = PermissibleValue(text="C15288",
                                   description="Orchiectomy",
                                   meaning=NCIT.C15288)
    C131680 = PermissibleValue(text="C131680",
                                     description="Partial Resection",
                                     meaning=NCIT.C131680)
    C15291 = PermissibleValue(text="C15291",
                                   description="Oophorectomy",
                                   meaning=NCIT.C15291)
    C15190 = PermissibleValue(text="C15190",
                                   description="Needle Biopsy",
                                   meaning=NCIT.C15190)
    C15343 = PermissibleValue(text="C15343",
                                   description="Transurethral Prostatic Resection",
                                   meaning=NCIT.C15343)
    C15755 = PermissibleValue(text="C15755",
                                   description="Lumpectomy",
                                   meaning=NCIT.C15755)
    C51928 = PermissibleValue(text="C51928",
                                   description="Partial Nephrectomy",
                                   meaning=NCIT.C51928)
    C28743 = PermissibleValue(text="C28743",
                                   description="Punch Biopsy",
                                   meaning=NCIT.C28743)
    C15294 = PermissibleValue(text="C15294",
                                   description="Pancreatectomy",
                                   meaning=NCIT.C15294)
    C15214 = PermissibleValue(text="C15214",
                                   description="Craniotomy",
                                   meaning=NCIT.C15214)
    C131672 = PermissibleValue(text="C131672",
                                     description="Gross Total Resection",
                                     meaning=NCIT.C131672)
    C13347 = PermissibleValue(text="C13347",
                                   description="Aspirate",
                                   meaning=NCIT.C13347)
    C51690 = PermissibleValue(text="C51690",
                                   description="Wedge Excision",
                                   meaning=NCIT.C51690)
    C51778 = PermissibleValue(text="C51778",
                                   description="Radical Nephrectomy",
                                   meaning=NCIT.C51778)
    C15356 = PermissibleValue(text="C15356",
                                   description="Whipple Procedure",
                                   meaning=NCIT.C15356)
    C15389 = PermissibleValue(text="C15389",
                                   description="Endoscopic Biopsy",
                                   meaning=NCIT.C15389)
    C15272 = PermissibleValue(text="C15272",
                                   description="Lobectomy",
                                   meaning=NCIT.C15272)
    C15217 = PermissibleValue(text="C15217",
                                   description="Cystectomy",
                                   meaning=NCIT.C15217)
    C51624 = PermissibleValue(text="C51624",
                                   description="Left Colectomy",
                                   meaning=NCIT.C51624)
    C51605 = PermissibleValue(text="C51605",
                                   description="Salpingectomy",
                                   meaning=NCIT.C51605)
    C51679 = PermissibleValue(text="C51679",
                                   description="Tonsillectomy",
                                   meaning=NCIT.C51679)
    C159340 = PermissibleValue(text="C159340",
                                     description="Peritoneal Lavage",
                                     meaning=NCIT.C159340)
    C94461 = PermissibleValue(text="C94461",
                                   description="Metastasectomy",
                                   meaning=NCIT.C94461)
    C51604 = PermissibleValue(text="C51604",
                                   description="Glossectomy",
                                   meaning=NCIT.C51604)

    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.collectionMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.459207+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Salpingo-oophorectomy",
                PermissibleValue(text="Salpingo-oophorectomy",
                                 description="Salpingo-oophorectomy") )
        setattr(cls, "Other Surgical Resection",
                PermissibleValue(text="Other Surgical Resection",
                                 description="Other Surgical Resection") )

class EnumCRDC-H.SpecimenCreationActivity.derivationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.derivationMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.747316+00:00",
    )

class EnumCRDC-H.SpecimenProcessingActivity.activityType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity activity_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenProcessingActivity.activityType",
        description="Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity activity_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:53.891937+00:00",
    )

class EnumCRDC-H.SpecimenProcessingActivity.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type
    """
    true = PermissibleValue(text="true",
                               description="true")
    false = PermissibleValue(text="false",
                                 description="false")
    C63523 = PermissibleValue(text="C63523",
                                   description="Optimal Cutting Temperature Compound",
                                   meaning=NCIT.C63523)
    C143028 = PermissibleValue(text="C143028",
                                     description="Formalin-Fixed Paraffin-Embedded",
                                     meaning=NCIT.C143028)
    C84517 = PermissibleValue(text="C84517",
                                   description="Fresh Specimen",
                                   meaning=NCIT.C84517)
    C70717 = PermissibleValue(text="C70717",
                                   description="Frozen Specimen",
                                   meaning=NCIT.C70717)
    C63521 = PermissibleValue(text="C63521",
                                   description="Quick Freeze",
                                   meaning=NCIT.C63521)
    C16475 = PermissibleValue(text="C16475",
                                   description="Cryopreservation",
                                   meaning=NCIT.C16475)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenProcessingActivity.methodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.036358+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect",
                                 description="Not Allowed To Collect") )

class EnumCRDC-H.SpecimenStorageActivity.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenStorageActivity.methodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.209569+00:00",
    )

class EnumCRDC-H.Subject.species(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject species
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.species",
        description="Autogenerated Enumeration for CRDC-H Subject species",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.393972+00:00",
    )

class EnumCRDC-H.Subject.breed(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject breed
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.breed",
        description="Autogenerated Enumeration for CRDC-H Subject breed",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.549391+00:00",
    )

class EnumCRDC-H.Subject.sex(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject sex
    """
    C16576 = PermissibleValue(text="C16576",
                                   description="Female",
                                   meaning=NCIT.C16576)
    C20197 = PermissibleValue(text="C20197",
                                   description="Male",
                                   meaning=NCIT.C20197)
    C38046 = PermissibleValue(text="C38046",
                                   description="Unspecified",
                                   meaning=NCIT.C38046)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.sex",
        description="Autogenerated Enumeration for CRDC-H Subject sex",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.691890+00:00",
    )

class EnumCRDC-H.Subject.ethnicity(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject ethnicity
    """
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")
    C41222 = PermissibleValue(text="C41222",
                                   description="Not Hispanic or Latino",
                                   meaning=NCIT.C41222)
    C17459 = PermissibleValue(text="C17459",
                                   description="Hispanic or Latino",
                                   meaning=NCIT.C17459)
    C141478 = PermissibleValue(text="C141478",
                                     description="Not Allowed To Collect",
                                     meaning=NCIT.C141478)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.ethnicity",
        description="Autogenerated Enumeration for CRDC-H Subject ethnicity",
        code_set=None,
        code_set_version="2021-05-27T15:46:54.857987+00:00",
    )

class EnumCRDC-H.Subject.race(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject race
    """
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")
    C16352 = PermissibleValue(text="C16352",
                                   description="Black or African American",
                                   meaning=NCIT.C16352)
    C41219 = PermissibleValue(text="C41219",
                                   description="Native Hawaiian or Other Pacific Islander",
                                   meaning=NCIT.C41219)
    C41260 = PermissibleValue(text="C41260",
                                   description="Asian",
                                   meaning=NCIT.C41260)
    C41259 = PermissibleValue(text="C41259",
                                   description="American Indian or Alaska Native",
                                   meaning=NCIT.C41259)
    C41261 = PermissibleValue(text="C41261",
                                   description="White",
                                   meaning=NCIT.C41261)
    C141478 = PermissibleValue(text="C141478",
                                     description="Not Allowed To Collect",
                                     meaning=NCIT.C141478)
    C17649 = PermissibleValue(text="C17649",
                                   description="Other",
                                   meaning=NCIT.C17649)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.race",
        description="Autogenerated Enumeration for CRDC-H Subject race",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.024955+00:00",
    )

class EnumCRDC-H.Subject.vitalStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject vital_status
    """
    C37987 = PermissibleValue(text="C37987",
                                   description="Alive",
                                   meaning=NCIT.C37987)
    C28554 = PermissibleValue(text="C28554",
                                   description="Dead",
                                   meaning=NCIT.C28554)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.vitalStatus",
        description="Autogenerated Enumeration for CRDC-H Subject vital_status",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.199468+00:00",
    )

class EnumCRDC-H.Subject.causeOfDeath(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject cause_of_death
    """
    C164157 = PermissibleValue(text="C164157",
                                     description="Surgical Complication",
                                     meaning=NCIT.C164157)
    C85075 = PermissibleValue(text="C85075",
                                   description="Spinal Muscular Atrophy",
                                   meaning=NCIT.C85075)
    C156428 = PermissibleValue(text="C156428",
                                     description="Non-Cancer Related Death",
                                     meaning=NCIT.C156428)
    C27990 = PermissibleValue(text="C27990",
                                   description="Toxicity",
                                   meaning=NCIT.C27990)
    C8278 = PermissibleValue(text="C8278",
                                 description="Cancer-Related Condition",
                                 meaning=NCIT.C8278)
    C9439 = PermissibleValue(text="C9439",
                                 description="Chronic Kidney Disease, Stage 5",
                                 meaning=NCIT.C9439)
    C2931 = PermissibleValue(text="C2931",
                                 description="Cardiovascular Disorder",
                                 meaning=NCIT.C2931)
    C3149 = PermissibleValue(text="C3149",
                                 description="Kidney Disorder",
                                 meaning=NCIT.C3149)
    C26726 = PermissibleValue(text="C26726",
                                   description="Infectious Disorder",
                                   meaning=NCIT.C26726)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.causeOfDeath",
        description="Autogenerated Enumeration for CRDC-H Subject cause_of_death",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.394072+00:00",
    )

class EnumCRDC-H.Substance.substanceType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance substance_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Substance.substanceType",
        description="Autogenerated Enumeration for CRDC-H Substance substance_type",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.571454+00:00",
    )

class EnumCRDC-H.Substance.role(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance role
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Substance.role",
        description="Autogenerated Enumeration for CRDC-H Substance role",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.719056+00:00",
    )

class EnumCRDC-H.TimePoint.indexEventType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TimePoint indexEventType
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TimePoint.indexEventType",
        description="Autogenerated Enumeration for CRDC-H TimePoint indexEventType",
        code_set=None,
        code_set_version="2021-05-27T15:46:55.866722+00:00",
    )

class EnumCRDC-H.Treatment.type(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment type
    """
    C15533 = PermissibleValue(text="C15533",
                                   description="Chemoprotection",
                                   meaning=NCIT.C15533)
    C165192 = PermissibleValue(text="C165192",
                                     description="Combination Radiotherapy",
                                     meaning=NCIT.C165192)
    C93196 = PermissibleValue(text="C93196",
                                   description="Syngeneic Stem Cell Transplantation",
                                   meaning=NCIT.C93196)
    C152055 = PermissibleValue(text="C152055",
                                     description="Direct Mixed Photon and Electron Field",
                                     meaning=NCIT.C152055)
    C165194 = PermissibleValue(text="C165194",
                                     description="Stem Cell Therapy",
                                     meaning=NCIT.C165194)
    C64172 = PermissibleValue(text="C64172",
                                   description="Anticonvulsant Therapy",
                                   meaning=NCIT.C64172)
    C92991 = PermissibleValue(text="C92991",
                                   description="Systemic Radiation Therapy",
                                   meaning=NCIT.C92991)
    C95484 = PermissibleValue(text="C95484",
                                   description="CyberKnife",
                                   meaning=NCIT.C95484)
    C17998 = PermissibleValue(text="C17998",
                                   description="Unknown",
                                   meaning=NCIT.C17998)
    C43234 = PermissibleValue(text="C43234",
                                   description="Not Reported",
                                   meaning=NCIT.C43234)
    C17649 = PermissibleValue(text="C17649",
                                   description="Other",
                                   meaning=NCIT.C17649)
    C15195 = PermissibleValue(text="C15195",
                                   description="Internal Radiation Therapy",
                                   meaning=NCIT.C15195)
    C15329 = PermissibleValue(text="C15329",
                                   description="Surgical Procedure",
                                   meaning=NCIT.C15329)
    C15313 = PermissibleValue(text="C15313",
                                   description="Radiation Therapy",
                                   meaning=NCIT.C15313)
    C15632 = PermissibleValue(text="C15632",
                                   description="Chemotherapy",
                                   meaning=NCIT.C15632)
    C15445 = PermissibleValue(text="C15445",
                                   description="Hormone Therapy",
                                   meaning=NCIT.C15445)
    C15751 = PermissibleValue(text="C15751",
                                   description="External Beam Radiation Therapy",
                                   meaning=NCIT.C15751)
    C15215 = PermissibleValue(text="C15215",
                                   description="Cryosurgery",
                                   meaning=NCIT.C15215)
    C15289 = PermissibleValue(text="C15289",
                                   description="Organ Transplantation",
                                   meaning=NCIT.C15289)
    C15431 = PermissibleValue(text="C15431",
                                   description="Hematopoietic Cell Transplantation",
                                   meaning=NCIT.C15431)
    C15262 = PermissibleValue(text="C15262",
                                   description="Immunotherapy",
                                   meaning=NCIT.C15262)
    C67444 = PermissibleValue(text="C67444",
                                   description="Ethanol Ablation Therapy",
                                   meaning=NCIT.C67444)
    C16035 = PermissibleValue(text="C16035",
                                   description="3-Dimensional Conformal Radiation Therapy",
                                   meaning=NCIT.C16035)
    C138187 = PermissibleValue(text="C138187",
                                     description="Haploidentical Hematopoietic Cell Transplantation",
                                     meaning=NCIT.C138187)
    C20985 = PermissibleValue(text="C20985",
                                   description="Ablation Therapy",
                                   meaning=NCIT.C20985)
    C16135 = PermissibleValue(text="C16135",
                                   description="Intensity-Modulated Radiation Therapy",
                                   meaning=NCIT.C16135)
    C16039 = PermissibleValue(text="C16039",
                                   description="Autologous Hematopoietic Stem Cell Transplantation",
                                   meaning=NCIT.C16039)
    C46089 = PermissibleValue(text="C46089",
                                   description="Allogeneic Hematopoietic Stem Cell Transplantation",
                                   meaning=NCIT.C46089)
    C15986 = PermissibleValue(text="C15986",
                                   description="Pharmacotherapy",
                                   meaning=NCIT.C15986)
    C15358 = PermissibleValue(text="C15358",
                                   description="Stereotactic Radiosurgery",
                                   meaning=NCIT.C15358)
    C66897 = PermissibleValue(text="C66897",
                                   description="Proton Beam Radiation Therapy",
                                   meaning=NCIT.C66897)
    C157968 = PermissibleValue(text="C157968",
                                     description="Radioactive Iodine Therapy",
                                     meaning=NCIT.C157968)
    C15666 = PermissibleValue(text="C15666",
                                   description="Radiofrequency Ablation",
                                   meaning=NCIT.C15666)
    C15696 = PermissibleValue(text="C15696",
                                   description="Radiosurgery",
                                   meaning=NCIT.C15696)
    C15747 = PermissibleValue(text="C15747",
                                   description="Supportive Care",
                                   meaning=NCIT.C15747)
    C62714 = PermissibleValue(text="C62714",
                                   description="Nonmyeloablative Allogeneic Hematopoietic Stem Cell Transplantation",
                                   meaning=NCIT.C62714)
    C66899 = PermissibleValue(text="C66899",
                                   description="Pleurodesis",
                                   meaning=NCIT.C66899)
    C66891 = PermissibleValue(text="C66891",
                                   description="Interstitial Radiation Therapy",
                                   meaning=NCIT.C66891)
    C76243 = PermissibleValue(text="C76243",
                                   description="Targeted Molecular Therapy",
                                   meaning=NCIT.C76243)
    C93340 = PermissibleValue(text="C93340",
                                   description="Radioembolization",
                                   meaning=NCIT.C93340)
    C798 = PermissibleValue(text="C798",
                               description="Radiosensitizing Agent",
                               meaning=NCIT.C798)
    C15651 = PermissibleValue(text="C15651",
                                   description="High-Dose Rate Brachytherapy",
                                   meaning=NCIT.C15651)
    C15393 = PermissibleValue(text="C15393",
                                   description="Isolated Chemotherapeutic Limb Perfusion",
                                   meaning=NCIT.C15393)
    C15230 = PermissibleValue(text="C15230",
                                   description="Embolization Therapy",
                                   meaning=NCIT.C15230)
    C70840 = PermissibleValue(text="C70840",
                                   description="Blinded Clinical Study",
                                   meaning=NCIT.C70840)
    C165189 = PermissibleValue(text="C165189",
                                     description="Conventional Radiotherapy",
                                     meaning=NCIT.C165189)
    C15370 = PermissibleValue(text="C15370",
                                   description="Steroid Therapy",
                                   meaning=NCIT.C15370)
    C15752 = PermissibleValue(text="C15752",
                                   description="Chemoembolization",
                                   meaning=NCIT.C15752)
    C62726 = PermissibleValue(text="C62726",
                                   description="Hypofractionated Radiation Therapy",
                                   meaning=NCIT.C62726)
    C104914 = PermissibleValue(text="C104914",
                                     description="Photon Beam Radiation Therapy",
                                     meaning=NCIT.C104914)
    C116466 = PermissibleValue(text="C116466",
                                     description="Autologous-Autologous Tandem Hematopoietic Stem Cell Transplantation",
                                     meaning=NCIT.C116466)
    C443 = PermissibleValue(text="C443",
                               description="Biphosphonate",
                               meaning=NCIT.C443)
    C116643 = PermissibleValue(text="C116643",
                                     description="Microwave Ablation",
                                     meaning=NCIT.C116643)
    C15470 = PermissibleValue(text="C15470",
                                   description="Isotope Therapy",
                                   meaning=NCIT.C15470)
    C141342 = PermissibleValue(text="C141342",
                                     description="Concurrent Chemoradiation",
                                     meaning=NCIT.C141342)
    C85254 = PermissibleValue(text="C85254",
                                   description="Low-Dose Rate Brachytherapy",
                                   meaning=NCIT.C85254)
    C15382 = PermissibleValue(text="C15382",
                                   description="Gamma Knife",
                                   meaning=NCIT.C15382)

    _defn = EnumDefinition(
        name="EnumCRDC-H.Treatment.type",
        description="Autogenerated Enumeration for CRDC-H Treatment type",
        code_set=None,
        code_set_version="2021-05-27T15:46:56.015730+00:00",
    )

# Slots
class slots:
    pass

slots.bodySite__site = Slot(uri=CCDH.site, name="bodySite__site", curie=CCDH.curie('site'),
                   model_uri=CCDH.bodySite__site, domain=None, range=Union[str, "EnumCRDC-H.BodySite.site"])

slots.bodySite__qualifier = Slot(uri=CCDH.qualifier, name="bodySite__qualifier", curie=CCDH.curie('qualifier'),
                   model_uri=CCDH.bodySite__qualifier, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.BodySite.qualifier"], List[Union[str, "EnumCRDC-H.BodySite.qualifier"]]]])

slots.biologicProduct__id = Slot(uri=CCDH.id, name="biologicProduct__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.biologicProduct__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicProduct__identifier = Slot(uri=CCDH.identifier, name="biologicProduct__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.biologicProduct__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.biologicProduct__description = Slot(uri=CCDH.description, name="biologicProduct__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.biologicProduct__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicProduct__product_type = Slot(uri=CCDH.product_type, name="biologicProduct__product_type", curie=CCDH.curie('product_type'),
                   model_uri=CCDH.biologicProduct__product_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.BiologicProduct.productType"]])

slots.biologicProduct__passage_number = Slot(uri=CCDH.passage_number, name="biologicProduct__passage_number", curie=CCDH.curie('passage_number'),
                   model_uri=CCDH.biologicProduct__passage_number, domain=None, range=Optional[Union[Union[int, CcdhInteger], List[Union[int, CcdhInteger]]]])

slots.biologicProduct__growth_rate = Slot(uri=CCDH.growth_rate, name="biologicProduct__growth_rate", curie=CCDH.curie('growth_rate'),
                   model_uri=CCDH.biologicProduct__growth_rate, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.cancerGradeObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerGradeObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerGradeObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.CancerGradeObservation.observationType"])

slots.cancerGradeObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="cancerGradeObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.cancerGradeObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.valueCodeableConcept"]])

slots.cancerGradeObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerGradeObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGradeObservationSet__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"]])

slots.cancerGradeObservationSet__observations = Slot(uri=CCDH.observations, name="cancerGradeObservationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerGradeObservationSet__observations, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.cancerStageObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerStageObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerStageObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.CancerStageObservation.observationType"])

slots.cancerStageObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="cancerStageObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.cancerStageObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservation.valueCodeableConcept"]])

slots.cancerStageObservationSet__category = Slot(uri=CCDH.category, name="cancerStageObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerStageObservationSet__category, domain=None, range=Union[str, "EnumCRDC-H.CancerStageObservationSet.category"])

slots.cancerStageObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerStageObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageObservationSet__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"]])

slots.cancerStageObservationSet__observations = Slot(uri=CCDH.observations, name="cancerStageObservationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerStageObservationSet__observations, domain=None, range=Optional[Union[Union[dict, CancerStageObservation], List[Union[dict, CancerStageObservation]]]])

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

slots.diagnosis__id = Slot(uri=CCDH.id, name="diagnosis__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.diagnosis__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.diagnosis__identifier = Slot(uri=CCDH.identifier, name="diagnosis__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.diagnosis__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.diagnosis__age_at_diagnosis = Slot(uri=CCDH.age_at_diagnosis, name="diagnosis__age_at_diagnosis", curie=CCDH.curie('age_at_diagnosis'),
                   model_uri=CCDH.diagnosis__age_at_diagnosis, domain=None, range=Optional[Union[dict, Quantity]])

slots.diagnosis__year_at_diagnosis = Slot(uri=CCDH.year_at_diagnosis, name="diagnosis__year_at_diagnosis", curie=CCDH.curie('year_at_diagnosis'),
                   model_uri=CCDH.diagnosis__year_at_diagnosis, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.diagnosis__condition = Slot(uri=CCDH.condition, name="diagnosis__condition", curie=CCDH.curie('condition'),
                   model_uri=CCDH.diagnosis__condition, domain=None, range=Optional[Union[str, "EnumCRDC-H.Diagnosis.condition"]])

slots.diagnosis__primary_site = Slot(uri=CCDH.primary_site, name="diagnosis__primary_site", curie=CCDH.curie('primary_site'),
                   model_uri=CCDH.diagnosis__primary_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__metastatic_site = Slot(uri=CCDH.metastatic_site, name="diagnosis__metastatic_site", curie=CCDH.curie('metastatic_site'),
                   model_uri=CCDH.diagnosis__metastatic_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__stage = Slot(uri=CCDH.stage, name="diagnosis__stage", curie=CCDH.curie('stage'),
                   model_uri=CCDH.diagnosis__stage, domain=None, range=Optional[Union[Union[dict, CancerStageObservationSet], List[Union[dict, CancerStageObservationSet]]]])

slots.diagnosis__grade = Slot(uri=CCDH.grade, name="diagnosis__grade", curie=CCDH.curie('grade'),
                   model_uri=CCDH.diagnosis__grade, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.diagnosis__morphology = Slot(uri=CCDH.morphology, name="diagnosis__morphology", curie=CCDH.curie('morphology'),
                   model_uri=CCDH.diagnosis__morphology, domain=None, range=Optional[Union[str, "EnumCRDC-H.Diagnosis.morphology"]])

slots.diagnosis__disease_status = Slot(uri=CCDH.disease_status, name="diagnosis__disease_status", curie=CCDH.curie('disease_status'),
                   model_uri=CCDH.diagnosis__disease_status, domain=None, range=Optional[Union[str, "EnumCRDC-H.Diagnosis.diseaseStatus"]])

slots.diagnosis__prior_diagnosis = Slot(uri=CCDH.prior_diagnosis, name="diagnosis__prior_diagnosis", curie=CCDH.curie('prior_diagnosis'),
                   model_uri=CCDH.diagnosis__prior_diagnosis, domain=None, range=Optional[Union[dict, Diagnosis]])

slots.diagnosis__method_of_diagnosis = Slot(uri=CCDH.method_of_diagnosis, name="diagnosis__method_of_diagnosis", curie=CCDH.curie('method_of_diagnosis'),
                   model_uri=CCDH.diagnosis__method_of_diagnosis, domain=None, range=Optional[Union[str, "EnumCRDC-H.Diagnosis.methodOfDiagnosis"]])

slots.diagnosis__related_specimen = Slot(uri=CCDH.related_specimen, name="diagnosis__related_specimen", curie=CCDH.curie('related_specimen'),
                   model_uri=CCDH.diagnosis__related_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.document__id = Slot(uri=CCDH.id, name="document__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.document__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.document__identifier = Slot(uri=CCDH.identifier, name="document__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.document__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.document__document_type = Slot(uri=CCDH.document_type, name="document__document_type", curie=CCDH.curie('document_type'),
                   model_uri=CCDH.document__document_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Document.documentType"]])

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
                   model_uri=CCDH.exposure__tobacco_use, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.exposure__alcohol_use = Slot(uri=CCDH.alcohol_use, name="exposure__alcohol_use", curie=CCDH.curie('alcohol_use'),
                   model_uri=CCDH.exposure__alcohol_use, domain=None, range=Optional[Union[dict, Entity]])

slots.exposure__environmental = Slot(uri=CCDH.environmental, name="exposure__environmental", curie=CCDH.curie('environmental'),
                   model_uri=CCDH.exposure__environmental, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.exposure__subject = Slot(uri=CCDH.subject, name="exposure__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.exposure__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.identifier__value = Slot(uri=CCDH.value, name="identifier__value", curie=CCDH.curie('value'),
                   model_uri=CCDH.identifier__value, domain=None, range=Union[str, CcdhString])

slots.identifier__system = Slot(uri=CCDH.system, name="identifier__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.identifier__system, domain=None, range=Optional[Union[str, CcdhString]])

slots.identifier__type = Slot(uri=CCDH.type, name="identifier__type", curie=CCDH.curie('type'),
                   model_uri=CCDH.identifier__type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Identifier.type"]])

slots.observation__id = Slot(uri=CCDH.id, name="observation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.observation__id, domain=None, range=Union[str, CcdhString])

slots.observation__category = Slot(uri=CCDH.category, name="observation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.observation__category, domain=None, range=Union[str, "EnumCRDC-H.Observation.category"])

slots.observation__observation_type = Slot(uri=CCDH.observation_type, name="observation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.observation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.Observation.observationType"])

slots.observation__method_type = Slot(uri=CCDH.method_type, name="observation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.observation__method_type, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.Observation.methodType"], List[Union[str, "EnumCRDC-H.Observation.methodType"]]]])

slots.observation__focus = Slot(uri=CCDH.focus, name="observation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.observation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.observation__subject = Slot(uri=CCDH.subject, name="observation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.observation__subject, domain=None, range=Optional[Union[dict, Subject]])

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
                   model_uri=CCDH.observation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.observation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="observation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.observation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.observation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="observation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.observation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.Observation.valueCodeableConcept"]])

slots.organization__id = Slot(uri=CCDH.id, name="organization__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.organization__id, domain=None, range=Union[str, CcdhString])

slots.organization__identifier = Slot(uri=CCDH.identifier, name="organization__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.organization__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.organization__name = Slot(uri=CCDH.name, name="organization__name", curie=CCDH.curie('name'),
                   model_uri=CCDH.organization__name, domain=None, range=Optional[Union[str, CcdhString]])

slots.organization__alias = Slot(uri=CCDH.alias, name="organization__alias", curie=CCDH.curie('alias'),
                   model_uri=CCDH.organization__alias, domain=None, range=Optional[Union[str, CcdhString]])

slots.organization__organization_type = Slot(uri=CCDH.organization_type, name="organization__organization_type", curie=CCDH.curie('organization_type'),
                   model_uri=CCDH.organization__organization_type, domain=None, range=Optional[Union[str, CcdhString]])

slots.quantity__valueDecimal = Slot(uri=CCDH.valueDecimal, name="quantity__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.quantity__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.quantity__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="quantity__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.quantity__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.Quantity.valueCodeableConcept"]])

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
                   model_uri=CCDH.researchProject__primary_anatomic_site, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.ResearchProject.primaryAnatomicSite"], List[Union[str, "EnumCRDC-H.ResearchProject.primaryAnatomicSite"]]]])

slots.researchProject__url = Slot(uri=CCDH.url, name="researchProject__url", curie=CCDH.curie('url'),
                   model_uri=CCDH.researchProject__url, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.researchProject__part_of = Slot(uri=CCDH.part_of, name="researchProject__part_of", curie=CCDH.curie('part_of'),
                   model_uri=CCDH.researchProject__part_of, domain=None, range=Optional[Union[Union[dict, ResearchProject], List[Union[dict, ResearchProject]]]])

slots.researchProject__research_project_type = Slot(uri=CCDH.research_project_type, name="researchProject__research_project_type", curie=CCDH.curie('research_project_type'),
                   model_uri=CCDH.researchProject__research_project_type, domain=None, range=Union[str, "EnumCRDC-H.ResearchProject.researchProjectType"])

slots.researchProject__date_iacuc_approval = Slot(uri=CCDH.date_iacuc_approval, name="researchProject__date_iacuc_approval", curie=CCDH.curie('date_iacuc_approval'),
                   model_uri=CCDH.researchProject__date_iacuc_approval, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.researchSubject__id = Slot(uri=CCDH.id, name="researchSubject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.researchSubject__id, domain=None, range=Union[str, CcdhString])

slots.researchSubject__identifier = Slot(uri=CCDH.identifier, name="researchSubject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.researchSubject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.researchSubject__description = Slot(uri=CCDH.description, name="researchSubject__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.researchSubject__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.researchSubject__member_of_research_project = Slot(uri=CCDH.member_of_research_project, name="researchSubject__member_of_research_project", curie=CCDH.curie('member_of_research_project'),
                   model_uri=CCDH.researchSubject__member_of_research_project, domain=None, range=Optional[Union[dict, ResearchProject]])

slots.researchSubject__age_at_enrollment = Slot(uri=CCDH.age_at_enrollment, name="researchSubject__age_at_enrollment", curie=CCDH.curie('age_at_enrollment'),
                   model_uri=CCDH.researchSubject__age_at_enrollment, domain=None, range=Optional[Union[dict, Quantity]])

slots.researchSubject__primary_diagnosis_condition = Slot(uri=CCDH.primary_diagnosis_condition, name="researchSubject__primary_diagnosis_condition", curie=CCDH.curie('primary_diagnosis_condition'),
                   model_uri=CCDH.researchSubject__primary_diagnosis_condition, domain=None, range=Optional[Union[str, "EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition"]])

slots.researchSubject__primary_diagnosis_site = Slot(uri=CCDH.primary_diagnosis_site, name="researchSubject__primary_diagnosis_site", curie=CCDH.curie('primary_diagnosis_site'),
                   model_uri=CCDH.researchSubject__primary_diagnosis_site, domain=None, range=Optional[Union[str, "EnumCRDC-H.ResearchSubject.primaryDiagnosisSite"]])

slots.researchSubject__primary_diagnosis = Slot(uri=CCDH.primary_diagnosis, name="researchSubject__primary_diagnosis", curie=CCDH.curie('primary_diagnosis'),
                   model_uri=CCDH.researchSubject__primary_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__comorbid_diagnoses = Slot(uri=CCDH.comorbid_diagnoses, name="researchSubject__comorbid_diagnoses", curie=CCDH.curie('comorbid_diagnoses'),
                   model_uri=CCDH.researchSubject__comorbid_diagnoses, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__index_timepoint = Slot(uri=CCDH.index_timepoint, name="researchSubject__index_timepoint", curie=CCDH.curie('index_timepoint'),
                   model_uri=CCDH.researchSubject__index_timepoint, domain=None, range=Optional[Union[str, "EnumCRDC-H.ResearchSubject.indexTimepoint"]])

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
                   model_uri=CCDH.specimen__specimen_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.specimenType"]])

slots.specimen__analyte_type = Slot(uri=CCDH.analyte_type, name="specimen__analyte_type", curie=CCDH.curie('analyte_type'),
                   model_uri=CCDH.specimen__analyte_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.analyteType"]])

slots.specimen__associated_project = Slot(uri=CCDH.associated_project, name="specimen__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH.specimen__associated_project, domain=None, range=Optional[Union[dict, ResearchProject]])

slots.specimen__data_provider = Slot(uri=CCDH.data_provider, name="specimen__data_provider", curie=CCDH.curie('data_provider'),
                   model_uri=CCDH.specimen__data_provider, domain=None, range=Optional[Union[dict, Organization]])

slots.specimen__source_material_type = Slot(uri=CCDH.source_material_type, name="specimen__source_material_type", curie=CCDH.curie('source_material_type'),
                   model_uri=CCDH.specimen__source_material_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.sourceMaterialType"]])

slots.specimen__parent_specimen = Slot(uri=CCDH.parent_specimen, name="specimen__parent_specimen", curie=CCDH.curie('parent_specimen'),
                   model_uri=CCDH.specimen__parent_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.specimen__source_subject = Slot(uri=CCDH.source_subject, name="specimen__source_subject", curie=CCDH.curie('source_subject'),
                   model_uri=CCDH.specimen__source_subject, domain=None, range=Optional[Union[dict, Subject]])

slots.specimen__source_model_system = Slot(uri=CCDH.source_model_system, name="specimen__source_model_system", curie=CCDH.curie('source_model_system'),
                   model_uri=CCDH.specimen__source_model_system, domain=None, range=Optional[Union[dict, Entity]])

slots.specimen__tumor_status_at_collection = Slot(uri=CCDH.tumor_status_at_collection, name="specimen__tumor_status_at_collection", curie=CCDH.curie('tumor_status_at_collection'),
                   model_uri=CCDH.specimen__tumor_status_at_collection, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.tumorStatusAtCollection"]])

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
                   model_uri=CCDH.specimen__quantity_measure, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimen__quality_measure = Slot(uri=CCDH.quality_measure, name="specimen__quality_measure", curie=CCDH.curie('quality_measure'),
                   model_uri=CCDH.specimen__quality_measure, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimen__cellular_composition_type = Slot(uri=CCDH.cellular_composition_type, name="specimen__cellular_composition_type", curie=CCDH.curie('cellular_composition_type'),
                   model_uri=CCDH.specimen__cellular_composition_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.cellularCompositionType"]])

slots.specimen__histological_composition_measure = Slot(uri=CCDH.histological_composition_measure, name="specimen__histological_composition_measure", curie=CCDH.curie('histological_composition_measure'),
                   model_uri=CCDH.specimen__histological_composition_measure, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimen__general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="specimen__general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                   model_uri=CCDH.specimen__general_tissue_morphology, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.generalTissueMorphology"]])

slots.specimen__specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="specimen__specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                   model_uri=CCDH.specimen__specific_tissue_morphology, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.specificTissueMorphology"]])

slots.specimen__preinvasive_tissue_morphology = Slot(uri=CCDH.preinvasive_tissue_morphology, name="specimen__preinvasive_tissue_morphology", curie=CCDH.curie('preinvasive_tissue_morphology'),
                   model_uri=CCDH.specimen__preinvasive_tissue_morphology, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.preinvasiveTissueMorphology"]])

slots.specimen__morphology_pathologically_confirmed = Slot(uri=CCDH.morphology_pathologically_confirmed, name="specimen__morphology_pathologically_confirmed", curie=CCDH.curie('morphology_pathologically_confirmed'),
                   model_uri=CCDH.specimen__morphology_pathologically_confirmed, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.specimen__morphology_assessor_role = Slot(uri=CCDH.morphology_assessor_role, name="specimen__morphology_assessor_role", curie=CCDH.curie('morphology_assessor_role'),
                   model_uri=CCDH.specimen__morphology_assessor_role, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.morphologyAssessorRole"]])

slots.specimen__morphlogy_assessment_method = Slot(uri=CCDH.morphlogy_assessment_method, name="specimen__morphlogy_assessment_method", curie=CCDH.curie('morphlogy_assessment_method'),
                   model_uri=CCDH.specimen__morphlogy_assessment_method, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.morphlogyAssessmentMethod"]])

slots.specimen__degree_of_dysplasia = Slot(uri=CCDH.degree_of_dysplasia, name="specimen__degree_of_dysplasia", curie=CCDH.curie('degree_of_dysplasia'),
                   model_uri=CCDH.specimen__degree_of_dysplasia, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.degreeOfDysplasia"]])

slots.specimen__dysplasia_fraction = Slot(uri=CCDH.dysplasia_fraction, name="specimen__dysplasia_fraction", curie=CCDH.curie('dysplasia_fraction'),
                   model_uri=CCDH.specimen__dysplasia_fraction, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimen__related_document = Slot(uri=CCDH.related_document, name="specimen__related_document", curie=CCDH.curie('related_document'),
                   model_uri=CCDH.specimen__related_document, domain=None, range=Optional[Union[Union[dict, Document], List[Union[dict, Document]]]])

slots.specimen__section_location = Slot(uri=CCDH.section_location, name="specimen__section_location", curie=CCDH.curie('section_location'),
                   model_uri=CCDH.specimen__section_location, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.sectionLocation"]])

slots.specimen__derived_product = Slot(uri=CCDH.derived_product, name="specimen__derived_product", curie=CCDH.curie('derived_product'),
                   model_uri=CCDH.specimen__derived_product, domain=None, range=Optional[Union[Union[dict, BiologicProduct], List[Union[dict, BiologicProduct]]]])

slots.specimen__distance_from_paired_specimen = Slot(uri=CCDH.distance_from_paired_specimen, name="specimen__distance_from_paired_specimen", curie=CCDH.curie('distance_from_paired_specimen'),
                   model_uri=CCDH.specimen__distance_from_paired_specimen, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenContainer__id = Slot(uri=CCDH.id, name="specimenContainer__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenContainer__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__identifier = Slot(uri=CCDH.identifier, name="specimenContainer__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.specimenContainer__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.specimenContainer__container_type = Slot(uri=CCDH.container_type, name="specimenContainer__container_type", curie=CCDH.curie('container_type'),
                   model_uri=CCDH.specimenContainer__container_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenContainer.containerType"]])

slots.specimenContainer__container_number = Slot(uri=CCDH.container_number, name="specimenContainer__container_number", curie=CCDH.curie('container_number'),
                   model_uri=CCDH.specimenContainer__container_number, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__additive = Slot(uri=CCDH.additive, name="specimenContainer__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenContainer__additive, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

slots.specimenContainer__parent_container = Slot(uri=CCDH.parent_container, name="specimenContainer__parent_container", curie=CCDH.curie('parent_container'),
                   model_uri=CCDH.specimenContainer__parent_container, domain=None, range=Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]])

slots.specimenContainer__charge_type = Slot(uri=CCDH.charge_type, name="specimenContainer__charge_type", curie=CCDH.curie('charge_type'),
                   model_uri=CCDH.specimenContainer__charge_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenContainer.chargeType"]])

slots.specimenCreationActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenCreationActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenCreationActivity__activity_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.activityType"]])

slots.specimenCreationActivity__date_started = Slot(uri=CCDH.date_started, name="specimenCreationActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenCreationActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenCreationActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenCreationActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenCreationActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenCreationActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenCreationActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenCreationActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenCreationActivity__collection_method_type = Slot(uri=CCDH.collection_method_type, name="specimenCreationActivity__collection_method_type", curie=CCDH.curie('collection_method_type'),
                   model_uri=CCDH.specimenCreationActivity__collection_method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.collectionMethodType"]])

slots.specimenCreationActivity__derivation_method_type = Slot(uri=CCDH.derivation_method_type, name="specimenCreationActivity__derivation_method_type", curie=CCDH.curie('derivation_method_type'),
                   model_uri=CCDH.specimenCreationActivity__derivation_method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenCreationActivity.derivationMethodType"]])

slots.specimenCreationActivity__additive = Slot(uri=CCDH.additive, name="specimenCreationActivity__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenCreationActivity__additive, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

slots.specimenCreationActivity__collection_site = Slot(uri=CCDH.collection_site, name="specimenCreationActivity__collection_site", curie=CCDH.curie('collection_site'),
                   model_uri=CCDH.specimenCreationActivity__collection_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.specimenCreationActivity__input_specimen = Slot(uri=CCDH.input_specimen, name="specimenCreationActivity__input_specimen", curie=CCDH.curie('input_specimen'),
                   model_uri=CCDH.specimenCreationActivity__input_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.specimenCreationActivity__quantity_collected = Slot(uri=CCDH.quantity_collected, name="specimenCreationActivity__quantity_collected", curie=CCDH.curie('quantity_collected'),
                   model_uri=CCDH.specimenCreationActivity__quantity_collected, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenCreationActivity__execution_observation = Slot(uri=CCDH.execution_observation, name="specimenCreationActivity__execution_observation", curie=CCDH.curie('execution_observation'),
                   model_uri=CCDH.specimenCreationActivity__execution_observation, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimenCreationActivity__specimen_order = Slot(uri=CCDH.specimen_order, name="specimenCreationActivity__specimen_order", curie=CCDH.curie('specimen_order'),
                   model_uri=CCDH.specimenCreationActivity__specimen_order, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenProcessingActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenProcessingActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenProcessingActivity__activity_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenProcessingActivity.activityType"]])

slots.specimenProcessingActivity__date_started = Slot(uri=CCDH.date_started, name="specimenProcessingActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenProcessingActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenProcessingActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenProcessingActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenProcessingActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenProcessingActivity__duration = Slot(uri=CCDH.duration, name="specimenProcessingActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH.specimenProcessingActivity__duration, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenProcessingActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenProcessingActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenProcessingActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenProcessingActivity__method_type = Slot(uri=CCDH.method_type, name="specimenProcessingActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenProcessingActivity__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenProcessingActivity.methodType"]])

slots.specimenProcessingActivity__additive = Slot(uri=CCDH.additive, name="specimenProcessingActivity__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenProcessingActivity__additive, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

slots.specimenProcessingActivity__execution_observation = Slot(uri=CCDH.execution_observation, name="specimenProcessingActivity__execution_observation", curie=CCDH.curie('execution_observation'),
                   model_uri=CCDH.specimenProcessingActivity__execution_observation, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenStorageActivity__date_started = Slot(uri=CCDH.date_started, name="specimenStorageActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenStorageActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenStorageActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenStorageActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenStorageActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenStorageActivity__duration = Slot(uri=CCDH.duration, name="specimenStorageActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH.specimenStorageActivity__duration, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenStorageActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenStorageActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenStorageActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenStorageActivity__method_type = Slot(uri=CCDH.method_type, name="specimenStorageActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenStorageActivity__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenStorageActivity.methodType"]])

slots.specimenStorageActivity__container = Slot(uri=CCDH.container, name="specimenStorageActivity__container", curie=CCDH.curie('container'),
                   model_uri=CCDH.specimenStorageActivity__container, domain=None, range=Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]])

slots.specimenTransportActivity__date_started = Slot(uri=CCDH.date_started, name="specimenTransportActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenTransportActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenTransportActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenTransportActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenTransportActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenTransportActivity__duration = Slot(uri=CCDH.duration, name="specimenTransportActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH.specimenTransportActivity__duration, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.specimenTransportActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenTransportActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenTransportActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenTransportActivity__transport_origin = Slot(uri=CCDH.transport_origin, name="specimenTransportActivity__transport_origin", curie=CCDH.curie('transport_origin'),
                   model_uri=CCDH.specimenTransportActivity__transport_origin, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenTransportActivity__transport_destination = Slot(uri=CCDH.transport_destination, name="specimenTransportActivity__transport_destination", curie=CCDH.curie('transport_destination'),
                   model_uri=CCDH.specimenTransportActivity__transport_destination, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenTransportActivity__execution_observation = Slot(uri=CCDH.execution_observation, name="specimenTransportActivity__execution_observation", curie=CCDH.curie('execution_observation'),
                   model_uri=CCDH.specimenTransportActivity__execution_observation, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenTransportActivity__execution_conditions = Slot(uri=CCDH.execution_conditions, name="specimenTransportActivity__execution_conditions", curie=CCDH.curie('execution_conditions'),
                   model_uri=CCDH.specimenTransportActivity__execution_conditions, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.subject__id = Slot(uri=CCDH.id, name="subject__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.subject__id, domain=None, range=Union[str, CcdhString])

slots.subject__identifier = Slot(uri=CCDH.identifier, name="subject__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.subject__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.subject__species = Slot(uri=CCDH.species, name="subject__species", curie=CCDH.curie('species'),
                   model_uri=CCDH.subject__species, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.species"]])

slots.subject__breed = Slot(uri=CCDH.breed, name="subject__breed", curie=CCDH.curie('breed'),
                   model_uri=CCDH.subject__breed, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.breed"]])

slots.subject__sex = Slot(uri=CCDH.sex, name="subject__sex", curie=CCDH.curie('sex'),
                   model_uri=CCDH.subject__sex, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.sex"]])

slots.subject__ethnicity = Slot(uri=CCDH.ethnicity, name="subject__ethnicity", curie=CCDH.curie('ethnicity'),
                   model_uri=CCDH.subject__ethnicity, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.ethnicity"]])

slots.subject__race = Slot(uri=CCDH.race, name="subject__race", curie=CCDH.curie('race'),
                   model_uri=CCDH.subject__race, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.Subject.race"], List[Union[str, "EnumCRDC-H.Subject.race"]]]])

slots.subject__year_of_birth = Slot(uri=CCDH.year_of_birth, name="subject__year_of_birth", curie=CCDH.curie('year_of_birth'),
                   model_uri=CCDH.subject__year_of_birth, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__vital_status = Slot(uri=CCDH.vital_status, name="subject__vital_status", curie=CCDH.curie('vital_status'),
                   model_uri=CCDH.subject__vital_status, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.vitalStatus"]])

slots.subject__age_at_death = Slot(uri=CCDH.age_at_death, name="subject__age_at_death", curie=CCDH.curie('age_at_death'),
                   model_uri=CCDH.subject__age_at_death, domain=None, range=Optional[Union[dict, Quantity]])

slots.subject__year_of_death = Slot(uri=CCDH.year_of_death, name="subject__year_of_death", curie=CCDH.curie('year_of_death'),
                   model_uri=CCDH.subject__year_of_death, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__cause_of_death = Slot(uri=CCDH.cause_of_death, name="subject__cause_of_death", curie=CCDH.curie('cause_of_death'),
                   model_uri=CCDH.subject__cause_of_death, domain=None, range=Optional[Union[str, "EnumCRDC-H.Subject.causeOfDeath"]])

slots.substance__substance_type = Slot(uri=CCDH.substance_type, name="substance__substance_type", curie=CCDH.curie('substance_type'),
                   model_uri=CCDH.substance__substance_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Substance.substanceType"]])

slots.substance__role = Slot(uri=CCDH.role, name="substance__role", curie=CCDH.curie('role'),
                   model_uri=CCDH.substance__role, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.Substance.role"], List[Union[str, "EnumCRDC-H.Substance.role"]]]])

slots.timePoint__dateTime = Slot(uri=CCDH.dateTime, name="timePoint__dateTime", curie=CCDH.curie('dateTime'),
                   model_uri=CCDH.timePoint__dateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__indexDate = Slot(uri=CCDH.indexDate, name="timePoint__indexDate", curie=CCDH.curie('indexDate'),
                   model_uri=CCDH.timePoint__indexDate, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__indexEventType = Slot(uri=CCDH.indexEventType, name="timePoint__indexEventType", curie=CCDH.curie('indexEventType'),
                   model_uri=CCDH.timePoint__indexEventType, domain=None, range=Optional[Union[str, "EnumCRDC-H.TimePoint.indexEventType"]])

slots.timePoint__offsetFromIndex = Slot(uri=CCDH.offsetFromIndex, name="timePoint__offsetFromIndex", curie=CCDH.curie('offsetFromIndex'),
                   model_uri=CCDH.timePoint__offsetFromIndex, domain=None, range=Optional[Union[dict, Quantity]])

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
                   model_uri=CCDH.treatment__type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Treatment.type"]])

slots.treatment__therapeutic_agent = Slot(uri=CCDH.therapeutic_agent, name="treatment__therapeutic_agent", curie=CCDH.curie('therapeutic_agent'),
                   model_uri=CCDH.treatment__therapeutic_agent, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

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
