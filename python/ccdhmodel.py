# Auto generated from ccdhmodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-29 21:22
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
    """ An integer number.  This data type is based on the decimal type, but the fractional component is not allowed.  There are no restrictions on the size of the integer. """
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
    """ A date and time string specified using a specialized concatenation of the date and time data types, in the general format YYYY-MM-DDThh:mm:ss+zz:zz. """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "ccdh_dateTime"
    type_model_uri = CCDH.CcdhDateTime


class CcdhCurie(Uriorcurie):
    """ A compact URI (CURIE), which is a bipartite identifier of the form prefix:reference, in which the prefix is a convenient abbreviation of a URI.  It is expressed in the format “prefix:reference”. When a mapping of prefix to base URI is provided (external to this data type), a CURIE may be mapped to a URI. """
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



class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Entity
    class_class_curie: ClassVar[str] = "ccdh:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CCDH.Entity


@dataclass
class AlcoholExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to alcohol, as generated
    through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.AlcoholExposureObservation
    class_class_curie: ClassVar[str] = "ccdh:AlcoholExposureObservation"
    class_name: ClassVar[str] = "AlcoholExposureObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.AlcoholExposureObservation

    observation_type: Union[str, "CCDHAlcoholExposureObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHAlcoholExposureObservationCategory"]] = None
    method_type: Optional[Union[str, "CCDHAlcoholExposureObservationMethodType"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, "Entity"]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[int, CcdhInteger]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, "Quantity"]] = None
    valueCodeableConcept: Optional[Union[str, "CCDHAlcoholExposureObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHAlcoholExposureObservationObservationType):
            self.observation_type = CCDHAlcoholExposureObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHAlcoholExposureObservationCategory):
            self.category = CCDHAlcoholExposureObservationCategory(self.category)

        if self.method_type is not None and not isinstance(self.method_type, CCDHAlcoholExposureObservationMethodType):
            self.method_type = CCDHAlcoholExposureObservationMethodType(self.method_type)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity()

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhInteger):
            self.valueInteger = CcdhInteger(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHAlcoholExposureObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHAlcoholExposureObservationValueCodeableConcept(self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class BodySite(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BodySite
    class_class_curie: ClassVar[str] = "ccdh:BodySite"
    class_name: ClassVar[str] = "BodySite"
    class_model_uri: ClassVar[URIRef] = CCDH.BodySite

    site: Union[str, "CCDHBodySiteSite"] = None
    qualifier: Optional[Union[Union[str, "CCDHBodySiteQualifier"], List[Union[str, "CCDHBodySiteQualifier"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.site is None:
            raise ValueError("site must be supplied")
        if not isinstance(self.site, CCDHBodySiteSite):
            self.site = CCDHBodySiteSite(self.site)

        if self.qualifier is None:
            self.qualifier = []
        if not isinstance(self.qualifier, list):
            self.qualifier = [self.qualifier]
        self.qualifier = [v if isinstance(v, CCDHBodySiteQualifier) else CCDHBodySiteQualifier(v) for v in self.qualifier]

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
    product_type: Optional[Union[str, "CCDHBiologicProductProductType"]] = None
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

        if self.product_type is not None and not isinstance(self.product_type, CCDHBiologicProductProductType):
            self.product_type = CCDHBiologicProductProductType(self.product_type)

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
    cancer grade observation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation
    class_class_curie: ClassVar[str] = "ccdh:CancerGradeObservation"
    class_name: ClassVar[str] = "CancerGradeObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation

    observation_type: Union[str, "CCDHCancerGradeObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHCancerGradeObservationCategory"]] = None
    method_type: Optional[Union[str, "CCDHCancerGradeObservationMethodType"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, "Entity"]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[int, CcdhInteger]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, "Quantity"]] = None
    valueCodeableConcept: Optional[Union[str, "CCDHCancerGradeObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHCancerGradeObservationObservationType):
            self.observation_type = CCDHCancerGradeObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHCancerGradeObservationCategory):
            self.category = CCDHCancerGradeObservationCategory(self.category)

        if self.method_type is not None and not isinstance(self.method_type, CCDHCancerGradeObservationMethodType):
            self.method_type = CCDHCancerGradeObservationMethodType(self.method_type)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity()

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhInteger):
            self.valueInteger = CcdhInteger(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHCancerGradeObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHCancerGradeObservationValueCodeableConcept(self.valueCodeableConcept)

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

    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHCancerGradeObservationSetCategory"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "CCDHCancerGradeObservationSetMethodType"], List[Union[str, "CCDHCancerGradeObservationSetMethodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerGradeObservation], List[Union[dict, CancerGradeObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHCancerGradeObservationSetCategory):
            self.category = CCDHCancerGradeObservationSetCategory(self.category)

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHCancerGradeObservationSetMethodType) else CCDHCancerGradeObservationSetMethodType(v) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self._normalize_inlined_slot(slot_name="observations", slot_type=CancerGradeObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

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

    observation_type: Union[str, "CCDHCancerStageObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHCancerStageObservationCategory"]] = None
    method_type: Optional[Union[str, "CCDHCancerStageObservationMethodType"]] = None
    focus: Optional[Union[dict, "Entity"]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, "Entity"]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[int, CcdhInteger]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, "Quantity"]] = None
    valueCodeableConcept: Optional[Union[str, "CCDHCancerStageObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHCancerStageObservationObservationType):
            self.observation_type = CCDHCancerStageObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHCancerStageObservationCategory):
            self.category = CCDHCancerStageObservationCategory(self.category)

        if self.method_type is not None and not isinstance(self.method_type, CCDHCancerStageObservationMethodType):
            self.method_type = CCDHCancerStageObservationMethodType(self.method_type)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity()

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhInteger):
            self.valueInteger = CcdhInteger(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHCancerStageObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHCancerStageObservationValueCodeableConcept(self.valueCodeableConcept)

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

    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHCancerStageObservationSetCategory"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "CCDHCancerStageObservationSetMethodType"], List[Union[str, "CCDHCancerStageObservationSetMethodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerStageObservation], List[Union[dict, CancerStageObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHCancerStageObservationSetCategory):
            self.category = CCDHCancerStageObservationSetCategory(self.category)

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHCancerStageObservationSetMethodType) else CCDHCancerStageObservationSetMethodType(v) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

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
    """
    A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time.
    May be used to capture information about neoplastic and non-neoplastic conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Diagnosis
    class_class_curie: ClassVar[str] = "ccdh:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = CCDH.Diagnosis

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    age_at_diagnosis: Optional[Union[dict, "Quantity"]] = None
    year_at_diagnosis: Optional[Union[int, CcdhInteger]] = None
    condition: Optional[Union[str, "CCDHDiagnosisCondition"]] = None
    primary_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    metastatic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    stage: Optional[Union[Union[dict, CancerStageObservationSet], List[Union[dict, CancerStageObservationSet]]]] = empty_list()
    grade: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    morphology: Optional[Union[str, "CCDHDiagnosisMorphology"]] = None
    disease_status: Optional[Union[str, "CCDHDiagnosisDiseaseStatus"]] = None
    prior_diagnosis: Optional[Union[dict, "Diagnosis"]] = None
    method_of_diagnosis: Optional[Union[str, "CCDHDiagnosisMethodOfDiagnosis"]] = None
    related_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    supporting_observations: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.age_at_diagnosis is not None and not isinstance(self.age_at_diagnosis, Quantity):
            self.age_at_diagnosis = Quantity(**self.age_at_diagnosis)

        if self.year_at_diagnosis is not None and not isinstance(self.year_at_diagnosis, CcdhInteger):
            self.year_at_diagnosis = CcdhInteger(self.year_at_diagnosis)

        if self.condition is not None and not isinstance(self.condition, CCDHDiagnosisCondition):
            self.condition = CCDHDiagnosisCondition(self.condition)

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
        self.stage = [v if isinstance(v, CancerStageObservationSet) else CancerStageObservationSet(**v) for v in self.stage]

        if self.grade is None:
            self.grade = []
        if not isinstance(self.grade, list):
            self.grade = [self.grade]
        self.grade = [v if isinstance(v, Entity) else Entity(**v) for v in self.grade]

        if self.morphology is not None and not isinstance(self.morphology, CCDHDiagnosisMorphology):
            self.morphology = CCDHDiagnosisMorphology(self.morphology)

        if self.disease_status is not None and not isinstance(self.disease_status, CCDHDiagnosisDiseaseStatus):
            self.disease_status = CCDHDiagnosisDiseaseStatus(self.disease_status)

        if self.prior_diagnosis is not None and not isinstance(self.prior_diagnosis, Diagnosis):
            self.prior_diagnosis = Diagnosis(**self.prior_diagnosis)

        if self.method_of_diagnosis is not None and not isinstance(self.method_of_diagnosis, CCDHDiagnosisMethodOfDiagnosis):
            self.method_of_diagnosis = CCDHDiagnosisMethodOfDiagnosis(self.method_of_diagnosis)

        if self.related_specimen is None:
            self.related_specimen = []
        if not isinstance(self.related_specimen, list):
            self.related_specimen = [self.related_specimen]
        self.related_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.related_specimen]

        if self.supporting_observations is None:
            self.supporting_observations = []
        if not isinstance(self.supporting_observations, list):
            self.supporting_observations = [self.supporting_observations]
        self._normalize_inlined_slot(slot_name="supporting_observations", slot_type=Observation, key_name="observation_type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DimensionalObservation(Entity):
    """
    A structured object that describes a single data item about the physical dimensions of an entity (e.g. length
    width, area), as generated through a point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.DimensionalObservation
    class_class_curie: ClassVar[str] = "ccdh:DimensionalObservation"
    class_name: ClassVar[str] = "DimensionalObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.DimensionalObservation

    observation_type: Union[str, "CCDHDimensionalObservationObservationType"] = None
    valueQuantity: Union[dict, "Quantity"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHDimensionalObservationCategory"]] = None
    method_type: Optional[Union[Union[str, "CCDHDimensionalObservationMethodType"], List[Union[str, "CCDHDimensionalObservationMethodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHDimensionalObservationObservationType):
            self.observation_type = CCDHDimensionalObservationObservationType(self.observation_type)

        if self.valueQuantity is None:
            raise ValueError("valueQuantity must be supplied")
        if not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHDimensionalObservationCategory):
            self.category = CCDHDimensionalObservationCategory(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHDimensionalObservationMethodType) else CCDHDimensionalObservationMethodType(v) for v in self.method_type]

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class DimensionalObservationSet(Entity):
    """
    A set of one or more discrete observations about the physical dimensions of an object (e.g. length, width, area).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.DimensionalObservationSet
    class_class_curie: ClassVar[str] = "ccdh:DimensionalObservationSet"
    class_name: ClassVar[str] = "DimensionalObservationSet"
    class_model_uri: ClassVar[URIRef] = CCDH.DimensionalObservationSet

    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHDimensionalObservationSetCategory"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "CCDHDimensionalObservationSetMethodType"], List[Union[str, "CCDHDimensionalObservationSetMethodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, DimensionalObservation], List[Union[dict, DimensionalObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHDimensionalObservationSetCategory):
            self.category = CCDHDimensionalObservationSetCategory(self.category)

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHDimensionalObservationSetMethodType) else CCDHDimensionalObservationSetMethodType(v) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self._normalize_inlined_slot(slot_name="observations", slot_type=DimensionalObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

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
    document_type: Optional[Union[str, "CCDHDocumentDocumentType"]] = None
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

        if self.document_type is not None and not isinstance(self.document_type, CCDHDocumentDocumentType):
            self.document_type = CCDHDocumentDocumentType(self.document_type)

        if self.description is not None and not isinstance(self.description, CcdhString):
            self.description = CcdhString(self.description)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.url is None:
            self.url = []
        if not isinstance(self.url, list):
            self.url = [self.url]
        self.url = [v if isinstance(v, CcdhString) else CcdhString(v) for v in self.url]

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to an environmental factor,
    as generated through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.EnvironmentalExposureObservation
    class_class_curie: ClassVar[str] = "ccdh:EnvironmentalExposureObservation"
    class_name: ClassVar[str] = "EnvironmentalExposureObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.EnvironmentalExposureObservation

    observation_type: Union[str, "CCDHEnvironmentalExposureObservationObservationType"] = None
    valueCodeableConcept: Union[str, "CCDHEnvironmentalExposureObservationValueCodeableConcept"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHEnvironmentalExposureObservationCategory"]] = None
    method_type: Optional[Union[str, "CCDHEnvironmentalExposureObservationMethodType"]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, "Organization"]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[int, CcdhInteger]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHEnvironmentalExposureObservationObservationType):
            self.observation_type = CCDHEnvironmentalExposureObservationObservationType(self.observation_type)

        if self.valueCodeableConcept is None:
            raise ValueError("valueCodeableConcept must be supplied")
        if not isinstance(self.valueCodeableConcept, CCDHEnvironmentalExposureObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHEnvironmentalExposureObservationValueCodeableConcept(self.valueCodeableConcept)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHEnvironmentalExposureObservationCategory):
            self.category = CCDHEnvironmentalExposureObservationCategory(self.category)

        if self.method_type is not None and not isinstance(self.method_type, CCDHEnvironmentalExposureObservationMethodType):
            self.method_type = CCDHEnvironmentalExposureObservationMethodType(self.method_type)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity()

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhInteger):
            self.valueInteger = CcdhInteger(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

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
    tobacco_exposure: Optional[Union[Union[dict, "TobaccoExposureObservation"], List[Union[dict, "TobaccoExposureObservation"]]]] = empty_list()
    alcohol_exposure: Optional[Union[Union[dict, AlcoholExposureObservation], List[Union[dict, AlcoholExposureObservation]]]] = empty_list()
    environmental_exposure: Optional[Union[Union[dict, EnvironmentalExposureObservation], List[Union[dict, EnvironmentalExposureObservation]]]] = empty_list()
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

        if self.tobacco_exposure is None:
            self.tobacco_exposure = []
        if not isinstance(self.tobacco_exposure, list):
            self.tobacco_exposure = [self.tobacco_exposure]
        self._normalize_inlined_slot(slot_name="tobacco_exposure", slot_type=TobaccoExposureObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.alcohol_exposure is None:
            self.alcohol_exposure = []
        if not isinstance(self.alcohol_exposure, list):
            self.alcohol_exposure = [self.alcohol_exposure]
        self._normalize_inlined_slot(slot_name="alcohol_exposure", slot_type=AlcoholExposureObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.environmental_exposure is None:
            self.environmental_exposure = []
        if not isinstance(self.environmental_exposure, list):
            self.environmental_exposure = [self.environmental_exposure]
        self._normalize_inlined_slot(slot_name="environmental_exposure", slot_type=EnvironmentalExposureObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

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
    type: Optional[Union[str, "CCDHIdentifierType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is None:
            raise ValueError("value must be supplied")
        if not isinstance(self.value, CcdhString):
            self.value = CcdhString(self.value)

        if self.system is not None and not isinstance(self.system, CcdhString):
            self.system = CcdhString(self.system)

        if self.type is not None and not isinstance(self.type, CCDHIdentifierType):
            self.type = CCDHIdentifierType(self.type)

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

    observation_type: Union[str, "CCDHObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHObservationCategory"]] = None
    method_type: Optional[Union[Union[str, "CCDHObservationMethodType"], List[Union[str, "CCDHObservationMethodType"]]]] = empty_list()
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
    valueCodeableConcept: Optional[Union[str, "CCDHObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHObservationObservationType):
            self.observation_type = CCDHObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHObservationCategory):
            self.category = CCDHObservationCategory(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHObservationMethodType) else CCDHObservationMethodType(v) for v in self.method_type]

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
            self.valueEntity = Entity()

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

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHObservationValueCodeableConcept(self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class ObservationSet(Entity):
    """
    A structured object to hold related data items about an entity, as generated through a point-in-time observation,
    measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ObservationSet
    class_class_curie: ClassVar[str] = "ccdh:ObservationSet"
    class_name: ClassVar[str] = "ObservationSet"
    class_model_uri: ClassVar[URIRef] = CCDH.ObservationSet

    id: Union[str, CcdhString] = None
    category: Union[str, "CCDHObservationSetCategory"] = None
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "CCDHObservationSetMethodType"], List[Union[str, "CCDHObservationSetMethodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        if not isinstance(self.category, CCDHObservationSetCategory):
            self.category = CCDHObservationSetCategory(self.category)

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHObservationSetMethodType) else CCDHObservationSetMethodType(v) for v in self.method_type]

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.observations is None:
            self.observations = []
        if not isinstance(self.observations, list):
            self.observations = [self.observations]
        self._normalize_inlined_slot(slot_name="observations", slot_type=Observation, key_name="observation_type", inlined_as_list=True, keyed=False)

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
    valueCodeableConcept: Optional[Union[str, "CCDHQuantityValueCodeableConcept"]] = None
    unit: Optional[Union[str, "CCDHQuantityUnit"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHQuantityValueCodeableConcept):
            self.valueCodeableConcept = CCDHQuantityValueCodeableConcept(self.valueCodeableConcept)

        if self.unit is not None and not isinstance(self.unit, CCDHQuantityUnit):
            self.unit = CCDHQuantityUnit(self.unit)

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

    research_project_type: Union[str, "CCDHResearchProjectResearchProjectType"] = None
    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[Union[str, CcdhString]] = None
    name_shortened: Optional[Union[str, CcdhString]] = None
    description: Optional[Union[str, CcdhString]] = None
    description_shortened: Optional[Union[str, CcdhString]] = None
    sponsor: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    date_started: Optional[Union[str, CcdhDateTime]] = None
    date_ended: Optional[Union[str, CcdhDateTime]] = None
    primary_anatomic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
    url: Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ResearchProject"], List[Union[dict, "ResearchProject"]]]] = empty_list()
    date_iacuc_approval: Optional[Union[str, CcdhDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.research_project_type is None:
            raise ValueError("research_project_type must be supplied")
        if not isinstance(self.research_project_type, CCDHResearchProjectResearchProjectType):
            self.research_project_type = CCDHResearchProjectResearchProjectType(self.research_project_type)

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
        self._normalize_inlined_slot(slot_name="primary_anatomic_site", slot_type=BodySite, key_name="site", inlined_as_list=True, keyed=False)

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
    primary_diagnosis_condition: Optional[Union[str, "CCDHResearchSubjectPrimaryDiagnosisCondition"]] = None
    primary_diagnosis_site: Optional[Union[dict, BodySite]] = None
    primary_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    comorbid_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    index_timepoint: Optional[Union[str, "CCDHResearchSubjectIndexTimepoint"]] = None
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

        if self.primary_diagnosis_condition is not None and not isinstance(self.primary_diagnosis_condition, CCDHResearchSubjectPrimaryDiagnosisCondition):
            self.primary_diagnosis_condition = CCDHResearchSubjectPrimaryDiagnosisCondition(self.primary_diagnosis_condition)

        if self.primary_diagnosis_site is not None and not isinstance(self.primary_diagnosis_site, BodySite):
            self.primary_diagnosis_site = BodySite(**self.primary_diagnosis_site)

        if self.primary_diagnosis is None:
            self.primary_diagnosis = []
        if not isinstance(self.primary_diagnosis, list):
            self.primary_diagnosis = [self.primary_diagnosis]
        self.primary_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.primary_diagnosis]

        if self.comorbid_diagnosis is None:
            self.comorbid_diagnosis = []
        if not isinstance(self.comorbid_diagnosis, list):
            self.comorbid_diagnosis = [self.comorbid_diagnosis]
        self.comorbid_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.comorbid_diagnosis]

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, CCDHResearchSubjectIndexTimepoint):
            self.index_timepoint = CCDHResearchSubjectIndexTimepoint(self.index_timepoint)

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
    specimen_type: Optional[Union[str, "CCDHSpecimenSpecimenType"]] = None
    analyte_type: Optional[Union[str, "CCDHSpecimenAnalyteType"]] = None
    associated_project: Optional[Union[dict, ResearchProject]] = None
    data_provider: Optional[Union[dict, Organization]] = None
    source_material_type: Optional[Union[str, "CCDHSpecimenSourceMaterialType"]] = None
    parent_specimen: Optional[Union[Union[dict, "Specimen"], List[Union[dict, "Specimen"]]]] = empty_list()
    source_subject: Optional[Union[dict, "Subject"]] = None
    source_model_system: Optional[Union[dict, Entity]] = None
    tumor_status_at_collection: Optional[Union[str, "CCDHSpecimenTumorStatusAtCollection"]] = None
    creation_activity: Optional[Union[dict, "SpecimenCreationActivity"]] = None
    processing_activity: Optional[Union[Union[dict, "SpecimenProcessingActivity"], List[Union[dict, "SpecimenProcessingActivity"]]]] = empty_list()
    storage_activity: Optional[Union[Union[dict, "SpecimenStorageActivity"], List[Union[dict, "SpecimenStorageActivity"]]]] = empty_list()
    transport_activity: Optional[Union[Union[dict, "SpecimenTransportActivity"], List[Union[dict, "SpecimenTransportActivity"]]]] = empty_list()
    contained_in: Optional[Union[dict, "SpecimenContainer"]] = None
    dimensional_measure: Optional[Union[dict, DimensionalObservationSet]] = None
    quantity_measure: Optional[Union[Union[dict, "SpecimenQuantityObservation"], List[Union[dict, "SpecimenQuantityObservation"]]]] = empty_list()
    quality_measure: Optional[Union[Union[dict, "SpecimenQualityObservation"], List[Union[dict, "SpecimenQualityObservation"]]]] = empty_list()
    cellular_composition_type: Optional[Union[str, "CCDHSpecimenCellularCompositionType"]] = None
    histological_composition_measure: Optional[Union[Union[dict, ObservationSet], List[Union[dict, ObservationSet]]]] = empty_list()
    general_tissue_morphology: Optional[Union[str, "CCDHSpecimenGeneralTissueMorphology"]] = None
    specific_tissue_morphology: Optional[Union[str, "CCDHSpecimenSpecificTissueMorphology"]] = None
    preinvasive_tissue_morphology: Optional[Union[str, "CCDHSpecimenPreinvasiveTissueMorphology"]] = None
    morphology_pathologically_confirmed: Optional[Union[bool, CcdhBoolean]] = None
    morphology_assessor_role: Optional[Union[str, "CCDHSpecimenMorphologyAssessorRole"]] = None
    morphlogy_assessment_method: Optional[Union[str, "CCDHSpecimenMorphlogyAssessmentMethod"]] = None
    degree_of_dysplasia: Optional[Union[str, "CCDHSpecimenDegreeOfDysplasia"]] = None
    dysplasia_fraction: Optional[Union[str, CcdhString]] = None
    related_document: Optional[Union[Union[dict, Document], List[Union[dict, Document]]]] = empty_list()
    section_location: Optional[Union[str, "CCDHSpecimenSectionLocation"]] = None
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

        if self.specimen_type is not None and not isinstance(self.specimen_type, CCDHSpecimenSpecimenType):
            self.specimen_type = CCDHSpecimenSpecimenType(self.specimen_type)

        if self.analyte_type is not None and not isinstance(self.analyte_type, CCDHSpecimenAnalyteType):
            self.analyte_type = CCDHSpecimenAnalyteType(self.analyte_type)

        if self.associated_project is not None and not isinstance(self.associated_project, ResearchProject):
            self.associated_project = ResearchProject(**self.associated_project)

        if self.data_provider is not None and not isinstance(self.data_provider, Organization):
            self.data_provider = Organization(**self.data_provider)

        if self.source_material_type is not None and not isinstance(self.source_material_type, CCDHSpecimenSourceMaterialType):
            self.source_material_type = CCDHSpecimenSourceMaterialType(self.source_material_type)

        if self.parent_specimen is None:
            self.parent_specimen = []
        if not isinstance(self.parent_specimen, list):
            self.parent_specimen = [self.parent_specimen]
        self.parent_specimen = [v if isinstance(v, Specimen) else Specimen(**v) for v in self.parent_specimen]

        if self.source_subject is not None and not isinstance(self.source_subject, Subject):
            self.source_subject = Subject(**self.source_subject)

        if self.source_model_system is not None and not isinstance(self.source_model_system, Entity):
            self.source_model_system = Entity()

        if self.tumor_status_at_collection is not None and not isinstance(self.tumor_status_at_collection, CCDHSpecimenTumorStatusAtCollection):
            self.tumor_status_at_collection = CCDHSpecimenTumorStatusAtCollection(self.tumor_status_at_collection)

        if self.creation_activity is not None and not isinstance(self.creation_activity, SpecimenCreationActivity):
            self.creation_activity = SpecimenCreationActivity(**self.creation_activity)

        if self.processing_activity is None:
            self.processing_activity = []
        if not isinstance(self.processing_activity, list):
            self.processing_activity = [self.processing_activity]
        self.processing_activity = [v if isinstance(v, SpecimenProcessingActivity) else SpecimenProcessingActivity(**v) for v in self.processing_activity]

        if self.storage_activity is None:
            self.storage_activity = []
        if not isinstance(self.storage_activity, list):
            self.storage_activity = [self.storage_activity]
        self.storage_activity = [v if isinstance(v, SpecimenStorageActivity) else SpecimenStorageActivity(**v) for v in self.storage_activity]

        if self.transport_activity is None:
            self.transport_activity = []
        if not isinstance(self.transport_activity, list):
            self.transport_activity = [self.transport_activity]
        self.transport_activity = [v if isinstance(v, SpecimenTransportActivity) else SpecimenTransportActivity(**v) for v in self.transport_activity]

        if self.contained_in is not None and not isinstance(self.contained_in, SpecimenContainer):
            self.contained_in = SpecimenContainer(**self.contained_in)

        if self.dimensional_measure is not None and not isinstance(self.dimensional_measure, DimensionalObservationSet):
            self.dimensional_measure = DimensionalObservationSet(**self.dimensional_measure)

        if self.quantity_measure is None:
            self.quantity_measure = []
        if not isinstance(self.quantity_measure, list):
            self.quantity_measure = [self.quantity_measure]
        self._normalize_inlined_slot(slot_name="quantity_measure", slot_type=SpecimenQuantityObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.quality_measure is None:
            self.quality_measure = []
        if not isinstance(self.quality_measure, list):
            self.quality_measure = [self.quality_measure]
        self._normalize_inlined_slot(slot_name="quality_measure", slot_type=SpecimenQualityObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, CCDHSpecimenCellularCompositionType):
            self.cellular_composition_type = CCDHSpecimenCellularCompositionType(self.cellular_composition_type)

        if self.histological_composition_measure is None:
            self.histological_composition_measure = []
        if not isinstance(self.histological_composition_measure, list):
            self.histological_composition_measure = [self.histological_composition_measure]
        self._normalize_inlined_slot(slot_name="histological_composition_measure", slot_type=ObservationSet, key_name="id", inlined_as_list=True, keyed=False)

        if self.general_tissue_morphology is not None and not isinstance(self.general_tissue_morphology, CCDHSpecimenGeneralTissueMorphology):
            self.general_tissue_morphology = CCDHSpecimenGeneralTissueMorphology(self.general_tissue_morphology)

        if self.specific_tissue_morphology is not None and not isinstance(self.specific_tissue_morphology, CCDHSpecimenSpecificTissueMorphology):
            self.specific_tissue_morphology = CCDHSpecimenSpecificTissueMorphology(self.specific_tissue_morphology)

        if self.preinvasive_tissue_morphology is not None and not isinstance(self.preinvasive_tissue_morphology, CCDHSpecimenPreinvasiveTissueMorphology):
            self.preinvasive_tissue_morphology = CCDHSpecimenPreinvasiveTissueMorphology(self.preinvasive_tissue_morphology)

        if self.morphology_pathologically_confirmed is not None and not isinstance(self.morphology_pathologically_confirmed, CcdhBoolean):
            self.morphology_pathologically_confirmed = CcdhBoolean(self.morphology_pathologically_confirmed)

        if self.morphology_assessor_role is not None and not isinstance(self.morphology_assessor_role, CCDHSpecimenMorphologyAssessorRole):
            self.morphology_assessor_role = CCDHSpecimenMorphologyAssessorRole(self.morphology_assessor_role)

        if self.morphlogy_assessment_method is not None and not isinstance(self.morphlogy_assessment_method, CCDHSpecimenMorphlogyAssessmentMethod):
            self.morphlogy_assessment_method = CCDHSpecimenMorphlogyAssessmentMethod(self.morphlogy_assessment_method)

        if self.degree_of_dysplasia is not None and not isinstance(self.degree_of_dysplasia, CCDHSpecimenDegreeOfDysplasia):
            self.degree_of_dysplasia = CCDHSpecimenDegreeOfDysplasia(self.degree_of_dysplasia)

        if self.dysplasia_fraction is not None and not isinstance(self.dysplasia_fraction, CcdhString):
            self.dysplasia_fraction = CcdhString(self.dysplasia_fraction)

        if self.related_document is None:
            self.related_document = []
        if not isinstance(self.related_document, list):
            self.related_document = [self.related_document]
        self.related_document = [v if isinstance(v, Document) else Document(**v) for v in self.related_document]

        if self.section_location is not None and not isinstance(self.section_location, CCDHSpecimenSectionLocation):
            self.section_location = CCDHSpecimenSectionLocation(self.section_location)

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
    A vessel in which a specimen is held or to which it is attached - for storage or as a substrate for growth (e.g. a
    cell culture dish) or analysis (e.g. a microscope slide or 96-well plate)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenContainer
    class_class_curie: ClassVar[str] = "ccdh:SpecimenContainer"
    class_name: ClassVar[str] = "SpecimenContainer"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenContainer

    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    container_type: Optional[Union[str, "CCDHSpecimenContainerContainerType"]] = None
    container_number: Optional[Union[str, CcdhString]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    parent_container: Optional[Union[Union[dict, "SpecimenContainer"], List[Union[dict, "SpecimenContainer"]]]] = empty_list()
    charge_type: Optional[Union[str, "CCDHSpecimenContainerChargeType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.container_type is not None and not isinstance(self.container_type, CCDHSpecimenContainerContainerType):
            self.container_type = CCDHSpecimenContainerContainerType(self.container_type)

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

        if self.charge_type is not None and not isinstance(self.charge_type, CCDHSpecimenContainerChargeType):
            self.charge_type = CCDHSpecimenContainerChargeType(self.charge_type)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenCreationActivity(Entity):
    """
    The process of creating a specimen. This may occur through observing and/or collecting material from an biological
    source or natural setting, or through derivation from an existing specimen (e.g. via portioning or aliquoting).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenCreationActivity"
    class_name: ClassVar[str] = "SpecimenCreationActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity

    activity_type: Optional[Union[str, "CCDHSpecimenCreationActivityActivityType"]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    collection_method_type: Optional[Union[str, "CCDHSpecimenCreationActivityCollectionMethodType"]] = None
    derivation_method_type: Optional[Union[str, "CCDHSpecimenCreationActivityDerivationMethodType"]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    collection_site: Optional[Union[dict, BodySite]] = None
    quantity_collected: Optional[Union[dict, Quantity]] = None
    execution_observation: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    specimen_order: Optional[Union[int, CcdhInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CCDHSpecimenCreationActivityActivityType):
            self.activity_type = CCDHSpecimenCreationActivityActivityType(self.activity_type)

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.collection_method_type is not None and not isinstance(self.collection_method_type, CCDHSpecimenCreationActivityCollectionMethodType):
            self.collection_method_type = CCDHSpecimenCreationActivityCollectionMethodType(self.collection_method_type)

        if self.derivation_method_type is not None and not isinstance(self.derivation_method_type, CCDHSpecimenCreationActivityDerivationMethodType):
            self.derivation_method_type = CCDHSpecimenCreationActivityDerivationMethodType(self.derivation_method_type)

        if self.additive is None:
            self.additive = []
        if not isinstance(self.additive, list):
            self.additive = [self.additive]
        self.additive = [v if isinstance(v, Substance) else Substance(**v) for v in self.additive]

        if self.collection_site is not None and not isinstance(self.collection_site, BodySite):
            self.collection_site = BodySite(**self.collection_site)

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, Quantity):
            self.quantity_collected = Quantity(**self.quantity_collected)

        if self.execution_observation is None:
            self.execution_observation = []
        if not isinstance(self.execution_observation, list):
            self.execution_observation = [self.execution_observation]
        self._normalize_inlined_slot(slot_name="execution_observation", slot_type=Observation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.specimen_order is not None and not isinstance(self.specimen_order, CcdhInteger):
            self.specimen_order = CcdhInteger(self.specimen_order)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenQuantityObservation(Entity):
    """
    A structured object that describes a single data item about the quantity of an entity, as generated through a
    point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenQuantityObservation
    class_class_curie: ClassVar[str] = "ccdh:SpecimenQuantityObservation"
    class_name: ClassVar[str] = "SpecimenQuantityObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenQuantityObservation

    observation_type: Union[str, "CCDHSpecimenQuantityObservationObservationType"] = None
    valueQuantity: Union[dict, Quantity] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHSpecimenQuantityObservationCategory"]] = None
    method_type: Optional[Union[Union[str, "CCDHSpecimenQuantityObservationMethodType"], List[Union[str, "CCDHSpecimenQuantityObservationMethodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[Decimal, CcdhDecimal]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueCodeableConcept: Optional[Union[str, "CCDHSpecimenQuantityObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHSpecimenQuantityObservationObservationType):
            self.observation_type = CCDHSpecimenQuantityObservationObservationType(self.observation_type)

        if self.valueQuantity is None:
            raise ValueError("valueQuantity must be supplied")
        if not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHSpecimenQuantityObservationCategory):
            self.category = CCDHSpecimenQuantityObservationCategory(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHSpecimenQuantityObservationMethodType) else CCDHSpecimenQuantityObservationMethodType(v) for v in self.method_type]

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
            self.valueEntity = Entity()

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

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHSpecimenQuantityObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHSpecimenQuantityObservationValueCodeableConcept(self.valueCodeableConcept)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenQualityObservation(Entity):
    """
    A structured object that describes a characteristic of a specimen indicative of its quality or suitability for
    use, as generated through a point-in-time observation or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenQualityObservation
    class_class_curie: ClassVar[str] = "ccdh:SpecimenQualityObservation"
    class_name: ClassVar[str] = "SpecimenQualityObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenQualityObservation

    observation_type: Union[str, "CCDHSpecimenQualityObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHSpecimenQualityObservationCategory"]] = None
    method_type: Optional[Union[Union[str, "CCDHSpecimenQualityObservationMethodType"], List[Union[str, "CCDHSpecimenQualityObservationMethodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[Decimal, CcdhDecimal]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHSpecimenQualityObservationObservationType):
            self.observation_type = CCDHSpecimenQualityObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHSpecimenQualityObservationCategory):
            self.category = CCDHSpecimenQualityObservationCategory(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, CCDHSpecimenQualityObservationMethodType) else CCDHSpecimenQualityObservationMethodType(v) for v in self.method_type]

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
            self.valueEntity = Entity()

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

    activity_type: Optional[Union[str, "CCDHSpecimenProcessingActivityActivityType"]] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    duration: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    performed_by: Optional[Union[dict, Organization]] = None
    method_type: Optional[Union[str, "CCDHSpecimenProcessingActivityMethodType"]] = None
    additive: Optional[Union[Union[dict, "Substance"], List[Union[dict, "Substance"]]]] = empty_list()
    execution_observation: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity_type is not None and not isinstance(self.activity_type, CCDHSpecimenProcessingActivityActivityType):
            self.activity_type = CCDHSpecimenProcessingActivityActivityType(self.activity_type)

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

        if self.method_type is not None and not isinstance(self.method_type, CCDHSpecimenProcessingActivityMethodType):
            self.method_type = CCDHSpecimenProcessingActivityMethodType(self.method_type)

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
    method_type: Optional[Union[str, "CCDHSpecimenStorageActivityMethodType"]] = None
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

        if self.method_type is not None and not isinstance(self.method_type, CCDHSpecimenStorageActivityMethodType):
            self.method_type = CCDHSpecimenStorageActivityMethodType(self.method_type)

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
    species: Optional[Union[str, "CCDHSubjectSpecies"]] = None
    breed: Optional[Union[str, "CCDHSubjectBreed"]] = None
    sex: Optional[Union[str, "CCDHSubjectSex"]] = None
    ethnicity: Optional[Union[str, "CCDHSubjectEthnicity"]] = None
    race: Optional[Union[Union[str, "CCDHSubjectRace"], List[Union[str, "CCDHSubjectRace"]]]] = empty_list()
    year_of_birth: Optional[Union[int, CcdhInteger]] = None
    vital_status: Optional[Union[str, "CCDHSubjectVitalStatus"]] = None
    age_at_death: Optional[Union[dict, Quantity]] = None
    year_of_death: Optional[Union[int, CcdhInteger]] = None
    cause_of_death: Optional[Union[str, "CCDHSubjectCauseOfDeath"]] = None

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

        if self.species is not None and not isinstance(self.species, CCDHSubjectSpecies):
            self.species = CCDHSubjectSpecies(self.species)

        if self.breed is not None and not isinstance(self.breed, CCDHSubjectBreed):
            self.breed = CCDHSubjectBreed(self.breed)

        if self.sex is not None and not isinstance(self.sex, CCDHSubjectSex):
            self.sex = CCDHSubjectSex(self.sex)

        if self.ethnicity is not None and not isinstance(self.ethnicity, CCDHSubjectEthnicity):
            self.ethnicity = CCDHSubjectEthnicity(self.ethnicity)

        if self.race is None:
            self.race = []
        if not isinstance(self.race, list):
            self.race = [self.race]
        self.race = [v if isinstance(v, CCDHSubjectRace) else CCDHSubjectRace(v) for v in self.race]

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, CcdhInteger):
            self.year_of_birth = CcdhInteger(self.year_of_birth)

        if self.vital_status is not None and not isinstance(self.vital_status, CCDHSubjectVitalStatus):
            self.vital_status = CCDHSubjectVitalStatus(self.vital_status)

        if self.age_at_death is not None and not isinstance(self.age_at_death, Quantity):
            self.age_at_death = Quantity(**self.age_at_death)

        if self.year_of_death is not None and not isinstance(self.year_of_death, CcdhInteger):
            self.year_of_death = CcdhInteger(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, CCDHSubjectCauseOfDeath):
            self.cause_of_death = CCDHSubjectCauseOfDeath(self.cause_of_death)

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

    substance_type: Optional[Union[str, "CCDHSubstanceSubstanceType"]] = None
    role: Optional[Union[Union[str, "CCDHSubstanceRole"], List[Union[str, "CCDHSubstanceRole"]]]] = empty_list()
    substance_quantity: Optional[Union[dict, Quantity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.substance_type is not None and not isinstance(self.substance_type, CCDHSubstanceSubstanceType):
            self.substance_type = CCDHSubstanceSubstanceType(self.substance_type)

        if self.role is None:
            self.role = []
        if not isinstance(self.role, list):
            self.role = [self.role]
        self.role = [v if isinstance(v, CCDHSubstanceRole) else CCDHSubstanceRole(v) for v in self.role]

        if self.substance_quantity is not None and not isinstance(self.substance_quantity, Quantity):
            self.substance_quantity = Quantity(**self.substance_quantity)

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

    id: Optional[Union[str, CcdhString]] = None
    dateTime: Optional[Union[str, CcdhDateTime]] = None
    indexTimePoint: Optional[Union[dict, "TimePoint"]] = None
    offsetFromIndex: Optional[Union[dict, Quantity]] = None
    eventType: Optional[Union[Union[str, "CCDHTimePointEventType"], List[Union[str, "CCDHTimePointEventType"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.dateTime is not None and not isinstance(self.dateTime, CcdhDateTime):
            self.dateTime = CcdhDateTime(self.dateTime)

        if self.indexTimePoint is not None and not isinstance(self.indexTimePoint, TimePoint):
            self.indexTimePoint = TimePoint(**self.indexTimePoint)

        if self.offsetFromIndex is not None and not isinstance(self.offsetFromIndex, Quantity):
            self.offsetFromIndex = Quantity(**self.offsetFromIndex)

        if self.eventType is None:
            self.eventType = []
        if not isinstance(self.eventType, list):
            self.eventType = [self.eventType]
        self.eventType = [v if isinstance(v, CCDHTimePointEventType) else CCDHTimePointEventType(v) for v in self.eventType]

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
class TobaccoExposureObservation(Entity):
    """
    A structured object that describes a single data item about an individual's exposure to tobacco, as generated
    through a point-in-time observation, measurement, or interpretation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.TobaccoExposureObservation
    class_class_curie: ClassVar[str] = "ccdh:TobaccoExposureObservation"
    class_name: ClassVar[str] = "TobaccoExposureObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.TobaccoExposureObservation

    observation_type: Union[str, "CCDHTobaccoExposureObservationObservationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "CCDHTobaccoExposureObservationCategory"]] = None
    method_type: Optional[Union[str, "CCDHTobaccoExposureObservationMethodType"]] = None
    focus: Optional[Union[dict, Entity]] = None
    subject: Optional[Union[dict, Subject]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[int, CcdhInteger]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueQuantity: Optional[Union[dict, Quantity]] = None
    valueCodeableConcept: Optional[Union[str, "CCDHTobaccoExposureObservationValueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, CCDHTobaccoExposureObservationObservationType):
            self.observation_type = CCDHTobaccoExposureObservationObservationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, CCDHTobaccoExposureObservationCategory):
            self.category = CCDHTobaccoExposureObservationCategory(self.category)

        if self.method_type is not None and not isinstance(self.method_type, CCDHTobaccoExposureObservationMethodType):
            self.method_type = CCDHTobaccoExposureObservationMethodType(self.method_type)

        if self.focus is not None and not isinstance(self.focus, Entity):
            self.focus = Entity()

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.performed_by is not None and not isinstance(self.performed_by, Organization):
            self.performed_by = Organization(**self.performed_by)

        if self.valueEntity is not None and not isinstance(self.valueEntity, Entity):
            self.valueEntity = Entity()

        if self.valueString is not None and not isinstance(self.valueString, CcdhString):
            self.valueString = CcdhString(self.valueString)

        if self.valueInteger is not None and not isinstance(self.valueInteger, CcdhInteger):
            self.valueInteger = CcdhInteger(self.valueInteger)

        if self.valueDecimal is not None and not isinstance(self.valueDecimal, CcdhDecimal):
            self.valueDecimal = CcdhDecimal(self.valueDecimal)

        if self.valueBoolean is not None and not isinstance(self.valueBoolean, CcdhBoolean):
            self.valueBoolean = CcdhBoolean(self.valueBoolean)

        if self.valueDateTime is not None and not isinstance(self.valueDateTime, CcdhDateTime):
            self.valueDateTime = CcdhDateTime(self.valueDateTime)

        if self.valueQuantity is not None and not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, CCDHTobaccoExposureObservationValueCodeableConcept):
            self.valueCodeableConcept = CCDHTobaccoExposureObservationValueCodeableConcept(self.valueCodeableConcept)

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

    treatment_for_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    subject: Optional[Union[dict, Subject]] = None
    date_started: Optional[Union[dict, TimePoint]] = None
    date_ended: Optional[Union[dict, TimePoint]] = None
    id: Optional[Union[str, CcdhString]] = None
    identifier: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    regimen: Optional[Union[str, "CCDHTreatmentRegimen"]] = None
    therapeutic_agent: Optional[Union[dict, Substance]] = None
    treatment_anatomic_site: Optional[Union[dict, BodySite]] = None
    treatment_effect: Optional[Union[str, "CCDHTreatmentTreatmentEffect"]] = None
    treatment_intent: Optional[Union[str, "CCDHTreatmentTreatmentIntent"]] = None
    treatment_outcome: Optional[Union[str, "CCDHTreatmentTreatmentOutcome"]] = None
    treatment_type: Optional[Union[str, "CCDHTreatmentTreatmentType"]] = None
    treatment_frequency: Optional[Union[str, "CCDHTreatmentTreatmentFrequency"]] = None
    concurrent_treatment: Optional[Union[Union[dict, "Treatment"], List[Union[dict, "Treatment"]]]] = empty_list()
    number_of_cycles: Optional[Union[int, CcdhInteger]] = None
    treatment_end_reason: Optional[Union[Union[str, "CCDHTreatmentTreatmentEndReason"], List[Union[str, "CCDHTreatmentTreatmentEndReason"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.treatment_for_diagnosis is None:
            self.treatment_for_diagnosis = []
        if not isinstance(self.treatment_for_diagnosis, list):
            self.treatment_for_diagnosis = [self.treatment_for_diagnosis]
        self.treatment_for_diagnosis = [v if isinstance(v, Diagnosis) else Diagnosis(**v) for v in self.treatment_for_diagnosis]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.identifier is None:
            self.identifier = []
        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier]
        self._normalize_inlined_slot(slot_name="identifier", slot_type=Identifier, key_name="value", inlined_as_list=True, keyed=False)

        if self.regimen is not None and not isinstance(self.regimen, CCDHTreatmentRegimen):
            self.regimen = CCDHTreatmentRegimen(self.regimen)

        if self.therapeutic_agent is not None and not isinstance(self.therapeutic_agent, Substance):
            self.therapeutic_agent = Substance(**self.therapeutic_agent)

        if self.treatment_anatomic_site is not None and not isinstance(self.treatment_anatomic_site, BodySite):
            self.treatment_anatomic_site = BodySite(**self.treatment_anatomic_site)

        if self.treatment_effect is not None and not isinstance(self.treatment_effect, CCDHTreatmentTreatmentEffect):
            self.treatment_effect = CCDHTreatmentTreatmentEffect(self.treatment_effect)

        if self.treatment_intent is not None and not isinstance(self.treatment_intent, CCDHTreatmentTreatmentIntent):
            self.treatment_intent = CCDHTreatmentTreatmentIntent(self.treatment_intent)

        if self.treatment_outcome is not None and not isinstance(self.treatment_outcome, CCDHTreatmentTreatmentOutcome):
            self.treatment_outcome = CCDHTreatmentTreatmentOutcome(self.treatment_outcome)

        if self.treatment_type is not None and not isinstance(self.treatment_type, CCDHTreatmentTreatmentType):
            self.treatment_type = CCDHTreatmentTreatmentType(self.treatment_type)

        if self.treatment_frequency is not None and not isinstance(self.treatment_frequency, CCDHTreatmentTreatmentFrequency):
            self.treatment_frequency = CCDHTreatmentTreatmentFrequency(self.treatment_frequency)

        if self.concurrent_treatment is None:
            self.concurrent_treatment = []
        if not isinstance(self.concurrent_treatment, list):
            self.concurrent_treatment = [self.concurrent_treatment]
        self.concurrent_treatment = [v if isinstance(v, Treatment) else Treatment(**v) for v in self.concurrent_treatment]

        if self.number_of_cycles is not None and not isinstance(self.number_of_cycles, CcdhInteger):
            self.number_of_cycles = CcdhInteger(self.number_of_cycles)

        if self.treatment_end_reason is None:
            self.treatment_end_reason = []
        if not isinstance(self.treatment_end_reason, list):
            self.treatment_end_reason = [self.treatment_end_reason]
        self.treatment_end_reason = [v if isinstance(v, CCDHTreatmentTreatmentEndReason) else CCDHTreatmentTreatmentEndReason(v) for v in self.treatment_end_reason]

        super().__post_init__(**kwargs)


# Enumerations
class CCDHAlcoholExposureObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation category
    """
    _defn = EnumDefinition(
        name="CCDHAlcoholExposureObservationCategory",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:41.425006+00:00",
    )

class CCDHAlcoholExposureObservationObservationType(EnumDefinitionImpl):
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
        name="CCDHAlcoholExposureObservationObservationType",
        description="Types of observations about a Subject's exposure to alcohol.",
    )

class CCDHAlcoholExposureObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHAlcoholExposureObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:41.795152+00:00",
    )

class CCDHAlcoholExposureObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHAlcoholExposureObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:41.937510+00:00",
    )

class CCDHBodySiteSite(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite site
    """
    _defn = EnumDefinition(
        name="CCDHBodySiteSite",
        description="Autogenerated Enumeration for CRDC-H BodySite site",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.082845+00:00",
    )

class CCDHBodySiteQualifier(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite qualifier
    """
    _defn = EnumDefinition(
        name="CCDHBodySiteQualifier",
        description="Autogenerated Enumeration for CRDC-H BodySite qualifier",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.225917+00:00",
    )

class CCDHBiologicProductProductType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BiologicProduct product_type
    """
    _defn = EnumDefinition(
        name="CCDHBiologicProductProductType",
        description="Autogenerated Enumeration for CRDC-H BiologicProduct product_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.368836+00:00",
    )

class CCDHCancerGradeObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation category
    """
    _defn = EnumDefinition(
        name="CCDHCancerGradeObservationCategory",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.517581+00:00",
    )

class CCDHCancerGradeObservationObservationType(EnumDefinitionImpl):

    enneking_msts_grade = PermissibleValue(text="enneking_msts_grade",
                                                             description="The text term used to describe the surgical grade of the musculoskeletal sarcoma, using the Enneking staging system approved by the Musculoskeletal Tumor Society (MSTS).")
    esophageal_columnar_dysplasia_degree = PermissibleValue(text="esophageal_columnar_dysplasia_degree",
                                                                                               description="Text term to describe the amount of dysplasia found within the benign esophageal columnar mucosa.")
    inpc_grade = PermissibleValue(text="inpc_grade",
                                           description="Text term used to describe the classification of neuroblastic differentiation within neuroblastoma tumors, as defined by the International Neuroblastoma Pathology Classification (INPC).")
    gleason_grade_group = PermissibleValue(text="gleason_grade_group",
                                                             description="The text term used to describe the overall grouping of grades defined by the Gleason grading classification, which is used to determine the aggressiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    primary_gleason_grade = PermissibleValue(text="primary_gleason_grade",
                                                                 description="The text term used to describe the primary Gleason score, which describes the pattern of cells making up the largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggresiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    secondary_gleason_grade = PermissibleValue(text="secondary_gleason_grade",
                                                                     description="The text term used to describe the secondary Gleason score, which describes the pattern of cells making up the second largest area of the tumor. The primary and secondary Gleason pattern grades are combined to determine the patient's Gleason grade group, which is used to determine the aggresiveness of prostate cancer. Note that this grade describes the entire prostatectomy specimen and is not specific to the sample used for sequencing.")
    tumor_grade = PermissibleValue(text="tumor_grade",
                                             description="Text value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.")

    _defn = EnumDefinition(
        name="CCDHCancerGradeObservationObservationType",
    )

class CCDHCancerGradeObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHCancerGradeObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.816350+00:00",
    )

class CCDHCancerGradeObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHCancerGradeObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:42.965121+00:00",
    )

class CCDHCancerGradeObservationSetCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservationSet category
    """
    _defn = EnumDefinition(
        name="CCDHCancerGradeObservationSetCategory",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservationSet category",
        code_set=None,
        code_set_version="2021-05-30T01:20:43.108032+00:00",
    )

class CCDHCancerGradeObservationSetMethodType(EnumDefinitionImpl):
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
        name="CCDHCancerGradeObservationSetMethodType",
        description="A morphologic classification system of malignant tumors, usually relating to disease progression and clinical outcome. It is based upon the presence or absence of several morphologic parameters, including tumor cell necrosis, cytologic atypia, nuclear pleomorphism and mitotic figures, the architectural infiltrating patterns, and the degree of tumor cell differentiation. Malignant tumors usually are graded I-III",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Unspecified grading system",
                PermissibleValue(text="Unspecified grading system") )

class CCDHCancerStageObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation category
    """
    _defn = EnumDefinition(
        name="CCDHCancerStageObservationCategory",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:43.397748+00:00",
    )

class CCDHCancerStageObservationObservationType(EnumDefinitionImpl):

    Overall = PermissibleValue(text="Overall")

    _defn = EnumDefinition(
        name="CCDHCancerStageObservationObservationType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Tumor (T)",
                PermissibleValue(text="Tumor (T)") )
        setattr(cls, "Node (N)",
                PermissibleValue(text="Node (N)") )
        setattr(cls, "Metastasis (M)",
                PermissibleValue(text="Metastasis (M)") )
        setattr(cls, "Clinical Overall",
                PermissibleValue(text="Clinical Overall") )
        setattr(cls, "Clinical Tumor (T)",
                PermissibleValue(text="Clinical Tumor (T)") )
        setattr(cls, "Clinical Node (N)",
                PermissibleValue(text="Clinical Node (N)") )
        setattr(cls, "Clinical Metastasis (M)",
                PermissibleValue(text="Clinical Metastasis (M)") )
        setattr(cls, "Pathological Overall",
                PermissibleValue(text="Pathological Overall") )
        setattr(cls, "Pathological Tumor (T)",
                PermissibleValue(text="Pathological Tumor (T)") )
        setattr(cls, "Pathological Node (N)",
                PermissibleValue(text="Pathological Node (N)") )
        setattr(cls, "Pathological Metastasis (M)",
                PermissibleValue(text="Pathological Metastasis (M)") )

class CCDHCancerStageObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHCancerStageObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:43.687860+00:00",
    )

class CCDHCancerStageObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHCancerStageObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:43.827516+00:00",
    )

class CCDHCancerStageObservationSetCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservationSet category
    """
    _defn = EnumDefinition(
        name="CCDHCancerStageObservationSetCategory",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservationSet category",
        code_set=None,
        code_set_version="2021-05-30T01:20:43.974874+00:00",
    )

class CCDHCancerStageObservationSetMethodType(EnumDefinitionImpl):
    """
    Classification systems used for defining the point in the natural history of a malignant disease a patient is when
    a diagnosis is made
    """
    _defn = EnumDefinition(
        name="CCDHCancerStageObservationSetMethodType",
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

class CCDHDiagnosisCondition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis condition
    """
    Cancer = PermissibleValue(text="Cancer")
    Pneumoblastoma = PermissibleValue(text="Pneumoblastoma")
    Chorioangioma = PermissibleValue(text="Chorioangioma")
    Ganglioneuromatosis = PermissibleValue(text="Ganglioneuromatosis")
    Myofibromatosis = PermissibleValue(text="Myofibromatosis")
    Glomangiomyoma = PermissibleValue(text="Glomangiomyoma")
    Astroblastoma = PermissibleValue(text="Astroblastoma")
    Myxosarcoma = PermissibleValue(text="Myxosarcoma")
    Myelomatosis = PermissibleValue(text="Myelomatosis")
    Germinoma = PermissibleValue(text="Germinoma")
    Reticulohistiocytoma = PermissibleValue(text="Reticulohistiocytoma")
    Pituicytoma = PermissibleValue(text="Pituicytoma")
    Fibromyxoma = PermissibleValue(text="Fibromyxoma")
    Teratocarcinoma = PermissibleValue(text="Teratocarcinoma")
    Lymphangioleiomyomatosis = PermissibleValue(text="Lymphangioleiomyomatosis")
    Subependymoma = PermissibleValue(text="Subependymoma")
    RAEB = PermissibleValue(text="RAEB")
    Neurolipocytoma = PermissibleValue(text="Neurolipocytoma")
    Carcinomatosis = PermissibleValue(text="Carcinomatosis")
    Osteofibrosarcoma = PermissibleValue(text="Osteofibrosarcoma")
    Fibrochondrosarcoma = PermissibleValue(text="Fibrochondrosarcoma")
    Neurocytoma = PermissibleValue(text="Neurocytoma")
    Angiomyxoma = PermissibleValue(text="Angiomyxoma")
    Fibroliposarcoma = PermissibleValue(text="Fibroliposarcoma")
    Neurilemosarcoma = PermissibleValue(text="Neurilemosarcoma")
    Trichodiscoma = PermissibleValue(text="Trichodiscoma")
    Esthesioneuroblastoma = PermissibleValue(text="Esthesioneuroblastoma")
    Gangliocytoma = PermissibleValue(text="Gangliocytoma")
    Myxolipoma = PermissibleValue(text="Myxolipoma")
    Ependymoblastoma = PermissibleValue(text="Ependymoblastoma")
    Lymphangiosarcoma = PermissibleValue(text="Lymphangiosarcoma")
    Angioblastoma = PermissibleValue(text="Angioblastoma")
    Angioendotheliomatosis = PermissibleValue(text="Angioendotheliomatosis")
    Angiosarcoma = PermissibleValue(text="Angiosarcoma")
    Porocarcinoma = PermissibleValue(text="Porocarcinoma")
    Neurothekeoma = PermissibleValue(text="Neurothekeoma")
    Chorioadenoma = PermissibleValue(text="Chorioadenoma")
    Spermatocytoma = PermissibleValue(text="Spermatocytoma")
    Trichilemmocarcinoma = PermissibleValue(text="Trichilemmocarcinoma")
    Immunocytoma = PermissibleValue(text="Immunocytoma")
    Cholangioma = PermissibleValue(text="Cholangioma")
    Glioblastoma = PermissibleValue(text="Glioblastoma")
    Reninoma = PermissibleValue(text="Reninoma")
    Lymphangiomyomatosis = PermissibleValue(text="Lymphangiomyomatosis")
    Angioleiomyoma = PermissibleValue(text="Angioleiomyoma")
    Elastofibroma = PermissibleValue(text="Elastofibroma")
    Angiomyoma = PermissibleValue(text="Angiomyoma")
    Polyembryoma = PermissibleValue(text="Polyembryoma")
    Fibrofolliculoma = PermissibleValue(text="Fibrofolliculoma")
    Myofibroblastoma = PermissibleValue(text="Myofibroblastoma")
    Neuroastrocytoma = PermissibleValue(text="Neuroastrocytoma")
    Medullomyoblastoma = PermissibleValue(text="Medullomyoblastoma")
    Hepatocholangiocarcinoma = PermissibleValue(text="Hepatocholangiocarcinoma")
    Leiomyofibroma = PermissibleValue(text="Leiomyofibroma")
    Chemodectoma = PermissibleValue(text="Chemodectoma")
    Adenoameloblastoma = PermissibleValue(text="Adenoameloblastoma")
    Neuronevus = PermissibleValue(text="Neuronevus")
    Leiomyoblastoma = PermissibleValue(text="Leiomyoblastoma")
    Pineoblastoma = PermissibleValue(text="Pineoblastoma")
    Gemistocytoma = PermissibleValue(text="Gemistocytoma")
    Fibromyxolipoma = PermissibleValue(text="Fibromyxolipoma")
    Cholangiocarcinoma = PermissibleValue(text="Cholangiocarcinoma",
                                                           description="Cholangiocarcinoma")
    Neurofibrosarcoma = PermissibleValue(text="Neurofibrosarcoma")
    CPNET = PermissibleValue(text="CPNET")
    Chorionepithelioma = PermissibleValue(text="Chorionepithelioma")
    Lymphangiomyoma = PermissibleValue(text="Lymphangiomyoma")
    Esthesioneuroepithelioma = PermissibleValue(text="Esthesioneuroepithelioma")
    Dentinoma = PermissibleValue(text="Dentinoma")
    Lipoleiomyoma = PermissibleValue(text="Lipoleiomyoma")
    Myxoliposarcoma = PermissibleValue(text="Myxoliposarcoma")
    Hibernoma = PermissibleValue(text="Hibernoma")
    RARS = PermissibleValue(text="RARS")
    Syringofibroadenoma = PermissibleValue(text="Syringofibroadenoma")
    Pancreatoblastoma = PermissibleValue(text="Pancreatoblastoma",
                                                         description="Pancreatoblastoma")
    Pinealoma = PermissibleValue(text="Pinealoma")
    Myoepithelioma = PermissibleValue(text="Myoepithelioma")
    Gonadoblastoma = PermissibleValue(text="Gonadoblastoma")
    PPNET = PermissibleValue(text="PPNET")
    Luteinoma = PermissibleValue(text="Luteinoma")
    Parachordoma = PermissibleValue(text="Parachordoma")
    Pheochromoblastoma = PermissibleValue(text="Pheochromoblastoma")
    Trichoepithelioma = PermissibleValue(text="Trichoepithelioma")
    Craniopharyngioma = PermissibleValue(text="Craniopharyngioma")
    Ectomesenchymoma = PermissibleValue(text="Ectomesenchymoma")
    Spongioneuroblastoma = PermissibleValue(text="Spongioneuroblastoma")
    Prolactinoma = PermissibleValue(text="Prolactinoma")
    Trichilemmoma = PermissibleValue(text="Trichilemmoma")
    Ganglioneuroma = PermissibleValue(text="Ganglioneuroma")
    Sialoblastoma = PermissibleValue(text="Sialoblastoma")
    Adenolipoma = PermissibleValue(text="Adenolipoma")
    Nesidioblastoma = PermissibleValue(text="Nesidioblastoma")
    Fibromyoma = PermissibleValue(text="Fibromyoma")
    Neurinomatosis = PermissibleValue(text="Neurinomatosis")
    Myosarcoma = PermissibleValue(text="Myosarcoma")
    Adenosarcoma = PermissibleValue(text="Adenosarcoma",
                                               description="Adenosarcoma")
    Preleukemia = PermissibleValue(text="Preleukemia")
    CASTLE = PermissibleValue(text="CASTLE")
    Chloroma = PermissibleValue(text="Chloroma")
    Adenomyoma = PermissibleValue(text="Adenomyoma")
    Odontoameloblastoma = PermissibleValue(text="Odontoameloblastoma")
    Rhabdosarcoma = PermissibleValue(text="Rhabdosarcoma")
    Angioendothelioma = PermissibleValue(text="Angioendothelioma")
    Carcinofibroma = PermissibleValue(text="Carcinofibroma")
    Lipoblastoma = PermissibleValue(text="Lipoblastoma")
    Ecchondrosis = PermissibleValue(text="Ecchondrosis")
    Enchondroma = PermissibleValue(text="Enchondroma")
    Xanthofibroma = PermissibleValue(text="Xanthofibroma")
    Ganglioneuroblastoma = PermissibleValue(text="Ganglioneuroblastoma")
    Lymphoblastoma = PermissibleValue(text="Lymphoblastoma")
    Hypernephroma = PermissibleValue(text="Hypernephroma")
    Myofibroma = PermissibleValue(text="Myofibroma")
    Malignancy = PermissibleValue(text="Malignancy")
    Chorioepithelioma = PermissibleValue(text="Chorioepithelioma")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    Osteofibroma = PermissibleValue(text="Osteofibroma")
    Haemangiosarcoma = PermissibleValue(text="Haemangiosarcoma")
    M6A = PermissibleValue(text="M6A")
    Retinocytoma = PermissibleValue(text="Retinocytoma")
    Microglioma = PermissibleValue(text="Microglioma")
    Apudoma = PermissibleValue(text="Apudoma")
    Hidradenocarcinoma = PermissibleValue(text="Hidradenocarcinoma")
    GANT = PermissibleValue(text="GANT")
    Glioneuroma = PermissibleValue(text="Glioneuroma")
    Gonocytoma = PermissibleValue(text="Gonocytoma")
    Lipoblastomatosis = PermissibleValue(text="Lipoblastomatosis")
    Adenoacanthoma = PermissibleValue(text="Adenoacanthoma")
    Erythroleukemia = PermissibleValue(text="Erythroleukemia")
    Astroglioma = PermissibleValue(text="Astroglioma")
    Osteochondroma = PermissibleValue(text="Osteochondroma")
    Angiomyofibroblastoma = PermissibleValue(text="Angiomyofibroblastoma")
    Lymphoepithelioma = PermissibleValue(text="Lymphoepithelioma")
    MGUS = PermissibleValue(text="MGUS")
    Hepatocarcinoma = PermissibleValue(text="Hepatocarcinoma")
    Fibrolipoma = PermissibleValue(text="Fibrolipoma")
    Masculinovoblastoma = PermissibleValue(text="Masculinovoblastoma")
    Adenolymphoma = PermissibleValue(text="Adenolymphoma")
    Glomangioma = PermissibleValue(text="Glomangioma")
    Myelolipoma = PermissibleValue(text="Myelolipoma")
    Chromaffinoma = PermissibleValue(text="Chromaffinoma")
    MANEC = PermissibleValue(text="MANEC")
    Adenomyoepithelioma = PermissibleValue(text="Adenomyoepithelioma")
    Myoma = PermissibleValue(text="Myoma")
    Oncocytoma = PermissibleValue(text="Oncocytoma")
    Medullocytoma = PermissibleValue(text="Medullocytoma")
    Osteochondrosarcoma = PermissibleValue(text="Osteochondrosarcoma")
    SETTLE = PermissibleValue(text="SETTLE")
    Oligodendroblastoma = PermissibleValue(text="Oligodendroblastoma")
    Esthesioneurocytoma = PermissibleValue(text="Esthesioneurocytoma")
    Lipoadenoma = PermissibleValue(text="Lipoadenoma")
    Dysgerminoma = PermissibleValue(text="Dysgerminoma",
                                               description="Ovarian Dysgerminoma")
    Hidrocystoma = PermissibleValue(text="Hidrocystoma")
    Angiokeratoma = PermissibleValue(text="Angiokeratoma")
    Orchioblastoma = PermissibleValue(text="Orchioblastoma")
    Glomangiosarcoma = PermissibleValue(text="Glomangiosarcoma")
    Oligoastrocytoma = PermissibleValue(text="Oligoastrocytoma",
                                                       description="Oligoastrocytoma")
    Pineocytoma = PermissibleValue(text="Pineocytoma")
    Angiomyolipoma = PermissibleValue(text="Angiomyolipoma")
    Gliosarcoma = PermissibleValue(text="Gliosarcoma")
    M6B = PermissibleValue(text="M6B")
    Hemolymphangioma = PermissibleValue(text="Hemolymphangioma")
    Sympathicoblastoma = PermissibleValue(text="Sympathicoblastoma")
    Ecchondroma = PermissibleValue(text="Ecchondroma")
    Fibromyxosarcoma = PermissibleValue(text="Fibromyxosarcoma")
    Gliofibroma = PermissibleValue(text="Gliofibroma")
    Neurinoma = PermissibleValue(text="Neurinoma")
    Gynandroblastoma = PermissibleValue(text="Gynandroblastoma")
    Trichofolliculoma = PermissibleValue(text="Trichofolliculoma")
    Melanoameloblastoma = PermissibleValue(text="Melanoameloblastoma")
    Angiomyosarcoma = PermissibleValue(text="Angiomyosarcoma")
    Neurosarcoma = PermissibleValue(text="Neurosarcoma")
    Haemangioblastoma = PermissibleValue(text="Haemangioblastoma")
    Hepatoblastoma = PermissibleValue(text="Hepatoblastoma")

    _defn = EnumDefinition(
        name="CCDHDiagnosisCondition",
        description="Autogenerated Enumeration for CRDC-H Diagnosis condition",
        code_set=None,
        code_set_version="2021-05-30T01:20:44.257150+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Thymoma, type B1, malignant",
                PermissibleValue(text="Thymoma, type B1, malignant") )
        setattr(cls, "Mucosal lentiginous melanoma",
                PermissibleValue(text="Mucosal lentiginous melanoma") )
        setattr(cls, "Sarcoma, NOS",
                PermissibleValue(text="Sarcoma, NOS") )
        setattr(cls, "Papillary urothelial neoplasm of low malignant potential",
                PermissibleValue(text="Papillary urothelial neoplasm of low malignant potential") )
        setattr(cls, "Malignant lymphoma, centroblastic, diffuse",
                PermissibleValue(text="Malignant lymphoma, centroblastic, diffuse") )
        setattr(cls, "Acute lymphatic leukemia",
                PermissibleValue(text="Acute lymphatic leukemia") )
        setattr(cls, "Hodgkin lymphoma, lymphocyte-rich",
                PermissibleValue(text="Hodgkin lymphoma, lymphocyte-rich") )
        setattr(cls, "Carcinoma, intestinal type",
                PermissibleValue(text="Carcinoma, intestinal type") )
        setattr(cls, "Neoplasm, uncertain whether benign or malignant",
                PermissibleValue(text="Neoplasm, uncertain whether benign or malignant") )
        setattr(cls, "Myoepithelial tumor",
                PermissibleValue(text="Myoepithelial tumor") )
        setattr(cls, "Central neuroblastoma",
                PermissibleValue(text="Central neuroblastoma") )
        setattr(cls, "Mixed phenotype acute leukemia, T/myeloid, NOS",
                PermissibleValue(text="Mixed phenotype acute leukemia, T/myeloid, NOS") )
        setattr(cls, "Teratoma, differentiated",
                PermissibleValue(text="Teratoma, differentiated") )
        setattr(cls, "Lobular carcinoma, noninfiltrating",
                PermissibleValue(text="Lobular carcinoma, noninfiltrating") )
        setattr(cls, "Familial polyposis coli",
                PermissibleValue(text="Familial polyposis coli") )
        setattr(cls, "Spindle epithelial tumor with thymus-like differentiation",
                PermissibleValue(text="Spindle epithelial tumor with thymus-like differentiation") )
        setattr(cls, "Bronchial adenoma, cylindroid",
                PermissibleValue(text="Bronchial adenoma, cylindroid") )
        setattr(cls, "Endometrioid adenoma, borderline malignancy",
                PermissibleValue(text="Endometrioid adenoma, borderline malignancy") )
        setattr(cls, "Olfactory neuroblastoma",
                PermissibleValue(text="Olfactory neuroblastoma") )
        setattr(cls, "Hemangioendothelial sarcoma",
                PermissibleValue(text="Hemangioendothelial sarcoma") )
        setattr(cls, "Mixed type rhabdomyosarcoma",
                PermissibleValue(text="Mixed type rhabdomyosarcoma") )
        setattr(cls, "Low grade adenosquamous carcinoma",
                PermissibleValue(text="Low grade adenosquamous carcinoma") )
        setattr(cls, "Large cell carcinoma, NOS",
                PermissibleValue(text="Large cell carcinoma, NOS") )
        setattr(cls, "Carcinoma, anaplastic, NOS",
                PermissibleValue(text="Carcinoma, anaplastic, NOS") )
        setattr(cls, "Neurofibroma, NOS",
                PermissibleValue(text="Neurofibroma, NOS") )
        setattr(cls, "Metaplastic carcinoma, NOS",
                PermissibleValue(text="Metaplastic carcinoma, NOS") )
        setattr(cls, "Achromic nevus",
                PermissibleValue(text="Achromic nevus") )
        setattr(cls, "Tubular carcinoma",
                PermissibleValue(text="Tubular carcinoma") )
        setattr(cls, "Serous cystadenofibroma, NOS",
                PermissibleValue(text="Serous cystadenofibroma, NOS") )
        setattr(cls, "Lipid-rich urothelial carcinoma",
                PermissibleValue(text="Lipid-rich urothelial carcinoma") )
        setattr(cls, "Ganglioglioma, NOS",
                PermissibleValue(text="Ganglioglioma, NOS") )
        setattr(cls, "Endometrial stromal nodule",
                PermissibleValue(text="Endometrial stromal nodule") )
        setattr(cls, "Epidermoid carcinoma, NOS",
                PermissibleValue(text="Epidermoid carcinoma, NOS") )
        setattr(cls, "Ovarian stromal tumor",
                PermissibleValue(text="Ovarian stromal tumor") )
        setattr(cls, "Large cell (Ki-1+) lymphoma",
                PermissibleValue(text="Large cell (Ki-1+) lymphoma") )
        setattr(cls, "Balloon cell melanoma",
                PermissibleValue(text="Balloon cell melanoma") )
        setattr(cls, "Retinoblastoma, NOS",
                PermissibleValue(text="Retinoblastoma, NOS") )
        setattr(cls, "Malignant reticulosis, NOS",
                PermissibleValue(text="Malignant reticulosis, NOS") )
        setattr(cls, "Colloid adenoma",
                PermissibleValue(text="Colloid adenoma") )
        setattr(cls, "Vaginal intraepithelial neoplasia, grade III",
                PermissibleValue(text="Vaginal intraepithelial neoplasia, grade III") )
        setattr(cls, "Reticulum cell sarcoma, NOS",
                PermissibleValue(text="Reticulum cell sarcoma, NOS") )
        setattr(cls, "Jadassohn blue nevus",
                PermissibleValue(text="Jadassohn blue nevus") )
        setattr(cls, "Smooth muscle tumor, NOS",
                PermissibleValue(text="Smooth muscle tumor, NOS") )
        setattr(cls, "Serous borderline tumor-micropapillary variant",
                PermissibleValue(text="Serous borderline tumor-micropapillary variant") )
        setattr(cls, "Bile duct adenocarcinoma",
                PermissibleValue(text="Bile duct adenocarcinoma") )
        setattr(cls, "Intraductal papillary carcinoma",
                PermissibleValue(text="Intraductal papillary carcinoma") )
        setattr(cls, "Tubulocystic renal cell carcinoma",
                PermissibleValue(text="Tubulocystic renal cell carcinoma",
                                 description="Tubulocystic Renal Cell Carcinoma") )
        setattr(cls, "Mucinous adenofibroma of borderline malignancy",
                PermissibleValue(text="Mucinous adenofibroma of borderline malignancy") )
        setattr(cls, "Leukemia, NOS",
                PermissibleValue(text="Leukemia, NOS") )
        setattr(cls, "Metastasizing leiomyoma",
                PermissibleValue(text="Metastasizing leiomyoma") )
        setattr(cls, "Kupffer cell sarcoma",
                PermissibleValue(text="Kupffer cell sarcoma") )
        setattr(cls, "Brenner tumor, malignant",
                PermissibleValue(text="Brenner tumor, malignant") )
        setattr(cls, "Acute bilineal leukemia",
                PermissibleValue(text="Acute bilineal leukemia") )
        setattr(cls, "Noninvasive pancreatobiliary papillary neoplasm with high grade dysplasia",
                PermissibleValue(text="Noninvasive pancreatobiliary papillary neoplasm with high grade dysplasia") )
        setattr(cls, "Nodular hidradenoma",
                PermissibleValue(text="Nodular hidradenoma") )
        setattr(cls, "Adenocarcinoma with mixed subtypes",
                PermissibleValue(text="Adenocarcinoma with mixed subtypes") )
        setattr(cls, "Acute lymphoblastic leukemia, precursor cell type",
                PermissibleValue(text="Acute lymphoblastic leukemia, precursor cell type") )
        setattr(cls, "Seminoma, anaplastic",
                PermissibleValue(text="Seminoma, anaplastic") )
        setattr(cls, "Hepatocellular carcinoma, clear cell type",
                PermissibleValue(text="Hepatocellular carcinoma, clear cell type") )
        setattr(cls, "Transitional pineal tumor",
                PermissibleValue(text="Transitional pineal tumor") )
        setattr(cls, "Squamous cell carcinoma, keratinizing, NOS",
                PermissibleValue(text="Squamous cell carcinoma, keratinizing, NOS") )
        setattr(cls, "Undifferentiated uterine sarcoma",
                PermissibleValue(text="Undifferentiated uterine sarcoma") )
        setattr(cls, "Neuroendocrine tumor, well differentiated",
                PermissibleValue(text="Neuroendocrine tumor, well differentiated") )
        setattr(cls, "Hodgkin sarcoma",
                PermissibleValue(text="Hodgkin sarcoma") )
        setattr(cls, "Germ cell tumors with associated hematological malignancy",
                PermissibleValue(text="Germ cell tumors with associated hematological malignancy") )
        setattr(cls, "Fetal adenoma",
                PermissibleValue(text="Fetal adenoma") )
        setattr(cls, "Endometrial stromal sarcoma, high grade",
                PermissibleValue(text="Endometrial stromal sarcoma, high grade") )
        setattr(cls, "Atypical hyperplasia/Endometrioid intraepithelial neoplasm",
                PermissibleValue(text="Atypical hyperplasia/Endometrioid intraepithelial neoplasm") )
        setattr(cls, "Precursor T-cell lymphoblastic leukemia",
                PermissibleValue(text="Precursor T-cell lymphoblastic leukemia") )
        setattr(cls, "Lymphangioma, NOS",
                PermissibleValue(text="Lymphangioma, NOS") )
        setattr(cls, "Myxoid leiomyosarcoma",
                PermissibleValue(text="Myxoid leiomyosarcoma") )
        setattr(cls, "Anaplastic large cell lymphoma, ALK positive",
                PermissibleValue(text="Anaplastic large cell lymphoma, ALK positive") )
        setattr(cls, "Endometrioid cystadenoma, NOS",
                PermissibleValue(text="Endometrioid cystadenoma, NOS") )
        setattr(cls, "Malignant peripheral nerve sheath tumor with rhabdomyoblastic differentiation",
                PermissibleValue(text="Malignant peripheral nerve sheath tumor with rhabdomyoblastic differentiation") )
        setattr(cls, "Osteoblastoma, NOS",
                PermissibleValue(text="Osteoblastoma, NOS") )
        setattr(cls, "Intraepithelial squamous cell carcinoma",
                PermissibleValue(text="Intraepithelial squamous cell carcinoma") )
        setattr(cls, "Acute monoblastic and monocytic leukemia",
                PermissibleValue(text="Acute monoblastic and monocytic leukemia") )
        setattr(cls, "Nonencapsulated sclerosing adenocarcinoma",
                PermissibleValue(text="Nonencapsulated sclerosing adenocarcinoma") )
        setattr(cls, "Circumscribed arachnoidal cerebellar sarcoma",
                PermissibleValue(text="Circumscribed arachnoidal cerebellar sarcoma") )
        setattr(cls, "Lymphoepithelioma-like carcinoma",
                PermissibleValue(text="Lymphoepithelioma-like carcinoma") )
        setattr(cls, "Fibro-osteoma",
                PermissibleValue(text="Fibro-osteoma") )
        setattr(cls, "Precursor cell lymphoblastic lymphoma, NOS",
                PermissibleValue(text="Precursor cell lymphoblastic lymphoma, NOS") )
        setattr(cls, "Neurotropic melanoma, malignant",
                PermissibleValue(text="Neurotropic melanoma, malignant") )
        setattr(cls, "Acute myeloid leukemia, inv(16)(p13;q22)",
                PermissibleValue(text="Acute myeloid leukemia, inv(16)(p13;q22)") )
        setattr(cls, "Endometrioid adenofibroma, NOS",
                PermissibleValue(text="Endometrioid adenofibroma, NOS") )
        setattr(cls, "Degenerated schwannoma",
                PermissibleValue(text="Degenerated schwannoma") )
        setattr(cls, "Neuroblastoma, NOS",
                PermissibleValue(text="Neuroblastoma, NOS") )
        setattr(cls, "Malignant lymphoma, small cell, NOS",
                PermissibleValue(text="Malignant lymphoma, small cell, NOS") )
        setattr(cls, "Malignant giant cell tumor of soft parts",
                PermissibleValue(text="Malignant giant cell tumor of soft parts") )
        setattr(cls, "Embryonal carcinoma, NOS",
                PermissibleValue(text="Embryonal carcinoma, NOS") )
        setattr(cls, "Plexiform leiomyoma",
                PermissibleValue(text="Plexiform leiomyoma") )
        setattr(cls, "VAIN III",
                PermissibleValue(text="VAIN III") )
        setattr(cls, "Adenocarcinoma with neuroendocrine differentiation",
                PermissibleValue(text="Adenocarcinoma with neuroendocrine differentiation") )
        setattr(cls, "Solid and cystic tumor",
                PermissibleValue(text="Solid and cystic tumor") )
        setattr(cls, "Ameloblastic fibroma",
                PermissibleValue(text="Ameloblastic fibroma") )
        setattr(cls, "Renomedullary fibroma",
                PermissibleValue(text="Renomedullary fibroma") )
        setattr(cls, "Pigmented basal cell carcinoma",
                PermissibleValue(text="Pigmented basal cell carcinoma") )
        setattr(cls, "Parafollicular cell carcinoma",
                PermissibleValue(text="Parafollicular cell carcinoma") )
        setattr(cls, "Acute leukemia, Burkitt type",
                PermissibleValue(text="Acute leukemia, Burkitt type") )
        setattr(cls, "Cylindrical cell papilloma",
                PermissibleValue(text="Cylindrical cell papilloma") )
        setattr(cls, "Carcinoma, diffuse type",
                PermissibleValue(text="Carcinoma, diffuse type") )
        setattr(cls, "Mixed ductal-endocrine carcinoma",
                PermissibleValue(text="Mixed ductal-endocrine carcinoma") )
        setattr(cls, "Melanotic progonoma",
                PermissibleValue(text="Melanotic progonoma") )
        setattr(cls, "Spindle cell nevus, NOS",
                PermissibleValue(text="Spindle cell nevus, NOS") )
        setattr(cls, "Acute promyelocytic leukemia, NOS",
                PermissibleValue(text="Acute promyelocytic leukemia, NOS") )
        setattr(cls, "Comedocarcinoma, noninfiltrating",
                PermissibleValue(text="Comedocarcinoma, noninfiltrating") )
        setattr(cls, "Endometrioid adenofibroma, borderline malignancy",
                PermissibleValue(text="Endometrioid adenofibroma, borderline malignancy") )
        setattr(cls, "Mucous carcinoma",
                PermissibleValue(text="Mucous carcinoma") )
        setattr(cls, "Juvenile carcinoma of breast",
                PermissibleValue(text="Juvenile carcinoma of breast") )
        setattr(cls, "Dedifferentiated chordoma",
                PermissibleValue(text="Dedifferentiated chordoma") )
        setattr(cls, "Insular carcinoma",
                PermissibleValue(text="Insular carcinoma") )
        setattr(cls, "Teratoma, benign",
                PermissibleValue(text="Teratoma, benign") )
        setattr(cls, "Blue nevus, NOS",
                PermissibleValue(text="Blue nevus, NOS") )
        setattr(cls, "Embryonal rhabdomyosarcoma, NOS",
                PermissibleValue(text="Embryonal rhabdomyosarcoma, NOS") )
        setattr(cls, "Hypereosinophilic syndrome",
                PermissibleValue(text="Hypereosinophilic syndrome") )
        setattr(cls, "Chronic lymphocytic leukemia",
                PermissibleValue(text="Chronic lymphocytic leukemia") )
        setattr(cls, "Stromal endometriosis",
                PermissibleValue(text="Stromal endometriosis") )
        setattr(cls, "Acute progressive histiocytosis X",
                PermissibleValue(text="Acute progressive histiocytosis X") )
        setattr(cls, "Melanotic MPNST",
                PermissibleValue(text="Melanotic MPNST") )
        setattr(cls, "Chromaffin tumor",
                PermissibleValue(text="Chromaffin tumor") )
        setattr(cls, "Histiocytoma, NOS",
                PermissibleValue(text="Histiocytoma, NOS") )
        setattr(cls, "Adenosquamous carcinoma",
                PermissibleValue(text="Adenosquamous carcinoma") )
        setattr(cls, "Atypical polypoid adenomyoma",
                PermissibleValue(text="Atypical polypoid adenomyoma") )
        setattr(cls, "Adult T-cell leukemia/lymphoma (HTLV-1 positive) (includes all variants)",
                PermissibleValue(text="Adult T-cell leukemia/lymphoma (HTLV-1 positive) (includes all variants)") )
        setattr(cls, "Clear cell odontogenic tumor",
                PermissibleValue(text="Clear cell odontogenic tumor") )
        setattr(cls, "Leukemic reticuloendotheliosis",
                PermissibleValue(text="Leukemic reticuloendotheliosis") )
        setattr(cls, "Histiocytic sarcoma",
                PermissibleValue(text="Histiocytic sarcoma") )
        setattr(cls, "Myelogenous leukemia, NOS",
                PermissibleValue(text="Myelogenous leukemia, NOS") )
        setattr(cls, "Pindborg tumor",
                PermissibleValue(text="Pindborg tumor") )
        setattr(cls, "Pituitary carcinoma, NOS",
                PermissibleValue(text="Pituitary carcinoma, NOS") )
        setattr(cls, "Halo nevus",
                PermissibleValue(text="Halo nevus") )
        setattr(cls, "Calcifying epithelioma of Malherbe",
                PermissibleValue(text="Calcifying epithelioma of Malherbe") )
        setattr(cls, "Follicular lymphoma, grade 2",
                PermissibleValue(text="Follicular lymphoma, grade 2") )
        setattr(cls, "Meningioma, anaplastic",
                PermissibleValue(text="Meningioma, anaplastic") )
        setattr(cls, "Eosinophilic granuloma",
                PermissibleValue(text="Eosinophilic granuloma") )
        setattr(cls, "Embryonal tumor with multilayered rosettes, NOS",
                PermissibleValue(text="Embryonal tumor with multilayered rosettes, NOS") )
        setattr(cls, "Hodgkin lymphoma, lymphocyte depletion, reticular",
                PermissibleValue(text="Hodgkin lymphoma, lymphocyte depletion, reticular") )
        setattr(cls, "Plasma cell leukemia",
                PermissibleValue(text="Plasma cell leukemia") )
        setattr(cls, "Lobular adenocarcinoma",
                PermissibleValue(text="Lobular adenocarcinoma") )
        setattr(cls, "Papillary tumor of the pineal region",
                PermissibleValue(text="Papillary tumor of the pineal region") )
        setattr(cls, "Primary diffuse large B-cell lymphoma of the CNS",
                PermissibleValue(text="Primary diffuse large B-cell lymphoma of the CNS") )
        setattr(cls, "Ductal carcinoma in situ, solid type",
                PermissibleValue(text="Ductal carcinoma in situ, solid type") )
        setattr(cls, "Epithelioma, NOS",
                PermissibleValue(text="Epithelioma, NOS") )
        setattr(cls, "Malignant melanoma in junctional nevus",
                PermissibleValue(text="Malignant melanoma in junctional nevus") )
        setattr(cls, "Chronic lymphocytic leukemia, B-cell type (includes all variants of BCLL)",
                PermissibleValue(text="Chronic lymphocytic leukemia, B-cell type (includes all variants of BCLL)") )
        setattr(cls, "Fibrillary astrocytoma",
                PermissibleValue(text="Fibrillary astrocytoma") )
        setattr(cls, "Poorly cohesive carcinoma",
                PermissibleValue(text="Poorly cohesive carcinoma") )
        setattr(cls, "Endometrioid cystadenofibroma, NOS",
                PermissibleValue(text="Endometrioid cystadenofibroma, NOS") )
        setattr(cls, "Cribriform comedo-type carcinoma",
                PermissibleValue(text="Cribriform comedo-type carcinoma") )
        setattr(cls, "Tubular androblastoma, NOS",
                PermissibleValue(text="Tubular androblastoma, NOS") )
        setattr(cls, "B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and classical Hodgkin lymphoma",
                PermissibleValue(text="B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and classical Hodgkin lymphoma") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, goblet cell type",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, goblet cell type") )
        setattr(cls, "Langerhans cell histiocytosis, multifocal",
                PermissibleValue(text="Langerhans cell histiocytosis, multifocal") )
        setattr(cls, "Papillary adenofibroma",
                PermissibleValue(text="Papillary adenofibroma") )
        setattr(cls, "Giant cell tumor of tendon sheath",
                PermissibleValue(text="Giant cell tumor of tendon sheath") )
        setattr(cls, "Thymoma, lymphocytic, NOS",
                PermissibleValue(text="Thymoma, lymphocytic, NOS") )
        setattr(cls, "Malignant schwannoma, NOS",
                PermissibleValue(text="Malignant schwannoma, NOS") )
        setattr(cls, "Mixed endocrine and exocrine adenocarcinoma",
                PermissibleValue(text="Mixed endocrine and exocrine adenocarcinoma") )
        setattr(cls, "Ameloblastoma, NOS",
                PermissibleValue(text="Ameloblastoma, NOS") )
        setattr(cls, "Plexiform schwannoma",
                PermissibleValue(text="Plexiform schwannoma") )
        setattr(cls, "Mixed germ cell sex cord-stromal tumor, unclassified",
                PermissibleValue(text="Mixed germ cell sex cord-stromal tumor, unclassified") )
        setattr(cls, "Hodgkin disease, nodular sclerosis, lymphocyte depletion",
                PermissibleValue(text="Hodgkin disease, nodular sclerosis, lymphocyte depletion") )
        setattr(cls, "Mucinous cystoma",
                PermissibleValue(text="Mucinous cystoma") )
        setattr(cls, "Intraductal papillary mucinous neoplasm with an associated invasive carcinoma",
                PermissibleValue(text="Intraductal papillary mucinous neoplasm with an associated invasive carcinoma") )
        setattr(cls, "Chronic myelomonocytic leukemia in transformation",
                PermissibleValue(text="Chronic myelomonocytic leukemia in transformation") )
        setattr(cls, "Solitary plasmacytoma",
                PermissibleValue(text="Solitary plasmacytoma") )
        setattr(cls, "Fetal rhabdomyoma",
                PermissibleValue(text="Fetal rhabdomyoma") )
        setattr(cls, "Transitional cell papilloma, NOS",
                PermissibleValue(text="Transitional cell papilloma, NOS") )
        setattr(cls, "Carcinoid tumor, NOS, of appendix",
                PermissibleValue(text="Carcinoid tumor, NOS, of appendix") )
        setattr(cls, "Cortical T ALL",
                PermissibleValue(text="Cortical T ALL") )
        setattr(cls, "Mesonephroma, NOS",
                PermissibleValue(text="Mesonephroma, NOS") )
        setattr(cls, "Papillary carcinoma, diffuse sclerosing",
                PermissibleValue(text="Papillary carcinoma, diffuse sclerosing") )
        setattr(cls, "Gastrointestinal pacemaker cell tumor",
                PermissibleValue(text="Gastrointestinal pacemaker cell tumor") )
        setattr(cls, "Acinar adenoma",
                PermissibleValue(text="Acinar adenoma") )
        setattr(cls, "Genital rhabdomyoma",
                PermissibleValue(text="Genital rhabdomyoma") )
        setattr(cls, "Thymoma, type B2, malignant",
                PermissibleValue(text="Thymoma, type B2, malignant") )
        setattr(cls, "Glioma, NOS",
                PermissibleValue(text="Glioma, NOS") )
        setattr(cls, "Therapy-related myelodysplastic syndrome, epipodophyllotoxin-related",
                PermissibleValue(text="Therapy-related myelodysplastic syndrome, epipodophyllotoxin-related") )
        setattr(cls, "Giant cell tumor of tendon sheath, malignant",
                PermissibleValue(text="Giant cell tumor of tendon sheath, malignant") )
        setattr(cls, "Intraductal and lobular carcinoma",
                PermissibleValue(text="Intraductal and lobular carcinoma") )
        setattr(cls, "Papillary transitional cell carcinoma",
                PermissibleValue(text="Papillary transitional cell carcinoma") )
        setattr(cls, "Midline carcinoma of children and young adults with NUT rearrangement",
                PermissibleValue(text="Midline carcinoma of children and young adults with NUT rearrangement") )
        setattr(cls, "Eccrine poroma, malignant",
                PermissibleValue(text="Eccrine poroma, malignant") )
        setattr(cls, "Intraductal papillary adenocarcinoma, NOS",
                PermissibleValue(text="Intraductal papillary adenocarcinoma, NOS") )
        setattr(cls, "Nevus, NOS",
                PermissibleValue(text="Nevus, NOS") )
        setattr(cls, "Clear cell adenocarcinoma, mesonephroid",
                PermissibleValue(text="Clear cell adenocarcinoma, mesonephroid") )
        setattr(cls, "Meningothelial sarcoma",
                PermissibleValue(text="Meningothelial sarcoma") )
        setattr(cls, "Acute myeloid leukemia (megakaryoblastic) with t(1;22)(p13;q13); RBM15-MKL1",
                PermissibleValue(text="Acute myeloid leukemia (megakaryoblastic) with t(1;22)(p13;q13); RBM15-MKL1") )
        setattr(cls, "Juvenile chronic myelomonocytic leukemia",
                PermissibleValue(text="Juvenile chronic myelomonocytic leukemia") )
        setattr(cls, "Myelodysplastic syndrome, unclassifiable",
                PermissibleValue(text="Myelodysplastic syndrome, unclassifiable") )
        setattr(cls, "Melanocytoma, NOS",
                PermissibleValue(text="Melanocytoma, NOS") )
        setattr(cls, "Periosteal fibrosarcoma",
                PermissibleValue(text="Periosteal fibrosarcoma") )
        setattr(cls, "Villoglandular adenoma",
                PermissibleValue(text="Villoglandular adenoma") )
        setattr(cls, "Large cell carcinoma with rhabdoid phenotype",
                PermissibleValue(text="Large cell carcinoma with rhabdoid phenotype") )
        setattr(cls, "Infantile hemangioma",
                PermissibleValue(text="Infantile hemangioma") )
        setattr(cls, "Adenofibroma, NOS",
                PermissibleValue(text="Adenofibroma, NOS") )
        setattr(cls, "Mucinous cystic tumor with high-grade dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with high-grade dysplasia") )
        setattr(cls, "Dysplastic gangliocytoma of cerebellum (Lhermitte-Duclos)",
                PermissibleValue(text="Dysplastic gangliocytoma of cerebellum (Lhermitte-Duclos)") )
        setattr(cls, "Melanoma, NOS",
                PermissibleValue(text="Melanoma, NOS",
                                 description="Not Otherwise Specified Melanoma") )
        setattr(cls, "Melanotic neuroectodermal tumor",
                PermissibleValue(text="Melanotic neuroectodermal tumor") )
        setattr(cls, "Polyvesicular vitelline tumor",
                PermissibleValue(text="Polyvesicular vitelline tumor") )
        setattr(cls, "Minimally invasive adenocarcinoma, mucinous",
                PermissibleValue(text="Minimally invasive adenocarcinoma, mucinous",
                                 description="Mucinous Bronchioloalveolar Carcinoma") )
        setattr(cls, "Juxtacortical chondroma",
                PermissibleValue(text="Juxtacortical chondroma") )
        setattr(cls, "Papillary carcinoma of thyroid",
                PermissibleValue(text="Papillary carcinoma of thyroid") )
        setattr(cls, "Anaplastic large B-cell lymphoma",
                PermissibleValue(text="Anaplastic large B-cell lymphoma") )
        setattr(cls, "FAB M5 (includes all variants)",
                PermissibleValue(text="FAB M5 (includes all variants)") )
        setattr(cls, "Fetal fat cell lipoma",
                PermissibleValue(text="Fetal fat cell lipoma") )
        setattr(cls, "Angioma, NOS",
                PermissibleValue(text="Angioma, NOS") )
        setattr(cls, "Renal cell carcinoma, sarcomatoid",
                PermissibleValue(text="Renal cell carcinoma, sarcomatoid") )
        setattr(cls, "Adrenal cortical tumor, benign",
                PermissibleValue(text="Adrenal cortical tumor, benign") )
        setattr(cls, "Refractory anemia",
                PermissibleValue(text="Refractory anemia") )
        setattr(cls, "Nephroma, NOS",
                PermissibleValue(text="Nephroma, NOS") )
        setattr(cls, "Fibroid uterus",
                PermissibleValue(text="Fibroid uterus") )
        setattr(cls, "Malignant mucinous adenofibroma",
                PermissibleValue(text="Malignant mucinous adenofibroma") )
        setattr(cls, "Chronic eosinophilic leukemia, NOS",
                PermissibleValue(text="Chronic eosinophilic leukemia, NOS") )
        setattr(cls, "Metaplastic meningioma",
                PermissibleValue(text="Metaplastic meningioma") )
        setattr(cls, "Mesothelioma, biphasic, malignant",
                PermissibleValue(text="Mesothelioma, biphasic, malignant") )
        setattr(cls, "Astrocytoma, low grade",
                PermissibleValue(text="Astrocytoma, low grade") )
        setattr(cls, "Testicular adenoma",
                PermissibleValue(text="Testicular adenoma") )
        setattr(cls, "Precursor cell lymphoblastic leukemia, NOS",
                PermissibleValue(text="Precursor cell lymphoblastic leukemia, NOS") )
        setattr(cls, "Epidermoid carcinoma, keratinizing",
                PermissibleValue(text="Epidermoid carcinoma, keratinizing") )
        setattr(cls, "Invasive mole, NOS",
                PermissibleValue(text="Invasive mole, NOS") )
        setattr(cls, "Systemic mastocytosis with AHNMD",
                PermissibleValue(text="Systemic mastocytosis with AHNMD") )
        setattr(cls, "Struma ovarii, malignant",
                PermissibleValue(text="Struma ovarii, malignant") )
        setattr(cls, "Myeloid sarcoma",
                PermissibleValue(text="Myeloid sarcoma") )
        setattr(cls, "Malignant serous adenofibroma",
                PermissibleValue(text="Malignant serous adenofibroma") )
        setattr(cls, "Subacute lymphoid leukemia",
                PermissibleValue(text="Subacute lymphoid leukemia") )
        setattr(cls, "Infiltrating duct and cribriform carcinoma",
                PermissibleValue(text="Infiltrating duct and cribriform carcinoma") )
        setattr(cls, "Askin tumor",
                PermissibleValue(text="Askin tumor") )
        setattr(cls, "Verrucous epidermoid carcinoma",
                PermissibleValue(text="Verrucous epidermoid carcinoma") )
        setattr(cls, "Mixed phenotype acute leukemia, B/myeloid, NOS",
                PermissibleValue(text="Mixed phenotype acute leukemia, B/myeloid, NOS") )
        setattr(cls, "Intraductal papillomatosis, NOS",
                PermissibleValue(text="Intraductal papillomatosis, NOS") )
        setattr(cls, "Bile duct adenoma",
                PermissibleValue(text="Bile duct adenoma") )
        setattr(cls, "Partial hydatidiform mole",
                PermissibleValue(text="Partial hydatidiform mole") )
        setattr(cls, "Primary cutaneous CD8-positive aggressive epidermotropic cytotoxic T-cell lymphoma",
                PermissibleValue(text="Primary cutaneous CD8-positive aggressive epidermotropic cytotoxic T-cell lymphoma") )
        setattr(cls, "Jugulotympanic paraganglioma",
                PermissibleValue(text="Jugulotympanic paraganglioma") )
        setattr(cls, "Medulloblastoma, classic",
                PermissibleValue(text="Medulloblastoma, classic") )
        setattr(cls, "Bronchiolar carcinoma",
                PermissibleValue(text="Bronchiolar carcinoma") )
        setattr(cls, "Cystic hygroma",
                PermissibleValue(text="Cystic hygroma") )
        setattr(cls, "Infantile myofibromatosis",
                PermissibleValue(text="Infantile myofibromatosis") )
        setattr(cls, "Primitive polar spongioblastoma",
                PermissibleValue(text="Primitive polar spongioblastoma") )
        setattr(cls, "Low grade cribriform cystadenocarcinoma (LGCCC)",
                PermissibleValue(text="Low grade cribriform cystadenocarcinoma (LGCCC)") )
        setattr(cls, "Malignant chondroid syringoma",
                PermissibleValue(text="Malignant chondroid syringoma") )
        setattr(cls, "Mucinous carcinoid",
                PermissibleValue(text="Mucinous carcinoid") )
        setattr(cls, "Islet cell tumor, NOS",
                PermissibleValue(text="Islet cell tumor, NOS") )
        setattr(cls, "Fibroblastic liposarcoma",
                PermissibleValue(text="Fibroblastic liposarcoma") )
        setattr(cls, "Primary cutaneous anaplastic large cell lymphoma",
                PermissibleValue(text="Primary cutaneous anaplastic large cell lymphoma") )
        setattr(cls, "Combined small cell-adenocarcinoma",
                PermissibleValue(text="Combined small cell-adenocarcinoma") )
        setattr(cls, "Lymphoma, NOS",
                PermissibleValue(text="Lymphoma, NOS") )
        setattr(cls, "Cystic lymphangioma",
                PermissibleValue(text="Cystic lymphangioma") )
        setattr(cls, "Malignant lymphoma, mixed lymphocytic-histiocytic, nodular",
                PermissibleValue(text="Malignant lymphoma, mixed lymphocytic-histiocytic, nodular") )
        setattr(cls, "Bronchiolo-alveolar carcinoma; type II pneumocyte",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma; type II pneumocyte") )
        setattr(cls, "Interstitial cell tumor, NOS",
                PermissibleValue(text="Interstitial cell tumor, NOS") )
        setattr(cls, "Extracutaneous mastocytoma",
                PermissibleValue(text="Extracutaneous mastocytoma") )
        setattr(cls, "Sweat gland adenocarcinoma",
                PermissibleValue(text="Sweat gland adenocarcinoma") )
        setattr(cls, "Mucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Mucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Flat intraepithelial glandular neoplasia, high grade",
                PermissibleValue(text="Flat intraepithelial glandular neoplasia, high grade") )
        setattr(cls, "Odontogenic tumor, NOS",
                PermissibleValue(text="Odontogenic tumor, NOS") )
        setattr(cls, "Mixed embryonal rhabdomyosarcoma and alveolar rhabdomyosarcoma",
                PermissibleValue(text="Mixed embryonal rhabdomyosarcoma and alveolar rhabdomyosarcoma") )
        setattr(cls, "Mixed cell adenoma",
                PermissibleValue(text="Mixed cell adenoma") )
        setattr(cls, "Mucinous carcinoma",
                PermissibleValue(text="Mucinous carcinoma") )
        setattr(cls, "Combined large cell neuroendocrine carcinoma",
                PermissibleValue(text="Combined large cell neuroendocrine carcinoma") )
        setattr(cls, "Paget disease and intraductal carcinoma of breast",
                PermissibleValue(text="Paget disease and intraductal carcinoma of breast") )
        setattr(cls, "Lymphoepithelioid lymphoma",
                PermissibleValue(text="Lymphoepithelioid lymphoma") )
        setattr(cls, "Malignant tumor, giant cell type",
                PermissibleValue(text="Malignant tumor, giant cell type") )
        setattr(cls, "Leydig cell tumor, NOS",
                PermissibleValue(text="Leydig cell tumor, NOS") )
        setattr(cls, "Acute myelomonocytic leukemia with abnormal eosinophils",
                PermissibleValue(text="Acute myelomonocytic leukemia with abnormal eosinophils") )
        setattr(cls, "Malignant multilocular cystic nephroma",
                PermissibleValue(text="Malignant multilocular cystic nephroma") )
        setattr(cls, "Carcinosarcoma, embryonal",
                PermissibleValue(text="Carcinosarcoma, embryonal") )
        setattr(cls, "Encapsulated papillary carcinoma",
                PermissibleValue(text="Encapsulated papillary carcinoma") )
        setattr(cls, "Eccrine poroma",
                PermissibleValue(text="Eccrine poroma") )
        setattr(cls, "Carcinoma with osteoclast-like giant cells",
                PermissibleValue(text="Carcinoma with osteoclast-like giant cells") )
        setattr(cls, "Adenocarcinoma, diffuse type",
                PermissibleValue(text="Adenocarcinoma, diffuse type") )
        setattr(cls, "Mixed medullary-papillary carcinoma",
                PermissibleValue(text="Mixed medullary-papillary carcinoma") )
        setattr(cls, "Transitional cell papilloma, inverted, NOS",
                PermissibleValue(text="Transitional cell papilloma, inverted, NOS") )
        setattr(cls, "Cylindrical cell carcinoma",
                PermissibleValue(text="Cylindrical cell carcinoma") )
        setattr(cls, "Primary cutaneous CD30+ large T-cell lymphoma",
                PermissibleValue(text="Primary cutaneous CD30+ large T-cell lymphoma") )
        setattr(cls, "Sex cord-gonadal stromal tumor, mixed forms",
                PermissibleValue(text="Sex cord-gonadal stromal tumor, mixed forms") )
        setattr(cls, "Fibrous mesothelioma, malignant",
                PermissibleValue(text="Fibrous mesothelioma, malignant") )
        setattr(cls, "Mesonephric adenocarcinoma",
                PermissibleValue(text="Mesonephric adenocarcinoma") )
        setattr(cls, "Papillary transitional cell carcinoma, non-invasive",
                PermissibleValue(text="Papillary transitional cell carcinoma, non-invasive") )
        setattr(cls, "Malignant lymphoma, noncleaved, diffuse, NOS",
                PermissibleValue(text="Malignant lymphoma, noncleaved, diffuse, NOS") )
        setattr(cls, "Alveolar rhabdomyosarcoma",
                PermissibleValue(text="Alveolar rhabdomyosarcoma") )
        setattr(cls, "Papillary urothelial carcinoma, non-invasive",
                PermissibleValue(text="Papillary urothelial carcinoma, non-invasive") )
        setattr(cls, "Mucinous cystadenofibroma, NOS",
                PermissibleValue(text="Mucinous cystadenofibroma, NOS") )
        setattr(cls, "Myelosclerosis with myeloid metaplasia",
                PermissibleValue(text="Myelosclerosis with myeloid metaplasia") )
        setattr(cls, "Cellular angiofibroma",
                PermissibleValue(text="Cellular angiofibroma") )
        setattr(cls, "Peripheral T-cell lymphoma, pleomorphic small cell",
                PermissibleValue(text="Peripheral T-cell lymphoma, pleomorphic small cell") )
        setattr(cls, "Fibrous papule of nose",
                PermissibleValue(text="Fibrous papule of nose") )
        setattr(cls, "Glandular intraepithelial neoplasia, high grade",
                PermissibleValue(text="Glandular intraepithelial neoplasia, high grade") )
        setattr(cls, "Papillary epidermoid carcinoma",
                PermissibleValue(text="Papillary epidermoid carcinoma") )
        setattr(cls, "Intraepithelial carcinoma, NOS",
                PermissibleValue(text="Intraepithelial carcinoma, NOS") )
        setattr(cls, "Adenoid basal carcinoma",
                PermissibleValue(text="Adenoid basal carcinoma") )
        setattr(cls, "Papillary meningioma",
                PermissibleValue(text="Papillary meningioma") )
        setattr(cls, "Aleukemic myeloid leukemia",
                PermissibleValue(text="Aleukemic myeloid leukemia") )
        setattr(cls, "Pre-T ALL",
                PermissibleValue(text="Pre-T ALL") )
        setattr(cls, "Papillary mucinous cystadenocarcinoma",
                PermissibleValue(text="Papillary mucinous cystadenocarcinoma") )
        setattr(cls, "Adnexal tumor, benign",
                PermissibleValue(text="Adnexal tumor, benign") )
        setattr(cls, "DIN 3",
                PermissibleValue(text="DIN 3") )
        setattr(cls, "Mucinous tumor, NOS, of low malignant potential",
                PermissibleValue(text="Mucinous tumor, NOS, of low malignant potential") )
        setattr(cls, "Metaplastic carcinoma of no special type",
                PermissibleValue(text="Metaplastic carcinoma of no special type") )
        setattr(cls, "Nonlipid reticuloendotheliosis",
                PermissibleValue(text="Nonlipid reticuloendotheliosis") )
        setattr(cls, "Sertoli-Leydig cell tumor, well differentiated",
                PermissibleValue(text="Sertoli-Leydig cell tumor, well differentiated") )
        setattr(cls, "Plasmacytic leukemia",
                PermissibleValue(text="Plasmacytic leukemia") )
        setattr(cls, "Undifferentiated round cell sarcoma",
                PermissibleValue(text="Undifferentiated round cell sarcoma") )
        setattr(cls, "Hemangiopericytic meningioma",
                PermissibleValue(text="Hemangiopericytic meningioma") )
        setattr(cls, "Spindled mesothelioma",
                PermissibleValue(text="Spindled mesothelioma") )
        setattr(cls, "Sweat gland tumor, benign",
                PermissibleValue(text="Sweat gland tumor, benign") )
        setattr(cls, "Tumor cells, uncertain whether benign or malignant",
                PermissibleValue(text="Tumor cells, uncertain whether benign or malignant") )
        setattr(cls, "Medulloblastoma, non-WNT/non-SHH",
                PermissibleValue(text="Medulloblastoma, non-WNT/non-SHH") )
        setattr(cls, "Hepatoma, malignant",
                PermissibleValue(text="Hepatoma, malignant") )
        setattr(cls, "Systemic light chain disease",
                PermissibleValue(text="Systemic light chain disease") )
        setattr(cls, "Chronic leukemia, NOS",
                PermissibleValue(text="Chronic leukemia, NOS") )
        setattr(cls, "Malignant mucinous cystadenofibroma",
                PermissibleValue(text="Malignant mucinous cystadenofibroma") )
        setattr(cls, "Papillary carcinoma in situ",
                PermissibleValue(text="Papillary carcinoma in situ") )
        setattr(cls, "Adenocarcinoid tumor",
                PermissibleValue(text="Adenocarcinoid tumor") )
        setattr(cls, "Giant cell angiofibroma",
                PermissibleValue(text="Giant cell angiofibroma") )
        setattr(cls, "Lipid-rich Sertoli cell tumor",
                PermissibleValue(text="Lipid-rich Sertoli cell tumor") )
        setattr(cls, "Indolent systemic mastocytosis",
                PermissibleValue(text="Indolent systemic mastocytosis") )
        setattr(cls, "Cystadenoma, NOS",
                PermissibleValue(text="Cystadenoma, NOS") )
        setattr(cls, "Osteochondromatosis, NOS",
                PermissibleValue(text="Osteochondromatosis, NOS") )
        setattr(cls, "Undifferentiated epithelioid sarcoma",
                PermissibleValue(text="Undifferentiated epithelioid sarcoma") )
        setattr(cls, "Intraglandular papillary neoplasm with low grade intraepithelial neoplasia",
                PermissibleValue(text="Intraglandular papillary neoplasm with low grade intraepithelial neoplasia") )
        setattr(cls, "Hygroma, NOS",
                PermissibleValue(text="Hygroma, NOS") )
        setattr(cls, "Neuroepithelioma, NOS",
                PermissibleValue(text="Neuroepithelioma, NOS") )
        setattr(cls, "Squamous cell carcinoma in situ, NOS",
                PermissibleValue(text="Squamous cell carcinoma in situ, NOS") )
        setattr(cls, "Paget disease, extramammary",
                PermissibleValue(text="Paget disease, extramammary") )
        setattr(cls, "Squamous cell carcinoma, spindle cell",
                PermissibleValue(text="Squamous cell carcinoma, spindle cell") )
        setattr(cls, "Carcinoma, metastatic, NOS",
                PermissibleValue(text="Carcinoma, metastatic, NOS") )
        setattr(cls, "Therapy-related acute myeloid leukemia, alkylating agent related",
                PermissibleValue(text="Therapy-related acute myeloid leukemia, alkylating agent related") )
        setattr(cls, "Congenital fibrosarcoma",
                PermissibleValue(text="Congenital fibrosarcoma") )
        setattr(cls, "Squamous intraepithelial neoplasia, low grade",
                PermissibleValue(text="Squamous intraepithelial neoplasia, low grade") )
        setattr(cls, "Hodgkin granuloma",
                PermissibleValue(text="Hodgkin granuloma") )
        setattr(cls, "Systemic EBV positive T-cell lymphoproliferative disease of childhood",
                PermissibleValue(text="Systemic EBV positive T-cell lymphoproliferative disease of childhood") )
        setattr(cls, "Desmoplastic melanoma, malignant",
                PermissibleValue(text="Desmoplastic melanoma, malignant") )
        setattr(cls, "Hurthle cell adenoma",
                PermissibleValue(text="Hurthle cell adenoma") )
        setattr(cls, "EBV positive diffuse large B-cell lymphoma of the elderly",
                PermissibleValue(text="EBV positive diffuse large B-cell lymphoma of the elderly") )
        setattr(cls, "Epithelioid hemangioma",
                PermissibleValue(text="Epithelioid hemangioma") )
        setattr(cls, "Anaplastic large cell lymphoma, ALK negative",
                PermissibleValue(text="Anaplastic large cell lymphoma, ALK negative") )
        setattr(cls, "Cellular blue nevus",
                PermissibleValue(text="Cellular blue nevus") )
        setattr(cls, "Adult T-cell leukemia",
                PermissibleValue(text="Adult T-cell leukemia") )
        setattr(cls, "Alveolar cell carcinoma",
                PermissibleValue(text="Alveolar cell carcinoma") )
        setattr(cls, "Tubulopapillary adenocarcinoma",
                PermissibleValue(text="Tubulopapillary adenocarcinoma") )
        setattr(cls, "Mixed adenomatous and hyperplastic polyp",
                PermissibleValue(text="Mixed adenomatous and hyperplastic polyp") )
        setattr(cls, "Solid adenocarcinoma with mucin formation",
                PermissibleValue(text="Solid adenocarcinoma with mucin formation") )
        setattr(cls, "Acidophil adenoma",
                PermissibleValue(text="Acidophil adenoma") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma, NOS",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma, NOS") )
        setattr(cls, "Malignant myoepithelioma",
                PermissibleValue(text="Malignant myoepithelioma") )
        setattr(cls, "Langerhans cell histiocytosis, mono-ostotic",
                PermissibleValue(text="Langerhans cell histiocytosis, mono-ostotic") )
        setattr(cls, "Duct adenocarcinoma, NOS",
                PermissibleValue(text="Duct adenocarcinoma, NOS") )
        setattr(cls, "Odontogenic myxoma",
                PermissibleValue(text="Odontogenic myxoma") )
        setattr(cls, "Acute lymphoblastic leukemia, L2 type, NOS",
                PermissibleValue(text="Acute lymphoblastic leukemia, L2 type, NOS") )
        setattr(cls, "Embryonal sarcoma",
                PermissibleValue(text="Embryonal sarcoma") )
        setattr(cls, "Thecoma, luteinized",
                PermissibleValue(text="Thecoma, luteinized") )
        setattr(cls, "Endotheliomatous meningioma",
                PermissibleValue(text="Endotheliomatous meningioma") )
        setattr(cls, "Alpha heavy chain disease",
                PermissibleValue(text="Alpha heavy chain disease") )
        setattr(cls, "Lipoma, NOS",
                PermissibleValue(text="Lipoma, NOS") )
        setattr(cls, "Mediterranean lymphoma",
                PermissibleValue(text="Mediterranean lymphoma") )
        setattr(cls, "Blastic plasmacytoid dendritic cell neoplasm",
                PermissibleValue(text="Blastic plasmacytoid dendritic cell neoplasm") )
        setattr(cls, "Gonadal stromal tumor, NOS",
                PermissibleValue(text="Gonadal stromal tumor, NOS") )
        setattr(cls, "Superficial well differentiated liposarcoma",
                PermissibleValue(text="Superficial well differentiated liposarcoma") )
        setattr(cls, "Granulosa cell-theca cell tumor",
                PermissibleValue(text="Granulosa cell-theca cell tumor") )
        setattr(cls, "Clear cell (glycogen-rich) urothelial carcinoma",
                PermissibleValue(text="Clear cell (glycogen-rich) urothelial carcinoma") )
        setattr(cls, "Bizarre leiomyoma",
                PermissibleValue(text="Bizarre leiomyoma") )
        setattr(cls, "Retinal anlage tumor",
                PermissibleValue(text="Retinal anlage tumor") )
        setattr(cls, "Epithelioid and spindle cell nevus",
                PermissibleValue(text="Epithelioid and spindle cell nevus") )
        setattr(cls, "Intraductal papilloma with ductal carcinoma in situ",
                PermissibleValue(text="Intraductal papilloma with ductal carcinoma in situ") )
        setattr(cls, "Sertoli-Leydig cell tumor, sarcomatoid",
                PermissibleValue(text="Sertoli-Leydig cell tumor, sarcomatoid") )
        setattr(cls, "Nonencapsulated sclerosing carcinoma",
                PermissibleValue(text="Nonencapsulated sclerosing carcinoma") )
        setattr(cls, "Intravascular large B-cell lymphoma",
                PermissibleValue(text="Intravascular large B-cell lymphoma") )
        setattr(cls, "Invasive hydatidiform mole",
                PermissibleValue(text="Invasive hydatidiform mole") )
        setattr(cls, "Melanotic medulloblastoma",
                PermissibleValue(text="Melanotic medulloblastoma") )
        setattr(cls, "Clear cell sarcoma, of tendons and aponeuroses",
                PermissibleValue(text="Clear cell sarcoma, of tendons and aponeuroses") )
        setattr(cls, "Schneiderian papilloma, NOS",
                PermissibleValue(text="Schneiderian papilloma, NOS") )
        setattr(cls, "Arteriovenous hemangioma",
                PermissibleValue(text="Arteriovenous hemangioma") )
        setattr(cls, "Olfactory neurogenic tumor",
                PermissibleValue(text="Olfactory neurogenic tumor") )
        setattr(cls, "Oligodendroglioma, anaplastic",
                PermissibleValue(text="Oligodendroglioma, anaplastic") )
        setattr(cls, "Proliferative polycythemia",
                PermissibleValue(text="Proliferative polycythemia") )
        setattr(cls, "Endovascular papillary angioendothelioma",
                PermissibleValue(text="Endovascular papillary angioendothelioma") )
        setattr(cls, "Macrofollicular adenoma",
                PermissibleValue(text="Macrofollicular adenoma") )
        setattr(cls, "Papillary cystadenocarcinoma, NOS",
                PermissibleValue(text="Papillary cystadenocarcinoma, NOS") )
        setattr(cls, "Choroid plexus papilloma, NOS",
                PermissibleValue(text="Choroid plexus papilloma, NOS") )
        setattr(cls, "Intestinal-type adenocarcinoma",
                PermissibleValue(text="Intestinal-type adenocarcinoma") )
        setattr(cls, "Colloid carcinoma",
                PermissibleValue(text="Colloid carcinoma") )
        setattr(cls, "Invasive lobular carcinoma, alveolar type",
                PermissibleValue(text="Invasive lobular carcinoma, alveolar type") )
        setattr(cls, "Papillotubular adenoma",
                PermissibleValue(text="Papillotubular adenoma") )
        setattr(cls, "Sweat gland adenoma",
                PermissibleValue(text="Sweat gland adenoma") )
        setattr(cls, "Turban tumor",
                PermissibleValue(text="Turban tumor") )
        setattr(cls, "Mixed germ cell tumor",
                PermissibleValue(text="Mixed germ cell tumor") )
        setattr(cls, "Fibroepithelioma, NOS",
                PermissibleValue(text="Fibroepithelioma, NOS") )
        setattr(cls, "Thymoma, type C",
                PermissibleValue(text="Thymoma, type C") )
        setattr(cls, "FAB M6",
                PermissibleValue(text="FAB M6") )
        setattr(cls, "Malignant mastocytoma",
                PermissibleValue(text="Malignant mastocytoma") )
        setattr(cls, "Adenocarcinoma in situ in a polyp, NOS",
                PermissibleValue(text="Adenocarcinoma in situ in a polyp, NOS") )
        setattr(cls, "Pseudomucinous cystadenoma, NOS",
                PermissibleValue(text="Pseudomucinous cystadenoma, NOS") )
        setattr(cls, "Papillomatosis, NOS",
                PermissibleValue(text="Papillomatosis, NOS") )
        setattr(cls, "Synovioma, benign",
                PermissibleValue(text="Synovioma, benign") )
        setattr(cls, "Mixed carcinoid-adenocarcinoma",
                PermissibleValue(text="Mixed carcinoid-adenocarcinoma") )
        setattr(cls, "Odontogenic carcinosarcoma",
                PermissibleValue(text="Odontogenic carcinosarcoma") )
        setattr(cls, "Basal cell epithelioma",
                PermissibleValue(text="Basal cell epithelioma") )
        setattr(cls, "Papillary mucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Papillary mucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Intracystic papillary adenoma",
                PermissibleValue(text="Intracystic papillary adenoma") )
        setattr(cls, "Squamous cell papilloma, inverted",
                PermissibleValue(text="Squamous cell papilloma, inverted") )
        setattr(cls, "Chronic myeloproliferative disorder",
                PermissibleValue(text="Chronic myeloproliferative disorder") )
        setattr(cls, "Basosquamous carcinoma",
                PermissibleValue(text="Basosquamous carcinoma") )
        setattr(cls, "Ceruminous carcinoma",
                PermissibleValue(text="Ceruminous carcinoma") )
        setattr(cls, "Infiltrating lobular mixed with other types of carcinoma",
                PermissibleValue(text="Infiltrating lobular mixed with other types of carcinoma") )
        setattr(cls, "Malignant lymphoma, lymphocytic, intermediate differentiation, nodular",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, intermediate differentiation, nodular") )
        setattr(cls, "Solid pseudopapillary carcinoma",
                PermissibleValue(text="Solid pseudopapillary carcinoma") )
        setattr(cls, "Dermal nevus",
                PermissibleValue(text="Dermal nevus") )
        setattr(cls, "Squamous cell carcinoma, HPV-negative",
                PermissibleValue(text="Squamous cell carcinoma, HPV-negative") )
        setattr(cls, "Malignant lymphoma, small cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, small cleaved cell, NOS") )
        setattr(cls, "Primary cutaneous neuroendocrine carcinoma",
                PermissibleValue(text="Primary cutaneous neuroendocrine carcinoma") )
        setattr(cls, "Mucinous cystic tumor with an associated invasive carcinoma",
                PermissibleValue(text="Mucinous cystic tumor with an associated invasive carcinoma") )
        setattr(cls, "Malignant lymphoma, mixed small and large cell, diffuse",
                PermissibleValue(text="Malignant lymphoma, mixed small and large cell, diffuse") )
        setattr(cls, "Fibrosarcomatous dermatofibrosarcoma protuberans",
                PermissibleValue(text="Fibrosarcomatous dermatofibrosarcoma protuberans") )
        setattr(cls, "Leiomyosarcoma, NOS",
                PermissibleValue(text="Leiomyosarcoma, NOS") )
        setattr(cls, "Juvenile melanoma",
                PermissibleValue(text="Juvenile melanoma") )
        setattr(cls, "ACTH-producing tumor",
                PermissibleValue(text="ACTH-producing tumor") )
        setattr(cls, "Spindle cell angioendothelioma",
                PermissibleValue(text="Spindle cell angioendothelioma") )
        setattr(cls, "Stromal tumor with minor sex cord elements",
                PermissibleValue(text="Stromal tumor with minor sex cord elements") )
        setattr(cls, "Malignant lymphoma, small cleaved cell, diffuse",
                PermissibleValue(text="Malignant lymphoma, small cleaved cell, diffuse") )
        setattr(cls, "Urothelial papilloma, NOS",
                PermissibleValue(text="Urothelial papilloma, NOS") )
        setattr(cls, "Granular cell myoblastoma, NOS",
                PermissibleValue(text="Granular cell myoblastoma, NOS") )
        setattr(cls, "Angiomatous meningioma",
                PermissibleValue(text="Angiomatous meningioma") )
        setattr(cls, "Malignant lymphoma, large cell, cleaved and noncleaved",
                PermissibleValue(text="Malignant lymphoma, large cell, cleaved and noncleaved") )
        setattr(cls, "Mature T ALL",
                PermissibleValue(text="Mature T ALL") )
        setattr(cls, "Tubulo-papillary adenoma",
                PermissibleValue(text="Tubulo-papillary adenoma") )
        setattr(cls, "Malignant histiocytosis",
                PermissibleValue(text="Malignant histiocytosis") )
        setattr(cls, "Diffuse melanocytosis",
                PermissibleValue(text="Diffuse melanocytosis") )
        setattr(cls, "Choroid plexus papilloma, malignant",
                PermissibleValue(text="Choroid plexus papilloma, malignant") )
        setattr(cls, "Malignant melanoma, regressing",
                PermissibleValue(text="Malignant melanoma, regressing") )
        setattr(cls, "Polycythemia vera",
                PermissibleValue(text="Polycythemia vera") )
        setattr(cls, "Neuroendocrine carcinoma, poorly differentiated",
                PermissibleValue(text="Neuroendocrine carcinoma, poorly differentiated") )
        setattr(cls, "Serous cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Serous cystadenofibroma of borderline malignancy") )
        setattr(cls, "Skin appendage carcinoma",
                PermissibleValue(text="Skin appendage carcinoma") )
        setattr(cls, "Pilomatrixoma, malignant",
                PermissibleValue(text="Pilomatrixoma, malignant") )
        setattr(cls, "Diktyoma, malignant",
                PermissibleValue(text="Diktyoma, malignant") )
        setattr(cls, "Encapsulated papillary carcinoma with invasion",
                PermissibleValue(text="Encapsulated papillary carcinoma with invasion") )
        setattr(cls, "Seromucinous carcinoma",
                PermissibleValue(text="Seromucinous carcinoma",
                                 description="Ovarian Seromucinous Carcinoma") )
        setattr(cls, "Melanotic neurofibroma",
                PermissibleValue(text="Melanotic neurofibroma") )
        setattr(cls, "Intraepidermal carcinoma, NOS",
                PermissibleValue(text="Intraepidermal carcinoma, NOS") )
        setattr(cls, "Malignant schwannoma with rhabdomyoblastic differentiation",
                PermissibleValue(text="Malignant schwannoma with rhabdomyoblastic differentiation") )
        setattr(cls, "Hutchinson melanotic freckle, NOS",
                PermissibleValue(text="Hutchinson melanotic freckle, NOS") )
        setattr(cls, "Medullary carcinoma, NOS",
                PermissibleValue(text="Medullary carcinoma, NOS") )
        setattr(cls, "Mucinous adenocarcinoma, endocervical type",
                PermissibleValue(text="Mucinous adenocarcinoma, endocervical type") )
        setattr(cls, "Acoustic neuroma",
                PermissibleValue(text="Acoustic neuroma") )
        setattr(cls, "Osteogenic sarcoma, NOS",
                PermissibleValue(text="Osteogenic sarcoma, NOS") )
        setattr(cls, "Dermoid, NOS",
                PermissibleValue(text="Dermoid, NOS") )
        setattr(cls, "Noninvasive pancreatobiliary papillary neoplasm with low grade intraepithelial neoplasia",
                PermissibleValue(text="Noninvasive pancreatobiliary papillary neoplasm with low grade intraepithelial neoplasia") )
        setattr(cls, "Mucinous cystic tumor of borderline malignancy",
                PermissibleValue(text="Mucinous cystic tumor of borderline malignancy") )
        setattr(cls, "Aortic body tumor",
                PermissibleValue(text="Aortic body tumor") )
        setattr(cls, "Basal cell tumor",
                PermissibleValue(text="Basal cell tumor") )
        setattr(cls, "Combined carcinoid and adenocarcinoma",
                PermissibleValue(text="Combined carcinoid and adenocarcinoma") )
        setattr(cls, "Struma ovarii, NOS",
                PermissibleValue(text="Struma ovarii, NOS") )
        setattr(cls, "Burkitt lymphoma, NOS (Includes all variants)",
                PermissibleValue(text="Burkitt lymphoma, NOS (Includes all variants)") )
        setattr(cls, "Pilocytic astrocytoma",
                PermissibleValue(text="Pilocytic astrocytoma") )
        setattr(cls, "Osteosarcoma, NOS",
                PermissibleValue(text="Osteosarcoma, NOS") )
        setattr(cls, "Insulinoma, NOS",
                PermissibleValue(text="Insulinoma, NOS") )
        setattr(cls, "Tumor cells, malignant",
                PermissibleValue(text="Tumor cells, malignant") )
        setattr(cls, "Mucoid cell adenocarcinoma",
                PermissibleValue(text="Mucoid cell adenocarcinoma") )
        setattr(cls, "Thymoma, organoid, malignant",
                PermissibleValue(text="Thymoma, organoid, malignant") )
        setattr(cls, "Subacute lymphatic leukemia",
                PermissibleValue(text="Subacute lymphatic leukemia") )
        setattr(cls, "Refractory anemia with sideroblasts",
                PermissibleValue(text="Refractory anemia with sideroblasts") )
        setattr(cls, "Enteropathy type intestinal T-cell lymphoma",
                PermissibleValue(text="Enteropathy type intestinal T-cell lymphoma") )
        setattr(cls, "Malignant lymphoma, NOS",
                PermissibleValue(text="Malignant lymphoma, NOS") )
        setattr(cls, "Angiotropic lymphoma",
                PermissibleValue(text="Angiotropic lymphoma") )
        setattr(cls, "Extraventricular neurocytoma",
                PermissibleValue(text="Extraventricular neurocytoma") )
        setattr(cls, "Intraosseous low grade osteosarcoma",
                PermissibleValue(text="Intraosseous low grade osteosarcoma") )
        setattr(cls, "Protoplasmic astrocytoma",
                PermissibleValue(text="Protoplasmic astrocytoma") )
        setattr(cls, "Extra-abdominal desmoid",
                PermissibleValue(text="Extra-abdominal desmoid") )
        setattr(cls, "Myoepithelial adenoma",
                PermissibleValue(text="Myoepithelial adenoma") )
        setattr(cls, "Sclerosing liposarcoma",
                PermissibleValue(text="Sclerosing liposarcoma") )
        setattr(cls, "Follicular adenocarcinoma, well differentiated",
                PermissibleValue(text="Follicular adenocarcinoma, well differentiated") )
        setattr(cls, "Malignant lymphoma, large B-cell, diffuse, immunoblastic, NOS",
                PermissibleValue(text="Malignant lymphoma, large B-cell, diffuse, immunoblastic, NOS") )
        setattr(cls, "Desmoplastic infantile astrocytoma",
                PermissibleValue(text="Desmoplastic infantile astrocytoma") )
        setattr(cls, "Sarcomatosis, NOS",
                PermissibleValue(text="Sarcomatosis, NOS") )
        setattr(cls, "Mucinous cystic neoplasm with high-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with high-grade intraepithelial neoplasia") )
        setattr(cls, "Tumor, NOS",
                PermissibleValue(text="Tumor, NOS") )
        setattr(cls, "Brenner tumor, borderline malignancy",
                PermissibleValue(text="Brenner tumor, borderline malignancy") )
        setattr(cls, "Comedocarcinoma, NOS",
                PermissibleValue(text="Comedocarcinoma, NOS") )
        setattr(cls, "Lymphosarcoma, NOS",
                PermissibleValue(text="Lymphosarcoma, NOS") )
        setattr(cls, "Medulloblastoma, group 3",
                PermissibleValue(text="Medulloblastoma, group 3") )
        setattr(cls, "Endolymphatic stromal myosis",
                PermissibleValue(text="Endolymphatic stromal myosis") )
        setattr(cls, "Sertoli-Leydig cell tumor, intermediate differentiation, with heterologous elements",
                PermissibleValue(text="Sertoli-Leydig cell tumor, intermediate differentiation, with heterologous elements") )
        setattr(cls, "Precursor cell lymphoblastic leukemia, not phenotyped",
                PermissibleValue(text="Precursor cell lymphoblastic leukemia, not phenotyped") )
        setattr(cls, "Myxofibroma, NOS",
                PermissibleValue(text="Myxofibroma, NOS") )
        setattr(cls, "Mixed invasive mucinous and non-mucinous adenocarcinoma",
                PermissibleValue(text="Mixed invasive mucinous and non-mucinous adenocarcinoma") )
        setattr(cls, "Angiocentric immunoproliferative lesion",
                PermissibleValue(text="Angiocentric immunoproliferative lesion") )
        setattr(cls, "Adenocarcinoma in adenomatous polyposis coli",
                PermissibleValue(text="Adenocarcinoma in adenomatous polyposis coli") )
        setattr(cls, "Spindle cell carcinoma, NOS",
                PermissibleValue(text="Spindle cell carcinoma, NOS") )
        setattr(cls, "Mixed acinar-ductal carcinoma",
                PermissibleValue(text="Mixed acinar-ductal carcinoma",
                                 description="Mixed Acinar-Ductal Carcinoma of the Pancreas") )
        setattr(cls, "Transitional cell carcinoma, sarcomatoid",
                PermissibleValue(text="Transitional cell carcinoma, sarcomatoid") )
        setattr(cls, "Hepatoblastoma, mixed epithelial-mesenchymal",
                PermissibleValue(text="Hepatoblastoma, mixed epithelial-mesenchymal") )
        setattr(cls, "Mammary carcinoma, in situ",
                PermissibleValue(text="Mammary carcinoma, in situ") )
        setattr(cls, "Papillary syringadenoma",
                PermissibleValue(text="Papillary syringadenoma") )
        setattr(cls, "Fibroblastic meningioma",
                PermissibleValue(text="Fibroblastic meningioma") )
        setattr(cls, "Solid papillary carcinoma in situ",
                PermissibleValue(text="Solid papillary carcinoma in situ") )
        setattr(cls, "Skin appendage tumor, benign",
                PermissibleValue(text="Skin appendage tumor, benign") )
        setattr(cls, "Plasmablastic lymphoma",
                PermissibleValue(text="Plasmablastic lymphoma") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with hyperdiploidy",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with hyperdiploidy") )
        setattr(cls, "Oxyphilic adenoma",
                PermissibleValue(text="Oxyphilic adenoma") )
        setattr(cls, "Ameloblastic sarcoma",
                PermissibleValue(text="Ameloblastic sarcoma") )
        setattr(cls, "Mixed mesenchymal sarcoma",
                PermissibleValue(text="Mixed mesenchymal sarcoma") )
        setattr(cls, "Neurofibromatosis, NOS",
                PermissibleValue(text="Neurofibromatosis, NOS") )
        setattr(cls, "Neurilemoma, malignant",
                PermissibleValue(text="Neurilemoma, malignant") )
        setattr(cls, "c-ALL",
                PermissibleValue(text="c-ALL") )
        setattr(cls, "Lymphoproliferative disease, NOS",
                PermissibleValue(text="Lymphoproliferative disease, NOS") )
        setattr(cls, "Mucinous cystic neoplasm with intermediate-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with intermediate-grade intraepithelial neoplasia") )
        setattr(cls, "Chondroblastoma, NOS",
                PermissibleValue(text="Chondroblastoma, NOS") )
        setattr(cls, "Intermediate and giant congenital nevus",
                PermissibleValue(text="Intermediate and giant congenital nevus") )
        setattr(cls, "Gangliocytic paraganglioma",
                PermissibleValue(text="Gangliocytic paraganglioma") )
        setattr(cls, "Sebaceous adenocarcinoma",
                PermissibleValue(text="Sebaceous adenocarcinoma",
                                 description="Head and Neck Sebaceous Carcinoma") )
        setattr(cls, "Neuroendocrine carcinoma, moderately differentiated",
                PermissibleValue(text="Neuroendocrine carcinoma, moderately differentiated") )
        setattr(cls, "Granulosa cell carcinoma",
                PermissibleValue(text="Granulosa cell carcinoma") )
        setattr(cls, "Mature T-cell lymphoma, NOS",
                PermissibleValue(text="Mature T-cell lymphoma, NOS") )
        setattr(cls, "Glucagon-like peptide-producing tumor",
                PermissibleValue(text="Glucagon-like peptide-producing tumor") )
        setattr(cls, "Chronic lymphoproliferative disorder of NK cells",
                PermissibleValue(text="Chronic lymphoproliferative disorder of NK cells") )
        setattr(cls, "Chromaffin paraganglioma",
                PermissibleValue(text="Chromaffin paraganglioma") )
        setattr(cls, "Malignant eccrine spiradenoma",
                PermissibleValue(text="Malignant eccrine spiradenoma") )
        setattr(cls, "Pancreatobiliary-type carcinoma",
                PermissibleValue(text="Pancreatobiliary-type carcinoma") )
        setattr(cls, "Metaplastic carcinoma with osseous differentiation",
                PermissibleValue(text="Metaplastic carcinoma with osseous differentiation") )
        setattr(cls, "Enteroglucagonoma, NOS",
                PermissibleValue(text="Enteroglucagonoma, NOS") )
        setattr(cls, "Polymorphic reticulosis",
                PermissibleValue(text="Polymorphic reticulosis") )
        setattr(cls, "Primary cutaneous follicle centre lymphoma",
                PermissibleValue(text="Primary cutaneous follicle centre lymphoma") )
        setattr(cls, "Glucagonoma, NOS",
                PermissibleValue(text="Glucagonoma, NOS") )
        setattr(cls, "Parosteal osteosarcoma",
                PermissibleValue(text="Parosteal osteosarcoma") )
        setattr(cls, "Biphenotypic sinonasal sarcoma",
                PermissibleValue(text="Biphenotypic sinonasal sarcoma",
                                 description="Biphenotypic Sinonasal Sarcoma") )
        setattr(cls, "Duct cell carcinoma",
                PermissibleValue(text="Duct cell carcinoma") )
        setattr(cls, "Infiltrating basal cell carcinoma, NOS",
                PermissibleValue(text="Infiltrating basal cell carcinoma, NOS") )
        setattr(cls, "Sarcomatoid carcinoma",
                PermissibleValue(text="Sarcomatoid carcinoma") )
        setattr(cls, "Duct carcinoma, NOS",
                PermissibleValue(text="Duct carcinoma, NOS") )
        setattr(cls, "Adenocarcinoma with cartilaginous metaplasia",
                PermissibleValue(text="Adenocarcinoma with cartilaginous metaplasia") )
        setattr(cls, "Bile duct cystadenocarcinoma",
                PermissibleValue(text="Bile duct cystadenocarcinoma") )
        setattr(cls, "Schneiderian papilloma, inverted",
                PermissibleValue(text="Schneiderian papilloma, inverted") )
        setattr(cls, "Papillary mucinous tumor of low malignant potential",
                PermissibleValue(text="Papillary mucinous tumor of low malignant potential") )
        setattr(cls, "Epithelioid mesothelioma, NOS",
                PermissibleValue(text="Epithelioid mesothelioma, NOS") )
        setattr(cls, "Ewing tumor",
                PermissibleValue(text="Ewing tumor") )
        setattr(cls, "Neurilemoma, NOS",
                PermissibleValue(text="Neurilemoma, NOS") )
        setattr(cls, "Androblastoma, benign",
                PermissibleValue(text="Androblastoma, benign") )
        setattr(cls, "Non-invasive EFVPTC",
                PermissibleValue(text="Non-invasive EFVPTC") )
        setattr(cls, "Nodular melanoma",
                PermissibleValue(text="Nodular melanoma",
                                 description="Nodular Melanoma") )
        setattr(cls, "Meningiomatosis, NOS",
                PermissibleValue(text="Meningiomatosis, NOS") )
        setattr(cls, "Atypical adenoma",
                PermissibleValue(text="Atypical adenoma") )
        setattr(cls, "Scirrhous carcinoma",
                PermissibleValue(text="Scirrhous carcinoma") )
        setattr(cls, "Epithelioid MPNST",
                PermissibleValue(text="Epithelioid MPNST") )
        setattr(cls, "Mucinous cystic neoplasm with intermediate-grade dysplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with intermediate-grade dysplasia") )
        setattr(cls, "Androblastoma, malignant",
                PermissibleValue(text="Androblastoma, malignant") )
        setattr(cls, "Aorticopulmonary paraganglioma",
                PermissibleValue(text="Aorticopulmonary paraganglioma") )
        setattr(cls, "Infiltrating ductular carcinoma",
                PermissibleValue(text="Infiltrating ductular carcinoma") )
        setattr(cls, "Ependymoma, NOS",
                PermissibleValue(text="Ependymoma, NOS") )
        setattr(cls, "Malignant lymphoma, large B-cell, diffuse, NOS",
                PermissibleValue(text="Malignant lymphoma, large B-cell, diffuse, NOS") )
        setattr(cls, "Squamous cell carcinoma, acantholytic",
                PermissibleValue(text="Squamous cell carcinoma, acantholytic") )
        setattr(cls, "C cell carcinoma",
                PermissibleValue(text="C cell carcinoma") )
        setattr(cls, "Follicular dendritic cell tumor",
                PermissibleValue(text="Follicular dendritic cell tumor") )
        setattr(cls, "Bronchial adenoma, NOS",
                PermissibleValue(text="Bronchial adenoma, NOS") )
        setattr(cls, "Central primitive neuroectodermal tumor, NOS",
                PermissibleValue(text="Central primitive neuroectodermal tumor, NOS") )
        setattr(cls, "Adult rhabdomyoma",
                PermissibleValue(text="Adult rhabdomyoma") )
        setattr(cls, "Low grade appendiceal mucinous neoplasm",
                PermissibleValue(text="Low grade appendiceal mucinous neoplasm") )
        setattr(cls, "Sertoli cell carcinoma",
                PermissibleValue(text="Sertoli cell carcinoma") )
        setattr(cls, "Aleukemic myelogenous leukemia",
                PermissibleValue(text="Aleukemic myelogenous leukemia") )
        setattr(cls, "Acute biphenotypic leukemia",
                PermissibleValue(text="Acute biphenotypic leukemia") )
        setattr(cls, "Refractory thrombocytopenia",
                PermissibleValue(text="Refractory thrombocytopenia") )
        setattr(cls, "Malignant lymphoma, large cell, NOS",
                PermissibleValue(text="Malignant lymphoma, large cell, NOS") )
        setattr(cls, "Combined small cell-squamous cell carcinoma",
                PermissibleValue(text="Combined small cell-squamous cell carcinoma") )
        setattr(cls, "LCIS, NOS",
                PermissibleValue(text="LCIS, NOS") )
        setattr(cls, "Mucinous adenocarcinoma",
                PermissibleValue(text="Mucinous adenocarcinoma") )
        setattr(cls, "Localized fibrous tumor",
                PermissibleValue(text="Localized fibrous tumor") )
        setattr(cls, "Giant cell carcinoma",
                PermissibleValue(text="Giant cell carcinoma") )
        setattr(cls, "Transitional papilloma, inverted, benign",
                PermissibleValue(text="Transitional papilloma, inverted, benign") )
        setattr(cls, "Desmoplastic infantile ganglioglioma",
                PermissibleValue(text="Desmoplastic infantile ganglioglioma") )
        setattr(cls, "Noninvasive pancreatobiliary papillary neoplasm with high grade intraepithelial neoplasia",
                PermissibleValue(text="Noninvasive pancreatobiliary papillary neoplasm with high grade intraepithelial neoplasia") )
        setattr(cls, "Myloproliferative neoplasm, unclassifiable",
                PermissibleValue(text="Myloproliferative neoplasm, unclassifiable") )
        setattr(cls, "Glomus jugulare tumor, NOS",
                PermissibleValue(text="Glomus jugulare tumor, NOS") )
        setattr(cls, "Composite Hodgkin and non-Hodgkin lymphoma",
                PermissibleValue(text="Composite Hodgkin and non-Hodgkin lymphoma") )
        setattr(cls, "Thymoma, atypical, malignant",
                PermissibleValue(text="Thymoma, atypical, malignant") )
        setattr(cls, "Luteoma, NOS",
                PermissibleValue(text="Luteoma, NOS") )
        setattr(cls, "Enteric adenocarcinoma",
                PermissibleValue(text="Enteric adenocarcinoma",
                                 description="Lung Enteric Adenocarcinoma") )
        setattr(cls, "Mesothelioma, biphasic, NOS",
                PermissibleValue(text="Mesothelioma, biphasic, NOS") )
        setattr(cls, "Neuroendocrine tumor, grade 2",
                PermissibleValue(text="Neuroendocrine tumor, grade 2") )
        setattr(cls, "Clear cell hidradenoma",
                PermissibleValue(text="Clear cell hidradenoma") )
        setattr(cls, "Periapical cemental dysplasia",
                PermissibleValue(text="Periapical cemental dysplasia") )
        setattr(cls, "Papillary cystic tumor",
                PermissibleValue(text="Papillary cystic tumor") )
        setattr(cls, "Trophoblastic tumor, epithelioid",
                PermissibleValue(text="Trophoblastic tumor, epithelioid") )
        setattr(cls, "Carcinoma with neuroendocrine differentiation",
                PermissibleValue(text="Carcinoma with neuroendocrine differentiation") )
        setattr(cls, "Hidradenoma, NOS",
                PermissibleValue(text="Hidradenoma, NOS") )
        setattr(cls, "Hodgkin lymphoma, mixed cellularity, NOS",
                PermissibleValue(text="Hodgkin lymphoma, mixed cellularity, NOS") )
        setattr(cls, "Glandular intraepithelial neoplasia, grade I",
                PermissibleValue(text="Glandular intraepithelial neoplasia, grade I") )
        setattr(cls, "Endometrioid carcinoma with squamous differentiation",
                PermissibleValue(text="Endometrioid carcinoma with squamous differentiation",
                                 description="Endometrial Squamous Cell Carcinoma") )
        setattr(cls, "Apocrine adenocarcinoma",
                PermissibleValue(text="Apocrine adenocarcinoma") )
        setattr(cls, "EC cell carcinoid",
                PermissibleValue(text="EC cell carcinoid") )
        setattr(cls, "Medulloepithelioma, benign",
                PermissibleValue(text="Medulloepithelioma, benign") )
        setattr(cls, "Primary cutaneous DLBCL, leg type",
                PermissibleValue(text="Primary cutaneous DLBCL, leg type") )
        setattr(cls, "Adenocarcinoma with cartilaginous and osseous metaplasia",
                PermissibleValue(text="Adenocarcinoma with cartilaginous and osseous metaplasia") )
        setattr(cls, "FAB MO",
                PermissibleValue(text="FAB MO") )
        setattr(cls, "Chronic myelomonocytic leukemia, Type 1",
                PermissibleValue(text="Chronic myelomonocytic leukemia, Type 1") )
        setattr(cls, "Basal cell carcinoma, nodular",
                PermissibleValue(text="Basal cell carcinoma, nodular") )
        setattr(cls, "Hilus cell tumor",
                PermissibleValue(text="Hilus cell tumor") )
        setattr(cls, "Vulvar intraepithelial neoplasia, grade III",
                PermissibleValue(text="Vulvar intraepithelial neoplasia, grade III") )
        setattr(cls, "Islet cell adenocarcinoma",
                PermissibleValue(text="Islet cell adenocarcinoma") )
        setattr(cls, "Medulloblastoma with extensive nodularity",
                PermissibleValue(text="Medulloblastoma with extensive nodularity") )
        setattr(cls, "Flat adenoma",
                PermissibleValue(text="Flat adenoma") )
        setattr(cls, "Pancreatic endocrine tumor, benign",
                PermissibleValue(text="Pancreatic endocrine tumor, benign") )
        setattr(cls, "Adrenal cortical adenoma, clear cell",
                PermissibleValue(text="Adrenal cortical adenoma, clear cell") )
        setattr(cls, "Atypical proliferative papillary serous tumor",
                PermissibleValue(text="Atypical proliferative papillary serous tumor") )
        setattr(cls, "Enteroglucagonoma, malignant",
                PermissibleValue(text="Enteroglucagonoma, malignant") )
        setattr(cls, "Mixed tumor, malignant, NOS",
                PermissibleValue(text="Mixed tumor, malignant, NOS") )
        setattr(cls, "Cementoma, NOS",
                PermissibleValue(text="Cementoma, NOS") )
        setattr(cls, "Papillary cystadenoma, NOS",
                PermissibleValue(text="Papillary cystadenoma, NOS") )
        setattr(cls, "Intraductal papillary-mucinous tumor with moderate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with moderate dysplasia") )
        setattr(cls, "Stem cell leukemia",
                PermissibleValue(text="Stem cell leukemia") )
        setattr(cls, "Adrenal cortical adenoma, compact cell",
                PermissibleValue(text="Adrenal cortical adenoma, compact cell") )
        setattr(cls, "Reticulosarcoma, NOS",
                PermissibleValue(text="Reticulosarcoma, NOS") )
        setattr(cls, "Endometrioid cystadenocarcinoma",
                PermissibleValue(text="Endometrioid cystadenocarcinoma") )
        setattr(cls, "Unclassified tumor, borderline malignancy",
                PermissibleValue(text="Unclassified tumor, borderline malignancy") )
        setattr(cls, "Hodgkin disease, nodular sclerosis, mixed cellularity",
                PermissibleValue(text="Hodgkin disease, nodular sclerosis, mixed cellularity") )
        setattr(cls, "Acute myelogenous leukemia",
                PermissibleValue(text="Acute myelogenous leukemia") )
        setattr(cls, "Verrucous carcinoma, NOS",
                PermissibleValue(text="Verrucous carcinoma, NOS") )
        setattr(cls, "Squamous cell carcinoma, small cell, nonkeratinizing",
                PermissibleValue(text="Squamous cell carcinoma, small cell, nonkeratinizing") )
        setattr(cls, "Mixed acinar-endocrine-ductal carcinoma",
                PermissibleValue(text="Mixed acinar-endocrine-ductal carcinoma") )
        setattr(cls, "Osteocartilaginous exostosis",
                PermissibleValue(text="Osteocartilaginous exostosis") )
        setattr(cls, "Malignant tumor, spindle cell type",
                PermissibleValue(text="Malignant tumor, spindle cell type") )
        setattr(cls, "Brenner tumor, NOS",
                PermissibleValue(text="Brenner tumor, NOS") )
        setattr(cls, "Adenocarcinoma in tubular adenoma",
                PermissibleValue(text="Adenocarcinoma in tubular adenoma") )
        setattr(cls, "Lepidic adenocarcinoma",
                PermissibleValue(text="Lepidic adenocarcinoma") )
        setattr(cls, "Adenoma, NOS",
                PermissibleValue(text="Adenoma, NOS") )
        setattr(cls, "Angioblastic meningioma",
                PermissibleValue(text="Angioblastic meningioma") )
        setattr(cls, "T-zone lymphoma",
                PermissibleValue(text="T-zone lymphoma") )
        setattr(cls, "Acute myeloid leukemia, NOS",
                PermissibleValue(text="Acute myeloid leukemia, NOS") )
        setattr(cls, "Intracanalicular fibroadenoma",
                PermissibleValue(text="Intracanalicular fibroadenoma") )
        setattr(cls, "Papillary carcinoma, NOS",
                PermissibleValue(text="Papillary carcinoma, NOS") )
        setattr(cls, "Plexiform neuroma",
                PermissibleValue(text="Plexiform neuroma") )
        setattr(cls, "Sclerosing rhabdomyosarcoma",
                PermissibleValue(text="Sclerosing rhabdomyosarcoma") )
        setattr(cls, "Splenic marginal zone B-cell lymphoma",
                PermissibleValue(text="Splenic marginal zone B-cell lymphoma") )
        setattr(cls, "Endometrioid adenocarcinoma, ciliated cell variant",
                PermissibleValue(text="Endometrioid adenocarcinoma, ciliated cell variant") )
        setattr(cls, "Cervical intraepithelial neoplasia, grade III",
                PermissibleValue(text="Cervical intraepithelial neoplasia, grade III") )
        setattr(cls, "Mucin-secreting carcinoma",
                PermissibleValue(text="Mucin-secreting carcinoma") )
        setattr(cls, "Synovioma, malignant",
                PermissibleValue(text="Synovioma, malignant") )
        setattr(cls, "Stromal sarcoma, NOS",
                PermissibleValue(text="Stromal sarcoma, NOS") )
        setattr(cls, "Splenic diffuse red pulp small B-cell lymphoma",
                PermissibleValue(text="Splenic diffuse red pulp small B-cell lymphoma") )
        setattr(cls, "Malignant lymphoma, cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, cleaved cell, NOS") )
        setattr(cls, "Dysplastic nevus",
                PermissibleValue(text="Dysplastic nevus") )
        setattr(cls, "Spindle cell melanoma, NOS",
                PermissibleValue(text="Spindle cell melanoma, NOS") )
        setattr(cls, "Chronic myelogenous leukemia, Philadelphia chromosome (Ph 1) positive",
                PermissibleValue(text="Chronic myelogenous leukemia, Philadelphia chromosome (Ph 1) positive") )
        setattr(cls, "Bronchiolar adenocarcinoma",
                PermissibleValue(text="Bronchiolar adenocarcinoma") )
        setattr(cls, "Salivary duct carcinoma",
                PermissibleValue(text="Salivary duct carcinoma",
                                 description="Salivary Duct Carcinoma") )
        setattr(cls, "Multicystic mesothelioma, benign",
                PermissibleValue(text="Multicystic mesothelioma, benign") )
        setattr(cls, "Microfollicular adenoma, NOS",
                PermissibleValue(text="Microfollicular adenoma, NOS") )
        setattr(cls, "Endometrial stromatosis",
                PermissibleValue(text="Endometrial stromatosis") )
        setattr(cls, "Acinar cell adenoma",
                PermissibleValue(text="Acinar cell adenoma") )
        setattr(cls, "Gastrin cell tumor",
                PermissibleValue(text="Gastrin cell tumor") )
        setattr(cls, "Skin appendage adenoma",
                PermissibleValue(text="Skin appendage adenoma") )
        setattr(cls, "Malignant lymphoma, mixed cell type, follicular",
                PermissibleValue(text="Malignant lymphoma, mixed cell type, follicular") )
        setattr(cls, "Malignant lymphoma, follicle center, NOS",
                PermissibleValue(text="Malignant lymphoma, follicle center, NOS") )
        setattr(cls, "Endocrine adenomatosis",
                PermissibleValue(text="Endocrine adenomatosis") )
        setattr(cls, "Pleomorphic adenoma",
                PermissibleValue(text="Pleomorphic adenoma") )
        setattr(cls, "Adenocarcinoma, cribriform comedo-type",
                PermissibleValue(text="Adenocarcinoma, cribriform comedo-type") )
        setattr(cls, "Krukenberg tumor",
                PermissibleValue(text="Krukenberg tumor") )
        setattr(cls, "Diktyoma, benign",
                PermissibleValue(text="Diktyoma, benign") )
        setattr(cls, "Acute erythremic myelosis",
                PermissibleValue(text="Acute erythremic myelosis") )
        setattr(cls, "Adult granulosa cell tumor",
                PermissibleValue(text="Adult granulosa cell tumor") )
        setattr(cls, "Combined hepatocellular carcinoma and cholangiocarcinoma",
                PermissibleValue(text="Combined hepatocellular carcinoma and cholangiocarcinoma") )
        setattr(cls, "Squamous cell carcinoma with horn formation",
                PermissibleValue(text="Squamous cell carcinoma with horn formation") )
        setattr(cls, "Fibroepithelioma of Pinkus type",
                PermissibleValue(text="Fibroepithelioma of Pinkus type") )
        setattr(cls, "Extranodal marginal zone lymphoma of mucosa-associated lymphoid tissue",
                PermissibleValue(text="Extranodal marginal zone lymphoma of mucosa-associated lymphoid tissue") )
        setattr(cls, "Ductal intraepithelial neoplasia 3",
                PermissibleValue(text="Ductal intraepithelial neoplasia 3") )
        setattr(cls, "Black adenoma",
                PermissibleValue(text="Black adenoma") )
        setattr(cls, "Eccrine spiradenoma",
                PermissibleValue(text="Eccrine spiradenoma") )
        setattr(cls, "Peripheral T-cell lymphoma, AILD (Angioimmunoblastic Lymphadenopathy with Dysproteinemia)",
                PermissibleValue(text="Peripheral T-cell lymphoma, AILD (Angioimmunoblastic Lymphadenopathy with Dysproteinemia)") )
        setattr(cls, "Sertoli-Leydig cell tumor of intermediate differentiation",
                PermissibleValue(text="Sertoli-Leydig cell tumor of intermediate differentiation") )
        setattr(cls, "Prolymphocytic leukemia, B-cell type",
                PermissibleValue(text="Prolymphocytic leukemia, B-cell type") )
        setattr(cls, "Non-lymphocytic leukemia, NOS",
                PermissibleValue(text="Non-lymphocytic leukemia, NOS") )
        setattr(cls, "Cutaneous mastocytosis",
                PermissibleValue(text="Cutaneous mastocytosis") )
        setattr(cls, "Periosteal fibroma",
                PermissibleValue(text="Periosteal fibroma") )
        setattr(cls, "Nested urothelial carcinoma",
                PermissibleValue(text="Nested urothelial carcinoma") )
        setattr(cls, "Pseudomyxoma peritonei with unknown primary site",
                PermissibleValue(text="Pseudomyxoma peritonei with unknown primary site") )
        setattr(cls, "Glioma, malignant",
                PermissibleValue(text="Glioma, malignant") )
        setattr(cls, "Subacute leukemia, NOS",
                PermissibleValue(text="Subacute leukemia, NOS") )
        setattr(cls, "Apocrine cystadenoma",
                PermissibleValue(text="Apocrine cystadenoma") )
        setattr(cls, "Follicular lymphoma, grade 1",
                PermissibleValue(text="Follicular lymphoma, grade 1") )
        setattr(cls, "Liver cell adenoma",
                PermissibleValue(text="Liver cell adenoma") )
        setattr(cls, "Classical Hodgkin lymphoma, lymphocyte depletion, NOS",
                PermissibleValue(text="Classical Hodgkin lymphoma, lymphocyte depletion, NOS") )
        setattr(cls, "Fibromatosis-like metaplastic carcinoma",
                PermissibleValue(text="Fibromatosis-like metaplastic carcinoma") )
        setattr(cls, "Spongioblastoma, NOS",
                PermissibleValue(text="Spongioblastoma, NOS") )
        setattr(cls, "Chief cell adenoma",
                PermissibleValue(text="Chief cell adenoma") )
        setattr(cls, "True histiocytic lymphoma",
                PermissibleValue(text="True histiocytic lymphoma") )
        setattr(cls, "Clear cell ependymoma",
                PermissibleValue(text="Clear cell ependymoma") )
        setattr(cls, "Plasmacytic lymphoma",
                PermissibleValue(text="Plasmacytic lymphoma") )
        setattr(cls, "Mixed glioma",
                PermissibleValue(text="Mixed glioma") )
        setattr(cls, "Combined small cell carcinoma",
                PermissibleValue(text="Combined small cell carcinoma") )
        setattr(cls, "Undifferentiated leukaemia",
                PermissibleValue(text="Undifferentiated leukaemia") )
        setattr(cls, "ECL cell carcinoid, malignant",
                PermissibleValue(text="ECL cell carcinoid, malignant") )
        setattr(cls, "Thecoma, malignant",
                PermissibleValue(text="Thecoma, malignant") )
        setattr(cls, "Squamous cell papilloma, NOS",
                PermissibleValue(text="Squamous cell papilloma, NOS") )
        setattr(cls, "Mantle zone lymphoma",
                PermissibleValue(text="Mantle zone lymphoma") )
        setattr(cls, "Thymoma, type AB, NOS",
                PermissibleValue(text="Thymoma, type AB, NOS") )
        setattr(cls, "Basal cell carcinoma, fibroepithelial",
                PermissibleValue(text="Basal cell carcinoma, fibroepithelial") )
        setattr(cls, "Islet cell adenomatosis",
                PermissibleValue(text="Islet cell adenomatosis") )
        setattr(cls, "DCIS, NOS",
                PermissibleValue(text="DCIS, NOS") )
        setattr(cls, "Cribriform carcinoma in situ",
                PermissibleValue(text="Cribriform carcinoma in situ") )
        setattr(cls, "Chronic lymphoid leukemia",
                PermissibleValue(text="Chronic lymphoid leukemia") )
        setattr(cls, "Basal cell carcinoma, morpheic",
                PermissibleValue(text="Basal cell carcinoma, morpheic") )
        setattr(cls, "Malignant lymphoma, centroblasticcentrocytic, diffuse",
                PermissibleValue(text="Malignant lymphoma, centroblasticcentrocytic, diffuse") )
        setattr(cls, "Thymoma, mixed type, NOS",
                PermissibleValue(text="Thymoma, mixed type, NOS") )
        setattr(cls, "NUT carcinoma",
                PermissibleValue(text="NUT carcinoma",
                                 description="NUT Carcinoma") )
        setattr(cls, "Basal cell adenocarcinoma",
                PermissibleValue(text="Basal cell adenocarcinoma",
                                 description="Salivary Gland Basal Cell Adenocarcinoma") )
        setattr(cls, "Brooke tumor",
                PermissibleValue(text="Brooke tumor") )
        setattr(cls, "Pro-T ALL",
                PermissibleValue(text="Pro-T ALL") )
        setattr(cls, "Follicular adenocarcinoma, NOS",
                PermissibleValue(text="Follicular adenocarcinoma, NOS") )
        setattr(cls, "Thymoma, mixed type, malignant",
                PermissibleValue(text="Thymoma, mixed type, malignant") )
        setattr(cls, "Meningeal melanocytoma",
                PermissibleValue(text="Meningeal melanocytoma") )
        setattr(cls, "Papillary pseudomucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Papillary pseudomucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Malignant lymphoma, lymphocytic, intermediate differentiation, diffuse",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, intermediate differentiation, diffuse") )
        setattr(cls, "Insulinoma, malignant",
                PermissibleValue(text="Insulinoma, malignant") )
        setattr(cls, "Steroid cell tumor, NOS",
                PermissibleValue(text="Steroid cell tumor, NOS") )
        setattr(cls, "Mature teratoma",
                PermissibleValue(text="Mature teratoma") )
        setattr(cls, "Malignant lymphoma, lymphoplasmacytic",
                PermissibleValue(text="Malignant lymphoma, lymphoplasmacytic") )
        setattr(cls, "Columnar cell papilloma",
                PermissibleValue(text="Columnar cell papilloma") )
        setattr(cls, "Aggressive osteoblastoma",
                PermissibleValue(text="Aggressive osteoblastoma") )
        setattr(cls, "Thymoma, predominantly cortical, NOS",
                PermissibleValue(text="Thymoma, predominantly cortical, NOS") )
        setattr(cls, "Multiple adenomatous polyps",
                PermissibleValue(text="Multiple adenomatous polyps") )
        setattr(cls, "Diffuse astrocytoma",
                PermissibleValue(text="Diffuse astrocytoma") )
        setattr(cls, "Collecting duct carcinoma",
                PermissibleValue(text="Collecting duct carcinoma",
                                 description="Carcinoma of the Collecting Ducts of Bellini") )
        setattr(cls, "Polycythemia rubra vera",
                PermissibleValue(text="Polycythemia rubra vera") )
        setattr(cls, "Hand-Schuller-Christian disease",
                PermissibleValue(text="Hand-Schuller-Christian disease") )
        setattr(cls, "Malignant lymphoma, nodular, NOS",
                PermissibleValue(text="Malignant lymphoma, nodular, NOS") )
        setattr(cls, "Paget disease of breast",
                PermissibleValue(text="Paget disease of breast") )
        setattr(cls, "Glomus tumor, malignant",
                PermissibleValue(text="Glomus tumor, malignant") )
        setattr(cls, "Argentaffinoma, NOS",
                PermissibleValue(text="Argentaffinoma, NOS") )
        setattr(cls, "Thymoma, type AB, malignant",
                PermissibleValue(text="Thymoma, type AB, malignant") )
        setattr(cls, "Follicular adenocarcinoma, moderately differentiated",
                PermissibleValue(text="Follicular adenocarcinoma, moderately differentiated") )
        setattr(cls, "Intramuscular hemangioma",
                PermissibleValue(text="Intramuscular hemangioma") )
        setattr(cls, "Myeloid leukemia associated with Down Syndrome",
                PermissibleValue(text="Myeloid leukemia associated with Down Syndrome") )
        setattr(cls, "Post transplant lymphoproliferative disorder, NOS",
                PermissibleValue(text="Post transplant lymphoproliferative disorder, NOS") )
        setattr(cls, "Malignant lymphoma, small noncleaved, Burkitt type",
                PermissibleValue(text="Malignant lymphoma, small noncleaved, Burkitt type") )
        setattr(cls, "Capillary hemangioma",
                PermissibleValue(text="Capillary hemangioma") )
        setattr(cls, "Arrhenoblastoma, malignant",
                PermissibleValue(text="Arrhenoblastoma, malignant") )
        setattr(cls, "Fascial fibroma",
                PermissibleValue(text="Fascial fibroma") )
        setattr(cls, "Biliary intraepithelial neoplasia, grade 3",
                PermissibleValue(text="Biliary intraepithelial neoplasia, grade 3") )
        setattr(cls, "Immature teratoma, malignant",
                PermissibleValue(text="Immature teratoma, malignant") )
        setattr(cls, "Epithelioid sarcoma",
                PermissibleValue(text="Epithelioid sarcoma") )
        setattr(cls, "Placental site trophoblastic tumor",
                PermissibleValue(text="Placental site trophoblastic tumor") )
        setattr(cls, "Plexiform fibrohistiocytic tumor",
                PermissibleValue(text="Plexiform fibrohistiocytic tumor") )
        setattr(cls, "Hepatocellular carcinoma, sarcomatoid",
                PermissibleValue(text="Hepatocellular carcinoma, sarcomatoid") )
        setattr(cls, "Glandular intraepithelial neoplasia, grade II",
                PermissibleValue(text="Glandular intraepithelial neoplasia, grade II") )
        setattr(cls, "CIN III with severe dysplasia",
                PermissibleValue(text="CIN III with severe dysplasia") )
        setattr(cls, "Cystic mesothelioma, benign",
                PermissibleValue(text="Cystic mesothelioma, benign") )
        setattr(cls, "Dedifferentiated chondrosarcoma",
                PermissibleValue(text="Dedifferentiated chondrosarcoma") )
        setattr(cls, "Cerebellar sarcoma, NOS",
                PermissibleValue(text="Cerebellar sarcoma, NOS") )
        setattr(cls, "Canalicular adenoma",
                PermissibleValue(text="Canalicular adenoma") )
        setattr(cls, "Intraductal papilloma with lobular carcinoma in situ",
                PermissibleValue(text="Intraductal papilloma with lobular carcinoma in situ") )
        setattr(cls, "Papillary pseudomucinous cystadenocarcinoma",
                PermissibleValue(text="Papillary pseudomucinous cystadenocarcinoma") )
        setattr(cls, "Transitional cell carcinoma, spindle cell",
                PermissibleValue(text="Transitional cell carcinoma, spindle cell") )
        setattr(cls, "Compound odontoma",
                PermissibleValue(text="Compound odontoma") )
        setattr(cls, "Noninvasive pancreatobiliary papillary neoplasm with low grade dysplasia",
                PermissibleValue(text="Noninvasive pancreatobiliary papillary neoplasm with low grade dysplasia") )
        setattr(cls, "Conventional central osteosarcoma",
                PermissibleValue(text="Conventional central osteosarcoma") )
        setattr(cls, "Acute myelofibrosis",
                PermissibleValue(text="Acute myelofibrosis") )
        setattr(cls, "Alveolar carcinoma",
                PermissibleValue(text="Alveolar carcinoma") )
        setattr(cls, "Classical Hodgkin lymphoma, nodular sclerosis, grade 2",
                PermissibleValue(text="Classical Hodgkin lymphoma, nodular sclerosis, grade 2") )
        setattr(cls, "Hydroa vacciniforme-like lymphoma",
                PermissibleValue(text="Hydroa vacciniforme-like lymphoma") )
        setattr(cls, "Central osteosarcoma",
                PermissibleValue(text="Central osteosarcoma") )
        setattr(cls, "Chondromatous giant cell tumor",
                PermissibleValue(text="Chondromatous giant cell tumor") )
        setattr(cls, "Eccrine acrospiroma",
                PermissibleValue(text="Eccrine acrospiroma") )
        setattr(cls, "Follicular adenoma, oxyphilic cell",
                PermissibleValue(text="Follicular adenoma, oxyphilic cell") )
        setattr(cls, "Papillary ependymoma",
                PermissibleValue(text="Papillary ependymoma") )
        setattr(cls, "Infiltrating basal cell carcinoma, non-sclerosing",
                PermissibleValue(text="Infiltrating basal cell carcinoma, non-sclerosing") )
        setattr(cls, "Bronchio-alveolar carcinoma, mucinous",
                PermissibleValue(text="Bronchio-alveolar carcinoma, mucinous") )
        setattr(cls, "Agnogenic myeloid metaplasia",
                PermissibleValue(text="Agnogenic myeloid metaplasia") )
        setattr(cls, "Carcinoid tumor, argentaffin, malignant",
                PermissibleValue(text="Carcinoid tumor, argentaffin, malignant") )
        setattr(cls, "Myeloproliferative disease, NOS",
                PermissibleValue(text="Myeloproliferative disease, NOS") )
        setattr(cls, "Carcinoma, NOS",
                PermissibleValue(text="Carcinoma, NOS") )
        setattr(cls, "Langerhans cell histiocytosis, NOS",
                PermissibleValue(text="Langerhans cell histiocytosis, NOS") )
        setattr(cls, "Mixed acinar-endocrine carcinoma",
                PermissibleValue(text="Mixed acinar-endocrine carcinoma") )
        setattr(cls, "Thymic carcinoma, NOS",
                PermissibleValue(text="Thymic carcinoma, NOS") )
        setattr(cls, "Hairy cell leukemia variant",
                PermissibleValue(text="Hairy cell leukemia variant") )
        setattr(cls, "Klatskin tumor",
                PermissibleValue(text="Klatskin tumor") )
        setattr(cls, "Nephroblastoma, NOS",
                PermissibleValue(text="Nephroblastoma, NOS") )
        setattr(cls, "Spindle cell rhabdomyosarcoma",
                PermissibleValue(text="Spindle cell rhabdomyosarcoma") )
        setattr(cls, "Astrocytoma, anaplastic",
                PermissibleValue(text="Astrocytoma, anaplastic") )
        setattr(cls, "Myeloid and lymphoid neoplasms with FGFR1 abnormalities",
                PermissibleValue(text="Myeloid and lymphoid neoplasms with FGFR1 abnormalities") )
        setattr(cls, "Clear cell cystadenoma",
                PermissibleValue(text="Clear cell cystadenoma") )
        setattr(cls, "Pleuropulmonary blastoma",
                PermissibleValue(text="Pleuropulmonary blastoma") )
        setattr(cls, "Dermatofibroma lenticulare",
                PermissibleValue(text="Dermatofibroma lenticulare") )
        setattr(cls, "Superficial spreading adenocarcinoma",
                PermissibleValue(text="Superficial spreading adenocarcinoma") )
        setattr(cls, "Triton tumor, malignant",
                PermissibleValue(text="Triton tumor, malignant") )
        setattr(cls, "Ceruminous adenocarcinoma",
                PermissibleValue(text="Ceruminous adenocarcinoma") )
        setattr(cls, "Acute myeloid leukemia with multilineage dysplasia",
                PermissibleValue(text="Acute myeloid leukemia with multilineage dysplasia") )
        setattr(cls, "Acinar cell tumor",
                PermissibleValue(text="Acinar cell tumor") )
        setattr(cls, "Teratoma with malignant transformation",
                PermissibleValue(text="Teratoma with malignant transformation") )
        setattr(cls, "Adenocarcinoma, intestinal type",
                PermissibleValue(text="Adenocarcinoma, intestinal type",
                                 description="Intestinal-Type Adenocarcinoma") )
        setattr(cls, "FAB M4",
                PermissibleValue(text="FAB M4") )
        setattr(cls, "Papillary microcarcinoma",
                PermissibleValue(text="Papillary microcarcinoma") )
        setattr(cls, "Differentiated penile intraepithelial neoplasia",
                PermissibleValue(text="Differentiated penile intraepithelial neoplasia") )
        setattr(cls, "B-ALL",
                PermissibleValue(text="B-ALL") )
        setattr(cls, "Invasive mucinous adenocarcinoma",
                PermissibleValue(text="Invasive mucinous adenocarcinoma") )
        setattr(cls, "Infiltrating papillary adenocarcinoma",
                PermissibleValue(text="Infiltrating papillary adenocarcinoma") )
        setattr(cls, "Basal cell adenoma",
                PermissibleValue(text="Basal cell adenoma") )
        setattr(cls, "Intracystic papillary tumor with high grade dysplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade dysplasia") )
        setattr(cls, "SALT lymphoma",
                PermissibleValue(text="SALT lymphoma") )
        setattr(cls, "Adenomatoid odontogenic tumor",
                PermissibleValue(text="Adenomatoid odontogenic tumor") )
        setattr(cls, "Sezary syndrome",
                PermissibleValue(text="Sezary syndrome") )
        setattr(cls, "Heavy chain disease, NOS",
                PermissibleValue(text="Heavy chain disease, NOS") )
        setattr(cls, "Meningeal sarcoma",
                PermissibleValue(text="Meningeal sarcoma") )
        setattr(cls, "Primary cutaneous CD30+ T-cell lymphoproliferative disorder",
                PermissibleValue(text="Primary cutaneous CD30+ T-cell lymphoproliferative disorder") )
        setattr(cls, "Mucoid carcinoma",
                PermissibleValue(text="Mucoid carcinoma") )
        setattr(cls, "Atypical proliferating serous tumor",
                PermissibleValue(text="Atypical proliferating serous tumor") )
        setattr(cls, "Malignant lymphoma, lymphocytic, poorly differentiated, nodular",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, poorly differentiated, nodular") )
        setattr(cls, "Sinonasal papilloma, NOS",
                PermissibleValue(text="Sinonasal papilloma, NOS") )
        setattr(cls, "Spindle cell melanoma, type B",
                PermissibleValue(text="Spindle cell melanoma, type B") )
        setattr(cls, "Skin-associated lymphoid tissue lymphoma",
                PermissibleValue(text="Skin-associated lymphoid tissue lymphoma") )
        setattr(cls, "Acute lymphoblastic leukemia, NOS",
                PermissibleValue(text="Acute lymphoblastic leukemia, NOS") )
        setattr(cls, "Diffuse astrocytoma, IDH-mutant",
                PermissibleValue(text="Diffuse astrocytoma, IDH-mutant") )
        setattr(cls, "Hyalinizing trabecular adenoma",
                PermissibleValue(text="Hyalinizing trabecular adenoma") )
        setattr(cls, "Chondroid chordoma",
                PermissibleValue(text="Chondroid chordoma") )
        setattr(cls, "Keratotoc papilloma",
                PermissibleValue(text="Keratotoc papilloma") )
        setattr(cls, "Sinonasal papilloma, exophytic",
                PermissibleValue(text="Sinonasal papilloma, exophytic") )
        setattr(cls, "Diffuse astrocytoma, IDH-wildtype",
                PermissibleValue(text="Diffuse astrocytoma, IDH-wildtype") )
        setattr(cls, "Syncytial meningioma",
                PermissibleValue(text="Syncytial meningioma") )
        setattr(cls, "Atypical proliferative endometrioid tumor",
                PermissibleValue(text="Atypical proliferative endometrioid tumor") )
        setattr(cls, "Prolymphocytic leukemia, NOS",
                PermissibleValue(text="Prolymphocytic leukemia, NOS") )
        setattr(cls, "Interstitial cell tumor, benign",
                PermissibleValue(text="Interstitial cell tumor, benign") )
        setattr(cls, "Histiocytic medullary reticulosis",
                PermissibleValue(text="Histiocytic medullary reticulosis") )
        setattr(cls, "Invasive carcinoma, NST",
                PermissibleValue(text="Invasive carcinoma, NST") )
        setattr(cls, "Diffuse leptomeningeal glioneuronal tumor",
                PermissibleValue(text="Diffuse leptomeningeal glioneuronal tumor") )
        setattr(cls, "Adrenal cortical adenocarcinoma",
                PermissibleValue(text="Adrenal cortical adenocarcinoma") )
        setattr(cls, "Hidradenoma papilliferum",
                PermissibleValue(text="Hidradenoma papilliferum") )
        setattr(cls, "Clear cell adenofibroma",
                PermissibleValue(text="Clear cell adenofibroma") )
        setattr(cls, "BALT lymphoma",
                PermissibleValue(text="BALT lymphoma") )
        setattr(cls, "Malignant lymphoma, undifferentiated cell, non-Burkitt",
                PermissibleValue(text="Malignant lymphoma, undifferentiated cell, non-Burkitt") )
        setattr(cls, "Mucinous adenocarcinofibroma",
                PermissibleValue(text="Mucinous adenocarcinofibroma") )
        setattr(cls, "Intramuscular lipoma",
                PermissibleValue(text="Intramuscular lipoma") )
        setattr(cls, "Adenocystic carcinoma",
                PermissibleValue(text="Adenocystic carcinoma") )
        setattr(cls, "Atypical chronic myeloid leukemia, BCR/ABL negative",
                PermissibleValue(text="Atypical chronic myeloid leukemia, BCR/ABL negative") )
        setattr(cls, "Melanocytic nevus",
                PermissibleValue(text="Melanocytic nevus") )
        setattr(cls, "Odontogenic ghost cell tumor",
                PermissibleValue(text="Odontogenic ghost cell tumor") )
        setattr(cls, "Acute myeloid leukemia, t(15:17)(g22;q11-12)",
                PermissibleValue(text="Acute myeloid leukemia, t(15:17)(g22;q11-12)") )
        setattr(cls, "Odontogenic tumor, malignant",
                PermissibleValue(text="Odontogenic tumor, malignant") )
        setattr(cls, "Epithelioid mesothelioma, malignant",
                PermissibleValue(text="Epithelioid mesothelioma, malignant") )
        setattr(cls, "Langerhans cell granulomatosis",
                PermissibleValue(text="Langerhans cell granulomatosis") )
        setattr(cls, "Chronic lymphatic leukemia",
                PermissibleValue(text="Chronic lymphatic leukemia") )
        setattr(cls, "Pseudomyxoma peritonei",
                PermissibleValue(text="Pseudomyxoma peritonei") )
        setattr(cls, "Lymphangioendothelioma, malignant",
                PermissibleValue(text="Lymphangioendothelioma, malignant") )
        setattr(cls, "Soft tissue perineurioma",
                PermissibleValue(text="Soft tissue perineurioma") )
        setattr(cls, "Squamous cell carcinoma, clear cell type",
                PermissibleValue(text="Squamous cell carcinoma, clear cell type") )
        setattr(cls, "Squamous cell carcinoma, NOS",
                PermissibleValue(text="Squamous cell carcinoma, NOS") )
        setattr(cls, "Carotid body tumor",
                PermissibleValue(text="Carotid body tumor") )
        setattr(cls, "Thymic large B-cell lymphoma",
                PermissibleValue(text="Thymic large B-cell lymphoma") )
        setattr(cls, "Spitz nevus",
                PermissibleValue(text="Spitz nevus") )
        setattr(cls, "Eosinophil carcinoma",
                PermissibleValue(text="Eosinophil carcinoma") )
        setattr(cls, "Mixed acidophil-basophil carcinoma",
                PermissibleValue(text="Mixed acidophil-basophil carcinoma") )
        setattr(cls, "Vipoma, malignant",
                PermissibleValue(text="Vipoma, malignant") )
        setattr(cls, "Cystic teratoma, NOS",
                PermissibleValue(text="Cystic teratoma, NOS") )
        setattr(cls, "Neoplasm, NOS",
                PermissibleValue(text="Neoplasm, NOS") )
        setattr(cls, "Transient abnormal myelopoiesis",
                PermissibleValue(text="Transient abnormal myelopoiesis") )
        setattr(cls, "Adenocarcinoma with squamous metaplasia",
                PermissibleValue(text="Adenocarcinoma with squamous metaplasia") )
        setattr(cls, "MPNST, NOS",
                PermissibleValue(text="MPNST, NOS") )
        setattr(cls, "Papillary carcinoma, encapsulated",
                PermissibleValue(text="Papillary carcinoma, encapsulated") )
        setattr(cls, "Fascial fibrosarcoma",
                PermissibleValue(text="Fascial fibrosarcoma") )
        setattr(cls, "Squamous cell carcinoma, pseudoglandular",
                PermissibleValue(text="Squamous cell carcinoma, pseudoglandular") )
        setattr(cls, "Mucinous adenofibroma, NOS",
                PermissibleValue(text="Mucinous adenofibroma, NOS") )
        setattr(cls, "Mucous adenocarcinoma",
                PermissibleValue(text="Mucous adenocarcinoma") )
        setattr(cls, "Mucinous cystadenoma, NOS",
                PermissibleValue(text="Mucinous cystadenoma, NOS") )
        setattr(cls, "Oat cell carcinoma",
                PermissibleValue(text="Oat cell carcinoma") )
        setattr(cls, "Megakaryocytic leukemia",
                PermissibleValue(text="Megakaryocytic leukemia") )
        setattr(cls, "Intraductal papilloma",
                PermissibleValue(text="Intraductal papilloma") )
        setattr(cls, "Supratentorial PNET",
                PermissibleValue(text="Supratentorial PNET") )
        setattr(cls, "Chronic myeloproliferative disease, NOS",
                PermissibleValue(text="Chronic myeloproliferative disease, NOS") )
        setattr(cls, "Noninfiltrating intraductal papillary adenocarcinoma",
                PermissibleValue(text="Noninfiltrating intraductal papillary adenocarcinoma") )
        setattr(cls, "Round cell osteosarcoma",
                PermissibleValue(text="Round cell osteosarcoma") )
        setattr(cls, "Myelodysplastic syndrome, NOS",
                PermissibleValue(text="Myelodysplastic syndrome, NOS") )
        setattr(cls, "Adenocarcinoma in situ in adenomatous polyp",
                PermissibleValue(text="Adenocarcinoma in situ in adenomatous polyp") )
        setattr(cls, "Sclerosing stromal tumor",
                PermissibleValue(text="Sclerosing stromal tumor") )
        setattr(cls, "Transitional cell carcinoma",
                PermissibleValue(text="Transitional cell carcinoma",
                                 description="Ovarian Transitional Cell Carcinoma") )
        setattr(cls, "Hodgkin lymphoma, nodular sclerosis, cellular phase",
                PermissibleValue(text="Hodgkin lymphoma, nodular sclerosis, cellular phase") )
        setattr(cls, "Perineurioma, malignant",
                PermissibleValue(text="Perineurioma, malignant") )
        setattr(cls, "Enterochromaffin-like cell tumor, malignant",
                PermissibleValue(text="Enterochromaffin-like cell tumor, malignant") )
        setattr(cls, "Adrenal cortical adenoma, glomerulosa cell",
                PermissibleValue(text="Adrenal cortical adenoma, glomerulosa cell") )
        setattr(cls, "PNET, NOS",
                PermissibleValue(text="PNET, NOS") )
        setattr(cls, "Glandular intraepithelial neoplasia, grade III",
                PermissibleValue(text="Glandular intraepithelial neoplasia, grade III") )
        setattr(cls, "Mucoid adenocarcinoma",
                PermissibleValue(text="Mucoid adenocarcinoma") )
        setattr(cls, "Granular cell tumor of the sellar region",
                PermissibleValue(text="Granular cell tumor of the sellar region") )
        setattr(cls, "Merkel cell tumor",
                PermissibleValue(text="Merkel cell tumor") )
        setattr(cls, "Follicular carcinoma, trabecular",
                PermissibleValue(text="Follicular carcinoma, trabecular") )
        setattr(cls, "Glycogen-rich carcinoma",
                PermissibleValue(text="Glycogen-rich carcinoma") )
        setattr(cls, "Wolffian duct adenoma",
                PermissibleValue(text="Wolffian duct adenoma") )
        setattr(cls, "Giant cell sarcoma",
                PermissibleValue(text="Giant cell sarcoma") )
        setattr(cls, "Acute myeloid leukemia, AML1(CBF-alpha)/ETO",
                PermissibleValue(text="Acute myeloid leukemia, AML1(CBF-alpha)/ETO") )
        setattr(cls, "Anaplastic medulloblastoma",
                PermissibleValue(text="Anaplastic medulloblastoma") )
        setattr(cls, "Immunoproliferative small intestinal disease",
                PermissibleValue(text="Immunoproliferative small intestinal disease") )
        setattr(cls, "Mucinous cystic tumor with intermediate dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with intermediate dysplasia") )
        setattr(cls, "Acute lymphoid leukemia",
                PermissibleValue(text="Acute lymphoid leukemia") )
        setattr(cls, "Mucin-secreting adenocarcinoma",
                PermissibleValue(text="Mucin-secreting adenocarcinoma") )
        setattr(cls, "Intracystic papillary tumor with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade intraepithelial neoplasia") )
        setattr(cls, "Medullary carcinoma with amyloid stroma",
                PermissibleValue(text="Medullary carcinoma with amyloid stroma") )
        setattr(cls, "Pancreatic microadenoma",
                PermissibleValue(text="Pancreatic microadenoma") )
        setattr(cls, "Gigantiform cementoma",
                PermissibleValue(text="Gigantiform cementoma") )
        setattr(cls, "Psammomatous schwannoma",
                PermissibleValue(text="Psammomatous schwannoma") )
        setattr(cls, "Clear cell carcinoma",
                PermissibleValue(text="Clear cell carcinoma") )
        setattr(cls, "Pigmented adenoma",
                PermissibleValue(text="Pigmented adenoma") )
        setattr(cls, "Papillary cystadenoma, borderline malignancy",
                PermissibleValue(text="Papillary cystadenoma, borderline malignancy") )
        setattr(cls, "Blastoma, NOS",
                PermissibleValue(text="Blastoma, NOS") )
        setattr(cls, "Piloid astrocytoma",
                PermissibleValue(text="Piloid astrocytoma") )
        setattr(cls, "Desmoid, NOS",
                PermissibleValue(text="Desmoid, NOS") )
        setattr(cls, "Central neurocytoma",
                PermissibleValue(text="Central neurocytoma") )
        setattr(cls, "Extraosseous plasmacytoma",
                PermissibleValue(text="Extraosseous plasmacytoma") )
        setattr(cls, "Clear cell sarcoma, NOS",
                PermissibleValue(text="Clear cell sarcoma, NOS") )
        setattr(cls, "Tumor, benign",
                PermissibleValue(text="Tumor, benign") )
        setattr(cls, "Medulloblastoma, WNT-activated",
                PermissibleValue(text="Medulloblastoma, WNT-activated") )
        setattr(cls, "Biliary papillomatosis",
                PermissibleValue(text="Biliary papillomatosis") )
        setattr(cls, "Choroid plexus papilloma, anaplastic",
                PermissibleValue(text="Choroid plexus papilloma, anaplastic") )
        setattr(cls, "Acute myeloid leukemia without maturation",
                PermissibleValue(text="Acute myeloid leukemia without maturation") )
        setattr(cls, "Pigmented nevus, NOS",
                PermissibleValue(text="Pigmented nevus, NOS") )
        setattr(cls, "Hodgkin lymphoma, lymphocyte depletion, NOS",
                PermissibleValue(text="Hodgkin lymphoma, lymphocyte depletion, NOS") )
        setattr(cls, "Acinar adenocarcinoma, sarcomatoid",
                PermissibleValue(text="Acinar adenocarcinoma, sarcomatoid") )
        setattr(cls, "Renal cell carcinoma, NOS",
                PermissibleValue(text="Renal cell carcinoma, NOS") )
        setattr(cls, "Malignant lymphoma, lymphocytic, diffuse, NOS",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, diffuse, NOS") )
        setattr(cls, "Mucinous adenoma",
                PermissibleValue(text="Mucinous adenoma") )
        setattr(cls, "Papillary syringocystadenoma",
                PermissibleValue(text="Papillary syringocystadenoma") )
        setattr(cls, "Arrhenoblastoma, benign",
                PermissibleValue(text="Arrhenoblastoma, benign") )
        setattr(cls, "Spongioblastoma multiforme",
                PermissibleValue(text="Spongioblastoma multiforme") )
        setattr(cls, "Endometrioid cystadenoma, borderline malignancy",
                PermissibleValue(text="Endometrioid cystadenoma, borderline malignancy") )
        setattr(cls, "Intraepidermal squamous cell carcinoma, Bowen type",
                PermissibleValue(text="Intraepidermal squamous cell carcinoma, Bowen type") )
        setattr(cls, "Solid carcinoma, NOS",
                PermissibleValue(text="Solid carcinoma, NOS") )
        setattr(cls, "Carcinoma, undifferentiated, NOS",
                PermissibleValue(text="Carcinoma, undifferentiated, NOS") )
        setattr(cls, "Thymoma, lymphocytic, malignant",
                PermissibleValue(text="Thymoma, lymphocytic, malignant") )
        setattr(cls, "Adenomatous polyp, NOS",
                PermissibleValue(text="Adenomatous polyp, NOS") )
        setattr(cls, "Papillary serous adenocarcinoma",
                PermissibleValue(text="Papillary serous adenocarcinoma") )
        setattr(cls, "Pheochromocytoma, malignant",
                PermissibleValue(text="Pheochromocytoma, malignant") )
        setattr(cls, "NK-cell large granular lymphocytic leukemia",
                PermissibleValue(text="NK-cell large granular lymphocytic leukemia") )
        setattr(cls, "Soft tissue sarcoma",
                PermissibleValue(text="Soft tissue sarcoma") )
        setattr(cls, "Neoplasm, secondary",
                PermissibleValue(text="Neoplasm, secondary") )
        setattr(cls, "Syringocystadenoma papilliferum",
                PermissibleValue(text="Syringocystadenoma papilliferum") )
        setattr(cls, "Burkitt tumor",
                PermissibleValue(text="Burkitt tumor") )
        setattr(cls, "Invasive encapsulated follicular variant of papillary thyroid carcinoma (invasive EFVPTC)",
                PermissibleValue(text="Invasive encapsulated follicular variant of papillary thyroid carcinoma (invasive EFVPTC)") )
        setattr(cls, "Urothelial carcinoma in situ",
                PermissibleValue(text="Urothelial carcinoma in situ") )
        setattr(cls, "Cystosarcoma phyllodes, benign",
                PermissibleValue(text="Cystosarcoma phyllodes, benign") )
        setattr(cls, "Myxoid liposarcoma",
                PermissibleValue(text="Myxoid liposarcoma") )
        setattr(cls, "Serous surface papillary tumor of borderline malignancy",
                PermissibleValue(text="Serous surface papillary tumor of borderline malignancy") )
        setattr(cls, "Fibroxanthoma, malignant",
                PermissibleValue(text="Fibroxanthoma, malignant") )
        setattr(cls, "Dabska tumor",
                PermissibleValue(text="Dabska tumor") )
        setattr(cls, "Adenocarcinoma in polypoid adenoma",
                PermissibleValue(text="Adenocarcinoma in polypoid adenoma") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with t(5;14)(q31;q32); IL3-IGH",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with t(5;14)(q31;q32); IL3-IGH") )
        setattr(cls, "Thymoma, spindle cell, NOS",
                PermissibleValue(text="Thymoma, spindle cell, NOS") )
        setattr(cls, "Intraductal papillary mucinous neoplasm with high grade dysplasia",
                PermissibleValue(text="Intraductal papillary mucinous neoplasm with high grade dysplasia") )
        setattr(cls, "Acute myeloid leukemia, PML/RAR-alpha",
                PermissibleValue(text="Acute myeloid leukemia, PML/RAR-alpha") )
        setattr(cls, "Acute myeloid leukemia with inv(3)(q21q26.2) or t(3;3)(q21;q26.2); RPN1-EVI1",
                PermissibleValue(text="Acute myeloid leukemia with inv(3)(q21q26.2) or t(3;3)(q21;q26.2); RPN1-EVI1") )
        setattr(cls, "Small cell sarcoma",
                PermissibleValue(text="Small cell sarcoma") )
        setattr(cls, "Neoplasm, malignant, uncertain whether primary or metastatic",
                PermissibleValue(text="Neoplasm, malignant, uncertain whether primary or metastatic") )
        setattr(cls, "Inflammatory adenocarcinoma",
                PermissibleValue(text="Inflammatory adenocarcinoma") )
        setattr(cls, "Telangiectatic osteosarcoma",
                PermissibleValue(text="Telangiectatic osteosarcoma") )
        setattr(cls, "Amelanotic melanoma",
                PermissibleValue(text="Amelanotic melanoma") )
        setattr(cls, "Atypical proliferating clear cell tumor",
                PermissibleValue(text="Atypical proliferating clear cell tumor") )
        setattr(cls, "Monoclonal gammopathy of undetermined significance",
                PermissibleValue(text="Monoclonal gammopathy of undetermined significance") )
        setattr(cls, "Acute myeloid leukaemia, t(8;21)(q22;q22)",
                PermissibleValue(text="Acute myeloid leukaemia, t(8;21)(q22;q22)") )
        setattr(cls, "Malignant lymphoma, convoluted cell",
                PermissibleValue(text="Malignant lymphoma, convoluted cell") )
        setattr(cls, "Adenoid cystic carcinoma",
                PermissibleValue(text="Adenoid cystic carcinoma") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, indeterminate type",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, indeterminate type") )
        setattr(cls, "Wilms tumor",
                PermissibleValue(text="Wilms tumor") )
        setattr(cls, "Clear cell tumor, NOS",
                PermissibleValue(text="Clear cell tumor, NOS") )
        setattr(cls, "Compound nevus",
                PermissibleValue(text="Compound nevus") )
        setattr(cls, "Sessile serrated adenoma",
                PermissibleValue(text="Sessile serrated adenoma") )
        setattr(cls, "Aggressive angiomyxoma",
                PermissibleValue(text="Aggressive angiomyxoma") )
        setattr(cls, "Endometrioid adenocarcinoma, secretory variant",
                PermissibleValue(text="Endometrioid adenocarcinoma, secretory variant") )
        setattr(cls, "Adult T-cell lymphoma/leukemia",
                PermissibleValue(text="Adult T-cell lymphoma/leukemia") )
        setattr(cls, "Intraductal papillary-mucinous tumor with low grade dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with low grade dysplasia") )
        setattr(cls, "Mucinous cystic tumor with moderate dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with moderate dysplasia") )
        setattr(cls, "Langerhans cell sarcoma",
                PermissibleValue(text="Langerhans cell sarcoma") )
        setattr(cls, "Ductal carcinoma in situ, papillary",
                PermissibleValue(text="Ductal carcinoma in situ, papillary") )
        setattr(cls, "Acute erythremia",
                PermissibleValue(text="Acute erythremia") )
        setattr(cls, "Urothelial carcinoma with trophoblastic differentiation",
                PermissibleValue(text="Urothelial carcinoma with trophoblastic differentiation") )
        setattr(cls, "Sarcoma botryoides",
                PermissibleValue(text="Sarcoma botryoides") )
        setattr(cls, "Papillocystic adenocarcinoma",
                PermissibleValue(text="Papillocystic adenocarcinoma") )
        setattr(cls, "Perivascular epithelioid cell tumor, malignant",
                PermissibleValue(text="Perivascular epithelioid cell tumor, malignant") )
        setattr(cls, "Alpha cell tumor, NOS",
                PermissibleValue(text="Alpha cell tumor, NOS") )
        setattr(cls, "Dermatofibroma, NOS",
                PermissibleValue(text="Dermatofibroma, NOS") )
        setattr(cls, "Squamous cell carcinoma, microinvasive",
                PermissibleValue(text="Squamous cell carcinoma, microinvasive") )
        setattr(cls, "Adamantinoma, NOS",
                PermissibleValue(text="Adamantinoma, NOS") )
        setattr(cls, "Extranodal NK/T-cell lymphoma, nasal type",
                PermissibleValue(text="Extranodal NK/T-cell lymphoma, nasal type") )
        setattr(cls, "Sezary disease",
                PermissibleValue(text="Sezary disease") )
        setattr(cls, "Intracystic papillary tumor with high grade entraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary tumor with high grade entraepithelial neoplasia") )
        setattr(cls, "Serous cystadenocarcinofibroma",
                PermissibleValue(text="Serous cystadenocarcinofibroma") )
        setattr(cls, "Waldenstrom macroglobulinemia",
                PermissibleValue(text="Waldenstrom macroglobulinemia") )
        setattr(cls, "Lymphoid leukemia, NOS",
                PermissibleValue(text="Lymphoid leukemia, NOS") )
        setattr(cls, "Hodgkin paragranuloma, nodular",
                PermissibleValue(text="Hodgkin paragranuloma, nodular") )
        setattr(cls, "Water-clear cell adenoma",
                PermissibleValue(text="Water-clear cell adenoma") )
        setattr(cls, "Transitional papilloma, inverted, NOS",
                PermissibleValue(text="Transitional papilloma, inverted, NOS") )
        setattr(cls, "Common ALL",
                PermissibleValue(text="Common ALL") )
        setattr(cls, "Clear cell adenofibroma of borderline malignancy",
                PermissibleValue(text="Clear cell adenofibroma of borderline malignancy") )
        setattr(cls, "Hemangiopericytoma, malignant",
                PermissibleValue(text="Hemangiopericytoma, malignant") )
        setattr(cls, "Bednar tumor",
                PermissibleValue(text="Bednar tumor") )
        setattr(cls, "Infiltrating and papillary adenocarcinoma",
                PermissibleValue(text="Infiltrating and papillary adenocarcinoma") )
        setattr(cls, "Ghost cell odontogenic carcinoma",
                PermissibleValue(text="Ghost cell odontogenic carcinoma") )
        setattr(cls, "Aleukemic granulocytic leukemia",
                PermissibleValue(text="Aleukemic granulocytic leukemia") )
        setattr(cls, "Pleomorphic lipoma",
                PermissibleValue(text="Pleomorphic lipoma") )
        setattr(cls, "Well differentiated papillary mesothelioma, benign",
                PermissibleValue(text="Well differentiated papillary mesothelioma, benign") )
        setattr(cls, "Invasive lobular carcinoma",
                PermissibleValue(text="Invasive lobular carcinoma") )
        setattr(cls, "Periosteal osteosarcoma",
                PermissibleValue(text="Periosteal osteosarcoma") )
        setattr(cls, "Odontogenic tumor, benign",
                PermissibleValue(text="Odontogenic tumor, benign") )
        setattr(cls, "Somatostatin cell tumor, NOS",
                PermissibleValue(text="Somatostatin cell tumor, NOS") )
        setattr(cls, "Refractory neutropenia",
                PermissibleValue(text="Refractory neutropenia") )
        setattr(cls, "Invasive mammary carcinoma",
                PermissibleValue(text="Invasive mammary carcinoma") )
        setattr(cls, "Aggressive digital papillary adenoma",
                PermissibleValue(text="Aggressive digital papillary adenoma") )
        setattr(cls, "Tubular adenoma, NOS",
                PermissibleValue(text="Tubular adenoma, NOS") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with hypodiploidy (Hypodiploid ALL)",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with hypodiploidy (Hypodiploid ALL)") )
        setattr(cls, "Granulosa cell tumor, NOS",
                PermissibleValue(text="Granulosa cell tumor, NOS") )
        setattr(cls, "Squamous cell carcinoma, metastatic, NOS",
                PermissibleValue(text="Squamous cell carcinoma, metastatic, NOS") )
        setattr(cls, "Follicular carcinoma, NOS",
                PermissibleValue(text="Follicular carcinoma, NOS") )
        setattr(cls, "Follicular adenoma",
                PermissibleValue(text="Follicular adenoma") )
        setattr(cls, "Malignant lymphoma, mixed small cleaved and large cell, follicular",
                PermissibleValue(text="Malignant lymphoma, mixed small cleaved and large cell, follicular") )
        setattr(cls, "Papillary serous tumor of low malignant potential",
                PermissibleValue(text="Papillary serous tumor of low malignant potential") )
        setattr(cls, "Acute monoblastic leukemia",
                PermissibleValue(text="Acute monoblastic leukemia") )
        setattr(cls, "Malignant lymphoma, large B-cell, diffuse, centroblastic, NOS",
                PermissibleValue(text="Malignant lymphoma, large B-cell, diffuse, centroblastic, NOS") )
        setattr(cls, "Intraductal carcinoma, solid type",
                PermissibleValue(text="Intraductal carcinoma, solid type") )
        setattr(cls, "Adenocarcinoma in situ in polypoid adenoma",
                PermissibleValue(text="Adenocarcinoma in situ in polypoid adenoma") )
        setattr(cls, "Mucoid cell adenoma",
                PermissibleValue(text="Mucoid cell adenoma") )
        setattr(cls, "Atypical medullary carcinoma",
                PermissibleValue(text="Atypical medullary carcinoma") )
        setattr(cls, "Mesenchymoma, benign",
                PermissibleValue(text="Mesenchymoma, benign") )
        setattr(cls, "Adenocarcinoma in villous adenoma",
                PermissibleValue(text="Adenocarcinoma in villous adenoma") )
        setattr(cls, "Serous papillary cystic tumor of borderline malignancy",
                PermissibleValue(text="Serous papillary cystic tumor of borderline malignancy") )
        setattr(cls, "Pick tubular adenoma",
                PermissibleValue(text="Pick tubular adenoma") )
        setattr(cls, "Carcinoma in situ, NOS",
                PermissibleValue(text="Carcinoma in situ, NOS") )
        setattr(cls, "Gastrointestinal autonomic nerve tumor",
                PermissibleValue(text="Gastrointestinal autonomic nerve tumor") )
        setattr(cls, "Malignant lymphoma, non-cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, non-cleaved cell, NOS") )
        setattr(cls, "Subependymal giant cell astrocytoma",
                PermissibleValue(text="Subependymal giant cell astrocytoma") )
        setattr(cls, "Juvenile fibroadenoma",
                PermissibleValue(text="Juvenile fibroadenoma") )
        setattr(cls, "Renal cell carcinoma, chromophobe type",
                PermissibleValue(text="Renal cell carcinoma, chromophobe type") )
        setattr(cls, "Granulocytic sarcoma",
                PermissibleValue(text="Granulocytic sarcoma") )
        setattr(cls, "Unclassified tumor, malignant",
                PermissibleValue(text="Unclassified tumor, malignant") )
        setattr(cls, "Multiple myeloma",
                PermissibleValue(text="Multiple myeloma") )
        setattr(cls, "Trabecular carcinoma",
                PermissibleValue(text="Trabecular carcinoma") )
        setattr(cls, "Plexiform fibromyxoma",
                PermissibleValue(text="Plexiform fibromyxoma") )
        setattr(cls, "Refractory cytopenia with multilineage dysplasia",
                PermissibleValue(text="Refractory cytopenia with multilineage dysplasia") )
        setattr(cls, "Balloon cell nevus",
                PermissibleValue(text="Balloon cell nevus") )
        setattr(cls, "Squamous cell carcinoma, large cell, nonkeratinizing, NOS",
                PermissibleValue(text="Squamous cell carcinoma, large cell, nonkeratinizing, NOS") )
        setattr(cls, "AML M6",
                PermissibleValue(text="AML M6") )
        setattr(cls, "Pseudomucinous cystadenocarcinoma, NOS",
                PermissibleValue(text="Pseudomucinous cystadenocarcinoma, NOS") )
        setattr(cls, "Adamantinoma, malignant",
                PermissibleValue(text="Adamantinoma, malignant") )
        setattr(cls, "Colloid adenocarcinoma",
                PermissibleValue(text="Colloid adenocarcinoma",
                                 description="Lung Mucinous Adenocarcinoma") )
        setattr(cls, "Chondromatosis, NOS",
                PermissibleValue(text="Chondromatosis, NOS") )
        setattr(cls, "Malignant lymphoma, undifferentiated cell type, NOS",
                PermissibleValue(text="Malignant lymphoma, undifferentiated cell type, NOS") )
        setattr(cls, "Aggressive fibromatosis",
                PermissibleValue(text="Aggressive fibromatosis") )
        setattr(cls, "Intraductal carcinoma, noninfiltrating, NOS",
                PermissibleValue(text="Intraductal carcinoma, noninfiltrating, NOS") )
        setattr(cls, "Intraneural perineurioma",
                PermissibleValue(text="Intraneural perineurioma") )
        setattr(cls, "Invasive carcinoma of no special type",
                PermissibleValue(text="Invasive carcinoma of no special type") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, NOS",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, NOS") )
        setattr(cls, "Mesothelial papilloma",
                PermissibleValue(text="Mesothelial papilloma") )
        setattr(cls, "Liver cell carcinoma",
                PermissibleValue(text="Liver cell carcinoma") )
        setattr(cls, "Erythremic myelosis, NOS",
                PermissibleValue(text="Erythremic myelosis, NOS") )
        setattr(cls, "Epithelioid glioblastoma",
                PermissibleValue(text="Epithelioid glioblastoma") )
        setattr(cls, "Papillary squamous cell carcinoma, non-invasive",
                PermissibleValue(text="Papillary squamous cell carcinoma, non-invasive") )
        setattr(cls, "Serous adenofibroma, NOS",
                PermissibleValue(text="Serous adenofibroma, NOS") )
        setattr(cls, "Mediastinal (thymic) large B-cell lymphoma",
                PermissibleValue(text="Mediastinal (thymic) large B-cell lymphoma") )
        setattr(cls, "Sclerosing hepatic carcinoma",
                PermissibleValue(text="Sclerosing hepatic carcinoma") )
        setattr(cls, "Glassy cell carcinoma",
                PermissibleValue(text="Glassy cell carcinoma") )
        setattr(cls, "Ewing sarcoma",
                PermissibleValue(text="Ewing sarcoma") )
        setattr(cls, "Myeloid neoplasms with PDGFRB rearrangement",
                PermissibleValue(text="Myeloid neoplasms with PDGFRB rearrangement") )
        setattr(cls, "Acute myelocytic leukemia",
                PermissibleValue(text="Acute myelocytic leukemia") )
        setattr(cls, "Non-invasive encapsulated follicular variant of papillary thyroid carcinoma (non-invasive EFVPTC)",
                PermissibleValue(text="Non-invasive encapsulated follicular variant of papillary thyroid carcinoma (non-invasive EFVPTC)") )
        setattr(cls, "Marginal zone lymphoma, NOS",
                PermissibleValue(text="Marginal zone lymphoma, NOS",
                                 description="Marginal Zone Lymphoma Not Otherwise Specified") )
        setattr(cls, "Pleomorphic rhabdomyosarcoma, NOS",
                PermissibleValue(text="Pleomorphic rhabdomyosarcoma, NOS") )
        setattr(cls, "Islet cell tumor, benign",
                PermissibleValue(text="Islet cell tumor, benign") )
        setattr(cls, "Pseudosarcomatous carcinoma",
                PermissibleValue(text="Pseudosarcomatous carcinoma") )
        setattr(cls, "Carcinoma with osseous differentiation",
                PermissibleValue(text="Carcinoma with osseous differentiation") )
        setattr(cls, "Somatostatinoma, NOS",
                PermissibleValue(text="Somatostatinoma, NOS") )
        setattr(cls, "Glioblastoma with sarcomatous component",
                PermissibleValue(text="Glioblastoma with sarcomatous component") )
        setattr(cls, "Mesenteric fibromatosis",
                PermissibleValue(text="Mesenteric fibromatosis") )
        setattr(cls, "Large granular lymphocytosis, NOS",
                PermissibleValue(text="Large granular lymphocytosis, NOS") )
        setattr(cls, "Intradermal nevus",
                PermissibleValue(text="Intradermal nevus") )
        setattr(cls, "Mesenchymoma, malignant",
                PermissibleValue(text="Mesenchymoma, malignant") )
        setattr(cls, "Lymphomatoid granulomatosis",
                PermissibleValue(text="Lymphomatoid granulomatosis") )
        setattr(cls, "Mesothelioma, NOS",
                PermissibleValue(text="Mesothelioma, NOS") )
        setattr(cls, "Thymoma, medullary, NOS",
                PermissibleValue(text="Thymoma, medullary, NOS") )
        setattr(cls, "Urothelial carcinoma with divergent differentiation",
                PermissibleValue(text="Urothelial carcinoma with divergent differentiation") )
        setattr(cls, "Adenocarcinoma with osseous metaplasia",
                PermissibleValue(text="Adenocarcinoma with osseous metaplasia") )
        setattr(cls, "Gamma heavy chain disease",
                PermissibleValue(text="Gamma heavy chain disease") )
        setattr(cls, "Epidermoid carcinoma in situ with questionable stromal invasion",
                PermissibleValue(text="Epidermoid carcinoma in situ with questionable stromal invasion") )
        setattr(cls, "Giant cell fibroblastoma",
                PermissibleValue(text="Giant cell fibroblastoma") )
        setattr(cls, "Malignant lymphoma, non-Hodgkin, NOS",
                PermissibleValue(text="Malignant lymphoma, non-Hodgkin, NOS") )
        setattr(cls, "Anaplastic large cell lymphoma, CD30+",
                PermissibleValue(text="Anaplastic large cell lymphoma, CD30+") )
        setattr(cls, "Adenocarcinoma in situ, NOS",
                PermissibleValue(text="Adenocarcinoma in situ, NOS") )
        setattr(cls, "Malignant mast cell tumor",
                PermissibleValue(text="Malignant mast cell tumor") )
        setattr(cls, "Malignant lymphoma, small B lymphocytic, NOS",
                PermissibleValue(text="Malignant lymphoma, small B lymphocytic, NOS") )
        setattr(cls, "Malignant midline reticulosis",
                PermissibleValue(text="Malignant midline reticulosis") )
        setattr(cls, "Giant fibroadenoma",
                PermissibleValue(text="Giant fibroadenoma") )
        setattr(cls, "Mixed teratoma and seminoma",
                PermissibleValue(text="Mixed teratoma and seminoma") )
        setattr(cls, "Franklin disease",
                PermissibleValue(text="Franklin disease") )
        setattr(cls, "Gliomatosis cerebri",
                PermissibleValue(text="Gliomatosis cerebri") )
        setattr(cls, "Mixed tumor, NOS",
                PermissibleValue(text="Mixed tumor, NOS") )
        setattr(cls, "Epithelial tumor, benign",
                PermissibleValue(text="Epithelial tumor, benign") )
        setattr(cls, "Acute myeloid leukemia, t(16;16)(p 13;q 11)",
                PermissibleValue(text="Acute myeloid leukemia, t(16;16)(p 13;q 11)") )
        setattr(cls, "T-cell large granular lymphocytic leukemia",
                PermissibleValue(text="T-cell large granular lymphocytic leukemia") )
        setattr(cls, "Infiltrating duct adenocarcinoma",
                PermissibleValue(text="Infiltrating duct adenocarcinoma") )
        setattr(cls, "Acinar cell cystadenocarcinoma",
                PermissibleValue(text="Acinar cell cystadenocarcinoma",
                                 description="Pancreatic Acinar Cell Cystadenocarcinoma") )
        setattr(cls, "Glandular papilloma",
                PermissibleValue(text="Glandular papilloma") )
        setattr(cls, "Hemangioma, NOS",
                PermissibleValue(text="Hemangioma, NOS") )
        setattr(cls, "Pilomyxoid astrocytoma",
                PermissibleValue(text="Pilomyxoid astrocytoma") )
        setattr(cls, "Precursor T-cell lymphoblastic lymphoma",
                PermissibleValue(text="Precursor T-cell lymphoblastic lymphoma") )
        setattr(cls, "Ductal carcinoma in situ, comedo type",
                PermissibleValue(text="Ductal carcinoma in situ, comedo type") )
        setattr(cls, "Thecoma, NOS",
                PermissibleValue(text="Thecoma, NOS") )
        setattr(cls, "Adenocarcinoma, endocervical type",
                PermissibleValue(text="Adenocarcinoma, endocervical type") )
        setattr(cls, "Epithelioid cell nevus",
                PermissibleValue(text="Epithelioid cell nevus") )
        setattr(cls, "Pulmonary blastoma",
                PermissibleValue(text="Pulmonary blastoma") )
        setattr(cls, "Glomoid sarcoma",
                PermissibleValue(text="Glomoid sarcoma") )
        setattr(cls, "Follicular lymphoma, NOS",
                PermissibleValue(text="Follicular lymphoma, NOS") )
        setattr(cls, "Brenner tumor, proliferating",
                PermissibleValue(text="Brenner tumor, proliferating") )
        setattr(cls, "Mixed acidophil-basophil adenoma",
                PermissibleValue(text="Mixed acidophil-basophil adenoma") )
        setattr(cls, "Papilloma, NOS",
                PermissibleValue(text="Papilloma, NOS") )
        setattr(cls, "Sarcomatoid mesothelioma",
                PermissibleValue(text="Sarcomatoid mesothelioma",
                                 description="Sarcomatoid Mesothelioma") )
        setattr(cls, "Malignant lymphoma, small lymphocytic, diffuse",
                PermissibleValue(text="Malignant lymphoma, small lymphocytic, diffuse") )
        setattr(cls, "Hodgkin lymphoma, lymphocyte predominance, nodular",
                PermissibleValue(text="Hodgkin lymphoma, lymphocyte predominance, nodular") )
        setattr(cls, "Acute myelomonocytic leukemia",
                PermissibleValue(text="Acute myelomonocytic leukemia") )
        setattr(cls, "Atypical fibroxanthoma",
                PermissibleValue(text="Atypical fibroxanthoma") )
        setattr(cls, "Indeterminate dendritic cell tumor",
                PermissibleValue(text="Indeterminate dendritic cell tumor") )
        setattr(cls, "Psammomatous meningioma",
                PermissibleValue(text="Psammomatous meningioma") )
        setattr(cls, "Basophil adenocarcinoma",
                PermissibleValue(text="Basophil adenocarcinoma") )
        setattr(cls, "Water-clear cell carcinoma",
                PermissibleValue(text="Water-clear cell carcinoma") )
        setattr(cls, "Neuroendocrine tumor, grade 1",
                PermissibleValue(text="Neuroendocrine tumor, grade 1") )
        setattr(cls, "Malignant lymphoma, lymphocytic, poorly differentiated, diffuse",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, poorly differentiated, diffuse") )
        setattr(cls, "Pleomorphic xanthoastrocytoma",
                PermissibleValue(text="Pleomorphic xanthoastrocytoma") )
        setattr(cls, "Cribriform carcinoma, NOS",
                PermissibleValue(text="Cribriform carcinoma, NOS") )
        setattr(cls, "Adamantinoma of long bones",
                PermissibleValue(text="Adamantinoma of long bones") )
        setattr(cls, "Inflammatory myofibroblastic tumor",
                PermissibleValue(text="Inflammatory myofibroblastic tumor",
                                 description="Inflammatory Myofibroblastic Tumor") )
        setattr(cls, "Thymoma, cortical, NOS",
                PermissibleValue(text="Thymoma, cortical, NOS") )
        setattr(cls, "Metaplastic carcinoma with other types mesenchymal differentiation",
                PermissibleValue(text="Metaplastic carcinoma with other types mesenchymal differentiation") )
        setattr(cls, "Angioimmunoblastic T-cell lymphoma",
                PermissibleValue(text="Angioimmunoblastic T-cell lymphoma") )
        setattr(cls, "Acute erythroid leukaemia",
                PermissibleValue(text="Acute erythroid leukaemia") )
        setattr(cls, "Solid and papillary epithelial neoplasm",
                PermissibleValue(text="Solid and papillary epithelial neoplasm") )
        setattr(cls, "Melanocytoma, eyeball",
                PermissibleValue(text="Melanocytoma, eyeball") )
        setattr(cls, "Retroperitoneal fibromatosis",
                PermissibleValue(text="Retroperitoneal fibromatosis") )
        setattr(cls, "Immature teratoma, NOS",
                PermissibleValue(text="Immature teratoma, NOS") )
        setattr(cls, "Classical Hodgkin lymphoma, nodular sclerosis, cellular phase",
                PermissibleValue(text="Classical Hodgkin lymphoma, nodular sclerosis, cellular phase") )
        setattr(cls, "Abdominal fibromatosis",
                PermissibleValue(text="Abdominal fibromatosis") )
        setattr(cls, "Thymoma, organoid, NOS",
                PermissibleValue(text="Thymoma, organoid, NOS") )
        setattr(cls, "Angiocentric glioma",
                PermissibleValue(text="Angiocentric glioma") )
        setattr(cls, "Nerve sheath myxoma",
                PermissibleValue(text="Nerve sheath myxoma") )
        setattr(cls, "Involuting nevus",
                PermissibleValue(text="Involuting nevus") )
        setattr(cls, "Adenocarcinoma in situ in tubulovillous adenoma",
                PermissibleValue(text="Adenocarcinoma in situ in tubulovillous adenoma") )
        setattr(cls, "Mast cell sarcoma",
                PermissibleValue(text="Mast cell sarcoma") )
        setattr(cls, "Acute myeloid leukemia, MLL",
                PermissibleValue(text="Acute myeloid leukemia, MLL") )
        setattr(cls, "Renomedullary interstitial cell tumor",
                PermissibleValue(text="Renomedullary interstitial cell tumor") )
        setattr(cls, "Acute myeloid leukemia, minimal differentiation",
                PermissibleValue(text="Acute myeloid leukemia, minimal differentiation") )
        setattr(cls, "Reserve cell carcinoma",
                PermissibleValue(text="Reserve cell carcinoma") )
        setattr(cls, "Minimally invasive adenocarcinoma, NOS",
                PermissibleValue(text="Minimally invasive adenocarcinoma, NOS") )
        setattr(cls, "Monoclonal gammopathy, NOS",
                PermissibleValue(text="Monoclonal gammopathy, NOS") )
        setattr(cls, "Gelatinous carcinoma",
                PermissibleValue(text="Gelatinous carcinoma") )
        setattr(cls, "Gastrointestinal stromal tumor, malignant",
                PermissibleValue(text="Gastrointestinal stromal tumor, malignant") )
        setattr(cls, "Hydatidiform mole, NOS",
                PermissibleValue(text="Hydatidiform mole, NOS") )
        setattr(cls, "Retinoblastoma, spontaneously regressed",
                PermissibleValue(text="Retinoblastoma, spontaneously regressed") )
        setattr(cls, "Bronchiolo-alveolar adenocarcinoma, NOS",
                PermissibleValue(text="Bronchiolo-alveolar adenocarcinoma, NOS") )
        setattr(cls, "Serous cystadenocarcinoma, NOS",
                PermissibleValue(text="Serous cystadenocarcinoma, NOS") )
        setattr(cls, "Spongioblastoma polare",
                PermissibleValue(text="Spongioblastoma polare") )
        setattr(cls, "Leydig cell tumor, benign",
                PermissibleValue(text="Leydig cell tumor, benign") )
        setattr(cls, "Chronic myelogenous leukemia, t(9;22)(q34;q11)",
                PermissibleValue(text="Chronic myelogenous leukemia, t(9;22)(q34;q11)") )
        setattr(cls, "Adenocarcinoma with spindle cell metaplasia",
                PermissibleValue(text="Adenocarcinoma with spindle cell metaplasia") )
        setattr(cls, "Complete hydatidiform mole",
                PermissibleValue(text="Complete hydatidiform mole") )
        setattr(cls, "Malignant lymphoma, follicular, NOS",
                PermissibleValue(text="Malignant lymphoma, follicular, NOS") )
        setattr(cls, "Intraductal tubular-papillary neoplasm, low grade",
                PermissibleValue(text="Intraductal tubular-papillary neoplasm, low grade") )
        setattr(cls, "Parietal cell carcinoma",
                PermissibleValue(text="Parietal cell carcinoma") )
        setattr(cls, "Clear cell cystadenofibroma",
                PermissibleValue(text="Clear cell cystadenofibroma") )
        setattr(cls, "Adenocarcinoma of anal ducts",
                PermissibleValue(text="Adenocarcinoma of anal ducts") )
        setattr(cls, "Subacute granulocytic leukemia",
                PermissibleValue(text="Subacute granulocytic leukemia") )
        setattr(cls, "Esophageal squamous intraepithelial neoplasia (dysplasia), high grade",
                PermissibleValue(text="Esophageal squamous intraepithelial neoplasia (dysplasia), high grade") )
        setattr(cls, "Classical Hodgkin lymphoma, lymphocyte-rich",
                PermissibleValue(text="Classical Hodgkin lymphoma, lymphocyte-rich") )
        setattr(cls, "Adenocarcinoma admixed with neuroendocrine carcinoma",
                PermissibleValue(text="Adenocarcinoma admixed with neuroendocrine carcinoma") )
        setattr(cls, "Abdominal desmoid",
                PermissibleValue(text="Abdominal desmoid") )
        setattr(cls, "Thymoma, atypical, NOS",
                PermissibleValue(text="Thymoma, atypical, NOS") )
        setattr(cls, "Fibrous meningioma",
                PermissibleValue(text="Fibrous meningioma") )
        setattr(cls, "Malignant lymphoma, small cell, noncleaved, diffuse",
                PermissibleValue(text="Malignant lymphoma, small cell, noncleaved, diffuse") )
        setattr(cls, "Polymorphous low grade adenocarcinoma",
                PermissibleValue(text="Polymorphous low grade adenocarcinoma") )
        setattr(cls, "Primary amyloidosis",
                PermissibleValue(text="Primary amyloidosis") )
        setattr(cls, "Cellular leiomyoma",
                PermissibleValue(text="Cellular leiomyoma") )
        setattr(cls, "Nonchromaffin paraganglioma, NOS",
                PermissibleValue(text="Nonchromaffin paraganglioma, NOS") )
        setattr(cls, "Lipomatous medulloblastoma",
                PermissibleValue(text="Lipomatous medulloblastoma") )
        setattr(cls, "Mesonephric tumor, NOS",
                PermissibleValue(text="Mesonephric tumor, NOS") )
        setattr(cls, "Chondroid syringoma",
                PermissibleValue(text="Chondroid syringoma") )
        setattr(cls, "Infiltrating duct mixed with other types of carcinoma",
                PermissibleValue(text="Infiltrating duct mixed with other types of carcinoma") )
        setattr(cls, "Mucin-producing adenocarcinoma",
                PermissibleValue(text="Mucin-producing adenocarcinoma") )
        setattr(cls, "Clear cell cystadenocarcinofibroma",
                PermissibleValue(text="Clear cell cystadenocarcinofibroma") )
        setattr(cls, "Lipoma-like liposarcoma",
                PermissibleValue(text="Lipoma-like liposarcoma") )
        setattr(cls, "Central odontogenic fibroma",
                PermissibleValue(text="Central odontogenic fibroma") )
        setattr(cls, "Mucin-producing carcinoma",
                PermissibleValue(text="Mucin-producing carcinoma") )
        setattr(cls, "Mucinous cystic neoplasm with high-grade dysplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with high-grade dysplasia") )
        setattr(cls, "Acute promyelocytic leukaemia, t(15;17)(q22;q11-12)",
                PermissibleValue(text="Acute promyelocytic leukaemia, t(15;17)(q22;q11-12)") )
        setattr(cls, "Traditional serrated adenoma",
                PermissibleValue(text="Traditional serrated adenoma") )
        setattr(cls, "Paraganglioma, benign",
                PermissibleValue(text="Paraganglioma, benign") )
        setattr(cls, "Common precursor B ALL",
                PermissibleValue(text="Common precursor B ALL") )
        setattr(cls, "Clear cell meningioma",
                PermissibleValue(text="Clear cell meningioma") )
        setattr(cls, "Adenocarcinoma combined with other types of carcinoma",
                PermissibleValue(text="Adenocarcinoma combined with other types of carcinoma") )
        setattr(cls, "Refractory anemia with ring sideroblasts associated with marked thrombocytosis",
                PermissibleValue(text="Refractory anemia with ring sideroblasts associated with marked thrombocytosis") )
        setattr(cls, "Metatypical carcinoma",
                PermissibleValue(text="Metatypical carcinoma") )
        setattr(cls, "Papillomatosis, glandular",
                PermissibleValue(text="Papillomatosis, glandular") )
        setattr(cls, "Pleomorphic cell sarcoma",
                PermissibleValue(text="Pleomorphic cell sarcoma") )
        setattr(cls, "Interdigitating cell sarcoma",
                PermissibleValue(text="Interdigitating cell sarcoma") )
        setattr(cls, "Intraductal papillary-mucinous tumor with intermediate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous tumor with intermediate dysplasia") )
        setattr(cls, "Basal cell carcinoma, micronodular",
                PermissibleValue(text="Basal cell carcinoma, micronodular") )
        setattr(cls, "Alveolar adenocarcinoma",
                PermissibleValue(text="Alveolar adenocarcinoma") )
        setattr(cls, "Infiltrating duct carcinoma, NOS",
                PermissibleValue(text="Infiltrating duct carcinoma, NOS") )
        setattr(cls, "Infiltrating basal cell carcinoma, sclerosing",
                PermissibleValue(text="Infiltrating basal cell carcinoma, sclerosing") )
        setattr(cls, "Rhabdomyoma, NOS",
                PermissibleValue(text="Rhabdomyoma, NOS") )
        setattr(cls, "Pituitary adenoma, NOS",
                PermissibleValue(text="Pituitary adenoma, NOS") )
        setattr(cls, "Tanycytic ependymoma",
                PermissibleValue(text="Tanycytic ependymoma") )
        setattr(cls, "Malignant lymphoma, large cell, cleaved, diffuse",
                PermissibleValue(text="Malignant lymphoma, large cell, cleaved, diffuse") )
        setattr(cls, "Subacute myeloid leukemia",
                PermissibleValue(text="Subacute myeloid leukemia") )
        setattr(cls, "Rhabdomyosarcoma with ganglionic differentiation",
                PermissibleValue(text="Rhabdomyosarcoma with ganglionic differentiation") )
        setattr(cls, "Pancreatic endocrine tumor, nonfunctioning",
                PermissibleValue(text="Pancreatic endocrine tumor, nonfunctioning") )
        setattr(cls, "Sertoli cell adenoma",
                PermissibleValue(text="Sertoli cell adenoma") )
        setattr(cls, "Cavernous hemangioma",
                PermissibleValue(text="Cavernous hemangioma") )
        setattr(cls, "Lentigo maligna",
                PermissibleValue(text="Lentigo maligna") )
        setattr(cls, "Cystosarcoma phyllodes, NOS",
                PermissibleValue(text="Cystosarcoma phyllodes, NOS") )
        setattr(cls, "Lobular and ductal carcinoma",
                PermissibleValue(text="Lobular and ductal carcinoma") )
        setattr(cls, "Malignant lymphoma, small cell diffuse",
                PermissibleValue(text="Malignant lymphoma, small cell diffuse") )
        setattr(cls, "Sebaceous epithelioma",
                PermissibleValue(text="Sebaceous epithelioma") )
        setattr(cls, "Lymphoblastic leukemia, NOS",
                PermissibleValue(text="Lymphoblastic leukemia, NOS") )
        setattr(cls, "Embryonal tumor with rhabdoid features",
                PermissibleValue(text="Embryonal tumor with rhabdoid features") )
        setattr(cls, "Metastatic signet ring cell carcinoma",
                PermissibleValue(text="Metastatic signet ring cell carcinoma") )
        setattr(cls, "Atypical lipoma",
                PermissibleValue(text="Atypical lipoma") )
        setattr(cls, "Peripheral T-cell lymphoma, large cell",
                PermissibleValue(text="Peripheral T-cell lymphoma, large cell") )
        setattr(cls, "Sebaceous carcinoma",
                PermissibleValue(text="Sebaceous carcinoma") )
        setattr(cls, "Choriocarcinoma, NOS",
                PermissibleValue(text="Choriocarcinoma, NOS") )
        setattr(cls, "Well differentiated liposarcoma of superficial soft tissue",
                PermissibleValue(text="Well differentiated liposarcoma of superficial soft tissue") )
        setattr(cls, "Tumor, malignant, NOS",
                PermissibleValue(text="Tumor, malignant, NOS") )
        setattr(cls, "Spindle cell melanoma, type A",
                PermissibleValue(text="Spindle cell melanoma, type A") )
        setattr(cls, "Carcinoma in pleomorphic adenoma",
                PermissibleValue(text="Carcinoma in pleomorphic adenoma") )
        setattr(cls, "Anaplastic large cell lymphoma, T cell and Null cell type",
                PermissibleValue(text="Anaplastic large cell lymphoma, T cell and Null cell type") )
        setattr(cls, "Low-grade intramedullary osteosarcoma",
                PermissibleValue(text="Low-grade intramedullary osteosarcoma") )
        setattr(cls, "Histiocytoid hemangioma",
                PermissibleValue(text="Histiocytoid hemangioma") )
        setattr(cls, "Multiple meningiomas",
                PermissibleValue(text="Multiple meningiomas") )
        setattr(cls, "Hepatocellular carcinoma, NOS",
                PermissibleValue(text="Hepatocellular carcinoma, NOS") )
        setattr(cls, "Pilar tumor",
                PermissibleValue(text="Pilar tumor") )
        setattr(cls, "Transitional carcinoma",
                PermissibleValue(text="Transitional carcinoma") )
        setattr(cls, "Pigmented schwannoma",
                PermissibleValue(text="Pigmented schwannoma") )
        setattr(cls, "Chronic granulocytic leukemia, BCR/ABL",
                PermissibleValue(text="Chronic granulocytic leukemia, BCR/ABL") )
        setattr(cls, "Small cell neuroendocrine carcinoma",
                PermissibleValue(text="Small cell neuroendocrine carcinoma",
                                 description="Colorectal Small Cell Neuroendocrine Carcinoma") )
        setattr(cls, "Monocytoid B-cell lymphoma",
                PermissibleValue(text="Monocytoid B-cell lymphoma") )
        setattr(cls, "Mixed tumor, salivary gland type, NOS",
                PermissibleValue(text="Mixed tumor, salivary gland type, NOS") )
        setattr(cls, "Fibrous histiocytoma of tendon sheath",
                PermissibleValue(text="Fibrous histiocytoma of tendon sheath") )
        setattr(cls, "Therapy related myeloid neoplasm",
                PermissibleValue(text="Therapy related myeloid neoplasm") )
        setattr(cls, "Hodgkin disease, nodular sclerosis, lymphocyte predominance",
                PermissibleValue(text="Hodgkin disease, nodular sclerosis, lymphocyte predominance") )
        setattr(cls, "Infiltrating lobular carcinoma and ductal carcinoma in situ",
                PermissibleValue(text="Infiltrating lobular carcinoma and ductal carcinoma in situ") )
        setattr(cls, "Intraductal papillary neoplasm with intermediate grade neoplasia",
                PermissibleValue(text="Intraductal papillary neoplasm with intermediate grade neoplasia") )
        setattr(cls, "Granulosa cell tumor, adult type",
                PermissibleValue(text="Granulosa cell tumor, adult type",
                                 description="Adult Type Ovarian Granulosa Cell Tumor") )
        setattr(cls, "Plexiform hemangioma",
                PermissibleValue(text="Plexiform hemangioma") )
        setattr(cls, "Benign cystic nephroma",
                PermissibleValue(text="Benign cystic nephroma") )
        setattr(cls, "Vipoma, NOS",
                PermissibleValue(text="Vipoma, NOS") )
        setattr(cls, "Carcinoma simplex",
                PermissibleValue(text="Carcinoma simplex") )
        setattr(cls, "Papillary carcinoma, follicular variant",
                PermissibleValue(text="Papillary carcinoma, follicular variant") )
        setattr(cls, "Papillary and follicular carcinoma",
                PermissibleValue(text="Papillary and follicular carcinoma") )
        setattr(cls, "Endocervical adenocarcinoma usual type",
                PermissibleValue(text="Endocervical adenocarcinoma usual type") )
        setattr(cls, "Pre-pre-B ALL",
                PermissibleValue(text="Pre-pre-B ALL") )
        setattr(cls, "Pre-B ALL",
                PermissibleValue(text="Pre-B ALL") )
        setattr(cls, "G cell tumor, NOS",
                PermissibleValue(text="G cell tumor, NOS") )
        setattr(cls, "Diffuse astrocytoma, low grade",
                PermissibleValue(text="Diffuse astrocytoma, low grade") )
        setattr(cls, "Secretory meningioma",
                PermissibleValue(text="Secretory meningioma") )
        setattr(cls, "Serous tumor, NOS, of low malignant potential",
                PermissibleValue(text="Serous tumor, NOS, of low malignant potential") )
        setattr(cls, "Dermatofibrosarcoma, NOS",
                PermissibleValue(text="Dermatofibrosarcoma, NOS") )
        setattr(cls, "Carcinoma with productive fibrosis",
                PermissibleValue(text="Carcinoma with productive fibrosis") )
        setattr(cls, "Seminoma, NOS",
                PermissibleValue(text="Seminoma, NOS") )
        setattr(cls, "Hodgkin lymphoma, nodular sclerosis, grade 2",
                PermissibleValue(text="Hodgkin lymphoma, nodular sclerosis, grade 2") )
        setattr(cls, "Ceruminous adenoma",
                PermissibleValue(text="Ceruminous adenoma") )
        setattr(cls, "Von Recklinghausen disease",
                PermissibleValue(text="Von Recklinghausen disease") )
        setattr(cls, "Oncocytic Schneiderian papilloma",
                PermissibleValue(text="Oncocytic Schneiderian papilloma") )
        setattr(cls, "Chondroblastoma, malignant",
                PermissibleValue(text="Chondroblastoma, malignant") )
        setattr(cls, "Oxyphilic adenocarcinoma",
                PermissibleValue(text="Oxyphilic adenocarcinoma") )
        setattr(cls, "Liposarcoma, well differentiated",
                PermissibleValue(text="Liposarcoma, well differentiated") )
        setattr(cls, "Plasmacytoma, NOS",
                PermissibleValue(text="Plasmacytoma, NOS") )
        setattr(cls, "Non-invasive FTP",
                PermissibleValue(text="Non-invasive FTP") )
        setattr(cls, "Endometrioid adenocarcinoma, villoglandular",
                PermissibleValue(text="Endometrioid adenocarcinoma, villoglandular") )
        setattr(cls, "Pigmented spindle cell nevus of Reed",
                PermissibleValue(text="Pigmented spindle cell nevus of Reed") )
        setattr(cls, "Marginal zone B-cell lymphoma, NOS",
                PermissibleValue(text="Marginal zone B-cell lymphoma, NOS") )
        setattr(cls, "Endometrial sarcoma, NOS",
                PermissibleValue(text="Endometrial sarcoma, NOS") )
        setattr(cls, "Dermoid cyst, NOS",
                PermissibleValue(text="Dermoid cyst, NOS") )
        setattr(cls, "Terminal duct adenocarcinoma",
                PermissibleValue(text="Terminal duct adenocarcinoma") )
        setattr(cls, "Adenomatous polyposis coli",
                PermissibleValue(text="Adenomatous polyposis coli") )
        setattr(cls, "Squamous cell carcinoma, HPV-positive",
                PermissibleValue(text="Squamous cell carcinoma, HPV-positive") )
        setattr(cls, "Pleomorphic rhabdomyosarcoma, adult type",
                PermissibleValue(text="Pleomorphic rhabdomyosarcoma, adult type") )
        setattr(cls, "Diffuse large B-cell lymphoma, NOS",
                PermissibleValue(text="Diffuse large B-cell lymphoma, NOS") )
        setattr(cls, "Carcinoma in situ in a polyp, NOS",
                PermissibleValue(text="Carcinoma in situ in a polyp, NOS") )
        setattr(cls, "Hepatoid adenocarcinoma",
                PermissibleValue(text="Hepatoid adenocarcinoma",
                                 description="Hepatoid Adenocarcinoma") )
        setattr(cls, "Pulmonary adenomatosis",
                PermissibleValue(text="Pulmonary adenomatosis") )
        setattr(cls, "Intraductal papillary tumor with high grade dysplasia",
                PermissibleValue(text="Intraductal papillary tumor with high grade dysplasia") )
        setattr(cls, "Pleomorphic leiomyoma",
                PermissibleValue(text="Pleomorphic leiomyoma") )
        setattr(cls, "Renal cell carcinoma, spindle cell",
                PermissibleValue(text="Renal cell carcinoma, spindle cell") )
        setattr(cls, "Granular cell myoblastoma, malignant",
                PermissibleValue(text="Granular cell myoblastoma, malignant") )
        setattr(cls, "Atypical chronic myeloid leukemia, Philadelphia chromosome (Ph1) negative",
                PermissibleValue(text="Atypical chronic myeloid leukemia, Philadelphia chromosome (Ph1) negative") )
        setattr(cls, "Glandular intraepithelial neoplasia, low grade",
                PermissibleValue(text="Glandular intraepithelial neoplasia, low grade") )
        setattr(cls, "Complex odontoma",
                PermissibleValue(text="Complex odontoma") )
        setattr(cls, "Solitary myeloma",
                PermissibleValue(text="Solitary myeloma") )
        setattr(cls, "Meningeal melanoma",
                PermissibleValue(text="Meningeal melanoma") )
        setattr(cls, "Leiomyomatosis, NOS",
                PermissibleValue(text="Leiomyomatosis, NOS") )
        setattr(cls, "Cellular schwannoma",
                PermissibleValue(text="Cellular schwannoma") )
        setattr(cls, "Intraductal papillary-mucinous neoplasm with moderate dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous neoplasm with moderate dysplasia") )
        setattr(cls, "RAEB I",
                PermissibleValue(text="RAEB I") )
        setattr(cls, "Glomus tumor, NOS",
                PermissibleValue(text="Glomus tumor, NOS") )
        setattr(cls, "Plasma cell tumor",
                PermissibleValue(text="Plasma cell tumor") )
        setattr(cls, "Hemangioma simplex",
                PermissibleValue(text="Hemangioma simplex") )
        setattr(cls, "Malignant lymphoma, histiocytic, NOS",
                PermissibleValue(text="Malignant lymphoma, histiocytic, NOS") )
        setattr(cls, "MPNST with rhabdomyoblastic differentiation",
                PermissibleValue(text="MPNST with rhabdomyoblastic differentiation") )
        setattr(cls, "Esophageal glandular dysplasia (intraepithelial neoplasia), low grade",
                PermissibleValue(text="Esophageal glandular dysplasia (intraepithelial neoplasia), low grade") )
        setattr(cls, "Mesodermal mixed tumor",
                PermissibleValue(text="Mesodermal mixed tumor") )
        setattr(cls, "Atypical fibrous histiocytoma",
                PermissibleValue(text="Atypical fibrous histiocytoma") )
        setattr(cls, "Tubulovillous adenoma, NOS",
                PermissibleValue(text="Tubulovillous adenoma, NOS") )
        setattr(cls, "Carcinoma with apocrine metaplasia",
                PermissibleValue(text="Carcinoma with apocrine metaplasia") )
        setattr(cls, "Germ cell tumor, NOS",
                PermissibleValue(text="Germ cell tumor, NOS") )
        setattr(cls, "Intraductal papillary-mucinous adenoma",
                PermissibleValue(text="Intraductal papillary-mucinous adenoma") )
        setattr(cls, "Transitional papilloma",
                PermissibleValue(text="Transitional papilloma") )
        setattr(cls, "Endometrial stromal sarcoma, low grade",
                PermissibleValue(text="Endometrial stromal sarcoma, low grade") )
        setattr(cls, "Ductal papilloma",
                PermissibleValue(text="Ductal papilloma") )
        setattr(cls, "FAB Ll",
                PermissibleValue(text="FAB Ll") )
        setattr(cls, "Liposarcoma, NOS",
                PermissibleValue(text="Liposarcoma, NOS") )
        setattr(cls, "Follicular adenocarcinoma, trabecular",
                PermissibleValue(text="Follicular adenocarcinoma, trabecular") )
        setattr(cls, "Cystoma, NOS",
                PermissibleValue(text="Cystoma, NOS") )
        setattr(cls, "Anaplastic astrocytoma, IDH-wildtype",
                PermissibleValue(text="Anaplastic astrocytoma, IDH-wildtype") )
        setattr(cls, "Acinic cell tumor",
                PermissibleValue(text="Acinic cell tumor") )
        setattr(cls, "Lymphomatoid papulosis",
                PermissibleValue(text="Lymphomatoid papulosis") )
        setattr(cls, "Renal carcinoma, collecting duct type",
                PermissibleValue(text="Renal carcinoma, collecting duct type") )
        setattr(cls, "Pigmented dermatofibrosarcoma protuberans",
                PermissibleValue(text="Pigmented dermatofibrosarcoma protuberans") )
        setattr(cls, "Essential thrombocythemia",
                PermissibleValue(text="Essential thrombocythemia") )
        setattr(cls, "Fibrous histiocytoma, NOS",
                PermissibleValue(text="Fibrous histiocytoma, NOS") )
        setattr(cls, "B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and Burkitt lymphoma",
                PermissibleValue(text="B-cell lymphoma, unclassifiable, with features intermediate between diffuse large B-cell lymphoma and Burkitt lymphoma") )
        setattr(cls, "Adnexal carcinoma",
                PermissibleValue(text="Adnexal carcinoma") )
        setattr(cls, "Perifollicular fibroma",
                PermissibleValue(text="Perifollicular fibroma") )
        setattr(cls, "Hilar cell tumor",
                PermissibleValue(text="Hilar cell tumor") )
        setattr(cls, "Acute lymphoblastic leukemia-lymphoma, NOS",
                PermissibleValue(text="Acute lymphoblastic leukemia-lymphoma, NOS") )
        setattr(cls, "Mixed cell adenocarcinoma",
                PermissibleValue(text="Mixed cell adenocarcinoma") )
        setattr(cls, "Splenic lymphoma with villous lymphocytes",
                PermissibleValue(text="Splenic lymphoma with villous lymphocytes") )
        setattr(cls, "Anaplastic oligoastrocytoma",
                PermissibleValue(text="Anaplastic oligoastrocytoma") )
        setattr(cls, "Follicular carcinoma, encapsulated",
                PermissibleValue(text="Follicular carcinoma, encapsulated") )
        setattr(cls, "Intracortical osteosarcoma",
                PermissibleValue(text="Intracortical osteosarcoma") )
        setattr(cls, "Mucinous cystic neoplasm with low-grade intraepithelial neoplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with low-grade intraepithelial neoplasia") )
        setattr(cls, "Myxoinflammatory fibroblastic sarcoma (MIFS)",
                PermissibleValue(text="Myxoinflammatory fibroblastic sarcoma (MIFS)") )
        setattr(cls, "Thymic carcinoma with adenoid cystic carcinoma-like features",
                PermissibleValue(text="Thymic carcinoma with adenoid cystic carcinoma-like features") )
        setattr(cls, "Prolymphocytic leukemia, T-cell type",
                PermissibleValue(text="Prolymphocytic leukemia, T-cell type") )
        setattr(cls, "Sertoli-Leydig cell tumor, retiform",
                PermissibleValue(text="Sertoli-Leydig cell tumor, retiform") )
        setattr(cls, "Schwannoma, NOS",
                PermissibleValue(text="Schwannoma, NOS") )
        setattr(cls, "Warthin tumor",
                PermissibleValue(text="Warthin tumor") )
        setattr(cls, "Intraepidermal nevus",
                PermissibleValue(text="Intraepidermal nevus") )
        setattr(cls, "Congenital peribronchial myofibroblastic tumor",
                PermissibleValue(text="Congenital peribronchial myofibroblastic tumor") )
        setattr(cls, "Malignant lymphoma, diffuse, NOS",
                PermissibleValue(text="Malignant lymphoma, diffuse, NOS") )
        setattr(cls, "Transitional cell carcinoma, micropapillary",
                PermissibleValue(text="Transitional cell carcinoma, micropapillary") )
        setattr(cls, "Diffuse large B-cell lymphoma associated with chronic inflammation",
                PermissibleValue(text="Diffuse large B-cell lymphoma associated with chronic inflammation") )
        setattr(cls, "Microcystic adenoma",
                PermissibleValue(text="Microcystic adenoma") )
        setattr(cls, "Atypical follicular adenoma",
                PermissibleValue(text="Atypical follicular adenoma") )
        setattr(cls, "Aleukemic leukemia, NOS",
                PermissibleValue(text="Aleukemic leukemia, NOS") )
        setattr(cls, "Acute myeloid leukemia with t(9;11)(p22;q23); MLLT3-MLL",
                PermissibleValue(text="Acute myeloid leukemia with t(9;11)(p22;q23); MLLT3-MLL") )
        setattr(cls, "Megakaryocytic myelosclerosis",
                PermissibleValue(text="Megakaryocytic myelosclerosis") )
        setattr(cls, "Round cell liposarcoma",
                PermissibleValue(text="Round cell liposarcoma") )
        setattr(cls, "Malignant lymphoma, mixed cell type, nodular",
                PermissibleValue(text="Malignant lymphoma, mixed cell type, nodular") )
        setattr(cls, "High grade surface osteosarcoma",
                PermissibleValue(text="High grade surface osteosarcoma") )
        setattr(cls, "Acute leukemia, NOS",
                PermissibleValue(text="Acute leukemia, NOS") )
        setattr(cls, "Craniopharyngioma, adamantinomatous",
                PermissibleValue(text="Craniopharyngioma, adamantinomatous") )
        setattr(cls, "Medulloblastoma, SHH-activated and TP53-wildtype",
                PermissibleValue(text="Medulloblastoma, SHH-activated and TP53-wildtype") )
        setattr(cls, "Pilomatricoma, malignant",
                PermissibleValue(text="Pilomatricoma, malignant") )
        setattr(cls, "Lymphangioendothelial sarcoma",
                PermissibleValue(text="Lymphangioendothelial sarcoma") )
        setattr(cls, "Kaposiform hemangioendothelioma",
                PermissibleValue(text="Kaposiform hemangioendothelioma") )
        setattr(cls, "Intraductal papillary neoplasm with associated invasive carcinoma",
                PermissibleValue(text="Intraductal papillary neoplasm with associated invasive carcinoma") )
        setattr(cls, "Pilomatrix carcinoma",
                PermissibleValue(text="Pilomatrix carcinoma") )
        setattr(cls, "Neoplasm, benign",
                PermissibleValue(text="Neoplasm, benign") )
        setattr(cls, "Mucosal-associated lymphoid tissue lymphoma",
                PermissibleValue(text="Mucosal-associated lymphoid tissue lymphoma") )
        setattr(cls, "Hepatoid yolk sac tumor",
                PermissibleValue(text="Hepatoid yolk sac tumor") )
        setattr(cls, "Angioimmunoblastic lymphoma",
                PermissibleValue(text="Angioimmunoblastic lymphoma") )
        setattr(cls, "Linitis plastica",
                PermissibleValue(text="Linitis plastica") )
        setattr(cls, "Ganglioglioma, anaplastic",
                PermissibleValue(text="Ganglioglioma, anaplastic") )
        setattr(cls, "Malignant lymphoma, Hodgkin",
                PermissibleValue(text="Malignant lymphoma, Hodgkin") )
        setattr(cls, "Papillary renal cell carcinoma",
                PermissibleValue(text="Papillary renal cell carcinoma") )
        setattr(cls, "PEComa, malignant",
                PermissibleValue(text="PEComa, malignant") )
        setattr(cls, "Florid osseous dysplasia",
                PermissibleValue(text="Florid osseous dysplasia") )
        setattr(cls, "Follicular lymphoma, grade 3",
                PermissibleValue(text="Follicular lymphoma, grade 3") )
        setattr(cls, "Olfactory neurocytoma",
                PermissibleValue(text="Olfactory neurocytoma") )
        setattr(cls, "Acinar cell carcinoma",
                PermissibleValue(text="Acinar cell carcinoma",
                                 description="Acinar Cell Carcinoma") )
        setattr(cls, "Pinkus tumor",
                PermissibleValue(text="Pinkus tumor") )
        setattr(cls, "Glioblastoma multiforme",
                PermissibleValue(text="Glioblastoma multiforme") )
        setattr(cls, "Mixed epithelioid and spindle cell melanoma",
                PermissibleValue(text="Mixed epithelioid and spindle cell melanoma") )
        setattr(cls, "Mesothelioma, benign",
                PermissibleValue(text="Mesothelioma, benign") )
        setattr(cls, "Papillary squamous cell carcinoma in situ",
                PermissibleValue(text="Papillary squamous cell carcinoma in situ") )
        setattr(cls, "Intracystic papillary neoplasm with intermediate grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary neoplasm with intermediate grade intraepithelial neoplasia") )
        setattr(cls, "Idiopathic thrombocythemia",
                PermissibleValue(text="Idiopathic thrombocythemia") )
        setattr(cls, "FAB L3",
                PermissibleValue(text="FAB L3") )
        setattr(cls, "Intracystic papillary adenocarcinoma",
                PermissibleValue(text="Intracystic papillary adenocarcinoma") )
        setattr(cls, "Osteoblastic sarcoma",
                PermissibleValue(text="Osteoblastic sarcoma") )
        setattr(cls, "Subepidermal nodular fibrosis",
                PermissibleValue(text="Subepidermal nodular fibrosis") )
        setattr(cls, "Reticulosarcoma, diffuse",
                PermissibleValue(text="Reticulosarcoma, diffuse") )
        setattr(cls, "Malignant lymphoma, centroblastic, NOS",
                PermissibleValue(text="Malignant lymphoma, centroblastic, NOS") )
        setattr(cls, "Regressing nevus",
                PermissibleValue(text="Regressing nevus") )
        setattr(cls, "Squamous papilloma",
                PermissibleValue(text="Squamous papilloma") )
        setattr(cls, "Intraductal papillary neoplasm with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intraductal papillary neoplasm with high grade intraepithelial neoplasia") )
        setattr(cls, "Medulloepithelioma, NOS",
                PermissibleValue(text="Medulloepithelioma, NOS") )
        setattr(cls, "Melanotic psammomatous MPNST",
                PermissibleValue(text="Melanotic psammomatous MPNST") )
        setattr(cls, "Giant osteoid osteoma",
                PermissibleValue(text="Giant osteoid osteoma") )
        setattr(cls, "Low-grade serous carcinoma",
                PermissibleValue(text="Low-grade serous carcinoma") )
        setattr(cls, "Langerhans cell histiocytosis, disseminated",
                PermissibleValue(text="Langerhans cell histiocytosis, disseminated") )
        setattr(cls, "Sertoli cell tumor, NOS",
                PermissibleValue(text="Sertoli cell tumor, NOS") )
        setattr(cls, "Fibroxanthoma, NOS",
                PermissibleValue(text="Fibroxanthoma, NOS") )
        setattr(cls, "Therapy-related acute myeloid leukemia, epipodophyllotoxin-related",
                PermissibleValue(text="Therapy-related acute myeloid leukemia, epipodophyllotoxin-related") )
        setattr(cls, "Myelomonocytic leukemia, NOS",
                PermissibleValue(text="Myelomonocytic leukemia, NOS") )
        setattr(cls, "Small cell carcinoma, fusiform cell",
                PermissibleValue(text="Small cell carcinoma, fusiform cell") )
        setattr(cls, "Epithelioma, benign",
                PermissibleValue(text="Epithelioma, benign") )
        setattr(cls, "Myelodysplastic/myeloproliferative neoplasm, unclassifiable",
                PermissibleValue(text="Myelodysplastic/myeloproliferative neoplasm, unclassifiable") )
        setattr(cls, "Congenital generalized fibromatosis",
                PermissibleValue(text="Congenital generalized fibromatosis") )
        setattr(cls, "B-cell lymphocytic leukemia/small lymphocytic lymphoma",
                PermissibleValue(text="B-cell lymphocytic leukemia/small lymphocytic lymphoma") )
        setattr(cls, "Papillary carcinoma, tall cell",
                PermissibleValue(text="Papillary carcinoma, tall cell") )
        setattr(cls, "Stromal myosis, NOS",
                PermissibleValue(text="Stromal myosis, NOS") )
        setattr(cls, "Peripheral neuroectodermal tumor",
                PermissibleValue(text="Peripheral neuroectodermal tumor") )
        setattr(cls, "Odontoma, NOS",
                PermissibleValue(text="Odontoma, NOS") )
        setattr(cls, "Leydig cell tumor, malignant",
                PermissibleValue(text="Leydig cell tumor, malignant") )
        setattr(cls, "Desmoplastic mesothelioma",
                PermissibleValue(text="Desmoplastic mesothelioma",
                                 description="Desmoplastic Mesothelioma") )
        setattr(cls, "Acute myeloid leukemia with maturation",
                PermissibleValue(text="Acute myeloid leukemia with maturation") )
        setattr(cls, "Fetal adenocarcinoma",
                PermissibleValue(text="Fetal adenocarcinoma") )
        setattr(cls, "Anaplastic astrocytoma, IDH-mutant",
                PermissibleValue(text="Anaplastic astrocytoma, IDH-mutant") )
        setattr(cls, "VIN III",
                PermissibleValue(text="VIN III") )
        setattr(cls, "Leptomeningeal sarcoma",
                PermissibleValue(text="Leptomeningeal sarcoma") )
        setattr(cls, "Noninfiltrating intracystic carcinoma",
                PermissibleValue(text="Noninfiltrating intracystic carcinoma") )
        setattr(cls, "Blastic NK cell lymphoma",
                PermissibleValue(text="Blastic NK cell lymphoma") )
        setattr(cls, "Squamous intraepithelial neoplasia, grade I",
                PermissibleValue(text="Squamous intraepithelial neoplasia, grade I") )
        setattr(cls, "Classical Hodgkin lymphoma, lymphocyte depletion, reticular",
                PermissibleValue(text="Classical Hodgkin lymphoma, lymphocyte depletion, reticular") )
        setattr(cls, "Intraductal papillary neoplasm, NOS",
                PermissibleValue(text="Intraductal papillary neoplasm, NOS") )
        setattr(cls, "Granulocytic leukemia, NOS",
                PermissibleValue(text="Granulocytic leukemia, NOS") )
        setattr(cls, "Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)",
                PermissibleValue(text="Encapsulated follicular variant of papillary thyroid carcinoma, NOS (EFVPTC, NOS)") )
        setattr(cls, "Hemangioblastic meningioma",
                PermissibleValue(text="Hemangioblastic meningioma") )
        setattr(cls, "Epithelioma, malignant",
                PermissibleValue(text="Epithelioma, malignant") )
        setattr(cls, "Mixed embryonal carcinoma and teratoma",
                PermissibleValue(text="Mixed embryonal carcinoma and teratoma") )
        setattr(cls, "Epidermoid carcinoma, large cell, nonkeratinizing",
                PermissibleValue(text="Epidermoid carcinoma, large cell, nonkeratinizing") )
        setattr(cls, "Invasive fibroma",
                PermissibleValue(text="Invasive fibroma") )
        setattr(cls, "Solid papillary carcinoma with invasion",
                PermissibleValue(text="Solid papillary carcinoma with invasion") )
        setattr(cls, "Mesenchymal chondrosarcoma",
                PermissibleValue(text="Mesenchymal chondrosarcoma") )
        setattr(cls, "Acute lymphocytic leukemia",
                PermissibleValue(text="Acute lymphocytic leukemia") )
        setattr(cls, "Malignant serous cystadenofibroma",
                PermissibleValue(text="Malignant serous cystadenofibroma") )
        setattr(cls, "High-grade neuroendocrine carcinoma",
                PermissibleValue(text="High-grade neuroendocrine carcinoma") )
        setattr(cls, "Myelodysplastic syndrome with 5q deletion (5q-) syndrome",
                PermissibleValue(text="Myelodysplastic syndrome with 5q deletion (5q-) syndrome") )
        setattr(cls, "Multicentric basal cell carcinoma",
                PermissibleValue(text="Multicentric basal cell carcinoma") )
        setattr(cls, "Mixed liposarcoma",
                PermissibleValue(text="Mixed liposarcoma") )
        setattr(cls, "Neurogenic sarcoma",
                PermissibleValue(text="Neurogenic sarcoma") )
        setattr(cls, "Papillary adenocarcinoma, NOS",
                PermissibleValue(text="Papillary adenocarcinoma, NOS") )
        setattr(cls, "Recklinghausen disease",
                PermissibleValue(text="Recklinghausen disease") )
        setattr(cls, "Thymoma, medullary, malignant",
                PermissibleValue(text="Thymoma, medullary, malignant") )
        setattr(cls, "Spermatocytic seminoma",
                PermissibleValue(text="Spermatocytic seminoma") )
        setattr(cls, "Solitary fibrous tumor/hemangiopericytoma Grade 2 (CNS)",
                PermissibleValue(text="Solitary fibrous tumor/hemangiopericytoma Grade 2 (CNS)") )
        setattr(cls, "Squamous odontogenic tumor",
                PermissibleValue(text="Squamous odontogenic tumor") )
        setattr(cls, "Glycogenic rhabdomyoma",
                PermissibleValue(text="Glycogenic rhabdomyoma") )
        setattr(cls, "Spindle cell sarcoma",
                PermissibleValue(text="Spindle cell sarcoma") )
        setattr(cls, "Lymphoplasmacyte-rich meningioma",
                PermissibleValue(text="Lymphoplasmacyte-rich meningioma") )
        setattr(cls, "Synovial sarcoma, monophasic fibrous",
                PermissibleValue(text="Synovial sarcoma, monophasic fibrous") )
        setattr(cls, "Mesonephroma, benign",
                PermissibleValue(text="Mesonephroma, benign") )
        setattr(cls, "Acidophil adenocarcinoma",
                PermissibleValue(text="Acidophil adenocarcinoma") )
        setattr(cls, "Large cell medulloblastoma",
                PermissibleValue(text="Large cell medulloblastoma") )
        setattr(cls, "Intraosseous well differentiated osteosarcoma",
                PermissibleValue(text="Intraosseous well differentiated osteosarcoma") )
        setattr(cls, "Multiple endocrine adenomas",
                PermissibleValue(text="Multiple endocrine adenomas") )
        setattr(cls, "Malignant lymphoma, large cleaved cell, follicular",
                PermissibleValue(text="Malignant lymphoma, large cleaved cell, follicular") )
        setattr(cls, "Carotid body paraganglioma",
                PermissibleValue(text="Carotid body paraganglioma") )
        setattr(cls, "Bronchio-alveolar carcinoma, mixed mucinous and non-mucinous",
                PermissibleValue(text="Bronchio-alveolar carcinoma, mixed mucinous and non-mucinous") )
        setattr(cls, "Myeloma, NOS",
                PermissibleValue(text="Myeloma, NOS") )
        setattr(cls, "Mesenchymoma, NOS",
                PermissibleValue(text="Mesenchymoma, NOS") )
        setattr(cls, "Malignant lymphoma, large cell, immunoblastic",
                PermissibleValue(text="Malignant lymphoma, large cell, immunoblastic") )
        setattr(cls, "Chronic idiopathic myelofibrosis",
                PermissibleValue(text="Chronic idiopathic myelofibrosis") )
        setattr(cls, "Diffuse midline glioma, H3 K27M-mutant",
                PermissibleValue(text="Diffuse midline glioma, H3 K27M-mutant") )
        setattr(cls, "Calcifying nested epithelial stromal tumor",
                PermissibleValue(text="Calcifying nested epithelial stromal tumor") )
        setattr(cls, "Cemento-ossifying fibroma",
                PermissibleValue(text="Cemento-ossifying fibroma") )
        setattr(cls, "Aleukemic lymphoid leukemia",
                PermissibleValue(text="Aleukemic lymphoid leukemia") )
        setattr(cls, "Hepatoid carcinoma",
                PermissibleValue(text="Hepatoid carcinoma") )
        setattr(cls, "Hepatosplenic T-cell lymphoma",
                PermissibleValue(text="Hepatosplenic T-cell lymphoma") )
        setattr(cls, "Fibrosarcoma, NOS",
                PermissibleValue(text="Fibrosarcoma, NOS") )
        setattr(cls, "Intracystic papilloma",
                PermissibleValue(text="Intracystic papilloma") )
        setattr(cls, "Transitional cell carcinoma in situ",
                PermissibleValue(text="Transitional cell carcinoma in situ") )
        setattr(cls, "Classical Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis",
                PermissibleValue(text="Classical Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis") )
        setattr(cls, "Pulmonary myxoid sarcoma with EWSR1-CREB1 translocation",
                PermissibleValue(text="Pulmonary myxoid sarcoma with EWSR1-CREB1 translocation") )
        setattr(cls, "Cystosarcoma phyllodes, malignant",
                PermissibleValue(text="Cystosarcoma phyllodes, malignant") )
        setattr(cls, "Precancerous melanosis, NOS",
                PermissibleValue(text="Precancerous melanosis, NOS") )
        setattr(cls, "Digital papillary adenocarcinoma",
                PermissibleValue(text="Digital papillary adenocarcinoma") )
        setattr(cls, "Malignant lymphoma, histiocytic, nodular",
                PermissibleValue(text="Malignant lymphoma, histiocytic, nodular") )
        setattr(cls, "Phyllodes tumor, malignant",
                PermissibleValue(text="Phyllodes tumor, malignant") )
        setattr(cls, "Liposarcoma, differentiated",
                PermissibleValue(text="Liposarcoma, differentiated") )
        setattr(cls, "Subependymal astrocytoma, NOS",
                PermissibleValue(text="Subependymal astrocytoma, NOS") )
        setattr(cls, "Myxoid fibroma",
                PermissibleValue(text="Myxoid fibroma") )
        setattr(cls, "Lymphoproliferative disorder, NOS",
                PermissibleValue(text="Lymphoproliferative disorder, NOS") )
        setattr(cls, "Sclerosing epithelioid fibrosarcoma",
                PermissibleValue(text="Sclerosing epithelioid fibrosarcoma") )
        setattr(cls, "Hemangioendothelioma, malignant",
                PermissibleValue(text="Hemangioendothelioma, malignant") )
        setattr(cls, "Acute myeloid leukemia without prior myelodysplastic syndrome",
                PermissibleValue(text="Acute myeloid leukemia without prior myelodysplastic syndrome") )
        setattr(cls, "Grawitz tumor",
                PermissibleValue(text="Grawitz tumor") )
        setattr(cls, "Primitive neuroectodermal tumor, NOS",
                PermissibleValue(text="Primitive neuroectodermal tumor, NOS") )
        setattr(cls, "Acute myeloid leukemia with prior myelodysplastic syndrome",
                PermissibleValue(text="Acute myeloid leukemia with prior myelodysplastic syndrome") )
        setattr(cls, "Carcinoid tumor of uncertain malignant potential",
                PermissibleValue(text="Carcinoid tumor of uncertain malignant potential") )
        setattr(cls, "Ossifying fibromyxoid tumor",
                PermissibleValue(text="Ossifying fibromyxoid tumor") )
        setattr(cls, "T-cell large granular lymphocytosis",
                PermissibleValue(text="T-cell large granular lymphocytosis") )
        setattr(cls, "Malignant lymphoma, large B-cell, NOS",
                PermissibleValue(text="Malignant lymphoma, large B-cell, NOS") )
        setattr(cls, "Embryonal carcinoma, infantile",
                PermissibleValue(text="Embryonal carcinoma, infantile") )
        setattr(cls, "Urachal carcinoma",
                PermissibleValue(text="Urachal carcinoma") )
        setattr(cls, "Malignant lymphoma, large cell, noncleaved, follicular",
                PermissibleValue(text="Malignant lymphoma, large cell, noncleaved, follicular") )
        setattr(cls, "Hairy cell leukaemia variant",
                PermissibleValue(text="Hairy cell leukaemia variant") )
        setattr(cls, "Solitary fibrous tumor/hemangiopericytoma Grade 1 (CNS)",
                PermissibleValue(text="Solitary fibrous tumor/hemangiopericytoma Grade 1 (CNS)") )
        setattr(cls, "Aggressive systemic mastocytosis",
                PermissibleValue(text="Aggressive systemic mastocytosis") )
        setattr(cls, "Microcystic adnexal carcinoma",
                PermissibleValue(text="Microcystic adnexal carcinoma") )
        setattr(cls, "Paget disease and infiltrating duct carcinoma of breast",
                PermissibleValue(text="Paget disease and infiltrating duct carcinoma of breast") )
        setattr(cls, "Adenocarcinoma, cylindroid",
                PermissibleValue(text="Adenocarcinoma, cylindroid") )
        setattr(cls, "Ossifying fibroma",
                PermissibleValue(text="Ossifying fibroma") )
        setattr(cls, "Carcinoma showing thymus-like element",
                PermissibleValue(text="Carcinoma showing thymus-like element") )
        setattr(cls, "Transitional cell papilloma, benign",
                PermissibleValue(text="Transitional cell papilloma, benign") )
        setattr(cls, "Endometrioid cystadenofibroma, malignant",
                PermissibleValue(text="Endometrioid cystadenofibroma, malignant") )
        setattr(cls, "Granulosa cell tumor, sarcomatoid",
                PermissibleValue(text="Granulosa cell tumor, sarcomatoid") )
        setattr(cls, "Carcinoma in a polyp, NOS",
                PermissibleValue(text="Carcinoma in a polyp, NOS") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, Clara cell",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, Clara cell") )
        setattr(cls, "Fibroma, NOS",
                PermissibleValue(text="Fibroma, NOS") )
        setattr(cls, "Signet ring cell adenocarcinoma",
                PermissibleValue(text="Signet ring cell adenocarcinoma") )
        setattr(cls, "Adrenal cortical adenoma, NOS",
                PermissibleValue(text="Adrenal cortical adenoma, NOS") )
        setattr(cls, "Verrucous papilloma",
                PermissibleValue(text="Verrucous papilloma") )
        setattr(cls, "Bronchial adenoma, carcinoid",
                PermissibleValue(text="Bronchial adenoma, carcinoid") )
        setattr(cls, "Refractory anemia with excess blasts",
                PermissibleValue(text="Refractory anemia with excess blasts") )
        setattr(cls, "Dendritic cell sarcoma, NOS",
                PermissibleValue(text="Dendritic cell sarcoma, NOS") )
        setattr(cls, "Epithelioid hemangioendothelioma, NOS",
                PermissibleValue(text="Epithelioid hemangioendothelioma, NOS") )
        setattr(cls, "Hepatocellular carcinoma, fibrolamellar",
                PermissibleValue(text="Hepatocellular carcinoma, fibrolamellar") )
        setattr(cls, "Nodular hidradenoma, malignant",
                PermissibleValue(text="Nodular hidradenoma, malignant") )
        setattr(cls, "Dedifferentiated liposarcoma",
                PermissibleValue(text="Dedifferentiated liposarcoma",
                                 description="Dedifferentiated Liposarcoma") )
        setattr(cls, "Mucinous cystadenocarcinoma, NOS",
                PermissibleValue(text="Mucinous cystadenocarcinoma, NOS") )
        setattr(cls, "Acute panmyelosis, NOS",
                PermissibleValue(text="Acute panmyelosis, NOS") )
        setattr(cls, "Adenocarcinoma in situ in villous adenoma",
                PermissibleValue(text="Adenocarcinoma in situ in villous adenoma") )
        setattr(cls, "Immunoproliferative disease, NOS",
                PermissibleValue(text="Immunoproliferative disease, NOS") )
        setattr(cls, "Hodgkin lymphoma, nodular sclerosis, NOS",
                PermissibleValue(text="Hodgkin lymphoma, nodular sclerosis, NOS") )
        setattr(cls, "Subareolar duct papillomatosis",
                PermissibleValue(text="Subareolar duct papillomatosis") )
        setattr(cls, "Pleomorphic carcinoma",
                PermissibleValue(text="Pleomorphic carcinoma") )
        setattr(cls, "Myeloid and lymphoid neoplasms with PDGFRA rearrangement",
                PermissibleValue(text="Myeloid and lymphoid neoplasms with PDGFRA rearrangement") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with t(1;19)(q23;p13.3); E2A-PBX1 (TCF3-PBX1)",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with t(1;19)(q23;p13.3); E2A-PBX1 (TCF3-PBX1)") )
        setattr(cls, "Chronic granulocytic leukemia, Philadelphia chromosome (Ph1) positive",
                PermissibleValue(text="Chronic granulocytic leukemia, Philadelphia chromosome (Ph1) positive") )
        setattr(cls, "Di Guglielmo disease",
                PermissibleValue(text="Di Guglielmo disease") )
        setattr(cls, "Acinar carcinoma",
                PermissibleValue(text="Acinar carcinoma") )
        setattr(cls, "Paraganglioma, malignant",
                PermissibleValue(text="Paraganglioma, malignant") )
        setattr(cls, "Water-clear cell adenocarcinoma",
                PermissibleValue(text="Water-clear cell adenocarcinoma") )
        setattr(cls, "Ossifying fibromyxoid tumor, malignant",
                PermissibleValue(text="Ossifying fibromyxoid tumor, malignant") )
        setattr(cls, "Subcutaneous panniculitis-like T-cell lymphoma",
                PermissibleValue(text="Subcutaneous panniculitis-like T-cell lymphoma") )
        setattr(cls, "Diffuse meningiomatosis",
                PermissibleValue(text="Diffuse meningiomatosis") )
        setattr(cls, "Extra-adrenal paraganglioma, NOS",
                PermissibleValue(text="Extra-adrenal paraganglioma, NOS") )
        setattr(cls, "Atypical carcinoid tumor",
                PermissibleValue(text="Atypical carcinoid tumor") )
        setattr(cls, "Neoplasm, malignant",
                PermissibleValue(text="Neoplasm, malignant") )
        setattr(cls, "Theca cell-granulosa cell tumor",
                PermissibleValue(text="Theca cell-granulosa cell tumor") )
        setattr(cls, "Ductal carcinoma, cribriform type",
                PermissibleValue(text="Ductal carcinoma, cribriform type") )
        setattr(cls, "Adult teratoma, NOS",
                PermissibleValue(text="Adult teratoma, NOS") )
        setattr(cls, "Adrenal cortical adenoma, mixed cell",
                PermissibleValue(text="Adrenal cortical adenoma, mixed cell") )
        setattr(cls, "Granular cell adenocarcinoma",
                PermissibleValue(text="Granular cell adenocarcinoma") )
        setattr(cls, "Eccrine adenocarcinoma",
                PermissibleValue(text="Eccrine adenocarcinoma") )
        setattr(cls, "Giant cell tumor of soft parts, NOS",
                PermissibleValue(text="Giant cell tumor of soft parts, NOS") )
        setattr(cls, "Fetal lipoma, NOS",
                PermissibleValue(text="Fetal lipoma, NOS") )
        setattr(cls, "Infiltrating duct and mucinous carcinoma",
                PermissibleValue(text="Infiltrating duct and mucinous carcinoma") )
        setattr(cls, "Mucocarcinoid tumor",
                PermissibleValue(text="Mucocarcinoid tumor") )
        setattr(cls, "Choroid plexus carcinoma",
                PermissibleValue(text="Choroid plexus carcinoma") )
        setattr(cls, "Papillary mucinous cystadenoma, NOS",
                PermissibleValue(text="Papillary mucinous cystadenoma, NOS") )
        setattr(cls, "Sclerosing hemangioma",
                PermissibleValue(text="Sclerosing hemangioma") )
        setattr(cls, "Serotonin producing carcinoid",
                PermissibleValue(text="Serotonin producing carcinoid") )
        setattr(cls, "Cellular ependymoma",
                PermissibleValue(text="Cellular ependymoma") )
        setattr(cls, "Serrated adenoma",
                PermissibleValue(text="Serrated adenoma") )
        setattr(cls, "Traditional sessile serrated adenoma",
                PermissibleValue(text="Traditional sessile serrated adenoma") )
        setattr(cls, "Mucoepidermoid carcinoma",
                PermissibleValue(text="Mucoepidermoid carcinoma",
                                 description="Mucoepidermoid Carcinoma") )
        setattr(cls, "Desmoplastic small round cell tumor",
                PermissibleValue(text="Desmoplastic small round cell tumor") )
        setattr(cls, "Atypical leiomyoma",
                PermissibleValue(text="Atypical leiomyoma") )
        setattr(cls, "Cystadenocarcinoma, NOS",
                PermissibleValue(text="Cystadenocarcinoma, NOS") )
        setattr(cls, "Subacute lymphocytic leukemia",
                PermissibleValue(text="Subacute lymphocytic leukemia") )
        setattr(cls, "Infiltrating duct and colloid carcinoma",
                PermissibleValue(text="Infiltrating duct and colloid carcinoma") )
        setattr(cls, "Chordoma, NOS",
                PermissibleValue(text="Chordoma, NOS") )
        setattr(cls, "Perineural MPNST",
                PermissibleValue(text="Perineural MPNST") )
        setattr(cls, "Mesenchymal tumor, malignant",
                PermissibleValue(text="Mesenchymal tumor, malignant") )
        setattr(cls, "Intraductal carcinoma, NOS",
                PermissibleValue(text="Intraductal carcinoma, NOS") )
        setattr(cls, "Strumal carcinoid",
                PermissibleValue(text="Strumal carcinoid") )
        setattr(cls, "Nephrogenic adenofibroma",
                PermissibleValue(text="Nephrogenic adenofibroma") )
        setattr(cls, "Basophil adenoma",
                PermissibleValue(text="Basophil adenoma") )
        setattr(cls, "Hepatocellular carcinoma, scirrhous",
                PermissibleValue(text="Hepatocellular carcinoma, scirrhous") )
        setattr(cls, "Synovioma, NOS",
                PermissibleValue(text="Synovioma, NOS") )
        setattr(cls, "Lymphoepithelial carcinoma",
                PermissibleValue(text="Lymphoepithelial carcinoma",
                                 description="Nasopharyngeal Type Undifferentiated Carcinoma") )
        setattr(cls, "Acidophil carcinoma",
                PermissibleValue(text="Acidophil carcinoma") )
        setattr(cls, "Mucoepidermoid tumor",
                PermissibleValue(text="Mucoepidermoid tumor") )
        setattr(cls, "Mucinous cystadenocarcinoma, non-invasive",
                PermissibleValue(text="Mucinous cystadenocarcinoma, non-invasive") )
        setattr(cls, "Squamous intraepithelial neoplasia, grade II",
                PermissibleValue(text="Squamous intraepithelial neoplasia, grade II") )
        setattr(cls, "Lymphosarcoma, diffuse",
                PermissibleValue(text="Lymphosarcoma, diffuse") )
        setattr(cls, "Mixed adenocarcinoma and squamous cell carcinoma",
                PermissibleValue(text="Mixed adenocarcinoma and squamous cell carcinoma") )
        setattr(cls, "Small cell carcinoma, hypercalcemic type",
                PermissibleValue(text="Small cell carcinoma, hypercalcemic type",
                                 description="Ovarian Small Cell Carcinoma, Hypercalcemic Type") )
        setattr(cls, "Typical carcinoid",
                PermissibleValue(text="Typical carcinoid") )
        setattr(cls, "FAB M3 (includes all variants)",
                PermissibleValue(text="FAB M3 (includes all variants)") )
        setattr(cls, "Oncocytic carcinoma",
                PermissibleValue(text="Oncocytic carcinoma",
                                 description="Oxyphilic Adenocarcinoma") )
        setattr(cls, "Craniopharyngioma, papillary",
                PermissibleValue(text="Craniopharyngioma, papillary") )
        setattr(cls, "Syringoma, NOS",
                PermissibleValue(text="Syringoma, NOS") )
        setattr(cls, "Flat intraepithelial neoplasia, high grade",
                PermissibleValue(text="Flat intraepithelial neoplasia, high grade") )
        setattr(cls, "Primary myelofibrosis",
                PermissibleValue(text="Primary myelofibrosis") )
        setattr(cls, "Plasmacytoma of bone",
                PermissibleValue(text="Plasmacytoma of bone") )
        setattr(cls, "Teratoid medulloepithelioma, benign",
                PermissibleValue(text="Teratoid medulloepithelioma, benign") )
        setattr(cls, "Interdigitating dendritic cell sarcoma",
                PermissibleValue(text="Interdigitating dendritic cell sarcoma") )
        setattr(cls, "Plexiform neurofibroma",
                PermissibleValue(text="Plexiform neurofibroma") )
        setattr(cls, "Thymoma, type B1, NOS",
                PermissibleValue(text="Thymoma, type B1, NOS") )
        setattr(cls, "Infiltrating angiolipoma",
                PermissibleValue(text="Infiltrating angiolipoma") )
        setattr(cls, "Low-grade fibromyxoid sarcoma",
                PermissibleValue(text="Low-grade fibromyxoid sarcoma") )
        setattr(cls, "Sebaceous adenoma",
                PermissibleValue(text="Sebaceous adenoma") )
        setattr(cls, "Serous cystadenoma, borderline malignancy",
                PermissibleValue(text="Serous cystadenoma, borderline malignancy") )
        setattr(cls, "Tumor embolus",
                PermissibleValue(text="Tumor embolus") )
        setattr(cls, "Subependymal glioma",
                PermissibleValue(text="Subependymal glioma") )
        setattr(cls, "Synovial sarcoma, epithelioid cell",
                PermissibleValue(text="Synovial sarcoma, epithelioid cell") )
        setattr(cls, "Sweat gland tumor, NOS",
                PermissibleValue(text="Sweat gland tumor, NOS") )
        setattr(cls, "Parietal cell adenocarcinoma",
                PermissibleValue(text="Parietal cell adenocarcinoma") )
        setattr(cls, "Letterer-Siwe disease",
                PermissibleValue(text="Letterer-Siwe disease") )
        setattr(cls, "Clear cell adenoma",
                PermissibleValue(text="Clear cell adenoma") )
        setattr(cls, "Follicular thyroid carcinoma (FTC), encapsulated angioinvasive",
                PermissibleValue(text="Follicular thyroid carcinoma (FTC), encapsulated angioinvasive") )
        setattr(cls, "Papillary carcinoma, oxyphilic cell",
                PermissibleValue(text="Papillary carcinoma, oxyphilic cell") )
        setattr(cls, "Ameloblastic carcinoma",
                PermissibleValue(text="Ameloblastic carcinoma") )
        setattr(cls, "Duct carcinoma, desmoplastic type",
                PermissibleValue(text="Duct carcinoma, desmoplastic type") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with t(9;22)(q34;q11.2); BCR-ABL1",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with t(9;22)(q34;q11.2); BCR-ABL1") )
        setattr(cls, "Enterochromaffin-like cell carcinoid, NOS",
                PermissibleValue(text="Enterochromaffin-like cell carcinoid, NOS") )
        setattr(cls, "Hodgkin lymphoma, NOS",
                PermissibleValue(text="Hodgkin lymphoma, NOS") )
        setattr(cls, "Serous surface papillary carcinoma",
                PermissibleValue(text="Serous surface papillary carcinoma") )
        setattr(cls, "Villous adenoma, NOS",
                PermissibleValue(text="Villous adenoma, NOS") )
        setattr(cls, "Infiltrating duct and tubular carcinoma",
                PermissibleValue(text="Infiltrating duct and tubular carcinoma") )
        setattr(cls, "Granular cell carcinoma",
                PermissibleValue(text="Granular cell carcinoma") )
        setattr(cls, "Chronic granulocytic leukemia, NOS",
                PermissibleValue(text="Chronic granulocytic leukemia, NOS") )
        setattr(cls, "Mucinous cystic tumor with low grade dysplasia",
                PermissibleValue(text="Mucinous cystic tumor with low grade dysplasia") )
        setattr(cls, "Sinonasal papilloma, fungiform",
                PermissibleValue(text="Sinonasal papilloma, fungiform") )
        setattr(cls, "Acute myeloid leukemia with mutated NPM1",
                PermissibleValue(text="Acute myeloid leukemia with mutated NPM1") )
        setattr(cls, "Basaloid carcinoma",
                PermissibleValue(text="Basaloid carcinoma") )
        setattr(cls, "Langerhans cell granulomatosis, unifocal",
                PermissibleValue(text="Langerhans cell granulomatosis, unifocal") )
        setattr(cls, "Mastocytoma, NOS",
                PermissibleValue(text="Mastocytoma, NOS") )
        setattr(cls, "Juvenile nevus",
                PermissibleValue(text="Juvenile nevus") )
        setattr(cls, "Adenomatoid tumor, NOS",
                PermissibleValue(text="Adenomatoid tumor, NOS") )
        setattr(cls, "Idiopathic hemorrhagic thrombocythaemia",
                PermissibleValue(text="Idiopathic hemorrhagic thrombocythaemia") )
        setattr(cls, "Intraductal papillary-mucinous carcinoma, non-invasive",
                PermissibleValue(text="Intraductal papillary-mucinous carcinoma, non-invasive") )
        setattr(cls, "Trabecular adenocarcinoma",
                PermissibleValue(text="Trabecular adenocarcinoma") )
        setattr(cls, "Cloacogenic carcinoma",
                PermissibleValue(text="Cloacogenic carcinoma") )
        setattr(cls, "Cutaneous T-cell lymphoma, NOS",
                PermissibleValue(text="Cutaneous T-cell lymphoma, NOS") )
        setattr(cls, "Astrocytic glioma",
                PermissibleValue(text="Astrocytic glioma") )
        setattr(cls, "Precursor B-cell lymphoblastic leukemia",
                PermissibleValue(text="Precursor B-cell lymphoblastic leukemia") )
        setattr(cls, "MPNST with glandular differentiation",
                PermissibleValue(text="MPNST with glandular differentiation") )
        setattr(cls, "Sessile serrated polyp",
                PermissibleValue(text="Sessile serrated polyp") )
        setattr(cls, "Splenic marginal zone lymphoma, NOS",
                PermissibleValue(text="Splenic marginal zone lymphoma, NOS") )
        setattr(cls, "Teratoma, NOS",
                PermissibleValue(text="Teratoma, NOS") )
        setattr(cls, "Malignant mastocytosis",
                PermissibleValue(text="Malignant mastocytosis") )
        setattr(cls, "Periosteal chondroma",
                PermissibleValue(text="Periosteal chondroma") )
        setattr(cls, "Hurthle cell adenocarcinoma",
                PermissibleValue(text="Hurthle cell adenocarcinoma") )
        setattr(cls, "Embryonal rhabdomyosarcoma, pleomorphic",
                PermissibleValue(text="Embryonal rhabdomyosarcoma, pleomorphic") )
        setattr(cls, "Angiolipoma, NOS",
                PermissibleValue(text="Angiolipoma, NOS") )
        setattr(cls, "Epithelioid hemangioendothelioma, malignant",
                PermissibleValue(text="Epithelioid hemangioendothelioma, malignant") )
        setattr(cls, "Microcystic meningioma",
                PermissibleValue(text="Microcystic meningioma") )
        setattr(cls, "Polar spongioblastoma",
                PermissibleValue(text="Polar spongioblastoma") )
        setattr(cls, "Thymoma, spindle cell, malignant",
                PermissibleValue(text="Thymoma, spindle cell, malignant") )
        setattr(cls, "Acral lentiginous melanoma, malignant",
                PermissibleValue(text="Acral lentiginous melanoma, malignant") )
        setattr(cls, "Granulosa cell tumor, malignant",
                PermissibleValue(text="Granulosa cell tumor, malignant") )
        setattr(cls, "Chorioadenoma destruens",
                PermissibleValue(text="Chorioadenoma destruens") )
        setattr(cls, "Urticaria pigmentosa",
                PermissibleValue(text="Urticaria pigmentosa") )
        setattr(cls, "Mixed pancreatic endocrine and exocrine tumor, malignant",
                PermissibleValue(text="Mixed pancreatic endocrine and exocrine tumor, malignant") )
        setattr(cls, "Pro-B ALL",
                PermissibleValue(text="Pro-B ALL") )
        setattr(cls, "Follicular lymphoma, grade 3A",
                PermissibleValue(text="Follicular lymphoma, grade 3A") )
        setattr(cls, "Chronic myelomonocytic leukemia, NOS",
                PermissibleValue(text="Chronic myelomonocytic leukemia, NOS") )
        setattr(cls, "Myeloproliferative neoplasm, NOS",
                PermissibleValue(text="Myeloproliferative neoplasm, NOS") )
        setattr(cls, "Enterochromaffin cell carcinoid",
                PermissibleValue(text="Enterochromaffin cell carcinoid") )
        setattr(cls, "Malignant teratoma, intermediate",
                PermissibleValue(text="Malignant teratoma, intermediate") )
        setattr(cls, "Scirrhous adenocarcinoma",
                PermissibleValue(text="Scirrhous adenocarcinoma") )
        setattr(cls, "Tumorlet, benign",
                PermissibleValue(text="Tumorlet, benign") )
        setattr(cls, "Hodgkin disease, lymphocyte predominance, NOS",
                PermissibleValue(text="Hodgkin disease, lymphocyte predominance, NOS") )
        setattr(cls, "Small cell carcinoma pulmonary type",
                PermissibleValue(text="Small cell carcinoma pulmonary type") )
        setattr(cls, "Ependymoma, anaplastic",
                PermissibleValue(text="Ependymoma, anaplastic") )
        setattr(cls, "Periductal stromal tumor, low grade",
                PermissibleValue(text="Periductal stromal tumor, low grade") )
        setattr(cls, "Spindle cell lipoma",
                PermissibleValue(text="Spindle cell lipoma") )
        setattr(cls, "Cyst-associated renal cell carcinoma",
                PermissibleValue(text="Cyst-associated renal cell carcinoma") )
        setattr(cls, "Myxoma, NOS",
                PermissibleValue(text="Myxoma, NOS") )
        setattr(cls, "Gelatinous adenocarcinoma",
                PermissibleValue(text="Gelatinous adenocarcinoma") )
        setattr(cls, "Cystadenofibroma, NOS",
                PermissibleValue(text="Cystadenofibroma, NOS") )
        setattr(cls, "Squamous cell carcinoma, nonkeratinizing, NOS",
                PermissibleValue(text="Squamous cell carcinoma, nonkeratinizing, NOS") )
        setattr(cls, "Meningioma, malignant",
                PermissibleValue(text="Meningioma, malignant") )
        setattr(cls, "Mu heavy chain disease",
                PermissibleValue(text="Mu heavy chain disease") )
        setattr(cls, "Myelocytic leukemia, NOS",
                PermissibleValue(text="Myelocytic leukemia, NOS") )
        setattr(cls, "Cylindroma, NOS",
                PermissibleValue(text="Cylindroma, NOS") )
        setattr(cls, "Intracystic papillary neoplasm with low grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary neoplasm with low grade intraepithelial neoplasia") )
        setattr(cls, "Villous papilloma",
                PermissibleValue(text="Villous papilloma") )
        setattr(cls, "Solitary fibrous tumor, malignant",
                PermissibleValue(text="Solitary fibrous tumor, malignant") )
        setattr(cls, "Teratoid medulloepithelioma",
                PermissibleValue(text="Teratoid medulloepithelioma") )
        setattr(cls, "Granular cell tumor, NOS",
                PermissibleValue(text="Granular cell tumor, NOS") )
        setattr(cls, "Intraductal papillary adenocarcinoma with invasion",
                PermissibleValue(text="Intraductal papillary adenocarcinoma with invasion") )
        setattr(cls, "Angioimmunoblastic lymphadenopathy",
                PermissibleValue(text="Angioimmunoblastic lymphadenopathy") )
        setattr(cls, "Lymphatic leukemic, NOS",
                PermissibleValue(text="Lymphatic leukemic, NOS") )
        setattr(cls, "Bile duct carcinoma",
                PermissibleValue(text="Bile duct carcinoma") )
        setattr(cls, "Sertoli cell tumor with lipid storage",
                PermissibleValue(text="Sertoli cell tumor with lipid storage") )
        setattr(cls, "Mixed phenotype acute leukemia with t(9;22)(q34;q11.2); BCR-ABL1",
                PermissibleValue(text="Mixed phenotype acute leukemia with t(9;22)(q34;q11.2); BCR-ABL1") )
        setattr(cls, "Intraductal micropapillary carcinoma",
                PermissibleValue(text="Intraductal micropapillary carcinoma") )
        setattr(cls, "Tibial adamantinoma",
                PermissibleValue(text="Tibial adamantinoma") )
        setattr(cls, "PIN III",
                PermissibleValue(text="PIN III") )
        setattr(cls, "Synovial sarcoma, spindle cell",
                PermissibleValue(text="Synovial sarcoma, spindle cell") )
        setattr(cls, "Thymoma, predominantly cortical, malignant",
                PermissibleValue(text="Thymoma, predominantly cortical, malignant") )
        setattr(cls, "Sex cord-gonadal stromal tumor, incompletely differentiated",
                PermissibleValue(text="Sex cord-gonadal stromal tumor, incompletely differentiated") )
        setattr(cls, "Melanoma in situ",
                PermissibleValue(text="Melanoma in situ") )
        setattr(cls, "Spindle cell oncocytoma",
                PermissibleValue(text="Spindle cell oncocytoma") )
        setattr(cls, "Chromophobe adenoma",
                PermissibleValue(text="Chromophobe adenoma") )
        setattr(cls, "Infiltrating lipoma",
                PermissibleValue(text="Infiltrating lipoma") )
        setattr(cls, "Low-grade myofibroblastic sarcoma",
                PermissibleValue(text="Low-grade myofibroblastic sarcoma") )
        setattr(cls, "Calcifying epithelial odontogenic tumor",
                PermissibleValue(text="Calcifying epithelial odontogenic tumor") )
        setattr(cls, "Invasive lobular carcinoma, solid type",
                PermissibleValue(text="Invasive lobular carcinoma, solid type") )
        setattr(cls, "Subacute myelogenous leukemia",
                PermissibleValue(text="Subacute myelogenous leukemia") )
        setattr(cls, "Atypical choroid plexus papilloma",
                PermissibleValue(text="Atypical choroid plexus papilloma") )
        setattr(cls, "Clear cell sarcoma of kidney",
                PermissibleValue(text="Clear cell sarcoma of kidney") )
        setattr(cls, "Pheochromocytoma, NOS",
                PermissibleValue(text="Pheochromocytoma, NOS") )
        setattr(cls, "Tenosynovial giant cell tumor",
                PermissibleValue(text="Tenosynovial giant cell tumor") )
        setattr(cls, "Squamous cell epithelioma",
                PermissibleValue(text="Squamous cell epithelioma") )
        setattr(cls, "Ameloblastic fibrosarcoma",
                PermissibleValue(text="Ameloblastic fibrosarcoma") )
        setattr(cls, "Embryonal teratoma",
                PermissibleValue(text="Embryonal teratoma") )
        setattr(cls, "Papilloma of bladder",
                PermissibleValue(text="Papilloma of bladder") )
        setattr(cls, "Round cell carcinoma",
                PermissibleValue(text="Round cell carcinoma") )
        setattr(cls, "Sex cord tumor with annular tubules",
                PermissibleValue(text="Sex cord tumor with annular tubules") )
        setattr(cls, "Neuroectodermal tumor, NOS",
                PermissibleValue(text="Neuroectodermal tumor, NOS") )
        setattr(cls, "Urothelial carcinoma with squamous differentiation",
                PermissibleValue(text="Urothelial carcinoma with squamous differentiation") )
        setattr(cls, "Juvenile hemangioma",
                PermissibleValue(text="Juvenile hemangioma") )
        setattr(cls, "Pleomorphic lobular carcinoma in situ",
                PermissibleValue(text="Pleomorphic lobular carcinoma in situ") )
        setattr(cls, "Aleukemic lymphatic leukemia",
                PermissibleValue(text="Aleukemic lymphatic leukemia") )
        setattr(cls, "Pacinian tumor",
                PermissibleValue(text="Pacinian tumor") )
        setattr(cls, "Hurthle cell tumor",
                PermissibleValue(text="Hurthle cell tumor") )
        setattr(cls, "Brown fat tumor",
                PermissibleValue(text="Brown fat tumor") )
        setattr(cls, "Syringomatous carcinoma",
                PermissibleValue(text="Syringomatous carcinoma") )
        setattr(cls, "Rhabdomyosarcoma, NOS",
                PermissibleValue(text="Rhabdomyosarcoma, NOS") )
        setattr(cls, "Micropapillary serous carcinoma",
                PermissibleValue(text="Micropapillary serous carcinoma") )
        setattr(cls, "Malignant teratoma, undifferentiated",
                PermissibleValue(text="Malignant teratoma, undifferentiated") )
        setattr(cls, "Embryonal adenoma",
                PermissibleValue(text="Embryonal adenoma") )
        setattr(cls, "Pericanalicular fibroadenoma",
                PermissibleValue(text="Pericanalicular fibroadenoma") )
        setattr(cls, "Malignant melanoma in giant pigmented nevus",
                PermissibleValue(text="Malignant melanoma in giant pigmented nevus") )
        setattr(cls, "Condylomatous carcinoma",
                PermissibleValue(text="Condylomatous carcinoma") )
        setattr(cls, "Gastrointestinal stromal tumor, uncertain malignant potential",
                PermissibleValue(text="Gastrointestinal stromal tumor, uncertain malignant potential") )
        setattr(cls, "Endometrioid adenocarcinoma, NOS",
                PermissibleValue(text="Endometrioid adenocarcinoma, NOS") )
        setattr(cls, "Mixed mesenchymal tumor",
                PermissibleValue(text="Mixed mesenchymal tumor") )
        setattr(cls, "Malignant lymphoma, plasmacytoid",
                PermissibleValue(text="Malignant lymphoma, plasmacytoid") )
        setattr(cls, "Thymoma, type B2, NOS",
                PermissibleValue(text="Thymoma, type B2, NOS") )
        setattr(cls, "Intravascular B-cell lymphoma",
                PermissibleValue(text="Intravascular B-cell lymphoma") )
        setattr(cls, "Mixed basal-squamous cell carcinoma",
                PermissibleValue(text="Mixed basal-squamous cell carcinoma") )
        setattr(cls, "Primary cutaneous gamma-delta T-cell lymphoma",
                PermissibleValue(text="Primary cutaneous gamma-delta T-cell lymphoma") )
        setattr(cls, "Adenocarcinoma in a polyp, NOS",
                PermissibleValue(text="Adenocarcinoma in a polyp, NOS") )
        setattr(cls, "Beta cell tumor, malignant",
                PermissibleValue(text="Beta cell tumor, malignant") )
        setattr(cls, "Acute promyelocytic leukaemia, PML-RAR-alpha",
                PermissibleValue(text="Acute promyelocytic leukaemia, PML-RAR-alpha") )
        setattr(cls, "Preleukemic syndrome",
                PermissibleValue(text="Preleukemic syndrome") )
        setattr(cls, "Hemangioendothelioma, NOS",
                PermissibleValue(text="Hemangioendothelioma, NOS") )
        setattr(cls, "Villous adenocarcinoma",
                PermissibleValue(text="Villous adenocarcinoma") )
        setattr(cls, "Hereditary leiomyomatosis & RCC-associated renal cell carcinoma",
                PermissibleValue(text="Hereditary leiomyomatosis & RCC-associated renal cell carcinoma") )
        setattr(cls, "Hodgkin disease, nodular sclerosis, syncytial variant",
                PermissibleValue(text="Hodgkin disease, nodular sclerosis, syncytial variant") )
        setattr(cls, "Nonpigmented nevus",
                PermissibleValue(text="Nonpigmented nevus") )
        setattr(cls, "Medulloblastoma, NOS",
                PermissibleValue(text="Medulloblastoma, NOS") )
        setattr(cls, "Desmoplastic medulloblastoma",
                PermissibleValue(text="Desmoplastic medulloblastoma") )
        setattr(cls, "Small cell carcinoma, intermediate cell",
                PermissibleValue(text="Small cell carcinoma, intermediate cell") )
        setattr(cls, "Unclassified tumor, malignant, uncertain whether primary or metastatic",
                PermissibleValue(text="Unclassified tumor, malignant, uncertain whether primary or metastatic") )
        setattr(cls, "Primary cutaneous CD4-positive small/medium T-cell lymphoma",
                PermissibleValue(text="Primary cutaneous CD4-positive small/medium T-cell lymphoma") )
        setattr(cls, "Carcinoid tumor, argentaffin, NOS",
                PermissibleValue(text="Carcinoid tumor, argentaffin, NOS") )
        setattr(cls, "Rhabdoid tumor, NOS",
                PermissibleValue(text="Rhabdoid tumor, NOS") )
        setattr(cls, "Acinic cell adenocarcinoma",
                PermissibleValue(text="Acinic cell adenocarcinoma") )
        setattr(cls, "Cellular fibroma",
                PermissibleValue(text="Cellular fibroma") )
        setattr(cls, "Malignant rhabdoid tumor",
                PermissibleValue(text="Malignant rhabdoid tumor") )
        setattr(cls, "Intracystic papillary neoplasm with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intracystic papillary neoplasm with high grade intraepithelial neoplasia") )
        setattr(cls, "Synovial sarcoma, biphasic",
                PermissibleValue(text="Synovial sarcoma, biphasic") )
        setattr(cls, "Neuroendocrine carcinoma, well-differentiated",
                PermissibleValue(text="Neuroendocrine carcinoma, well-differentiated") )
        setattr(cls, "Fetal lipomatosis",
                PermissibleValue(text="Fetal lipomatosis") )
        setattr(cls, "Malignant peripheral nerve sheath tumor",
                PermissibleValue(text="Malignant peripheral nerve sheath tumor") )
        setattr(cls, "Adrenal medullary paraganglioma",
                PermissibleValue(text="Adrenal medullary paraganglioma") )
        setattr(cls, "Giant cell tumor of bone, malignant",
                PermissibleValue(text="Giant cell tumor of bone, malignant") )
        setattr(cls, "Oligodendroglioma, IDH-mutant and 1p/19q-codeleted",
                PermissibleValue(text="Oligodendroglioma, IDH-mutant and 1p/19q-codeleted") )
        setattr(cls, "Ductal carcinoma in situ, micropapillary",
                PermissibleValue(text="Ductal carcinoma in situ, micropapillary") )
        setattr(cls, "Mucinous cystadenocarcinofibroma",
                PermissibleValue(text="Mucinous cystadenocarcinofibroma") )
        setattr(cls, "Eccrine papillary adenocarcinoma",
                PermissibleValue(text="Eccrine papillary adenocarcinoma") )
        setattr(cls, "Adenocarcinoma in situ, mucinous",
                PermissibleValue(text="Adenocarcinoma in situ, mucinous",
                                 description="Mucinous Lung Adenocarcinoma In Situ") )
        setattr(cls, "Biliary intraepithelial neoplasia, low grade",
                PermissibleValue(text="Biliary intraepithelial neoplasia, low grade") )
        setattr(cls, "Non-invasive low grade serous carcinoma",
                PermissibleValue(text="Non-invasive low grade serous carcinoma") )
        setattr(cls, "Tubular carcinoid",
                PermissibleValue(text="Tubular carcinoid") )
        setattr(cls, "Malignant lymphoma, follicle center, follicular",
                PermissibleValue(text="Malignant lymphoma, follicle center, follicular") )
        setattr(cls, "Calcifying odontogenic cyst",
                PermissibleValue(text="Calcifying odontogenic cyst") )
        setattr(cls, "Proliferating trichilemmal tumor",
                PermissibleValue(text="Proliferating trichilemmal tumor") )
        setattr(cls, "Osteoblastoma, malignant",
                PermissibleValue(text="Osteoblastoma, malignant") )
        setattr(cls, "T lymphoblastic leukemia/lymphoma",
                PermissibleValue(text="T lymphoblastic leukemia/lymphoma") )
        setattr(cls, "Rodent ulcer",
                PermissibleValue(text="Rodent ulcer") )
        setattr(cls, "Periosteal chondrosarcoma",
                PermissibleValue(text="Periosteal chondrosarcoma") )
        setattr(cls, "Mixed squamous cell and glandular papilloma",
                PermissibleValue(text="Mixed squamous cell and glandular papilloma") )
        setattr(cls, "Acute mixed lineage leukemia",
                PermissibleValue(text="Acute mixed lineage leukemia") )
        setattr(cls, "Tumor cells, benign",
                PermissibleValue(text="Tumor cells, benign") )
        setattr(cls, "Thymoma, type A, malignant",
                PermissibleValue(text="Thymoma, type A, malignant") )
        setattr(cls, "T-cell rich large B-cell lymphoma",
                PermissibleValue(text="T-cell rich large B-cell lymphoma") )
        setattr(cls, "Tumorlet, NOS",
                PermissibleValue(text="Tumorlet, NOS") )
        setattr(cls, "Follicular fibroma",
                PermissibleValue(text="Follicular fibroma") )
        setattr(cls, "Papillary pseudomucinous cystadenoma, NOS",
                PermissibleValue(text="Papillary pseudomucinous cystadenoma, NOS") )
        setattr(cls, "Angiofibroma, NOS",
                PermissibleValue(text="Angiofibroma, NOS") )
        setattr(cls, "Gastrin cell tumor, malignant",
                PermissibleValue(text="Gastrin cell tumor, malignant") )
        setattr(cls, "Chronic myeloid leukemia, NOS",
                PermissibleValue(text="Chronic myeloid leukemia, NOS") )
        setattr(cls, "Atypical proliferative mucinous tumor",
                PermissibleValue(text="Atypical proliferative mucinous tumor") )
        setattr(cls, "Epithelioid mesothelioma, benign",
                PermissibleValue(text="Epithelioid mesothelioma, benign") )
        setattr(cls, "Sweat gland carcinoma",
                PermissibleValue(text="Sweat gland carcinoma") )
        setattr(cls, "Pulmonary artery intimal sarcoma",
                PermissibleValue(text="Pulmonary artery intimal sarcoma") )
        setattr(cls, "Immunoblastic sarcoma",
                PermissibleValue(text="Immunoblastic sarcoma") )
        setattr(cls, "Papillary hidradenoma",
                PermissibleValue(text="Papillary hidradenoma") )
        setattr(cls, "Wolffian duct carcinoma",
                PermissibleValue(text="Wolffian duct carcinoma") )
        setattr(cls, "Thymoma, benign",
                PermissibleValue(text="Thymoma, benign") )
        setattr(cls, "Lymphangioendothelioma, NOS",
                PermissibleValue(text="Lymphangioendothelioma, NOS") )
        setattr(cls, "Malignant teratoma, trophoblastic",
                PermissibleValue(text="Malignant teratoma, trophoblastic") )
        setattr(cls, "Metanephric adenoma",
                PermissibleValue(text="Metanephric adenoma") )
        setattr(cls, "Tubulolobular carcinoma",
                PermissibleValue(text="Tubulolobular carcinoma") )
        setattr(cls, "Spiradenoma, NOS",
                PermissibleValue(text="Spiradenoma, NOS") )
        setattr(cls, "Mycosis fungoides",
                PermissibleValue(text="Mycosis fungoides") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with t(12;21)(p13;q22); TEL-AML1 (ETV6-RUNX1)",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with t(12;21)(p13;q22); TEL-AML1 (ETV6-RUNX1)") )
        setattr(cls, "Villoglandular carcinoma",
                PermissibleValue(text="Villoglandular carcinoma") )
        setattr(cls, "Serous surface papilloma",
                PermissibleValue(text="Serous surface papilloma") )
        setattr(cls, "Neuroendocrine carcinoma, NOS",
                PermissibleValue(text="Neuroendocrine carcinoma, NOS") )
        setattr(cls, "Malignant melanoma in Hutchinson melanotic freckle",
                PermissibleValue(text="Malignant melanoma in Hutchinson melanotic freckle") )
        setattr(cls, "Pancreatic peptide and pancreatic peptide-like peptide within terminal tyrosine amide producing tumor",
                PermissibleValue(text="Pancreatic peptide and pancreatic peptide-like peptide within terminal tyrosine amide producing tumor") )
        setattr(cls, "Carcinoid, NOS, of appendix",
                PermissibleValue(text="Carcinoid, NOS, of appendix") )
        setattr(cls, "Follicular carcinoma, moderately differentiated",
                PermissibleValue(text="Follicular carcinoma, moderately differentiated") )
        setattr(cls, "GIST, malignant",
                PermissibleValue(text="GIST, malignant") )
        setattr(cls, "Metaplastic carcinoma with chondroid differentiation",
                PermissibleValue(text="Metaplastic carcinoma with chondroid differentiation") )
        setattr(cls, "T/NK-cell lymphoma",
                PermissibleValue(text="T/NK-cell lymphoma") )
        setattr(cls, "Hodgkin lymphoma, nodular sclerosis, grade 1",
                PermissibleValue(text="Hodgkin lymphoma, nodular sclerosis, grade 1") )
        setattr(cls, "Mucinous carcinoma, intestinal type",
                PermissibleValue(text="Mucinous carcinoma, intestinal type") )
        setattr(cls, "Hodgkin disease, lymphocyte predominance, diffuse",
                PermissibleValue(text="Hodgkin disease, lymphocyte predominance, diffuse") )
        setattr(cls, "Chondroblastic osteosarcoma",
                PermissibleValue(text="Chondroblastic osteosarcoma") )
        setattr(cls, "Chronic myelocytic leukemia, NOS",
                PermissibleValue(text="Chronic myelocytic leukemia, NOS") )
        setattr(cls, "Mucinous tubular and spindle cell carcinoma",
                PermissibleValue(text="Mucinous tubular and spindle cell carcinoma") )
        setattr(cls, "Malignant lymphoma, large cell, diffuse, NOS",
                PermissibleValue(text="Malignant lymphoma, large cell, diffuse, NOS") )
        setattr(cls, "AIN III",
                PermissibleValue(text="AIN III") )
        setattr(cls, "Chromophobe cell renal carcinoma",
                PermissibleValue(text="Chromophobe cell renal carcinoma") )
        setattr(cls, "Papillary cystadenoma lymphomatosum",
                PermissibleValue(text="Papillary cystadenoma lymphomatosum") )
        setattr(cls, "Juvenile angiofibroma",
                PermissibleValue(text="Juvenile angiofibroma") )
        setattr(cls, "Embryonal hepatoma",
                PermissibleValue(text="Embryonal hepatoma") )
        setattr(cls, "Malignant lymphoma, lymphoblastic, NOS",
                PermissibleValue(text="Malignant lymphoma, lymphoblastic, NOS") )
        setattr(cls, "Sertoli-Leydig cell tumor, NOS",
                PermissibleValue(text="Sertoli-Leydig cell tumor, NOS") )
        setattr(cls, "Thymoma, lymphocyte-rich, NOS",
                PermissibleValue(text="Thymoma, lymphocyte-rich, NOS") )
        setattr(cls, "Immunoglobulin deposition disease",
                PermissibleValue(text="Immunoglobulin deposition disease") )
        setattr(cls, "Chromophobe adenocarcinoma",
                PermissibleValue(text="Chromophobe adenocarcinoma") )
        setattr(cls, "Lennert lymphoma",
                PermissibleValue(text="Lennert lymphoma") )
        setattr(cls, "Serous adenocarcinoma, NOS",
                PermissibleValue(text="Serous adenocarcinoma, NOS") )
        setattr(cls, "Malignant melanoma in congenital melanocytic nevus",
                PermissibleValue(text="Malignant melanoma in congenital melanocytic nevus") )
        setattr(cls, "Sclerosing sweat duct carcinoma",
                PermissibleValue(text="Sclerosing sweat duct carcinoma") )
        setattr(cls, "Acute megakaryoblastic leukaemia",
                PermissibleValue(text="Acute megakaryoblastic leukaemia") )
        setattr(cls, "Benign fibrous histiocytoma",
                PermissibleValue(text="Benign fibrous histiocytoma") )
        setattr(cls, "Multifocal superficial basal cell carcinoma",
                PermissibleValue(text="Multifocal superficial basal cell carcinoma") )
        setattr(cls, "Hairy nevus",
                PermissibleValue(text="Hairy nevus") )
        setattr(cls, "Myoepithelial carcinoma",
                PermissibleValue(text="Myoepithelial carcinoma",
                                 description="Malignant Myoepithelioma") )
        setattr(cls, "Gastrointestinal stromal tumor, NOS",
                PermissibleValue(text="Gastrointestinal stromal tumor, NOS") )
        setattr(cls, "Desmoplastic melanoma, amelanotic",
                PermissibleValue(text="Desmoplastic melanoma, amelanotic") )
        setattr(cls, "Refractory anemia without sideroblasts",
                PermissibleValue(text="Refractory anemia without sideroblasts") )
        setattr(cls, "Malignant tumor, fusiform cell type",
                PermissibleValue(text="Malignant tumor, fusiform cell type") )
        setattr(cls, "Therapy-related myelodysplastic syndrome, NOS",
                PermissibleValue(text="Therapy-related myelodysplastic syndrome, NOS") )
        setattr(cls, "Adenocarcinoma in situ, non-mucinous",
                PermissibleValue(text="Adenocarcinoma in situ, non-mucinous") )
        setattr(cls, "Hemangiopericytoma, NOS",
                PermissibleValue(text="Hemangiopericytoma, NOS") )
        setattr(cls, "Undifferentiated sarcoma",
                PermissibleValue(text="Undifferentiated sarcoma") )
        setattr(cls, "Malignant hydatidiform mole",
                PermissibleValue(text="Malignant hydatidiform mole") )
        setattr(cls, "Bowen disease",
                PermissibleValue(text="Bowen disease") )
        setattr(cls, "Serous carcinoma, NOS",
                PermissibleValue(text="Serous carcinoma, NOS") )
        setattr(cls, "Therapy-related acute myeloid leukemia, NOS",
                PermissibleValue(text="Therapy-related acute myeloid leukemia, NOS") )
        setattr(cls, "Carcinoma showing thymus-like differentiation",
                PermissibleValue(text="Carcinoma showing thymus-like differentiation") )
        setattr(cls, "Fibroblastic osteosarcoma",
                PermissibleValue(text="Fibroblastic osteosarcoma") )
        setattr(cls, "Follicular carcinoma, minimally invasive",
                PermissibleValue(text="Follicular carcinoma, minimally invasive") )
        setattr(cls, "Rhabdoid meningioma",
                PermissibleValue(text="Rhabdoid meningioma") )
        setattr(cls, "Chronic monocytic leukemia",
                PermissibleValue(text="Chronic monocytic leukemia") )
        setattr(cls, "Oncocytic adenoma",
                PermissibleValue(text="Oncocytic adenoma") )
        setattr(cls, "Choriocarcinoma combined with embryonal carcinoma",
                PermissibleValue(text="Choriocarcinoma combined with embryonal carcinoma") )
        setattr(cls, "Melanotic schwannoma",
                PermissibleValue(text="Melanotic schwannoma") )
        setattr(cls, "Malignant perivascular epithelial cell tumor",
                PermissibleValue(text="Malignant perivascular epithelial cell tumor") )
        setattr(cls, "Theca cell tumor",
                PermissibleValue(text="Theca cell tumor") )
        setattr(cls, "Dermatofibrosarcoma protuberans, NOS",
                PermissibleValue(text="Dermatofibrosarcoma protuberans, NOS") )
        setattr(cls, "Intratubular germ cell neoplasia",
                PermissibleValue(text="Intratubular germ cell neoplasia") )
        setattr(cls, "Blast cell leukemia",
                PermissibleValue(text="Blast cell leukemia") )
        setattr(cls, "Monomorphic adenoma",
                PermissibleValue(text="Monomorphic adenoma") )
        setattr(cls, "Adenocarcinoma of rete ovarii",
                PermissibleValue(text="Adenocarcinoma of rete ovarii") )
        setattr(cls, "Hodgkin disease, lymphocytic-histiocytic predominance",
                PermissibleValue(text="Hodgkin disease, lymphocytic-histiocytic predominance") )
        setattr(cls, "Ossifying renal tumor",
                PermissibleValue(text="Ossifying renal tumor") )
        setattr(cls, "Fibrous mesothelioma, benign",
                PermissibleValue(text="Fibrous mesothelioma, benign") )
        setattr(cls, "Large cell neuroendocrine carcinoma",
                PermissibleValue(text="Large cell neuroendocrine carcinoma") )
        setattr(cls, "Mixed small cell carcinoma",
                PermissibleValue(text="Mixed small cell carcinoma") )
        setattr(cls, "Meningeal melanomatosis",
                PermissibleValue(text="Meningeal melanomatosis") )
        setattr(cls, "Adenocarcinoma, metastatic, NOS",
                PermissibleValue(text="Adenocarcinoma, metastatic, NOS") )
        setattr(cls, "Carcinoid tumor, NOS",
                PermissibleValue(text="Carcinoid tumor, NOS") )
        setattr(cls, "Oncocytic adenocarcinoma",
                PermissibleValue(text="Oncocytic adenocarcinoma") )
        setattr(cls, "Thymoma, type A, NOS",
                PermissibleValue(text="Thymoma, type A, NOS") )
        setattr(cls, "T-cell rich/histiocyte-rich large B-cell lymphoma",
                PermissibleValue(text="T-cell rich/histiocyte-rich large B-cell lymphoma") )
        setattr(cls, "Carcinoma with chondroid differentiation",
                PermissibleValue(text="Carcinoma with chondroid differentiation") )
        setattr(cls, "Adrenal medullary paraganglioma, malignant",
                PermissibleValue(text="Adrenal medullary paraganglioma, malignant") )
        setattr(cls, "Malignant lymphoma, noncleaved cell, follicular, NOS",
                PermissibleValue(text="Malignant lymphoma, noncleaved cell, follicular, NOS") )
        setattr(cls, "Adult T-cell lymphoma",
                PermissibleValue(text="Adult T-cell lymphoma") )
        setattr(cls, "Thymoma, epithelial, malignant",
                PermissibleValue(text="Thymoma, epithelial, malignant") )
        setattr(cls, "Epithelial-myoepithelial carcinoma",
                PermissibleValue(text="Epithelial-myoepithelial carcinoma",
                                 description="Epithelial-Myoepithelial Carcinoma") )
        setattr(cls, "Follicular dendritic cell sarcoma",
                PermissibleValue(text="Follicular dendritic cell sarcoma") )
        setattr(cls, "B cell lymphoma, NOS",
                PermissibleValue(text="B cell lymphoma, NOS") )
        setattr(cls, "Leiomyoma, NOS",
                PermissibleValue(text="Leiomyoma, NOS") )
        setattr(cls, "Retinoblastoma, differentiated",
                PermissibleValue(text="Retinoblastoma, differentiated") )
        setattr(cls, "Aleukemic lymphocytic leukemia",
                PermissibleValue(text="Aleukemic lymphocytic leukemia") )
        setattr(cls, "Solid carcinoma with mucin formation",
                PermissibleValue(text="Solid carcinoma with mucin formation") )
        setattr(cls, "Mucinous carcinoma, gastric type",
                PermissibleValue(text="Mucinous carcinoma, gastric type") )
        setattr(cls, "Serous tubal intraepithelial carcinoma",
                PermissibleValue(text="Serous tubal intraepithelial carcinoma") )
        setattr(cls, "Odontogenic sarcoma",
                PermissibleValue(text="Odontogenic sarcoma") )
        setattr(cls, "Thymoma, epithelial, NOS",
                PermissibleValue(text="Thymoma, epithelial, NOS") )
        setattr(cls, "Epidermoid carcinoma, spindle cell",
                PermissibleValue(text="Epidermoid carcinoma, spindle cell") )
        setattr(cls, "Bile duct cystadenoma",
                PermissibleValue(text="Bile duct cystadenoma") )
        setattr(cls, "Inflammatory carcinoma",
                PermissibleValue(text="Inflammatory carcinoma") )
        setattr(cls, "Hodgkin lymphoma, nodular lymphocyte predominance",
                PermissibleValue(text="Hodgkin lymphoma, nodular lymphocyte predominance") )
        setattr(cls, "Gastrointestinal stromal sarcoma",
                PermissibleValue(text="Gastrointestinal stromal sarcoma") )
        setattr(cls, "Endometrioid carcinoma, NOS",
                PermissibleValue(text="Endometrioid carcinoma, NOS",
                                 description="Endometrial Carcinoma") )
        setattr(cls, "Epithelial ependymoma",
                PermissibleValue(text="Epithelial ependymoma") )
        setattr(cls, "Spindle epithelial tumor with thymus-like element",
                PermissibleValue(text="Spindle epithelial tumor with thymus-like element") )
        setattr(cls, "Peripheral T-cell lymphoma, NOS",
                PermissibleValue(text="Peripheral T-cell lymphoma, NOS") )
        setattr(cls, "Non-Hodgkin lymphoma, NOS",
                PermissibleValue(text="Non-Hodgkin lymphoma, NOS") )
        setattr(cls, "Pilomatrixoma, NOS",
                PermissibleValue(text="Pilomatrixoma, NOS") )
        setattr(cls, "Schmincke tumor",
                PermissibleValue(text="Schmincke tumor") )
        setattr(cls, "Osteoid osteoma, NOS",
                PermissibleValue(text="Osteoid osteoma, NOS") )
        setattr(cls, "Gastrinoma, NOS",
                PermissibleValue(text="Gastrinoma, NOS") )
        setattr(cls, "Pseudomucinous adenocarcinoma",
                PermissibleValue(text="Pseudomucinous adenocarcinoma") )
        setattr(cls, "Unclassified tumor, benign",
                PermissibleValue(text="Unclassified tumor, benign") )
        setattr(cls, "Multiple hemorrhagic sarcoma",
                PermissibleValue(text="Multiple hemorrhagic sarcoma") )
        setattr(cls, "Pineal parenchymal tumor of intermediate differentiation",
                PermissibleValue(text="Pineal parenchymal tumor of intermediate differentiation") )
        setattr(cls, "Serous microcystic adenoma",
                PermissibleValue(text="Serous microcystic adenoma") )
        setattr(cls, "Clear cell odontogenic carcinoma",
                PermissibleValue(text="Clear cell odontogenic carcinoma") )
        setattr(cls, "Round cell sarcoma",
                PermissibleValue(text="Round cell sarcoma") )
        setattr(cls, "Cin III, NOS",
                PermissibleValue(text="Cin III, NOS") )
        setattr(cls, "Serous cystadenoma, NOS",
                PermissibleValue(text="Serous cystadenoma, NOS") )
        setattr(cls, "Acquired cystic disease-associated renal cell carcinoma (RCC)",
                PermissibleValue(text="Acquired cystic disease-associated renal cell carcinoma (RCC)") )
        setattr(cls, "Monstrocellular sarcoma",
                PermissibleValue(text="Monstrocellular sarcoma") )
        setattr(cls, "Malignant lymphoma, undifferentiated, Burkitt type",
                PermissibleValue(text="Malignant lymphoma, undifferentiated, Burkitt type") )
        setattr(cls, "Alveolar adenoma",
                PermissibleValue(text="Alveolar adenoma") )
        setattr(cls, "Chronic neutrophilic leukemia",
                PermissibleValue(text="Chronic neutrophilic leukemia") )
        setattr(cls, "Proliferating trichilemmal cyst",
                PermissibleValue(text="Proliferating trichilemmal cyst") )
        setattr(cls, "Differentiated-type vulvar intraepithelial neoplasia",
                PermissibleValue(text="Differentiated-type vulvar intraepithelial neoplasia") )
        setattr(cls, "Epithelial tumor, malignant",
                PermissibleValue(text="Epithelial tumor, malignant") )
        setattr(cls, "Bronchial-associated lymphoid tissue lymphoma",
                PermissibleValue(text="Bronchial-associated lymphoid tissue lymphoma") )
        setattr(cls, "Mixed islet cell and exocrine adenocarcinoma",
                PermissibleValue(text="Mixed islet cell and exocrine adenocarcinoma") )
        setattr(cls, "Follicular carcinoma, oxyphilic cell",
                PermissibleValue(text="Follicular carcinoma, oxyphilic cell") )
        setattr(cls, "Serous endometrial intraepithelial carcinoma",
                PermissibleValue(text="Serous endometrial intraepithelial carcinoma",
                                 description="Serous Endometrial Intraepithelial Carcinoma") )
        setattr(cls, "ECL cell carcinoid, NOS",
                PermissibleValue(text="ECL cell carcinoid, NOS") )
        setattr(cls, "Fibrous astrocytoma",
                PermissibleValue(text="Fibrous astrocytoma") )
        setattr(cls, "Renal cell adenocarcinoma",
                PermissibleValue(text="Renal cell adenocarcinoma") )
        setattr(cls, "Sex cord tumor, NOS",
                PermissibleValue(text="Sex cord tumor, NOS") )
        setattr(cls, "Mixed phenotype acute leukemia with t(v;11q23); MLL rearranged",
                PermissibleValue(text="Mixed phenotype acute leukemia with t(v;11q23); MLL rearranged") )
        setattr(cls, "Reticulum cell sarcoma, diffuse",
                PermissibleValue(text="Reticulum cell sarcoma, diffuse") )
        setattr(cls, "Alveolar soft part sarcoma",
                PermissibleValue(text="Alveolar soft part sarcoma") )
        setattr(cls, "Solitary fibrous tumor/hemangiopericytoma Grade 3 (CNS)",
                PermissibleValue(text="Solitary fibrous tumor/hemangiopericytoma Grade 3 (CNS)") )
        setattr(cls, "Spindle cell hemangioendothelioma",
                PermissibleValue(text="Spindle cell hemangioendothelioma") )
        setattr(cls, "Malignant cystic nephroma",
                PermissibleValue(text="Malignant cystic nephroma") )
        setattr(cls, "Trichilemmal carcinoma",
                PermissibleValue(text="Trichilemmal carcinoma") )
        setattr(cls, "Endometrioid cystadenofibroma, borderline malignancy",
                PermissibleValue(text="Endometrioid cystadenofibroma, borderline malignancy") )
        setattr(cls, "Acute non-lymphocytic leukemia",
                PermissibleValue(text="Acute non-lymphocytic leukemia") )
        setattr(cls, "Adult cystic teratoma",
                PermissibleValue(text="Adult cystic teratoma") )
        setattr(cls, "Hepatocellular carcinoma, spindle cell variant",
                PermissibleValue(text="Hepatocellular carcinoma, spindle cell variant") )
        setattr(cls, "Papillary serous cystadenoma, NOS",
                PermissibleValue(text="Papillary serous cystadenoma, NOS") )
        setattr(cls, "Giant pigmented nevus, NOS",
                PermissibleValue(text="Giant pigmented nevus, NOS") )
        setattr(cls, "Thymoma, type B3, NOS",
                PermissibleValue(text="Thymoma, type B3, NOS") )
        setattr(cls, "Verrucous keratotic hemangioma",
                PermissibleValue(text="Verrucous keratotic hemangioma") )
        setattr(cls, "Endometrial stromal sarcoma, NOS",
                PermissibleValue(text="Endometrial stromal sarcoma, NOS") )
        setattr(cls, "Carcinoma with other types mesenchymal differentiation",
                PermissibleValue(text="Carcinoma with other types mesenchymal differentiation") )
        setattr(cls, "CNS Embryonal tumor with rhabdoid features",
                PermissibleValue(text="CNS Embryonal tumor with rhabdoid features") )
        setattr(cls, "Germ cell tumor, nonseminomatous",
                PermissibleValue(text="Germ cell tumor, nonseminomatous") )
        setattr(cls, "Ancient schwannoma",
                PermissibleValue(text="Ancient schwannoma") )
        setattr(cls, "Myeloid leukemia, NOS",
                PermissibleValue(text="Myeloid leukemia, NOS") )
        setattr(cls, "Endometrioid adenofibroma, malignant",
                PermissibleValue(text="Endometrioid adenofibroma, malignant") )
        setattr(cls, "Astrocytoma, NOS",
                PermissibleValue(text="Astrocytoma, NOS") )
        setattr(cls, "Blue nevus, malignant",
                PermissibleValue(text="Blue nevus, malignant") )
        setattr(cls, "Transitional cell papilloma, inverted, benign",
                PermissibleValue(text="Transitional cell papilloma, inverted, benign") )
        setattr(cls, "Microcystic urothelial carcinoma",
                PermissibleValue(text="Microcystic urothelial carcinoma") )
        setattr(cls, "Hydatid mole",
                PermissibleValue(text="Hydatid mole") )
        setattr(cls, "Intraductal papillary-mucinous carcinoma, invasive",
                PermissibleValue(text="Intraductal papillary-mucinous carcinoma, invasive") )
        setattr(cls, "Esophageal squamous intraepithelial neoplasia (dysplasia), low grade",
                PermissibleValue(text="Esophageal squamous intraepithelial neoplasia (dysplasia), low grade") )
        setattr(cls, "Inflammatory liposarcoma",
                PermissibleValue(text="Inflammatory liposarcoma") )
        setattr(cls, "Carcinoid, NOS",
                PermissibleValue(text="Carcinoid, NOS") )
        setattr(cls, "Neuroma, NOS",
                PermissibleValue(text="Neuroma, NOS") )
        setattr(cls, "Intraductal carcinoma and lobular carcinoma in situ",
                PermissibleValue(text="Intraductal carcinoma and lobular carcinoma in situ") )
        setattr(cls, "Adenocarcinoma with apocrine metaplasia",
                PermissibleValue(text="Adenocarcinoma with apocrine metaplasia") )
        setattr(cls, "Sertoli-Leydig cell tumor, poorly differentiated, with heterologous elements",
                PermissibleValue(text="Sertoli-Leydig cell tumor, poorly differentiated, with heterologous elements") )
        setattr(cls, "Racemose hemangioma",
                PermissibleValue(text="Racemose hemangioma") )
        setattr(cls, "ALK positive large B-cell lymphoma",
                PermissibleValue(text="ALK positive large B-cell lymphoma") )
        setattr(cls, "FAB L2",
                PermissibleValue(text="FAB L2") )
        setattr(cls, "Micropapillary adenocarcinoma",
                PermissibleValue(text="Micropapillary adenocarcinoma") )
        setattr(cls, "Anaplastic pleomorphic xanthroastrocytoma",
                PermissibleValue(text="Anaplastic pleomorphic xanthroastrocytoma") )
        setattr(cls, "Myofibroblastic tumor, peribronchial",
                PermissibleValue(text="Myofibroblastic tumor, peribronchial") )
        setattr(cls, "Paraganglioma, NOS",
                PermissibleValue(text="Paraganglioma, NOS") )
        setattr(cls, "Mullerian adenosarcoma",
                PermissibleValue(text="Mullerian adenosarcoma") )
        setattr(cls, "Unclassified tumor, uncertain whether benign or malignant",
                PermissibleValue(text="Unclassified tumor, uncertain whether benign or malignant") )
        setattr(cls, "Signet ring cell carcinoma",
                PermissibleValue(text="Signet ring cell carcinoma") )
        setattr(cls, "Choriocarcinoma combined with teratorna",
                PermissibleValue(text="Choriocarcinoma combined with teratorna") )
        setattr(cls, "Therapy-related myelodysplastic syndrome, alkylating agent related",
                PermissibleValue(text="Therapy-related myelodysplastic syndrome, alkylating agent related") )
        setattr(cls, "Endometrioid adenoma, NOS",
                PermissibleValue(text="Endometrioid adenoma, NOS") )
        setattr(cls, "Interstitial cell tumor, malignant",
                PermissibleValue(text="Interstitial cell tumor, malignant") )
        setattr(cls, "Yolk sac tumor",
                PermissibleValue(text="Yolk sac tumor") )
        setattr(cls, "Epithelioid cell sarcoma",
                PermissibleValue(text="Epithelioid cell sarcoma") )
        setattr(cls, "Polypoid adenoma",
                PermissibleValue(text="Polypoid adenoma") )
        setattr(cls, "Sweat gland tumor, malignant",
                PermissibleValue(text="Sweat gland tumor, malignant") )
        setattr(cls, "Intratubular malignant germ cells",
                PermissibleValue(text="Intratubular malignant germ cells") )
        setattr(cls, "Neoplasm, metastatic",
                PermissibleValue(text="Neoplasm, metastatic") )
        setattr(cls, "Aleukemic monocytic leukemia",
                PermissibleValue(text="Aleukemic monocytic leukemia") )
        setattr(cls, "Neuroendocrine carcinoma, low grade",
                PermissibleValue(text="Neuroendocrine carcinoma, low grade") )
        setattr(cls, "Solid pseudopapillary tumor",
                PermissibleValue(text="Solid pseudopapillary tumor") )
        setattr(cls, "Serous adenocarcinofibroma",
                PermissibleValue(text="Serous adenocarcinofibroma") )
        setattr(cls, "Biliary intraepithelial neoplasia, high grade",
                PermissibleValue(text="Biliary intraepithelial neoplasia, high grade") )
        setattr(cls, "Malignant lymphoma, centroblasticcentrocytic, follicular",
                PermissibleValue(text="Malignant lymphoma, centroblasticcentrocytic, follicular") )
        setattr(cls, "Acute myloid leukemia, 11q23 abnormalities",
                PermissibleValue(text="Acute myloid leukemia, 11q23 abnormalities") )
        setattr(cls, "Langerhans cell histiocytosis, generalized",
                PermissibleValue(text="Langerhans cell histiocytosis, generalized") )
        setattr(cls, "B lymphoblastic leukemia/lymphoma with t(v;11q23); MLL rearranged",
                PermissibleValue(text="B lymphoblastic leukemia/lymphoma with t(v;11q23); MLL rearranged") )
        setattr(cls, "Malignant melanoma, NOS",
                PermissibleValue(text="Malignant melanoma, NOS") )
        setattr(cls, "Thymoma, NOS",
                PermissibleValue(text="Thymoma, NOS") )
        setattr(cls, "Malignant lymphoma, small lymphocytic, NOS",
                PermissibleValue(text="Malignant lymphoma, small lymphocytic, NOS") )
        setattr(cls, "Cutaneous histiocytoma, NOS",
                PermissibleValue(text="Cutaneous histiocytoma, NOS") )
        setattr(cls, "Aggressive NK-cell leukaemia",
                PermissibleValue(text="Aggressive NK-cell leukaemia") )
        setattr(cls, "Polymorphic post transplant lymphoproliferative disorder",
                PermissibleValue(text="Polymorphic post transplant lymphoproliferative disorder") )
        setattr(cls, "Chromophobe carcinoma",
                PermissibleValue(text="Chromophobe carcinoma") )
        setattr(cls, "Refractory anemia with excess blasts in transformation",
                PermissibleValue(text="Refractory anemia with excess blasts in transformation") )
        setattr(cls, "Desmoplastic fibroma",
                PermissibleValue(text="Desmoplastic fibroma") )
        setattr(cls, "Intestinal T-cell lymphoma",
                PermissibleValue(text="Intestinal T-cell lymphoma") )
        setattr(cls, "Histiocyte-rich large B-cell lymphoma",
                PermissibleValue(text="Histiocyte-rich large B-cell lymphoma") )
        setattr(cls, "Thymoma, malignant, NOS",
                PermissibleValue(text="Thymoma, malignant, NOS") )
        setattr(cls, "Matrical carcinoma",
                PermissibleValue(text="Matrical carcinoma") )
        setattr(cls, "Intravascular bronchial alveolar tumor",
                PermissibleValue(text="Intravascular bronchial alveolar tumor") )
        setattr(cls, "Cystic partially differentiated nephroblastoma",
                PermissibleValue(text="Cystic partially differentiated nephroblastoma") )
        setattr(cls, "Odontogenic fibroma, NOS",
                PermissibleValue(text="Odontogenic fibroma, NOS") )
        setattr(cls, "Pancreatic endocrine tumor, NOS",
                PermissibleValue(text="Pancreatic endocrine tumor, NOS") )
        setattr(cls, "Lactating adenoma",
                PermissibleValue(text="Lactating adenoma") )
        setattr(cls, "Minimally invasive adenocarcinoma, non-mucinous",
                PermissibleValue(text="Minimally invasive adenocarcinoma, non-mucinous") )
        setattr(cls, "Acquired tufted hemangioma",
                PermissibleValue(text="Acquired tufted hemangioma") )
        setattr(cls, "Malignant tenosynovial giant cell tumor",
                PermissibleValue(text="Malignant tenosynovial giant cell tumor") )
        setattr(cls, "Fibroblastic reticular cell tumor",
                PermissibleValue(text="Fibroblastic reticular cell tumor") )
        setattr(cls, "Schneiderian carcinoma",
                PermissibleValue(text="Schneiderian carcinoma") )
        setattr(cls, "Myofibroblastic tumor, NOS",
                PermissibleValue(text="Myofibroblastic tumor, NOS") )
        setattr(cls, "Large B-cell lymphoma arising in HHV8-associated multicentric Castleman disease",
                PermissibleValue(text="Large B-cell lymphoma arising in HHV8-associated multicentric Castleman disease") )
        setattr(cls, "Malignant fibrous histiocytoma (MFH) of bone",
                PermissibleValue(text="Malignant fibrous histiocytoma (MFH) of bone") )
        setattr(cls, "Malignant lymphomatous polyposis",
                PermissibleValue(text="Malignant lymphomatous polyposis") )
        setattr(cls, "Smooth muscle tumor of uncertain malignant potential",
                PermissibleValue(text="Smooth muscle tumor of uncertain malignant potential") )
        setattr(cls, "Odontogenic myxofibroma",
                PermissibleValue(text="Odontogenic myxofibroma") )
        setattr(cls, "Adenomatosis, NOS",
                PermissibleValue(text="Adenomatosis, NOS") )
        setattr(cls, "Myelodysplastic syndrome with isolated del (5q)",
                PermissibleValue(text="Myelodysplastic syndrome with isolated del (5q)") )
        setattr(cls, "Trabecular adenoma",
                PermissibleValue(text="Trabecular adenoma") )
        setattr(cls, "Squamous cell carcinoma, sarcomatoid",
                PermissibleValue(text="Squamous cell carcinoma, sarcomatoid") )
        setattr(cls, "Acute myeloblastic leukemia",
                PermissibleValue(text="Acute myeloblastic leukemia") )
        setattr(cls, "Classical Hodgkin lymphoma, mixed cellularity, NOS",
                PermissibleValue(text="Classical Hodgkin lymphoma, mixed cellularity, NOS") )
        setattr(cls, "Squamous intraepithelial neoplasia, grade III",
                PermissibleValue(text="Squamous intraepithelial neoplasia, grade III") )
        setattr(cls, "Perineurioma, NOS",
                PermissibleValue(text="Perineurioma, NOS") )
        setattr(cls, "Paget disease, mammary",
                PermissibleValue(text="Paget disease, mammary") )
        setattr(cls, "Refractory anemia with ringed sideroblasts",
                PermissibleValue(text="Refractory anemia with ringed sideroblasts") )
        setattr(cls, "Folliculome lipidique",
                PermissibleValue(text="Folliculome lipidique") )
        setattr(cls, "Intracystic papillary neoplasm with associated invasive carcinoma",
                PermissibleValue(text="Intracystic papillary neoplasm with associated invasive carcinoma") )
        setattr(cls, "Ameloblastic fibrodentinosarcoma",
                PermissibleValue(text="Ameloblastic fibrodentinosarcoma") )
        setattr(cls, "Hepatoma, benign",
                PermissibleValue(text="Hepatoma, benign") )
        setattr(cls, "Ameloblastic fibro-odontoma",
                PermissibleValue(text="Ameloblastic fibro-odontoma") )
        setattr(cls, "Intraductal papillary-mucinous neoplasm with low grade dysplasia",
                PermissibleValue(text="Intraductal papillary-mucinous neoplasm with low grade dysplasia") )
        setattr(cls, "Malignant lymphoma, large cell, cleaved, NOS",
                PermissibleValue(text="Malignant lymphoma, large cell, cleaved, NOS") )
        setattr(cls, "Epithelioid cell melanoma",
                PermissibleValue(text="Epithelioid cell melanoma") )
        setattr(cls, "Synovial sarcoma, NOS",
                PermissibleValue(text="Synovial sarcoma, NOS") )
        setattr(cls, "Intracystic carcinoma, NOS",
                PermissibleValue(text="Intracystic carcinoma, NOS") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "Ectopic hamartomatous thymoma",
                PermissibleValue(text="Ectopic hamartomatous thymoma") )
        setattr(cls, "Odontogenic carcinoma",
                PermissibleValue(text="Odontogenic carcinoma") )
        setattr(cls, "Malignant lymphoma, lymphoplasmacytoid",
                PermissibleValue(text="Malignant lymphoma, lymphoplasmacytoid") )
        setattr(cls, "Basal cell carcinoma, desmoplastic type",
                PermissibleValue(text="Basal cell carcinoma, desmoplastic type") )
        setattr(cls, "Mesonephroma, malignant",
                PermissibleValue(text="Mesonephroma, malignant") )
        setattr(cls, "Endocrine tumor, functioning, NOS",
                PermissibleValue(text="Endocrine tumor, functioning, NOS") )
        setattr(cls, "Intraductal papillary tumor with high grade intraepithelial neoplasia",
                PermissibleValue(text="Intraductal papillary tumor with high grade intraepithelial neoplasia") )
        setattr(cls, "Refractory cytopenia of childhood",
                PermissibleValue(text="Refractory cytopenia of childhood") )
        setattr(cls, "Venous hemangioma",
                PermissibleValue(text="Venous hemangioma") )
        setattr(cls, "Small cell carcinoma, NOS",
                PermissibleValue(text="Small cell carcinoma, NOS") )
        setattr(cls, "Lobular carcinoma in situ, NOS",
                PermissibleValue(text="Lobular carcinoma in situ, NOS") )
        setattr(cls, "Pleomorphic liposarcoma",
                PermissibleValue(text="Pleomorphic liposarcoma") )
        setattr(cls, "Malignant lymphoma, small cleaved cell, follicular",
                PermissibleValue(text="Malignant lymphoma, small cleaved cell, follicular") )
        setattr(cls, "DCIS, papillary",
                PermissibleValue(text="DCIS, papillary") )
        setattr(cls, "Choriocarcinoma combined with other germ cell elements",
                PermissibleValue(text="Choriocarcinoma combined with other germ cell elements") )
        setattr(cls, "Chronic myelomonocytic leukemia, Type II",
                PermissibleValue(text="Chronic myelomonocytic leukemia, Type II") )
        setattr(cls, "Malignant lymphoma, mixed lymphocytic-histiocytic, diffuse",
                PermissibleValue(text="Malignant lymphoma, mixed lymphocytic-histiocytic, diffuse") )
        setattr(cls, "Prostatic intraepithelial neoplasia, grade III",
                PermissibleValue(text="Prostatic intraepithelial neoplasia, grade III") )
        setattr(cls, "Endodermal sinus tumor",
                PermissibleValue(text="Endodermal sinus tumor") )
        setattr(cls, "PP/PYY producing tumor",
                PermissibleValue(text="PP/PYY producing tumor") )
        setattr(cls, "FAB M1",
                PermissibleValue(text="FAB M1") )
        setattr(cls, "Hypernephroid tumor",
                PermissibleValue(text="Hypernephroid tumor") )
        setattr(cls, "Arrhenoblastoma, NOS",
                PermissibleValue(text="Arrhenoblastoma, NOS") )
        setattr(cls, "Pseudomucinous cystadenoma, borderline malignancy",
                PermissibleValue(text="Pseudomucinous cystadenoma, borderline malignancy") )
        setattr(cls, "Adenoma of nipple",
                PermissibleValue(text="Adenoma of nipple") )
        setattr(cls, "Cystic tumor of atrio-ventricular node",
                PermissibleValue(text="Cystic tumor of atrio-ventricular node") )
        setattr(cls, "Osteosarcoma in Paget disease of bone",
                PermissibleValue(text="Osteosarcoma in Paget disease of bone") )
        setattr(cls, "Sertoli-Leydig cell tumor, poorly differentiated",
                PermissibleValue(text="Sertoli-Leydig cell tumor, poorly differentiated") )
        setattr(cls, "Intraductal papillary mucinous neoplasm (IPMN) with an associated invasive carcinoma",
                PermissibleValue(text="Intraductal papillary mucinous neoplasm (IPMN) with an associated invasive carcinoma") )
        setattr(cls, "Sertoli-Leydig cell tumor, retiform, with heterologous elements",
                PermissibleValue(text="Sertoli-Leydig cell tumor, retiform, with heterologous elements") )
        setattr(cls, "Retinoblastoma, undifferentiated",
                PermissibleValue(text="Retinoblastoma, undifferentiated") )
        setattr(cls, "Chronic myelogenous leukemia, BCR-ABL positive",
                PermissibleValue(text="Chronic myelogenous leukemia, BCR-ABL positive") )
        setattr(cls, "Androblastoma, NOS",
                PermissibleValue(text="Androblastoma, NOS") )
        setattr(cls, "Small congenital nevus",
                PermissibleValue(text="Small congenital nevus") )
        setattr(cls, "Teratoblastoma, malignant",
                PermissibleValue(text="Teratoblastoma, malignant") )
        setattr(cls, "Desmoplastic nodular medulloblastoma",
                PermissibleValue(text="Desmoplastic nodular medulloblastoma") )
        setattr(cls, "FAB M4Eo",
                PermissibleValue(text="FAB M4Eo") )
        setattr(cls, "Essential hemorrhagic thrombocythaemia",
                PermissibleValue(text="Essential hemorrhagic thrombocythaemia") )
        setattr(cls, "Apocrine adenoma",
                PermissibleValue(text="Apocrine adenoma") )
        setattr(cls, "Chronic granulocytic leukemia, t(9;22)(q34;q11)",
                PermissibleValue(text="Chronic granulocytic leukemia, t(9;22)(q34;q11)") )
        setattr(cls, "Phyllodes tumor, NOS",
                PermissibleValue(text="Phyllodes tumor, NOS") )
        setattr(cls, "Nonchromaffin paraganglioma, malignant",
                PermissibleValue(text="Nonchromaffin paraganglioma, malignant") )
        setattr(cls, "Mixed meningioma",
                PermissibleValue(text="Mixed meningioma") )
        setattr(cls, "Chondroid lipoma",
                PermissibleValue(text="Chondroid lipoma") )
        setattr(cls, "Cervical intraepithelial neoplasia, low grade",
                PermissibleValue(text="Cervical intraepithelial neoplasia, low grade") )
        setattr(cls, "Diffuse cutaneous mastocytosis",
                PermissibleValue(text="Diffuse cutaneous mastocytosis") )
        setattr(cls, "Superficial spreading melanoma",
                PermissibleValue(text="Superficial spreading melanoma",
                                 description="Superficial Spreading Melanoma") )
        setattr(cls, "Gemistocytic astrocytoma",
                PermissibleValue(text="Gemistocytic astrocytoma") )
        setattr(cls, "Meningothelial meningioma",
                PermissibleValue(text="Meningothelial meningioma") )
        setattr(cls, "Papillary and follicular adenocarcinoma",
                PermissibleValue(text="Papillary and follicular adenocarcinoma") )
        setattr(cls, "Malignant lymphoma, noncleaved, NOS",
                PermissibleValue(text="Malignant lymphoma, noncleaved, NOS") )
        setattr(cls, "Chondrosarcoma grade 2/3",
                PermissibleValue(text="Chondrosarcoma grade 2/3") )
        setattr(cls, "Tumor, metastatic",
                PermissibleValue(text="Tumor, metastatic") )
        setattr(cls, "Infiltrating duct and lobular carcinoma in situ",
                PermissibleValue(text="Infiltrating duct and lobular carcinoma in situ") )
        setattr(cls, "Symplastic leiomyoma",
                PermissibleValue(text="Symplastic leiomyoma") )
        setattr(cls, "Mast cell tumor, NOS",
                PermissibleValue(text="Mast cell tumor, NOS") )
        setattr(cls, "Anaplastic oligodendroglioma, IDH-mutant and 1p/19q-codeleted",
                PermissibleValue(text="Anaplastic oligodendroglioma, IDH-mutant and 1p/19q-codeleted") )
        setattr(cls, "Rathke pouch tumor",
                PermissibleValue(text="Rathke pouch tumor") )
        setattr(cls, "Enteropathy associated T-cell lymphoma",
                PermissibleValue(text="Enteropathy associated T-cell lymphoma") )
        setattr(cls, "Eosinophilic leukemia",
                PermissibleValue(text="Eosinophilic leukemia") )
        setattr(cls, "Embryonal adenocarcinoma",
                PermissibleValue(text="Embryonal adenocarcinoma") )
        setattr(cls, "Dermal and epidermal nevus",
                PermissibleValue(text="Dermal and epidermal nevus") )
        setattr(cls, "Small cell osteosarcoma",
                PermissibleValue(text="Small cell osteosarcoma") )
        setattr(cls, "Acute granulocytic leukemia",
                PermissibleValue(text="Acute granulocytic leukemia") )
        setattr(cls, "FAB M2, t(8;21)(q22;q22)",
                PermissibleValue(text="FAB M2, t(8;21)(q22;q22)") )
        setattr(cls, "Soft tissue tumor, benign",
                PermissibleValue(text="Soft tissue tumor, benign") )
        setattr(cls, "Burkitt-like lymphoma",
                PermissibleValue(text="Burkitt-like lymphoma") )
        setattr(cls, "Esophageal glandular dysplasia (intraepithelial neoplasia), high grade",
                PermissibleValue(text="Esophageal glandular dysplasia (intraepithelial neoplasia), high grade") )
        setattr(cls, "Solitary fibrous tumor",
                PermissibleValue(text="Solitary fibrous tumor") )
        setattr(cls, "Transitional meningioma",
                PermissibleValue(text="Transitional meningioma") )
        setattr(cls, "Peripheral primitive neuroectodermal tumor, NOS",
                PermissibleValue(text="Peripheral primitive neuroectodermal tumor, NOS") )
        setattr(cls, "Clear cell chondrosarcoma",
                PermissibleValue(text="Clear cell chondrosarcoma") )
        setattr(cls, "Atypical meningioma",
                PermissibleValue(text="Atypical meningioma") )
        setattr(cls, "FAB M2, AML1(CBF-alpha)/ETO",
                PermissibleValue(text="FAB M2, AML1(CBF-alpha)/ETO") )
        setattr(cls, "Epithelioid leiomyosarcoma",
                PermissibleValue(text="Epithelioid leiomyosarcoma") )
        setattr(cls, "Monoblastic leukemia, NOS",
                PermissibleValue(text="Monoblastic leukemia, NOS") )
        setattr(cls, "Juvenile myelomonocytic leukemia",
                PermissibleValue(text="Juvenile myelomonocytic leukemia") )
        setattr(cls, "Eccrine papillary adenoma",
                PermissibleValue(text="Eccrine papillary adenoma") )
        setattr(cls, "Infiltrating lobular carcinoma, NOS",
                PermissibleValue(text="Infiltrating lobular carcinoma, NOS") )
        setattr(cls, "Tubular androblastoma with lipid storage",
                PermissibleValue(text="Tubular androblastoma with lipid storage") )
        setattr(cls, "Squamous cell carcinoma, large cell, keratinizing",
                PermissibleValue(text="Squamous cell carcinoma, large cell, keratinizing") )
        setattr(cls, "Acute lymphoblastic leukemia, mature B-cell type",
                PermissibleValue(text="Acute lymphoblastic leukemia, mature B-cell type") )
        setattr(cls, "Jugular paraganglioma",
                PermissibleValue(text="Jugular paraganglioma") )
        setattr(cls, "Myelofibrosis with myeloid metaplasia",
                PermissibleValue(text="Myelofibrosis with myeloid metaplasia") )
        setattr(cls, "Anal intraepithelial neoplasia, low grade",
                PermissibleValue(text="Anal intraepithelial neoplasia, low grade") )
        setattr(cls, "Islet cell adenoma",
                PermissibleValue(text="Islet cell adenoma") )
        setattr(cls, "Adenocarcinoma in situ in tubular adenoma",
                PermissibleValue(text="Adenocarcinoma in situ in tubular adenoma") )
        setattr(cls, "Argentaffinoma, malignant",
                PermissibleValue(text="Argentaffinoma, malignant") )
        setattr(cls, "Rhabdoid sarcoma",
                PermissibleValue(text="Rhabdoid sarcoma") )
        setattr(cls, "Malignant lymphoma, large cleaved cell, NOS",
                PermissibleValue(text="Malignant lymphoma, large cleaved cell, NOS") )
        setattr(cls, "Granulosa cell tumor, juvenile",
                PermissibleValue(text="Granulosa cell tumor, juvenile") )
        setattr(cls, "Stromal tumor, NOS",
                PermissibleValue(text="Stromal tumor, NOS") )
        setattr(cls, "Medullary adenocarcinoma",
                PermissibleValue(text="Medullary adenocarcinoma") )
        setattr(cls, "Malignant lymphoma, histiocytic, diffuse",
                PermissibleValue(text="Malignant lymphoma, histiocytic, diffuse") )
        setattr(cls, "Lymphocytic leukemia, NOS",
                PermissibleValue(text="Lymphocytic leukemia, NOS") )
        setattr(cls, "Teratoma, malignant, NOS",
                PermissibleValue(text="Teratoma, malignant, NOS") )
        setattr(cls, "G cell tumor, malignant",
                PermissibleValue(text="G cell tumor, malignant") )
        setattr(cls, "Bellini duct carcinoma",
                PermissibleValue(text="Bellini duct carcinoma") )
        setattr(cls, "Non-small cell carcinoma",
                PermissibleValue(text="Non-small cell carcinoma") )
        setattr(cls, "Tubular adenocarcinoma",
                PermissibleValue(text="Tubular adenocarcinoma") )
        setattr(cls, "Mixed adenoneuroendocrine carcinoma",
                PermissibleValue(text="Mixed adenoneuroendocrine carcinoma",
                                 description="Digestive System Mixed Adenoneuroendocrine Carcinoma") )
        setattr(cls, "Tumor cells, NOS",
                PermissibleValue(text="Tumor cells, NOS") )
        setattr(cls, "Pancreatic endocrine tumor, malignant",
                PermissibleValue(text="Pancreatic endocrine tumor, malignant") )
        setattr(cls, "Malignant lymphoma, lymphocytic, NOS",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, NOS") )
        setattr(cls, "Fibroepithelial basal cell carcinoma, Pinkus type",
                PermissibleValue(text="Fibroepithelial basal cell carcinoma, Pinkus type") )
        setattr(cls, "Giant cell and spindle cell carcinoma",
                PermissibleValue(text="Giant cell and spindle cell carcinoma") )
        setattr(cls, "Phyllodes tumor, benign",
                PermissibleValue(text="Phyllodes tumor, benign") )
        setattr(cls, "Cylindroma of skin",
                PermissibleValue(text="Cylindroma of skin") )
        setattr(cls, "Angiomatoid fibrous histiocytoma",
                PermissibleValue(text="Angiomatoid fibrous histiocytoma") )
        setattr(cls, "Chordoid meningioma",
                PermissibleValue(text="Chordoid meningioma") )
        setattr(cls, "Dysembryoplastic neuroepithelial tumor",
                PermissibleValue(text="Dysembryoplastic neuroepithelial tumor") )
        setattr(cls, "Chondroma, NOS",
                PermissibleValue(text="Chondroma, NOS") )
        setattr(cls, "Malignant lymphoma, mixed cell type, diffuse",
                PermissibleValue(text="Malignant lymphoma, mixed cell type, diffuse") )
        setattr(cls, "Plasma cell myeloma",
                PermissibleValue(text="Plasma cell myeloma") )
        setattr(cls, "Gastrointestinal stromal tumor, benign",
                PermissibleValue(text="Gastrointestinal stromal tumor, benign") )
        setattr(cls, "Embryonal tumor with multilayered rosettes C19MC-altered",
                PermissibleValue(text="Embryonal tumor with multilayered rosettes C19MC-altered") )
        setattr(cls, "Atypical teratoid/rhabdoid tumor",
                PermissibleValue(text="Atypical teratoid/rhabdoid tumor") )
        setattr(cls, "Malignant lymphoma, immunoblastic, NOS",
                PermissibleValue(text="Malignant lymphoma, immunoblastic, NOS") )
        setattr(cls, "Epidermoid carcinoma in situ, NOS",
                PermissibleValue(text="Epidermoid carcinoma in situ, NOS") )
        setattr(cls, "Urothelial carcinoma, NOS",
                PermissibleValue(text="Urothelial carcinoma, NOS") )
        setattr(cls, "Steroid cell tumor, malignant",
                PermissibleValue(text="Steroid cell tumor, malignant") )
        setattr(cls, "Langerhans cell histiocytosis, unifocal",
                PermissibleValue(text="Langerhans cell histiocytosis, unifocal") )
        setattr(cls, "Testicular stromal tumor",
                PermissibleValue(text="Testicular stromal tumor") )
        setattr(cls, "Solid teratoma",
                PermissibleValue(text="Solid teratoma") )
        setattr(cls, "Hemangiopericytoma, benign",
                PermissibleValue(text="Hemangiopericytoma, benign") )
        setattr(cls, "Malignant teratoma, anaplastic",
                PermissibleValue(text="Malignant teratoma, anaplastic") )
        setattr(cls, "Papillary squamous cell carcinoma",
                PermissibleValue(text="Papillary squamous cell carcinoma") )
        setattr(cls, "Carcinosarcoma, NOS",
                PermissibleValue(text="Carcinosarcoma, NOS") )
        setattr(cls, "Acute myeloid leukemia with myelodysplasia-related changes",
                PermissibleValue(text="Acute myeloid leukemia with myelodysplasia-related changes") )
        setattr(cls, "Hurthle cell carcinoma",
                PermissibleValue(text="Hurthle cell carcinoma") )
        setattr(cls, "Ameloblastic fibrodentinoma",
                PermissibleValue(text="Ameloblastic fibrodentinoma") )
        setattr(cls, "Chronic erythremia",
                PermissibleValue(text="Chronic erythremia") )
        setattr(cls, "Eosinophil adenoma",
                PermissibleValue(text="Eosinophil adenoma") )
        setattr(cls, "Malignant lymphoma, centroblastic, follicular",
                PermissibleValue(text="Malignant lymphoma, centroblastic, follicular") )
        setattr(cls, "Systemic tissue mast cell disease",
                PermissibleValue(text="Systemic tissue mast cell disease") )
        setattr(cls, "Combined small cell-large carcinoma",
                PermissibleValue(text="Combined small cell-large carcinoma") )
        setattr(cls, "Cutaneous lymphoma, NOS",
                PermissibleValue(text="Cutaneous lymphoma, NOS") )
        setattr(cls, "Myxopapillary ependymoma",
                PermissibleValue(text="Myxopapillary ependymoma") )
        setattr(cls, "Soft tissue tumor, malignant",
                PermissibleValue(text="Soft tissue tumor, malignant") )
        setattr(cls, "Syringadenoma, NOS",
                PermissibleValue(text="Syringadenoma, NOS") )
        setattr(cls, "Monocytic leukemia, NOS",
                PermissibleValue(text="Monocytic leukemia, NOS") )
        setattr(cls, "Intraductal papillary neoplasm with low grade intraepithelial neoplasia",
                PermissibleValue(text="Intraductal papillary neoplasm with low grade intraepithelial neoplasia") )
        setattr(cls, "Ductal carcinoma, NOS",
                PermissibleValue(text="Ductal carcinoma, NOS") )
        setattr(cls, "Adenocarcinoma of anal glands",
                PermissibleValue(text="Adenocarcinoma of anal glands") )
        setattr(cls, "Papillary glioneuronal tumor",
                PermissibleValue(text="Papillary glioneuronal tumor") )
        setattr(cls, "Malignant lymphoma, lymphocytic, well differentiated, nodular",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, well differentiated, nodular") )
        setattr(cls, "Systemic mastocytosis with associated hematological clonal non-mast cell disorder",
                PermissibleValue(text="Systemic mastocytosis with associated hematological clonal non-mast cell disorder") )
        setattr(cls, "Hepatocellular adenoma",
                PermissibleValue(text="Hepatocellular adenoma") )
        setattr(cls, "Malignant myelosclerosis",
                PermissibleValue(text="Malignant myelosclerosis") )
        setattr(cls, "Diffuse intraductal papillomatosis",
                PermissibleValue(text="Diffuse intraductal papillomatosis") )
        setattr(cls, "Non-invasive mammary carcinoma",
                PermissibleValue(text="Non-invasive mammary carcinoma") )
        setattr(cls, "Verrucous squamous cell carcinoma",
                PermissibleValue(text="Verrucous squamous cell carcinoma") )
        setattr(cls, "Adrenal cortical adenoma, pigmented",
                PermissibleValue(text="Adrenal cortical adenoma, pigmented") )
        setattr(cls, "Parasympathetic paraganglioma",
                PermissibleValue(text="Parasympathetic paraganglioma") )
        setattr(cls, "Acute myeloid leukemia, M6 type",
                PermissibleValue(text="Acute myeloid leukemia, M6 type") )
        setattr(cls, "Papillotubular adenocarcinoma",
                PermissibleValue(text="Papillotubular adenocarcinoma") )
        setattr(cls, "Solitary mastocytoma of skin",
                PermissibleValue(text="Solitary mastocytoma of skin") )
        setattr(cls, "Thymoma, lymphocyte-rich, malignant",
                PermissibleValue(text="Thymoma, lymphocyte-rich, malignant") )
        setattr(cls, "Adenomyoepithelioma with carcinoma",
                PermissibleValue(text="Adenomyoepithelioma with carcinoma") )
        setattr(cls, "Juxtacortical chondrosarcoma",
                PermissibleValue(text="Juxtacortical chondrosarcoma") )
        setattr(cls, "Adenocarcinoma in multiple adenomatous polyps",
                PermissibleValue(text="Adenocarcinoma in multiple adenomatous polyps") )
        setattr(cls, "Mesonephric adenoma",
                PermissibleValue(text="Mesonephric adenoma") )
        setattr(cls, "Undifferentiated spindle cell sarcoma",
                PermissibleValue(text="Undifferentiated spindle cell sarcoma") )
        setattr(cls, "Noninfiltrating intraductal papillary carcinoma",
                PermissibleValue(text="Noninfiltrating intraductal papillary carcinoma") )
        setattr(cls, "Papillary transitional cell neoplasm of low malignant potential",
                PermissibleValue(text="Papillary transitional cell neoplasm of low malignant potential") )
        setattr(cls, "Fibrous mesothelioma, NOS",
                PermissibleValue(text="Fibrous mesothelioma, NOS") )
        setattr(cls, "Intraductal adenocarcinoma, noninfiltrating, NOS",
                PermissibleValue(text="Intraductal adenocarcinoma, noninfiltrating, NOS") )
        setattr(cls, "Sex cord-gonadal stromal tumor, NOS",
                PermissibleValue(text="Sex cord-gonadal stromal tumor, NOS") )
        setattr(cls, "Malignant lymphoma, lymphocytic, well differentiated, diffuse",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, well differentiated, diffuse") )
        setattr(cls, "Mixed pineal tumor",
                PermissibleValue(text="Mixed pineal tumor") )
        setattr(cls, "Acute myelosclerosis, NOS",
                PermissibleValue(text="Acute myelosclerosis, NOS") )
        setattr(cls, "Intraductal papillary neoplasm with high grade dysplasia",
                PermissibleValue(text="Intraductal papillary neoplasm with high grade dysplasia") )
        setattr(cls, "Alpha cell tumor, malignant",
                PermissibleValue(text="Alpha cell tumor, malignant") )
        setattr(cls, "Infiltrating duct and lobular carcinoma",
                PermissibleValue(text="Infiltrating duct and lobular carcinoma") )
        setattr(cls, "Endometrioid tumor of low malignant potential",
                PermissibleValue(text="Endometrioid tumor of low malignant potential") )
        setattr(cls, "Mesoblastic nephroma",
                PermissibleValue(text="Mesoblastic nephroma") )
        setattr(cls, "Acute panmyelosis with myelofibrosis",
                PermissibleValue(text="Acute panmyelosis with myelofibrosis") )
        setattr(cls, "RAEB II",
                PermissibleValue(text="RAEB II") )
        setattr(cls, "Juvenile histiocytoma",
                PermissibleValue(text="Juvenile histiocytoma") )
        setattr(cls, "Basaloid squamous cell carcinoma",
                PermissibleValue(text="Basaloid squamous cell carcinoma",
                                 description="Basaloid Squamous Cell Carcinoma") )
        setattr(cls, "Myelofibrosis as a result of myeloproliferative disease",
                PermissibleValue(text="Myelofibrosis as a result of myeloproliferative disease") )
        setattr(cls, "Renal medullary carcinoma",
                PermissibleValue(text="Renal medullary carcinoma",
                                 description="Kidney Medullary Carcinoma") )
        setattr(cls, "Hepatocellular carcinoma, pleomorphic type",
                PermissibleValue(text="Hepatocellular carcinoma, pleomorphic type") )
        setattr(cls, "Giant cell glioblastoma",
                PermissibleValue(text="Giant cell glioblastoma") )
        setattr(cls, "Classical Hodgkin lymphoma, nodular sclerosis, grade 1",
                PermissibleValue(text="Classical Hodgkin lymphoma, nodular sclerosis, grade 1") )
        setattr(cls, "Pilomatricoma, NOS",
                PermissibleValue(text="Pilomatricoma, NOS") )
        setattr(cls, "Squamous carcinoma",
                PermissibleValue(text="Squamous carcinoma") )
        setattr(cls, "Primary serous papillary carcinoma of peritoneum",
                PermissibleValue(text="Primary serous papillary carcinoma of peritoneum") )
        setattr(cls, "Intraductal carcinoma, clinging",
                PermissibleValue(text="Intraductal carcinoma, clinging") )
        setattr(cls, "Acute myeloid leukemia with t(8;21)(q22;q22); RUNX1-RUNX1T1",
                PermissibleValue(text="Acute myeloid leukemia with t(8;21)(q22;q22); RUNX1-RUNX1T1") )
        setattr(cls, "Malignant fibrous histiocytoma",
                PermissibleValue(text="Malignant fibrous histiocytoma") )
        setattr(cls, "T-cell lymphoma, NOS",
                PermissibleValue(text="T-cell lymphoma, NOS") )
        setattr(cls, "Anal intraepithelial neoplasia, grade III",
                PermissibleValue(text="Anal intraepithelial neoplasia, grade III") )
        setattr(cls, "Follicular lymphoma, small cleaved cell",
                PermissibleValue(text="Follicular lymphoma, small cleaved cell") )
        setattr(cls, "Hepatoblastoma, epithelioid",
                PermissibleValue(text="Hepatoblastoma, epithelioid") )
        setattr(cls, "Olfactory neuroepithelioma",
                PermissibleValue(text="Olfactory neuroepithelioma") )
        setattr(cls, "Medullary osteosarcoma",
                PermissibleValue(text="Medullary osteosarcoma") )
        setattr(cls, "Squamous intraepithelial neoplasia, high grade",
                PermissibleValue(text="Squamous intraepithelial neoplasia, high grade") )
        setattr(cls, "Myofibroblastic sarcoma",
                PermissibleValue(text="Myofibroblastic sarcoma") )
        setattr(cls, "Mixed adenocarcinoma and epidermoid carcinoma",
                PermissibleValue(text="Mixed adenocarcinoma and epidermoid carcinoma") )
        setattr(cls, "Somatostatinoma, malignant",
                PermissibleValue(text="Somatostatinoma, malignant") )
        setattr(cls, "Nodal marginal zone lymphoma",
                PermissibleValue(text="Nodal marginal zone lymphoma") )
        setattr(cls, "Proliferative dermal lesion in congenital nevus",
                PermissibleValue(text="Proliferative dermal lesion in congenital nevus") )
        setattr(cls, "Periapical cemento-osseous dysplasia",
                PermissibleValue(text="Periapical cemento-osseous dysplasia") )
        setattr(cls, "Low-grade central osteosarcoma",
                PermissibleValue(text="Low-grade central osteosarcoma") )
        setattr(cls, "Lipid-rich carcinoma",
                PermissibleValue(text="Lipid-rich carcinoma") )
        setattr(cls, "Lepidic predominant adenocarcinoma",
                PermissibleValue(text="Lepidic predominant adenocarcinoma",
                                 description="Lepidic Predominant Adenocarcinoma") )
        setattr(cls, "Malignant tumor, small cell type",
                PermissibleValue(text="Malignant tumor, small cell type") )
        setattr(cls, "Adenocarcinoma, NOS",
                PermissibleValue(text="Adenocarcinoma, NOS") )
        setattr(cls, "Wolffian duct tumor",
                PermissibleValue(text="Wolffian duct tumor") )
        setattr(cls, "Oligodendroglioma, NOS",
                PermissibleValue(text="Oligodendroglioma, NOS") )
        setattr(cls, "Melanoma, malignant, of soft parts",
                PermissibleValue(text="Melanoma, malignant, of soft parts") )
        setattr(cls, "Extra-adrenal paraganglioma, malignant",
                PermissibleValue(text="Extra-adrenal paraganglioma, malignant") )
        setattr(cls, "Goblet cell carcinoid",
                PermissibleValue(text="Goblet cell carcinoid") )
        setattr(cls, "Mixed pineocytoma-pineoblastoma",
                PermissibleValue(text="Mixed pineocytoma-pineoblastoma") )
        setattr(cls, "Ameloblastic odontosarcoma",
                PermissibleValue(text="Ameloblastic odontosarcoma") )
        setattr(cls, "Junction nevus",
                PermissibleValue(text="Junction nevus") )
        setattr(cls, "Hodgkin disease, NOS",
                PermissibleValue(text="Hodgkin disease, NOS") )
        setattr(cls, "Composite carcinoid",
                PermissibleValue(text="Composite carcinoid") )
        setattr(cls, "Papillary carcinoma, columnar cell",
                PermissibleValue(text="Papillary carcinoma, columnar cell") )
        setattr(cls, "Cystic mesothelioma, NOS",
                PermissibleValue(text="Cystic mesothelioma, NOS") )
        setattr(cls, "Undifferentiated high-grade pleomorphic sarcoma",
                PermissibleValue(text="Undifferentiated high-grade pleomorphic sarcoma") )
        setattr(cls, "Cystic hypersecretory carcinoma",
                PermissibleValue(text="Cystic hypersecretory carcinoma") )
        setattr(cls, "Phosphaturic mesenchymal tumor, malignant",
                PermissibleValue(text="Phosphaturic mesenchymal tumor, malignant") )
        setattr(cls, "Mantle cell lymphoma (Includes all variants blastic, pleomorphic, small cell)",
                PermissibleValue(text="Mantle cell lymphoma (Includes all variants blastic, pleomorphic, small cell)") )
        setattr(cls, "MiT family translocation renal cell carcinoma",
                PermissibleValue(text="MiT family translocation renal cell carcinoma",
                                 description="MiT Family Translocation-Associated Renal Cell Carcinoma") )
        setattr(cls, "Medulloblastoma, group 4",
                PermissibleValue(text="Medulloblastoma, group 4") )
        setattr(cls, "Clear cell adenocarcinofibroma",
                PermissibleValue(text="Clear cell adenocarcinofibroma") )
        setattr(cls, "Clear cell adenocarcinoma, NOS",
                PermissibleValue(text="Clear cell adenocarcinoma, NOS") )
        setattr(cls, "Splenic B-cell lymphoma/leukemia, unclassifiable",
                PermissibleValue(text="Splenic B-cell lymphoma/leukemia, unclassifiable") )
        setattr(cls, "Dermoid cyst with secondary tumor",
                PermissibleValue(text="Dermoid cyst with secondary tumor") )
        setattr(cls, "Thymoma, type B3, malignant",
                PermissibleValue(text="Thymoma, type B3, malignant") )
        setattr(cls, "PTLD, NOS",
                PermissibleValue(text="PTLD, NOS") )
        setattr(cls, "Angiocentric T-cell lymphoma",
                PermissibleValue(text="Angiocentric T-cell lymphoma") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, Clara cell and goblet cell type",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, Clara cell and goblet cell type") )
        setattr(cls, "DCIS, comedo type",
                PermissibleValue(text="DCIS, comedo type") )
        setattr(cls, "Duct adenoma, NOS",
                PermissibleValue(text="Duct adenoma, NOS") )
        setattr(cls, "Squamous cell carcinoma, adenoid",
                PermissibleValue(text="Squamous cell carcinoma, adenoid") )
        setattr(cls, "Lymphosarcoma cell leukemia",
                PermissibleValue(text="Lymphosarcoma cell leukemia") )
        setattr(cls, "Classical Hodgkin lymphoma, nodular sclerosis, NOS",
                PermissibleValue(text="Classical Hodgkin lymphoma, nodular sclerosis, NOS") )
        setattr(cls, "Queyrat erythroplasia",
                PermissibleValue(text="Queyrat erythroplasia") )
        setattr(cls, "Intravascular leiomyomatosis",
                PermissibleValue(text="Intravascular leiomyomatosis") )
        setattr(cls, "Meningioma, NOS",
                PermissibleValue(text="Meningioma, NOS") )
        setattr(cls, "Giant cell sarcoma of bone",
                PermissibleValue(text="Giant cell sarcoma of bone") )
        setattr(cls, "T-gamma lymphoproliferative disease",
                PermissibleValue(text="T-gamma lymphoproliferative disease") )
        setattr(cls, "Osteoma, NOS",
                PermissibleValue(text="Osteoma, NOS") )
        setattr(cls, "High-grade serous carcinoma",
                PermissibleValue(text="High-grade serous carcinoma") )
        setattr(cls, "GIST, NOS",
                PermissibleValue(text="GIST, NOS") )
        setattr(cls, "Intraductal tubulopapillary neoplasm",
                PermissibleValue(text="Intraductal tubulopapillary neoplasm") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, type II pneumocyte and goblet cell type",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, type II pneumocyte and goblet cell type") )
        setattr(cls, "Beta cell adenoma",
                PermissibleValue(text="Beta cell adenoma") )
        setattr(cls, "Hepatoma, NOS",
                PermissibleValue(text="Hepatoma, NOS") )
        setattr(cls, "Acinic cell adenoma",
                PermissibleValue(text="Acinic cell adenoma") )
        setattr(cls, "Invasive micropapillary carcinoma",
                PermissibleValue(text="Invasive micropapillary carcinoma") )
        setattr(cls, "Well differentiated thymic carcinoma",
                PermissibleValue(text="Well differentiated thymic carcinoma") )
        setattr(cls, "Gastrinoma, malignant",
                PermissibleValue(text="Gastrinoma, malignant") )
        setattr(cls, "Bronchiolo-alveolar carcinoma, non-mucinous",
                PermissibleValue(text="Bronchiolo-alveolar carcinoma, non-mucinous") )
        setattr(cls, "Epithelioid malignant peripheral nerve sheath tumor",
                PermissibleValue(text="Epithelioid malignant peripheral nerve sheath tumor") )
        setattr(cls, "Clear cell cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Clear cell cystadenofibroma of borderline malignancy") )
        setattr(cls, "Adrenal cortical tumor, NOS",
                PermissibleValue(text="Adrenal cortical tumor, NOS") )
        setattr(cls, "Medullary carcinoma with lymphoid stroma",
                PermissibleValue(text="Medullary carcinoma with lymphoid stroma") )
        setattr(cls, "Malignant melanoma in precancerous melanosis",
                PermissibleValue(text="Malignant melanoma in precancerous melanosis") )
        setattr(cls, "Malignant lymphoma, large cell, noncleaved, NOS",
                PermissibleValue(text="Malignant lymphoma, large cell, noncleaved, NOS") )
        setattr(cls, "Epidermoid carcinoma, small cell, nonkeratinizing",
                PermissibleValue(text="Epidermoid carcinoma, small cell, nonkeratinizing") )
        setattr(cls, "Tumor, secondary",
                PermissibleValue(text="Tumor, secondary") )
        setattr(cls, "Glioblastoma, IDH-mutant",
                PermissibleValue(text="Glioblastoma, IDH-mutant") )
        setattr(cls, "Carcinoma in adenomatous polyp",
                PermissibleValue(text="Carcinoma in adenomatous polyp") )
        setattr(cls, "MALT lymphoma",
                PermissibleValue(text="MALT lymphoma") )
        setattr(cls, "Follicular lymphoma, grade 3B",
                PermissibleValue(text="Follicular lymphoma, grade 3B") )
        setattr(cls, "Pleomorphic lobular carcinoma",
                PermissibleValue(text="Pleomorphic lobular carcinoma") )
        setattr(cls, "NUT midline carcinoma",
                PermissibleValue(text="NUT midline carcinoma") )
        setattr(cls, "Juvenile astrocytoma",
                PermissibleValue(text="Juvenile astrocytoma") )
        setattr(cls, "Adenocarcinoma, pancreatobiliary type",
                PermissibleValue(text="Adenocarcinoma, pancreatobiliary type") )
        setattr(cls, "Serous cystoma",
                PermissibleValue(text="Serous cystoma") )
        setattr(cls, "Sympathetic paraganglioma",
                PermissibleValue(text="Sympathetic paraganglioma") )
        setattr(cls, "Adenocarcinoma in adenomatous polyp",
                PermissibleValue(text="Adenocarcinoma in adenomatous polyp") )
        setattr(cls, "Papillary adenoma, NOS",
                PermissibleValue(text="Papillary adenoma, NOS") )
        setattr(cls, "Esophageal intraepithelial neoplasia, high grade",
                PermissibleValue(text="Esophageal intraepithelial neoplasia, high grade") )
        setattr(cls, "Acute basophilic leukaemia",
                PermissibleValue(text="Acute basophilic leukaemia") )
        setattr(cls, "Papillary adenocarcinoma, follicular variant",
                PermissibleValue(text="Papillary adenocarcinoma, follicular variant") )
        setattr(cls, "Hodgkin disease, nodular sclerosis, NOS",
                PermissibleValue(text="Hodgkin disease, nodular sclerosis, NOS") )
        setattr(cls, "Giant cell tumor of bone, NOS",
                PermissibleValue(text="Giant cell tumor of bone, NOS") )
        setattr(cls, "Mixed medullary-follicular carcinoma",
                PermissibleValue(text="Mixed medullary-follicular carcinoma") )
        setattr(cls, "Acinar adenocarcinoma",
                PermissibleValue(text="Acinar adenocarcinoma") )
        setattr(cls, "Serrated adenocarcinoma",
                PermissibleValue(text="Serrated adenocarcinoma") )
        setattr(cls, "Papillary serous cystadenoma, borderline malignancy",
                PermissibleValue(text="Papillary serous cystadenoma, borderline malignancy") )
        setattr(cls, "Adenocarcinoma in tubolovillous adenoma",
                PermissibleValue(text="Adenocarcinoma in tubolovillous adenoma") )
        setattr(cls, "Infantile fibrosarcoma",
                PermissibleValue(text="Infantile fibrosarcoma") )
        setattr(cls, "Phyllodes tumor, borderline",
                PermissibleValue(text="Phyllodes tumor, borderline") )
        setattr(cls, "Hodgkin paragranuloma, NOS",
                PermissibleValue(text="Hodgkin paragranuloma, NOS") )
        setattr(cls, "Thymoma, cortical, malignant",
                PermissibleValue(text="Thymoma, cortical, malignant") )
        setattr(cls, "Mucinous cystadenofibroma of borderline malignancy",
                PermissibleValue(text="Mucinous cystadenofibroma of borderline malignancy") )
        setattr(cls, "GIST, benign",
                PermissibleValue(text="GIST, benign") )
        setattr(cls, "Islet cell carcinoma",
                PermissibleValue(text="Islet cell carcinoma") )
        setattr(cls, "Eccrine cystadenoma",
                PermissibleValue(text="Eccrine cystadenoma") )
        setattr(cls, "Mullerian mixed tumor",
                PermissibleValue(text="Mullerian mixed tumor") )
        setattr(cls, "Multiple neurofibromatosis",
                PermissibleValue(text="Multiple neurofibromatosis") )
        setattr(cls, "Mesothelioma, malignant",
                PermissibleValue(text="Mesothelioma, malignant") )
        setattr(cls, "Acute myeloid leukemia with mutated CEBPA",
                PermissibleValue(text="Acute myeloid leukemia with mutated CEBPA") )
        setattr(cls, "Pancreatobiliary neoplasm, non-invasive",
                PermissibleValue(text="Pancreatobiliary neoplasm, non-invasive") )
        setattr(cls, "Warty carcinoma",
                PermissibleValue(text="Warty carcinoma") )
        setattr(cls, "Micropapillary carcinoma, NOS",
                PermissibleValue(text="Micropapillary carcinoma, NOS") )
        setattr(cls, "Glioblastoma, IDH wildtype",
                PermissibleValue(text="Glioblastoma, IDH wildtype") )
        setattr(cls, "Acute monocytic leukemia",
                PermissibleValue(text="Acute monocytic leukemia") )
        setattr(cls, "FAB M7",
                PermissibleValue(text="FAB M7") )
        setattr(cls, "Mucinous cystic neoplasm with an associated invasive carcinoma",
                PermissibleValue(text="Mucinous cystic neoplasm with an associated invasive carcinoma",
                                 description="Bile Duct Cystadenocarcinoma") )
        setattr(cls, "Subacute monocytic leukemia",
                PermissibleValue(text="Subacute monocytic leukemia") )
        setattr(cls, "Dermoid cyst with malignant transformation",
                PermissibleValue(text="Dermoid cyst with malignant transformation") )
        setattr(cls, "Vascular leiomyoma",
                PermissibleValue(text="Vascular leiomyoma") )
        setattr(cls, "Retinoblastoma, diffuse",
                PermissibleValue(text="Retinoblastoma, diffuse") )
        setattr(cls, "Deep histiocytoma",
                PermissibleValue(text="Deep histiocytoma") )
        setattr(cls, "Malignant lymphoma, large cell, noncleaved, diffuse",
                PermissibleValue(text="Malignant lymphoma, large cell, noncleaved, diffuse") )
        setattr(cls, "Peripheral T-cell lymphoma, pleomorphic medium and large cell",
                PermissibleValue(text="Peripheral T-cell lymphoma, pleomorphic medium and large cell") )
        setattr(cls, "Mast cell leukaemia",
                PermissibleValue(text="Mast cell leukaemia") )
        setattr(cls, "Ameloblastoma, malignant",
                PermissibleValue(text="Ameloblastoma, malignant") )
        setattr(cls, "Non-invasive follicular thyroid neoplasm with papillary-like nuclear features (NIFTP)",
                PermissibleValue(text="Non-invasive follicular thyroid neoplasm with papillary-like nuclear features (NIFTP)") )
        setattr(cls, "Chondromyxoid fibroma",
                PermissibleValue(text="Chondromyxoid fibroma") )
        setattr(cls, "Granular cell tumor, malignant",
                PermissibleValue(text="Granular cell tumor, malignant") )
        setattr(cls, "Cerebellar liponeurocytoma",
                PermissibleValue(text="Cerebellar liponeurocytoma") )
        setattr(cls, "Mucinous cystic neoplasm with low-grade dysplasia",
                PermissibleValue(text="Mucinous cystic neoplasm with low-grade dysplasia") )
        setattr(cls, "Large cell calcifying Sertoli cell tumor",
                PermissibleValue(text="Large cell calcifying Sertoli cell tumor") )
        setattr(cls, "Cavernous lymphangioma",
                PermissibleValue(text="Cavernous lymphangioma") )
        setattr(cls, "Myxoid chondrosarcoma",
                PermissibleValue(text="Myxoid chondrosarcoma") )
        setattr(cls, "Botryoid sarcoma",
                PermissibleValue(text="Botryoid sarcoma") )
        setattr(cls, "Adrenal cortical carcinoma",
                PermissibleValue(text="Adrenal cortical carcinoma") )
        setattr(cls, "Epithelioid leiomyoma",
                PermissibleValue(text="Epithelioid leiomyoma") )
        setattr(cls, "Malignant lymphoma, lymphocytic, nodular, NOS",
                PermissibleValue(text="Malignant lymphoma, lymphocytic, nodular, NOS") )
        setattr(cls, "Squamous papillomatosis",
                PermissibleValue(text="Squamous papillomatosis") )
        setattr(cls, "Ductal carcinoma in situ, NOS",
                PermissibleValue(text="Ductal carcinoma in situ, NOS") )
        setattr(cls, "Basophil carcinoma",
                PermissibleValue(text="Basophil carcinoma") )
        setattr(cls, "Secondary carcinoma",
                PermissibleValue(text="Secondary carcinoma") )
        setattr(cls, "Pagetoid reticulosis",
                PermissibleValue(text="Pagetoid reticulosis") )
        setattr(cls, "Undifferentiated pleomorphic sarcoma",
                PermissibleValue(text="Undifferentiated pleomorphic sarcoma") )
        setattr(cls, "Invasive lobular carcinoma, tubulolobular variant",
                PermissibleValue(text="Invasive lobular carcinoma, tubulolobular variant") )
        setattr(cls, "Mixed subependymoma-ependymoma",
                PermissibleValue(text="Mixed subependymoma-ependymoma") )
        setattr(cls, "Primary effusion lymphoma",
                PermissibleValue(text="Primary effusion lymphoma") )
        setattr(cls, "Squamotransitional cell carcinoma",
                PermissibleValue(text="Squamotransitional cell carcinoma") )
        setattr(cls, "Cystic astrocytoma",
                PermissibleValue(text="Cystic astrocytoma") )
        setattr(cls, "Plasmacytoma, extramedullary",
                PermissibleValue(text="Plasmacytoma, extramedullary") )
        setattr(cls, "Follicular carcinoma, well differentiated",
                PermissibleValue(text="Follicular carcinoma, well differentiated") )
        setattr(cls, "Chordoid glioma",
                PermissibleValue(text="Chordoid glioma") )
        setattr(cls, "Precursor B-cell lymphoblastic lymphoma",
                PermissibleValue(text="Precursor B-cell lymphoblastic lymphoma") )
        setattr(cls, "Cementifying fibroma",
                PermissibleValue(text="Cementifying fibroma") )
        setattr(cls, "Adrenal rest tumor",
                PermissibleValue(text="Adrenal rest tumor") )
        setattr(cls, "Hairy cell leukemia",
                PermissibleValue(text="Hairy cell leukemia") )
        setattr(cls, "Peripheral odontogenic fibroma",
                PermissibleValue(text="Peripheral odontogenic fibroma") )
        setattr(cls, "Struma ovarii and carcinoid",
                PermissibleValue(text="Struma ovarii and carcinoid") )
        setattr(cls, "Ameloblastic fibro-odontosarcoma",
                PermissibleValue(text="Ameloblastic fibro-odontosarcoma") )
        setattr(cls, "Seminoma with high mitotic index",
                PermissibleValue(text="Seminoma with high mitotic index") )
        setattr(cls, "Nonencapsulated sclerosing tumor",
                PermissibleValue(text="Nonencapsulated sclerosing tumor") )
        setattr(cls, "Cartilaginous exostosis",
                PermissibleValue(text="Cartilaginous exostosis") )
        setattr(cls, "Mixed tumor, salivary gland type, malignant",
                PermissibleValue(text="Mixed tumor, salivary gland type, malignant") )
        setattr(cls, "Acute myeloid leukemia, CBF-beta/MYH11",
                PermissibleValue(text="Acute myeloid leukemia, CBF-beta/MYH11") )
        setattr(cls, "Aortic body paraganglioma",
                PermissibleValue(text="Aortic body paraganglioma") )
        setattr(cls, "Junctional nevus, NOS",
                PermissibleValue(text="Junctional nevus, NOS") )
        setattr(cls, "Odontogenic fibrosarcoma",
                PermissibleValue(text="Odontogenic fibrosarcoma") )
        setattr(cls, "Mixed hepatocellular and bile duct carcinoma",
                PermissibleValue(text="Mixed hepatocellular and bile duct carcinoma") )
        setattr(cls, "L-cell tumor",
                PermissibleValue(text="L-cell tumor") )
        setattr(cls, "Malignant lymphoma, large cell, follicular, NOS",
                PermissibleValue(text="Malignant lymphoma, large cell, follicular, NOS") )
        setattr(cls, "RAEB-T",
                PermissibleValue(text="RAEB-T") )
        setattr(cls, "Papillary urothelial carcinoma",
                PermissibleValue(text="Papillary urothelial carcinoma") )
        setattr(cls, "Periosteal sarcoma, NOS",
                PermissibleValue(text="Periosteal sarcoma, NOS") )
        setattr(cls, "Acute myeloid leukemia with abnormal marrow eosinophils (includes all variants)",
                PermissibleValue(text="Acute myeloid leukemia with abnormal marrow eosinophils (includes all variants)") )
        setattr(cls, "Serous adenofibroma of borderline malignancy",
                PermissibleValue(text="Serous adenofibroma of borderline malignancy") )
        setattr(cls, "Langerhans cell histiocytosis, poly-ostotic",
                PermissibleValue(text="Langerhans cell histiocytosis, poly-ostotic") )
        setattr(cls, "Kaposi sarcoma",
                PermissibleValue(text="Kaposi sarcoma") )
        setattr(cls, "Meningeal sarcomatosis",
                PermissibleValue(text="Meningeal sarcomatosis") )
        setattr(cls, "Epithelioma adenoides cysticum",
                PermissibleValue(text="Epithelioma adenoides cysticum") )
        setattr(cls, "Combined/mixed carcinoid and adenocarcinoma",
                PermissibleValue(text="Combined/mixed carcinoid and adenocarcinoma") )
        setattr(cls, "Lipoid cell tumor of ovary",
                PermissibleValue(text="Lipoid cell tumor of ovary") )
        setattr(cls, "Carcinoma in situ in adenomatous polyp",
                PermissibleValue(text="Carcinoma in situ in adenomatous polyp") )
        setattr(cls, "Lentigo maligna melanoma",
                PermissibleValue(text="Lentigo maligna melanoma",
                                 description="Lentigo Maligna Melanoma") )
        setattr(cls, "Juxtacortical osteosarcoma",
                PermissibleValue(text="Juxtacortical osteosarcoma") )
        setattr(cls, "Eccrine dermal cylindroma",
                PermissibleValue(text="Eccrine dermal cylindroma") )
        setattr(cls, "Ductal carcinoma in situ, cribriform type",
                PermissibleValue(text="Ductal carcinoma in situ, cribriform type") )
        setattr(cls, "NK/T-cell lymphoma, nasal and nasal-type",
                PermissibleValue(text="NK/T-cell lymphoma, nasal and nasal-type") )
        setattr(cls, "Fibroameloblastic odontoma",
                PermissibleValue(text="Fibroameloblastic odontoma") )
        setattr(cls, "Rosette-forming glioneuronal tumor",
                PermissibleValue(text="Rosette-forming glioneuronal tumor") )
        setattr(cls, "Glucagonoma, malignant",
                PermissibleValue(text="Glucagonoma, malignant") )
        setattr(cls, "Ependymoma, RELA fusion-positive",
                PermissibleValue(text="Ependymoma, RELA fusion-positive") )
        setattr(cls, "Burkitt cell leukemia",
                PermissibleValue(text="Burkitt cell leukemia") )
        setattr(cls, "Eosinophil adenocarcinoma",
                PermissibleValue(text="Eosinophil adenocarcinoma") )
        setattr(cls, "Magnocellular nevus",
                PermissibleValue(text="Magnocellular nevus") )
        setattr(cls, "Intraductal tubular-papillary neoplasm, high grade",
                PermissibleValue(text="Intraductal tubular-papillary neoplasm, high grade") )
        setattr(cls, "Papillary serous cystadenocarcinoma",
                PermissibleValue(text="Papillary serous cystadenocarcinoma") )
        setattr(cls, "Polygonal cell carcinoma",
                PermissibleValue(text="Polygonal cell carcinoma") )
        setattr(cls, "Medulloblastoma, SHH-activated and TP53-mutant",
                PermissibleValue(text="Medulloblastoma, SHH-activated and TP53-mutant") )
        setattr(cls, "Merkel cell carcinoma",
                PermissibleValue(text="Merkel cell carcinoma") )
        setattr(cls, "Malignant lymphoma, centroblasticcentrocytic, NOS",
                PermissibleValue(text="Malignant lymphoma, centroblasticcentrocytic, NOS") )
        setattr(cls, "Fibroadenoma, NOS",
                PermissibleValue(text="Fibroadenoma, NOS") )
        setattr(cls, "Adrenal cortical tumor, malignant",
                PermissibleValue(text="Adrenal cortical tumor, malignant") )
        setattr(cls, "Anaplastic large cell lymphoma, NOS",
                PermissibleValue(text="Anaplastic large cell lymphoma, NOS") )
        setattr(cls, "Malignant lymphoma, centrocytic",
                PermissibleValue(text="Malignant lymphoma, centrocytic") )
        setattr(cls, "Lobular carcinoma, NOS",
                PermissibleValue(text="Lobular carcinoma, NOS") )
        setattr(cls, "Malignant tumor, clear cell type",
                PermissibleValue(text="Malignant tumor, clear cell type") )
        setattr(cls, "Intimal sarcoma",
                PermissibleValue(text="Intimal sarcoma") )
        setattr(cls, "FAB M2, NOS",
                PermissibleValue(text="FAB M2, NOS") )
        setattr(cls, "Hemangioendothelioma, benign",
                PermissibleValue(text="Hemangioendothelioma, benign") )
        setattr(cls, "Codman tumor",
                PermissibleValue(text="Codman tumor") )
        setattr(cls, "Hepatosplenic gamma-delta cell lymphoma",
                PermissibleValue(text="Hepatosplenic gamma-delta cell lymphoma") )
        setattr(cls, "Cementoblastoma, benign",
                PermissibleValue(text="Cementoblastoma, benign") )
        setattr(cls, "Stromal tumor, benign",
                PermissibleValue(text="Stromal tumor, benign") )
        setattr(cls, "Embryonal carcinoma, polyembryonal type",
                PermissibleValue(text="Embryonal carcinoma, polyembryonal type") )
        setattr(cls, "Somatostatin cell tumor, malignant",
                PermissibleValue(text="Somatostatin cell tumor, malignant") )
        setattr(cls, "Juxtaglomerular tumor",
                PermissibleValue(text="Juxtaglomerular tumor") )
        setattr(cls, "Intraepidermal epithelioma of Jadassohn",
                PermissibleValue(text="Intraepidermal epithelioma of Jadassohn") )
        setattr(cls, "Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis",
                PermissibleValue(text="Hodgkin lymphoma, lymphocyte depletion, diffuse fibrosis") )
        setattr(cls, "Papillary neoplasm, pancreatobiliary-type, with high grade intraepithelial neoplasia",
                PermissibleValue(text="Papillary neoplasm, pancreatobiliary-type, with high grade intraepithelial neoplasia") )
        setattr(cls, "Primary intraosseous carcinoma",
                PermissibleValue(text="Primary intraosseous carcinoma") )
        setattr(cls, "Capillary lymphangioma",
                PermissibleValue(text="Capillary lymphangioma") )
        setattr(cls, "Histiocytosis X, NOS",
                PermissibleValue(text="Histiocytosis X, NOS") )
        setattr(cls, "Squamous cell carcinoma in situ with questionable stromal invasion",
                PermissibleValue(text="Squamous cell carcinoma in situ with questionable stromal invasion") )
        setattr(cls, "Acute myeloid leukemia with t(6;9)(p23;q34); DEK-NUP214",
                PermissibleValue(text="Acute myeloid leukemia with t(6;9)(p23;q34); DEK-NUP214") )
        setattr(cls, "Clear cell cystic tumor of borderline malignancy",
                PermissibleValue(text="Clear cell cystic tumor of borderline malignancy") )
        setattr(cls, "MPNST with mesenchymal differentiation",
                PermissibleValue(text="MPNST with mesenchymal differentiation") )
        setattr(cls, "Secretory carcinoma of breast",
                PermissibleValue(text="Secretory carcinoma of breast") )
        setattr(cls, "Chordoid glioma of third ventricle",
                PermissibleValue(text="Chordoid glioma of third ventricle") )
        setattr(cls, "Basal cell carcinoma, NOS",
                PermissibleValue(text="Basal cell carcinoma, NOS") )
        setattr(cls, "Chondrosarcoma, NOS",
                PermissibleValue(text="Chondrosarcoma, NOS") )
        setattr(cls, "Lipid cell tumor of ovary",
                PermissibleValue(text="Lipid cell tumor of ovary") )
        setattr(cls, "Renal cell carcinoma, unclassified",
                PermissibleValue(text="Renal cell carcinoma, unclassified",
                                 description="Unclassified Renal Cell Carcinoma") )

class CCDHDiagnosisMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis morphology
    """
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="CCDHDiagnosisMorphology",
        description="Autogenerated Enumeration for CRDC-H Diagnosis morphology",
        code_set=None,
        code_set_version="2021-05-30T01:20:46.336069+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "9805/3",
                PermissibleValue(text="9805/3") )
        setattr(cls, "8257/3",
                PermissibleValue(text="8257/3") )
        setattr(cls, "8001/1",
                PermissibleValue(text="8001/1") )
        setattr(cls, "9691/3",
                PermissibleValue(text="9691/3") )
        setattr(cls, "8144/3",
                PermissibleValue(text="8144/3") )
        setattr(cls, "9757/3",
                PermissibleValue(text="9757/3") )
        setattr(cls, "8509/3",
                PermissibleValue(text="8509/3") )
        setattr(cls, "8572/3",
                PermissibleValue(text="8572/3") )
        setattr(cls, "8780/0",
                PermissibleValue(text="8780/0") )
        setattr(cls, "8935/3",
                PermissibleValue(text="8935/3") )
        setattr(cls, "8403/3",
                PermissibleValue(text="8403/3") )
        setattr(cls, "9105/3",
                PermissibleValue(text="9105/3") )
        setattr(cls, "9756/3",
                PermissibleValue(text="9756/3") )
        setattr(cls, "9064/3",
                PermissibleValue(text="9064/3") )
        setattr(cls, "8902/3",
                PermissibleValue(text="8902/3") )
        setattr(cls, "9910/3",
                PermissibleValue(text="9910/3") )
        setattr(cls, "8402/3",
                PermissibleValue(text="8402/3") )
        setattr(cls, "8850/0",
                PermissibleValue(text="8850/0") )
        setattr(cls, "8722/3",
                PermissibleValue(text="8722/3") )
        setattr(cls, "9931/3",
                PermissibleValue(text="9931/3") )
        setattr(cls, "9760/3",
                PermissibleValue(text="9760/3") )
        setattr(cls, "8034/3",
                PermissibleValue(text="8034/3") )
        setattr(cls, "8407/3",
                PermissibleValue(text="8407/3") )
        setattr(cls, "9728/3",
                PermissibleValue(text="9728/3") )
        setattr(cls, "9081/3",
                PermissibleValue(text="9081/3") )
        setattr(cls, "8700/0",
                PermissibleValue(text="8700/0") )
        setattr(cls, "9510/0",
                PermissibleValue(text="9510/0") )
        setattr(cls, "9396/3",
                PermissibleValue(text="9396/3") )
        setattr(cls, "8141/3",
                PermissibleValue(text="8141/3") )
        setattr(cls, "8130/1",
                PermissibleValue(text="8130/1") )
        setattr(cls, "8825/3",
                PermissibleValue(text="8825/3") )
        setattr(cls, "9321/0",
                PermissibleValue(text="9321/0") )
        setattr(cls, "8522/1",
                PermissibleValue(text="8522/1") )
        setattr(cls, "8030/3",
                PermissibleValue(text="8030/3") )
        setattr(cls, "8585/3",
                PermissibleValue(text="8585/3") )
        setattr(cls, "9675/3",
                PermissibleValue(text="9675/3") )
        setattr(cls, "9401/3",
                PermissibleValue(text="9401/3") )
        setattr(cls, "8319/3",
                PermissibleValue(text="8319/3") )
        setattr(cls, "9130/0",
                PermissibleValue(text="9130/0") )
        setattr(cls, "8523/3",
                PermissibleValue(text="8523/3") )
        setattr(cls, "9535/0",
                PermissibleValue(text="9535/0") )
        setattr(cls, "8409/3",
                PermissibleValue(text="8409/3") )
        setattr(cls, "8580/0",
                PermissibleValue(text="8580/0") )
        setattr(cls, "8975/1",
                PermissibleValue(text="8975/1") )
        setattr(cls, "8031/3",
                PermissibleValue(text="8031/3") )
        setattr(cls, "8130/2",
                PermissibleValue(text="8130/2") )
        setattr(cls, "9125/0",
                PermissibleValue(text="9125/0") )
        setattr(cls, "8221/0",
                PermissibleValue(text="8221/0") )
        setattr(cls, "9020/3",
                PermissibleValue(text="9020/3") )
        setattr(cls, "8812/3",
                PermissibleValue(text="8812/3") )
        setattr(cls, "8804/3",
                PermissibleValue(text="8804/3") )
        setattr(cls, "8740/3",
                PermissibleValue(text="8740/3") )
        setattr(cls, "8175/3",
                PermissibleValue(text="8175/3") )
        setattr(cls, "8250/2",
                PermissibleValue(text="8250/2") )
        setattr(cls, "9506/1",
                PermissibleValue(text="9506/1") )
        setattr(cls, "8023/3",
                PermissibleValue(text="8023/3") )
        setattr(cls, "9122/0",
                PermissibleValue(text="9122/0") )
        setattr(cls, "9172/0",
                PermissibleValue(text="9172/0") )
        setattr(cls, "9082/3",
                PermissibleValue(text="9082/3") )
        setattr(cls, "8263/3",
                PermissibleValue(text="8263/3") )
        setattr(cls, "8930/0",
                PermissibleValue(text="8930/0") )
        setattr(cls, "8726/0",
                PermissibleValue(text="8726/0") )
        setattr(cls, "8051/0",
                PermissibleValue(text="8051/0") )
        setattr(cls, "8173/3",
                PermissibleValue(text="8173/3") )
        setattr(cls, "9045/3",
                PermissibleValue(text="9045/3") )
        setattr(cls, "8550/1",
                PermissibleValue(text="8550/1") )
        setattr(cls, "8242/1",
                PermissibleValue(text="8242/1") )
        setattr(cls, "8000/1",
                PermissibleValue(text="8000/1") )
        setattr(cls, "9251/3",
                PermissibleValue(text="9251/3") )
        setattr(cls, "8260/0",
                PermissibleValue(text="8260/0") )
        setattr(cls, "8413/3",
                PermissibleValue(text="8413/3") )
        setattr(cls, "9364/3",
                PermissibleValue(text="9364/3") )
        setattr(cls, "9390/1",
                PermissibleValue(text="9390/1") )
        setattr(cls, "8110/0",
                PermissibleValue(text="8110/0") )
        setattr(cls, "9110/1",
                PermissibleValue(text="9110/1") )
        setattr(cls, "9800/3",
                PermissibleValue(text="9800/3") )
        setattr(cls, "8405/0",
                PermissibleValue(text="8405/0") )
        setattr(cls, "8410/0",
                PermissibleValue(text="8410/0") )
        setattr(cls, "9717/3",
                PermissibleValue(text="9717/3") )
        setattr(cls, "9133/3",
                PermissibleValue(text="9133/3") )
        setattr(cls, "9411/3",
                PermissibleValue(text="9411/3") )
        setattr(cls, "8936/0",
                PermissibleValue(text="8936/0") )
        setattr(cls, "8255/3",
                PermissibleValue(text="8255/3") )
        setattr(cls, "8950/3",
                PermissibleValue(text="8950/3") )
        setattr(cls, "9827/3",
                PermissibleValue(text="9827/3") )
        setattr(cls, "9170/0",
                PermissibleValue(text="9170/0") )
        setattr(cls, "8880/0",
                PermissibleValue(text="8880/0") )
        setattr(cls, "9180/3",
                PermissibleValue(text="9180/3") )
        setattr(cls, "8230/2",
                PermissibleValue(text="8230/2") )
        setattr(cls, "8991/3",
                PermissibleValue(text="8991/3") )
        setattr(cls, "8344/3",
                PermissibleValue(text="8344/3") )
        setattr(cls, "9390/3",
                PermissibleValue(text="9390/3") )
        setattr(cls, "9130/1",
                PermissibleValue(text="9130/1") )
        setattr(cls, "8140/6",
                PermissibleValue(text="8140/6") )
        setattr(cls, "8453/3",
                PermissibleValue(text="8453/3") )
        setattr(cls, "8693/3",
                PermissibleValue(text="8693/3") )
        setattr(cls, "8813/3",
                PermissibleValue(text="8813/3") )
        setattr(cls, "8584/1",
                PermissibleValue(text="8584/1") )
        setattr(cls, "9241/0",
                PermissibleValue(text="9241/0") )
        setattr(cls, "9895/3",
                PermissibleValue(text="9895/3") )
        setattr(cls, "9476/3",
                PermissibleValue(text="9476/3") )
        setattr(cls, "9161/1",
                PermissibleValue(text="9161/1") )
        setattr(cls, "9182/3",
                PermissibleValue(text="9182/3") )
        setattr(cls, "8120/1",
                PermissibleValue(text="8120/1") )
        setattr(cls, "9652/3",
                PermissibleValue(text="9652/3") )
        setattr(cls, "8390/0",
                PermissibleValue(text="8390/0") )
        setattr(cls, "8333/3",
                PermissibleValue(text="8333/3") )
        setattr(cls, "8332/3",
                PermissibleValue(text="8332/3") )
        setattr(cls, "8336/0",
                PermissibleValue(text="8336/0") )
        setattr(cls, "8152/3",
                PermissibleValue(text="8152/3") )
        setattr(cls, "8042/3",
                PermissibleValue(text="8042/3") )
        setattr(cls, "9560/0",
                PermissibleValue(text="9560/0") )
        setattr(cls, "9230/3",
                PermissibleValue(text="9230/3") )
        setattr(cls, "9171/0",
                PermissibleValue(text="9171/0") )
        setattr(cls, "9898/1",
                PermissibleValue(text="9898/1") )
        setattr(cls, "8371/0",
                PermissibleValue(text="8371/0") )
        setattr(cls, "8971/3",
                PermissibleValue(text="8971/3") )
        setattr(cls, "8400/0",
                PermissibleValue(text="8400/0") )
        setattr(cls, "9161/0",
                PermissibleValue(text="9161/0") )
        setattr(cls, "8542/3",
                PermissibleValue(text="8542/3") )
        setattr(cls, "9444/1",
                PermissibleValue(text="9444/1") )
        setattr(cls, "8723/0",
                PermissibleValue(text="8723/0") )
        setattr(cls, "9502/0",
                PermissibleValue(text="9502/0") )
        setattr(cls, "8323/3",
                PermissibleValue(text="8323/3") )
        setattr(cls, "8341/3",
                PermissibleValue(text="8341/3") )
        setattr(cls, "9073/1",
                PermissibleValue(text="9073/1") )
        setattr(cls, "9191/0",
                PermissibleValue(text="9191/0") )
        setattr(cls, "8120/0",
                PermissibleValue(text="8120/0") )
        setattr(cls, "8430/3",
                PermissibleValue(text="8430/3") )
        setattr(cls, "9769/1",
                PermissibleValue(text="9769/1") )
        setattr(cls, "8406/0",
                PermissibleValue(text="8406/0") )
        setattr(cls, "9533/0",
                PermissibleValue(text="9533/0") )
        setattr(cls, "8471/0",
                PermissibleValue(text="8471/0") )
        setattr(cls, "8502/3",
                PermissibleValue(text="8502/3") )
        setattr(cls, "9251/1",
                PermissibleValue(text="9251/1") )
        setattr(cls, "8714/3",
                PermissibleValue(text="8714/3") )
        setattr(cls, "9050/0",
                PermissibleValue(text="9050/0") )
        setattr(cls, "9250/1",
                PermissibleValue(text="9250/1") )
        setattr(cls, "8131/3",
                PermissibleValue(text="8131/3") )
        setattr(cls, "8761/3",
                PermissibleValue(text="8761/3") )
        setattr(cls, "9352/1",
                PermissibleValue(text="9352/1") )
        setattr(cls, "9187/3",
                PermissibleValue(text="9187/3") )
        setattr(cls, "8460/3",
                PermissibleValue(text="8460/3") )
        setattr(cls, "9121/0",
                PermissibleValue(text="9121/0") )
        setattr(cls, "8508/3",
                PermissibleValue(text="8508/3") )
        setattr(cls, "8150/3",
                PermissibleValue(text="8150/3") )
        setattr(cls, "9142/0",
                PermissibleValue(text="9142/0") )
        setattr(cls, "9170/3",
                PermissibleValue(text="9170/3") )
        setattr(cls, "8743/3",
                PermissibleValue(text="8743/3") )
        setattr(cls, "9394/1",
                PermissibleValue(text="9394/1") )
        setattr(cls, "8450/3",
                PermissibleValue(text="8450/3") )
        setattr(cls, "8280/3",
                PermissibleValue(text="8280/3") )
        setattr(cls, "8097/3",
                PermissibleValue(text="8097/3") )
        setattr(cls, "8861/0",
                PermissibleValue(text="8861/0") )
        setattr(cls, "9751/1",
                PermissibleValue(text="9751/1") )
        setattr(cls, "8430/1",
                PermissibleValue(text="8430/1") )
        setattr(cls, "9708/3",
                PermissibleValue(text="9708/3") )
        setattr(cls, "9570/0",
                PermissibleValue(text="9570/0") )
        setattr(cls, "8966/0",
                PermissibleValue(text="8966/0") )
        setattr(cls, "8052/3",
                PermissibleValue(text="8052/3") )
        setattr(cls, "9065/3",
                PermissibleValue(text="9065/3") )
        setattr(cls, "8720/3",
                PermissibleValue(text="8720/3") )
        setattr(cls, "9531/0",
                PermissibleValue(text="9531/0") )
        setattr(cls, "8501/2",
                PermissibleValue(text="8501/2") )
        setattr(cls, "9561/3",
                PermissibleValue(text="9561/3") )
        setattr(cls, "8772/0",
                PermissibleValue(text="8772/0") )
        setattr(cls, "8210/3",
                PermissibleValue(text="8210/3") )
        setattr(cls, "9054/0",
                PermissibleValue(text="9054/0") )
        setattr(cls, "8474/1",
                PermissibleValue(text="8474/1") )
        setattr(cls, "8540/3",
                PermissibleValue(text="8540/3") )
        setattr(cls, "9702/3",
                PermissibleValue(text="9702/3") )
        setattr(cls, "8832/0",
                PermissibleValue(text="8832/0") )
        setattr(cls, "9084/3",
                PermissibleValue(text="9084/3") )
        setattr(cls, "8960/1",
                PermissibleValue(text="8960/1") )
        setattr(cls, "8330/3",
                PermissibleValue(text="8330/3") )
        setattr(cls, "8893/0",
                PermissibleValue(text="8893/0") )
        setattr(cls, "9661/3",
                PermissibleValue(text="9661/3") )
        setattr(cls, "9753/1",
                PermissibleValue(text="9753/1") )
        setattr(cls, "9571/3",
                PermissibleValue(text="9571/3") )
        setattr(cls, "8500/2",
                PermissibleValue(text="8500/2") )
        setattr(cls, "8851/3",
                PermissibleValue(text="8851/3") )
        setattr(cls, "8040/1",
                PermissibleValue(text="8040/1") )
        setattr(cls, "8333/0",
                PermissibleValue(text="8333/0") )
        setattr(cls, "8560/3",
                PermissibleValue(text="8560/3") )
        setattr(cls, "8990/0",
                PermissibleValue(text="8990/0") )
        setattr(cls, "9509/1",
                PermissibleValue(text="9509/1") )
        setattr(cls, "8147/3",
                PermissibleValue(text="8147/3") )
        setattr(cls, "8454/0",
                PermissibleValue(text="8454/0") )
        setattr(cls, "9210/1",
                PermissibleValue(text="9210/1") )
        setattr(cls, "8076/2",
                PermissibleValue(text="8076/2") )
        setattr(cls, "9521/3",
                PermissibleValue(text="9521/3") )
        setattr(cls, "8622/1",
                PermissibleValue(text="8622/1") )
        setattr(cls, "8460/2",
                PermissibleValue(text="8460/2") )
        setattr(cls, "9471/3",
                PermissibleValue(text="9471/3") )
        setattr(cls, "8631/0",
                PermissibleValue(text="8631/0") )
        setattr(cls, "8161/3",
                PermissibleValue(text="8161/3") )
        setattr(cls, "8895/0",
                PermissibleValue(text="8895/0") )
        setattr(cls, "9174/0",
                PermissibleValue(text="9174/0") )
        setattr(cls, "9192/3",
                PermissibleValue(text="9192/3") )
        setattr(cls, "9940/3",
                PermissibleValue(text="9940/3") )
        setattr(cls, "9470/3",
                PermissibleValue(text="9470/3") )
        setattr(cls, "8963/3",
                PermissibleValue(text="8963/3") )
        setattr(cls, "8050/2",
                PermissibleValue(text="8050/2") )
        setattr(cls, "8090/1",
                PermissibleValue(text="8090/1") )
        setattr(cls, "8071/3",
                PermissibleValue(text="8071/3") )
        setattr(cls, "8912/3",
                PermissibleValue(text="8912/3") )
        setattr(cls, "8894/3",
                PermissibleValue(text="8894/3") )
        setattr(cls, "8180/3",
                PermissibleValue(text="8180/3") )
        setattr(cls, "9270/0",
                PermissibleValue(text="9270/0") )
        setattr(cls, "8081/2",
                PermissibleValue(text="8081/2") )
        setattr(cls, "9086/3",
                PermissibleValue(text="9086/3") )
        setattr(cls, "8580/1",
                PermissibleValue(text="8580/1") )
        setattr(cls, "9874/3",
                PermissibleValue(text="9874/3") )
        setattr(cls, "9242/3",
                PermissibleValue(text="9242/3") )
        setattr(cls, "8215/3",
                PermissibleValue(text="8215/3") )
        setattr(cls, "8000/3",
                PermissibleValue(text="8000/3") )
        setattr(cls, "8408/0",
                PermissibleValue(text="8408/0") )
        setattr(cls, "8153/1",
                PermissibleValue(text="8153/1") )
        setattr(cls, "9431/1",
                PermissibleValue(text="9431/1") )
        setattr(cls, "8830/0",
                PermissibleValue(text="8830/0") )
        setattr(cls, "9688/3",
                PermissibleValue(text="9688/3") )
        setattr(cls, "9989/3",
                PermissibleValue(text="9989/3") )
        setattr(cls, "9580/0",
                PermissibleValue(text="9580/0") )
        setattr(cls, "9350/1",
                PermissibleValue(text="9350/1") )
        setattr(cls, "9102/3",
                PermissibleValue(text="9102/3") )
        setattr(cls, "8850/1",
                PermissibleValue(text="8850/1") )
        setattr(cls, "9391/3",
                PermissibleValue(text="9391/3") )
        setattr(cls, "8382/3",
                PermissibleValue(text="8382/3") )
        setattr(cls, "9755/3",
                PermissibleValue(text="9755/3") )
        setattr(cls, "8504/3",
                PermissibleValue(text="8504/3") )
        setattr(cls, "8380/3",
                PermissibleValue(text="8380/3") )
        setattr(cls, "9015/0",
                PermissibleValue(text="9015/0") )
        setattr(cls, "8583/3",
                PermissibleValue(text="8583/3") )
        setattr(cls, "8713/0",
                PermissibleValue(text="8713/0") )
        setattr(cls, "8247/3",
                PermissibleValue(text="8247/3") )
        setattr(cls, "8640/3",
                PermissibleValue(text="8640/3") )
        setattr(cls, "9523/3",
                PermissibleValue(text="9523/3") )
        setattr(cls, "9044/3",
                PermissibleValue(text="9044/3") )
        setattr(cls, "8254/3",
                PermissibleValue(text="8254/3") )
        setattr(cls, "9384/1",
                PermissibleValue(text="9384/1") )
        setattr(cls, "8730/0",
                PermissibleValue(text="8730/0") )
        setattr(cls, "9252/0",
                PermissibleValue(text="9252/0") )
        setattr(cls, "8460/0",
                PermissibleValue(text="8460/0") )
        setattr(cls, "8315/3",
                PermissibleValue(text="8315/3") )
        setattr(cls, "9103/0",
                PermissibleValue(text="9103/0") )
        setattr(cls, "8728/3",
                PermissibleValue(text="8728/3") )
        setattr(cls, "8360/1",
                PermissibleValue(text="8360/1") )
        setattr(cls, "8200/3",
                PermissibleValue(text="8200/3") )
        setattr(cls, "8343/2",
                PermissibleValue(text="8343/2") )
        setattr(cls, "8710/3",
                PermissibleValue(text="8710/3") )
        setattr(cls, "8620/1",
                PermissibleValue(text="8620/1") )
        setattr(cls, "8650/1",
                PermissibleValue(text="8650/1") )
        setattr(cls, "8401/3",
                PermissibleValue(text="8401/3") )
        setattr(cls, "9992/3",
                PermissibleValue(text="9992/3") )
        setattr(cls, "8155/3",
                PermissibleValue(text="8155/3") )
        setattr(cls, "9808/3",
                PermissibleValue(text="9808/3") )
        setattr(cls, "9945/3",
                PermissibleValue(text="9945/3") )
        setattr(cls, "9020/1",
                PermissibleValue(text="9020/1") )
        setattr(cls, "9709/3",
                PermissibleValue(text="9709/3") )
        setattr(cls, "9410/3",
                PermissibleValue(text="9410/3") )
        setattr(cls, "8722/0",
                PermissibleValue(text="8722/0") )
        setattr(cls, "8746/3",
                PermissibleValue(text="8746/3") )
        setattr(cls, "9840/3",
                PermissibleValue(text="9840/3") )
        setattr(cls, "8339/3",
                PermissibleValue(text="8339/3") )
        setattr(cls, "9312/0",
                PermissibleValue(text="9312/0") )
        setattr(cls, "9360/1",
                PermissibleValue(text="9360/1") )
        setattr(cls, "8640/1",
                PermissibleValue(text="8640/1") )
        setattr(cls, "8855/3",
                PermissibleValue(text="8855/3") )
        setattr(cls, "8281/0",
                PermissibleValue(text="8281/0") )
        setattr(cls, "8374/0",
                PermissibleValue(text="8374/0") )
        setattr(cls, "8316/3",
                PermissibleValue(text="8316/3") )
        setattr(cls, "8813/0",
                PermissibleValue(text="8813/0") )
        setattr(cls, "8420/0",
                PermissibleValue(text="8420/0") )
        setattr(cls, "8970/3",
                PermissibleValue(text="8970/3") )
        setattr(cls, "9072/3",
                PermissibleValue(text="9072/3") )
        setattr(cls, "8280/0",
                PermissibleValue(text="8280/0") )
        setattr(cls, "9898/3",
                PermissibleValue(text="9898/3") )
        setattr(cls, "8441/0",
                PermissibleValue(text="8441/0") )
        setattr(cls, "8121/3",
                PermissibleValue(text="8121/3") )
        setattr(cls, "9100/3",
                PermissibleValue(text="9100/3") )
        setattr(cls, "9221/0",
                PermissibleValue(text="9221/0") )
        setattr(cls, "9871/3",
                PermissibleValue(text="9871/3") )
        setattr(cls, "8822/1",
                PermissibleValue(text="8822/1") )
        setattr(cls, "9282/0",
                PermissibleValue(text="9282/0") )
        setattr(cls, "8870/0",
                PermissibleValue(text="8870/0") )
        setattr(cls, "9534/0",
                PermissibleValue(text="9534/0") )
        setattr(cls, "8900/0",
                PermissibleValue(text="8900/0") )
        setattr(cls, "9372/3",
                PermissibleValue(text="9372/3") )
        setattr(cls, "9110/3",
                PermissibleValue(text="9110/3") )
        setattr(cls, "8124/3",
                PermissibleValue(text="8124/3") )
        setattr(cls, "8470/0",
                PermissibleValue(text="8470/0") )
        setattr(cls, "9310/0",
                PermissibleValue(text="9310/0") )
        setattr(cls, "9382/3",
                PermissibleValue(text="9382/3") )
        setattr(cls, "8313/0",
                PermissibleValue(text="8313/0") )
        setattr(cls, "8691/1",
                PermissibleValue(text="8691/1") )
        setattr(cls, "9505/1",
                PermissibleValue(text="9505/1") )
        setattr(cls, "9663/3",
                PermissibleValue(text="9663/3") )
        setattr(cls, "8314/3",
                PermissibleValue(text="8314/3") )
        setattr(cls, "9492/0",
                PermissibleValue(text="9492/0") )
        setattr(cls, "9814/3",
                PermissibleValue(text="9814/3") )
        setattr(cls, "9310/3",
                PermissibleValue(text="9310/3") )
        setattr(cls, "8013/3",
                PermissibleValue(text="8013/3") )
        setattr(cls, "9860/3",
                PermissibleValue(text="9860/3") )
        setattr(cls, "8451/1",
                PermissibleValue(text="8451/1") )
        setattr(cls, "8003/3",
                PermissibleValue(text="8003/3") )
        setattr(cls, "9741/3",
                PermissibleValue(text="9741/3") )
        setattr(cls, "9741/1",
                PermissibleValue(text="9741/1") )
        setattr(cls, "8910/3",
                PermissibleValue(text="8910/3") )
        setattr(cls, "9130/3",
                PermissibleValue(text="9130/3") )
        setattr(cls, "8343/3",
                PermissibleValue(text="8343/3") )
        setattr(cls, "8840/0",
                PermissibleValue(text="8840/0") )
        setattr(cls, "8076/3",
                PermissibleValue(text="8076/3") )
        setattr(cls, "8091/3",
                PermissibleValue(text="8091/3") )
        setattr(cls, "9052/3",
                PermissibleValue(text="9052/3") )
        setattr(cls, "9876/3",
                PermissibleValue(text="9876/3") )
        setattr(cls, "9351/1",
                PermissibleValue(text="9351/1") )
        setattr(cls, "8520/2",
                PermissibleValue(text="8520/2") )
        setattr(cls, "8070/3",
                PermissibleValue(text="8070/3") )
        setattr(cls, "8201/3",
                PermissibleValue(text="8201/3") )
        setattr(cls, "8524/3",
                PermissibleValue(text="8524/3") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "9450/3",
                PermissibleValue(text="9450/3") )
        setattr(cls, "8801/3",
                PermissibleValue(text="8801/3") )
        setattr(cls, "8590/1",
                PermissibleValue(text="8590/1") )
        setattr(cls, "8472/1",
                PermissibleValue(text="8472/1") )
        setattr(cls, "8641/0",
                PermissibleValue(text="8641/0") )
        setattr(cls, "9460/3",
                PermissibleValue(text="9460/3") )
        setattr(cls, "8373/0",
                PermissibleValue(text="8373/0") )
        setattr(cls, "8071/2",
                PermissibleValue(text="8071/2") )
        setattr(cls, "8519/2",
                PermissibleValue(text="8519/2") )
        setattr(cls, "8812/0",
                PermissibleValue(text="8812/0") )
        setattr(cls, "9084/0",
                PermissibleValue(text="9084/0") )
        setattr(cls, "9261/3",
                PermissibleValue(text="9261/3") )
        setattr(cls, "9671/3",
                PermissibleValue(text="9671/3") )
        setattr(cls, "9831/3",
                PermissibleValue(text="9831/3") )
        setattr(cls, "8408/3",
                PermissibleValue(text="8408/3") )
        setattr(cls, "8561/0",
                PermissibleValue(text="8561/0") )
        setattr(cls, "8852/0",
                PermissibleValue(text="8852/0") )
        setattr(cls, "9734/3",
                PermissibleValue(text="9734/3") )
        setattr(cls, "9281/0",
                PermissibleValue(text="9281/0") )
        setattr(cls, "8050/3",
                PermissibleValue(text="8050/3") )
        setattr(cls, "8151/3",
                PermissibleValue(text="8151/3") )
        setattr(cls, "9210/0",
                PermissibleValue(text="9210/0") )
        setattr(cls, "8503/3",
                PermissibleValue(text="8503/3") )
        setattr(cls, "8252/3",
                PermissibleValue(text="8252/3") )
        setattr(cls, "8581/1",
                PermissibleValue(text="8581/1") )
        setattr(cls, "8500/3",
                PermissibleValue(text="8500/3") )
        setattr(cls, "8601/0",
                PermissibleValue(text="8601/0") )
        setattr(cls, "8815/3",
                PermissibleValue(text="8815/3") )
        setattr(cls, "8463/1",
                PermissibleValue(text="8463/1") )
        setattr(cls, "9580/3",
                PermissibleValue(text="9580/3") )
        setattr(cls, "8160/0",
                PermissibleValue(text="8160/0") )
        setattr(cls, "8573/3",
                PermissibleValue(text="8573/3") )
        setattr(cls, "8692/1",
                PermissibleValue(text="8692/1") )
        setattr(cls, "8444/1",
                PermissibleValue(text="8444/1") )
        setattr(cls, "8442/1",
                PermissibleValue(text="8442/1") )
        setattr(cls, "8720/0",
                PermissibleValue(text="8720/0") )
        setattr(cls, "8842/0",
                PermissibleValue(text="8842/0") )
        setattr(cls, "9655/3",
                PermissibleValue(text="9655/3") )
        setattr(cls, "8742/3",
                PermissibleValue(text="8742/3") )
        setattr(cls, "8044/3",
                PermissibleValue(text="8044/3") )
        setattr(cls, "9110/0",
                PermissibleValue(text="9110/0") )
        setattr(cls, "8130/3",
                PermissibleValue(text="8130/3") )
        setattr(cls, "8251/0",
                PermissibleValue(text="8251/0") )
        setattr(cls, "8480/6",
                PermissibleValue(text="8480/6") )
        setattr(cls, "8263/2",
                PermissibleValue(text="8263/2") )
        setattr(cls, "8730/3",
                PermissibleValue(text="8730/3") )
        setattr(cls, "9080/1",
                PermissibleValue(text="9080/1") )
        setattr(cls, "9963/3",
                PermissibleValue(text="9963/3") )
        setattr(cls, "8574/3",
                PermissibleValue(text="8574/3") )
        setattr(cls, "9016/0",
                PermissibleValue(text="9016/0") )
        setattr(cls, "9540/3",
                PermissibleValue(text="9540/3") )
        setattr(cls, "8903/0",
                PermissibleValue(text="8903/0") )
        setattr(cls, "8370/0",
                PermissibleValue(text="8370/0") )
        setattr(cls, "9030/0",
                PermissibleValue(text="9030/0") )
        setattr(cls, "9811/3",
                PermissibleValue(text="9811/3") )
        setattr(cls, "8835/1",
                PermissibleValue(text="8835/1") )
        setattr(cls, "8552/3",
                PermissibleValue(text="8552/3") )
        setattr(cls, "9135/1",
                PermissibleValue(text="9135/1") )
        setattr(cls, "9013/0",
                PermissibleValue(text="9013/0") )
        setattr(cls, "8402/0",
                PermissibleValue(text="8402/0") )
        setattr(cls, "9530/0",
                PermissibleValue(text="9530/0") )
        setattr(cls, "8582/1",
                PermissibleValue(text="8582/1") )
        setattr(cls, "9662/3",
                PermissibleValue(text="9662/3") )
        setattr(cls, "8005/3",
                PermissibleValue(text="8005/3") )
        setattr(cls, "8012/3",
                PermissibleValue(text="8012/3") )
        setattr(cls, "8204/0",
                PermissibleValue(text="8204/0") )
        setattr(cls, "8840/3",
                PermissibleValue(text="8840/3") )
        setattr(cls, "8441/2",
                PermissibleValue(text="8441/2") )
        setattr(cls, "8073/3",
                PermissibleValue(text="8073/3") )
        setattr(cls, "9680/3",
                PermissibleValue(text="9680/3") )
        setattr(cls, "8190/0",
                PermissibleValue(text="8190/0") )
        setattr(cls, "9085/3",
                PermissibleValue(text="9085/3") )
        setattr(cls, "9311/0",
                PermissibleValue(text="9311/0") )
        setattr(cls, "8941/3",
                PermissibleValue(text="8941/3") )
        setattr(cls, "8981/3",
                PermissibleValue(text="8981/3") )
        setattr(cls, "8690/1",
                PermissibleValue(text="8690/1") )
        setattr(cls, "9365/3",
                PermissibleValue(text="9365/3") )
        setattr(cls, "8443/0",
                PermissibleValue(text="8443/0") )
        setattr(cls, "9701/3",
                PermissibleValue(text="9701/3") )
        setattr(cls, "8000/6",
                PermissibleValue(text="8000/6") )
        setattr(cls, "8621/1",
                PermissibleValue(text="8621/1") )
        setattr(cls, "8771/3",
                PermissibleValue(text="8771/3") )
        setattr(cls, "9193/3",
                PermissibleValue(text="9193/3") )
        setattr(cls, "8930/3",
                PermissibleValue(text="8930/3") )
        setattr(cls, "8151/0",
                PermissibleValue(text="8151/0") )
        setattr(cls, "8503/2",
                PermissibleValue(text="8503/2") )
        setattr(cls, "9714/3",
                PermissibleValue(text="9714/3") )
        setattr(cls, "9053/3",
                PermissibleValue(text="9053/3") )
        setattr(cls, "8210/0",
                PermissibleValue(text="8210/0") )
        setattr(cls, "8562/3",
                PermissibleValue(text="8562/3") )
        setattr(cls, "8810/3",
                PermissibleValue(text="8810/3") )
        setattr(cls, "9538/3",
                PermissibleValue(text="9538/3") )
        setattr(cls, "8471/3",
                PermissibleValue(text="8471/3") )
        setattr(cls, "8403/0",
                PermissibleValue(text="8403/0") )
        setattr(cls, "9759/3",
                PermissibleValue(text="9759/3") )
        setattr(cls, "9381/3",
                PermissibleValue(text="9381/3") )
        setattr(cls, "9195/3",
                PermissibleValue(text="9195/3") )
        setattr(cls, "8525/3",
                PermissibleValue(text="8525/3") )
        setattr(cls, "9813/3",
                PermissibleValue(text="9813/3") )
        setattr(cls, "9131/0",
                PermissibleValue(text="9131/0") )
        setattr(cls, "8253/3",
                PermissibleValue(text="8253/3") )
        setattr(cls, "8409/0",
                PermissibleValue(text="8409/0") )
        setattr(cls, "9194/3",
                PermissibleValue(text="9194/3") )
        setattr(cls, "8290/0",
                PermissibleValue(text="8290/0") )
        setattr(cls, "8380/2",
                PermissibleValue(text="8380/2") )
        setattr(cls, "8881/0",
                PermissibleValue(text="8881/0") )
        setattr(cls, "8080/2",
                PermissibleValue(text="8080/2") )
        setattr(cls, "9371/3",
                PermissibleValue(text="9371/3") )
        setattr(cls, "9200/0",
                PermissibleValue(text="9200/0") )
        setattr(cls, "9766/1",
                PermissibleValue(text="9766/1") )
        setattr(cls, "9392/3",
                PermissibleValue(text="9392/3") )
        setattr(cls, "8470/3",
                PermissibleValue(text="8470/3") )
        setattr(cls, "9373/0",
                PermissibleValue(text="9373/0") )
        setattr(cls, "8265/3",
                PermissibleValue(text="8265/3") )
        setattr(cls, "8631/1",
                PermissibleValue(text="8631/1") )
        setattr(cls, "8967/0",
                PermissibleValue(text="8967/0") )
        setattr(cls, "8959/3",
                PermissibleValue(text="8959/3") )
        setattr(cls, "8342/3",
                PermissibleValue(text="8342/3") )
        setattr(cls, "9971/3",
                PermissibleValue(text="9971/3") )
        setattr(cls, "8191/0",
                PermissibleValue(text="8191/0") )
        setattr(cls, "8571/3",
                PermissibleValue(text="8571/3") )
        setattr(cls, "9513/3",
                PermissibleValue(text="9513/3") )
        setattr(cls, "8163/3",
                PermissibleValue(text="8163/3") )
        setattr(cls, "9071/3",
                PermissibleValue(text="9071/3") )
        setattr(cls, "9815/3",
                PermissibleValue(text="9815/3") )
        setattr(cls, "9370/3",
                PermissibleValue(text="9370/3") )
        setattr(cls, "9473/3",
                PermissibleValue(text="9473/3") )
        setattr(cls, "8245/1",
                PermissibleValue(text="8245/1") )
        setattr(cls, "8742/2",
                PermissibleValue(text="8742/2") )
        setattr(cls, "9290/3",
                PermissibleValue(text="9290/3") )
        setattr(cls, "8935/1",
                PermissibleValue(text="8935/1") )
        setattr(cls, "9010/0",
                PermissibleValue(text="9010/0") )
        setattr(cls, "9930/3",
                PermissibleValue(text="9930/3") )
        setattr(cls, "8100/0",
                PermissibleValue(text="8100/0") )
        setattr(cls, "9946/3",
                PermissibleValue(text="9946/3") )
        setattr(cls, "8075/3",
                PermissibleValue(text="8075/3") )
        setattr(cls, "8761/0",
                PermissibleValue(text="8761/0") )
        setattr(cls, "8501/3",
                PermissibleValue(text="8501/3") )
        setattr(cls, "8248/1",
                PermissibleValue(text="8248/1") )
        setattr(cls, "8212/0",
                PermissibleValue(text="8212/0") )
        setattr(cls, "8834/1",
                PermissibleValue(text="8834/1") )
        setattr(cls, "8231/3",
                PermissibleValue(text="8231/3") )
        setattr(cls, "9300/0",
                PermissibleValue(text="9300/0") )
        setattr(cls, "9490/0",
                PermissibleValue(text="9490/0") )
        setattr(cls, "8480/0",
                PermissibleValue(text="8480/0") )
        setattr(cls, "8771/0",
                PermissibleValue(text="8771/0") )
        setattr(cls, "8244/3",
                PermissibleValue(text="8244/3") )
        setattr(cls, "9665/3",
                PermissibleValue(text="9665/3") )
        setattr(cls, "8681/1",
                PermissibleValue(text="8681/1") )
        setattr(cls, "8728/0",
                PermissibleValue(text="8728/0") )
        setattr(cls, "8862/0",
                PermissibleValue(text="8862/0") )
        setattr(cls, "8480/1",
                PermissibleValue(text="8480/1") )
        setattr(cls, "9817/3",
                PermissibleValue(text="9817/3") )
        setattr(cls, "8720/2",
                PermissibleValue(text="8720/2") )
        setattr(cls, "9052/0",
                PermissibleValue(text="9052/0") )
        setattr(cls, "8820/0",
                PermissibleValue(text="8820/0") )
        setattr(cls, "9000/0",
                PermissibleValue(text="9000/0") )
        setattr(cls, "9970/1",
                PermissibleValue(text="9970/1") )
        setattr(cls, "8383/3",
                PermissibleValue(text="8383/3") )
        setattr(cls, "9061/3",
                PermissibleValue(text="9061/3") )
        setattr(cls, "8850/3",
                PermissibleValue(text="8850/3") )
        setattr(cls, "8010/9",
                PermissibleValue(text="8010/9") )
        setattr(cls, "8505/0",
                PermissibleValue(text="8505/0") )
        setattr(cls, "8721/3",
                PermissibleValue(text="8721/3") )
        setattr(cls, "9400/3",
                PermissibleValue(text="9400/3") )
        setattr(cls, "8084/3",
                PermissibleValue(text="8084/3") )
        setattr(cls, "9698/3",
                PermissibleValue(text="9698/3") )
        setattr(cls, "8005/0",
                PermissibleValue(text="8005/0") )
        setattr(cls, "9181/3",
                PermissibleValue(text="9181/3") )
        setattr(cls, "8521/1",
                PermissibleValue(text="8521/1") )
        setattr(cls, "9911/3",
                PermissibleValue(text="9911/3") )
        setattr(cls, "8830/1",
                PermissibleValue(text="8830/1") )
        setattr(cls, "8522/3",
                PermissibleValue(text="8522/3") )
        setattr(cls, "8261/2",
                PermissibleValue(text="8261/2") )
        setattr(cls, "8145/3",
                PermissibleValue(text="8145/3") )
        setattr(cls, "8959/1",
                PermissibleValue(text="8959/1") )
        setattr(cls, "9474/3",
                PermissibleValue(text="9474/3") )
        setattr(cls, "8361/0",
                PermissibleValue(text="8361/0") )
        setattr(cls, "8290/3",
                PermissibleValue(text="8290/3") )
        setattr(cls, "8521/3",
                PermissibleValue(text="8521/3") )
        setattr(cls, "8272/0",
                PermissibleValue(text="8272/0") )
        setattr(cls, "8503/0",
                PermissibleValue(text="8503/0") )
        setattr(cls, "9695/3",
                PermissibleValue(text="9695/3") )
        setattr(cls, "8094/3",
                PermissibleValue(text="8094/3") )
        setattr(cls, "8482/3",
                PermissibleValue(text="8482/3") )
        setattr(cls, "9342/3",
                PermissibleValue(text="9342/3") )
        setattr(cls, "8935/0",
                PermissibleValue(text="8935/0") )
        setattr(cls, "8821/1",
                PermissibleValue(text="8821/1") )
        setattr(cls, "9174/1",
                PermissibleValue(text="9174/1") )
        setattr(cls, "9270/3",
                PermissibleValue(text="9270/3") )
        setattr(cls, "8093/3",
                PermissibleValue(text="8093/3") )
        setattr(cls, "9835/3",
                PermissibleValue(text="9835/3") )
        setattr(cls, "8120/3",
                PermissibleValue(text="8120/3") )
        setattr(cls, "9133/1",
                PermissibleValue(text="9133/1") )
        setattr(cls, "9432/1",
                PermissibleValue(text="9432/1") )
        setattr(cls, "8514/3",
                PermissibleValue(text="8514/3") )
        setattr(cls, "9185/3",
                PermissibleValue(text="9185/3") )
        setattr(cls, "9362/3",
                PermissibleValue(text="9362/3") )
        setattr(cls, "9136/1",
                PermissibleValue(text="9136/1") )
        setattr(cls, "9863/3",
                PermissibleValue(text="9863/3") )
        setattr(cls, "8831/0",
                PermissibleValue(text="8831/0") )
        setattr(cls, "8011/3",
                PermissibleValue(text="8011/3") )
        setattr(cls, "8583/1",
                PermissibleValue(text="8583/1") )
        setattr(cls, "9412/1",
                PermissibleValue(text="9412/1") )
        setattr(cls, "9767/1",
                PermissibleValue(text="9767/1") )
        setattr(cls, "9080/3",
                PermissibleValue(text="9080/3") )
        setattr(cls, "8806/3",
                PermissibleValue(text="8806/3") )
        setattr(cls, "8022/3",
                PermissibleValue(text="8022/3") )
        setattr(cls, "8513/3",
                PermissibleValue(text="8513/3") )
        setattr(cls, "8156/1",
                PermissibleValue(text="8156/1") )
        setattr(cls, "8504/2",
                PermissibleValue(text="8504/2") )
        setattr(cls, "8507/3",
                PermissibleValue(text="8507/3") )
        setattr(cls, "9732/3",
                PermissibleValue(text="9732/3") )
        setattr(cls, "8700/3",
                PermissibleValue(text="8700/3") )
        setattr(cls, "8140/2",
                PermissibleValue(text="8140/2") )
        setattr(cls, "8990/1",
                PermissibleValue(text="8990/1") )
        setattr(cls, "8146/0",
                PermissibleValue(text="8146/0") )
        setattr(cls, "8060/0",
                PermissibleValue(text="8060/0") )
        setattr(cls, "8096/0",
                PermissibleValue(text="8096/0") )
        setattr(cls, "9014/0",
                PermissibleValue(text="9014/0") )
        setattr(cls, "8095/3",
                PermissibleValue(text="8095/3") )
        setattr(cls, "9541/0",
                PermissibleValue(text="9541/0") )
        setattr(cls, "8083/3",
                PermissibleValue(text="8083/3") )
        setattr(cls, "8263/0",
                PermissibleValue(text="8263/0") )
        setattr(cls, "9451/3",
                PermissibleValue(text="9451/3") )
        setattr(cls, "8936/1",
                PermissibleValue(text="8936/1") )
        setattr(cls, "8800/3",
                PermissibleValue(text="8800/3") )
        setattr(cls, "8158/1",
                PermissibleValue(text="8158/1") )
        setattr(cls, "8174/3",
                PermissibleValue(text="8174/3") )
        setattr(cls, "9719/3",
                PermissibleValue(text="9719/3") )
        setattr(cls, "9718/3",
                PermissibleValue(text="9718/3") )
        setattr(cls, "8318/3",
                PermissibleValue(text="8318/3") )
        setattr(cls, "8711/3",
                PermissibleValue(text="8711/3") )
        setattr(cls, "9733/3",
                PermissibleValue(text="9733/3") )
        setattr(cls, "9866/3",
                PermissibleValue(text="9866/3") )
        setattr(cls, "8683/0",
                PermissibleValue(text="8683/0") )
        setattr(cls, "9083/3",
                PermissibleValue(text="9083/3") )
        setattr(cls, "9986/3",
                PermissibleValue(text="9986/3") )
        setattr(cls, "8272/3",
                PermissibleValue(text="8272/3") )
        setattr(cls, "8271/0",
                PermissibleValue(text="8271/0") )
        setattr(cls, "9571/0",
                PermissibleValue(text="9571/0") )
        setattr(cls, "8241/3",
                PermissibleValue(text="8241/3") )
        setattr(cls, "8391/0",
                PermissibleValue(text="8391/0") )
        setattr(cls, "8035/3",
                PermissibleValue(text="8035/3") )
        setattr(cls, "8857/0",
                PermissibleValue(text="8857/0") )
        setattr(cls, "9500/3",
                PermissibleValue(text="9500/3") )
        setattr(cls, "8154/3",
                PermissibleValue(text="8154/3") )
        setattr(cls, "8170/3",
                PermissibleValue(text="8170/3") )
        setattr(cls, "9596/3",
                PermissibleValue(text="9596/3") )
        setattr(cls, "9961/3",
                PermissibleValue(text="9961/3") )
        setattr(cls, "9302/0",
                PermissibleValue(text="9302/0") )
        setattr(cls, "8593/1",
                PermissibleValue(text="8593/1") )
        setattr(cls, "8633/1",
                PermissibleValue(text="8633/1") )
        setattr(cls, "9250/3",
                PermissibleValue(text="9250/3") )
        setattr(cls, "9826/3",
                PermissibleValue(text="9826/3") )
        setattr(cls, "8841/1",
                PermissibleValue(text="8841/1") )
        setattr(cls, "8213/3",
                PermissibleValue(text="8213/3") )
        setattr(cls, "8331/3",
                PermissibleValue(text="8331/3") )
        setattr(cls, "8150/0",
                PermissibleValue(text="8150/0") )
        setattr(cls, "8481/3",
                PermissibleValue(text="8481/3") )
        setattr(cls, "8591/1",
                PermissibleValue(text="8591/1") )
        setattr(cls, "8973/3",
                PermissibleValue(text="8973/3") )
        setattr(cls, "8407/0",
                PermissibleValue(text="8407/0") )
        setattr(cls, "8161/0",
                PermissibleValue(text="8161/0") )
        setattr(cls, "8712/0",
                PermissibleValue(text="8712/0") )
        setattr(cls, "8142/3",
                PermissibleValue(text="8142/3") )
        setattr(cls, "9175/0",
                PermissibleValue(text="9175/0") )
        setattr(cls, "8321/0",
                PermissibleValue(text="8321/0") )
        setattr(cls, "8790/0",
                PermissibleValue(text="8790/0") )
        setattr(cls, "9442/3",
                PermissibleValue(text="9442/3") )
        setattr(cls, "8400/3",
                PermissibleValue(text="8400/3") )
        setattr(cls, "9330/3",
                PermissibleValue(text="9330/3") )
        setattr(cls, "9221/3",
                PermissibleValue(text="9221/3") )
        setattr(cls, "8810/0",
                PermissibleValue(text="8810/0") )
        setattr(cls, "8570/3",
                PermissibleValue(text="8570/3") )
        setattr(cls, "8015/3",
                PermissibleValue(text="8015/3") )
        setattr(cls, "8021/3",
                PermissibleValue(text="8021/3") )
        setattr(cls, "8170/0",
                PermissibleValue(text="8170/0") )
        setattr(cls, "9550/0",
                PermissibleValue(text="9550/0") )
        setattr(cls, "8762/1",
                PermissibleValue(text="8762/1") )
        setattr(cls, "8317/3",
                PermissibleValue(text="8317/3") )
        setattr(cls, "8920/3",
                PermissibleValue(text="8920/3") )
        setattr(cls, "8898/1",
                PermissibleValue(text="8898/1") )
        setattr(cls, "8148/0",
                PermissibleValue(text="8148/0") )
        setattr(cls, "8085/3",
                PermissibleValue(text="8085/3") )
        setattr(cls, "9104/1",
                PermissibleValue(text="9104/1") )
        setattr(cls, "8833/3",
                PermissibleValue(text="8833/3") )
        setattr(cls, "8842/3",
                PermissibleValue(text="8842/3") )
        setattr(cls, "8261/0",
                PermissibleValue(text="8261/0") )
        setattr(cls, "9726/3",
                PermissibleValue(text="9726/3") )
        setattr(cls, "9385/3",
                PermissibleValue(text="9385/3") )
        setattr(cls, "9423/3",
                PermissibleValue(text="9423/3") )
        setattr(cls, "9271/0",
                PermissibleValue(text="9271/0") )
        setattr(cls, "8077/2",
                PermissibleValue(text="8077/2") )
        setattr(cls, "8551/3",
                PermissibleValue(text="8551/3") )
        setattr(cls, "9200/1",
                PermissibleValue(text="9200/1") )
        setattr(cls, "9186/3",
                PermissibleValue(text="9186/3") )
        setattr(cls, "8110/3",
                PermissibleValue(text="8110/3") )
        setattr(cls, "9000/3",
                PermissibleValue(text="9000/3") )
        setattr(cls, "8670/0",
                PermissibleValue(text="8670/0") )
        setattr(cls, "8744/3",
                PermissibleValue(text="8744/3") )
        setattr(cls, "8858/3",
                PermissibleValue(text="8858/3") )
        setattr(cls, "8680/1",
                PermissibleValue(text="8680/1") )
        setattr(cls, "8934/3",
                PermissibleValue(text="8934/3") )
        setattr(cls, "8541/3",
                PermissibleValue(text="8541/3") )
        setattr(cls, "8201/2",
                PermissibleValue(text="8201/2") )
        setattr(cls, "8010/6",
                PermissibleValue(text="8010/6") )
        setattr(cls, "9699/3",
                PermissibleValue(text="9699/3") )
        setattr(cls, "8380/0",
                PermissibleValue(text="8380/0") )
        setattr(cls, "9650/3",
                PermissibleValue(text="9650/3") )
        setattr(cls, "8959/0",
                PermissibleValue(text="8959/0") )
        setattr(cls, "8121/1",
                PermissibleValue(text="8121/1") )
        setattr(cls, "8854/0",
                PermissibleValue(text="8854/0") )
        setattr(cls, "9590/3",
                PermissibleValue(text="9590/3") )
        setattr(cls, "9395/3",
                PermissibleValue(text="9395/3") )
        setattr(cls, "9705/3",
                PermissibleValue(text="9705/3") )
        setattr(cls, "8461/3",
                PermissibleValue(text="8461/3") )
        setattr(cls, "9690/3",
                PermissibleValue(text="9690/3") )
        setattr(cls, "8623/1",
                PermissibleValue(text="8623/1") )
        setattr(cls, "8461/0",
                PermissibleValue(text="8461/0") )
        setattr(cls, "8725/0",
                PermissibleValue(text="8725/0") )
        setattr(cls, "8543/3",
                PermissibleValue(text="8543/3") )
        setattr(cls, "9678/3",
                PermissibleValue(text="9678/3") )
        setattr(cls, "8890/3",
                PermissibleValue(text="8890/3") )
        setattr(cls, "9477/3",
                PermissibleValue(text="9477/3") )
        setattr(cls, "9542/3",
                PermissibleValue(text="9542/3") )
        setattr(cls, "8815/0",
                PermissibleValue(text="8815/0") )
        setattr(cls, "9011/0",
                PermissibleValue(text="9011/0") )
        setattr(cls, "8772/3",
                PermissibleValue(text="8772/3") )
        setattr(cls, "8010/3",
                PermissibleValue(text="8010/3") )
        setattr(cls, "8090/3",
                PermissibleValue(text="8090/3") )
        setattr(cls, "8932/0",
                PermissibleValue(text="8932/0") )
        setattr(cls, "9503/3",
                PermissibleValue(text="9503/3") )
        setattr(cls, "8001/3",
                PermissibleValue(text="8001/3") )
        setattr(cls, "9591/3",
                PermissibleValue(text="9591/3") )
        setattr(cls, "8250/1",
                PermissibleValue(text="8250/1") )
        setattr(cls, "8245/3",
                PermissibleValue(text="8245/3") )
        setattr(cls, "8860/0",
                PermissibleValue(text="8860/0") )
        setattr(cls, "8000/0",
                PermissibleValue(text="8000/0") )
        setattr(cls, "8190/3",
                PermissibleValue(text="8190/3") )
        setattr(cls, "9673/3",
                PermissibleValue(text="9673/3") )
        setattr(cls, "8980/3",
                PermissibleValue(text="8980/3") )
        setattr(cls, "8375/0",
                PermissibleValue(text="8375/0") )
        setattr(cls, "9040/0",
                PermissibleValue(text="9040/0") )
        setattr(cls, "9000/1",
                PermissibleValue(text="9000/1") )
        setattr(cls, "8140/1",
                PermissibleValue(text="8140/1") )
        setattr(cls, "9124/3",
                PermissibleValue(text="9124/3") )
        setattr(cls, "8770/0",
                PermissibleValue(text="8770/0") )
        setattr(cls, "8310/0",
                PermissibleValue(text="8310/0") )
        setattr(cls, "8384/3",
                PermissibleValue(text="8384/3") )
        setattr(cls, "8390/3",
                PermissibleValue(text="8390/3") )
        setattr(cls, "9490/3",
                PermissibleValue(text="9490/3") )
        setattr(cls, "8901/3",
                PermissibleValue(text="8901/3") )
        setattr(cls, "8313/3",
                PermissibleValue(text="8313/3") )
        setattr(cls, "8410/3",
                PermissibleValue(text="8410/3") )
        setattr(cls, "8741/3",
                PermissibleValue(text="8741/3") )
        setattr(cls, "8452/3",
                PermissibleValue(text="8452/3") )
        setattr(cls, "9501/3",
                PermissibleValue(text="9501/3") )
        setattr(cls, "8462/1",
                PermissibleValue(text="8462/1") )
        setattr(cls, "8610/0",
                PermissibleValue(text="8610/0") )
        setattr(cls, "9522/3",
                PermissibleValue(text="9522/3") )
        setattr(cls, "8761/1",
                PermissibleValue(text="8761/1") )
        setattr(cls, "8825/0",
                PermissibleValue(text="8825/0") )
        setattr(cls, "8827/1",
                PermissibleValue(text="8827/1") )
        setattr(cls, "8221/3",
                PermissibleValue(text="8221/3") )
        setattr(cls, "8404/0",
                PermissibleValue(text="8404/0") )
        setattr(cls, "8077/0",
                PermissibleValue(text="8077/0") )
        setattr(cls, "9716/3",
                PermissibleValue(text="9716/3") )
        setattr(cls, "9063/3",
                PermissibleValue(text="9063/3") )
        setattr(cls, "9801/3",
                PermissibleValue(text="9801/3") )
        setattr(cls, "8070/33",
                PermissibleValue(text="8070/33") )
        setattr(cls, "9511/3",
                PermissibleValue(text="9511/3") )
        setattr(cls, "8372/0",
                PermissibleValue(text="8372/0") )
        setattr(cls, "9290/0",
                PermissibleValue(text="9290/0") )
        setattr(cls, "9055/0",
                PermissibleValue(text="9055/0") )
        setattr(cls, "9280/0",
                PermissibleValue(text="9280/0") )
        setattr(cls, "8370/1",
                PermissibleValue(text="8370/1") )
        setattr(cls, "8140/0",
                PermissibleValue(text="8140/0") )
        setattr(cls, "8020/3",
                PermissibleValue(text="8020/3") )
        setattr(cls, "9320/0",
                PermissibleValue(text="9320/0") )
        setattr(cls, "9806/3",
                PermissibleValue(text="9806/3") )
        setattr(cls, "8310/3",
                PermissibleValue(text="8310/3") )
        setattr(cls, "8770/3",
                PermissibleValue(text="8770/3") )
        setattr(cls, "9948/3",
                PermissibleValue(text="9948/3") )
        setattr(cls, "9867/3",
                PermissibleValue(text="9867/3") )
        setattr(cls, "9582/0",
                PermissibleValue(text="9582/0") )
        setattr(cls, "8040/0",
                PermissibleValue(text="8040/0") )
        setattr(cls, "8155/1",
                PermissibleValue(text="8155/1") )
        setattr(cls, "8311/3",
                PermissibleValue(text="8311/3") )
        setattr(cls, "8810/1",
                PermissibleValue(text="8810/1") )
        setattr(cls, "8602/0",
                PermissibleValue(text="8602/0") )
        setattr(cls, "8000/9",
                PermissibleValue(text="8000/9") )
        setattr(cls, "9070/3",
                PermissibleValue(text="9070/3") )
        setattr(cls, "8330/0",
                PermissibleValue(text="8330/0") )
        setattr(cls, "9873/3",
                PermissibleValue(text="9873/3") )
        setattr(cls, "8900/3",
                PermissibleValue(text="8900/3") )
        setattr(cls, "9507/0",
                PermissibleValue(text="9507/0") )
        setattr(cls, "8086/3",
                PermissibleValue(text="8086/3") )
        setattr(cls, "8162/3",
                PermissibleValue(text="8162/3") )
        setattr(cls, "8381/1",
                PermissibleValue(text="8381/1") )
        setattr(cls, "9653/3",
                PermissibleValue(text="9653/3") )
        setattr(cls, "9537/0",
                PermissibleValue(text="9537/0") )
        setattr(cls, "9727/3",
                PermissibleValue(text="9727/3") )
        setattr(cls, "9040/3",
                PermissibleValue(text="9040/3") )
        setattr(cls, "9514/1",
                PermissibleValue(text="9514/1") )
        setattr(cls, "9230/0",
                PermissibleValue(text="9230/0") )
        setattr(cls, "8092/3",
                PermissibleValue(text="8092/3") )
        setattr(cls, "9768/1",
                PermissibleValue(text="9768/1") )
        setattr(cls, "8242/3",
                PermissibleValue(text="8242/3") )
        setattr(cls, "9440/3",
                PermissibleValue(text="9440/3") )
        setattr(cls, "8032/3",
                PermissibleValue(text="8032/3") )
        setattr(cls, "8506/0",
                PermissibleValue(text="8506/0") )
        setattr(cls, "9532/0",
                PermissibleValue(text="9532/0") )
        setattr(cls, "8581/3",
                PermissibleValue(text="8581/3") )
        setattr(cls, "9493/0",
                PermissibleValue(text="9493/0") )
        setattr(cls, "9983/3",
                PermissibleValue(text="9983/3") )
        setattr(cls, "9712/3",
                PermissibleValue(text="9712/3") )
        setattr(cls, "8121/0",
                PermissibleValue(text="8121/0") )
        setattr(cls, "8200/0",
                PermissibleValue(text="8200/0") )
        setattr(cls, "9816/3",
                PermissibleValue(text="9816/3") )
        setattr(cls, "8381/3",
                PermissibleValue(text="8381/3") )
        setattr(cls, "8851/0",
                PermissibleValue(text="8851/0") )
        setattr(cls, "8441/3",
                PermissibleValue(text="8441/3") )
        setattr(cls, "9020/0",
                PermissibleValue(text="9020/0") )
        setattr(cls, "9833/3",
                PermissibleValue(text="9833/3") )
        setattr(cls, "8600/3",
                PermissibleValue(text="8600/3") )
        setattr(cls, "8103/0",
                PermissibleValue(text="8103/0") )
        setattr(cls, "8122/3",
                PermissibleValue(text="8122/3") )
        setattr(cls, "8453/2",
                PermissibleValue(text="8453/2") )
        setattr(cls, "8337/3",
                PermissibleValue(text="8337/3") )
        setattr(cls, "9865/3",
                PermissibleValue(text="9865/3") )
        setattr(cls, "9475/3",
                PermissibleValue(text="9475/3") )
        setattr(cls, "8098/3",
                PermissibleValue(text="8098/3") )
        setattr(cls, "8480/3",
                PermissibleValue(text="8480/3") )
        setattr(cls, "8140/3",
                PermissibleValue(text="8140/3") )
        setattr(cls, "8264/0",
                PermissibleValue(text="8264/0") )
        setattr(cls, "9581/3",
                PermissibleValue(text="9581/3") )
        setattr(cls, "9751/3",
                PermissibleValue(text="9751/3") )
        setattr(cls, "9341/3",
                PermissibleValue(text="9341/3") )
        setattr(cls, "8890/1",
                PermissibleValue(text="8890/1") )
        setattr(cls, "8078/3",
                PermissibleValue(text="8078/3") )
        setattr(cls, "8440/3",
                PermissibleValue(text="8440/3") )
        setattr(cls, "8281/3",
                PermissibleValue(text="8281/3") )
        setattr(cls, "8490/3",
                PermissibleValue(text="8490/3") )
        setattr(cls, "8904/0",
                PermissibleValue(text="8904/0") )
        setattr(cls, "9869/3",
                PermissibleValue(text="9869/3") )
        setattr(cls, "9820/3",
                PermissibleValue(text="9820/3") )
        setattr(cls, "9220/1",
                PermissibleValue(text="9220/1") )
        setattr(cls, "8830/3",
                PermissibleValue(text="8830/3") )
        setattr(cls, "9252/3",
                PermissibleValue(text="9252/3") )
        setattr(cls, "8210/2",
                PermissibleValue(text="8210/2") )
        setattr(cls, "8002/3",
                PermissibleValue(text="8002/3") )
        setattr(cls, "8634/1",
                PermissibleValue(text="8634/1") )
        setattr(cls, "9425/3",
                PermissibleValue(text="9425/3") )
        setattr(cls, "9120/0",
                PermissibleValue(text="9120/0") )
        setattr(cls, "9980/3",
                PermissibleValue(text="9980/3") )
        setattr(cls, "8300/0",
                PermissibleValue(text="8300/0") )
        setattr(cls, "8774/3",
                PermissibleValue(text="8774/3") )
        setattr(cls, "8045/3",
                PermissibleValue(text="8045/3") )
        setattr(cls, "8001/0",
                PermissibleValue(text="8001/0") )
        setattr(cls, "9051/3",
                PermissibleValue(text="9051/3") )
        setattr(cls, "9180/0",
                PermissibleValue(text="9180/0") )
        setattr(cls, "8983/3",
                PermissibleValue(text="8983/3") )
        setattr(cls, "9987/3",
                PermissibleValue(text="9987/3") )
        setattr(cls, "8052/0",
                PermissibleValue(text="8052/0") )
        setattr(cls, "9670/3",
                PermissibleValue(text="9670/3") )
        setattr(cls, "8330/1",
                PermissibleValue(text="8330/1") )
        setattr(cls, "8815/1",
                PermissibleValue(text="8815/1") )
        setattr(cls, "8824/1",
                PermissibleValue(text="8824/1") )
        setattr(cls, "9272/0",
                PermissibleValue(text="9272/0") )
        setattr(cls, "8940/3",
                PermissibleValue(text="8940/3") )
        setattr(cls, "8630/1",
                PermissibleValue(text="8630/1") )
        setattr(cls, "9390/0",
                PermissibleValue(text="9390/0") )
        setattr(cls, "9184/3",
                PermissibleValue(text="9184/3") )
        setattr(cls, "8594/1",
                PermissibleValue(text="8594/1") )
        setattr(cls, "8052/2",
                PermissibleValue(text="8052/2") )
        setattr(cls, "8982/0",
                PermissibleValue(text="8982/0") )
        setattr(cls, "9043/3",
                PermissibleValue(text="9043/3") )
        setattr(cls, "9966/3",
                PermissibleValue(text="9966/3") )
        setattr(cls, "9735/3",
                PermissibleValue(text="9735/3") )
        setattr(cls, "9101/3",
                PermissibleValue(text="9101/3") )
        setattr(cls, "9041/3",
                PermissibleValue(text="9041/3") )
        setattr(cls, "9896/3",
                PermissibleValue(text="9896/3") )
        setattr(cls, "9015/1",
                PermissibleValue(text="9015/1") )
        setattr(cls, "8102/3",
                PermissibleValue(text="8102/3") )
        setattr(cls, "9834/3",
                PermissibleValue(text="9834/3") )
        setattr(cls, "9837/3",
                PermissibleValue(text="9837/3") )
        setattr(cls, "8171/3",
                PermissibleValue(text="8171/3") )
        setattr(cls, "8082/3",
                PermissibleValue(text="8082/3") )
        setattr(cls, "8727/0",
                PermissibleValue(text="8727/0") )
        setattr(cls, "8014/3",
                PermissibleValue(text="8014/3") )
        setattr(cls, "9985/3",
                PermissibleValue(text="9985/3") )
        setattr(cls, "9424/3",
                PermissibleValue(text="9424/3") )
        setattr(cls, "9962/3",
                PermissibleValue(text="9962/3") )
        setattr(cls, "8680/3",
                PermissibleValue(text="8680/3") )
        setattr(cls, "9480/3",
                PermissibleValue(text="9480/3") )
        setattr(cls, "8826/0",
                PermissibleValue(text="8826/0") )
        setattr(cls, "8490/6",
                PermissibleValue(text="8490/6") )
        setattr(cls, "8163/2",
                PermissibleValue(text="8163/2") )
        setattr(cls, "9740/1",
                PermissibleValue(text="9740/1") )
        setattr(cls, "8853/3",
                PermissibleValue(text="8853/3") )
        setattr(cls, "9950/3",
                PermissibleValue(text="9950/3") )
        setattr(cls, "8345/3",
                PermissibleValue(text="8345/3") )
        setattr(cls, "8823/0",
                PermissibleValue(text="8823/0") )
        setattr(cls, "8010/0",
                PermissibleValue(text="8010/0") )
        setattr(cls, "9758/3",
                PermissibleValue(text="9758/3") )
        setattr(cls, "9050/3",
                PermissibleValue(text="9050/3") )
        setattr(cls, "8504/0",
                PermissibleValue(text="8504/0") )
        setattr(cls, "9322/0",
                PermissibleValue(text="9322/0") )
        setattr(cls, "9012/0",
                PermissibleValue(text="9012/0") )
        setattr(cls, "8380/1",
                PermissibleValue(text="8380/1") )
        setattr(cls, "8586/3",
                PermissibleValue(text="8586/3") )
        setattr(cls, "8148/2",
                PermissibleValue(text="8148/2") )
        setattr(cls, "8890/0",
                PermissibleValue(text="8890/0") )
        setattr(cls, "8033/3",
                PermissibleValue(text="8033/3") )
        setattr(cls, "8163/0",
                PermissibleValue(text="8163/0") )
        setattr(cls, "8311/1",
                PermissibleValue(text="8311/1") )
        setattr(cls, "8530/3",
                PermissibleValue(text="8530/3") )
        setattr(cls, "8745/3",
                PermissibleValue(text="8745/3") )
        setattr(cls, "8312/3",
                PermissibleValue(text="8312/3") )
        setattr(cls, "8510/3",
                PermissibleValue(text="8510/3") )
        setattr(cls, "8740/0",
                PermissibleValue(text="8740/0") )
        setattr(cls, "9363/0",
                PermissibleValue(text="9363/0") )
        setattr(cls, "8972/3",
                PermissibleValue(text="8972/3") )
        setattr(cls, "9270/1",
                PermissibleValue(text="9270/1") )
        setattr(cls, "8814/3",
                PermissibleValue(text="8814/3") )
        setattr(cls, "8150/1",
                PermissibleValue(text="8150/1") )
        setattr(cls, "9982/3",
                PermissibleValue(text="9982/3") )
        setattr(cls, "8470/2",
                PermissibleValue(text="8470/2") )
        setattr(cls, "8370/3",
                PermissibleValue(text="8370/3") )
        setattr(cls, "8896/3",
                PermissibleValue(text="8896/3") )
        setattr(cls, "8642/1",
                PermissibleValue(text="8642/1") )
        setattr(cls, "8895/3",
                PermissibleValue(text="8895/3") )
        setattr(cls, "8072/3",
                PermissibleValue(text="8072/3") )
        setattr(cls, "8270/0",
                PermissibleValue(text="8270/0") )
        setattr(cls, "9960/3",
                PermissibleValue(text="9960/3") )
        setattr(cls, "9836/3",
                PermissibleValue(text="9836/3") )
        setattr(cls, "8650/0",
                PermissibleValue(text="8650/0") )
        setattr(cls, "8585/1",
                PermissibleValue(text="8585/1") )
        setattr(cls, "8392/0",
                PermissibleValue(text="8392/0") )
        setattr(cls, "8240/3",
                PermissibleValue(text="8240/3") )
        setattr(cls, "8450/0",
                PermissibleValue(text="8450/0") )
        setattr(cls, "9807/3",
                PermissibleValue(text="9807/3") )
        setattr(cls, "9014/1",
                PermissibleValue(text="9014/1") )
        setattr(cls, "8933/3",
                PermissibleValue(text="8933/3") )
        setattr(cls, "9220/3",
                PermissibleValue(text="9220/3") )
        setattr(cls, "9051/0",
                PermissibleValue(text="9051/0") )
        setattr(cls, "9014/3",
                PermissibleValue(text="9014/3") )
        setattr(cls, "9823/3",
                PermissibleValue(text="9823/3") )
        setattr(cls, "9651/3",
                PermissibleValue(text="9651/3") )
        setattr(cls, "8473/1",
                PermissibleValue(text="8473/1") )
        setattr(cls, "9875/3",
                PermissibleValue(text="9875/3") )
        setattr(cls, "9220/0",
                PermissibleValue(text="9220/0") )
        setattr(cls, "8070/2",
                PermissibleValue(text="8070/2") )
        setattr(cls, "9891/3",
                PermissibleValue(text="9891/3") )
        setattr(cls, "8588/3",
                PermissibleValue(text="8588/3") )
        setattr(cls, "9731/3",
                PermissibleValue(text="9731/3") )
        setattr(cls, "9091/1",
                PermissibleValue(text="9091/1") )
        setattr(cls, "9832/3",
                PermissibleValue(text="9832/3") )
        setattr(cls, "9383/1",
                PermissibleValue(text="9383/1") )
        setattr(cls, "8854/3",
                PermissibleValue(text="8854/3") )
        setattr(cls, "9055/1",
                PermissibleValue(text="9055/1") )
        setattr(cls, "9508/3",
                PermissibleValue(text="9508/3") )
        setattr(cls, "9273/0",
                PermissibleValue(text="9273/0") )
        setattr(cls, "8800/9",
                PermissibleValue(text="8800/9") )
        setattr(cls, "8400/1",
                PermissibleValue(text="8400/1") )
        setattr(cls, "9737/3",
                PermissibleValue(text="9737/3") )
        setattr(cls, "8856/0",
                PermissibleValue(text="8856/0") )
        setattr(cls, "8582/3",
                PermissibleValue(text="8582/3") )
        setattr(cls, "8102/0",
                PermissibleValue(text="8102/0") )
        setattr(cls, "8575/3",
                PermissibleValue(text="8575/3") )
        setattr(cls, "9090/3",
                PermissibleValue(text="9090/3") )
        setattr(cls, "8211/0",
                PermissibleValue(text="8211/0") )
        setattr(cls, "9965/3",
                PermissibleValue(text="9965/3") )
        setattr(cls, "8728/1",
                PermissibleValue(text="8728/1") )
        setattr(cls, "9818/3",
                PermissibleValue(text="9818/3") )
        setattr(cls, "9042/3",
                PermissibleValue(text="9042/3") )
        setattr(cls, "8832/3",
                PermissibleValue(text="8832/3") )
        setattr(cls, "8070/6",
                PermissibleValue(text="8070/6") )
        setattr(cls, "8584/3",
                PermissibleValue(text="8584/3") )
        setattr(cls, "8857/3",
                PermissibleValue(text="8857/3") )
        setattr(cls, "8147/0",
                PermissibleValue(text="8147/0") )
        setattr(cls, "8650/3",
                PermissibleValue(text="8650/3") )
        setattr(cls, "9765/1",
                PermissibleValue(text="9765/1") )
        setattr(cls, "8750/0",
                PermissibleValue(text="8750/0") )
        setattr(cls, "9975/3",
                PermissibleValue(text="9975/3") )
        setattr(cls, "9231/3",
                PermissibleValue(text="9231/3") )
        setattr(cls, "8965/0",
                PermissibleValue(text="8965/0") )
        setattr(cls, "9123/0",
                PermissibleValue(text="9123/0") )
        setattr(cls, "8256/3",
                PermissibleValue(text="8256/3") )
        setattr(cls, "9750/3",
                PermissibleValue(text="9750/3") )
        setattr(cls, "8172/3",
                PermissibleValue(text="8172/3") )
        setattr(cls, "9984/3",
                PermissibleValue(text="9984/3") )
        setattr(cls, "8140/33",
                PermissibleValue(text="8140/33") )
        setattr(cls, "8347/3",
                PermissibleValue(text="8347/3") )
        setattr(cls, "9539/1",
                PermissibleValue(text="9539/1") )
        setattr(cls, "8120/2",
                PermissibleValue(text="8120/2") )
        setattr(cls, "8335/3",
                PermissibleValue(text="8335/3") )
        setattr(cls, "8004/3",
                PermissibleValue(text="8004/3") )
        setattr(cls, "9897/3",
                PermissibleValue(text="9897/3") )
        setattr(cls, "9664/3",
                PermissibleValue(text="9664/3") )
        setattr(cls, "9724/3",
                PermissibleValue(text="9724/3") )
        setattr(cls, "8249/3",
                PermissibleValue(text="8249/3") )
        setattr(cls, "8576/3",
                PermissibleValue(text="8576/3") )
        setattr(cls, "9341/1",
                PermissibleValue(text="9341/1") )
        setattr(cls, "8420/3",
                PermissibleValue(text="8420/3") )
        setattr(cls, "8152/1",
                PermissibleValue(text="8152/1") )
        setattr(cls, "8313/1",
                PermissibleValue(text="8313/1") )
        setattr(cls, "9393/3",
                PermissibleValue(text="9393/3") )
        setattr(cls, "8630/0",
                PermissibleValue(text="8630/0") )
        setattr(cls, "9302/3",
                PermissibleValue(text="9302/3") )
        setattr(cls, "9137/3",
                PermissibleValue(text="9137/3") )
        setattr(cls, "8836/1",
                PermissibleValue(text="8836/1") )
        setattr(cls, "8050/0",
                PermissibleValue(text="8050/0") )
        setattr(cls, "8350/3",
                PermissibleValue(text="8350/3") )
        setattr(cls, "8631/3",
                PermissibleValue(text="8631/3") )
        setattr(cls, "9512/3",
                PermissibleValue(text="9512/3") )
        setattr(cls, "9445/3",
                PermissibleValue(text="9445/3") )
        setattr(cls, "8802/3",
                PermissibleValue(text="8802/3") )
        setattr(cls, "8202/0",
                PermissibleValue(text="8202/0") )
        setattr(cls, "8580/3",
                PermissibleValue(text="8580/3") )
        setattr(cls, "9752/1",
                PermissibleValue(text="9752/1") )
        setattr(cls, "9754/3",
                PermissibleValue(text="9754/3") )
        setattr(cls, "8046/3",
                PermissibleValue(text="8046/3") )
        setattr(cls, "8401/0",
                PermissibleValue(text="8401/0") )
        setattr(cls, "8592/1",
                PermissibleValue(text="8592/1") )
        setattr(cls, "8680/0",
                PermissibleValue(text="8680/0") )
        setattr(cls, "9173/0",
                PermissibleValue(text="9173/0") )
        setattr(cls, "9870/3",
                PermissibleValue(text="9870/3") )
        setattr(cls, "8620/3",
                PermissibleValue(text="8620/3") )
        setattr(cls, "8711/0",
                PermissibleValue(text="8711/0") )
        setattr(cls, "9920/3",
                PermissibleValue(text="9920/3") )
        setattr(cls, "9060/3",
                PermissibleValue(text="9060/3") )
        setattr(cls, "9679/3",
                PermissibleValue(text="9679/3") )
        setattr(cls, "9015/3",
                PermissibleValue(text="9015/3") )
        setattr(cls, "8803/3",
                PermissibleValue(text="8803/3") )
        setattr(cls, "8300/3",
                PermissibleValue(text="8300/3") )
        setattr(cls, "8243/3",
                PermissibleValue(text="8243/3") )
        setattr(cls, "9301/0",
                PermissibleValue(text="9301/0") )
        setattr(cls, "8760/0",
                PermissibleValue(text="8760/0") )
        setattr(cls, "9442/1",
                PermissibleValue(text="9442/1") )
        setattr(cls, "8682/1",
                PermissibleValue(text="8682/1") )
        setattr(cls, "8043/3",
                PermissibleValue(text="8043/3") )
        setattr(cls, "9420/3",
                PermissibleValue(text="9420/3") )
        setattr(cls, "9441/3",
                PermissibleValue(text="9441/3") )
        setattr(cls, "8143/3",
                PermissibleValue(text="8143/3") )
        setattr(cls, "8522/2",
                PermissibleValue(text="8522/2") )
        setattr(cls, "8153/3",
                PermissibleValue(text="8153/3") )
        setattr(cls, "8632/1",
                PermissibleValue(text="8632/1") )
        setattr(cls, "9260/3",
                PermissibleValue(text="9260/3") )
        setattr(cls, "9413/0",
                PermissibleValue(text="9413/0") )
        setattr(cls, "9062/3",
                PermissibleValue(text="9062/3") )
        setattr(cls, "8320/3",
                PermissibleValue(text="8320/3") )
        setattr(cls, "9340/0",
                PermissibleValue(text="9340/0") )
        setattr(cls, "8940/0",
                PermissibleValue(text="8940/0") )
        setattr(cls, "9141/0",
                PermissibleValue(text="9141/0") )
        setattr(cls, "8773/3",
                PermissibleValue(text="8773/3") )
        setattr(cls, "9510/3",
                PermissibleValue(text="9510/3") )
        setattr(cls, "8660/0",
                PermissibleValue(text="8660/0") )
        setattr(cls, "8670/3",
                PermissibleValue(text="8670/3") )
        setattr(cls, "8931/3",
                PermissibleValue(text="8931/3") )
        setattr(cls, "9538/1",
                PermissibleValue(text="9538/1") )
        setattr(cls, "8074/3",
                PermissibleValue(text="8074/3") )
        setattr(cls, "8041/34",
                PermissibleValue(text="8041/34") )
        setattr(cls, "8811/0",
                PermissibleValue(text="8811/0") )
        setattr(cls, "8512/3",
                PermissibleValue(text="8512/3") )
        setattr(cls, "8921/3",
                PermissibleValue(text="8921/3") )
        setattr(cls, "9504/3",
                PermissibleValue(text="9504/3") )
        setattr(cls, "9742/3",
                PermissibleValue(text="9742/3") )
        setattr(cls, "9729/3",
                PermissibleValue(text="9729/3") )
        setattr(cls, "8322/0",
                PermissibleValue(text="8322/0") )
        setattr(cls, "8982/3",
                PermissibleValue(text="8982/3") )
        setattr(cls, "8160/3",
                PermissibleValue(text="8160/3") )
        setattr(cls, "8213/0",
                PermissibleValue(text="8213/0") )
        setattr(cls, "9361/1",
                PermissibleValue(text="9361/1") )
        setattr(cls, "8587/0",
                PermissibleValue(text="8587/0") )
        setattr(cls, "8780/3",
                PermissibleValue(text="8780/3") )
        setattr(cls, "8824/0",
                PermissibleValue(text="8824/0") )
        setattr(cls, "8990/3",
                PermissibleValue(text="8990/3") )
        setattr(cls, "8323/0",
                PermissibleValue(text="8323/0") )
        setattr(cls, "9520/3",
                PermissibleValue(text="9520/3") )
        setattr(cls, "9080/0",
                PermissibleValue(text="9080/0") )
        setattr(cls, "8408/1",
                PermissibleValue(text="8408/1") )
        setattr(cls, "8693/1",
                PermissibleValue(text="8693/1") )
        setattr(cls, "8453/0",
                PermissibleValue(text="8453/0") )
        setattr(cls, "8246/3",
                PermissibleValue(text="8246/3") )
        setattr(cls, "8892/0",
                PermissibleValue(text="8892/0") )
        setattr(cls, "9540/0",
                PermissibleValue(text="9540/0") )
        setattr(cls, "8381/0",
                PermissibleValue(text="8381/0") )
        setattr(cls, "9472/3",
                PermissibleValue(text="9472/3") )
        setattr(cls, "9421/1",
                PermissibleValue(text="9421/1") )
        setattr(cls, "8891/0",
                PermissibleValue(text="8891/0") )
        setattr(cls, "9684/3",
                PermissibleValue(text="9684/3") )
        setattr(cls, "9809/3",
                PermissibleValue(text="9809/3") )
        setattr(cls, "9562/0",
                PermissibleValue(text="9562/0") )
        setattr(cls, "9240/3",
                PermissibleValue(text="9240/3") )
        setattr(cls, "8334/0",
                PermissibleValue(text="8334/0") )
        setattr(cls, "8964/3",
                PermissibleValue(text="8964/3") )
        setattr(cls, "9380/3",
                PermissibleValue(text="9380/3") )
        setattr(cls, "8897/1",
                PermissibleValue(text="8897/1") )
        setattr(cls, "8936/3",
                PermissibleValue(text="8936/3") )
        setattr(cls, "9150/0",
                PermissibleValue(text="9150/0") )
        setattr(cls, "8589/3",
                PermissibleValue(text="8589/3") )
        setattr(cls, "9491/0",
                PermissibleValue(text="9491/0") )
        setattr(cls, "8260/3",
                PermissibleValue(text="8260/3") )
        setattr(cls, "9100/0",
                PermissibleValue(text="9100/0") )
        setattr(cls, "8101/0",
                PermissibleValue(text="8101/0") )
        setattr(cls, "8550/3",
                PermissibleValue(text="8550/3") )
        setattr(cls, "9150/1",
                PermissibleValue(text="9150/1") )
        setattr(cls, "8452/1",
                PermissibleValue(text="8452/1") )
        setattr(cls, "8156/3",
                PermissibleValue(text="8156/3") )
        setattr(cls, "9689/3",
                PermissibleValue(text="9689/3") )
        setattr(cls, "8550/0",
                PermissibleValue(text="8550/0") )
        setattr(cls, "8960/3",
                PermissibleValue(text="8960/3") )
        setattr(cls, "9725/3",
                PermissibleValue(text="9725/3") )
        setattr(cls, "9967/3",
                PermissibleValue(text="9967/3") )
        setattr(cls, "8220/3",
                PermissibleValue(text="8220/3") )
        setattr(cls, "9738/3",
                PermissibleValue(text="9738/3") )
        setattr(cls, "9964/3",
                PermissibleValue(text="9964/3") )
        setattr(cls, "8474/3",
                PermissibleValue(text="8474/3") )
        setattr(cls, "9687/3",
                PermissibleValue(text="9687/3") )
        setattr(cls, "9667/3",
                PermissibleValue(text="9667/3") )
        setattr(cls, "9100/1",
                PermissibleValue(text="9100/1") )
        setattr(cls, "8220/0",
                PermissibleValue(text="8220/0") )
        setattr(cls, "8149/0",
                PermissibleValue(text="8149/0") )
        setattr(cls, "8811/1",
                PermissibleValue(text="8811/1") )
        setattr(cls, "8240/1",
                PermissibleValue(text="8240/1") )
        setattr(cls, "8322/3",
                PermissibleValue(text="8322/3") )
        setattr(cls, "9120/3",
                PermissibleValue(text="9120/3") )
        setattr(cls, "9539/3",
                PermissibleValue(text="9539/3") )
        setattr(cls, "8250/3",
                PermissibleValue(text="8250/3") )
        setattr(cls, "8630/3",
                PermissibleValue(text="8630/3") )
        setattr(cls, "9505/3",
                PermissibleValue(text="9505/3") )
        setattr(cls, "8509/2",
                PermissibleValue(text="8509/2") )
        setattr(cls, "8053/0",
                PermissibleValue(text="8053/0") )
        setattr(cls, "9540/1",
                PermissibleValue(text="9540/1") )
        setattr(cls, "9501/0",
                PermissibleValue(text="9501/0") )
        setattr(cls, "8214/3",
                PermissibleValue(text="8214/3") )
        setattr(cls, "9275/0",
                PermissibleValue(text="9275/0") )
        setattr(cls, "8891/3",
                PermissibleValue(text="8891/3") )
        setattr(cls, "8894/0",
                PermissibleValue(text="8894/0") )
        setattr(cls, "9530/1",
                PermissibleValue(text="9530/1") )
        setattr(cls, "8325/0",
                PermissibleValue(text="8325/0") )
        setattr(cls, "9160/0",
                PermissibleValue(text="9160/0") )
        setattr(cls, "8723/3",
                PermissibleValue(text="8723/3") )
        setattr(cls, "9262/0",
                PermissibleValue(text="9262/0") )
        setattr(cls, "9183/3",
                PermissibleValue(text="9183/3") )
        setattr(cls, "8671/0",
                PermissibleValue(text="8671/0") )
        setattr(cls, "8507/2",
                PermissibleValue(text="8507/2") )
        setattr(cls, "8340/3",
                PermissibleValue(text="8340/3") )
        setattr(cls, "9274/0",
                PermissibleValue(text="9274/0") )
        setattr(cls, "8211/3",
                PermissibleValue(text="8211/3") )
        setattr(cls, "9971/1",
                PermissibleValue(text="9971/1") )
        setattr(cls, "8270/3",
                PermissibleValue(text="8270/3") )
        setattr(cls, "8346/3",
                PermissibleValue(text="8346/3") )
        setattr(cls, "9132/0",
                PermissibleValue(text="9132/0") )
        setattr(cls, "9064/2",
                PermissibleValue(text="9064/2") )
        setattr(cls, "8230/3",
                PermissibleValue(text="8230/3") )
        setattr(cls, "9872/3",
                PermissibleValue(text="9872/3") )
        setattr(cls, "8974/1",
                PermissibleValue(text="8974/1") )
        setattr(cls, "9812/3",
                PermissibleValue(text="9812/3") )
        setattr(cls, "8560/0",
                PermissibleValue(text="8560/0") )
        setattr(cls, "9243/3",
                PermissibleValue(text="9243/3") )
        setattr(cls, "9530/3",
                PermissibleValue(text="9530/3") )
        setattr(cls, "8634/3",
                PermissibleValue(text="8634/3") )
        setattr(cls, "9764/3",
                PermissibleValue(text="9764/3") )
        setattr(cls, "8440/0",
                PermissibleValue(text="8440/0") )
        setattr(cls, "8324/0",
                PermissibleValue(text="8324/0") )
        setattr(cls, "8852/3",
                PermissibleValue(text="8852/3") )
        setattr(cls, "8261/3",
                PermissibleValue(text="8261/3") )
        setattr(cls, "8951/3",
                PermissibleValue(text="8951/3") )
        setattr(cls, "8600/0",
                PermissibleValue(text="8600/0") )
        setattr(cls, "9430/3",
                PermissibleValue(text="9430/3") )
        setattr(cls, "9090/0",
                PermissibleValue(text="9090/0") )
        setattr(cls, "8051/3",
                PermissibleValue(text="8051/3") )
        setattr(cls, "8805/3",
                PermissibleValue(text="8805/3") )
        setattr(cls, "8011/0",
                PermissibleValue(text="8011/0") )
        setattr(cls, "8741/2",
                PermissibleValue(text="8741/2") )
        setattr(cls, "9502/3",
                PermissibleValue(text="9502/3") )
        setattr(cls, "8905/0",
                PermissibleValue(text="8905/0") )
        setattr(cls, "9478/3",
                PermissibleValue(text="9478/3") )
        setattr(cls, "8041/3",
                PermissibleValue(text="8041/3") )
        setattr(cls, "9861/3",
                PermissibleValue(text="9861/3") )
        setattr(cls, "9762/3",
                PermissibleValue(text="9762/3") )
        setattr(cls, "9654/3",
                PermissibleValue(text="9654/3") )
        setattr(cls, "9700/3",
                PermissibleValue(text="9700/3") )
        setattr(cls, "8010/2",
                PermissibleValue(text="8010/2") )
        setattr(cls, "9560/3",
                PermissibleValue(text="9560/3") )
        setattr(cls, "9560/1",
                PermissibleValue(text="9560/1") )
        setattr(cls, "9330/0",
                PermissibleValue(text="9330/0") )
        setattr(cls, "8123/3",
                PermissibleValue(text="8123/3") )
        setattr(cls, "9740/3",
                PermissibleValue(text="9740/3") )
        setattr(cls, "9991/3",
                PermissibleValue(text="9991/3") )
        setattr(cls, "9761/3",
                PermissibleValue(text="9761/3") )
        setattr(cls, "8251/3",
                PermissibleValue(text="8251/3") )
        setattr(cls, "8825/1",
                PermissibleValue(text="8825/1") )
        setattr(cls, "8262/3",
                PermissibleValue(text="8262/3") )
        setattr(cls, "9597/3",
                PermissibleValue(text="9597/3") )
        setattr(cls, "9659/3",
                PermissibleValue(text="9659/3") )
        setattr(cls, "9140/3",
                PermissibleValue(text="9140/3") )
        setattr(cls, "9150/3",
                PermissibleValue(text="9150/3") )
        setattr(cls, "8811/3",
                PermissibleValue(text="8811/3") )
        setattr(cls, "8520/3",
                PermissibleValue(text="8520/3") )
        setattr(cls, "8983/0",
                PermissibleValue(text="8983/0") )
        setattr(cls, "8800/0",
                PermissibleValue(text="8800/0") )
        setattr(cls, "8482/6",
                PermissibleValue(text="8482/6") )
        setattr(cls, "9180/6",
                PermissibleValue(text="9180/6") )
        setattr(cls, "8806/6",
                PermissibleValue(text="8806/6") )
        setattr(cls, "8310/6",
                PermissibleValue(text="8310/6") )
        setattr(cls, "9440/6",
                PermissibleValue(text="9440/6") )
        setattr(cls, "8720/6",
                PermissibleValue(text="8720/6") )
        setattr(cls, "8920/6",
                PermissibleValue(text="8920/6") )
        setattr(cls, "8500/6",
                PermissibleValue(text="8500/6") )
        setattr(cls, "8046/6",
                PermissibleValue(text="8046/6") )
        setattr(cls, "8800/6",
                PermissibleValue(text="8800/6") )
        setattr(cls, "8020/6",
                PermissibleValue(text="8020/6") )
        setattr(cls, "8041/6",
                PermissibleValue(text="8041/6") )
        setattr(cls, "8249/6",
                PermissibleValue(text="8249/6") )
        setattr(cls, "8471/1",
                PermissibleValue(text="8471/1") )
        setattr(cls, "8950/6",
                PermissibleValue(text="8950/6") )
        setattr(cls, "8240/6",
                PermissibleValue(text="8240/6") )
        setattr(cls, "8801/6",
                PermissibleValue(text="8801/6") )
        setattr(cls, "8441/6",
                PermissibleValue(text="8441/6") )
        setattr(cls, "8804/6",
                PermissibleValue(text="8804/6") )
        setattr(cls, "8311/6",
                PermissibleValue(text="8311/6") )
        setattr(cls, "8040/3",
                PermissibleValue(text="8040/3") )

class CCDHDiagnosisDiseaseStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis disease_status
    """
    _defn = EnumDefinition(
        name="CCDHDiagnosisDiseaseStatus",
        description="Autogenerated Enumeration for CRDC-H Diagnosis disease_status",
        code_set=None,
        code_set_version="2021-05-30T01:20:47.172919+00:00",
    )

class CCDHDiagnosisMethodOfDiagnosis(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis
    """
    Other = PermissibleValue(text="Other",
                                 description="Other")
    Laparotomy = PermissibleValue(text="Laparotomy",
                                           description="Laparotomy")
    Cytology = PermissibleValue(text="Cytology",
                                       description="Cytology")
    Debulking = PermissibleValue(text="Debulking",
                                         description="Debulking")
    Cystoscopy = PermissibleValue(text="Cystoscopy",
                                           description="Cystoscopy")
    Autopsy = PermissibleValue(text="Autopsy",
                                     description="Autopsy")
    Biopsy = PermissibleValue(text="Biopsy",
                                   description="Biopsy")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    Laparoscopy = PermissibleValue(text="Laparoscopy",
                                             description="Laparoscopy")
    Enucleation = PermissibleValue(text="Enucleation",
                                             description="Enucleation")
    Imaging = PermissibleValue(text="Imaging",
                                     description="Imaging Technique")
    Thoracentesis = PermissibleValue(text="Thoracentesis",
                                                 description="Thoracentesis")

    _defn = EnumDefinition(
        name="CCDHDiagnosisMethodOfDiagnosis",
        description="Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis",
        code_set=None,
        code_set_version="2021-05-30T01:20:47.324765+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Ultrasound Guided Biopsy",
                PermissibleValue(text="Ultrasound Guided Biopsy",
                                 description="Ultrasound guided biopsy") )
        setattr(cls, "Diagnostic Imaging",
                PermissibleValue(text="Diagnostic Imaging",
                                 description="Diagnostic Imaging") )
        setattr(cls, "Pap Smear",
                PermissibleValue(text="Pap Smear",
                                 description="Papanicolaou Smear Procedure") )
        setattr(cls, "Bone Marrow Aspirate",
                PermissibleValue(text="Bone Marrow Aspirate",
                                 description="Bone Marrow Aspiration") )
        setattr(cls, "Fine Needle Aspiration",
                PermissibleValue(text="Fine Needle Aspiration",
                                 description="Fine-Needle Aspiration") )
        setattr(cls, "Physical Exam",
                PermissibleValue(text="Physical Exam",
                                 description="Physical Examination") )
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )
        setattr(cls, "Pathologic Review",
                PermissibleValue(text="Pathologic Review",
                                 description="Pathologic Examination") )
        setattr(cls, "Excisional Biopsy",
                PermissibleValue(text="Excisional Biopsy",
                                 description="Excisional Biopsy") )
        setattr(cls, "Dilation and Curettage Procedure",
                PermissibleValue(text="Dilation and Curettage Procedure",
                                 description="Dilation and Curettage") )
        setattr(cls, "Surgical Resection",
                PermissibleValue(text="Surgical Resection",
                                 description="Excision") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not Reported") )
        setattr(cls, "Blood Draw",
                PermissibleValue(text="Blood Draw",
                                 description="Phlebotomy") )
        setattr(cls, "Incisional Biopsy",
                PermissibleValue(text="Incisional Biopsy",
                                 description="Incisional Biopsy") )
        setattr(cls, "Core Biopsy",
                PermissibleValue(text="Core Biopsy",
                                 description="Core Biopsy") )

class CCDHDimensionalObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservation category
    """
    _defn = EnumDefinition(
        name="CCDHDimensionalObservationCategory",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:47.491087+00:00",
    )

class CCDHDimensionalObservationObservationType(EnumDefinitionImpl):
    """
    Types of measurements that describe the physical dimensions of an entity (e.g. a Specimen)
    """
    length = PermissibleValue(text="length",
                                   description="The length of a three-dimensional specimen, as measured in a plane perpendicular to the planes in which the width and height of the specimen are measured.")
    width = PermissibleValue(text="width",
                                 description="The widthof a three-dimensional specimen, as measured in a plane perpendicular to the planes in which the length and height of the specimen are measured.")
    longest_dimension = PermissibleValue(text="longest_dimension",
                                                         description="The measured extent of the longest straight path across a specimen.")
    shortest_dimension = PermissibleValue(text="shortest_dimension",
                                                           description="The measured extent of the shortest straight path across a specimen.")
    intermediate_dimension = PermissibleValue(text="intermediate_dimension",
                                                                   description="The measured extent of the intermediate straight path across a specimen.")
    surface_area = PermissibleValue(text="surface_area",
                                               description="The total surface area of the specimen")

    _defn = EnumDefinition(
        name="CCDHDimensionalObservationObservationType",
        description="Types of measurements that describe the physical dimensions of an entity (e.g. a Specimen)",
    )

class CCDHDimensionalObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHDimensionalObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:47.944333+00:00",
    )

class CCDHDimensionalObservationSetCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservationSet category
    """
    _defn = EnumDefinition(
        name="CCDHDimensionalObservationSetCategory",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservationSet category",
        code_set=None,
        code_set_version="2021-05-30T01:20:48.257738+00:00",
    )

class CCDHDimensionalObservationSetMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservationSet method_type
    """
    _defn = EnumDefinition(
        name="CCDHDimensionalObservationSetMethodType",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:48.621404+00:00",
    )

class CCDHDocumentDocumentType(EnumDefinitionImpl):
    """
    The high-level type of the report (e.g. 'pathology report')
    """
    protocol = PermissibleValue(text="protocol",
                                       description="A protocol by which the sample was obtained or generated (e.g. a protocol listed in protocols.io)")

    _defn = EnumDefinition(
        name="CCDHDocumentDocumentType",
        description="The high-level type of the report (e.g. 'pathology report')",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pathology report",
                PermissibleValue(text="pathology report",
                                 description="A pathology report describing the specimen") )

class CCDHEnvironmentalExposureObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation category
    """
    _defn = EnumDefinition(
        name="CCDHEnvironmentalExposureObservationCategory",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:49.347812+00:00",
    )

class CCDHEnvironmentalExposureObservationObservationType(EnumDefinitionImpl):
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
                                                                                                   description="The yes/no/unknown indicator used to describe whether a patient was exposured to respirable crystalline silica, a widespread, naturally occurring, crystalline metal oxide that consists of different forms including quartz, cristobalite, tridymite, tripoli, ganister, chert and novaculite.")
    type_of_smoke_exposure = PermissibleValue(text="type_of_smoke_exposure",
                                                                   description="The text term used to describe the patient's specific type of smoke exposure.")

    _defn = EnumDefinition(
        name="CCDHEnvironmentalExposureObservationObservationType",
        description="Types of observations about a Subject's environmental exposures.",
    )

class CCDHEnvironmentalExposureObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHEnvironmentalExposureObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:50.082951+00:00",
    )

class CCDHEnvironmentalExposureObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHEnvironmentalExposureObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:50.598543+00:00",
    )

class CCDHIdentifierType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Identifier type
    """
    _defn = EnumDefinition(
        name="CCDHIdentifierType",
        description="Autogenerated Enumeration for CRDC-H Identifier type",
        code_set=None,
        code_set_version="2021-05-30T01:20:50.956156+00:00",
    )

class CCDHObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation category
    """
    _defn = EnumDefinition(
        name="CCDHObservationCategory",
        description="Autogenerated Enumeration for CRDC-H Observation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:51.323302+00:00",
    )

class CCDHObservationObservationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation observation_type
    """
    _defn = EnumDefinition(
        name="CCDHObservationObservationType",
        description="Autogenerated Enumeration for CRDC-H Observation observation_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:51.803978+00:00",
    )

class CCDHObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation method_type
    """
    _defn = EnumDefinition(
        name="CCDHObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H Observation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:51.952936+00:00",
    )

class CCDHObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.097008+00:00",
    )

class CCDHObservationSetCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ObservationSet category
    """
    _defn = EnumDefinition(
        name="CCDHObservationSetCategory",
        description="Autogenerated Enumeration for CRDC-H ObservationSet category",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.246141+00:00",
    )

class CCDHObservationSetMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ObservationSet method_type
    """
    _defn = EnumDefinition(
        name="CCDHObservationSetMethodType",
        description="Autogenerated Enumeration for CRDC-H ObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.399811+00:00",
    )

class CCDHQuantityValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHQuantityValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.550334+00:00",
    )

class CCDHQuantityUnit(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Quantity unit
    """
    _defn = EnumDefinition(
        name="CCDHQuantityUnit",
        description="Autogenerated Enumeration for CRDC-H Quantity unit",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.698718+00:00",
    )

class CCDHResearchProjectResearchProjectType(EnumDefinitionImpl):
    """
    A high-level type of research activity
    """
    Program = PermissibleValue(text="Program",
                                     description="A broad framework of goals to be achieved.")
    Project = PermissibleValue(text="Project",
                                     description="Any specifically defined piece of work that is undertaken or attempted to meet a single requirement.")

    _defn = EnumDefinition(
        name="CCDHResearchProjectResearchProjectType",
        description="A high-level type of research activity",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Clinical Trial",
                PermissibleValue(text="Clinical Trial",
                                 description="A research study that prospectively assigns participants to one or more health-related interventions to evaluate the effects on health outcomes.") )

class CCDHResearchSubjectPrimaryDiagnosisCondition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition
    """
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    Mesonephromas = PermissibleValue(text="Mesonephromas",
                                                 description="Mesonephric Neoplasm")
    Meningiomas = PermissibleValue(text="Meningiomas",
                                             description="Meningioma")
    Gliomas = PermissibleValue(text="Gliomas",
                                     description="Glioma")
    Other = PermissibleValue(text="Other")
    Neuroblastoma = PermissibleValue(text="Neuroblastoma")
    Thymoma = PermissibleValue(text="Thymoma")
    Glioblastoma = PermissibleValue(text="Glioblastoma")
    Cholangiocarcinoma = PermissibleValue(text="Cholangiocarcinoma")
    Sarcoma = PermissibleValue(text="Sarcoma")
    Osteosarcoma = PermissibleValue(text="Osteosarcoma")
    Mesothelioma = PermissibleValue(text="Mesothelioma")

    _defn = EnumDefinition(
        name="CCDHResearchSubjectPrimaryDiagnosisCondition",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition",
        code_set=None,
        code_set_version="2021-05-30T01:20:52.984589+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Myeloid Leukemias",
                PermissibleValue(text="Myeloid Leukemias",
                                 description="Myeloid Leukemia") )
        setattr(cls, "Precursor Cell Lymphoblastic Lymphoma",
                PermissibleValue(text="Precursor Cell Lymphoblastic Lymphoma",
                                 description="Lymphoblastic Lymphoma") )
        setattr(cls, "Not Applicable",
                PermissibleValue(text="Not Applicable") )
        setattr(cls, "Mast Cell Tumors",
                PermissibleValue(text="Mast Cell Tumors",
                                 description="Mast Cell Neoplasm") )
        setattr(cls, "Giant Cell Tumors",
                PermissibleValue(text="Giant Cell Tumors",
                                 description="Giant Cell Tumor") )
        setattr(cls, "Malignant Lymphomas, NOS or Diffuse",
                PermissibleValue(text="Malignant Lymphomas, NOS or Diffuse",
                                 description="Not Otherwise Specified or Diffuse Lymphoma") )
        setattr(cls, "Germ Cell Neoplasms",
                PermissibleValue(text="Germ Cell Neoplasms",
                                 description="Germ Cell Tumor") )
        setattr(cls, "Adenomas and Adenocarcinomas",
                PermissibleValue(text="Adenomas and Adenocarcinomas",
                                 description="Adenoma and Adenocarcinoma") )
        setattr(cls, "Squamous Cell Neoplasms",
                PermissibleValue(text="Squamous Cell Neoplasms",
                                 description="Squamous Cell Neoplasm") )
        setattr(cls, "Lipomatous Neoplasms",
                PermissibleValue(text="Lipomatous Neoplasms",
                                 description="Lipomatous Neoplasm") )
        setattr(cls, "Complex Mixed and Stromal Neoplasms",
                PermissibleValue(text="Complex Mixed and Stromal Neoplasms",
                                 description="Complex Mixed and Stromal Neoplasm") )
        setattr(cls, "Thymic Epithelial Neoplasms",
                PermissibleValue(text="Thymic Epithelial Neoplasms",
                                 description="Combined Thymic Epithelial Neoplasm") )
        setattr(cls, "Miscellaneous Tumors",
                PermissibleValue(text="Miscellaneous Tumors",
                                 description="Miscellaneous Neoplasm") )
        setattr(cls, "Osseous and Chondromatous Neoplasms",
                PermissibleValue(text="Osseous and Chondromatous Neoplasms",
                                 description="Osteogenic Neoplasm and Chondrogenic Neoplasm") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not Reported") )
        setattr(cls, "Lymphatic Vessel Tumors",
                PermissibleValue(text="Lymphatic Vessel Tumors",
                                 description="Lymphatic Vessel Neoplasm") )
        setattr(cls, "Adnexal and Skin Appendage Neoplasms",
                PermissibleValue(text="Adnexal and Skin Appendage Neoplasms",
                                 description="Adnexal Carcinoma and Skin Appendage Neoplasm") )
        setattr(cls, "Specialized Gonadal Neoplasms",
                PermissibleValue(text="Specialized Gonadal Neoplasms",
                                 description="Specialized Gonadal Neoplasm") )
        setattr(cls, "Fibromatous Neoplasms",
                PermissibleValue(text="Fibromatous Neoplasms",
                                 description="Fibromatosis") )
        setattr(cls, "Immunoproliferative Diseases",
                PermissibleValue(text="Immunoproliferative Diseases",
                                 description="Immunoproliferative Disease") )
        setattr(cls, "Plasma Cell Tumors",
                PermissibleValue(text="Plasma Cell Tumors",
                                 description="Plasma Cell Neoplasm") )
        setattr(cls, "Neoplasms of Histiocytes and Accessory Lymphoid Cells",
                PermissibleValue(text="Neoplasms of Histiocytes and Accessory Lymphoid Cells",
                                 description="Neoplasms of Histiocytes and Accessory Lymphoid Cells") )
        setattr(cls, "Mature T- and NK-Cell Lymphomas",
                PermissibleValue(text="Mature T- and NK-Cell Lymphomas",
                                 description="Mature T-Cell and NK-Cell Non-Hodgkin Lymphoma") )
        setattr(cls, "Cystic, Mucinous and Serous Neoplasms",
                PermissibleValue(text="Cystic, Mucinous and Serous Neoplasms",
                                 description="Cystic Neoplasm Mucinous Neoplasm and Serous Neoplasm") )
        setattr(cls, "Myxomatous Neoplasms",
                PermissibleValue(text="Myxomatous Neoplasms",
                                 description="Myxoma") )
        setattr(cls, "Other Hematologic Disorders",
                PermissibleValue(text="Other Hematologic Disorders",
                                 description="Other Hematologic and Lymphocytic Disorder") )
        setattr(cls, "Leukemias, NOS",
                PermissibleValue(text="Leukemias, NOS",
                                 description="Not Otherwise Specified Leukemia") )
        setattr(cls, "Lymphoid Leukemias",
                PermissibleValue(text="Lymphoid Leukemias",
                                 description="Lymphoid Leukemia") )
        setattr(cls, "Nevi and Melanomas",
                PermissibleValue(text="Nevi and Melanomas",
                                 description="Melanocytic Nevus and Melanoma") )
        setattr(cls, "Soft Tissue Tumors and Sarcomas, NOS",
                PermissibleValue(text="Soft Tissue Tumors and Sarcomas, NOS",
                                 description="Soft Tissue Neoplasm and Soft Tissue Sarcoma") )
        setattr(cls, "Chronic Myeloproliferative Disorders",
                PermissibleValue(text="Chronic Myeloproliferative Disorders",
                                 description="Chronic Myeloproliferative Neoplasm") )
        setattr(cls, "Mature B-Cell Lymphomas",
                PermissibleValue(text="Mature B-Cell Lymphomas",
                                 description="Mature B-Cell Non-Hodgkin Lymphoma") )
        setattr(cls, "Myelodysplastic Syndromes",
                PermissibleValue(text="Myelodysplastic Syndromes",
                                 description="Myelodysplastic Syndrome") )
        setattr(cls, "Trophoblastic neoplasms",
                PermissibleValue(text="Trophoblastic neoplasms",
                                 description="Trophoblastic Tumor") )
        setattr(cls, "Transitional Cell Papillomas and Carcinomas",
                PermissibleValue(text="Transitional Cell Papillomas and Carcinomas",
                                 description="Transitional Cell Papilloma and Transitional Cell Carcinoma") )
        setattr(cls, "Hodgkin Lymphoma",
                PermissibleValue(text="Hodgkin Lymphoma",
                                 description="Hodgkin Lymphoma") )
        setattr(cls, "Mesothelial Neoplasms",
                PermissibleValue(text="Mesothelial Neoplasms",
                                 description="Mesothelial Neoplasm") )
        setattr(cls, "Blood Vessel Tumors",
                PermissibleValue(text="Blood Vessel Tumors",
                                 description="Blood Vessel Neoplasm") )
        setattr(cls, "Epithelial Neoplasms, NOS",
                PermissibleValue(text="Epithelial Neoplasms, NOS",
                                 description="Not Otherwise Specified Epithelial Neoplasm") )
        setattr(cls, "Nerve Sheath Tumors",
                PermissibleValue(text="Nerve Sheath Tumors",
                                 description="Nerve Sheath Neoplasm") )
        setattr(cls, "Mucoepidermoid Neoplasms",
                PermissibleValue(text="Mucoepidermoid Neoplasms",
                                 description="Mucoepidermoid Carcinoma") )
        setattr(cls, "Odontogenic Tumors",
                PermissibleValue(text="Odontogenic Tumors",
                                 description="Odontogenic Neoplasm") )
        setattr(cls, "Granular Cell Tumors and Alveolar Soft Part Sarcomas",
                PermissibleValue(text="Granular Cell Tumors and Alveolar Soft Part Sarcomas",
                                 description="Granular Cell Tumor and Alveolar Soft Part Sarcoma") )
        setattr(cls, "Acinar Cell Neoplasms",
                PermissibleValue(text="Acinar Cell Neoplasms",
                                 description="Acinar Cell Neoplasm") )
        setattr(cls, "Ductal and Lobular Neoplasms",
                PermissibleValue(text="Ductal and Lobular Neoplasms",
                                 description="Ductal Breast Carcinoma In Situ and Lobular Carcinoma In Situ") )
        setattr(cls, "Paragangliomas and Glomus Tumors",
                PermissibleValue(text="Paragangliomas and Glomus Tumors",
                                 description="Paraganglioma And Glomus Tumor") )
        setattr(cls, "Neoplasms, NOS",
                PermissibleValue(text="Neoplasms, NOS",
                                 description="Not Otherwise Specified Neoplasm") )
        setattr(cls, "Other Leukemias",
                PermissibleValue(text="Other Leukemias",
                                 description="Other Leukemia") )
        setattr(cls, "Miscellaneous Bone Tumors",
                PermissibleValue(text="Miscellaneous Bone Tumors",
                                 description="Miscellaneous Bone Neoplasm") )
        setattr(cls, "Synovial-like Neoplasms",
                PermissibleValue(text="Synovial-like Neoplasms",
                                 description="Synovial Neoplasm") )
        setattr(cls, "Complex Epithelial Neoplasms",
                PermissibleValue(text="Complex Epithelial Neoplasms") )
        setattr(cls, "Fibroepithelial Neoplasms",
                PermissibleValue(text="Fibroepithelial Neoplasms",
                                 description="Fibroepithelial Neoplasm") )
        setattr(cls, "Basal Cell Neoplasms",
                PermissibleValue(text="Basal Cell Neoplasms",
                                 description="Basal Cell Neoplasm") )
        setattr(cls, "Neuroepitheliomatous Neoplasms",
                PermissibleValue(text="Neuroepitheliomatous Neoplasms",
                                 description="Neuroepithelial Neoplasm") )
        setattr(cls, "Myomatous Neoplasms",
                PermissibleValue(text="Myomatous Neoplasms",
                                 description="Myomatous Neoplasm") )
        setattr(cls, "Head and Neck Squamous Cell Carcinoma",
                PermissibleValue(text="Head and Neck Squamous Cell Carcinoma") )
        setattr(cls, "Lung Adenocarcinoma",
                PermissibleValue(text="Lung Adenocarcinoma") )
        setattr(cls, "Thyroid Carcinoma",
                PermissibleValue(text="Thyroid Carcinoma") )
        setattr(cls, "Testicular Germ Cell Tumors",
                PermissibleValue(text="Testicular Germ Cell Tumors") )
        setattr(cls, "Esophageal Carcinoma",
                PermissibleValue(text="Esophageal Carcinoma") )
        setattr(cls, "Multiple Myeloma",
                PermissibleValue(text="Multiple Myeloma") )
        setattr(cls, "HIV+ Tumor Molecular Characterization Project - Cervical Cancer",
                PermissibleValue(text="HIV+ Tumor Molecular Characterization Project - Cervical Cancer") )
        setattr(cls, "Brain Lower Grade Glioma",
                PermissibleValue(text="Brain Lower Grade Glioma") )
        setattr(cls, "Clear Cell Sarcoma of the Kidney",
                PermissibleValue(text="Clear Cell Sarcoma of the Kidney") )
        setattr(cls, "Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma",
                PermissibleValue(text="Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma") )
        setattr(cls, "Prostate Adenocarcinoma",
                PermissibleValue(text="Prostate Adenocarcinoma") )
        setattr(cls, "Bladder Urothelial Carcinoma",
                PermissibleValue(text="Bladder Urothelial Carcinoma") )
        setattr(cls, "Rhabdoid Tumor",
                PermissibleValue(text="Rhabdoid Tumor") )
        setattr(cls, "Pheochromocytoma and Paraganglioma",
                PermissibleValue(text="Pheochromocytoma and Paraganglioma") )
        setattr(cls, "Clear Cell Renal Cell Carcinoma",
                PermissibleValue(text="Clear Cell Renal Cell Carcinoma") )
        setattr(cls, "Pediatric/AYA Brain Tumors",
                PermissibleValue(text="Pediatric/AYA Brain Tumors") )
        setattr(cls, "Adrenocortical Carcinoma",
                PermissibleValue(text="Adrenocortical Carcinoma") )
        setattr(cls, "Colon Adenocarcinoma",
                PermissibleValue(text="Colon Adenocarcinoma") )
        setattr(cls, "Uterine Corpus Endometrial Carcinoma",
                PermissibleValue(text="Uterine Corpus Endometrial Carcinoma") )
        setattr(cls, "Oral Squamous Cell Carcinoma",
                PermissibleValue(text="Oral Squamous Cell Carcinoma") )
        setattr(cls, "High-Risk Wilms Tumor",
                PermissibleValue(text="High-Risk Wilms Tumor") )
        setattr(cls, "Papillary Renal Cell Carcinoma",
                PermissibleValue(text="Papillary Renal Cell Carcinoma") )
        setattr(cls, "Stomach Adenocarcinoma",
                PermissibleValue(text="Stomach Adenocarcinoma") )
        setattr(cls, "Chronic Lymphocytic Leukemia",
                PermissibleValue(text="Chronic Lymphocytic Leukemia") )
        setattr(cls, "Uveal Melanoma",
                PermissibleValue(text="Uveal Melanoma") )
        setattr(cls, "Glioblastoma Multiforme",
                PermissibleValue(text="Glioblastoma Multiforme") )
        setattr(cls, "Pancreatic Ductal Adenocarcinoma",
                PermissibleValue(text="Pancreatic Ductal Adenocarcinoma") )
        setattr(cls, "Ovarian Serous Cystadenocarcinoma",
                PermissibleValue(text="Ovarian Serous Cystadenocarcinoma") )
        setattr(cls, "Pancreatic Adenocarcinoma",
                PermissibleValue(text="Pancreatic Adenocarcinoma") )
        setattr(cls, "Chromophobe Renal Cell Carcinoma",
                PermissibleValue(text="Chromophobe Renal Cell Carcinoma") )
        setattr(cls, "Rectum Adenocarcinoma",
                PermissibleValue(text="Rectum Adenocarcinoma") )
        setattr(cls, "Kidney Renal Clear Cell Carcinoma",
                PermissibleValue(text="Kidney Renal Clear Cell Carcinoma") )
        setattr(cls, "Liver Hepatocellular Carcinoma",
                PermissibleValue(text="Liver Hepatocellular Carcinoma") )
        setattr(cls, "Early Onset Gastric Cancer",
                PermissibleValue(text="Early Onset Gastric Cancer") )
        setattr(cls, "HIV+ Tumor Molecular Characterization Project - Lung Cancer",
                PermissibleValue(text="HIV+ Tumor Molecular Characterization Project - Lung Cancer") )
        setattr(cls, "Acute Myeloid Leukemia",
                PermissibleValue(text="Acute Myeloid Leukemia") )
        setattr(cls, "Lung Squamous Cell Carcinoma",
                PermissibleValue(text="Lung Squamous Cell Carcinoma") )
        setattr(cls, "Skin Cutaneous Melanoma",
                PermissibleValue(text="Skin Cutaneous Melanoma") )
        setattr(cls, "Kidney Chromophobe",
                PermissibleValue(text="Kidney Chromophobe") )
        setattr(cls, "Uterine Carcinosarcoma",
                PermissibleValue(text="Uterine Carcinosarcoma") )
        setattr(cls, "Breast Invasive Carcinoma",
                PermissibleValue(text="Breast Invasive Carcinoma") )
        setattr(cls, "Kidney Renal Papillary Cell Carcinoma",
                PermissibleValue(text="Kidney Renal Papillary Cell Carcinoma") )
        setattr(cls, "Lymphoid Neoplasm Diffuse Large B-cell Lymphoma",
                PermissibleValue(text="Lymphoid Neoplasm Diffuse Large B-cell Lymphoma") )
        setattr(cls, "Acute Lymphoblastic Leukemia",
                PermissibleValue(text="Acute Lymphoblastic Leukemia") )
        setattr(cls, "Hepatocellular Carcinoma",
                PermissibleValue(text="Hepatocellular Carcinoma") )
        setattr(cls, "Burkitt Lymphoma",
                PermissibleValue(text="Burkitt Lymphoma") )

class CCDHResearchSubjectIndexTimepoint(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint
    """
    Recurrence = PermissibleValue(text="Recurrence")
    Diagnosis = PermissibleValue(text="Diagnosis",
                                         description="Diagnosis")

    _defn = EnumDefinition(
        name="CCDHResearchSubjectIndexTimepoint",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint",
        code_set=None,
        code_set_version="2021-05-30T01:20:53.262015+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Study Enrollment",
                PermissibleValue(text="Study Enrollment",
                                 description="Clinical Study Enrollment") )
        setattr(cls, "First Patient Visit",
                PermissibleValue(text="First Patient Visit",
                                 description="First Patient Visit") )
        setattr(cls, "First Treatment",
                PermissibleValue(text="First Treatment") )
        setattr(cls, "Sample Procurement",
                PermissibleValue(text="Sample Procurement",
                                 description="Tissue Procurement") )
        setattr(cls, "Initial Genomic Sequencing",
                PermissibleValue(text="Initial Genomic Sequencing") )

class CCDHSpecimenSpecimenType(EnumDefinitionImpl):
    """
    A high-level type of specimen, based on its derivation provenance (i.e. how far removed it is from the original
    sample extracted from a source).
    """
    portion = PermissibleValue(text="portion",
                                     description="A physical sub-part taken from an existing specimen.")
    aliquot = PermissibleValue(text="aliquot",
                                     description="A specimen that results from the division of some parent specimen into equal amounts for downstream analysis.")
    analyte = PermissibleValue(text="analyte",
                                     description="A specimen gnerated through the extraction of a specified class of substance/chemical (e.g. DNA, RNA, protein) from a parent specimen, which is stored in solution as an analyte.")
    slide = PermissibleValue(text="slide",
                                 description="A specimen that is mounted on a slide or coverslip for microscopic analysis.")

    _defn = EnumDefinition(
        name="CCDHSpecimenSpecimenType",
        description="A high-level type of specimen, based on its derivation provenance (i.e. how far removed it is from the original sample extracted from a source).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "initial sample",
                PermissibleValue(text="initial sample",
                                 description="A specimen representing the matieral that was directly collected from a subject (i.e. not generated through portioning, aliquoting, or analyte extraction from an existing specimen).") )

class CCDHSpecimenAnalyteType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen analyte_type
    """
    DNA = PermissibleValue(text="DNA",
                             description="DNA")
    RNA = PermissibleValue(text="RNA",
                             description="Ribonucleic Acid")
    Protein = PermissibleValue(text="Protein",
                                     description="Protein")
    cfDNA = PermissibleValue(text="cfDNA")
    G = PermissibleValue(text="G",
                         description="GenomePlex (Rubicon) Amplified DNA")
    H = PermissibleValue(text="H",
                         description="Hybrid Extraction RNA")
    E = PermissibleValue(text="E")
    D = PermissibleValue(text="D",
                         description="DNA")
    T = PermissibleValue(text="T",
                         description="Total Ribonucleic Acid")
    W = PermissibleValue(text="W",
                         description="Repli-G (Qiagen) DNA")
    S = PermissibleValue(text="S")
    R = PermissibleValue(text="R",
                         description="Ribonucleic Acid")
    X = PermissibleValue(text="X",
                         description="Repli-G X (Qiagen) DNA")
    Y = PermissibleValue(text="Y")

    _defn = EnumDefinition(
        name="CCDHSpecimenAnalyteType",
        description="Autogenerated Enumeration for CRDC-H Specimen analyte_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:53.566395+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Repli-G (Qiagen) DNA",
                PermissibleValue(text="Repli-G (Qiagen) DNA",
                                 description="Repli-G (Qiagen) DNA") )
        setattr(cls, "GenomePlex (Rubicon) Amplified DNA",
                PermissibleValue(text="GenomePlex (Rubicon) Amplified DNA") )
        setattr(cls, "Repli-G Pooled (Qiagen) DNA",
                PermissibleValue(text="Repli-G Pooled (Qiagen) DNA",
                                 description="REPLI-g Pooled DNA") )
        setattr(cls, "Repli-G X (Qiagen) DNA",
                PermissibleValue(text="Repli-G X (Qiagen) DNA",
                                 description="Repli-G X (Qiagen) DNA") )
        setattr(cls, "EBV Immortalized Normal",
                PermissibleValue(text="EBV Immortalized Normal",
                                 description="Normal Epstein-Barr Virus Immortalization") )
        setattr(cls, "FFPE RNA",
                PermissibleValue(text="FFPE RNA",
                                 description="Formalin-Fixed Paraffin-Embedded RNA") )
        setattr(cls, "FFPE DNA",
                PermissibleValue(text="FFPE DNA",
                                 description="Formalin-Fixed Paraffin-Embedded DNA") )
        setattr(cls, "Nuclei RNA",
                PermissibleValue(text="Nuclei RNA") )
        setattr(cls, "Total RNA",
                PermissibleValue(text="Total RNA",
                                 description="Total Ribonucleic Acid") )

class CCDHSpecimenSourceMaterialType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen source_material_type
    """
    Granulocytes = PermissibleValue(text="Granulocytes",
                                               description="Granulocyte")
    RNA = PermissibleValue(text="RNA")
    Tumor = PermissibleValue(text="Tumor",
                                 description="Neoplasm")
    Unknown = PermissibleValue(text="Unknown")
    DNA = PermissibleValue(text="DNA")
    Slides = PermissibleValue(text="Slides")
    Metastatic = PermissibleValue(text="Metastatic")
    Saliva = PermissibleValue(text="Saliva",
                                   description="Saliva")

    _defn = EnumDefinition(
        name="CCDHSpecimenSourceMaterialType",
        description="Autogenerated Enumeration for CRDC-H Specimen source_material_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:53.732738+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "61",
                PermissibleValue(text="61") )
        setattr(cls, "15",
                PermissibleValue(text="15") )
        setattr(cls, "02",
                PermissibleValue(text="02") )
        setattr(cls, "05",
                PermissibleValue(text="05") )
        setattr(cls, "03",
                PermissibleValue(text="03") )
        setattr(cls, "07",
                PermissibleValue(text="07") )
        setattr(cls, "30",
                PermissibleValue(text="30") )
        setattr(cls, "20",
                PermissibleValue(text="20") )
        setattr(cls, "17",
                PermissibleValue(text="17") )
        setattr(cls, "42",
                PermissibleValue(text="42") )
        setattr(cls, "04",
                PermissibleValue(text="04") )
        setattr(cls, "01",
                PermissibleValue(text="01") )
        setattr(cls, "08",
                PermissibleValue(text="08") )
        setattr(cls, "09",
                PermissibleValue(text="09") )
        setattr(cls, "50",
                PermissibleValue(text="50") )
        setattr(cls, "31",
                PermissibleValue(text="31") )
        setattr(cls, "16",
                PermissibleValue(text="16") )
        setattr(cls, "86",
                PermissibleValue(text="86") )
        setattr(cls, "06",
                PermissibleValue(text="06") )
        setattr(cls, "14",
                PermissibleValue(text="14") )
        setattr(cls, "40",
                PermissibleValue(text="40") )
        setattr(cls, "13",
                PermissibleValue(text="13") )
        setattr(cls, "10",
                PermissibleValue(text="10") )
        setattr(cls, "99",
                PermissibleValue(text="99") )
        setattr(cls, "11",
                PermissibleValue(text="11") )
        setattr(cls, "41",
                PermissibleValue(text="41") )
        setattr(cls, "60",
                PermissibleValue(text="60") )
        setattr(cls, "18",
                PermissibleValue(text="18") )
        setattr(cls, "12",
                PermissibleValue(text="12") )
        setattr(cls, "85",
                PermissibleValue(text="85") )
        setattr(cls, "32",
                PermissibleValue(text="32") )
        setattr(cls, "Lymphoid Normal",
                PermissibleValue(text="Lymphoid Normal") )
        setattr(cls, "EBV Immortalized Normal",
                PermissibleValue(text="EBV Immortalized Normal") )
        setattr(cls, "Pleural Effusion",
                PermissibleValue(text="Pleural Effusion") )
        setattr(cls, "Additional Metastatic",
                PermissibleValue(text="Additional Metastatic") )
        setattr(cls, "Fibroblasts from Bone Marrow Normal",
                PermissibleValue(text="Fibroblasts from Bone Marrow Normal") )
        setattr(cls, "Neoplasms of Uncertain and Unknown Behavior",
                PermissibleValue(text="Neoplasms of Uncertain and Unknown Behavior") )
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )
        setattr(cls, "Mononuclear Cells from Bone Marrow Normal",
                PermissibleValue(text="Mononuclear Cells from Bone Marrow Normal") )
        setattr(cls, "Recurrent Blood Derived Cancer - Bone Marrow",
                PermissibleValue(text="Recurrent Blood Derived Cancer - Bone Marrow") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "In Situ Neoplasms",
                PermissibleValue(text="In Situ Neoplasms") )
        setattr(cls, "Tumor Adjacent Normal - Post Neo-adjuvant Therapy",
                PermissibleValue(text="Tumor Adjacent Normal - Post Neo-adjuvant Therapy") )
        setattr(cls, "Post neo-adjuvant therapy",
                PermissibleValue(text="Post neo-adjuvant therapy") )
        setattr(cls, "Recurrent Blood Derived Cancer - Peripheral Blood",
                PermissibleValue(text="Recurrent Blood Derived Cancer - Peripheral Blood") )
        setattr(cls, "Additional - New Primary",
                PermissibleValue(text="Additional - New Primary") )
        setattr(cls, "Control Analyte",
                PermissibleValue(text="Control Analyte") )
        setattr(cls, "Repli-G (Qiagen) DNA",
                PermissibleValue(text="Repli-G (Qiagen) DNA") )
        setattr(cls, "Primary Blood Derived Cancer - Peripheral Blood",
                PermissibleValue(text="Primary Blood Derived Cancer - Peripheral Blood") )
        setattr(cls, "Blood Derived Normal",
                PermissibleValue(text="Blood Derived Normal") )
        setattr(cls, "FFPE Scrolls",
                PermissibleValue(text="FFPE Scrolls",
                                 description="Formalin Fixed Paraffin Embedded Tissue Scroll") )
        setattr(cls, "Primary Blood Derived Cancer - Bone Marrow",
                PermissibleValue(text="Primary Blood Derived Cancer - Bone Marrow") )
        setattr(cls, "Cell Line Derived Xenograft Tissue",
                PermissibleValue(text="Cell Line Derived Xenograft Tissue") )
        setattr(cls, "Xenograft Tissue",
                PermissibleValue(text="Xenograft Tissue") )
        setattr(cls, "Benign Neoplasms",
                PermissibleValue(text="Benign Neoplasms") )
        setattr(cls, "Blood Derived Liquid Biopsy",
                PermissibleValue(text="Blood Derived Liquid Biopsy") )
        setattr(cls, "Blood Derived Cancer - Bone Marrow",
                PermissibleValue(text="Blood Derived Cancer - Bone Marrow") )
        setattr(cls, "Buccal Cell Normal",
                PermissibleValue(text="Buccal Cell Normal") )
        setattr(cls, "Human Tumor Original Cells",
                PermissibleValue(text="Human Tumor Original Cells") )
        setattr(cls, "Primary Tumor",
                PermissibleValue(text="Primary Tumor",
                                 description="Primary Neoplasm") )
        setattr(cls, "Blood Derived Cancer - Bone Marrow, Post-treatment",
                PermissibleValue(text="Blood Derived Cancer - Bone Marrow, Post-treatment") )
        setattr(cls, "Normal Adjacent Tissue",
                PermissibleValue(text="Normal Adjacent Tissue") )
        setattr(cls, "Blood Derived Cancer - Peripheral Blood",
                PermissibleValue(text="Blood Derived Cancer - Peripheral Blood") )
        setattr(cls, "Recurrent Tumor",
                PermissibleValue(text="Recurrent Tumor") )
        setattr(cls, "Solid Tissue Normal",
                PermissibleValue(text="Solid Tissue Normal") )
        setattr(cls, "Cell Lines",
                PermissibleValue(text="Cell Lines") )
        setattr(cls, "Bone Marrow Normal",
                PermissibleValue(text="Bone Marrow Normal") )
        setattr(cls, "Repli-G X (Qiagen) DNA",
                PermissibleValue(text="Repli-G X (Qiagen) DNA") )
        setattr(cls, "Total RNA",
                PermissibleValue(text="Total RNA") )
        setattr(cls, "GenomePlex (Rubicon) Amplified DNA",
                PermissibleValue(text="GenomePlex (Rubicon) Amplified DNA") )
        setattr(cls, "Blood Derived Cancer - Peripheral Blood, Post-treatment",
                PermissibleValue(text="Blood Derived Cancer - Peripheral Blood, Post-treatment") )
        setattr(cls, "FFPE Recurrent",
                PermissibleValue(text="FFPE Recurrent") )
        setattr(cls, "Primary Xenograft Tissue",
                PermissibleValue(text="Primary Xenograft Tissue") )
        setattr(cls, "Expanded Next Generation Cancer Model",
                PermissibleValue(text="Expanded Next Generation Cancer Model") )
        setattr(cls, "Next Generation Cancer Model",
                PermissibleValue(text="Next Generation Cancer Model") )
        setattr(cls, "Mixed Adherent Suspension",
                PermissibleValue(text="Mixed Adherent Suspension") )

class CCDHSpecimenTumorStatusAtCollection(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenTumorStatusAtCollection",
        description="Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection",
        code_set=None,
        code_set_version="2021-05-30T01:20:53.925059+00:00",
    )

class CCDHSpecimenCellularCompositionType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type
    """
    Granulocytes = PermissibleValue(text="Granulocytes",
                                               description="Granulocyte")
    Cell = PermissibleValue(text="Cell",
                               description="Cell")
    Lymphocytes = PermissibleValue(text="Lymphocytes",
                                             description="Lymphocyte")
    Serum = PermissibleValue(text="Serum",
                                 description="Serum")
    Saliva = PermissibleValue(text="Saliva",
                                   description="Saliva")
    Plasma = PermissibleValue(text="Plasma",
                                   description="Plasma")
    Sputum = PermissibleValue(text="Sputum",
                                   description="Sputum")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="CCDHSpecimenCellularCompositionType",
        description="Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.067118+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Buccal Cells",
                PermissibleValue(text="Buccal Cells",
                                 description="Buccal Cell") )
        setattr(cls, "Adherent Cell Line",
                PermissibleValue(text="Adherent Cell Line") )
        setattr(cls, "3D Organoid",
                PermissibleValue(text="3D Organoid") )
        setattr(cls, "Peripheral Whole Blood",
                PermissibleValue(text="Peripheral Whole Blood",
                                 description="Peripheral Whole Blood") )
        setattr(cls, "Buffy Coat",
                PermissibleValue(text="Buffy Coat",
                                 description="Buffy Coat") )
        setattr(cls, "Human Original Cells",
                PermissibleValue(text="Human Original Cells") )
        setattr(cls, "Bone Marrow Components",
                PermissibleValue(text="Bone Marrow Components",
                                 description="Bone Marrow Component") )
        setattr(cls, "Liquid Suspension Cell Line",
                PermissibleValue(text="Liquid Suspension Cell Line") )
        setattr(cls, "Solid Tissue",
                PermissibleValue(text="Solid Tissue",
                                 description="Solid Tissue") )
        setattr(cls, "Fibroblasts from Bone Marrow Normal",
                PermissibleValue(text="Fibroblasts from Bone Marrow Normal",
                                 description="Normal Bone Marrow Fibroblast") )
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )
        setattr(cls, "3D Neurosphere",
                PermissibleValue(text="3D Neurosphere") )
        setattr(cls, "EBV Immortalized",
                PermissibleValue(text="EBV Immortalized",
                                 description="Epstein-Barr Virus Immortalized") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "Whole Bone Marrow",
                PermissibleValue(text="Whole Bone Marrow",
                                 description="Whole Bone Marrow") )
        setattr(cls, "2D Classical Conditionally Reprogrammed Cells",
                PermissibleValue(text="2D Classical Conditionally Reprogrammed Cells") )
        setattr(cls, "Bone Marrow Components NOS",
                PermissibleValue(text="Bone Marrow Components NOS",
                                 description="Bone Marrow Component Not Otherwise Specified") )
        setattr(cls, "Derived Cell Line",
                PermissibleValue(text="Derived Cell Line",
                                 description="Derived Cell Line") )
        setattr(cls, "Control Analyte",
                PermissibleValue(text="Control Analyte",
                                 description="Control Analyte") )
        setattr(cls, "2D Modified Conditionally Reprogrammed Cells",
                PermissibleValue(text="2D Modified Conditionally Reprogrammed Cells") )
        setattr(cls, "Peripheral Blood Components NOS",
                PermissibleValue(text="Peripheral Blood Components NOS",
                                 description="Peripheral Blood Component Not Otherwise Specified") )
        setattr(cls, "Sorted Cells",
                PermissibleValue(text="Sorted Cells") )
        setattr(cls, "3D Air-Liquid Interface Organoid",
                PermissibleValue(text="3D Air-Liquid Interface Organoid") )
        setattr(cls, "Mononuclear Cells from Bone Marrow Normal",
                PermissibleValue(text="Mononuclear Cells from Bone Marrow Normal",
                                 description="Normal Bone Marrow Monocyte") )
        setattr(cls, "Pleural Effusion",
                PermissibleValue(text="Pleural Effusion",
                                 description="Pleural Fluid") )
        setattr(cls, "Mixed Adherent Suspension",
                PermissibleValue(text="Mixed Adherent Suspension") )

class CCDHSpecimenGeneralTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology
    """
    Peritumoral = PermissibleValue(text="Peritumoral",
                                             description="Peritumoral")
    Normal = PermissibleValue(text="Normal",
                                   description="Normal")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    Abnormal = PermissibleValue(text="Abnormal",
                                       description="Abnormal")
    Tumor = PermissibleValue(text="Tumor",
                                 description="Malignant Neoplasm")

    _defn = EnumDefinition(
        name="CCDHSpecimenGeneralTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.242737+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )

class CCDHSpecimenSpecificTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology
    """
    Rhabdomyosarcoma = PermissibleValue(text="Rhabdomyosarcoma")

    _defn = EnumDefinition(
        name="CCDHSpecimenSpecificTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.391915+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "40",
                PermissibleValue(text="40") )
        setattr(cls, "61",
                PermissibleValue(text="61") )
        setattr(cls, "50",
                PermissibleValue(text="50") )
        setattr(cls, "81",
                PermissibleValue(text="81") )
        setattr(cls, "01",
                PermissibleValue(text="01") )
        setattr(cls, "00",
                PermissibleValue(text="00") )
        setattr(cls, "80",
                PermissibleValue(text="80") )
        setattr(cls, "52",
                PermissibleValue(text="52") )
        setattr(cls, "41",
                PermissibleValue(text="41") )
        setattr(cls, "10",
                PermissibleValue(text="10") )
        setattr(cls, "15",
                PermissibleValue(text="15") )
        setattr(cls, "60",
                PermissibleValue(text="60") )
        setattr(cls, "65",
                PermissibleValue(text="65") )
        setattr(cls, "03",
                PermissibleValue(text="03") )
        setattr(cls, "70",
                PermissibleValue(text="70") )
        setattr(cls, "64",
                PermissibleValue(text="64") )
        setattr(cls, "20",
                PermissibleValue(text="20") )
        setattr(cls, "02",
                PermissibleValue(text="02") )
        setattr(cls, "30",
                PermissibleValue(text="30") )
        setattr(cls, "04",
                PermissibleValue(text="04") )
        setattr(cls, "21",
                PermissibleValue(text="21") )
        setattr(cls, "71",
                PermissibleValue(text="71") )
        setattr(cls, "62",
                PermissibleValue(text="62") )
        setattr(cls, "51",
                PermissibleValue(text="51") )
        setattr(cls, "63",
                PermissibleValue(text="63") )
        setattr(cls, "Anal Cancer (all types)",
                PermissibleValue(text="Anal Cancer (all types)") )
        setattr(cls, "Clear cell sarcoma of the kidney (CCSK)",
                PermissibleValue(text="Clear cell sarcoma of the kidney (CCSK)") )
        setattr(cls, "Acute Leukemia of Ambiguous Lineage (ALAL)",
                PermissibleValue(text="Acute Leukemia of Ambiguous Lineage (ALAL)") )
        setattr(cls, "Lung Cancer (all types)",
                PermissibleValue(text="Lung Cancer (all types)") )
        setattr(cls, "NHL, Burkitt lymphoma (BL)",
                PermissibleValue(text="NHL, Burkitt lymphoma (BL)") )
        setattr(cls, "Osteosarcoma (OS)",
                PermissibleValue(text="Osteosarcoma (OS)") )
        setattr(cls, "Acute myeloid leukemia (AML)",
                PermissibleValue(text="Acute myeloid leukemia (AML)") )
        setattr(cls, "CNS, medulloblastoma",
                PermissibleValue(text="CNS, medulloblastoma") )
        setattr(cls, "Induction Failure AML (AML-IF)",
                PermissibleValue(text="Induction Failure AML (AML-IF)") )
        setattr(cls, "CNS, rhabdoid tumor",
                PermissibleValue(text="CNS, rhabdoid tumor") )
        setattr(cls, "Rhabdoid tumor (kidney) (RT)",
                PermissibleValue(text="Rhabdoid tumor (kidney) (RT)") )
        setattr(cls, "CNS, other",
                PermissibleValue(text="CNS, other") )
        setattr(cls, "Diffuse Large B-Cell Lymphoma (DLBCL)",
                PermissibleValue(text="Diffuse Large B-Cell Lymphoma (DLBCL)") )
        setattr(cls, "CNS, low grade glioma (LGG)",
                PermissibleValue(text="CNS, low grade glioma (LGG)") )
        setattr(cls, "Non cancerous tissue",
                PermissibleValue(text="Non cancerous tissue") )
        setattr(cls, "Acute lymphoblastic leukemia (ALL)",
                PermissibleValue(text="Acute lymphoblastic leukemia (ALL)") )
        setattr(cls, "Neuroblastoma (NBL)",
                PermissibleValue(text="Neuroblastoma (NBL)") )
        setattr(cls, "NHL, anaplastic large cell lymphoma",
                PermissibleValue(text="NHL, anaplastic large cell lymphoma") )
        setattr(cls, "Cervical Cancer (all types)",
                PermissibleValue(text="Cervical Cancer (all types)") )
        setattr(cls, "CNS, ependymoma",
                PermissibleValue(text="CNS, ependymoma") )
        setattr(cls, "Ewing sarcoma",
                PermissibleValue(text="Ewing sarcoma") )
        setattr(cls, "Soft tissue sarcoma, non-rhabdomyosarcoma",
                PermissibleValue(text="Soft tissue sarcoma, non-rhabdomyosarcoma") )
        setattr(cls, "Wilms tumor (WT)",
                PermissibleValue(text="Wilms tumor (WT)") )
        setattr(cls, "CNS, glioblastoma (GBM)",
                PermissibleValue(text="CNS, glioblastoma (GBM)") )

class CCDHSpecimenPreinvasiveTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenPreinvasiveTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.563839+00:00",
    )

class CCDHSpecimenMorphologyAssessorRole(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenMorphologyAssessorRole",
        description="Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.714208+00:00",
    )

class CCDHSpecimenMorphlogyAssessmentMethod(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenMorphlogyAssessmentMethod",
        description="Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.858041+00:00",
    )

class CCDHSpecimenDegreeOfDysplasia(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenDegreeOfDysplasia",
        description="Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia",
        code_set=None,
        code_set_version="2021-05-30T01:20:54.996418+00:00",
    )

class CCDHSpecimenSectionLocation(EnumDefinitionImpl):
    """
    The location in a parent specimen from which a section/portion was excised.
    """
    top = PermissibleValue(text="top",
                             description="The part of a specimen designated as its 'top' based on specified orientation cirteria.")
    unknown = PermissibleValue(text="unknown",
                                     description="An unknown location on a specimen.")
    bottom = PermissibleValue(text="bottom",
                                   description="The part of a specimen designated as its 'bottom' based on specified orientation cirteria.")

    _defn = EnumDefinition(
        name="CCDHSpecimenSectionLocation",
        description="The location in a parent specimen from which a section/portion was excised.",
    )

class CCDHSpecimenContainerContainerType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer container_type
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenContainerContainerType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer container_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:55.293532+00:00",
    )

class CCDHSpecimenContainerChargeType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenContainerChargeType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:55.439251+00:00",
    )

class CCDHSpecimenCreationActivityActivityType(EnumDefinitionImpl):
    """
    The high-level type of activity through which the specimen was generated (i.e. via collection from the original
    source, or via derivation from an existing specimen)
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenCreationActivityActivityType",
        description="The high-level type of activity through which the specimen was generated (i.e. via collection from the original source, or via derivation from an existing specimen)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "collection from source",
                PermissibleValue(text="collection from source",
                                 description="An activity that collects an initial sample directlly from a subject / source.") )
        setattr(cls, "derivation from specimen",
                PermissibleValue(text="derivation from specimen",
                                 description="An activity that derives a new specimen fro an existing one.") )

class CCDHSpecimenCreationActivityCollectionMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type
    """
    Yes = PermissibleValue(text="Yes")
    No = PermissibleValue(text="No")
    Metastasectomy = PermissibleValue(text="Metastasectomy")
    Lumpectomy = PermissibleValue(text="Lumpectomy")
    Salpingectomy = PermissibleValue(text="Salpingectomy")
    Pneumonectomy = PermissibleValue(text="Pneumonectomy")
    Oophorectomy = PermissibleValue(text="Oophorectomy")
    Enucleation = PermissibleValue(text="Enucleation")
    Cystectomy = PermissibleValue(text="Cystectomy")
    Indeterminant = PermissibleValue(text="Indeterminant")
    Lobectomy = PermissibleValue(text="Lobectomy")
    Lymphadenectomy = PermissibleValue(text="Lymphadenectomy")
    Orchiectomy = PermissibleValue(text="Orchiectomy")
    Pancreatectomy = PermissibleValue(text="Pancreatectomy")
    Biopsy = PermissibleValue(text="Biopsy")
    Other = PermissibleValue(text="Other")
    Autopsy = PermissibleValue(text="Autopsy")
    Unknown = PermissibleValue(text="Unknown")
    Aspirate = PermissibleValue(text="Aspirate")
    Paracentesis = PermissibleValue(text="Paracentesis")
    Omentectomy = PermissibleValue(text="Omentectomy")
    Thoracentesis = PermissibleValue(text="Thoracentesis")
    Transplant = PermissibleValue(text="Transplant")
    Tonsillectomy = PermissibleValue(text="Tonsillectomy")
    Maxillectomy = PermissibleValue(text="Maxillectomy")
    Palatectomy = PermissibleValue(text="Palatectomy")
    Mandibulectomy = PermissibleValue(text="Mandibulectomy")
    Glossectomy = PermissibleValue(text="Glossectomy")
    Laryngopharyngectomy = PermissibleValue(text="Laryngopharyngectomy")

    _defn = EnumDefinition(
        name="CCDHSpecimenCreationActivityCollectionMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:55.721149+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Incisional Biopsy",
                PermissibleValue(text="Incisional Biopsy") )
        setattr(cls, "Hysterectomy NOS",
                PermissibleValue(text="Hysterectomy NOS") )
        setattr(cls, "Abdomino-perineal Resection of Rectum",
                PermissibleValue(text="Abdomino-perineal Resection of Rectum") )
        setattr(cls, "Endoscopic Biopsy",
                PermissibleValue(text="Endoscopic Biopsy") )
        setattr(cls, "Gross Total Resection",
                PermissibleValue(text="Gross Total Resection") )
        setattr(cls, "Wedge Resection",
                PermissibleValue(text="Wedge Resection") )
        setattr(cls, "Blood Draw",
                PermissibleValue(text="Blood Draw") )
        setattr(cls, "Endo Rectal Tumor Resection",
                PermissibleValue(text="Endo Rectal Tumor Resection") )
        setattr(cls, "Open Radical Prostatectomy",
                PermissibleValue(text="Open Radical Prostatectomy") )
        setattr(cls, "Laparoscopic Biopsy",
                PermissibleValue(text="Laparoscopic Biopsy") )
        setattr(cls, "Other Surgical Resection",
                PermissibleValue(text="Other Surgical Resection") )
        setattr(cls, "Fine Needle Aspiration",
                PermissibleValue(text="Fine Needle Aspiration") )
        setattr(cls, "Open Craniotomy",
                PermissibleValue(text="Open Craniotomy") )
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )
        setattr(cls, "Thoracoscopic Biopsy",
                PermissibleValue(text="Thoracoscopic Biopsy") )
        setattr(cls, "Total Colectomy",
                PermissibleValue(text="Total Colectomy") )
        setattr(cls, "Core Biopsy",
                PermissibleValue(text="Core Biopsy") )
        setattr(cls, "Bone Marrow Aspirate",
                PermissibleValue(text="Bone Marrow Aspirate") )
        setattr(cls, "Simple Mastectomy",
                PermissibleValue(text="Simple Mastectomy") )
        setattr(cls, "Tumor Debulking",
                PermissibleValue(text="Tumor Debulking") )
        setattr(cls, "Partial Hepatectomy",
                PermissibleValue(text="Partial Hepatectomy") )
        setattr(cls, "Ascites Drainage",
                PermissibleValue(text="Ascites Drainage") )
        setattr(cls, "Laparoscopic Radical Prostatectomy with Robotics",
                PermissibleValue(text="Laparoscopic Radical Prostatectomy with Robotics") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "Salpingo-oophorectomy",
                PermissibleValue(text="Salpingo-oophorectomy") )
        setattr(cls, "Right Hemicolectomy",
                PermissibleValue(text="Right Hemicolectomy") )
        setattr(cls, "Supracervical Hysterectomy",
                PermissibleValue(text="Supracervical Hysterectomy") )
        setattr(cls, "Total Mastectomy",
                PermissibleValue(text="Total Mastectomy") )
        setattr(cls, "Surgical Resection",
                PermissibleValue(text="Surgical Resection") )
        setattr(cls, "Laparoscopic Radical Prostatectomy without Robotics",
                PermissibleValue(text="Laparoscopic Radical Prostatectomy without Robotics") )
        setattr(cls, "Simple Hysterectomy",
                PermissibleValue(text="Simple Hysterectomy") )
        setattr(cls, "Punch Biopsy",
                PermissibleValue(text="Punch Biopsy") )
        setattr(cls, "Full Hysterectomy",
                PermissibleValue(text="Full Hysterectomy") )
        setattr(cls, "Open Radical Nephrectomy",
                PermissibleValue(text="Open Radical Nephrectomy") )
        setattr(cls, "Endoscopic Mucosal Resection (EMR)",
                PermissibleValue(text="Endoscopic Mucosal Resection (EMR)") )
        setattr(cls, "Liquid Biopsy",
                PermissibleValue(text="Liquid Biopsy") )
        setattr(cls, "Excisional Biopsy",
                PermissibleValue(text="Excisional Biopsy") )
        setattr(cls, "Laparoscopic Partial Nephrectomy",
                PermissibleValue(text="Laparoscopic Partial Nephrectomy") )
        setattr(cls, "Anterior Resection of Rectum",
                PermissibleValue(text="Anterior Resection of Rectum") )
        setattr(cls, "Transverse Colectomy",
                PermissibleValue(text="Transverse Colectomy") )
        setattr(cls, "Laparoscopic Radical Nephrectomy",
                PermissibleValue(text="Laparoscopic Radical Nephrectomy") )
        setattr(cls, "Transurethral resection (TURBT)",
                PermissibleValue(text="Transurethral resection (TURBT)") )
        setattr(cls, "Subtotal Resection",
                PermissibleValue(text="Subtotal Resection") )
        setattr(cls, "Pan-Procto Colectomy",
                PermissibleValue(text="Pan-Procto Colectomy") )
        setattr(cls, "Sigmoid Colectomy",
                PermissibleValue(text="Sigmoid Colectomy") )
        setattr(cls, "Radical Hysterectomy",
                PermissibleValue(text="Radical Hysterectomy") )
        setattr(cls, "Tumor Resection",
                PermissibleValue(text="Tumor Resection") )
        setattr(cls, "Left Hemicolectomy",
                PermissibleValue(text="Left Hemicolectomy") )
        setattr(cls, "Local Resection (Exoresection; wall resection)",
                PermissibleValue(text="Local Resection (Exoresection; wall resection)") )
        setattr(cls, "Total Hepatectomy",
                PermissibleValue(text="Total Hepatectomy") )
        setattr(cls, "Whipple Procedure",
                PermissibleValue(text="Whipple Procedure") )
        setattr(cls, "Needle Biopsy",
                PermissibleValue(text="Needle Biopsy") )
        setattr(cls, "Peritoneal Lavage",
                PermissibleValue(text="Peritoneal Lavage") )
        setattr(cls, "Hand Assisted Laparoscopic Radical Nephrectomy",
                PermissibleValue(text="Hand Assisted Laparoscopic Radical Nephrectomy") )
        setattr(cls, "Modified Radical Mastectomy",
                PermissibleValue(text="Modified Radical Mastectomy") )
        setattr(cls, "Open Partial Nephrectomy",
                PermissibleValue(text="Open Partial Nephrectomy") )
        setattr(cls, "Buccal Mucosal Resection",
                PermissibleValue(text="Buccal Mucosal Resection") )
        setattr(cls, "Vertical Hemilaryngectomy",
                PermissibleValue(text="Vertical Hemilaryngectomy") )
        setattr(cls, "Radical Maxillectomy",
                PermissibleValue(text="Radical Maxillectomy") )
        setattr(cls, "Transoral Laser Excision",
                PermissibleValue(text="Transoral Laser Excision") )
        setattr(cls, "Radical Prostatectomy",
                PermissibleValue(text="Radical Prostatectomy") )
        setattr(cls, "Supraglottic Laryngectomy",
                PermissibleValue(text="Supraglottic Laryngectomy") )
        setattr(cls, "Endolaryngeal Excision",
                PermissibleValue(text="Endolaryngeal Excision") )
        setattr(cls, "Superficial Parotidectomy",
                PermissibleValue(text="Superficial Parotidectomy") )
        setattr(cls, "Total Nephrectomy",
                PermissibleValue(text="Total Nephrectomy") )
        setattr(cls, "Lymph Node Dissection",
                PermissibleValue(text="Lymph Node Dissection") )
        setattr(cls, "Partial Laryngectomy",
                PermissibleValue(text="Partial Laryngectomy") )
        setattr(cls, "Subtotal Prostatectomy",
                PermissibleValue(text="Subtotal Prostatectomy") )
        setattr(cls, "Transurethral Resection (TURP)",
                PermissibleValue(text="Transurethral Resection (TURP)") )
        setattr(cls, "Supracricoid Laryngectomy",
                PermissibleValue(text="Supracricoid Laryngectomy") )
        setattr(cls, "Radical Nephrectomy",
                PermissibleValue(text="Radical Nephrectomy") )
        setattr(cls, "Partial Nephrectomy",
                PermissibleValue(text="Partial Nephrectomy") )
        setattr(cls, "Deep Parotidectomy",
                PermissibleValue(text="Deep Parotidectomy") )
        setattr(cls, "Total Laryngectomy",
                PermissibleValue(text="Total Laryngectomy") )
        setattr(cls, "Partial Maxillectomy",
                PermissibleValue(text="Partial Maxillectomy") )
        setattr(cls, "Parotidectomy, NOS",
                PermissibleValue(text="Parotidectomy, NOS") )

class CCDHSpecimenCreationActivityDerivationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenCreationActivityDerivationMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:55.922818+00:00",
    )

class CCDHSpecimenQuantityObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation category
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenQuantityObservationCategory",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:56.063919+00:00",
    )

class CCDHSpecimenQuantityObservationObservationType(EnumDefinitionImpl):
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
        name="CCDHSpecimenQuantityObservationObservationType",
        description="Measures related to the quantity of a specimen or analyte it currently contains - e.g. its weight, volume, or concentration.",
    )

class CCDHSpecimenQuantityObservationMethodType(EnumDefinitionImpl):
    """
    A type of method used in determining the quantity of a specimen.
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenQuantityObservationMethodType",
        description="A type of method used in determining the quantity of a specimen.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UV Spec",
                PermissibleValue(text="UV Spec",
                                 description="A technique used to measure light absorbance across the ultraviolet and visible ranges of the electromagnetic spectrum.") )
        setattr(cls, "Pico Green",
                PermissibleValue(text="Pico Green",
                                 description="A technique applygin the Pico488 fluoresent sensor dye that is used for quantifying the amount of double-stranded DNA (dsDNA) present in a given sample.") )

class CCDHSpecimenQuantityObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenQuantityObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:56.500435+00:00",
    )

class CCDHSpecimenQualityObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQualityObservation category
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenQualityObservationCategory",
        description="Autogenerated Enumeration for CRDC-H SpecimenQualityObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:56.648843+00:00",
    )

class CCDHSpecimenQualityObservationObservationType(EnumDefinitionImpl):
    """
    Types of measurements that reflect the quality of a specimen or its suitability for use.
    """
    ribosomal_rna_28s_16s_ratio = PermissibleValue(text="ribosomal_rna_28s_16s_ratio")

    _defn = EnumDefinition(
        name="CCDHSpecimenQualityObservationObservationType",
        description="Types of measurements that reflect the quality of a specimen or its suitability for use.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "a260_a280_ratio  ",
                PermissibleValue(text="a260_a280_ratio  ") )

class CCDHSpecimenQualityObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQualityObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenQualityObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenQualityObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:56.932163+00:00",
    )

class CCDHSpecimenProcessingActivityActivityType(EnumDefinitionImpl):
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
        name="CCDHSpecimenProcessingActivityActivityType",
        description="The high-level type of processing activity performed.",
    )

class CCDHSpecimenProcessingActivityMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type
    """
    OCT = PermissibleValue(text="OCT",
                             description="Optimal Cutting Temperature Compound")
    Cryopreserved = PermissibleValue(text="Cryopreserved",
                                                 description="Cryopreservation")
    FFPE = PermissibleValue(text="FFPE",
                               description="Formalin-Fixed Paraffin-Embedded")
    Frozen = PermissibleValue(text="Frozen",
                                   description="Frozen Specimen")
    Unknown = PermissibleValue(text="Unknown")
    Fresh = PermissibleValue(text="Fresh",
                                 description="Fresh Specimen")
    false = PermissibleValue(text="false")
    true = PermissibleValue(text="true")

    _defn = EnumDefinition(
        name="CCDHSpecimenProcessingActivityMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:57.214920+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed To Collect",
                PermissibleValue(text="Not Allowed To Collect") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported") )
        setattr(cls, "Snap Frozen",
                PermissibleValue(text="Snap Frozen",
                                 description="Quick Freeze") )

class CCDHSpecimenStorageActivityMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type
    """
    _defn = EnumDefinition(
        name="CCDHSpecimenStorageActivityMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:57.367033+00:00",
    )

class CCDHSubjectSpecies(EnumDefinitionImpl):
    """
    The scientific binomial name for the species of the subject
    """
    _defn = EnumDefinition(
        name="CCDHSubjectSpecies",
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

class CCDHSubjectBreed(EnumDefinitionImpl):
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
        name="CCDHSubjectBreed",
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

class CCDHSubjectSex(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject sex
    """
    unspecified = PermissibleValue(text="unspecified")
    unknown = PermissibleValue(text="unknown")
    male = PermissibleValue(text="male")
    female = PermissibleValue(text="female")

    _defn = EnumDefinition(
        name="CCDHSubjectSex",
        description="Autogenerated Enumeration for CRDC-H Subject sex",
        code_set=None,
        code_set_version="2021-05-30T01:20:57.815308+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not reported",
                PermissibleValue(text="not reported") )

class CCDHSubjectEthnicity(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject ethnicity
    """
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="CCDHSubjectEthnicity",
        description="Autogenerated Enumeration for CRDC-H Subject ethnicity",
        code_set=None,
        code_set_version="2021-05-30T01:20:57.967504+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not reported",
                PermissibleValue(text="not reported") )
        setattr(cls, "not hispanic or latino",
                PermissibleValue(text="not hispanic or latino") )
        setattr(cls, "not allowed to collect",
                PermissibleValue(text="not allowed to collect") )
        setattr(cls, "hispanic or latino",
                PermissibleValue(text="hispanic or latino") )

class CCDHSubjectRace(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject race
    """
    other = PermissibleValue(text="other")
    white = PermissibleValue(text="white")
    asian = PermissibleValue(text="asian")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="CCDHSubjectRace",
        description="Autogenerated Enumeration for CRDC-H Subject race",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.127612+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "american indian or alaska native",
                PermissibleValue(text="american indian or alaska native") )
        setattr(cls, "native hawaiian or other pacific islander",
                PermissibleValue(text="native hawaiian or other pacific islander") )
        setattr(cls, "not reported",
                PermissibleValue(text="not reported") )
        setattr(cls, "black or african american",
                PermissibleValue(text="black or african american") )
        setattr(cls, "not allowed to collect",
                PermissibleValue(text="not allowed to collect") )

class CCDHSubjectVitalStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject vital_status
    """
    Alive = PermissibleValue(text="Alive",
                                 description="ALIVE")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")
    Dead = PermissibleValue(text="Dead",
                               description="DEAD")

    _defn = EnumDefinition(
        name="CCDHSubjectVitalStatus",
        description="Autogenerated Enumeration for CRDC-H Subject vital_status",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.285053+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not Reported") )

class CCDHSubjectCauseOfDeath(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject cause_of_death
    """
    Toxicity = PermissibleValue(text="Toxicity",
                                       description="Toxicity")
    Infection = PermissibleValue(text="Infection",
                                         description="Infection")
    Unknown = PermissibleValue(text="Unknown",
                                     description="Unknown")

    _defn = EnumDefinition(
        name="CCDHSubjectCauseOfDeath",
        description="Autogenerated Enumeration for CRDC-H Subject cause_of_death",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.425159+00:00",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Cancer Related",
                PermissibleValue(text="Not Cancer Related") )
        setattr(cls, "End-stage Renal Disease",
                PermissibleValue(text="End-stage Renal Disease",
                                 description="Chronic Kidney Disease, Stage 5") )
        setattr(cls, "Spinal Muscular Atrophy",
                PermissibleValue(text="Spinal Muscular Atrophy",
                                 description="Spinal Muscular Atrophy") )
        setattr(cls, "Cancer Related",
                PermissibleValue(text="Cancer Related") )
        setattr(cls, "Surgical Complications",
                PermissibleValue(text="Surgical Complications",
                                 description="Surgical Procedure Complication") )
        setattr(cls, "Not Reported",
                PermissibleValue(text="Not Reported",
                                 description="Not Reported") )
        setattr(cls, "Renal Disorder, NOS",
                PermissibleValue(text="Renal Disorder, NOS",
                                 description="Renal Disorder, NOS") )
        setattr(cls, "Cardiovascular Disorder, NOS",
                PermissibleValue(text="Cardiovascular Disorder, NOS",
                                 description="Cardiovascular Disorder, NOS") )

class CCDHSubstanceSubstanceType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance substance_type
    """
    _defn = EnumDefinition(
        name="CCDHSubstanceSubstanceType",
        description="Autogenerated Enumeration for CRDC-H Substance substance_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.580008+00:00",
    )

class CCDHSubstanceRole(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance role
    """
    _defn = EnumDefinition(
        name="CCDHSubstanceRole",
        description="Autogenerated Enumeration for CRDC-H Substance role",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.724324+00:00",
    )

class CCDHTimePointEventType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TimePoint eventType
    """
    _defn = EnumDefinition(
        name="CCDHTimePointEventType",
        description="Autogenerated Enumeration for CRDC-H TimePoint eventType",
        code_set=None,
        code_set_version="2021-05-30T01:20:58.867391+00:00",
    )

class CCDHTobaccoExposureObservationCategory(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation category
    """
    _defn = EnumDefinition(
        name="CCDHTobaccoExposureObservationCategory",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation category",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.015986+00:00",
    )

class CCDHTobaccoExposureObservationObservationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation observation_type
    """
    _defn = EnumDefinition(
        name="CCDHTobaccoExposureObservationObservationType",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation observation_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.158695+00:00",
    )

class CCDHTobaccoExposureObservationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="CCDHTobaccoExposureObservationMethodType",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.298209+00:00",
    )

class CCDHTobaccoExposureObservationValueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="CCDHTobaccoExposureObservationValueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.445886+00:00",
    )

class CCDHTreatmentRegimen(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment regimen
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentRegimen",
        description="Autogenerated Enumeration for CRDC-H Treatment regimen",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.589524+00:00",
    )

class CCDHTreatmentTreatmentEffect(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_effect
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentEffect",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_effect",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.733652+00:00",
    )

class CCDHTreatmentTreatmentIntent(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_intent
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentIntent",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_intent",
        code_set=None,
        code_set_version="2021-05-30T01:20:59.876966+00:00",
    )

class CCDHTreatmentTreatmentOutcome(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_outcome
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentOutcome",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_outcome",
        code_set=None,
        code_set_version="2021-05-30T01:21:00.016307+00:00",
    )

class CCDHTreatmentTreatmentType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_type
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentType",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_type",
        code_set=None,
        code_set_version="2021-05-30T01:21:00.199560+00:00",
    )

class CCDHTreatmentTreatmentFrequency(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_frequency
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentFrequency",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_frequency",
        code_set=None,
        code_set_version="2021-05-30T01:21:00.343474+00:00",
    )

class CCDHTreatmentTreatmentEndReason(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment treatment_end_reason
    """
    _defn = EnumDefinition(
        name="CCDHTreatmentTreatmentEndReason",
        description="Autogenerated Enumeration for CRDC-H Treatment treatment_end_reason",
        code_set=None,
        code_set_version="2021-05-30T01:21:00.486735+00:00",
    )

class CCDHHistologicalCompositionObservationObservationType(EnumDefinitionImpl):
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
                                                                             description="Numeric value to represent local response to cellular injury, marked by capillary dilatation, edema and leukocyte infiltration; clinically, inflammation is manifest by reddness, heat, pain, swelling and loss of function, with the need to heal damaged tissue.")
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
        name="CCDHHistologicalCompositionObservationObservationType",
        description="Types of measurements that describe microscopic characteristics of a specimen - typically related to its cellular and tissue composition.",
    )

class CCDHExecutionTimeObservation(EnumDefinitionImpl):
    """
    Types of observations about the duration of specific aspects / parts of an activity.
    """
    time_between_excision_and_freezing = PermissibleValue(text="time_between_excision_and_freezing",
                                                                                           description="The elapsed time between the excision and freezing of the specimen from its subject/source.")
    time_between_clamping_and_freezing = PermissibleValue(text="time_between_clamping_and_freezing",
                                                                                           description="The elapsed time between the clamping of blood supply and freezing of the specimen from its subject/source.")
    ischemic_time = PermissibleValue(text="ischemic_time",
                                                 description="Duration of time, in seconds, between when the specimen stopped receiving oxygen and when it was preserved or processed.")

    _defn = EnumDefinition(
        name="CCDHExecutionTimeObservation",
        description="Types of observations about the duration of specific aspects / parts of an activity.",
    )

class CCDHExecutionConditionObservation(EnumDefinitionImpl):
    """
    Types of observations about the environmental conditions under which specific aspects of an activity were
    performed.
    """
    ischemic_temperature = PermissibleValue(text="ischemic_temperature",
                                                               description="A term describing the temperature of a specimen when it experienced ischemia.")

    _defn = EnumDefinition(
        name="CCDHExecutionConditionObservation",
        description="Types of observations about the environmental conditions under which specific aspects of an activity were performed.",
    )

class CCDHTobbaccoExposureObservationObservationType(EnumDefinitionImpl):
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
                                                         description="The text term used to generally decribe how often the patient smokes.")
    time_between_waking_and_first_smoke = PermissibleValue(text="time_between_waking_and_first_smoke",
                                                                                             description="The text term used to describe the approximate amount of time elapsed between the time the patient wakes up in the morning to the time they smoke their first cigarette.")
    environmental_tobacco_smoke_exposure = PermissibleValue(text="environmental_tobacco_smoke_exposure",
                                                                                               description="The yes/no/unknown indicator used to describe whether a patient was exposed to smoke that is emitted from burning tobacco, including cigarettes, pipes, and cigars. This includes tobacco smoke exhaled by smokers.")
    tobacco_smoking_status = PermissibleValue(text="tobacco_smoking_status",
                                                                   description="Category describing current smoking status and smoking history as self-reported by a patient.")
    type_of_tobacco_used = PermissibleValue(text="type_of_tobacco_used",
                                                               description="The text term used to describe the specific type of tobacco used by the patient.")

    _defn = EnumDefinition(
        name="CCDHTobbaccoExposureObservationObservationType",
        description="Types of observations about a Subject's exposure to or use of tobacco.",
    )

class CCDHSubstanceRole(EnumDefinitionImpl):
    """
    A role played by the substance in a particular applicaton (e.g. the role of a lysis buffer when applied in a
    specimen creation activity, or the role of fixative when applied in specimen processing)
    """
    fixative = PermissibleValue(text="fixative",
                                       description="A substance applied preserve biological tissues from decay due to autolysis or putrefaction")

    _defn = EnumDefinition(
        name="CCDHSubstanceRole",
        description="A role played by the substance in a particular applicaton (e.g. the role of a lysis buffer when applied in a specimen creation activity, or the role of fixative when applied in specimen processing)",
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

# Slots
class slots:
    pass

slots.alcoholExposureObservation__id = Slot(uri=CCDH.id, name="alcoholExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.alcoholExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.alcoholExposureObservation__category = Slot(uri=CCDH.category, name="alcoholExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.alcoholExposureObservation__category, domain=None, range=Optional[Union[str, "CCDHAlcoholExposureObservationCategory"]])

slots.alcoholExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="alcoholExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.alcoholExposureObservation__observation_type, domain=None, range=Union[str, "CCDHAlcoholExposureObservationObservationType"])

slots.alcoholExposureObservation__method_type = Slot(uri=CCDH.method_type, name="alcoholExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.alcoholExposureObservation__method_type, domain=None, range=Optional[Union[str, "CCDHAlcoholExposureObservationMethodType"]])

slots.alcoholExposureObservation__focus = Slot(uri=CCDH.focus, name="alcoholExposureObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.alcoholExposureObservation__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.alcoholExposureObservation__subject = Slot(uri=CCDH.subject, name="alcoholExposureObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.alcoholExposureObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.alcoholExposureObservation__performed_by = Slot(uri=CCDH.performed_by, name="alcoholExposureObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.alcoholExposureObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.alcoholExposureObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="alcoholExposureObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.alcoholExposureObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.alcoholExposureObservation__valueString = Slot(uri=CCDH.valueString, name="alcoholExposureObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.alcoholExposureObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.alcoholExposureObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="alcoholExposureObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.alcoholExposureObservation__valueInteger, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.alcoholExposureObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="alcoholExposureObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.alcoholExposureObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.alcoholExposureObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="alcoholExposureObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.alcoholExposureObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.alcoholExposureObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="alcoholExposureObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.alcoholExposureObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.alcoholExposureObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="alcoholExposureObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.alcoholExposureObservation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.alcoholExposureObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="alcoholExposureObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.alcoholExposureObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHAlcoholExposureObservationValueCodeableConcept"]])

slots.bodySite__site = Slot(uri=CCDH.site, name="bodySite__site", curie=CCDH.curie('site'),
                   model_uri=CCDH.bodySite__site, domain=None, range=Union[str, "CCDHBodySiteSite"])

slots.bodySite__qualifier = Slot(uri=CCDH.qualifier, name="bodySite__qualifier", curie=CCDH.curie('qualifier'),
                   model_uri=CCDH.bodySite__qualifier, domain=None, range=Optional[Union[Union[str, "CCDHBodySiteQualifier"], List[Union[str, "CCDHBodySiteQualifier"]]]])

slots.biologicProduct__id = Slot(uri=CCDH.id, name="biologicProduct__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.biologicProduct__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicProduct__identifier = Slot(uri=CCDH.identifier, name="biologicProduct__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.biologicProduct__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.biologicProduct__description = Slot(uri=CCDH.description, name="biologicProduct__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.biologicProduct__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.biologicProduct__product_type = Slot(uri=CCDH.product_type, name="biologicProduct__product_type", curie=CCDH.curie('product_type'),
                   model_uri=CCDH.biologicProduct__product_type, domain=None, range=Optional[Union[str, "CCDHBiologicProductProductType"]])

slots.biologicProduct__passage_number = Slot(uri=CCDH.passage_number, name="biologicProduct__passage_number", curie=CCDH.curie('passage_number'),
                   model_uri=CCDH.biologicProduct__passage_number, domain=None, range=Optional[Union[Union[int, CcdhInteger], List[Union[int, CcdhInteger]]]])

slots.biologicProduct__growth_rate = Slot(uri=CCDH.growth_rate, name="biologicProduct__growth_rate", curie=CCDH.curie('growth_rate'),
                   model_uri=CCDH.biologicProduct__growth_rate, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.cancerGradeObservation__id = Slot(uri=CCDH.id, name="cancerGradeObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerGradeObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerGradeObservation__category = Slot(uri=CCDH.category, name="cancerGradeObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerGradeObservation__category, domain=None, range=Optional[Union[str, "CCDHCancerGradeObservationCategory"]])

slots.cancerGradeObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerGradeObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerGradeObservation__observation_type, domain=None, range=Union[str, "CCDHCancerGradeObservationObservationType"])

slots.cancerGradeObservation__method_type = Slot(uri=CCDH.method_type, name="cancerGradeObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGradeObservation__method_type, domain=None, range=Optional[Union[str, "CCDHCancerGradeObservationMethodType"]])

slots.cancerGradeObservation__focus = Slot(uri=CCDH.focus, name="cancerGradeObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerGradeObservation__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.cancerGradeObservation__subject = Slot(uri=CCDH.subject, name="cancerGradeObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerGradeObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerGradeObservation__performed_by = Slot(uri=CCDH.performed_by, name="cancerGradeObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.cancerGradeObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.cancerGradeObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="cancerGradeObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.cancerGradeObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.cancerGradeObservation__valueString = Slot(uri=CCDH.valueString, name="cancerGradeObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.cancerGradeObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerGradeObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="cancerGradeObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.cancerGradeObservation__valueInteger, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.cancerGradeObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="cancerGradeObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.cancerGradeObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.cancerGradeObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="cancerGradeObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.cancerGradeObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.cancerGradeObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="cancerGradeObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.cancerGradeObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.cancerGradeObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="cancerGradeObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.cancerGradeObservation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.cancerGradeObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="cancerGradeObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.cancerGradeObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHCancerGradeObservationValueCodeableConcept"]])

slots.cancerGradeObservationSet__id = Slot(uri=CCDH.id, name="cancerGradeObservationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerGradeObservationSet__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerGradeObservationSet__category = Slot(uri=CCDH.category, name="cancerGradeObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerGradeObservationSet__category, domain=None, range=Optional[Union[str, "CCDHCancerGradeObservationSetCategory"]])

slots.cancerGradeObservationSet__focus = Slot(uri=CCDH.focus, name="cancerGradeObservationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerGradeObservationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.cancerGradeObservationSet__subject = Slot(uri=CCDH.subject, name="cancerGradeObservationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerGradeObservationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerGradeObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerGradeObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGradeObservationSet__method_type, domain=None, range=Optional[Union[Union[str, "CCDHCancerGradeObservationSetMethodType"], List[Union[str, "CCDHCancerGradeObservationSetMethodType"]]]])

slots.cancerGradeObservationSet__performed_by = Slot(uri=CCDH.performed_by, name="cancerGradeObservationSet__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.cancerGradeObservationSet__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.cancerGradeObservationSet__observations = Slot(uri=CCDH.observations, name="cancerGradeObservationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerGradeObservationSet__observations, domain=None, range=Optional[Union[Union[dict, CancerGradeObservation], List[Union[dict, CancerGradeObservation]]]])

slots.cancerStageObservation__id = Slot(uri=CCDH.id, name="cancerStageObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerStageObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerStageObservation__category = Slot(uri=CCDH.category, name="cancerStageObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerStageObservation__category, domain=None, range=Optional[Union[str, "CCDHCancerStageObservationCategory"]])

slots.cancerStageObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerStageObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerStageObservation__observation_type, domain=None, range=Union[str, "CCDHCancerStageObservationObservationType"])

slots.cancerStageObservation__method_type = Slot(uri=CCDH.method_type, name="cancerStageObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageObservation__method_type, domain=None, range=Optional[Union[str, "CCDHCancerStageObservationMethodType"]])

slots.cancerStageObservation__focus = Slot(uri=CCDH.focus, name="cancerStageObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerStageObservation__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.cancerStageObservation__subject = Slot(uri=CCDH.subject, name="cancerStageObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerStageObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerStageObservation__performed_by = Slot(uri=CCDH.performed_by, name="cancerStageObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.cancerStageObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.cancerStageObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="cancerStageObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.cancerStageObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.cancerStageObservation__valueString = Slot(uri=CCDH.valueString, name="cancerStageObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.cancerStageObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerStageObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="cancerStageObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.cancerStageObservation__valueInteger, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.cancerStageObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="cancerStageObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.cancerStageObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.cancerStageObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="cancerStageObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.cancerStageObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.cancerStageObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="cancerStageObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.cancerStageObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.cancerStageObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="cancerStageObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.cancerStageObservation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.cancerStageObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="cancerStageObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.cancerStageObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHCancerStageObservationValueCodeableConcept"]])

slots.cancerStageObservationSet__id = Slot(uri=CCDH.id, name="cancerStageObservationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerStageObservationSet__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerStageObservationSet__category = Slot(uri=CCDH.category, name="cancerStageObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerStageObservationSet__category, domain=None, range=Optional[Union[str, "CCDHCancerStageObservationSetCategory"]])

slots.cancerStageObservationSet__focus = Slot(uri=CCDH.focus, name="cancerStageObservationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerStageObservationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.cancerStageObservationSet__subject = Slot(uri=CCDH.subject, name="cancerStageObservationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerStageObservationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerStageObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerStageObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageObservationSet__method_type, domain=None, range=Optional[Union[Union[str, "CCDHCancerStageObservationSetMethodType"], List[Union[str, "CCDHCancerStageObservationSetMethodType"]]]])

slots.cancerStageObservationSet__performed_by = Slot(uri=CCDH.performed_by, name="cancerStageObservationSet__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.cancerStageObservationSet__performed_by, domain=None, range=Optional[Union[dict, Organization]])

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

slots.diagnosis__subject = Slot(uri=CCDH.subject, name="diagnosis__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.diagnosis__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.diagnosis__age_at_diagnosis = Slot(uri=CCDH.age_at_diagnosis, name="diagnosis__age_at_diagnosis", curie=CCDH.curie('age_at_diagnosis'),
                   model_uri=CCDH.diagnosis__age_at_diagnosis, domain=None, range=Optional[Union[dict, Quantity]])

slots.diagnosis__year_at_diagnosis = Slot(uri=CCDH.year_at_diagnosis, name="diagnosis__year_at_diagnosis", curie=CCDH.curie('year_at_diagnosis'),
                   model_uri=CCDH.diagnosis__year_at_diagnosis, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.diagnosis__condition = Slot(uri=CCDH.condition, name="diagnosis__condition", curie=CCDH.curie('condition'),
                   model_uri=CCDH.diagnosis__condition, domain=None, range=Optional[Union[str, "CCDHDiagnosisCondition"]])

slots.diagnosis__primary_site = Slot(uri=CCDH.primary_site, name="diagnosis__primary_site", curie=CCDH.curie('primary_site'),
                   model_uri=CCDH.diagnosis__primary_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__metastatic_site = Slot(uri=CCDH.metastatic_site, name="diagnosis__metastatic_site", curie=CCDH.curie('metastatic_site'),
                   model_uri=CCDH.diagnosis__metastatic_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.diagnosis__stage = Slot(uri=CCDH.stage, name="diagnosis__stage", curie=CCDH.curie('stage'),
                   model_uri=CCDH.diagnosis__stage, domain=None, range=Optional[Union[Union[dict, CancerStageObservationSet], List[Union[dict, CancerStageObservationSet]]]])

slots.diagnosis__grade = Slot(uri=CCDH.grade, name="diagnosis__grade", curie=CCDH.curie('grade'),
                   model_uri=CCDH.diagnosis__grade, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.diagnosis__morphology = Slot(uri=CCDH.morphology, name="diagnosis__morphology", curie=CCDH.curie('morphology'),
                   model_uri=CCDH.diagnosis__morphology, domain=None, range=Optional[Union[str, "CCDHDiagnosisMorphology"]])

slots.diagnosis__disease_status = Slot(uri=CCDH.disease_status, name="diagnosis__disease_status", curie=CCDH.curie('disease_status'),
                   model_uri=CCDH.diagnosis__disease_status, domain=None, range=Optional[Union[str, "CCDHDiagnosisDiseaseStatus"]])

slots.diagnosis__prior_diagnosis = Slot(uri=CCDH.prior_diagnosis, name="diagnosis__prior_diagnosis", curie=CCDH.curie('prior_diagnosis'),
                   model_uri=CCDH.diagnosis__prior_diagnosis, domain=None, range=Optional[Union[dict, Diagnosis]])

slots.diagnosis__method_of_diagnosis = Slot(uri=CCDH.method_of_diagnosis, name="diagnosis__method_of_diagnosis", curie=CCDH.curie('method_of_diagnosis'),
                   model_uri=CCDH.diagnosis__method_of_diagnosis, domain=None, range=Optional[Union[str, "CCDHDiagnosisMethodOfDiagnosis"]])

slots.diagnosis__related_specimen = Slot(uri=CCDH.related_specimen, name="diagnosis__related_specimen", curie=CCDH.curie('related_specimen'),
                   model_uri=CCDH.diagnosis__related_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.diagnosis__supporting_observations = Slot(uri=CCDH.supporting_observations, name="diagnosis__supporting_observations", curie=CCDH.curie('supporting_observations'),
                   model_uri=CCDH.diagnosis__supporting_observations, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.dimensionalObservation__id = Slot(uri=CCDH.id, name="dimensionalObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.dimensionalObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.dimensionalObservation__category = Slot(uri=CCDH.category, name="dimensionalObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.dimensionalObservation__category, domain=None, range=Optional[Union[str, "CCDHDimensionalObservationCategory"]])

slots.dimensionalObservation__observation_type = Slot(uri=CCDH.observation_type, name="dimensionalObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.dimensionalObservation__observation_type, domain=None, range=Union[str, "CCDHDimensionalObservationObservationType"])

slots.dimensionalObservation__method_type = Slot(uri=CCDH.method_type, name="dimensionalObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.dimensionalObservation__method_type, domain=None, range=Optional[Union[Union[str, "CCDHDimensionalObservationMethodType"], List[Union[str, "CCDHDimensionalObservationMethodType"]]]])

slots.dimensionalObservation__focus = Slot(uri=CCDH.focus, name="dimensionalObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.dimensionalObservation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.dimensionalObservation__subject = Slot(uri=CCDH.subject, name="dimensionalObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.dimensionalObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.dimensionalObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="dimensionalObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.dimensionalObservation__valueQuantity, domain=None, range=Union[dict, Quantity])

slots.dimensionalObservationSet__id = Slot(uri=CCDH.id, name="dimensionalObservationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.dimensionalObservationSet__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.dimensionalObservationSet__category = Slot(uri=CCDH.category, name="dimensionalObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.dimensionalObservationSet__category, domain=None, range=Optional[Union[str, "CCDHDimensionalObservationSetCategory"]])

slots.dimensionalObservationSet__focus = Slot(uri=CCDH.focus, name="dimensionalObservationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.dimensionalObservationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.dimensionalObservationSet__subject = Slot(uri=CCDH.subject, name="dimensionalObservationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.dimensionalObservationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.dimensionalObservationSet__method_type = Slot(uri=CCDH.method_type, name="dimensionalObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.dimensionalObservationSet__method_type, domain=None, range=Optional[Union[Union[str, "CCDHDimensionalObservationSetMethodType"], List[Union[str, "CCDHDimensionalObservationSetMethodType"]]]])

slots.dimensionalObservationSet__performed_by = Slot(uri=CCDH.performed_by, name="dimensionalObservationSet__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.dimensionalObservationSet__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.dimensionalObservationSet__observations = Slot(uri=CCDH.observations, name="dimensionalObservationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.dimensionalObservationSet__observations, domain=None, range=Optional[Union[Union[dict, DimensionalObservation], List[Union[dict, DimensionalObservation]]]])

slots.document__id = Slot(uri=CCDH.id, name="document__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.document__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.document__identifier = Slot(uri=CCDH.identifier, name="document__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.document__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.document__document_type = Slot(uri=CCDH.document_type, name="document__document_type", curie=CCDH.curie('document_type'),
                   model_uri=CCDH.document__document_type, domain=None, range=Optional[Union[str, "CCDHDocumentDocumentType"]])

slots.document__description = Slot(uri=CCDH.description, name="document__description", curie=CCDH.curie('description'),
                   model_uri=CCDH.document__description, domain=None, range=Optional[Union[str, CcdhString]])

slots.document__focus = Slot(uri=CCDH.focus, name="document__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.document__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.document__url = Slot(uri=CCDH.url, name="document__url", curie=CCDH.curie('url'),
                   model_uri=CCDH.document__url, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.environmentalExposureObservation__id = Slot(uri=CCDH.id, name="environmentalExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.environmentalExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.environmentalExposureObservation__category = Slot(uri=CCDH.category, name="environmentalExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.environmentalExposureObservation__category, domain=None, range=Optional[Union[str, "CCDHEnvironmentalExposureObservationCategory"]])

slots.environmentalExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="environmentalExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.environmentalExposureObservation__observation_type, domain=None, range=Union[str, "CCDHEnvironmentalExposureObservationObservationType"])

slots.environmentalExposureObservation__method_type = Slot(uri=CCDH.method_type, name="environmentalExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.environmentalExposureObservation__method_type, domain=None, range=Optional[Union[str, "CCDHEnvironmentalExposureObservationMethodType"]])

slots.environmentalExposureObservation__focus = Slot(uri=CCDH.focus, name="environmentalExposureObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.environmentalExposureObservation__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.environmentalExposureObservation__subject = Slot(uri=CCDH.subject, name="environmentalExposureObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.environmentalExposureObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.environmentalExposureObservation__performed_by = Slot(uri=CCDH.performed_by, name="environmentalExposureObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.environmentalExposureObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.environmentalExposureObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="environmentalExposureObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.environmentalExposureObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.environmentalExposureObservation__valueString = Slot(uri=CCDH.valueString, name="environmentalExposureObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.environmentalExposureObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.environmentalExposureObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="environmentalExposureObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.environmentalExposureObservation__valueInteger, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.environmentalExposureObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="environmentalExposureObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.environmentalExposureObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.environmentalExposureObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="environmentalExposureObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.environmentalExposureObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.environmentalExposureObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="environmentalExposureObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.environmentalExposureObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.environmentalExposureObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="environmentalExposureObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.environmentalExposureObservation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.environmentalExposureObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="environmentalExposureObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.environmentalExposureObservation__valueCodeableConcept, domain=None, range=Union[str, "CCDHEnvironmentalExposureObservationValueCodeableConcept"])

slots.exposure__id = Slot(uri=CCDH.id, name="exposure__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.exposure__id, domain=None, range=Union[str, CcdhString])

slots.exposure__identifier = Slot(uri=CCDH.identifier, name="exposure__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.exposure__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.exposure__tobacco_exposure = Slot(uri=CCDH.tobacco_exposure, name="exposure__tobacco_exposure", curie=CCDH.curie('tobacco_exposure'),
                   model_uri=CCDH.exposure__tobacco_exposure, domain=None, range=Optional[Union[Union[dict, TobaccoExposureObservation], List[Union[dict, TobaccoExposureObservation]]]])

slots.exposure__alcohol_exposure = Slot(uri=CCDH.alcohol_exposure, name="exposure__alcohol_exposure", curie=CCDH.curie('alcohol_exposure'),
                   model_uri=CCDH.exposure__alcohol_exposure, domain=None, range=Optional[Union[Union[dict, AlcoholExposureObservation], List[Union[dict, AlcoholExposureObservation]]]])

slots.exposure__environmental_exposure = Slot(uri=CCDH.environmental_exposure, name="exposure__environmental_exposure", curie=CCDH.curie('environmental_exposure'),
                   model_uri=CCDH.exposure__environmental_exposure, domain=None, range=Optional[Union[Union[dict, EnvironmentalExposureObservation], List[Union[dict, EnvironmentalExposureObservation]]]])

slots.exposure__subject = Slot(uri=CCDH.subject, name="exposure__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.exposure__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.identifier__value = Slot(uri=CCDH.value, name="identifier__value", curie=CCDH.curie('value'),
                   model_uri=CCDH.identifier__value, domain=None, range=Union[str, CcdhString])

slots.identifier__system = Slot(uri=CCDH.system, name="identifier__system", curie=CCDH.curie('system'),
                   model_uri=CCDH.identifier__system, domain=None, range=Optional[Union[str, CcdhString]])

slots.identifier__type = Slot(uri=CCDH.type, name="identifier__type", curie=CCDH.curie('type'),
                   model_uri=CCDH.identifier__type, domain=None, range=Optional[Union[str, "CCDHIdentifierType"]])

slots.observation__id = Slot(uri=CCDH.id, name="observation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.observation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.observation__category = Slot(uri=CCDH.category, name="observation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.observation__category, domain=None, range=Optional[Union[str, "CCDHObservationCategory"]])

slots.observation__observation_type = Slot(uri=CCDH.observation_type, name="observation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.observation__observation_type, domain=None, range=Union[str, "CCDHObservationObservationType"])

slots.observation__method_type = Slot(uri=CCDH.method_type, name="observation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.observation__method_type, domain=None, range=Optional[Union[Union[str, "CCDHObservationMethodType"], List[Union[str, "CCDHObservationMethodType"]]]])

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
                   model_uri=CCDH.observation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHObservationValueCodeableConcept"]])

slots.observationSet__id = Slot(uri=CCDH.id, name="observationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.observationSet__id, domain=None, range=Union[str, CcdhString])

slots.observationSet__category = Slot(uri=CCDH.category, name="observationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.observationSet__category, domain=None, range=Union[str, "CCDHObservationSetCategory"])

slots.observationSet__focus = Slot(uri=CCDH.focus, name="observationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.observationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.observationSet__subject = Slot(uri=CCDH.subject, name="observationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.observationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.observationSet__method_type = Slot(uri=CCDH.method_type, name="observationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.observationSet__method_type, domain=None, range=Optional[Union[Union[str, "CCDHObservationSetMethodType"], List[Union[str, "CCDHObservationSetMethodType"]]]])

slots.observationSet__performed_by = Slot(uri=CCDH.performed_by, name="observationSet__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.observationSet__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.observationSet__observations = Slot(uri=CCDH.observations, name="observationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.observationSet__observations, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

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
                   model_uri=CCDH.quantity__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHQuantityValueCodeableConcept"]])

slots.quantity__unit = Slot(uri=CCDH.unit, name="quantity__unit", curie=CCDH.curie('unit'),
                   model_uri=CCDH.quantity__unit, domain=None, range=Optional[Union[str, "CCDHQuantityUnit"]])

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
                   model_uri=CCDH.researchProject__primary_anatomic_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

slots.researchProject__url = Slot(uri=CCDH.url, name="researchProject__url", curie=CCDH.curie('url'),
                   model_uri=CCDH.researchProject__url, domain=None, range=Optional[Union[Union[str, CcdhString], List[Union[str, CcdhString]]]])

slots.researchProject__part_of = Slot(uri=CCDH.part_of, name="researchProject__part_of", curie=CCDH.curie('part_of'),
                   model_uri=CCDH.researchProject__part_of, domain=None, range=Optional[Union[Union[dict, ResearchProject], List[Union[dict, ResearchProject]]]])

slots.researchProject__research_project_type = Slot(uri=CCDH.research_project_type, name="researchProject__research_project_type", curie=CCDH.curie('research_project_type'),
                   model_uri=CCDH.researchProject__research_project_type, domain=None, range=Union[str, "CCDHResearchProjectResearchProjectType"])

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
                   model_uri=CCDH.researchSubject__primary_diagnosis_condition, domain=None, range=Optional[Union[str, "CCDHResearchSubjectPrimaryDiagnosisCondition"]])

slots.researchSubject__primary_diagnosis_site = Slot(uri=CCDH.primary_diagnosis_site, name="researchSubject__primary_diagnosis_site", curie=CCDH.curie('primary_diagnosis_site'),
                   model_uri=CCDH.researchSubject__primary_diagnosis_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.researchSubject__primary_diagnosis = Slot(uri=CCDH.primary_diagnosis, name="researchSubject__primary_diagnosis", curie=CCDH.curie('primary_diagnosis'),
                   model_uri=CCDH.researchSubject__primary_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__comorbid_diagnosis = Slot(uri=CCDH.comorbid_diagnosis, name="researchSubject__comorbid_diagnosis", curie=CCDH.curie('comorbid_diagnosis'),
                   model_uri=CCDH.researchSubject__comorbid_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__index_timepoint = Slot(uri=CCDH.index_timepoint, name="researchSubject__index_timepoint", curie=CCDH.curie('index_timepoint'),
                   model_uri=CCDH.researchSubject__index_timepoint, domain=None, range=Optional[Union[str, "CCDHResearchSubjectIndexTimepoint"]])

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
                   model_uri=CCDH.specimen__specimen_type, domain=None, range=Optional[Union[str, "CCDHSpecimenSpecimenType"]])

slots.specimen__analyte_type = Slot(uri=CCDH.analyte_type, name="specimen__analyte_type", curie=CCDH.curie('analyte_type'),
                   model_uri=CCDH.specimen__analyte_type, domain=None, range=Optional[Union[str, "CCDHSpecimenAnalyteType"]])

slots.specimen__associated_project = Slot(uri=CCDH.associated_project, name="specimen__associated_project", curie=CCDH.curie('associated_project'),
                   model_uri=CCDH.specimen__associated_project, domain=None, range=Optional[Union[dict, ResearchProject]])

slots.specimen__data_provider = Slot(uri=CCDH.data_provider, name="specimen__data_provider", curie=CCDH.curie('data_provider'),
                   model_uri=CCDH.specimen__data_provider, domain=None, range=Optional[Union[dict, Organization]])

slots.specimen__source_material_type = Slot(uri=CCDH.source_material_type, name="specimen__source_material_type", curie=CCDH.curie('source_material_type'),
                   model_uri=CCDH.specimen__source_material_type, domain=None, range=Optional[Union[str, "CCDHSpecimenSourceMaterialType"]])

slots.specimen__parent_specimen = Slot(uri=CCDH.parent_specimen, name="specimen__parent_specimen", curie=CCDH.curie('parent_specimen'),
                   model_uri=CCDH.specimen__parent_specimen, domain=None, range=Optional[Union[Union[dict, Specimen], List[Union[dict, Specimen]]]])

slots.specimen__source_subject = Slot(uri=CCDH.source_subject, name="specimen__source_subject", curie=CCDH.curie('source_subject'),
                   model_uri=CCDH.specimen__source_subject, domain=None, range=Optional[Union[dict, Subject]])

slots.specimen__source_model_system = Slot(uri=CCDH.source_model_system, name="specimen__source_model_system", curie=CCDH.curie('source_model_system'),
                   model_uri=CCDH.specimen__source_model_system, domain=None, range=Optional[Union[dict, Entity]])

slots.specimen__tumor_status_at_collection = Slot(uri=CCDH.tumor_status_at_collection, name="specimen__tumor_status_at_collection", curie=CCDH.curie('tumor_status_at_collection'),
                   model_uri=CCDH.specimen__tumor_status_at_collection, domain=None, range=Optional[Union[str, "CCDHSpecimenTumorStatusAtCollection"]])

slots.specimen__creation_activity = Slot(uri=CCDH.creation_activity, name="specimen__creation_activity", curie=CCDH.curie('creation_activity'),
                   model_uri=CCDH.specimen__creation_activity, domain=None, range=Optional[Union[dict, SpecimenCreationActivity]])

slots.specimen__processing_activity = Slot(uri=CCDH.processing_activity, name="specimen__processing_activity", curie=CCDH.curie('processing_activity'),
                   model_uri=CCDH.specimen__processing_activity, domain=None, range=Optional[Union[Union[dict, SpecimenProcessingActivity], List[Union[dict, SpecimenProcessingActivity]]]])

slots.specimen__storage_activity = Slot(uri=CCDH.storage_activity, name="specimen__storage_activity", curie=CCDH.curie('storage_activity'),
                   model_uri=CCDH.specimen__storage_activity, domain=None, range=Optional[Union[Union[dict, SpecimenStorageActivity], List[Union[dict, SpecimenStorageActivity]]]])

slots.specimen__transport_activity = Slot(uri=CCDH.transport_activity, name="specimen__transport_activity", curie=CCDH.curie('transport_activity'),
                   model_uri=CCDH.specimen__transport_activity, domain=None, range=Optional[Union[Union[dict, SpecimenTransportActivity], List[Union[dict, SpecimenTransportActivity]]]])

slots.specimen__contained_in = Slot(uri=CCDH.contained_in, name="specimen__contained_in", curie=CCDH.curie('contained_in'),
                   model_uri=CCDH.specimen__contained_in, domain=None, range=Optional[Union[dict, SpecimenContainer]])

slots.specimen__dimensional_measure = Slot(uri=CCDH.dimensional_measure, name="specimen__dimensional_measure", curie=CCDH.curie('dimensional_measure'),
                   model_uri=CCDH.specimen__dimensional_measure, domain=None, range=Optional[Union[dict, DimensionalObservationSet]])

slots.specimen__quantity_measure = Slot(uri=CCDH.quantity_measure, name="specimen__quantity_measure", curie=CCDH.curie('quantity_measure'),
                   model_uri=CCDH.specimen__quantity_measure, domain=None, range=Optional[Union[Union[dict, SpecimenQuantityObservation], List[Union[dict, SpecimenQuantityObservation]]]])

slots.specimen__quality_measure = Slot(uri=CCDH.quality_measure, name="specimen__quality_measure", curie=CCDH.curie('quality_measure'),
                   model_uri=CCDH.specimen__quality_measure, domain=None, range=Optional[Union[Union[dict, SpecimenQualityObservation], List[Union[dict, SpecimenQualityObservation]]]])

slots.specimen__cellular_composition_type = Slot(uri=CCDH.cellular_composition_type, name="specimen__cellular_composition_type", curie=CCDH.curie('cellular_composition_type'),
                   model_uri=CCDH.specimen__cellular_composition_type, domain=None, range=Optional[Union[str, "CCDHSpecimenCellularCompositionType"]])

slots.specimen__histological_composition_measure = Slot(uri=CCDH.histological_composition_measure, name="specimen__histological_composition_measure", curie=CCDH.curie('histological_composition_measure'),
                   model_uri=CCDH.specimen__histological_composition_measure, domain=None, range=Optional[Union[Union[dict, ObservationSet], List[Union[dict, ObservationSet]]]])

slots.specimen__general_tissue_morphology = Slot(uri=CCDH.general_tissue_morphology, name="specimen__general_tissue_morphology", curie=CCDH.curie('general_tissue_morphology'),
                   model_uri=CCDH.specimen__general_tissue_morphology, domain=None, range=Optional[Union[str, "CCDHSpecimenGeneralTissueMorphology"]])

slots.specimen__specific_tissue_morphology = Slot(uri=CCDH.specific_tissue_morphology, name="specimen__specific_tissue_morphology", curie=CCDH.curie('specific_tissue_morphology'),
                   model_uri=CCDH.specimen__specific_tissue_morphology, domain=None, range=Optional[Union[str, "CCDHSpecimenSpecificTissueMorphology"]])

slots.specimen__preinvasive_tissue_morphology = Slot(uri=CCDH.preinvasive_tissue_morphology, name="specimen__preinvasive_tissue_morphology", curie=CCDH.curie('preinvasive_tissue_morphology'),
                   model_uri=CCDH.specimen__preinvasive_tissue_morphology, domain=None, range=Optional[Union[str, "CCDHSpecimenPreinvasiveTissueMorphology"]])

slots.specimen__morphology_pathologically_confirmed = Slot(uri=CCDH.morphology_pathologically_confirmed, name="specimen__morphology_pathologically_confirmed", curie=CCDH.curie('morphology_pathologically_confirmed'),
                   model_uri=CCDH.specimen__morphology_pathologically_confirmed, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.specimen__morphology_assessor_role = Slot(uri=CCDH.morphology_assessor_role, name="specimen__morphology_assessor_role", curie=CCDH.curie('morphology_assessor_role'),
                   model_uri=CCDH.specimen__morphology_assessor_role, domain=None, range=Optional[Union[str, "CCDHSpecimenMorphologyAssessorRole"]])

slots.specimen__morphlogy_assessment_method = Slot(uri=CCDH.morphlogy_assessment_method, name="specimen__morphlogy_assessment_method", curie=CCDH.curie('morphlogy_assessment_method'),
                   model_uri=CCDH.specimen__morphlogy_assessment_method, domain=None, range=Optional[Union[str, "CCDHSpecimenMorphlogyAssessmentMethod"]])

slots.specimen__degree_of_dysplasia = Slot(uri=CCDH.degree_of_dysplasia, name="specimen__degree_of_dysplasia", curie=CCDH.curie('degree_of_dysplasia'),
                   model_uri=CCDH.specimen__degree_of_dysplasia, domain=None, range=Optional[Union[str, "CCDHSpecimenDegreeOfDysplasia"]])

slots.specimen__dysplasia_fraction = Slot(uri=CCDH.dysplasia_fraction, name="specimen__dysplasia_fraction", curie=CCDH.curie('dysplasia_fraction'),
                   model_uri=CCDH.specimen__dysplasia_fraction, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimen__related_document = Slot(uri=CCDH.related_document, name="specimen__related_document", curie=CCDH.curie('related_document'),
                   model_uri=CCDH.specimen__related_document, domain=None, range=Optional[Union[Union[dict, Document], List[Union[dict, Document]]]])

slots.specimen__section_location = Slot(uri=CCDH.section_location, name="specimen__section_location", curie=CCDH.curie('section_location'),
                   model_uri=CCDH.specimen__section_location, domain=None, range=Optional[Union[str, "CCDHSpecimenSectionLocation"]])

slots.specimen__derived_product = Slot(uri=CCDH.derived_product, name="specimen__derived_product", curie=CCDH.curie('derived_product'),
                   model_uri=CCDH.specimen__derived_product, domain=None, range=Optional[Union[Union[dict, BiologicProduct], List[Union[dict, BiologicProduct]]]])

slots.specimen__distance_from_paired_specimen = Slot(uri=CCDH.distance_from_paired_specimen, name="specimen__distance_from_paired_specimen", curie=CCDH.curie('distance_from_paired_specimen'),
                   model_uri=CCDH.specimen__distance_from_paired_specimen, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenContainer__id = Slot(uri=CCDH.id, name="specimenContainer__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenContainer__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__identifier = Slot(uri=CCDH.identifier, name="specimenContainer__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.specimenContainer__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.specimenContainer__container_type = Slot(uri=CCDH.container_type, name="specimenContainer__container_type", curie=CCDH.curie('container_type'),
                   model_uri=CCDH.specimenContainer__container_type, domain=None, range=Optional[Union[str, "CCDHSpecimenContainerContainerType"]])

slots.specimenContainer__container_number = Slot(uri=CCDH.container_number, name="specimenContainer__container_number", curie=CCDH.curie('container_number'),
                   model_uri=CCDH.specimenContainer__container_number, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenContainer__additive = Slot(uri=CCDH.additive, name="specimenContainer__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenContainer__additive, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

slots.specimenContainer__parent_container = Slot(uri=CCDH.parent_container, name="specimenContainer__parent_container", curie=CCDH.curie('parent_container'),
                   model_uri=CCDH.specimenContainer__parent_container, domain=None, range=Optional[Union[Union[dict, SpecimenContainer], List[Union[dict, SpecimenContainer]]]])

slots.specimenContainer__charge_type = Slot(uri=CCDH.charge_type, name="specimenContainer__charge_type", curie=CCDH.curie('charge_type'),
                   model_uri=CCDH.specimenContainer__charge_type, domain=None, range=Optional[Union[str, "CCDHSpecimenContainerChargeType"]])

slots.specimenCreationActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenCreationActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenCreationActivity__activity_type, domain=None, range=Optional[Union[str, "CCDHSpecimenCreationActivityActivityType"]])

slots.specimenCreationActivity__date_started = Slot(uri=CCDH.date_started, name="specimenCreationActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenCreationActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenCreationActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenCreationActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenCreationActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenCreationActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenCreationActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenCreationActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenCreationActivity__collection_method_type = Slot(uri=CCDH.collection_method_type, name="specimenCreationActivity__collection_method_type", curie=CCDH.curie('collection_method_type'),
                   model_uri=CCDH.specimenCreationActivity__collection_method_type, domain=None, range=Optional[Union[str, "CCDHSpecimenCreationActivityCollectionMethodType"]])

slots.specimenCreationActivity__derivation_method_type = Slot(uri=CCDH.derivation_method_type, name="specimenCreationActivity__derivation_method_type", curie=CCDH.curie('derivation_method_type'),
                   model_uri=CCDH.specimenCreationActivity__derivation_method_type, domain=None, range=Optional[Union[str, "CCDHSpecimenCreationActivityDerivationMethodType"]])

slots.specimenCreationActivity__additive = Slot(uri=CCDH.additive, name="specimenCreationActivity__additive", curie=CCDH.curie('additive'),
                   model_uri=CCDH.specimenCreationActivity__additive, domain=None, range=Optional[Union[Union[dict, Substance], List[Union[dict, Substance]]]])

slots.specimenCreationActivity__collection_site = Slot(uri=CCDH.collection_site, name="specimenCreationActivity__collection_site", curie=CCDH.curie('collection_site'),
                   model_uri=CCDH.specimenCreationActivity__collection_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.specimenCreationActivity__quantity_collected = Slot(uri=CCDH.quantity_collected, name="specimenCreationActivity__quantity_collected", curie=CCDH.curie('quantity_collected'),
                   model_uri=CCDH.specimenCreationActivity__quantity_collected, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenCreationActivity__execution_observation = Slot(uri=CCDH.execution_observation, name="specimenCreationActivity__execution_observation", curie=CCDH.curie('execution_observation'),
                   model_uri=CCDH.specimenCreationActivity__execution_observation, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimenCreationActivity__specimen_order = Slot(uri=CCDH.specimen_order, name="specimenCreationActivity__specimen_order", curie=CCDH.curie('specimen_order'),
                   model_uri=CCDH.specimenCreationActivity__specimen_order, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.specimenQuantityObservation__id = Slot(uri=CCDH.id, name="specimenQuantityObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenQuantityObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQuantityObservation__category = Slot(uri=CCDH.category, name="specimenQuantityObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.specimenQuantityObservation__category, domain=None, range=Optional[Union[str, "CCDHSpecimenQuantityObservationCategory"]])

slots.specimenQuantityObservation__observation_type = Slot(uri=CCDH.observation_type, name="specimenQuantityObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.specimenQuantityObservation__observation_type, domain=None, range=Union[str, "CCDHSpecimenQuantityObservationObservationType"])

slots.specimenQuantityObservation__method_type = Slot(uri=CCDH.method_type, name="specimenQuantityObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenQuantityObservation__method_type, domain=None, range=Optional[Union[Union[str, "CCDHSpecimenQuantityObservationMethodType"], List[Union[str, "CCDHSpecimenQuantityObservationMethodType"]]]])

slots.specimenQuantityObservation__focus = Slot(uri=CCDH.focus, name="specimenQuantityObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.specimenQuantityObservation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenQuantityObservation__subject = Slot(uri=CCDH.subject, name="specimenQuantityObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.specimenQuantityObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.specimenQuantityObservation__performed_by = Slot(uri=CCDH.performed_by, name="specimenQuantityObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenQuantityObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenQuantityObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="specimenQuantityObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.specimenQuantityObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.specimenQuantityObservation__valueString = Slot(uri=CCDH.valueString, name="specimenQuantityObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.specimenQuantityObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQuantityObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="specimenQuantityObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.specimenQuantityObservation__valueInteger, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.specimenQuantityObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="specimenQuantityObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.specimenQuantityObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.specimenQuantityObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="specimenQuantityObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.specimenQuantityObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.specimenQuantityObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="specimenQuantityObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.specimenQuantityObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenQuantityObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="specimenQuantityObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.specimenQuantityObservation__valueQuantity, domain=None, range=Union[dict, Quantity])

slots.specimenQuantityObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="specimenQuantityObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.specimenQuantityObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHSpecimenQuantityObservationValueCodeableConcept"]])

slots.specimenQualityObservation__id = Slot(uri=CCDH.id, name="specimenQualityObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenQualityObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQualityObservation__category = Slot(uri=CCDH.category, name="specimenQualityObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.specimenQualityObservation__category, domain=None, range=Optional[Union[str, "CCDHSpecimenQualityObservationCategory"]])

slots.specimenQualityObservation__observation_type = Slot(uri=CCDH.observation_type, name="specimenQualityObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.specimenQualityObservation__observation_type, domain=None, range=Union[str, "CCDHSpecimenQualityObservationObservationType"])

slots.specimenQualityObservation__method_type = Slot(uri=CCDH.method_type, name="specimenQualityObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenQualityObservation__method_type, domain=None, range=Optional[Union[Union[str, "CCDHSpecimenQualityObservationMethodType"], List[Union[str, "CCDHSpecimenQualityObservationMethodType"]]]])

slots.specimenQualityObservation__focus = Slot(uri=CCDH.focus, name="specimenQualityObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.specimenQualityObservation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenQualityObservation__subject = Slot(uri=CCDH.subject, name="specimenQualityObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.specimenQualityObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.specimenQualityObservation__performed_by = Slot(uri=CCDH.performed_by, name="specimenQualityObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenQualityObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenQualityObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="specimenQualityObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.specimenQualityObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.specimenQualityObservation__valueString = Slot(uri=CCDH.valueString, name="specimenQualityObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.specimenQualityObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQualityObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="specimenQualityObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.specimenQualityObservation__valueInteger, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.specimenQualityObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="specimenQualityObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.specimenQualityObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.specimenQualityObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="specimenQualityObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.specimenQualityObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.specimenQualityObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="specimenQualityObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.specimenQualityObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.specimenProcessingActivity__activity_type = Slot(uri=CCDH.activity_type, name="specimenProcessingActivity__activity_type", curie=CCDH.curie('activity_type'),
                   model_uri=CCDH.specimenProcessingActivity__activity_type, domain=None, range=Optional[Union[str, "CCDHSpecimenProcessingActivityActivityType"]])

slots.specimenProcessingActivity__date_started = Slot(uri=CCDH.date_started, name="specimenProcessingActivity__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.specimenProcessingActivity__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenProcessingActivity__date_ended = Slot(uri=CCDH.date_ended, name="specimenProcessingActivity__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.specimenProcessingActivity__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.specimenProcessingActivity__duration = Slot(uri=CCDH.duration, name="specimenProcessingActivity__duration", curie=CCDH.curie('duration'),
                   model_uri=CCDH.specimenProcessingActivity__duration, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.specimenProcessingActivity__performed_by = Slot(uri=CCDH.performed_by, name="specimenProcessingActivity__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.specimenProcessingActivity__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.specimenProcessingActivity__method_type = Slot(uri=CCDH.method_type, name="specimenProcessingActivity__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenProcessingActivity__method_type, domain=None, range=Optional[Union[str, "CCDHSpecimenProcessingActivityMethodType"]])

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
                   model_uri=CCDH.specimenStorageActivity__method_type, domain=None, range=Optional[Union[str, "CCDHSpecimenStorageActivityMethodType"]])

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
                   model_uri=CCDH.subject__species, domain=None, range=Optional[Union[str, "CCDHSubjectSpecies"]])

slots.subject__breed = Slot(uri=CCDH.breed, name="subject__breed", curie=CCDH.curie('breed'),
                   model_uri=CCDH.subject__breed, domain=None, range=Optional[Union[str, "CCDHSubjectBreed"]])

slots.subject__sex = Slot(uri=CCDH.sex, name="subject__sex", curie=CCDH.curie('sex'),
                   model_uri=CCDH.subject__sex, domain=None, range=Optional[Union[str, "CCDHSubjectSex"]])

slots.subject__ethnicity = Slot(uri=CCDH.ethnicity, name="subject__ethnicity", curie=CCDH.curie('ethnicity'),
                   model_uri=CCDH.subject__ethnicity, domain=None, range=Optional[Union[str, "CCDHSubjectEthnicity"]])

slots.subject__race = Slot(uri=CCDH.race, name="subject__race", curie=CCDH.curie('race'),
                   model_uri=CCDH.subject__race, domain=None, range=Optional[Union[Union[str, "CCDHSubjectRace"], List[Union[str, "CCDHSubjectRace"]]]])

slots.subject__year_of_birth = Slot(uri=CCDH.year_of_birth, name="subject__year_of_birth", curie=CCDH.curie('year_of_birth'),
                   model_uri=CCDH.subject__year_of_birth, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__vital_status = Slot(uri=CCDH.vital_status, name="subject__vital_status", curie=CCDH.curie('vital_status'),
                   model_uri=CCDH.subject__vital_status, domain=None, range=Optional[Union[str, "CCDHSubjectVitalStatus"]])

slots.subject__age_at_death = Slot(uri=CCDH.age_at_death, name="subject__age_at_death", curie=CCDH.curie('age_at_death'),
                   model_uri=CCDH.subject__age_at_death, domain=None, range=Optional[Union[dict, Quantity]])

slots.subject__year_of_death = Slot(uri=CCDH.year_of_death, name="subject__year_of_death", curie=CCDH.curie('year_of_death'),
                   model_uri=CCDH.subject__year_of_death, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.subject__cause_of_death = Slot(uri=CCDH.cause_of_death, name="subject__cause_of_death", curie=CCDH.curie('cause_of_death'),
                   model_uri=CCDH.subject__cause_of_death, domain=None, range=Optional[Union[str, "CCDHSubjectCauseOfDeath"]])

slots.substance__substance_type = Slot(uri=CCDH.substance_type, name="substance__substance_type", curie=CCDH.curie('substance_type'),
                   model_uri=CCDH.substance__substance_type, domain=None, range=Optional[Union[str, "CCDHSubstanceSubstanceType"]])

slots.substance__role = Slot(uri=CCDH.role, name="substance__role", curie=CCDH.curie('role'),
                   model_uri=CCDH.substance__role, domain=None, range=Optional[Union[Union[str, "CCDHSubstanceRole"], List[Union[str, "CCDHSubstanceRole"]]]])

slots.substance__substance_quantity = Slot(uri=CCDH.substance_quantity, name="substance__substance_quantity", curie=CCDH.curie('substance_quantity'),
                   model_uri=CCDH.substance__substance_quantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.timePoint__id = Slot(uri=CCDH.id, name="timePoint__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.timePoint__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.timePoint__dateTime = Slot(uri=CCDH.dateTime, name="timePoint__dateTime", curie=CCDH.curie('dateTime'),
                   model_uri=CCDH.timePoint__dateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__indexTimePoint = Slot(uri=CCDH.indexTimePoint, name="timePoint__indexTimePoint", curie=CCDH.curie('indexTimePoint'),
                   model_uri=CCDH.timePoint__indexTimePoint, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePoint__offsetFromIndex = Slot(uri=CCDH.offsetFromIndex, name="timePoint__offsetFromIndex", curie=CCDH.curie('offsetFromIndex'),
                   model_uri=CCDH.timePoint__offsetFromIndex, domain=None, range=Optional[Union[dict, Quantity]])

slots.timePoint__eventType = Slot(uri=CCDH.eventType, name="timePoint__eventType", curie=CCDH.curie('eventType'),
                   model_uri=CCDH.timePoint__eventType, domain=None, range=Optional[Union[Union[str, "CCDHTimePointEventType"], List[Union[str, "CCDHTimePointEventType"]]]])

slots.timePeriod__periodStart_start = Slot(uri=CCDH.periodStart_start, name="timePeriod__periodStart_start", curie=CCDH.curie('periodStart_start'),
                   model_uri=CCDH.timePeriod__periodStart_start, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePeriod__periodEnd_end = Slot(uri=CCDH.periodEnd_end, name="timePeriod__periodEnd_end", curie=CCDH.curie('periodEnd_end'),
                   model_uri=CCDH.timePeriod__periodEnd_end, domain=None, range=Optional[Union[dict, TimePoint]])

slots.tobaccoExposureObservation__id = Slot(uri=CCDH.id, name="tobaccoExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.tobaccoExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.tobaccoExposureObservation__category = Slot(uri=CCDH.category, name="tobaccoExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.tobaccoExposureObservation__category, domain=None, range=Optional[Union[str, "CCDHTobaccoExposureObservationCategory"]])

slots.tobaccoExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="tobaccoExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.tobaccoExposureObservation__observation_type, domain=None, range=Union[str, "CCDHTobaccoExposureObservationObservationType"])

slots.tobaccoExposureObservation__method_type = Slot(uri=CCDH.method_type, name="tobaccoExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.tobaccoExposureObservation__method_type, domain=None, range=Optional[Union[str, "CCDHTobaccoExposureObservationMethodType"]])

slots.tobaccoExposureObservation__focus = Slot(uri=CCDH.focus, name="tobaccoExposureObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.tobaccoExposureObservation__focus, domain=None, range=Optional[Union[dict, Entity]])

slots.tobaccoExposureObservation__subject = Slot(uri=CCDH.subject, name="tobaccoExposureObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.tobaccoExposureObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.tobaccoExposureObservation__performed_by = Slot(uri=CCDH.performed_by, name="tobaccoExposureObservation__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.tobaccoExposureObservation__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.tobaccoExposureObservation__valueEntity = Slot(uri=CCDH.valueEntity, name="tobaccoExposureObservation__valueEntity", curie=CCDH.curie('valueEntity'),
                   model_uri=CCDH.tobaccoExposureObservation__valueEntity, domain=None, range=Optional[Union[dict, Entity]])

slots.tobaccoExposureObservation__valueString = Slot(uri=CCDH.valueString, name="tobaccoExposureObservation__valueString", curie=CCDH.curie('valueString'),
                   model_uri=CCDH.tobaccoExposureObservation__valueString, domain=None, range=Optional[Union[str, CcdhString]])

slots.tobaccoExposureObservation__valueInteger = Slot(uri=CCDH.valueInteger, name="tobaccoExposureObservation__valueInteger", curie=CCDH.curie('valueInteger'),
                   model_uri=CCDH.tobaccoExposureObservation__valueInteger, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.tobaccoExposureObservation__valueDecimal = Slot(uri=CCDH.valueDecimal, name="tobaccoExposureObservation__valueDecimal", curie=CCDH.curie('valueDecimal'),
                   model_uri=CCDH.tobaccoExposureObservation__valueDecimal, domain=None, range=Optional[Union[Decimal, CcdhDecimal]])

slots.tobaccoExposureObservation__valueBoolean = Slot(uri=CCDH.valueBoolean, name="tobaccoExposureObservation__valueBoolean", curie=CCDH.curie('valueBoolean'),
                   model_uri=CCDH.tobaccoExposureObservation__valueBoolean, domain=None, range=Optional[Union[bool, CcdhBoolean]])

slots.tobaccoExposureObservation__valueDateTime = Slot(uri=CCDH.valueDateTime, name="tobaccoExposureObservation__valueDateTime", curie=CCDH.curie('valueDateTime'),
                   model_uri=CCDH.tobaccoExposureObservation__valueDateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.tobaccoExposureObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="tobaccoExposureObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.tobaccoExposureObservation__valueQuantity, domain=None, range=Optional[Union[dict, Quantity]])

slots.tobaccoExposureObservation__valueCodeableConcept = Slot(uri=CCDH.valueCodeableConcept, name="tobaccoExposureObservation__valueCodeableConcept", curie=CCDH.curie('valueCodeableConcept'),
                   model_uri=CCDH.tobaccoExposureObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "CCDHTobaccoExposureObservationValueCodeableConcept"]])

slots.treatment__treatment_for_diagnosis = Slot(uri=CCDH.treatment_for_diagnosis, name="treatment__treatment_for_diagnosis", curie=CCDH.curie('treatment_for_diagnosis'),
                   model_uri=CCDH.treatment__treatment_for_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.treatment__subject = Slot(uri=CCDH.subject, name="treatment__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.treatment__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.treatment__date_started = Slot(uri=CCDH.date_started, name="treatment__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.treatment__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__date_ended = Slot(uri=CCDH.date_ended, name="treatment__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.treatment__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__id = Slot(uri=CCDH.id, name="treatment__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.treatment__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.treatment__identifier = Slot(uri=CCDH.identifier, name="treatment__identifier", curie=CCDH.curie('identifier'),
                   model_uri=CCDH.treatment__identifier, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.treatment__regimen = Slot(uri=CCDH.regimen, name="treatment__regimen", curie=CCDH.curie('regimen'),
                   model_uri=CCDH.treatment__regimen, domain=None, range=Optional[Union[str, "CCDHTreatmentRegimen"]])

slots.treatment__therapeutic_agent = Slot(uri=CCDH.therapeutic_agent, name="treatment__therapeutic_agent", curie=CCDH.curie('therapeutic_agent'),
                   model_uri=CCDH.treatment__therapeutic_agent, domain=None, range=Optional[Union[dict, Substance]])

slots.treatment__treatment_anatomic_site = Slot(uri=CCDH.treatment_anatomic_site, name="treatment__treatment_anatomic_site", curie=CCDH.curie('treatment_anatomic_site'),
                   model_uri=CCDH.treatment__treatment_anatomic_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.treatment__treatment_effect = Slot(uri=CCDH.treatment_effect, name="treatment__treatment_effect", curie=CCDH.curie('treatment_effect'),
                   model_uri=CCDH.treatment__treatment_effect, domain=None, range=Optional[Union[str, "CCDHTreatmentTreatmentEffect"]])

slots.treatment__treatment_intent = Slot(uri=CCDH.treatment_intent, name="treatment__treatment_intent", curie=CCDH.curie('treatment_intent'),
                   model_uri=CCDH.treatment__treatment_intent, domain=None, range=Optional[Union[str, "CCDHTreatmentTreatmentIntent"]])

slots.treatment__treatment_outcome = Slot(uri=CCDH.treatment_outcome, name="treatment__treatment_outcome", curie=CCDH.curie('treatment_outcome'),
                   model_uri=CCDH.treatment__treatment_outcome, domain=None, range=Optional[Union[str, "CCDHTreatmentTreatmentOutcome"]])

slots.treatment__treatment_type = Slot(uri=CCDH.treatment_type, name="treatment__treatment_type", curie=CCDH.curie('treatment_type'),
                   model_uri=CCDH.treatment__treatment_type, domain=None, range=Optional[Union[str, "CCDHTreatmentTreatmentType"]])

slots.treatment__treatment_frequency = Slot(uri=CCDH.treatment_frequency, name="treatment__treatment_frequency", curie=CCDH.curie('treatment_frequency'),
                   model_uri=CCDH.treatment__treatment_frequency, domain=None, range=Optional[Union[str, "CCDHTreatmentTreatmentFrequency"]])

slots.treatment__concurrent_treatment = Slot(uri=CCDH.concurrent_treatment, name="treatment__concurrent_treatment", curie=CCDH.curie('concurrent_treatment'),
                   model_uri=CCDH.treatment__concurrent_treatment, domain=None, range=Optional[Union[Union[dict, Treatment], List[Union[dict, Treatment]]]])

slots.treatment__number_of_cycles = Slot(uri=CCDH.number_of_cycles, name="treatment__number_of_cycles", curie=CCDH.curie('number_of_cycles'),
                   model_uri=CCDH.treatment__number_of_cycles, domain=None, range=Optional[Union[int, CcdhInteger]])

slots.treatment__treatment_end_reason = Slot(uri=CCDH.treatment_end_reason, name="treatment__treatment_end_reason", curie=CCDH.curie('treatment_end_reason'),
                   model_uri=CCDH.treatment__treatment_end_reason, domain=None, range=Optional[Union[Union[str, "CCDHTreatmentTreatmentEndReason"], List[Union[str, "CCDHTreatmentTreatmentEndReason"]]]])
