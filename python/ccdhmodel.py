# Auto generated from ccdhmodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-28 10:52
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

    observation_type: Union[str, "EnumCRDC-H.AlcoholExposureObservation.observationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.category"]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.methodType"]] = None
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
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.AlcoholExposureObservation.observationType):
            self.observation_type = EnumCRDC-H.AlcoholExposureObservation.observationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.AlcoholExposureObservation.category):
            self.category = EnumCRDC-H.AlcoholExposureObservation.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.AlcoholExposureObservation.methodType):
            self.method_type = EnumCRDC-H.AlcoholExposureObservation.methodType(self.method_type)

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

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept(self.valueCodeableConcept)

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
    cancer grade observation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation
    class_class_curie: ClassVar[str] = "ccdh:CancerGradeObservation"
    class_name: ClassVar[str] = "CancerGradeObservation"
    class_model_uri: ClassVar[URIRef] = CCDH.CancerGradeObservation

    observation_type: Union[str, "EnumCRDC-H.CancerGradeObservation.observationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.category"]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.methodType"]] = None
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
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.CancerGradeObservation.observationType):
            self.observation_type = EnumCRDC-H.CancerGradeObservation.observationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.CancerGradeObservation.category):
            self.category = EnumCRDC-H.CancerGradeObservation.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.CancerGradeObservation.methodType):
            self.method_type = EnumCRDC-H.CancerGradeObservation.methodType(self.method_type)

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

    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.CancerGradeObservationSet.category"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"], List[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerGradeObservation], List[Union[dict, CancerGradeObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.CancerGradeObservationSet.category):
            self.category = EnumCRDC-H.CancerGradeObservationSet.category(self.category)

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
        self.method_type = [v if isinstance(v, EnumCRDC-H.CancerGradeObservationSet.methodType) else EnumCRDC-H.CancerGradeObservationSet.methodType(v) for v in self.method_type]

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

    observation_type: Union[str, "EnumCRDC-H.CancerStageObservation.observationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.CancerStageObservation.category"]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.CancerStageObservation.methodType"]] = None
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
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.CancerStageObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.CancerStageObservation.observationType):
            self.observation_type = EnumCRDC-H.CancerStageObservation.observationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.CancerStageObservation.category):
            self.category = EnumCRDC-H.CancerStageObservation.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.CancerStageObservation.methodType):
            self.method_type = EnumCRDC-H.CancerStageObservation.methodType(self.method_type)

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

    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.CancerStageObservationSet.category"]] = None
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    method_type: Optional[Union[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"], List[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"]]]] = empty_list()
    performed_by: Optional[Union[dict, "Organization"]] = None
    observations: Optional[Union[Union[dict, CancerStageObservation], List[Union[dict, CancerStageObservation]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.CancerStageObservationSet.category):
            self.category = EnumCRDC-H.CancerStageObservationSet.category(self.category)

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
        self.method_type = [v if isinstance(v, EnumCRDC-H.CancerStageObservationSet.methodType) else EnumCRDC-H.CancerStageObservationSet.methodType(v) for v in self.method_type]

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
    supporting_observations: Optional[Union[Union[dict, "Observation"], List[Union[dict, "Observation"]]]] = empty_list()

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
        self.stage = [v if isinstance(v, CancerStageObservationSet) else CancerStageObservationSet(**v) for v in self.stage]

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

    observation_type: Union[str, "EnumCRDC-H.DimensionalObservation.observationType"] = None
    valueQuantity: Union[dict, "Quantity"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.DimensionalObservation.category"]] = None
    method_type: Optional[Union[Union[str, "EnumCRDC-H.DimensionalObservation.methodType"], List[Union[str, "EnumCRDC-H.DimensionalObservation.methodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, "Entity"], List[Union[dict, "Entity"]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.DimensionalObservation.observationType):
            self.observation_type = EnumCRDC-H.DimensionalObservation.observationType(self.observation_type)

        if self.valueQuantity is None:
            raise ValueError("valueQuantity must be supplied")
        if not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.DimensionalObservation.category):
            self.category = EnumCRDC-H.DimensionalObservation.category(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, EnumCRDC-H.DimensionalObservation.methodType) else EnumCRDC-H.DimensionalObservation.methodType(v) for v in self.method_type]

        if self.focus is None:
            self.focus = []
        if not isinstance(self.focus, list):
            self.focus = [self.focus]
        self.focus = [v if isinstance(v, Entity) else Entity(**v) for v in self.focus]

        if self.subject is not None and not isinstance(self.subject, Subject):
            self.subject = Subject(**self.subject)

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

    observation_type: Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.observationType"] = None
    valueCodeableConcept: Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.category"]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.methodType"]] = None
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
        if not isinstance(self.observation_type, EnumCRDC-H.EnvironmentalExposureObservation.observationType):
            self.observation_type = EnumCRDC-H.EnvironmentalExposureObservation.observationType(self.observation_type)

        if self.valueCodeableConcept is None:
            raise ValueError("valueCodeableConcept must be supplied")
        if not isinstance(self.valueCodeableConcept, EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept(self.valueCodeableConcept)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.EnvironmentalExposureObservation.category):
            self.category = EnumCRDC-H.EnvironmentalExposureObservation.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.EnvironmentalExposureObservation.methodType):
            self.method_type = EnumCRDC-H.EnvironmentalExposureObservation.methodType(self.method_type)

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

    observation_type: Union[str, "EnumCRDC-H.Observation.observationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.Observation.category"]] = None
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
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.Observation.observationType):
            self.observation_type = EnumCRDC-H.Observation.observationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.Observation.category):
            self.category = EnumCRDC-H.Observation.category(self.category)

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
    primary_anatomic_site: Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]] = empty_list()
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
    primary_diagnosis_condition: Optional[Union[str, "EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition"]] = None
    primary_diagnosis_site: Optional[Union[dict, BodySite]] = None
    primary_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
    comorbid_diagnosis: Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]] = empty_list()
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
    quantity_measure: Optional[Union[Union[dict, "SpecimenQuantityObservation"], List[Union[dict, "SpecimenQuantityObservation"]]]] = empty_list()
    quality_measure: Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]] = empty_list()
    cellular_composition_type: Optional[Union[str, "EnumCRDC-H.Specimen.cellularCompositionType"]] = None
    histological_composition_measure: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
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
            self.source_model_system = Entity()

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
            self.dimensional_measure = Entity()

        if self.quantity_measure is None:
            self.quantity_measure = []
        if not isinstance(self.quantity_measure, list):
            self.quantity_measure = [self.quantity_measure]
        self._normalize_inlined_slot(slot_name="quantity_measure", slot_type=SpecimenQuantityObservation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.quality_measure is None:
            self.quality_measure = []
        if not isinstance(self.quality_measure, list):
            self.quality_measure = [self.quality_measure]
        self._normalize_inlined_slot(slot_name="quality_measure", slot_type=Observation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.cellular_composition_type is not None and not isinstance(self.cellular_composition_type, EnumCRDC-H.Specimen.cellularCompositionType):
            self.cellular_composition_type = EnumCRDC-H.Specimen.cellularCompositionType(self.cellular_composition_type)

        if self.histological_composition_measure is None:
            self.histological_composition_measure = []
        if not isinstance(self.histological_composition_measure, list):
            self.histological_composition_measure = [self.histological_composition_measure]
        self.histological_composition_measure = [v if isinstance(v, Entity) else Entity(**v) for v in self.histological_composition_measure]

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

        if self.quantity_collected is not None and not isinstance(self.quantity_collected, Quantity):
            self.quantity_collected = Quantity(**self.quantity_collected)

        if self.execution_observation is None:
            self.execution_observation = []
        if not isinstance(self.execution_observation, list):
            self.execution_observation = [self.execution_observation]
        self._normalize_inlined_slot(slot_name="execution_observation", slot_type=Observation, key_name="observation_type", inlined_as_list=True, keyed=False)

        if self.specimen_order is not None and not isinstance(self.specimen_order, CcdhString):
            self.specimen_order = CcdhString(self.specimen_order)

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

    observation_type: Union[str, "EnumCRDC-H.SpecimenQuantityObservation.observationType"] = None
    valueQuantity: Union[dict, Quantity] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.category"]] = None
    method_type: Optional[Union[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.methodType"], List[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.methodType"]]]] = empty_list()
    focus: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    subject: Optional[Union[dict, "Subject"]] = None
    performed_by: Optional[Union[dict, Organization]] = None
    valueEntity: Optional[Union[dict, Entity]] = None
    valueString: Optional[Union[str, CcdhString]] = None
    valueInteger: Optional[Union[Decimal, CcdhDecimal]] = None
    valueDecimal: Optional[Union[Decimal, CcdhDecimal]] = None
    valueBoolean: Optional[Union[bool, CcdhBoolean]] = None
    valueDateTime: Optional[Union[str, CcdhDateTime]] = None
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.SpecimenQuantityObservation.observationType):
            self.observation_type = EnumCRDC-H.SpecimenQuantityObservation.observationType(self.observation_type)

        if self.valueQuantity is None:
            raise ValueError("valueQuantity must be supplied")
        if not isinstance(self.valueQuantity, Quantity):
            self.valueQuantity = Quantity(**self.valueQuantity)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.SpecimenQuantityObservation.category):
            self.category = EnumCRDC-H.SpecimenQuantityObservation.category(self.category)

        if self.method_type is None:
            self.method_type = []
        if not isinstance(self.method_type, list):
            self.method_type = [self.method_type]
        self.method_type = [v if isinstance(v, EnumCRDC-H.SpecimenQuantityObservation.methodType) else EnumCRDC-H.SpecimenQuantityObservation.methodType(v) for v in self.method_type]

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

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept(self.valueCodeableConcept)

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

    id: Optional[Union[str, CcdhString]] = None
    dateTime: Optional[Union[str, CcdhDateTime]] = None
    offsetFromIndex: Optional[Union[dict, Quantity]] = None
    eventType: Optional[Union[Union[str, "EnumCRDC-H.TimePoint.eventType"], List[Union[str, "EnumCRDC-H.TimePoint.eventType"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.dateTime is not None and not isinstance(self.dateTime, CcdhDateTime):
            self.dateTime = CcdhDateTime(self.dateTime)

        if self.offsetFromIndex is not None and not isinstance(self.offsetFromIndex, Quantity):
            self.offsetFromIndex = Quantity(**self.offsetFromIndex)

        if self.eventType is None:
            self.eventType = []
        if not isinstance(self.eventType, list):
            self.eventType = [self.eventType]
        self.eventType = [v if isinstance(v, EnumCRDC-H.TimePoint.eventType) else EnumCRDC-H.TimePoint.eventType(v) for v in self.eventType]

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

    observation_type: Union[str, "EnumCRDC-H.TobaccoExposureObservation.observationType"] = None
    id: Optional[Union[str, CcdhString]] = None
    category: Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.category"]] = None
    method_type: Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.methodType"]] = None
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
    valueCodeableConcept: Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observation_type is None:
            raise ValueError("observation_type must be supplied")
        if not isinstance(self.observation_type, EnumCRDC-H.TobaccoExposureObservation.observationType):
            self.observation_type = EnumCRDC-H.TobaccoExposureObservation.observationType(self.observation_type)

        if self.id is not None and not isinstance(self.id, CcdhString):
            self.id = CcdhString(self.id)

        if self.category is not None and not isinstance(self.category, EnumCRDC-H.TobaccoExposureObservation.category):
            self.category = EnumCRDC-H.TobaccoExposureObservation.category(self.category)

        if self.method_type is not None and not isinstance(self.method_type, EnumCRDC-H.TobaccoExposureObservation.methodType):
            self.method_type = EnumCRDC-H.TobaccoExposureObservation.methodType(self.method_type)

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

        if self.valueCodeableConcept is not None and not isinstance(self.valueCodeableConcept, EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept):
            self.valueCodeableConcept = EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept(self.valueCodeableConcept)

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
    date_started: Optional[Union[dict, TimePoint]] = None
    date_ended: Optional[Union[dict, TimePoint]] = None
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

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**self.date_started)

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**self.date_ended)

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
class EnumCRDC-H.AlcoholExposureObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.AlcoholExposureObservation.category",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:29.670886+00:00",
    )

class EnumCRDC-H.AlcoholExposureObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.AlcoholExposureObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:30.231439+00:00",
    )

class EnumCRDC-H.AlcoholExposureObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.AlcoholExposureObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:30.460657+00:00",
    )

class EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H AlcoholExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H AlcoholExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:30.679480+00:00",
    )

class EnumCRDC-H.BodySite.site(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite site
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BodySite.site",
        description="Autogenerated Enumeration for CRDC-H BodySite site",
        code_set=None,
        code_set_version="2021-05-28T14:50:30.877729+00:00",
    )

class EnumCRDC-H.BodySite.qualifier(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BodySite qualifier
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BodySite.qualifier",
        description="Autogenerated Enumeration for CRDC-H BodySite qualifier",
        code_set=None,
        code_set_version="2021-05-28T14:50:31.075481+00:00",
    )

class EnumCRDC-H.BiologicProduct.productType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H BiologicProduct product_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.BiologicProduct.productType",
        description="Autogenerated Enumeration for CRDC-H BiologicProduct product_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:31.277025+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.category",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:31.461859+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:31.649816+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:31.833787+00:00",
    )

class EnumCRDC-H.CancerGradeObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.011737+00:00",
    )

class EnumCRDC-H.CancerGradeObservationSet.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservationSet category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservationSet.category",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservationSet category",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.192944+00:00",
    )

class EnumCRDC-H.CancerGradeObservationSet.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerGradeObservationSet method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerGradeObservationSet.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerGradeObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.386780+00:00",
    )

class EnumCRDC-H.CancerStageObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.category",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.575253+00:00",
    )

class EnumCRDC-H.CancerStageObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.754540+00:00",
    )

class EnumCRDC-H.CancerStageObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:32.950052+00:00",
    )

class EnumCRDC-H.CancerStageObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:33.134744+00:00",
    )

class EnumCRDC-H.CancerStageObservationSet.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservationSet category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservationSet.category",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservationSet category",
        code_set=None,
        code_set_version="2021-05-28T14:50:33.300818+00:00",
    )

class EnumCRDC-H.CancerStageObservationSet.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H CancerStageObservationSet method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.CancerStageObservationSet.methodType",
        description="Autogenerated Enumeration for CRDC-H CancerStageObservationSet method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:33.474810+00:00",
    )

class EnumCRDC-H.Diagnosis.condition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis condition
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.condition",
        description="Autogenerated Enumeration for CRDC-H Diagnosis condition",
        code_set=None,
        code_set_version="2021-05-28T14:50:33.662724+00:00",
    )

class EnumCRDC-H.Diagnosis.morphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis morphology
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.morphology",
        description="Autogenerated Enumeration for CRDC-H Diagnosis morphology",
        code_set=None,
        code_set_version="2021-05-28T14:50:33.853634+00:00",
    )

class EnumCRDC-H.Diagnosis.diseaseStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis disease_status
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.diseaseStatus",
        description="Autogenerated Enumeration for CRDC-H Diagnosis disease_status",
        code_set=None,
        code_set_version="2021-05-28T14:50:34.070281+00:00",
    )

class EnumCRDC-H.Diagnosis.methodOfDiagnosis(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Diagnosis.methodOfDiagnosis",
        description="Autogenerated Enumeration for CRDC-H Diagnosis method_of_diagnosis",
        code_set=None,
        code_set_version="2021-05-28T14:50:34.260752+00:00",
    )

class EnumCRDC-H.DimensionalObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.DimensionalObservation.category",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:34.483677+00:00",
    )

class EnumCRDC-H.DimensionalObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.DimensionalObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:34.691382+00:00",
    )

class EnumCRDC-H.DimensionalObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H DimensionalObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.DimensionalObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H DimensionalObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:34.889316+00:00",
    )

class EnumCRDC-H.Document.documentType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Document document_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Document.documentType",
        description="Autogenerated Enumeration for CRDC-H Document document_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:35.155740+00:00",
    )

class EnumCRDC-H.EnvironmentalExposureObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.EnvironmentalExposureObservation.category",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:35.503081+00:00",
    )

class EnumCRDC-H.EnvironmentalExposureObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.EnvironmentalExposureObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:35.719891+00:00",
    )

class EnumCRDC-H.EnvironmentalExposureObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.EnvironmentalExposureObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:35.933852+00:00",
    )

class EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H EnvironmentalExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:36.178287+00:00",
    )

class EnumCRDC-H.Identifier.type(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Identifier type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Identifier.type",
        description="Autogenerated Enumeration for CRDC-H Identifier type",
        code_set=None,
        code_set_version="2021-05-28T14:50:36.362510+00:00",
    )

class EnumCRDC-H.Observation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.category",
        description="Autogenerated Enumeration for CRDC-H Observation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:36.618397+00:00",
    )

class EnumCRDC-H.Observation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.observationType",
        description="Autogenerated Enumeration for CRDC-H Observation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:36.828493+00:00",
    )

class EnumCRDC-H.Observation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.methodType",
        description="Autogenerated Enumeration for CRDC-H Observation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:37.057083+00:00",
    )

class EnumCRDC-H.Observation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Observation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Observation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:37.293753+00:00",
    )

class EnumCRDC-H.Quantity.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Quantity.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H Quantity valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:37.544802+00:00",
    )

class EnumCRDC-H.ResearchProject.researchProjectType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchProject research_project_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchProject.researchProjectType",
        description="Autogenerated Enumeration for CRDC-H ResearchProject research_project_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:37.740843+00:00",
    )

class EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchSubject.primaryDiagnosisCondition",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject primary_diagnosis_condition",
        code_set=None,
        code_set_version="2021-05-28T14:50:38.694625+00:00",
    )

class EnumCRDC-H.ResearchSubject.indexTimepoint(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.ResearchSubject.indexTimepoint",
        description="Autogenerated Enumeration for CRDC-H ResearchSubject index_timepoint",
        code_set=None,
        code_set_version="2021-05-28T14:50:38.891461+00:00",
    )

class EnumCRDC-H.Specimen.specimenType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen specimen_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.specimenType",
        description="Autogenerated Enumeration for CRDC-H Specimen specimen_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:39.092388+00:00",
    )

class EnumCRDC-H.Specimen.analyteType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen analyte_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.analyteType",
        description="Autogenerated Enumeration for CRDC-H Specimen analyte_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:39.303632+00:00",
    )

class EnumCRDC-H.Specimen.sourceMaterialType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen source_material_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.sourceMaterialType",
        description="Autogenerated Enumeration for CRDC-H Specimen source_material_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:39.578283+00:00",
    )

class EnumCRDC-H.Specimen.tumorStatusAtCollection(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.tumorStatusAtCollection",
        description="Autogenerated Enumeration for CRDC-H Specimen tumor_status_at_collection",
        code_set=None,
        code_set_version="2021-05-28T14:50:39.850361+00:00",
    )

class EnumCRDC-H.Specimen.cellularCompositionType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.cellularCompositionType",
        description="Autogenerated Enumeration for CRDC-H Specimen cellular_composition_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:40.062982+00:00",
    )

class EnumCRDC-H.Specimen.generalTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.generalTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen general_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-28T14:50:40.271728+00:00",
    )

class EnumCRDC-H.Specimen.specificTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.specificTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen specific_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-28T14:50:40.475471+00:00",
    )

class EnumCRDC-H.Specimen.preinvasiveTissueMorphology(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.preinvasiveTissueMorphology",
        description="Autogenerated Enumeration for CRDC-H Specimen preinvasive_tissue_morphology",
        code_set=None,
        code_set_version="2021-05-28T14:50:40.681008+00:00",
    )

class EnumCRDC-H.Specimen.morphologyAssessorRole(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.morphologyAssessorRole",
        description="Autogenerated Enumeration for CRDC-H Specimen morphology_assessor_role",
        code_set=None,
        code_set_version="2021-05-28T14:50:40.867721+00:00",
    )

class EnumCRDC-H.Specimen.morphlogyAssessmentMethod(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.morphlogyAssessmentMethod",
        description="Autogenerated Enumeration for CRDC-H Specimen morphlogy_assessment_method",
        code_set=None,
        code_set_version="2021-05-28T14:50:41.055283+00:00",
    )

class EnumCRDC-H.Specimen.degreeOfDysplasia(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.degreeOfDysplasia",
        description="Autogenerated Enumeration for CRDC-H Specimen degree_of_dysplasia",
        code_set=None,
        code_set_version="2021-05-28T14:50:41.290205+00:00",
    )

class EnumCRDC-H.Specimen.sectionLocation(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Specimen section_location
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Specimen.sectionLocation",
        description="Autogenerated Enumeration for CRDC-H Specimen section_location",
        code_set=None,
        code_set_version="2021-05-28T14:50:41.484355+00:00",
    )

class EnumCRDC-H.SpecimenContainer.containerType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer container_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenContainer.containerType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer container_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:41.670433+00:00",
    )

class EnumCRDC-H.SpecimenContainer.chargeType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenContainer.chargeType",
        description="Autogenerated Enumeration for CRDC-H SpecimenContainer charge_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:41.867911+00:00",
    )

class EnumCRDC-H.SpecimenCreationActivity.activityType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity activity_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.activityType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity activity_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:42.049261+00:00",
    )

class EnumCRDC-H.SpecimenCreationActivity.collectionMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.collectionMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity collection_method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:42.297693+00:00",
    )

class EnumCRDC-H.SpecimenCreationActivity.derivationMethodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenCreationActivity.derivationMethodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenCreationActivity derivation_method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:42.470628+00:00",
    )

class EnumCRDC-H.SpecimenQuantityObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenQuantityObservation.category",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:42.664368+00:00",
    )

class EnumCRDC-H.SpecimenQuantityObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenQuantityObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:42.908260+00:00",
    )

class EnumCRDC-H.SpecimenQuantityObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenQuantityObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:43.091032+00:00",
    )

class EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H SpecimenQuantityObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:43.284177+00:00",
    )

class EnumCRDC-H.SpecimenProcessingActivity.activityType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity activity_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenProcessingActivity.activityType",
        description="Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity activity_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:43.636967+00:00",
    )

class EnumCRDC-H.SpecimenProcessingActivity.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenProcessingActivity.methodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenProcessingActivity method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:43.818989+00:00",
    )

class EnumCRDC-H.SpecimenStorageActivity.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.SpecimenStorageActivity.methodType",
        description="Autogenerated Enumeration for CRDC-H SpecimenStorageActivity method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:43.989692+00:00",
    )

class EnumCRDC-H.Subject.species(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject species
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.species",
        description="Autogenerated Enumeration for CRDC-H Subject species",
        code_set=None,
        code_set_version="2021-05-28T14:50:44.178855+00:00",
    )

class EnumCRDC-H.Subject.breed(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject breed
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.breed",
        description="Autogenerated Enumeration for CRDC-H Subject breed",
        code_set=None,
        code_set_version="2021-05-28T14:50:44.357626+00:00",
    )

class EnumCRDC-H.Subject.sex(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject sex
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.sex",
        description="Autogenerated Enumeration for CRDC-H Subject sex",
        code_set=None,
        code_set_version="2021-05-28T14:50:44.564910+00:00",
    )

class EnumCRDC-H.Subject.ethnicity(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject ethnicity
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.ethnicity",
        description="Autogenerated Enumeration for CRDC-H Subject ethnicity",
        code_set=None,
        code_set_version="2021-05-28T14:50:44.787214+00:00",
    )

class EnumCRDC-H.Subject.race(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject race
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.race",
        description="Autogenerated Enumeration for CRDC-H Subject race",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.001779+00:00",
    )

class EnumCRDC-H.Subject.vitalStatus(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject vital_status
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.vitalStatus",
        description="Autogenerated Enumeration for CRDC-H Subject vital_status",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.214314+00:00",
    )

class EnumCRDC-H.Subject.causeOfDeath(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Subject cause_of_death
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Subject.causeOfDeath",
        description="Autogenerated Enumeration for CRDC-H Subject cause_of_death",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.429469+00:00",
    )

class EnumCRDC-H.Substance.substanceType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance substance_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Substance.substanceType",
        description="Autogenerated Enumeration for CRDC-H Substance substance_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.616262+00:00",
    )

class EnumCRDC-H.Substance.role(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Substance role
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Substance.role",
        description="Autogenerated Enumeration for CRDC-H Substance role",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.815333+00:00",
    )

class EnumCRDC-H.TimePoint.eventType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TimePoint eventType
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TimePoint.eventType",
        description="Autogenerated Enumeration for CRDC-H TimePoint eventType",
        code_set=None,
        code_set_version="2021-05-28T14:50:45.998620+00:00",
    )

class EnumCRDC-H.TobaccoExposureObservation.category(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation category
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TobaccoExposureObservation.category",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation category",
        code_set=None,
        code_set_version="2021-05-28T14:50:46.263397+00:00",
    )

class EnumCRDC-H.TobaccoExposureObservation.observationType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation observation_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TobaccoExposureObservation.observationType",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation observation_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:46.448947+00:00",
    )

class EnumCRDC-H.TobaccoExposureObservation.methodType(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation method_type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TobaccoExposureObservation.methodType",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation method_type",
        code_set=None,
        code_set_version="2021-05-28T14:50:46.633059+00:00",
    )

class EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H TobaccoExposureObservation valueCodeableConcept
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept",
        description="Autogenerated Enumeration for CRDC-H TobaccoExposureObservation valueCodeableConcept",
        code_set=None,
        code_set_version="2021-05-28T14:50:46.846185+00:00",
    )

class EnumCRDC-H.Treatment.type(EnumDefinitionImpl):
    """
    Autogenerated Enumeration for CRDC-H Treatment type
    """
    _defn = EnumDefinition(
        name="EnumCRDC-H.Treatment.type",
        description="Autogenerated Enumeration for CRDC-H Treatment type",
        code_set=None,
        code_set_version="2021-05-28T14:50:47.054555+00:00",
    )

# Slots
class slots:
    pass

slots.alcoholExposureObservation__id = Slot(uri=CCDH.id, name="alcoholExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.alcoholExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.alcoholExposureObservation__category = Slot(uri=CCDH.category, name="alcoholExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.alcoholExposureObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.category"]])

slots.alcoholExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="alcoholExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.alcoholExposureObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.AlcoholExposureObservation.observationType"])

slots.alcoholExposureObservation__method_type = Slot(uri=CCDH.method_type, name="alcoholExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.alcoholExposureObservation__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.methodType"]])

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
                   model_uri=CCDH.alcoholExposureObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.AlcoholExposureObservation.valueCodeableConcept"]])

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

slots.cancerGradeObservation__id = Slot(uri=CCDH.id, name="cancerGradeObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerGradeObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerGradeObservation__category = Slot(uri=CCDH.category, name="cancerGradeObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerGradeObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.category"]])

slots.cancerGradeObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerGradeObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerGradeObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.CancerGradeObservation.observationType"])

slots.cancerGradeObservation__method_type = Slot(uri=CCDH.method_type, name="cancerGradeObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGradeObservation__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.methodType"]])

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
                   model_uri=CCDH.cancerGradeObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservation.valueCodeableConcept"]])

slots.cancerGradeObservationSet__id = Slot(uri=CCDH.id, name="cancerGradeObservationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerGradeObservationSet__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerGradeObservationSet__category = Slot(uri=CCDH.category, name="cancerGradeObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerGradeObservationSet__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerGradeObservationSet.category"]])

slots.cancerGradeObservationSet__focus = Slot(uri=CCDH.focus, name="cancerGradeObservationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerGradeObservationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.cancerGradeObservationSet__subject = Slot(uri=CCDH.subject, name="cancerGradeObservationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerGradeObservationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerGradeObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerGradeObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerGradeObservationSet__method_type, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"], List[Union[str, "EnumCRDC-H.CancerGradeObservationSet.methodType"]]]])

slots.cancerGradeObservationSet__performed_by = Slot(uri=CCDH.performed_by, name="cancerGradeObservationSet__performed_by", curie=CCDH.curie('performed_by'),
                   model_uri=CCDH.cancerGradeObservationSet__performed_by, domain=None, range=Optional[Union[dict, Organization]])

slots.cancerGradeObservationSet__observations = Slot(uri=CCDH.observations, name="cancerGradeObservationSet__observations", curie=CCDH.curie('observations'),
                   model_uri=CCDH.cancerGradeObservationSet__observations, domain=None, range=Optional[Union[Union[dict, CancerGradeObservation], List[Union[dict, CancerGradeObservation]]]])

slots.cancerStageObservation__id = Slot(uri=CCDH.id, name="cancerStageObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerStageObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerStageObservation__category = Slot(uri=CCDH.category, name="cancerStageObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerStageObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservation.category"]])

slots.cancerStageObservation__observation_type = Slot(uri=CCDH.observation_type, name="cancerStageObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.cancerStageObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.CancerStageObservation.observationType"])

slots.cancerStageObservation__method_type = Slot(uri=CCDH.method_type, name="cancerStageObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageObservation__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservation.methodType"]])

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
                   model_uri=CCDH.cancerStageObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservation.valueCodeableConcept"]])

slots.cancerStageObservationSet__id = Slot(uri=CCDH.id, name="cancerStageObservationSet__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.cancerStageObservationSet__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.cancerStageObservationSet__category = Slot(uri=CCDH.category, name="cancerStageObservationSet__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.cancerStageObservationSet__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.CancerStageObservationSet.category"]])

slots.cancerStageObservationSet__focus = Slot(uri=CCDH.focus, name="cancerStageObservationSet__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.cancerStageObservationSet__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.cancerStageObservationSet__subject = Slot(uri=CCDH.subject, name="cancerStageObservationSet__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.cancerStageObservationSet__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.cancerStageObservationSet__method_type = Slot(uri=CCDH.method_type, name="cancerStageObservationSet__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.cancerStageObservationSet__method_type, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"], List[Union[str, "EnumCRDC-H.CancerStageObservationSet.methodType"]]]])

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

slots.diagnosis__supporting_observations = Slot(uri=CCDH.supporting_observations, name="diagnosis__supporting_observations", curie=CCDH.curie('supporting_observations'),
                   model_uri=CCDH.diagnosis__supporting_observations, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.dimensionalObservation__id = Slot(uri=CCDH.id, name="dimensionalObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.dimensionalObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.dimensionalObservation__category = Slot(uri=CCDH.category, name="dimensionalObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.dimensionalObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.DimensionalObservation.category"]])

slots.dimensionalObservation__observation_type = Slot(uri=CCDH.observation_type, name="dimensionalObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.dimensionalObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.DimensionalObservation.observationType"])

slots.dimensionalObservation__method_type = Slot(uri=CCDH.method_type, name="dimensionalObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.dimensionalObservation__method_type, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.DimensionalObservation.methodType"], List[Union[str, "EnumCRDC-H.DimensionalObservation.methodType"]]]])

slots.dimensionalObservation__focus = Slot(uri=CCDH.focus, name="dimensionalObservation__focus", curie=CCDH.curie('focus'),
                   model_uri=CCDH.dimensionalObservation__focus, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.dimensionalObservation__subject = Slot(uri=CCDH.subject, name="dimensionalObservation__subject", curie=CCDH.curie('subject'),
                   model_uri=CCDH.dimensionalObservation__subject, domain=None, range=Optional[Union[dict, Subject]])

slots.dimensionalObservation__valueQuantity = Slot(uri=CCDH.valueQuantity, name="dimensionalObservation__valueQuantity", curie=CCDH.curie('valueQuantity'),
                   model_uri=CCDH.dimensionalObservation__valueQuantity, domain=None, range=Union[dict, Quantity])

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

slots.environmentalExposureObservation__id = Slot(uri=CCDH.id, name="environmentalExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.environmentalExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.environmentalExposureObservation__category = Slot(uri=CCDH.category, name="environmentalExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.environmentalExposureObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.category"]])

slots.environmentalExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="environmentalExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.environmentalExposureObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.observationType"])

slots.environmentalExposureObservation__method_type = Slot(uri=CCDH.method_type, name="environmentalExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.environmentalExposureObservation__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.methodType"]])

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
                   model_uri=CCDH.environmentalExposureObservation__valueCodeableConcept, domain=None, range=Union[str, "EnumCRDC-H.EnvironmentalExposureObservation.valueCodeableConcept"])

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
                   model_uri=CCDH.identifier__type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Identifier.type"]])

slots.observation__id = Slot(uri=CCDH.id, name="observation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.observation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.observation__category = Slot(uri=CCDH.category, name="observation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.observation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.Observation.category"]])

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
                   model_uri=CCDH.researchProject__primary_anatomic_site, domain=None, range=Optional[Union[Union[dict, BodySite], List[Union[dict, BodySite]]]])

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
                   model_uri=CCDH.researchSubject__primary_diagnosis_site, domain=None, range=Optional[Union[dict, BodySite]])

slots.researchSubject__primary_diagnosis = Slot(uri=CCDH.primary_diagnosis, name="researchSubject__primary_diagnosis", curie=CCDH.curie('primary_diagnosis'),
                   model_uri=CCDH.researchSubject__primary_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

slots.researchSubject__comorbid_diagnosis = Slot(uri=CCDH.comorbid_diagnosis, name="researchSubject__comorbid_diagnosis", curie=CCDH.curie('comorbid_diagnosis'),
                   model_uri=CCDH.researchSubject__comorbid_diagnosis, domain=None, range=Optional[Union[Union[dict, Diagnosis], List[Union[dict, Diagnosis]]]])

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
                   model_uri=CCDH.specimen__quantity_measure, domain=None, range=Optional[Union[Union[dict, SpecimenQuantityObservation], List[Union[dict, SpecimenQuantityObservation]]]])

slots.specimen__quality_measure = Slot(uri=CCDH.quality_measure, name="specimen__quality_measure", curie=CCDH.curie('quality_measure'),
                   model_uri=CCDH.specimen__quality_measure, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimen__cellular_composition_type = Slot(uri=CCDH.cellular_composition_type, name="specimen__cellular_composition_type", curie=CCDH.curie('cellular_composition_type'),
                   model_uri=CCDH.specimen__cellular_composition_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.Specimen.cellularCompositionType"]])

slots.specimen__histological_composition_measure = Slot(uri=CCDH.histological_composition_measure, name="specimen__histological_composition_measure", curie=CCDH.curie('histological_composition_measure'),
                   model_uri=CCDH.specimen__histological_composition_measure, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

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

slots.specimenCreationActivity__quantity_collected = Slot(uri=CCDH.quantity_collected, name="specimenCreationActivity__quantity_collected", curie=CCDH.curie('quantity_collected'),
                   model_uri=CCDH.specimenCreationActivity__quantity_collected, domain=None, range=Optional[Union[dict, Quantity]])

slots.specimenCreationActivity__execution_observation = Slot(uri=CCDH.execution_observation, name="specimenCreationActivity__execution_observation", curie=CCDH.curie('execution_observation'),
                   model_uri=CCDH.specimenCreationActivity__execution_observation, domain=None, range=Optional[Union[Union[dict, Observation], List[Union[dict, Observation]]]])

slots.specimenCreationActivity__specimen_order = Slot(uri=CCDH.specimen_order, name="specimenCreationActivity__specimen_order", curie=CCDH.curie('specimen_order'),
                   model_uri=CCDH.specimenCreationActivity__specimen_order, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQuantityObservation__id = Slot(uri=CCDH.id, name="specimenQuantityObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.specimenQuantityObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.specimenQuantityObservation__category = Slot(uri=CCDH.category, name="specimenQuantityObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.specimenQuantityObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.category"]])

slots.specimenQuantityObservation__observation_type = Slot(uri=CCDH.observation_type, name="specimenQuantityObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.specimenQuantityObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.SpecimenQuantityObservation.observationType"])

slots.specimenQuantityObservation__method_type = Slot(uri=CCDH.method_type, name="specimenQuantityObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.specimenQuantityObservation__method_type, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.methodType"], List[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.methodType"]]]])

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
                   model_uri=CCDH.specimenQuantityObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.SpecimenQuantityObservation.valueCodeableConcept"]])

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

slots.timePoint__id = Slot(uri=CCDH.id, name="timePoint__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.timePoint__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.timePoint__dateTime = Slot(uri=CCDH.dateTime, name="timePoint__dateTime", curie=CCDH.curie('dateTime'),
                   model_uri=CCDH.timePoint__dateTime, domain=None, range=Optional[Union[str, CcdhDateTime]])

slots.timePoint__offsetFromIndex = Slot(uri=CCDH.offsetFromIndex, name="timePoint__offsetFromIndex", curie=CCDH.curie('offsetFromIndex'),
                   model_uri=CCDH.timePoint__offsetFromIndex, domain=None, range=Optional[Union[dict, Quantity]])

slots.timePoint__eventType = Slot(uri=CCDH.eventType, name="timePoint__eventType", curie=CCDH.curie('eventType'),
                   model_uri=CCDH.timePoint__eventType, domain=None, range=Optional[Union[Union[str, "EnumCRDC-H.TimePoint.eventType"], List[Union[str, "EnumCRDC-H.TimePoint.eventType"]]]])

slots.timePeriod__periodStart_start = Slot(uri=CCDH.periodStart_start, name="timePeriod__periodStart_start", curie=CCDH.curie('periodStart_start'),
                   model_uri=CCDH.timePeriod__periodStart_start, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePeriod__periodEnd_end = Slot(uri=CCDH.periodEnd_end, name="timePeriod__periodEnd_end", curie=CCDH.curie('periodEnd_end'),
                   model_uri=CCDH.timePeriod__periodEnd_end, domain=None, range=Optional[Union[dict, TimePoint]])

slots.tobaccoExposureObservation__id = Slot(uri=CCDH.id, name="tobaccoExposureObservation__id", curie=CCDH.curie('id'),
                   model_uri=CCDH.tobaccoExposureObservation__id, domain=None, range=Optional[Union[str, CcdhString]])

slots.tobaccoExposureObservation__category = Slot(uri=CCDH.category, name="tobaccoExposureObservation__category", curie=CCDH.curie('category'),
                   model_uri=CCDH.tobaccoExposureObservation__category, domain=None, range=Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.category"]])

slots.tobaccoExposureObservation__observation_type = Slot(uri=CCDH.observation_type, name="tobaccoExposureObservation__observation_type", curie=CCDH.curie('observation_type'),
                   model_uri=CCDH.tobaccoExposureObservation__observation_type, domain=None, range=Union[str, "EnumCRDC-H.TobaccoExposureObservation.observationType"])

slots.tobaccoExposureObservation__method_type = Slot(uri=CCDH.method_type, name="tobaccoExposureObservation__method_type", curie=CCDH.curie('method_type'),
                   model_uri=CCDH.tobaccoExposureObservation__method_type, domain=None, range=Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.methodType"]])

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
                   model_uri=CCDH.tobaccoExposureObservation__valueCodeableConcept, domain=None, range=Optional[Union[str, "EnumCRDC-H.TobaccoExposureObservation.valueCodeableConcept"]])

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

slots.treatment__date_started = Slot(uri=CCDH.date_started, name="treatment__date_started", curie=CCDH.curie('date_started'),
                   model_uri=CCDH.treatment__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.treatment__date_ended = Slot(uri=CCDH.date_ended, name="treatment__date_ended", curie=CCDH.curie('date_ended'),
                   model_uri=CCDH.treatment__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

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
