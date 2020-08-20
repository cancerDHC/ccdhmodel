
# Specimen schema


Any material sample taken from a biological entity (living or dead), or taken from a physical object or the environment. (Adapted from FHIR) Specimens are usually collected as an example of their kind, often for use in some investigation.


### Classes

 * [Coding](Coding.md)
 * [Entity](Entity.md) - Any resource that has its own identifier
    * [ConditionDiagnosis](ConditionDiagnosis.md)
    * [DocumentReference](DocumentReference.md)
    * [Organization](Organization.md)
    * [Project](Project.md)
    * [Specimen](Specimen.md)
    * [Visit](Visit.md)
 * [Identifier](Identifier.md)
 * [PatientOrBiologicalyDerivedMaterial](PatientOrBiologicalyDerivedMaterial.md)
    * [BiologicallyDerivedMaterial](BiologicallyDerivedMaterial.md)
    * [Patient](Patient.md)
 * [Quantity](Quantity.md)

### Mixins


### Slots

 * [analyte_type](analyte_type.md) - -> When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
    * [Specimen➞analyte_type](Specimen_analyte_type.md)
 * [associated_project](associated_project.md) - The Project associated with the specimen.
    * [Specimen➞associated_project](Specimen_associated_project.md)
 * [derived_from_specimen](derived_from_specimen.md)
    * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)
 * [derived_from_subject](derived_from_subject.md)
    * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)
 * [description](description.md) - -> A free text field to capture additional information or explanation about the specimen.
    * [Specimen➞description](Specimen_description.md)
 * [id](id.md)
    * [Specimen➞id](Specimen_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
 * [identifier](identifier.md) - -> A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier).
    * [Specimen➞identifier](Specimen_identifier.md)
 * [provided_by](provided_by.md) - The organization/center that provided the specimen.
    * [Specimen➞provided_by](Specimen_provided_by.md)
 * [source_material_type](source_material_type.md) - -> The general kind of material from which the specimen was derived, indicating the physical nature of the source material.
    * [Specimen➞source_material_type](Specimen_source_material_type.md)
 * [specimen_type](specimen_type.md) - -> The high-level type of the specimen, based on its how it has been derived from the original extracted sample.
    * [Specimen➞specimen_type](Specimen_specimen_type.md)

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Literal](types/Literal.md)  ([String](types/String.md)) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
