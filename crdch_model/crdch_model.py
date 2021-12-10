# Auto generated from crdch_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-18 01:06
# Schema: CRDC-H
#
# id: https://example.org/crdch
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GDC = CurieNamespace('GDC', 'http://example.org/gdc/')
HTAN = CurieNamespace('HTAN', 'http://example.org/htan/')
ICDC = CurieNamespace('ICDC', 'http://example.org/icdc/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PDC = CurieNamespace('PDC', 'http://example.org/pdc/')
CRDCH = CurieNamespace('crdch', 'https://example.org/crdch/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CRDCH


# Types
class CrdchString(String):
    """ A sequence of Unicode characters.  There are no limits on the number of characters in the string. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "crdch_string"
    type_model_uri = CRDCH.CrdchString


class CrdchInteger(Integer):
    """ An integer number.  This data type is based on the decimal type, but the fractional component is not allowed.  There are no restrictions on the size of the integer. """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "crdch_integer"
    type_model_uri = CRDCH.CrdchInteger


class CrdchDecimal(Decimal):
    """ A rational number that has a decimal representation.  This data type does not restrict the size or precision of the number. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "crdch_decimal"
    type_model_uri = CRDCH.CrdchDecimal


class CrdchBoolean(Boolean):
    """ Value representing either “true” or “false”.  Permissible values (case-sensitive) = “true”, “false”, “1”, “0”. """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "crdch_boolean"
    type_model_uri = CRDCH.CrdchBoolean


class CrdchDateTime(Datetime):
    """ A date and time string specified using a specialized concatenation of the date and time data types, in the general format YYYY-MM-DDThh:mm:ss+zz:zz. """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "crdch_dateTime"
    type_model_uri = CRDCH.CrdchDateTime


class CrdchCurie(Uriorcurie):
    """ A compact URI (CURIE), which is a bipartite identifier of the form prefix:reference, in which the prefix is a convenient abbreviation of a URI.  It is expressed in the format “prefix:reference”. When a mapping of prefix to base URI is provided (external to this data type), a CURIE may be mapped to a URI. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "crdch_curie"
    type_model_uri = CRDCH.CrdchCurie


class CrdchCode(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "crdch_code"
    type_model_uri = CRDCH.CrdchCode


# Class references



class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Entity
    class_class_curie: ClassVar[str] = "crdch:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CRDCH.Entity


@dataclass
class AlcoholExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to alcohol, as generated
    through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.AlcoholExposureObservation
    class_class_curie: ClassVar[str] = "crdch:AlcoholExposureObservation"
    class_name: ClassVar[str] = "AlcoholExposureObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.AlcoholExposureObservation

    observation_type: Union[dict, "CodeableConcept"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, "CodeableConcept"]] = None
    method_type: Optional[Union[dict, "CodeableConcept"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    value_integer: Optional[Union[int, CrdchInteger]] = None
    value_codeable_concept: Optional[Union[dict, "CodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.value_integer is not None and not isinstance(self.value_integer, CrdchInteger):
            self.value_integer = CrdchInteger(self.value_integer)

        if self.value_codeable_concept is not None and not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        super().__post_init__(**kwargs)


@dataclass
class BodySite(Entity):
    """
    A site in the body of an organism, typically described in terms of an anatomical concept and optional qualifiers
    (e.g. left/right, upper/lower). But body sites as defined here may include non-canonical sites, such as an
    implanted medical device.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.BodySite
    class_class_curie: ClassVar[str] = "crdch:BodySite"
    class_name: ClassVar[str] = "BodySite"
    class_model_uri: ClassVar[URIRef] = CRDCH.BodySite

    site: Union[dict, "CodeableConcept"] = None
    qualifier: Optional[Union[Union[dict, "CodeableConcept"], List[Union[dict, "CodeableConcept"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, CodeableConcept):
            self.site = CodeableConcept(**as_dict(self.site))

        if not isinstance(self.qualifier, list):
            self.qualifier = [self.qualifier] if self.qualifier is not None else []
        self.qualifier = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.qualifier]

        super().__post_init__(**kwargs)


@dataclass
class BiologicProduct(Entity):
    """
    A living organism, or a metabolically active biological system such as a cell culture, tissue culture, or organoid
    that is maintained or propagated in vitro.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.BiologicProduct
    class_class_curie: ClassVar[str] = "crdch:BiologicProduct"
    class_name: ClassVar[str] = "BiologicProduct"
    class_model_uri: ClassVar[URIRef] = CRDCH.BiologicProduct

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    description: Optional[Union[str, CrdchString]] = None
    product_type: Optional[Union[dict, "CodeableConcept"]] = None
    passage_number: Optional[Union[Union[int, CrdchInteger], List[Union[int, CrdchInteger]]]] = empty_list()
    growth_rate: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, CrdchString):
            self.description = CrdchString(self.description)

        if self.product_type is not None and not isinstance(self.product_type, CodeableConcept):
            self.product_type = CodeableConcept(**as_dict(self.product_type))

        if not isinstance(self.passage_number, list):
            self.passage_number = [self.passage_number] if self.passage_number is not None else []
        self.passage_number = [v if isinstance(v, CrdchInteger) else CrdchInteger(v) for v in self.passage_number]

        if not isinstance(self.growth_rate, list):
            self.growth_rate = [self.growth_rate] if self.growth_rate is not None else []
        self.growth_rate = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.growth_rate]

        super().__post_init__(**kwargs)


@dataclass
class CancerGradeObservation(Entity):
    """
    A data structure with key (observation_type) and value (value_codeable_concept) attributes that represents a
    single cancer grade observation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.CancerGradeObservation
    class_class_curie: ClassVar[str] = "crdch:CancerGradeObservation"
    class_name: ClassVar[str] = "CancerGradeObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.CancerGradeObservation

    observation_type: Union[dict, "CodeableConcept"] = None
    value_codeable_concept: Union[dict, "CodeableConcept"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, "CodeableConcept"]] = None
    method_type: Optional[Union[dict, "CodeableConcept"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_codeable_concept):
            self.MissingRequiredField("value_codeable_concept")
        if not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class CancerGradeObservationSet(Entity):
    """
    A structured object to hold related data items about the grade of cancer (e.g. overall, primary gleason, secondary
    gleason, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.CancerGradeObservationSet
    class_class_curie: ClassVar[str] = "crdch:CancerGradeObservationSet"
    class_name: ClassVar[str] = "CancerGradeObservationSet"
    class_model_uri: ClassVar[URIRef] = CRDCH.CancerGradeObservationSet

    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, "CodeableConcept"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[dict, "CodeableConcept"], List[Union[dict, "CodeableConcept"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerGradeObservation], List[Union[dict, CancerGradeObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=CancerGradeObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class CancerStageObservation(Entity):
    """
    A data structure with key (observation_type) and value (value_codeable_concept) attributes that represents a
    single cancer staging observation, such as the Clinical Metastasis (M) component of a clinical TNM staging.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.CancerStageObservation
    class_class_curie: ClassVar[str] = "crdch:CancerStageObservation"
    class_name: ClassVar[str] = "CancerStageObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.CancerStageObservation

    observation_type: Union[dict, "CodeableConcept"] = None
    value_codeable_concept: Union[dict, "CodeableConcept"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, "CodeableConcept"]] = None
    method_type: Optional[Union[dict, "CodeableConcept"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_codeable_concept):
            self.MissingRequiredField("value_codeable_concept")
        if not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class CancerStageObservationSet(Entity):
    """
    A structured object to hold related data items about the staging of cancer (e.g. overall, T, N, and M components
    of a Cancer Staging observation).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.CancerStageObservationSet
    class_class_curie: ClassVar[str] = "crdch:CancerStageObservationSet"
    class_name: ClassVar[str] = "CancerStageObservationSet"
    class_model_uri: ClassVar[URIRef] = CRDCH.CancerStageObservationSet

    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, "CodeableConcept"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[dict, "CodeableConcept"], List[Union[dict, "CodeableConcept"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerStageObservation], List[Union[dict, CancerStageObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=CancerStageObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class CodeableConcept(Entity):
    """
    A representation of a concept that may be defined by or mapped to one or more codes in code systems
    (terminologies, ontologies, dictionaries, code sets, etc) - but may also be defined by the provision of text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.CodeableConcept
    class_class_curie: ClassVar[str] = "crdch:CodeableConcept"
    class_name: ClassVar[str] = "CodeableConcept"
    class_model_uri: ClassVar[URIRef] = CRDCH.CodeableConcept

    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    text: Optional[Union[str, CrdchString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="coding", slot_type=Coding, key_name="code", keyed=False)

        if self.text is not None and not isinstance(self.text, CrdchString):
            self.text = CrdchString(self.text)

        super().__post_init__(**kwargs)


@dataclass
class Coding(Entity):
    """
    A structured representation of a coded/enumerated data value, that includes additional metadata about the code and
    code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Coding
    class_class_curie: ClassVar[str] = "crdch:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = CRDCH.Coding

    code: Union[str, CrdchString] = None
    system: Union[str, CrdchString] = None
    label: Optional[Union[str, CrdchString]] = None
    system_version: Optional[Union[str, CrdchString]] = None
    value_set: Optional[Union[str, CrdchString]] = None
    value_set_version: Optional[Union[str, CrdchString]] = None
    tag: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, CrdchString):
            self.code = CrdchString(self.code)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, CrdchString):
            self.system = CrdchString(self.system)

        if self.label is not None and not isinstance(self.label, CrdchString):
            self.label = CrdchString(self.label)

        if self.system_version is not None and not isinstance(self.system_version, CrdchString):
            self.system_version = CrdchString(self.system_version)

        if self.value_set is not None and not isinstance(self.value_set, CrdchString):
            self.value_set = CrdchString(self.value_set)

        if self.value_set_version is not None and not isinstance(self.value_set_version, CrdchString):
            self.value_set_version = CrdchString(self.value_set_version)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Diagnosis(Entity):
    """
    A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time.
    May be used to capture information about neoplastic and non-neoplastic conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Diagnosis
    class_class_curie: ClassVar[str] = "crdch:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = CRDCH.Diagnosis

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    age_at_diagnosis: Optional[Union[dict, "Quantity"]] = None
    diagnosis_date: Optional[Union[dict, "TimePoint"]] = None
    condition: Optional[Union[dict, CodeableConcept]] = None
    primary_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    metastatic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    stage: Optional[Union[Union[dict, CancerStageObservationSet], List[Union[dict, CancerStageObservationSet]]]] = empty_list()
    grade: Optional[Union[Union[dict, CancerGradeObservationSet], List[Union[dict, CancerGradeObservationSet]]]] = empty_list()
    morphology: Optional[Union[dict, CodeableConcept]] = None
    disease_status: Optional[Union[dict, CodeableConcept]] = None
    prior_diagnosis: Optional[Union[dict, "Diagnosis"]] = None
    method_of_diagnosis: Optional[Union[dict, CodeableConcept]] = None
    related_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    primary_tumor_dimensional_measures: Optional[Union[dict, "DimensionalObservationSet"]] = None
    supporting_observation: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.age_at_diagnosis is not None and not isinstance(self.age_at_diagnosis, Quantity):
            self.age_at_diagnosis = Quantity(**as_dict(self.age_at_diagnosis))

        if self.diagnosis_date is not None and not isinstance(self.diagnosis_date, TimePoint):
            self.diagnosis_date = TimePoint(**as_dict(self.diagnosis_date))

        if self.condition is not None and not isinstance(self.condition, CodeableConcept):
            self.condition = CodeableConcept(**as_dict(self.condition))

        self._normalize_inlined_as_list(slot_name="primary_site", slot_type=BodySite, key_name="site", keyed=False)

        self._normalize_inlined_as_list(slot_name="metastatic_site", slot_type=BodySite, key_name="site", keyed=False)

        if not isinstance(self.stage, list):
            self.stage = [self.stage] if self.stage is not None else []
        self.stage = [v if isinstance(v, CancerStageObservationSet) else CancerStageObservationSet(**as_dict(v)) for v in self.stage]

        if not isinstance(self.grade, list):
            self.grade = [self.grade] if self.grade is not None else []
        self.grade = [v if isinstance(v, CancerGradeObservationSet) else CancerGradeObservationSet(**as_dict(v)) for v in self.grade]

        if self.morphology is not None and not isinstance(self.morphology, CodeableConcept):
            self.morphology = CodeableConcept(**as_dict(self.morphology))

        if self.disease_status is not None and not isinstance(self.disease_status, CodeableConcept):
            self.disease_status = CodeableConcept(**as_dict(self.disease_status))

        if self.prior_diagnosis is not None and not isinstance(self.prior_diagnosis, Diagnosis):
            self.prior_diagnosis = Diagnosis(**as_dict(self.prior_diagnosis))

        if self.method_of_diagnosis is not None and not isinstance(self.method_of_diagnosis, CodeableConcept):
            self.method_of_diagnosis = CodeableConcept(**as_dict(self.method_of_diagnosis))

        if not isinstance(self.related_specimen, list):
            self.related_specimen = [self.related_specimen] if self.related_specimen is not None else []
        self.related_specimen = [v if isinstance(v, Specimen) else Specimen(**as_dict(v)) for v in self.related_specimen]

        if self.primary_tumor_dimensional_measures is not None and not isinstance(self.primary_tumor_dimensional_measures, DimensionalObservationSet):
            self.primary_tumor_dimensional_measures = DimensionalObservationSet(**as_dict(self.primary_tumor_dimensional_measures))

        self._normalize_inlined_as_list(slot_name="supporting_observation", slot_type=Observation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DimensionalObservation(Entity):
    """
    A structured object that describes a single data item about the physical dimensions of an entity (e.g. length
    width, area), as generated through a point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.DimensionalObservation
    class_class_curie: ClassVar[str] = "crdch:DimensionalObservation"
    class_name: ClassVar[str] = "DimensionalObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.DimensionalObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_quantity: Union[dict, "Quantity"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_quantity):
            self.MissingRequiredField("value_quantity")
        if not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class DimensionalObservationSet(Entity):
    """
    A set of one or more discrete observations about the physical dimensions of an object (e.g. length, width, area).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.DimensionalObservationSet
    class_class_curie: ClassVar[str] = "crdch:DimensionalObservationSet"
    class_name: ClassVar[str] = "DimensionalObservationSet"
    class_model_uri: ClassVar[URIRef] = CRDCH.DimensionalObservationSet

    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, DimensionalObservation], List[Union[dict, DimensionalObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=DimensionalObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Document(Entity):
    """
    A collection of information intented to be understood together as a whole, and codified in human-readable form.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Document
    class_class_curie: ClassVar[str] = "crdch:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = CRDCH.Document

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    document_type: Optional[Union[dict, CodeableConcept]] = None
    description: Optional[Union[str, CrdchString]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    url: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.document_type is not None and not isinstance(self.document_type, CodeableConcept):
            self.document_type = CodeableConcept(**as_dict(self.document_type))

        if self.description is not None and not isinstance(self.description, CrdchString):
            self.description = CrdchString(self.description)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if not isinstance(self.url, list):
            self.url = [self.url] if self.url is not None else []
        self.url = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.url]

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to an environmental factor,
    as generated through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.EnvironmentalExposureObservation
    class_class_curie: ClassVar[str] = "crdch:EnvironmentalExposureObservation"
    class_name: ClassVar[str] = "EnvironmentalExposureObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.EnvironmentalExposureObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_codeable_concept: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_codeable_concept):
            self.MissingRequiredField("value_codeable_concept")
        if not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class ExecutionConditionObservation(Entity):
    """
    A structured object that describes how long certain parts on an activity took to complete, as determined through a
    point-in-time observation or measurement.

    Information describing the environmental conditions in which an activity, or a specific part of an activity, was
    performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.ExecutionConditionObservation
    class_class_curie: ClassVar[str] = "crdch:ExecutionConditionObservation"
    class_name: ClassVar[str] = "ExecutionConditionObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.ExecutionConditionObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_codeable_concept: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_codeable_concept):
            self.MissingRequiredField("value_codeable_concept")
        if not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class ExecutionTimeObservation(Entity):
    """
    A structured object that describes how long certain parts on an activity took to complete, as determined through a
    point-in-time observation or measurement.

    Information describing the environmental conditions in which an activity, or a specific part of an activity, was
    performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.ExecutionTimeObservation
    class_class_curie: ClassVar[str] = "crdch:ExecutionTimeObservation"
    class_name: ClassVar[str] = "ExecutionTimeObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.ExecutionTimeObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_quantity: Union[dict, "Quantity"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_quantity):
            self.MissingRequiredField("value_quantity")
        if not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class Exposure(Entity):
    """
    Contact between an agent and a target. A state of contact or close proximity to a medicinal product, chemical,
    pathogen, radioisotope or other substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Exposure
    class_class_curie: ClassVar[str] = "crdch:Exposure"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = CRDCH.Exposure

    id: Union[str, CrdchString] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    tobacco_exposure: Optional[Union[Union[dict, "TobaccoExposureObservation"], List[Union[dict, "TobaccoExposureObservation"]]]] = empty_list()
    alcohol_exposure: Optional[Union[Union[dict, AlcoholExposureObservation], List[Union[dict, AlcoholExposureObservation]]]] = empty_list()
    environmental_exposure: Optional[Union[Union[dict, EnvironmentalExposureObservation], List[Union[dict, EnvironmentalExposureObservation]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="tobacco_exposure", slot_type=TobaccoExposureObservation, key_name="observation_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="alcohol_exposure", slot_type=AlcoholExposureObservation, key_name="observation_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="environmental_exposure", slot_type=EnvironmentalExposureObservation, key_name="observation_type", keyed=False)

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class HistologicalCompositionObservation(Entity):
    """
    An observation about characteristics of a specimen at a microscopic level - typically related to its cellular or
    tissue composition. (e.g. how many cells in the specimen are of a given type, or exhibit a particular cellular
    phenotype).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.HistologicalCompositionObservation
    class_class_curie: ClassVar[str] = "crdch:HistologicalCompositionObservation"
    class_name: ClassVar[str] = "HistologicalCompositionObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.HistologicalCompositionObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_quantity: Union[dict, "Quantity"] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_quantity):
            self.MissingRequiredField("value_quantity")
        if not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class HistologicalCompositionObservationSet(Entity):
    """
    A set of one or more discrete observations that quantify the relative or absolute composition of a specimen at
    cellular level - e.g. how many cells in the specimen are of a given type, or exhibit a particular cellular
    phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.HistologicalCompositionObservationSet
    class_class_curie: ClassVar[str] = "crdch:HistologicalCompositionObservationSet"
    class_name: ClassVar[str] = "HistologicalCompositionObservationSet"
    class_model_uri: ClassVar[URIRef] = CRDCH.HistologicalCompositionObservationSet

    id: Union[str, CrdchString] = None
    category: Union[dict, CodeableConcept] = None
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, HistologicalCompositionObservation], List[Union[dict, HistologicalCompositionObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=HistologicalCompositionObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(Entity):
    """
    An Identifier is associated with a unique object or entity within a given system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Identifier
    class_class_curie: ClassVar[str] = "crdch:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CRDCH.Identifier

    value: Union[str, CrdchString] = None
    system: Optional[Union[str, CrdchString]] = None
    type: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CrdchString):
            self.value = CrdchString(self.value)

        if self.system is not None and not isinstance(self.system, CrdchString):
            self.system = CrdchString(self.system)

        if self.type is not None and not isinstance(self.type, CodeableConcept):
            self.type = CodeableConcept(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass
class Observation(Entity):
    """
    A structured object that describes a single data item about an entity, as generated through a point-in-time
    observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Observation
    class_class_curie: ClassVar[str] = "crdch:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = CRDCH.Observation

    observation_type: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    value_entity: Optional[Union[dict, Entity]] = None
    value_string: Optional[Union[str, CrdchString]] = None
    value_integer: Optional[Union[Decimal, CrdchDecimal]] = None
    value_decimal: Optional[Union[Decimal, CrdchDecimal]] = None
    value_boolean: Optional[Union[bool, CrdchBoolean]] = None
    value_date_time: Optional[Union[str, CrdchDateTime]] = None
    value_quantity: Optional[Union[dict, "Quantity"]] = None
    value_codeable_concept: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.value_entity is not None and not isinstance(self.value_entity, Entity):
            self.value_entity = Entity()

        if self.value_string is not None and not isinstance(self.value_string, CrdchString):
            self.value_string = CrdchString(self.value_string)

        if self.value_integer is not None and not isinstance(self.value_integer, CrdchDecimal):
            self.value_integer = CrdchDecimal(self.value_integer)

        if self.value_decimal is not None and not isinstance(self.value_decimal, CrdchDecimal):
            self.value_decimal = CrdchDecimal(self.value_decimal)

        if self.value_boolean is not None and not isinstance(self.value_boolean, CrdchBoolean):
            self.value_boolean = CrdchBoolean(self.value_boolean)

        if self.value_date_time is not None and not isinstance(self.value_date_time, CrdchDateTime):
            self.value_date_time = CrdchDateTime(self.value_date_time)

        if self.value_quantity is not None and not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.value_codeable_concept is not None and not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        super().__post_init__(**kwargs)


@dataclass
class ObservationSet(Entity):
    """
    A structured object to hold related data items about an entity, as generated through a point-in-time observation,
    measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.ObservationSet
    class_class_curie: ClassVar[str] = "crdch:ObservationSet"
    class_name: ClassVar[str] = "ObservationSet"
    class_model_uri: ClassVar[URIRef] = CRDCH.ObservationSet

    id: Union[str, CrdchString] = None
    category: Union[dict, CodeableConcept] = None
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Organization(Entity):
    """
    A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or
    an institute within a university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Organization
    class_class_curie: ClassVar[str] = "crdch:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = CRDCH.Organization

    id: Union[str, CrdchString] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CrdchString]] = None
    alias: Optional[Union[str, CrdchString]] = None
    organization_type: Optional[Union[str, CrdchString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.name is not None and not isinstance(self.name, CrdchString):
            self.name = CrdchString(self.name)

        if self.alias is not None and not isinstance(self.alias, CrdchString):
            self.alias = CrdchString(self.alias)

        if self.organization_type is not None and not isinstance(self.organization_type, CrdchString):
            self.organization_type = CrdchString(self.organization_type)

        super().__post_init__(**kwargs)


@dataclass
class Quantity(Entity):
    """
    A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including
    a value and unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Quantity
    class_class_curie: ClassVar[str] = "crdch:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = CRDCH.Quantity

    value_decimal: Optional[Union[Decimal, CrdchDecimal]] = None
    value_codeable_concept: Optional[Union[dict, CodeableConcept]] = None
    unit: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value_decimal is not None and not isinstance(self.value_decimal, CrdchDecimal):
            self.value_decimal = CrdchDecimal(self.value_decimal)

        if self.value_codeable_concept is not None and not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        if self.unit is not None and not isinstance(self.unit, CodeableConcept):
            self.unit = CodeableConcept(**as_dict(self.unit))

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

    class_class_uri: ClassVar[URIRef] = CRDCH.ResearchProject
    class_class_curie: ClassVar[str] = "crdch:ResearchProject"
    class_name: ClassVar[str] = "ResearchProject"
    class_model_uri: ClassVar[URIRef] = CRDCH.ResearchProject

    research_project_type: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CrdchString]] = None
    name_shortened: Optional[Union[str, CrdchString]] = None
    description: Optional[Union[str, CrdchString]] = None
    description_shortened: Optional[Union[str, CrdchString]] = None
    sponsor: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    primary_anatomic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    url: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ResearchProject"], List[Union[dict, "ResearchProject"]]]] = empty_list()
    associated_timepoint: Optional[Union[Union[dict, "TimePoint"], List[Union[dict, "TimePoint"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.research_project_type):
            self.MissingRequiredField("research_project_type")
        if not isinstance(self.research_project_type, CodeableConcept):
            self.research_project_type = CodeableConcept(**as_dict(self.research_project_type))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.name is not None and not isinstance(self.name, CrdchString):
            self.name = CrdchString(self.name)

        if self.name_shortened is not None and not isinstance(self.name_shortened, CrdchString):
            self.name_shortened = CrdchString(self.name_shortened)

        if self.description is not None and not isinstance(self.description, CrdchString):
            self.description = CrdchString(self.description)

        if self.description_shortened is not None and not isinstance(self.description_shortened, CrdchString):
            self.description_shortened = CrdchString(self.description_shortened)

        if not isinstance(self.sponsor, list):
            self.sponsor = [self.sponsor] if self.sponsor is not None else []
        self.sponsor = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.sponsor]

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        self._normalize_inlined_as_list(slot_name="primary_anatomic_site", slot_type=BodySite, key_name="site", keyed=False)

        if not isinstance(self.url, list):
            self.url = [self.url] if self.url is not None else []
        self.url = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.url]

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=ResearchProject, key_name="research_project_type", keyed=False)

        if not isinstance(self.associated_timepoint, list):
            self.associated_timepoint = [self.associated_timepoint] if self.associated_timepoint is not None else []
        self.associated_timepoint = [v if isinstance(v, TimePoint) else TimePoint(**as_dict(v)) for v in self.associated_timepoint]

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

    class_class_uri: ClassVar[URIRef] = CRDCH.ResearchSubject
    class_class_curie: ClassVar[str] = "crdch:ResearchSubject"
    class_name: ClassVar[str] = "ResearchSubject"
    class_model_uri: ClassVar[URIRef] = CRDCH.ResearchSubject

    id: Union[str, CrdchString] = None
    associated_subject: Union[dict, "Subject"] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    description: Optional[Union[str, CrdchString]] = None
    member_of_research_project: Optional[Union[dict, ResearchProject]] = None
    age_at_enrollment: Optional[Union[dict, Quantity]] = None
    primary_diagnosis_condition: Optional[Union[dict, CodeableConcept]] = None
    primary_diagnosis_site: Optional[Union[dict, BodySite]] = None
    primary_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    comorbid_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    index_timepoint: Optional[Union[dict, CodeableConcept]] = None
    originating_site: Optional[Union[dict, Organization]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self._is_empty(self.associated_subject):
            self.MissingRequiredField("associated_subject")
        if not isinstance(self.associated_subject, Subject):
            self.associated_subject = Subject(**as_dict(self.associated_subject))

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, CrdchString):
            self.description = CrdchString(self.description)

        if self.member_of_research_project is not None and not isinstance(self.member_of_research_project, ResearchProject):
            self.member_of_research_project = ResearchProject(**as_dict(self.member_of_research_project))

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, Quantity):
            self.age_at_enrollment = Quantity(**as_dict(self.age_at_enrollment))

        if self.primary_diagnosis_condition is not None and not isinstance(self.primary_diagnosis_condition, CodeableConcept):
            self.primary_diagnosis_condition = CodeableConcept(**as_dict(self.primary_diagnosis_condition))

        if self.primary_diagnosis_site is not None and not isinstance(self.primary_diagnosis_site, BodySite):
            self.primary_diagnosis_site = BodySite(**as_dict(self.primary_diagnosis_site))

        if not isinstance(self.primary_diagnosis, list):
            self.primary_diagnosis = [self.primary_diagnosis] if self.primary_diagnosis is not None else []
        self.primary_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**as_dict(v)) for v in self.primary_diagnosis]

        if not isinstance(self.comorbid_diagnosis, list):
            self.comorbid_diagnosis = [self.comorbid_diagnosis] if self.comorbid_diagnosis is not None else []
        self.comorbid_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**as_dict(v)) for v in self.comorbid_diagnosis]

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, CodeableConcept):
            self.index_timepoint = CodeableConcept(**as_dict(self.index_timepoint))

        if self.originating_site is not None and not isinstance(self.originating_site, Organization):
            self.originating_site = Organization(**as_dict(self.originating_site))

        super().__post_init__(**kwargs)


@dataclass
class Specimen(Entity):
    """
    Any material taken as a sample from a biological entity (living or dead), or from a physical object or the
    environment. Specimens are usually collected as an example of their kind, often for use in some investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Specimen
    class_class_curie: ClassVar[str] = "crdch:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CRDCH.Specimen

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    description: Optional[Union[str, CrdchString]] = None
    specimen_type: Optional[Union[dict, CodeableConcept]] = None
    analyte_type: Optional[Union[dict, CodeableConcept]] = None
    associated_project: Optional[Union[dict, ResearchProject]] = None
    data_provider: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[dict, CodeableConcept]] = None
    parent_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    source_subject: Optional[Union[dict, "Subject"]] = None
    tumor_status_at_collection: Optional[Union[dict, CodeableConcept]] = None
    creation_activity: Optional[Union[dict, "SpecimenCreationActivity"]] = None
    processing_activity: Optional[Union[Union[dict, "SpecimenProcessingActivity"], List[Union[dict, "SpecimenProcessingActivity"]]]] = empty_list()
    storage_activity: Optional[Union[Union[dict, "SpecimenStorageActivity"], List[Union[dict, "SpecimenStorageActivity"]]]] = empty_list()
    transport_activity: Optional[Union[Union[dict, "SpecimenTransportActivity"], List[Union[dict, "SpecimenTransportActivity"]]]] = empty_list()
    contained_in: Optional[Union[dict, "SpecimenContainer"]] = None
    dimensional_measures: Optional[Union[dict, DimensionalObservationSet]] = None
    quantity_measure: Optional[Union[Union[dict, "SpecimenQuantityObservation"], List[Union[dict, "SpecimenQuantityObservation"]]]] = empty_list()
    quality_measure: Optional[Union[Union[dict, "SpecimenQualityObservation"], List[Union[dict, "SpecimenQualityObservation"]]]] = empty_list()
    cellular_composition_type: Optional[Union[dict, CodeableConcept]] = None
    histological_composition_measures: Optional[Union[Union[dict, HistologicalCompositionObservationSet], List[Union[dict, HistologicalCompositionObservationSet]]]] = empty_list()
    general_tissue_pathology: Optional[Union[dict, CodeableConcept]] = None
    specific_tissue_pathology: Optional[Union[dict, CodeableConcept]] = None
    preinvasive_tissue_morphology: Optional[Union[dict, CodeableConcept]] = None
    morphology_pathologically_confirmed: Optional[Union[bool, CrdchBoolean]] = None
    morphology_assessor_role: Optional[Union[dict, CodeableConcept]] = None
    morphology_assessment_method: Optional[Union[dict, CodeableConcept]] = None
    degree_of_dysplasia: Optional[Union[dict, CodeableConcept]] = None
    dysplasia_fraction: Optional[Union[str, CrdchString]] = None
    related_document: Optional[Union[Union[dict, Document], List[Union[dict, Document]]]] = empty_list()
    section_location: Optional[Union[dict, CodeableConcept]] = None
    derived_product: Optional[Union[Union[dict, BiologicProduct], List[Union[dict, BiologicProduct]]]] = empty_list()
    distance_from_paired_specimen: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, CrdchString):
            self.description = CrdchString(self.description)

        if self.specimen_type is not None and not isinstance(self.specimen_type, CodeableConcept):
            self.specimen_type = CodeableConcept(**as_dict(self.specimen_type))

        if self.analyte_type is not None and not isinstance(self.analyte_type, CodeableConcept):
            self.analyte_type = CodeableConcept(**as_dict(self.analyte_type))

        if self.associated_project is not None and not isinstance(self.associated_project, ResearchProject):
            self.associated_project = ResearchProject(**as_dict(self.associated_project))

        if self.data_provider is not None and not isinstance(self.data_provider, Organization):
            self.data_provider = Organization(**as_dict(self.data_provider))

        if self.source_material_type is not None and not isinstance(self.source_material_type, CodeableConcept):
            self.source_material_type = CodeableConcept(**as_dict(self.source_material_type))

        if not isinstance(self.parent_specimen, list):
            self.parent_specimen = [self.parent_specimen] if self.parent_specimen is not None else []
        self.parent_specimen = [v if isinstance(v, Specimen) else Specimen(**as_dict(v)) for v in self.parent_specimen]

        if self.source_subject is not None and not isinstance(self.source_subject, Subject):
            self.source_subject = Subject(**as_dict(self.source_subject))

        if self.tumor_status_at_collection is not None and not isinstance(self.tumor_status_at_collection, CodeableConcept):
            self.tumor_status_at_collection = CodeableConcept(**as_dict(self.tumor_status_at_collection))

        if self.creation_activity is not None and not isinstance(self.creation_activity, SpecimenCreationActivity):
            self.creation_activity = SpecimenCreationActivity(**as_dict(self.creation_activity))

        if not isinstance(self.processing_activity, list):
            self.processing_activity = [self.processing_activity] if self.processing_activity is not None else []
        self.processing_activity = [v if isinstance(v, SpecimenProcessingActivity) else SpecimenProcessingActivity(**as_dict(v)) for v in self.processing_activity]

        if not isinstance(self.storage_activity, list):
            self.storage_activity = [self.storage_activity] if self.storage_activity is not None else []
        self.storage_activity = [v if isinstance(v, SpecimenStorageActivity) else SpecimenStorageActivity(**as_dict(v)) for v in self.storage_activity]

        if not isinstance(self.transport_activity, list):
            self.transport_activity = [self.transport_activity] if self.transport_activity is not None else []
        self.transport_activity = [v if isinstance(v, SpecimenTransportActivity) else SpecimenTransportActivity(**as_dict(v)) for v in self.transport_activity]

        if self.contained_in is not None and not isinstance(self.contained_in, SpecimenContainer):
            self.contained_in = SpecimenContainer(**as_dict(self.contained_in))

        if self.dimensional_measures is not None and not isinstance(self.dimensional_measures, DimensionalObservationSet):
            self.dimensional_measures = DimensionalObservationSet(**as_dict(self.dimensional_measures))

        self._normalize_inlined_as_list(slot_name="quantity_measure", slot_type=SpecimenQuantityObservation, key_name="observation_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="quality_measure", slot_type=SpecimenQualityObservation, key_name="observation_type", keyed=False)

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, CodeableConcept):
            self.cellular_composition_type = CodeableConcept(**as_dict(self.cellular_composition_type))

        self._normalize_inlined_as_list(slot_name="histological_composition_measures", slot_type=HistologicalCompositionObservationSet, key_name="id", keyed=False)

        if self.general_tissue_pathology is not None and not isinstance(self.general_tissue_pathology, CodeableConcept):
            self.general_tissue_pathology = CodeableConcept(**as_dict(self.general_tissue_pathology))

        if self.specific_tissue_pathology is not None and not isinstance(self.specific_tissue_pathology, CodeableConcept):
            self.specific_tissue_pathology = CodeableConcept(**as_dict(self.specific_tissue_pathology))

        if self.preinvasive_tissue_morphology is not None and not isinstance(self.preinvasive_tissue_morphology, CodeableConcept):
            self.preinvasive_tissue_morphology = CodeableConcept(**as_dict(self.preinvasive_tissue_morphology))

        if self.morphology_pathologically_confirmed is not None and not isinstance(self.morphology_pathologically_confirmed, CrdchBoolean):
            self.morphology_pathologically_confirmed = CrdchBoolean(self.morphology_pathologically_confirmed)

        if self.morphology_assessor_role is not None and not isinstance(self.morphology_assessor_role, CodeableConcept):
            self.morphology_assessor_role = CodeableConcept(**as_dict(self.morphology_assessor_role))

        if self.morphology_assessment_method is not None and not isinstance(self.morphology_assessment_method, CodeableConcept):
            self.morphology_assessment_method = CodeableConcept(**as_dict(self.morphology_assessment_method))

        if self.degree_of_dysplasia is not None and not isinstance(self.degree_of_dysplasia, CodeableConcept):
            self.degree_of_dysplasia = CodeableConcept(**as_dict(self.degree_of_dysplasia))

        if self.dysplasia_fraction is not None and not isinstance(self.dysplasia_fraction, CrdchString):
            self.dysplasia_fraction = CrdchString(self.dysplasia_fraction)

        if not isinstance(self.related_document, list):
            self.related_document = [self.related_document] if self.related_document is not None else []
        self.related_document = [v if isinstance(v, Document) else Document(**as_dict(v)) for v in self.related_document]

        if self.section_location is not None and not isinstance(self.section_location, CodeableConcept):
            self.section_location = CodeableConcept(**as_dict(self.section_location))

        if not isinstance(self.derived_product, list):
            self.derived_product = [self.derived_product] if self.derived_product is not None else []
        self.derived_product = [v if isinstance(v, BiologicProduct) else BiologicProduct(**as_dict(v)) for v in self.derived_product]

        if self.distance_from_paired_specimen is not None and not isinstance(self.distance_from_paired_specimen, Quantity):
            self.distance_from_paired_specimen = Quantity(**as_dict(self.distance_from_paired_specimen))

        super().__post_init__(**kwargs)


@dataclass
class SpecimenContainer(Entity):
    """
    A vessel in which a specimen is held or to which it is attached - for storage or as a substrate for growth (e.g. a
    cell culture dish) or analysis (e.g. a microscope slide or 96-well plate)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenContainer
    class_class_curie: ClassVar[str] = "crdch:SpecimenContainer"
    class_name: ClassVar[str] = "SpecimenContainer"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenContainer

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    container_type: Optional[Union[dict, CodeableConcept]] = None
    container_number: Optional[Union[str, CrdchString]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    parent_container: Optional[Union[dict, "SpecimenContainer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.container_type is not None and not isinstance(self.container_type, CodeableConcept):
            self.container_type = CodeableConcept(**as_dict(self.container_type))

        if self.container_number is not None and not isinstance(self.container_number, CrdchString):
            self.container_number = CrdchString(self.container_number)

        if not isinstance(self.additive, list):
            self.additive = [self.additive] if self.additive is not None else []
        self.additive = [v if isinstance(v, Substance) else Substance(**as_dict(v)) for v in self.additive]

        if self.parent_container is not None and not isinstance(self.parent_container, SpecimenContainer):
            self.parent_container = SpecimenContainer(**as_dict(self.parent_container))

        super().__post_init__(**kwargs)


@dataclass
class SpecimenCreationActivity(Entity):
    """
    The process of creating a specimen. This may occur through observing and/or collecting material from an biological
    source or natural setting, or through derivation from an existing specimen (e.g. via portioning or aliquoting).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenCreationActivity
    class_class_curie: ClassVar[str] = "crdch:SpecimenCreationActivity"
    class_name: ClassVar[str] = "SpecimenCreationActivity"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenCreationActivity

    activity_type: Optional[Union[dict, CodeableConcept]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    collection_method_type: Optional[Union[dict, CodeableConcept]] = None
    derivation_method_type: Optional[Union[dict, CodeableConcept]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    collection_site: Optional[Union[dict, BodySite]] = None
    quantity_collected: Optional[Union[dict, Quantity]] = None
    execution_time_observation: Optional[Union[Union[dict, ExecutionTimeObservation], List[Union[dict, ExecutionTimeObservation]]]] = empty_list()
    execution_condition_observation: Optional[Union[Union[dict, ExecutionConditionObservation], List[Union[dict, ExecutionConditionObservation]]]] = empty_list()
    specimen_order: Optional[Union[int, CrdchInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CodeableConcept):
            self.activity_type = CodeableConcept(**as_dict(self.activity_type))

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.collection_method_type is not None and not isinstance(self.collection_method_type, CodeableConcept):
            self.collection_method_type = CodeableConcept(**as_dict(self.collection_method_type))

        if self.derivation_method_type is not None and not isinstance(self.derivation_method_type, CodeableConcept):
            self.derivation_method_type = CodeableConcept(**as_dict(self.derivation_method_type))

        if not isinstance(self.additive, list):
            self.additive = [self.additive] if self.additive is not None else []
        self.additive = [v if isinstance(v, Substance) else Substance(**as_dict(v)) for v in self.additive]

        if self.collection_site is not None and not isinstance(self.collection_site, BodySite):
            self.collection_site = BodySite(**as_dict(self.collection_site))

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, Quantity):
            self.quantity_collected = Quantity(**as_dict(self.quantity_collected))

        self._normalize_inlined_as_list(slot_name="execution_time_observation", slot_type=ExecutionTimeObservation, key_name="observation_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="execution_condition_observation", slot_type=ExecutionConditionObservation, key_name="observation_type", keyed=False)

        if self.specimen_order is not None and not isinstance(self.specimen_order, CrdchInteger):
            self.specimen_order = CrdchInteger(self.specimen_order)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenQualityObservation(Entity):
    """
    A structured object that describes a characteristic of a specimen indicative of its quality or suitability for
    use, as generated through a point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenQualityObservation
    class_class_curie: ClassVar[str] = "crdch:SpecimenQualityObservation"
    class_name: ClassVar[str] = "SpecimenQualityObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenQualityObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_quantity: Union[dict, Quantity] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, Organization]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_quantity):
            self.MissingRequiredField("value_quantity")
        if not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class SpecimenQuantityObservation(Entity):
    """
    A structured object that describes a single data item about the quantity of an entity, as generated through a
    point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenQuantityObservation
    class_class_curie: ClassVar[str] = "crdch:SpecimenQuantityObservation"
    class_name: ClassVar[str] = "SpecimenQuantityObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenQuantityObservation

    observation_type: Union[dict, CodeableConcept] = None
    value_quantity: Union[dict, Quantity] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, Organization]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self._is_empty(self.value_quantity):
            self.MissingRequiredField("value_quantity")
        if not isinstance(self.value_quantity, Quantity):
            self.value_quantity = Quantity(**as_dict(self.value_quantity))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type] if self.method_type is not None else []
        self.method_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.method_type]

        if not isinstance(self.focus, list):
            self.focus = [self.focus] if self.focus is not None else []
        self.focus = [v if isinstance(v, Entity) else Entity(**as_dict(v)) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        super().__post_init__(**kwargs)


@dataclass
class SpecimenProcessingActivity(Entity):
    """
    An activity that modifies the physical structure, composition, or state of a specimen. Unlike SpecimenCreation,
    SpecimenProcessing activities do not result in the generation of new entities - they take a single specimen as
    input, and output that same specimen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenProcessingActivity
    class_class_curie: ClassVar[str] = "crdch:SpecimenProcessingActivity"
    class_name: ClassVar[str] = "SpecimenProcessingActivity"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenProcessingActivity

    activity_type: Optional[Union[dict, CodeableConcept]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[Union[dict, Quantity], List[Union[dict, Quantity]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    execution_time_observation: Optional[Union[Union[dict, ExecutionTimeObservation], List[Union[dict, ExecutionTimeObservation]]]] = empty_list()
    execution_condition_observation: Optional[Union[Union[dict, ExecutionConditionObservation], List[Union[dict, ExecutionConditionObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CodeableConcept):
            self.activity_type = CodeableConcept(**as_dict(self.activity_type))

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if not isinstance(self.duration, list):
            self.duration = [self.duration] if self.duration is not None else []
        self.duration = [v if isinstance(v, Quantity) else Quantity(**as_dict(v)) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if not isinstance(self.additive, list):
            self.additive = [self.additive] if self.additive is not None else []
        self.additive = [v if isinstance(v, Substance) else Substance(**as_dict(v)) for v in self.additive]

        self._normalize_inlined_as_list(slot_name="execution_time_observation", slot_type=ExecutionTimeObservation, key_name="observation_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="execution_condition_observation", slot_type=ExecutionConditionObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenStorageActivity(Entity):
    """
    An activity in which a specimen is stored or maintained in a particular location, container, or state. Unlike
    'processing' activities, storage does not alter the
    intrinsic physical nature of a specimen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenStorageActivity
    class_class_curie: ClassVar[str] = "crdch:SpecimenStorageActivity"
    class_name: ClassVar[str] = "SpecimenStorageActivity"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenStorageActivity

    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[dict, Quantity]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    container: Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if self.duration is not None and not isinstance(self.duration, Quantity):
            self.duration = Quantity(**as_dict(self.duration))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if not isinstance(self.container, list):
            self.container = [self.container] if self.container is not None else []
        self.container = [v if isinstance(v, SpecimenContainer) else SpecimenContainer(**as_dict(v)) for v in self.container]

        super().__post_init__(**kwargs)


@dataclass
class SpecimenTransportActivity(Entity):
    """
    An activity through which a specimen is transported between locations or organizations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.SpecimenTransportActivity
    class_class_curie: ClassVar[str] = "crdch:SpecimenTransportActivity"
    class_name: ClassVar[str] = "SpecimenTransportActivity"
    class_model_uri: ClassVar[URIRef] = CRDCH.SpecimenTransportActivity

    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[Union[str, CrdchString], List[Union[str, CrdchString]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    transport_origin: Optional[Union[dict, Organization]] = None
    transport_destination: Optional[Union[dict, Organization]] = None
    execution_condition_observation: Optional[Union[Union[dict, ExecutionConditionObservation], List[Union[dict, ExecutionConditionObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if not isinstance(self.duration, list):
            self.duration = [self.duration] if self.duration is not None else []
        self.duration = [v if isinstance(v, CrdchString) else CrdchString(v) for v in self.duration]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.transport_origin is not None and not isinstance(self.transport_origin, Organization):
            self.transport_origin = Organization(**as_dict(self.transport_origin))

        if self.transport_destination is not None and not isinstance(self.transport_destination, Organization):
            self.transport_destination = Organization(**as_dict(self.transport_destination))

        self._normalize_inlined_as_list(slot_name="execution_condition_observation", slot_type=ExecutionConditionObservation, key_name="observation_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Subject(Entity):
    """
    Demographics and other administrative information about an individual or animal receiving care or other
    health-related services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Subject
    class_class_curie: ClassVar[str] = "crdch:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CRDCH.Subject

    id: Union[str, CrdchString] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    species: Optional[Union[dict, CodeableConcept]] = None
    breed: Optional[Union[dict, CodeableConcept]] = None
    sex: Optional[Union[dict, CodeableConcept]] = None
    ethnicity: Optional[Union[dict, CodeableConcept]] = None
    race: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    year_of_birth: Optional[Union[int, CrdchInteger]] = None
    vital_status: Optional[Union[dict, CodeableConcept]] = None
    age_at_death: Optional[Union[dict, Quantity]] = None
    year_of_death: Optional[Union[int, CrdchInteger]] = None
    cause_of_death: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if self.species is not None and not isinstance(self.species, CodeableConcept):
            self.species = CodeableConcept(**as_dict(self.species))

        if self.breed is not None and not isinstance(self.breed, CodeableConcept):
            self.breed = CodeableConcept(**as_dict(self.breed))

        if self.sex is not None and not isinstance(self.sex, CodeableConcept):
            self.sex = CodeableConcept(**as_dict(self.sex))

        if self.ethnicity is not None and not isinstance(self.ethnicity, CodeableConcept):
            self.ethnicity = CodeableConcept(**as_dict(self.ethnicity))

        if not isinstance(self.race, list):
            self.race = [self.race] if self.race is not None else []
        self.race = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.race]

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, CrdchInteger):
            self.year_of_birth = CrdchInteger(self.year_of_birth)

        if self.vital_status is not None and not isinstance(self.vital_status, CodeableConcept):
            self.vital_status = CodeableConcept(**as_dict(self.vital_status))

        if self.age_at_death is not None and not isinstance(self.age_at_death, Quantity):
            self.age_at_death = Quantity(**as_dict(self.age_at_death))

        if self.year_of_death is not None and not isinstance(self.year_of_death, CrdchInteger):
            self.year_of_death = CrdchInteger(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, CodeableConcept):
            self.cause_of_death = CodeableConcept(**as_dict(self.cause_of_death))

        super().__post_init__(**kwargs)


@dataclass
class Substance(Entity):
    """
    A type of material substance, or instance thereof, as used in a particular application. May include information
    about the role the substance played in a particular application.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Substance
    class_class_curie: ClassVar[str] = "crdch:Substance"
    class_name: ClassVar[str] = "Substance"
    class_model_uri: ClassVar[URIRef] = CRDCH.Substance

    substance_type: Optional[Union[dict, CodeableConcept]] = None
    role: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    substance_quantity: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.substance_type is not None and not isinstance(self.substance_type, CodeableConcept):
            self.substance_type = CodeableConcept(**as_dict(self.substance_type))

        if not isinstance(self.role, list):
            self.role = [self.role] if self.role is not None else []
        self.role = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.role]

        if self.substance_quantity is not None and not isinstance(self.substance_quantity, Quantity):
            self.substance_quantity = Quantity(**as_dict(self.substance_quantity))

        super().__post_init__(**kwargs)


@dataclass
class TimePoint(Entity):
    """
    A structured representation of a single point in time that allows direct/explicit declaration as a dateTime,
    specification in terms of offset from a defined index, or description of an event type as a proxy for the time
    point when it occurred.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.TimePoint
    class_class_curie: ClassVar[str] = "crdch:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = CRDCH.TimePoint

    id: Optional[Union[str, CrdchString]] = None
    date_time: Optional[Union[str, CrdchDateTime]] = None
    index_time_point: Optional[Union[dict, "TimePoint"]] = None
    offset_from_index: Optional[Union[dict, Quantity]] = None
    event_type: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.date_time is not None and not isinstance(self.date_time, CrdchDateTime):
            self.date_time = CrdchDateTime(self.date_time)

        if self.index_time_point is not None and not isinstance(self.index_time_point, TimePoint):
            self.index_time_point = TimePoint(**as_dict(self.index_time_point))

        if self.offset_from_index is not None and not isinstance(self.offset_from_index, Quantity):
            self.offset_from_index = Quantity(**as_dict(self.offset_from_index))

        if not isinstance(self.event_type, list):
            self.event_type = [self.event_type] if self.event_type is not None else []
        self.event_type = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.event_type]

        super().__post_init__(**kwargs)


@dataclass
class TimePeriod(Entity):
    """
    A period of time between a start and end time point.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.TimePeriod
    class_class_curie: ClassVar[str] = "crdch:TimePeriod"
    class_name: ClassVar[str] = "TimePeriod"
    class_model_uri: ClassVar[URIRef] = CRDCH.TimePeriod

    period_start_start: Optional[Union[dict, TimePoint]] = None
    period_end_end: Optional[Union[dict, TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.period_start_start is not None and not isinstance(self.period_start_start, TimePoint):
            self.period_start_start = TimePoint(**as_dict(self.period_start_start))

        if self.period_end_end is not None and not isinstance(self.period_end_end, TimePoint):
            self.period_end_end = TimePoint(**as_dict(self.period_end_end))

        super().__post_init__(**kwargs)


@dataclass
class TobaccoExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to tobacco, as generated
    through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.TobaccoExposureObservation
    class_class_curie: ClassVar[str] = "crdch:TobaccoExposureObservation"
    class_name: ClassVar[str] = "TobaccoExposureObservation"
    class_model_uri: ClassVar[URIRef] = CRDCH.TobaccoExposureObservation

    observation_type: Union[dict, CodeableConcept] = None
    id: Optional[Union[str, CrdchString]] = None
    category: Optional[Union[dict, CodeableConcept]] = None
    method_type: Optional[Union[dict, CodeableConcept]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, Subject]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    value_integer: Optional[Union[int, CrdchInteger]] = None
    value_codeable_concept: Optional[Union[dict, CodeableConcept]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_type):
            self.MissingRequiredField("observation_type")
        if not isinstance(self.observation_type, CodeableConcept):
            self.observation_type = CodeableConcept(**as_dict(self.observation_type))

        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        if self.category is not None and not isinstance(self.category, CodeableConcept):
            self.category = CodeableConcept(**as_dict(self.category))

        if self.method_type is not None and not isinstance(self.method_type, CodeableConcept):
            self.method_type = CodeableConcept(**as_dict(self.method_type))

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**as_dict(self.performed_by))

        if self.value_integer is not None and not isinstance(self.value_integer, CrdchInteger):
            self.value_integer = CrdchInteger(self.value_integer)

        if self.value_codeable_concept is not None and not isinstance(self.value_codeable_concept, CodeableConcept):
            self.value_codeable_concept = CodeableConcept(**as_dict(self.value_codeable_concept))

        super().__post_init__(**kwargs)


@dataclass
class Treatment(Entity):
    """
    Represent medication administration or other treatment types.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRDCH.Treatment
    class_class_curie: ClassVar[str] = "crdch:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = CRDCH.Treatment

    id: Optional[Union[str, CrdchString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    treatment_for_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    concurrent_treatment: Optional[Union[Union[dict, "Treatment"], List[Union[dict, "Treatment"]]]] = empty_list()
    treatment_type: Optional[Union[dict, CodeableConcept]] = None
    subject: Optional[Union[dict, Subject]] = None
    date_started: Optional[Union[dict, TimePoint]] = None
    date_ended: Optional[Union[dict, TimePoint]] = None
    treatment_end_reason: Optional[Union[Union[dict, CodeableConcept], List[Union[dict, CodeableConcept]]]] = empty_list()
    regimen: Optional[Union[dict, CodeableConcept]] = None
    therapeutic_agent: Optional[Union[dict, Substance]] = None
    number_of_cycles: Optional[Union[int, CrdchInteger]] = None
    treatment_frequency: Optional[Union[dict, CodeableConcept]] = None
    treatment_anatomic_site: Optional[Union[dict, BodySite]] = None
    treatment_intent: Optional[Union[dict, CodeableConcept]] = None
    treatment_effect: Optional[Union[dict, CodeableConcept]] = None
    treatment_outcome: Optional[Union[dict, CodeableConcept]] = None
    treatment_dose: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CrdchString):
            self.id = CrdchString(self.id)

        self._normalize_inlined_as_list(slot_name="identifier", slot_type=Identifier, key_name="value", keyed=False)

        if not isinstance(self.treatment_for_diagnosis, list):
            self.treatment_for_diagnosis = [self.treatment_for_diagnosis] if self.treatment_for_diagnosis is not None else []
        self.treatment_for_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**as_dict(v)) for v in self.treatment_for_diagnosis]

        if not isinstance(self.concurrent_treatment, list):
            self.concurrent_treatment = [self.concurrent_treatment] if self.concurrent_treatment is not None else []
        self.concurrent_treatment = [v if isinstance(v, Treatment) else Treatment(**as_dict(v)) for v in self.concurrent_treatment]

        if self.treatment_type is not None and not isinstance(self.treatment_type, CodeableConcept):
            self.treatment_type = CodeableConcept(**as_dict(self.treatment_type))

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**as_dict(self.subject))

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if not isinstance(self.treatment_end_reason, list):
            self.treatment_end_reason = [self.treatment_end_reason] if self.treatment_end_reason is not None else []
        self.treatment_end_reason = [v if isinstance(v, CodeableConcept) else CodeableConcept(**as_dict(v)) for v in self.treatment_end_reason]

        if self.regimen is not None and not isinstance(self.regimen, CodeableConcept):
            self.regimen = CodeableConcept(**as_dict(self.regimen))

        if self.therapeutic_agent is not None and not isinstance(self.therapeutic_agent, Substance):
            self.therapeutic_agent = Substance(**as_dict(self.therapeutic_agent))

        if self.number_of_cycles is not None and not isinstance(self.number_of_cycles, CrdchInteger):
            self.number_of_cycles = CrdchInteger(self.number_of_cycles)

        if self.treatment_frequency is not None and not isinstance(self.treatment_frequency, CodeableConcept):
            self.treatment_frequency = CodeableConcept(**as_dict(self.treatment_frequency))

        if self.treatment_anatomic_site is not None and not isinstance(self.treatment_anatomic_site, BodySite):
            self.treatment_anatomic_site = BodySite(**as_dict(self.treatment_anatomic_site))

        if self.treatment_intent is not None and not isinstance(self.treatment_intent, CodeableConcept):
            self.treatment_intent = CodeableConcept(**as_dict(self.treatment_intent))

        if self.treatment_effect is not None and not isinstance(self.treatment_effect, CodeableConcept):
            self.treatment_effect = CodeableConcept(**as_dict(self.treatment_effect))

        if self.treatment_outcome is not None and not isinstance(self.treatment_outcome, CodeableConcept):
            self.treatment_outcome = CodeableConcept(**as_dict(self.treatment_outcome))

        if self.treatment_dose is not None and not isinstance(self.treatment_dose, Quantity):
            self.treatment_dose = Quantity(**as_dict(self.treatment_dose))

        super().__post_init__(**kwargs)


# Enumerations
class EnumCRDCHAlcoholExposureObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHAlcoholExposureObservationCategory",
        code_set=None,
    )

class EnumCRDCHAlcoholExposureObservationObservationType(EnumDefinitionImpl):
    """
    Types of observations about a Subject's exposure to alcohol.
    """
    alcohol_days_per_week = PermissibleValue(text="alcohol_days_per_week",
                                                                 description="Numeric value used to describe the average number of days each week that a person consumes an alcoholic beverage.")
    alcohol_drinks_per_day = PermissibleValue(text="alcohol_drinks_per_day",
                                                                   description="Numeric value used to describe the average number of alcoholic beverages a person consumes per day.")
    alcohol_history = PermissibleValue(text="alcohol_history",
                                                     description="A response to a question that asks whether the participant has consumed at least 12 drinks of any kind of alcoholic beverage in their lifetime.")
    alcohol_intensity = PermissibleValue(text="alcohol_intensity",
                                                         description="Category to describe the patient's current level of alcohol use as self-reported by the patient.")

    _defn = EnumDefinition(
        name="EnumCRDCHAlcoholExposureObservationObservationType",
        description="Types of observations about a Subject's exposure to alcohol.",
    )

class EnumCRDCHAlcoholExposureObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHAlcoholExposureObservationMethodType",
        code_set=None,
    )

class EnumCRDCHAlcoholExposureObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHAlcoholExposureObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHBodySiteSite(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHBodySiteSite",
        code_set=None,
    )

class EnumCRDCHBodySiteQualifier(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHBodySiteQualifier",
        code_set=None,
    )

class EnumCRDCHBiologicProductProductType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHBiologicProductProductType",
        code_set=None,
    )

class EnumCRDCHCancerGradeObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationCategory",
        code_set=None,
    )

class EnumCRDCHCancerGradeObservationObservationType(EnumDefinitionImpl):

    enneking_msts_grade = PermissibleValue(text="enneking_msts_grade",
                                                             description="The text term used to describe the surgical grade of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).")
    esophageal_columnar_dysplasia_degree = PermissibleValue(text="esophageal_columnar_dysplasia_degree",
                                                                                               description="Text term to describe the amount of dysplasia found within the benign esophageal columnar mucosa.")
    inpc_grade = PermissibleValue(text="inpc_grade",
                                           description="Text term used to describe the classification of neuroblastic differentiation within neuroblastoma tumors, as defined by the International Neuroblastoma Pathology Classification (INPC).")
    gleason_grade_group = PermissibleValue(text="gleason_grade_group",
                                                             description="The text term used to describe the overall grouping of grades defined by the Gleason grading classification, which is used to determine the aggressiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    primary_gleason_grade = PermissibleValue(text="primary_gleason_grade",
                                                                 description="The text term used to describe the primary Gleason score, which describes the pattern of cells making up the largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggressiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    secondary_gleason_grade = PermissibleValue(text="secondary_gleason_grade",
                                                                     description="The text term used to describe the secondary Gleason score, which describes the pattern of cells making up the second largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggressiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    tumor_grade = PermissibleValue(text="tumor_grade",
                                             description="Text value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.")

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationObservationType",
    )

class EnumCRDCHCancerGradeObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationMethodType",
        code_set=None,
    )

class EnumCRDCHCancerGradeObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHCancerGradeObservationSetCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationSetCategory",
        code_set=None,
    )

class EnumCRDCHCancerGradeObservationSetMethodType(EnumDefinitionImpl):
    """
    A morphologic classification system of malignant tumors, usually relating to disease progression and clinical
    outcome. It is based upon the presence or absence of several morphologic parameters, including tumor cell
    necrosis, cytologic atypia, nuclear pleomorphism and mitotic figures, the architectural infiltrating patterns, and
    the degree of tumor cell differentiation. Malignant tumors usually are graded I-III
    """
    Gleason = PermissibleValue(text="Gleason",
                                     description="A grading system for prostatic carcinoma based on the microscopic glandular architectural patterns of the malignant epithelial cells. Nuclear atypia is not evaluated. It defines five patterns or grades which reflect decreasing differentiation.")
    INPC = PermissibleValue(text="INPC")

    _defn = EnumDefinition(
        name="EnumCRDCHCancerGradeObservationSetMethodType",
        description="A morphologic classification system of malignant tumors, usually relating to disease progression and clinical outcome. It is based upon the presence or absence of several morphologic parameters, including tumor cell necrosis, cytologic atypia, nuclear pleomorphism and mitotic figures, the architectural infiltrating patterns, and the degree of tumor cell differentiation. Malignant tumors usually are graded I-III",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Unspecified grading system",
                PermissibleValue(text="Unspecified grading system") )

class EnumCRDCHCancerStageObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationCategory",
        code_set=None,
    )

class EnumCRDCHCancerStageObservationObservationType(EnumDefinitionImpl):
    """
    Types of observations or components of a cancer staging assessment.
    """
    Overall = PermissibleValue(text="Overall",
                                     description="The overall stage of the disease")

    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationObservationType",
        description="Types of observations or components of a cancer staging assessment.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Tumor (T)",
                PermissibleValue(text="Tumor (T)",
                                 description="T classifies the size or direct extent of the primary tumor") )
        setattr(cls, "Node (N)",
                PermissibleValue(text="Node (N)",
                                 description="N classifies the degree of spread to regional lymph nodes") )
        setattr(cls, "Metastasis (M)",
                PermissibleValue(text="Metastasis (M)",
                                 description="M classifies the presence of distant metastasis") )
        setattr(cls, "Clinical Overall",
                PermissibleValue(text="Clinical Overall",
                                 description="The overall stage of the disease; clinical stage is determined from evidence acquired before treatment (including clinical examination, imaging, endoscopy, biopsy, surgical exploration)") )
        setattr(cls, "Clinical Tumor (T)",
                PermissibleValue(text="Clinical Tumor (T)",
                                 description="T classifies the size or direct extent of the primary tumor; clinical stage is determined from evidence acquired before treatment (including clinical examination, imaging, endoscopy, biopsy, surgical exploration)") )
        setattr(cls, "Clinical Node (N)",
                PermissibleValue(text="Clinical Node (N)",
                                 description="N classifies the degree of spread to regional lymph nodes; clinical stage is determined from evidence acquired before treatment (including clinical examination, imaging, endoscopy, biopsy, surgical exploration)") )
        setattr(cls, "Clinical Metastasis (M)",
                PermissibleValue(text="Clinical Metastasis (M)",
                                 description="M classifies the presence of distant metastasis; clinical stage is determined from evidence acquired before treatment (including clinical examination, imaging, endoscopy, biopsy, surgical exploration)") )
        setattr(cls, "Pathological Overall",
                PermissibleValue(text="Pathological Overall",
                                 description="The overall stage of the disease; stage given by histopathologic examination of a surgical specimen") )
        setattr(cls, "Pathological Tumor (T)",
                PermissibleValue(text="Pathological Tumor (T)",
                                 description="T classifies the size or direct extent of the primary tumor; stage given by histopathologic examination of a surgical specimen") )
        setattr(cls, "Pathological Node (N)",
                PermissibleValue(text="Pathological Node (N)",
                                 description="N classifies the degree of spread to regional lymph nodes; stage given by histopathologic examination of a surgical specimen") )
        setattr(cls, "Pathological Metastasis (M)",
                PermissibleValue(text="Pathological Metastasis (M)",
                                 description="M classifies the presence of distant metastasis; stage given by histopathologic examination of a surgical specimen") )
        setattr(cls, "Ann Arbor Substage Modifier",
                PermissibleValue(text="Ann Arbor Substage Modifier",
                                 description="The substage classification modifiers amend each stage based on distinct features.") )

class EnumCRDCHCancerStageObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationMethodType",
        code_set=None,
    )

class EnumCRDCHCancerStageObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHCancerStageObservationSetCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationSetCategory",
        code_set=None,
    )

class EnumCRDCHCancerStageObservationSetMethodType(EnumDefinitionImpl):
    """
    Classification systems used for defining the point in the natural history of a malignant disease a patient is when
    a diagnosis is made
    """
    _defn = EnumDefinition(
        name="EnumCRDCHCancerStageObservationSetMethodType",
        description="Classification systems used for defining the point in the natural history of a malignant disease a patient is when a diagnosis is made",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AJCC staging system 1st edition",
                PermissibleValue(text="AJCC staging system 1st edition",
                                 description="The 1st edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 2nd edition",
                PermissibleValue(text="AJCC staging system 2nd edition",
                                 description="The 2nd edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 3rd edition",
                PermissibleValue(text="AJCC staging system 3rd edition",
                                 description="The 3rd edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 4th edition",
                PermissibleValue(text="AJCC staging system 4th edition",
                                 description="The 4th edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 5th edition",
                PermissibleValue(text="AJCC staging system 5th edition",
                                 description="The 5th edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 6th edition",
                PermissibleValue(text="AJCC staging system 6th edition",
                                 description="The 6th edition of the criteria developed by the American Joint Committee on Cancer (AJCC) used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 7th edition",
                PermissibleValue(text="AJCC staging system 7th edition",
                                 description="The 7th edition of the criteria developed by the American Joint Committee on Cancer (AJCC) in 2010, used for the classification and staging of neoplastic diseases.") )
        setattr(cls, "AJCC staging system 8th edition",
                PermissibleValue(text="AJCC staging system 8th edition",
                                 description="The 8th edition of the criteria developed by the American Joint Committee on Cancer (AJCC), implemented in 2018, used for the classification and staging of neoplastic diseases") )
        setattr(cls, "Ann Arbor staging system",
                PermissibleValue(text="Ann Arbor staging system",
                                 description="The Ann Arbor Staging guidelines used in the staging of lymphomas") )
        setattr(cls, "COG Liver staging system",
                PermissibleValue(text="COG Liver staging system",
                                 description="A staging system developed by Children's Oncology Group (COG) that categorizes liver tumors based on the size and extent of the tumor.") )
        setattr(cls, "COG Renal staging system",
                PermissibleValue(text="COG Renal staging system",
                                 description="A staging system developed by Children's Oncology Group (COG) that categorizes renal tumors, often Wilms tumor, based on the size and extent of the tumor.") )
        setattr(cls, "Enneking MSTS staging system",
                PermissibleValue(text="Enneking MSTS staging system",
                                 description="A staging system for malignant mesenchymal tumors that takes into account the surgical grade, local extent, and presence or absence of metastasis.") )
        setattr(cls, "FIGO staging system",
                PermissibleValue(text="FIGO staging system",
                                 description="A set of staging terms for carcinoma developed by the International Federation of Gynecology and Obstetrics (FIGO).") )
        setattr(cls, "IGCCCG staging system",
                PermissibleValue(text="IGCCCG staging system") )
        setattr(cls, "INRG staging system",
                PermissibleValue(text="INRG staging system",
                                 description="A clinical staging system for neuroblastoma based on preoperative imaging and determined prior to any treatment, including surgery. It includes two stages of localized disease (L1 and L2) and two stages of metastatic disease (M and MS).") )
        setattr(cls, "INSS staging system",
                PermissibleValue(text="INSS staging system",
                                 description="A surgicopathological staging system for neuroblastoma, based on the Evans staging system.") )
        setattr(cls, "IRS staging system",
                PermissibleValue(text="IRS staging system",
                                 description="A system developed by the Intergroup Rhabdomyosarcoma Studies (IRS) group for staging rhabdomyosarcomas based on a modified TNM staging system.") )
        setattr(cls, "ISS staging system",
                PermissibleValue(text="ISS staging system",
                                 description="A plasma cell myeloma stage defined according to the international staging system.") )
        setattr(cls, "Masaoka staging system",
                PermissibleValue(text="Masaoka staging system",
                                 description="A thymoma stage defined according to the Masaoka-Koga staging criteria.") )
        setattr(cls, "Unspecified staging system",
                PermissibleValue(text="Unspecified staging system",
                                 description="For use when a data contributor has a cancer staging value, but no clearly specified staging system under which that value falls.") )

class EnumCRDCHDiagnosisCondition(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDiagnosisCondition",
        code_set=None,
    )

class EnumCRDCHDiagnosisMorphology(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDiagnosisMorphology",
        code_set=None,
    )

class EnumCRDCHDiagnosisDiseaseStatus(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDiagnosisDiseaseStatus",
        code_set=None,
    )

class EnumCRDCHDiagnosisMethodOfDiagnosis(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDiagnosisMethodOfDiagnosis",
        code_set=None,
    )

class EnumCRDCHDimensionalObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDimensionalObservationCategory",
        code_set=None,
    )

class EnumCRDCHDimensionalObservationObservationType(EnumDefinitionImpl):
    """
    Types of measurements that describe the physical dimensions of an entity (e.g. a Specimen)
    """
    length = PermissibleValue(text="length",
                                   description="The length of a three-dimensional specimen, as measured in a plane perpendicular to the planes in which the width and height of the specimen are measured.")
    width = PermissibleValue(text="width",
                                 description="The width of a three-dimensional specimen, as measured in a plane perpendicular to the planes in which the length and height of the specimen are measured.")
    longest_dimension = PermissibleValue(text="longest_dimension",
                                                         description="The measured extent of the longest straight path across a specimen.")
    shortest_dimension = PermissibleValue(text="shortest_dimension",
                                                           description="The measured extent of the shortest straight path across a specimen.")
    intermediate_dimension = PermissibleValue(text="intermediate_dimension",
                                                                   description="The measured extent of the intermediate straight path across a specimen.")
    surface_area = PermissibleValue(text="surface_area",
                                               description="The total surface area of the specimen")

    _defn = EnumDefinition(
        name="EnumCRDCHDimensionalObservationObservationType",
        description="Types of measurements that describe the physical dimensions of an entity (e.g. a Specimen)",
    )

class EnumCRDCHDimensionalObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDimensionalObservationMethodType",
        code_set=None,
    )

class EnumCRDCHDimensionalObservationSetCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDimensionalObservationSetCategory",
        code_set=None,
    )

class EnumCRDCHDimensionalObservationSetMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHDimensionalObservationSetMethodType",
        code_set=None,
    )

class EnumCRDCHDocumentDocumentType(EnumDefinitionImpl):
    """
    The high-level type of the report (e.g. 'pathology report')
    """
    protocol = PermissibleValue(text="protocol",
                                       description="A protocol by which the sample was obtained or generated (e.g. a protocol listed in protocols.io)")

    _defn = EnumDefinition(
        name="EnumCRDCHDocumentDocumentType",
        description="The high-level type of the report (e.g. 'pathology report')",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pathology report",
                PermissibleValue(text="pathology report",
                                 description="A pathology report describing the specimen") )

class EnumCRDCHEnvironmentalExposureObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHEnvironmentalExposureObservationCategory",
        code_set=None,
    )

class EnumCRDCHEnvironmentalExposureObservationObservationType(EnumDefinitionImpl):
    """
    Types of observations about a Subject's environmental exposures.
    """
    asbestos_exposure = PermissibleValue(text="asbestos_exposure",
                                                         description="The yes/no/unknown indicator used to describe whether the patient was exposed to asbestos.")
    coal_dust_exposure = PermissibleValue(text="coal_dust_exposure",
                                                           description="The yes/no/unknown indicator used to describe whether a patient was exposed to fine powder derived by the crushing of coal.")
    radon_exposure = PermissibleValue(text="radon_exposure",
                                                   description="The yes/no/unknown indicator used to describe whether the patient was exposed to radon.")
    respirable_crystalline_silica_exposure = PermissibleValue(text="respirable_crystalline_silica_exposure",
                                                                                                   description="The yes/no/unknown indicator used to describe whether a patient was exposed to respirable crystalline silica, a widespread, naturally occurring, crystalline metal oxide that consists of different forms including quartz, cristobalite, tridymite, tripoli, ganister, chert and novaculite.")
    type_of_smoke_exposure = PermissibleValue(text="type_of_smoke_exposure",
                                                                   description="The text term used to describe the patient's specific type of smoke exposure.")

    _defn = EnumDefinition(
        name="EnumCRDCHEnvironmentalExposureObservationObservationType",
        description="Types of observations about a Subject's environmental exposures.",
    )

class EnumCRDCHEnvironmentalExposureObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHEnvironmentalExposureObservationMethodType",
        code_set=None,
    )

class EnumCRDCHEnvironmentalExposureObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHEnvironmentalExposureObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHExecutionConditionObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionConditionObservationCategory",
        code_set=None,
    )

class EnumCRDCHExecutionConditionObservationObservationType(EnumDefinitionImpl):
    """
    Types of observations about the environmental conditions under which specific aspects of an activity were
    performed.
    """
    ischemic_temperature = PermissibleValue(text="ischemic_temperature",
                                                               description="A term describing the temperature of a specimen when it experienced ischemia.")

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionConditionObservationObservationType",
        description="Types of observations about the environmental conditions under which specific aspects of an activity were performed.",
    )

class EnumCRDCHExecutionConditionObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionConditionObservationMethodType",
        code_set=None,
    )

class EnumCRDCHExecutionConditionObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionConditionObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHExecutionTimeObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionTimeObservationCategory",
        code_set=None,
    )

class EnumCRDCHExecutionTimeObservationObservationType(EnumDefinitionImpl):
    """
    An observation about the duration of specific aspects / parts of an activity.
    """
    time_between_excision_and_freezing = PermissibleValue(text="time_between_excision_and_freezing",
                                                                                           description="The elapsed time between the excision and freezing of the specimen from its subject/source.")
    time_between_clamping_and_freezing = PermissibleValue(text="time_between_clamping_and_freezing",
                                                                                           description="The elapsed time between the clamping of blood supply and freezing of the specimen from its subject/source.")
    ischemic_time = PermissibleValue(text="ischemic_time",
                                                 description="Duration of time, in seconds, between when the specimen stopped receiving oxygen and when it was preserved or processed.")

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionTimeObservationObservationType",
        description="An observation about the duration of specific aspects / parts of an activity.",
    )

class EnumCRDCHExecutionTimeObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHExecutionTimeObservationMethodType",
        code_set=None,
    )

class EnumCRDCHHistologicalCompositionObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHHistologicalCompositionObservationCategory",
        code_set=None,
    )

class EnumCRDCHHistologicalCompositionObservationObservationType(EnumDefinitionImpl):
    """
    Types of measurements that describe microscopic characteristics of a specimen - typically related to its cellular
    and tissue composition.
    """
    number_proliferating_cells = PermissibleValue(text="number_proliferating_cells",
                                                                           description="Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s).")
    percent_eosinophil_infiltration = PermissibleValue(text="percent_eosinophil_infiltration",
                                                                                     description="Numeric value to represent the percentage of infiltration by eosinophils in a tumor sample or specimen.")
    percent_granulocyte_infiltration = PermissibleValue(text="percent_granulocyte_infiltration",
                                                                                       description="Numeric value to represent the percentage of infiltration by granulocytes in a tumor sample or specimen.")
    percent_inflam_infiltration = PermissibleValue(text="percent_inflam_infiltration",
                                                                             description="Numeric value to represent local response to cellular injury, marked by capillary dilatation, edema and leukocyte infiltration; clinically, inflammation is manifest by redness, heat, pain, swelling and loss of function, with the need to heal damaged tissue.")
    percent_lymphocyte_infiltration = PermissibleValue(text="percent_lymphocyte_infiltration",
                                                                                     description="Numeric value to represent the percentage of infiltration by lymphocytes in a solid tissue normal sample or specimen.")
    percent_monocyte_infiltration = PermissibleValue(text="percent_monocyte_infiltration",
                                                                                 description="Numeric value to represent the percentage of monocyte infiltration in a sample or specimen.")
    percent_necrosis = PermissibleValue(text="percent_necrosis",
                                                       description="Numeric value to represent the percentage of cell death in a malignant tumor sample or specimen.")
    percent_neutrophil_infiltration = PermissibleValue(text="percent_neutrophil_infiltration",
                                                                                     description="Numeric value to represent the percentage of infiltration by neutrophils in a tumor sample or specimen.")
    percent_normal_cells = PermissibleValue(text="percent_normal_cells",
                                                               description="Numeric value to represent the percentage of normal cell content in a malignant tumor sample or specimen.")
    percent_stromal_cells = PermissibleValue(text="percent_stromal_cells",
                                                                 description="Numeric value to represent the percentage of reactive cells that are present in a malignant tumor sample or specimen but are not malignant such as fibroblasts, vascular structures, etc.")
    percent_tumor_cells = PermissibleValue(text="percent_tumor_cells",
                                                             description="Numeric value that represents the percentage of infiltration by tumor cells in a sample.")
    percent_tumor_nuclei = PermissibleValue(text="percent_tumor_nuclei",
                                                               description="Numeric value to represent the percentage of tumor nuclei in a malignant neoplasm sample or specimen.")
    tumor_infiltrating_lymphocytes = PermissibleValue(text="tumor_infiltrating_lymphocytes",
                                                                                   description="Measure of Tumor-Infiltrating Lymphocytes")
    non_tumor_tissue_area = PermissibleValue(text="non_tumor_tissue_area",
                                                                 description="The area within a sample that is represented by non-tumor tissue.")
    tumor_tissue_area = PermissibleValue(text="tumor_tissue_area",
                                                         description="The area within a sample that is comprised of tumor tissue.")
    analysis_area = PermissibleValue(text="analysis_area",
                                                 description="The total area of a sample that is used for analysis.")
    analysis_area_percentage_stroma = PermissibleValue(text="analysis_area_percentage_stroma",
                                                                                     description="The percentage of the analysis area that is represented by stromal tissue.")
    analysis_area_percentage_tumor = PermissibleValue(text="analysis_area_percentage_tumor",
                                                                                   description="The percentage of the analysis area that is represented by tumor tissue.")
    analysis_area_percentage_glass = PermissibleValue(text="analysis_area_percentage_glass",
                                                                                   description="The area of a sample on a slide that is represented by glass; the area of the sample that represents gaps in the sample.")
    analysis_area_percentage_pigmented_tumor = PermissibleValue(text="analysis_area_percentage_pigmented_tumor",
                                                                                                       description="The area of a sample on a slide that is represented by pigmented tumor tissue, which will be analyzed.")

    _defn = EnumDefinition(
        name="EnumCRDCHHistologicalCompositionObservationObservationType",
        description="Types of measurements that describe microscopic characteristics of a specimen - typically related to its cellular and tissue composition.",
    )

class EnumCRDCHHistologicalCompositionObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHHistologicalCompositionObservationMethodType",
        code_set=None,
    )

class EnumCRDCHHistologicalCompositionObservationSetCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHHistologicalCompositionObservationSetCategory",
        code_set=None,
    )

class EnumCRDCHHistologicalCompositionObservationSetMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHHistologicalCompositionObservationSetMethodType",
        code_set=None,
    )

class EnumCRDCHIdentifierType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHIdentifierType",
        code_set=None,
    )

class EnumCRDCHObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationCategory",
        code_set=None,
    )

class EnumCRDCHObservationObservationType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationObservationType",
        code_set=None,
    )

class EnumCRDCHObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationMethodType",
        code_set=None,
    )

class EnumCRDCHObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHObservationSetCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationSetCategory",
        code_set=None,
    )

class EnumCRDCHObservationSetMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHObservationSetMethodType",
        code_set=None,
    )

class EnumCRDCHQuantityValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHQuantityValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHQuantityUnit(EnumDefinitionImpl):
    """
    The unit for a value
    """
    milligrams = PermissibleValue(text="milligrams")
    days = PermissibleValue(text="days")
    minutes = PermissibleValue(text="minutes")

    _defn = EnumDefinition(
        name="EnumCRDCHQuantityUnit",
        description="The unit for a value",
    )

class EnumCRDCHResearchProjectResearchProjectType(EnumDefinitionImpl):
    """
    A high-level type of research activity
    """
    Program = PermissibleValue(text="Program",
                                     description="A broad framework of goals to be achieved.")
    Project = PermissibleValue(text="Project",
                                     description="Any specifically defined piece of work that is undertaken or attempted to meet a single requirement.")

    _defn = EnumDefinition(
        name="EnumCRDCHResearchProjectResearchProjectType",
        description="A high-level type of research activity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Clinical Trial",
                PermissibleValue(text="Clinical Trial",
                                 description="A research study that prospectively assigns participants to one or more health-related interventions to evaluate the effects on health outcomes.") )

class EnumCRDCHResearchSubjectPrimaryDiagnosisCondition(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHResearchSubjectPrimaryDiagnosisCondition",
        code_set=None,
    )

class EnumCRDCHResearchSubjectIndexTimepoint(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHResearchSubjectIndexTimepoint",
        code_set=None,
    )

class EnumCRDCHSpecimenSpecimenType(EnumDefinitionImpl):
    """
    A high-level type of specimen, based on its derivation provenance (i.e. how far removed it is from the original
    sample extracted from a source).
    """
    portion = PermissibleValue(text="portion",
                                     description="A physical sub-part taken from an existing specimen.")
    aliquot = PermissibleValue(text="aliquot",
                                     description="A specimen that results from the division of some parent specimen into equal amounts for downstream analysis.")
    analyte = PermissibleValue(text="analyte",
                                     description="A specimen generated through the extraction of a specified class of substance/chemical (e.g. DNA, RNA, protein) from a parent specimen, which is stored in solution as an analyte.")
    slide = PermissibleValue(text="slide",
                                 description="A specimen that is mounted on a slide or coverslip for microscopic analysis.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenSpecimenType",
        description="A high-level type of specimen, based on its derivation provenance (i.e. how far removed it is from the original sample extracted from a source).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Fresh Specimen",
                PermissibleValue(text="Fresh Specimen",
                                 description="A specimen representing the material that was directly collected from a subject (i.e. not generated through portioning, aliquoting, or analyte extraction from an existing specimen).") )

class EnumCRDCHSpecimenAnalyteType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenAnalyteType",
        code_set=None,
    )

class EnumCRDCHSpecimenSourceMaterialType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenSourceMaterialType",
        code_set=None,
    )

class EnumCRDCHSpecimenTumorStatusAtCollection(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenTumorStatusAtCollection",
        code_set=None,
    )

class EnumCRDCHSpecimenCellularCompositionType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenCellularCompositionType",
        code_set=None,
    )

class EnumCRDCHSpecimenGeneralTissuePathology(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenGeneralTissuePathology",
        code_set=None,
    )

class EnumCRDCHSpecimenSpecificTissuePathology(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenSpecificTissuePathology",
        code_set=None,
    )

class EnumCRDCHSpecimenPreinvasiveTissueMorphology(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenPreinvasiveTissueMorphology",
        code_set=None,
    )

class EnumCRDCHSpecimenMorphologyAssessorRole(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenMorphologyAssessorRole",
        code_set=None,
    )

class EnumCRDCHSpecimenMorphologyAssessmentMethod(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenMorphologyAssessmentMethod",
        code_set=None,
    )

class EnumCRDCHSpecimenDegreeOfDysplasia(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenDegreeOfDysplasia",
        code_set=None,
    )

class EnumCRDCHSpecimenSectionLocation(EnumDefinitionImpl):
    """
    The location in a parent specimen from which a section/portion was excised.
    """
    top = PermissibleValue(text="top",
                             description="The part of a specimen designated as its 'top' based on specified orientation criteria.")
    unknown = PermissibleValue(text="unknown",
                                     description="An unknown location on a specimen.")
    bottom = PermissibleValue(text="bottom",
                                   description="The part of a specimen designated as its 'bottom' based on specified orientation criteria.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenSectionLocation",
        description="The location in a parent specimen from which a section/portion was excised.",
    )

class EnumCRDCHSpecimenContainerContainerType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenContainerContainerType",
        code_set=None,
    )

class EnumCRDCHSpecimenCreationActivityActivityType(EnumDefinitionImpl):
    """
    The high-level type of activity through which the specimen was generated (i.e. via collection from the original
    source, or via derivation from an existing specimen)
    """
    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenCreationActivityActivityType",
        description="The high-level type of activity through which the specimen was generated (i.e. via collection from the original source, or via derivation from an existing specimen)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "collection from source",
                PermissibleValue(text="collection from source",
                                 description="An activity that collects an initial sample directly from a subject / source.") )
        setattr(cls, "derivation from specimen",
                PermissibleValue(text="derivation from specimen",
                                 description="An activity that derives a new specimen from an existing one.") )

class EnumCRDCHSpecimenCreationActivityCollectionMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenCreationActivityCollectionMethodType",
        code_set=None,
    )

class EnumCRDCHSpecimenCreationActivityDerivationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenCreationActivityDerivationMethodType",
        code_set=None,
    )

class EnumCRDCHSpecimenQualityObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQualityObservationCategory",
        code_set=None,
    )

class EnumCRDCHSpecimenQualityObservationObservationType(EnumDefinitionImpl):
    """
    Types of measurements that reflect the quality of a specimen or its suitability for use.
    """
    ribosomal_rna_28s_16s_ratio = PermissibleValue(text="ribosomal_rna_28s_16s_ratio",
                                                                             description="Ratio of quantity of 28s RNA over that of 16s RNA.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQualityObservationObservationType",
        description="Types of measurements that reflect the quality of a specimen or its suitability for use.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "a260_a280_ratio  ",
                PermissibleValue(text="a260_a280_ratio  ",
                                 description="Ratio of absorbance measured at a wavelength of 260 over that at a wavelength of 280.") )

class EnumCRDCHSpecimenQualityObservationMethodType(EnumDefinitionImpl):
    """
    A type of method used in determining the quantity of a specimen.
    """
    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQualityObservationMethodType",
        description="A type of method used in determining the quantity of a specimen.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UV Spec",
                PermissibleValue(text="UV Spec",
                                 description="A technique used to measure light absorbance across the ultraviolet and visible ranges of the electromagnetic spectrum.") )
        setattr(cls, "Pico Green",
                PermissibleValue(text="Pico Green",
                                 description="A technique applying the Pico488 fluorescent sensor dye that is used for quantifying the amount of double-stranded DNA (dsDNA) present in a given sample.") )

class EnumCRDCHSpecimenQuantityObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQuantityObservationCategory",
        code_set=None,
    )

class EnumCRDCHSpecimenQuantityObservationObservationType(EnumDefinitionImpl):
    """
    Measures related to the quantity of a specimen or analyte it currently contains - e.g. its weight, volume, or
    concentration.
    """
    weight = PermissibleValue(text="weight",
                                   description="The current weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).")
    volume = PermissibleValue(text="volume",
                                   description="The current total volume of the specimen, at the time of recording.")
    concentration = PermissibleValue(text="concentration",
                                                 description="The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'analyte', or an 'aliquot' derived from an analyte). For example, the concentration of DNA in a specimen created through extracting DNA from a blood sample.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQuantityObservationObservationType",
        description="Measures related to the quantity of a specimen or analyte it currently contains - e.g. its weight, volume, or concentration.",
    )

class EnumCRDCHSpecimenQuantityObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenQuantityObservationMethodType",
        code_set=None,
    )

class EnumCRDCHSpecimenProcessingActivityActivityType(EnumDefinitionImpl):
    """
    The high-level type of processing activity performed.
    """
    Fixation = PermissibleValue(text="Fixation",
                                       description="A processing activity that applies chemicals to preserve biological tissues from decay due to autolysis or putrefaction")
    Freezing = PermissibleValue(text="Freezing",
                                       description="A processing activity that aims to freeze a specimen.")
    Mounting = PermissibleValue(text="Mounting",
                                       description="A processing activity that aims to secure a specimen or slide in place in preparation for further examination (usually via microscopy)")
    Preservation = PermissibleValue(text="Preservation",
                                               description="A processing activity that aims to preserve a specimen.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenProcessingActivityActivityType",
        description="The high-level type of processing activity performed.",
    )

class EnumCRDCHSpecimenProcessingActivityMethodType(EnumDefinitionImpl):
    """
    A type of method used to process a specimen (e.g. freezing, fixing, treating, preserving, labeling, etc.).
    """
    LN2 = PermissibleValue(text="LN2",
                             description="Freezing in liquid nitrogen.")
    isopentane = PermissibleValue(text="isopentane",
                                           description="Freezing in isopentane.")

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenProcessingActivityMethodType",
        description="A type of method used to process a specimen (e.g. freezing, fixing, treating, preserving, labeling, etc.).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Minues 80 Degrees Celsius Freezer",
                PermissibleValue(text="Minues 80 Degrees Celsius Freezer",
                                 description="Freezing at -80 degrees celcius") )
        setattr(cls, "-20",
                PermissibleValue(text="-20",
                                 description="Freezing at -20 degrees celcius") )

class EnumCRDCHSpecimenStorageActivityMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSpecimenStorageActivityMethodType",
        code_set=None,
    )

class EnumCRDCHSubjectSpecies(EnumDefinitionImpl):
    """
    The scientific binomial name for the species of the subject
    """
    _defn = EnumDefinition(
        name="EnumCRDCHSubjectSpecies",
        description="The scientific binomial name for the species of the subject",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Homo sapiens",
                PermissibleValue(text="Homo sapiens") )
        setattr(cls, "Canis familiaris",
                PermissibleValue(text="Canis familiaris") )
        setattr(cls, "Mus musculus",
                PermissibleValue(text="Mus musculus") )

class EnumCRDCHSubjectBreed(EnumDefinitionImpl):
    """
    A label given to a group of animals homogeneous in appearance and other characteristics that distinguish it from
    other animals of the same species.
    """
    Akita = PermissibleValue(text="Akita")
    Beagle = PermissibleValue(text="Beagle")
    Boxer = PermissibleValue(text="Boxer")
    Bulldog = PermissibleValue(text="Bulldog")
    Bullmastiff = PermissibleValue(text="Bullmastiff")
    Chihuahua = PermissibleValue(text="Chihuahua")
    Dalmatian = PermissibleValue(text="Dalmatian")
    Greyhound = PermissibleValue(text="Greyhound")
    Mastiff = PermissibleValue(text="Mastiff")
    Poodle = PermissibleValue(text="Poodle")
    Rottweiler = PermissibleValue(text="Rottweiler")
    Samoyed = PermissibleValue(text="Samoyed")
    Vizsla = PermissibleValue(text="Vizsla")
    Weimaraner = PermissibleValue(text="Weimaraner")

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectBreed",
        description="A label given to a group of animals homogeneous in appearance and other characteristics that distinguish it from other animals of the same species.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Staffordshire Terrier",
                PermissibleValue(text="American Staffordshire Terrier") )
        setattr(cls, "Australian Shepherd",
                PermissibleValue(text="Australian Shepherd") )
        setattr(cls, "Basset Hound",
                PermissibleValue(text="Basset Hound") )
        setattr(cls, "Belgian Malinois",
                PermissibleValue(text="Belgian Malinois") )
        setattr(cls, "Bernese Mountain Dog",
                PermissibleValue(text="Bernese Mountain Dog") )
        setattr(cls, "Black and Tan Coonhound",
                PermissibleValue(text="Black and Tan Coonhound") )
        setattr(cls, "Border Collie",
                PermissibleValue(text="Border Collie") )
        setattr(cls, "Boston Terrier",
                PermissibleValue(text="Boston Terrier") )
        setattr(cls, "Bouvier des Flandres",
                PermissibleValue(text="Bouvier des Flandres") )
        setattr(cls, "Cavalier King Charles Spaniel",
                PermissibleValue(text="Cavalier King Charles Spaniel") )
        setattr(cls, "Chesapeake Bay Retriever",
                PermissibleValue(text="Chesapeake Bay Retriever") )
        setattr(cls, "Chinese Shar-Pei",
                PermissibleValue(text="Chinese Shar-Pei") )
        setattr(cls, "Cocker Spaniel",
                PermissibleValue(text="Cocker Spaniel") )
        setattr(cls, "Doberman Pinscher",
                PermissibleValue(text="Doberman Pinscher") )
        setattr(cls, "English Setter",
                PermissibleValue(text="English Setter") )
        setattr(cls, "Flat-Coated Retriever",
                PermissibleValue(text="Flat-Coated Retriever") )
        setattr(cls, "French Bulldog",
                PermissibleValue(text="French Bulldog") )
        setattr(cls, "German Shepherd Dog",
                PermissibleValue(text="German Shepherd Dog") )
        setattr(cls, "German Shorthaired Pointer",
                PermissibleValue(text="German Shorthaired Pointer") )
        setattr(cls, "Giant Schnauzer",
                PermissibleValue(text="Giant Schnauzer") )
        setattr(cls, "Golden Retriever",
                PermissibleValue(text="Golden Retriever") )
        setattr(cls, "Gordon Setter",
                PermissibleValue(text="Gordon Setter") )
        setattr(cls, "Irish Setter",
                PermissibleValue(text="Irish Setter") )
        setattr(cls, "Irish Wolfhound",
                PermissibleValue(text="Irish Wolfhound") )
        setattr(cls, "Labrador Retriever",
                PermissibleValue(text="Labrador Retriever") )
        setattr(cls, "Miniature Schnauzer",
                PermissibleValue(text="Miniature Schnauzer") )
        setattr(cls, "Mixed Breed",
                PermissibleValue(text="Mixed Breed") )
        setattr(cls, "Parson Russell Terrier",
                PermissibleValue(text="Parson Russell Terrier") )
        setattr(cls, "Saint Bernard",
                PermissibleValue(text="Saint Bernard") )
        setattr(cls, "Shih Tzu",
                PermissibleValue(text="Shih Tzu") )
        setattr(cls, "Staffordshire Bull Terrier",
                PermissibleValue(text="Staffordshire Bull Terrier") )
        setattr(cls, "West Highland White Terrier",
                PermissibleValue(text="West Highland White Terrier") )
        setattr(cls, "Yorkshire Terrier",
                PermissibleValue(text="Yorkshire Terrier") )

class EnumCRDCHSubjectSex(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectSex",
        code_set=None,
    )

class EnumCRDCHSubjectEthnicity(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectEthnicity",
        code_set=None,
    )

class EnumCRDCHSubjectRace(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectRace",
        code_set=None,
    )

class EnumCRDCHSubjectVitalStatus(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectVitalStatus",
        code_set=None,
    )

class EnumCRDCHSubjectCauseOfDeath(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubjectCauseOfDeath",
        code_set=None,
    )

class EnumCRDCHSubstanceSubstanceType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubstanceSubstanceType",
        code_set=None,
    )

class EnumCRDCHSubstanceRole(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHSubstanceRole",
        code_set=None,
    )

class EnumCRDCHTimePointEventType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTimePointEventType",
        code_set=None,
    )

class EnumCRDCHTobaccoExposureObservationCategory(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTobaccoExposureObservationCategory",
        code_set=None,
    )

class EnumCRDCHTobaccoExposureObservationObservationType(EnumDefinitionImpl):
    """
    Types of observations about a Subject's exposure to or use of tobacco.
    """
    cigarettes_per_day = PermissibleValue(text="cigarettes_per_day",
                                                           description="The average number of cigarettes smoked per day.")
    pack_years_smoked = PermissibleValue(text="pack_years_smoked",
                                                         description="Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20.")
    tobacco_smoking_onset_year = PermissibleValue(text="tobacco_smoking_onset_year",
                                                                           description="The year in which the participant began smoking.")
    tobacco_smoking_quit_year = PermissibleValue(text="tobacco_smoking_quit_year",
                                                                         description="The year in which the participant quit smoking.")
    years_smoked = PermissibleValue(text="years_smoked",
                                               description="Numeric value (or unknown) to represent the number of years a person has been smoking.")
    smoking_frequency = PermissibleValue(text="smoking_frequency",
                                                         description="The text term used to generally describe how often the patient smokes.")
    time_between_waking_and_first_smoke = PermissibleValue(text="time_between_waking_and_first_smoke",
                                                                                             description="The text term used to describe the approximate amount of time elapsed between the time the patient wakes up in the morning to the time they smoke their first cigarette.")
    environmental_tobacco_smoke_exposure = PermissibleValue(text="environmental_tobacco_smoke_exposure",
                                                                                               description="The yes/no/unknown indicator used to describe whether a patient was exposed to smoke that is emitted from burning tobacco, including cigarettes, pipes, and cigars. This includes tobacco smoke exhaled by smokers.")
    tobacco_smoking_status = PermissibleValue(text="tobacco_smoking_status",
                                                                   description="Category describing current smoking status and smoking history as self-reported by a patient.")
    type_of_tobacco_used = PermissibleValue(text="type_of_tobacco_used",
                                                               description="The text term used to describe the specific type of tobacco used by the patient.")

    _defn = EnumDefinition(
        name="EnumCRDCHTobaccoExposureObservationObservationType",
        description="Types of observations about a Subject's exposure to or use of tobacco.",
    )

class EnumCRDCHTobaccoExposureObservationMethodType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTobaccoExposureObservationMethodType",
        code_set=None,
    )

class EnumCRDCHTobaccoExposureObservationValueCodeableConcept(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTobaccoExposureObservationValueCodeableConcept",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentType",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentEndReason(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentEndReason",
        code_set=None,
    )

class EnumCRDCHTreatmentRegimen(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentRegimen",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentFrequency(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentFrequency",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentIntent(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentIntent",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentEffect(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentEffect",
        code_set=None,
    )

class EnumCRDCHTreatmentTreatmentOutcome(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EnumCRDCHTreatmentTreatmentOutcome",
        code_set=None,
    )

class EnumCRDCHResearchProjectPrimaryAnatomicSite(EnumDefinitionImpl):
    """
    The text term used to describe the general location of the malignant disease, as categorized by the World Health
    Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).
    """
    _defn = EnumDefinition(
        name="EnumCRDCHResearchProjectPrimaryAnatomicSite",
        description="The text term used to describe the general location of the malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).",
    )

class EnumCRDCHSubstanceRole(EnumDefinitionImpl):
    """
    A role played by the substance in a particular application (e.g. the role of a lysis buffer when applied in a
    specimen creation activity, or the role of fixative when applied in specimen processing)
    """
    fixative = PermissibleValue(text="fixative",
                                       description="A substance applied preserve biological tissues from decay due to autolysis or putrefaction")

    _defn = EnumDefinition(
        name="EnumCRDCHSubstanceRole",
        description="A role played by the substance in a particular application (e.g. the role of a lysis buffer when applied in a specimen creation activity, or the role of fixative when applied in specimen processing)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "lysis buffer",
                PermissibleValue(text="lysis buffer",
                                 description="A buffer applied to lyse and extract content from biological material.") )
        setattr(cls, "mounting medium",
                PermissibleValue(text="mounting medium",
                                 description="A substance applied to secure a specimen or slide in place for further examination (typically through microscopy)") )
        setattr(cls, "collection media",
                PermissibleValue(text="collection media",
                                 description="A substance applied to stabilize or support the growth/metabolic activity of a specimen or derived product such as a cell line.") )

class EnumCRDCHTimePointEventType(EnumDefinitionImpl):
    """
    A specific type of event for which a timepoint is captured
    """
    _defn = EnumDefinition(
        name="EnumCRDCHTimePointEventType",
        description="A specific type of event for which a timepoint is captured",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IACUC approval",
                PermissibleValue(text="IACUC approval",
                                 description="The date that the Institutional Animal Care and Use Committee (IACUC) approved an animal study protocol. This date cannot be released to funding agencies until congruency between the animal use in the funding proposal and the IACUC approved protocol has been verified.") )
        setattr(cls, "IRB approval",
                PermissibleValue(text="IRB approval",
                                 description="The date that the Institutional Review Board (IRB) approved a study protocol") )
        setattr(cls, "Histological confirmation of diagnosis",
                PermissibleValue(text="Histological confirmation of diagnosis",
                                 description="The date that a histological diagnosis was confirmed.") )

# Slots

