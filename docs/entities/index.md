
# Ccdh-Mvp schema





### Classes

 * [CodeableConcept](CodeableConcept.md)
 * [Coding](Coding.md) - A structured representation of a coded/enumerated data value, that includes additional metadata about the code and code system.
 * [Entity](Entity.md) - Any resource that has its own identifier
     * [Patient](Patient.md)
     * [Project](Project.md)
     * [ResearchSubject](ResearchSubject.md) - A research subject is the entity of interest in a research study, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.
     * [Specimen](Specimen.md) - Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.
 * [Identifier](Identifier.md)
 * [Quantity](Quantity.md) - A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including a value and unit.

### Mixins


### Slots

 * [➞coding](codeableConcept__coding.md) - A reference to a code defined by a terminology system
 * [➞text](codeableConcept__text.md) - A human language representation of the concept represented by the Coding
 * [➞code](coding__code.md) - The value of the code itself.
 * [➞display](coding__display.md) - A human-readable name for the code.
 * [➞system](coding__system.md) - The code system where the code is defined.
 * [➞version](coding__version.md) - The version of the code system.
 * [id](id.md)
     * [Patient➞id](Patient_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
     * [Project➞id](Project_id.md)
     * [ResearchSubject➞id](ResearchSubject_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
     * [Specimen➞id](Specimen_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
 * [➞system](identifier__system.md) - The system or namespace that defines the identifier.
 * [➞type](identifier__type.md) - A code that defines the type of the identifier.
 * [➞value](identifier__value.md) - The value of the identifier, as defined by the system.
 * [➞identifier](patient__identifier.md) - A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems. 
 * [➞taxon](patient__taxon.md) - The taxonomic group (e.g. species) of the patient.
 * [➞comparator](quantity__comparator.md) - How to understand the value  . . .   < | <= | >= | >
 * [➞unit](quantity__unit.md) - Unit representation (e.g. mg, mL)
 * [➞value](quantity__value.md) - Numerical value (with implicit precision)
 * [➞associated_patient](researchSubject__associated_patient.md) - A reference to the Patient that is this ResearchSubject
 * [➞associated_project](researchSubject__associated_project.md) - A reference to the Project(s) of which this ResearchSubject is a member
 * [➞identifier](researchSubject__identifier.md) - A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier. 
 * [➞primary_disease_site](researchSubject__primary_disease_site.md) - The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.
 * [➞primary_disease_type](researchSubject__primary_disease_type.md) - The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). 
 * [➞analyte_concentration](specimen__analyte_concentration.md) - The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'analyte', or an 'aliquot' derived from an analyte). e.g. the concentration of DNA in a specimen created through extracting DNA from a blood sample.
 * [➞analyte_concentration_method](specimen__analyte_concentration_method.md) - The method used to determine the concentration of purified analyte  within a solution.
 * [➞analyte_type](specimen__analyte_type.md) - When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
 * [➞associated_project](specimen__associated_project.md) - The Project associated with the specimen.
 * [➞cellular_composition](specimen__cellular_composition.md) - The cellular composition of the sample
 * [➞current_volume](specimen__current_volume.md) - The current total volume of the specimen, at the time of recording.
 * [➞current_weight](specimen__current_weight.md) - The current weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
 * [➞derived_from_specimen](specimen__derived_from_specimen.md) - A source/parent specimen from which this one was directly derived.
 * [➞derived_from_subject](specimen__derived_from_subject.md) - The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.
 * [➞general_tissue_morphology](specimen__general_tissue_morphology.md) - A term describing at a high-level the kind of tissue collected in a specimen, with respect to disease status or proximity to tumor tissue (e.g. is it normal, abnormal, tumor, tumor-adjacent). 
 * [➞identifier](specimen__identifier.md) - A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). 
 * [➞matched_normal_flag](specimen__matched_normal_flag.md) - A flag indicating that there is no matched normal aliquot for this case that can be used for variant calling purposes.
 * [➞qualification_status_flag](specimen__qualification_status_flag.md) - A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
 * [➞source_material_type](specimen__source_material_type.md) - The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
 * [➞specific_tissue_morphology](specimen__specific_tissue_morphology.md) - A term describing the specific pathology exhibited by the tissue in a specimen.
 * [➞specimen_type](specimen__specimen_type.md) - The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 

### Types


#### Built in

 * **Bool**
 * **Decimal**
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
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [Url](types/Url.md)  ([String](types/String.md)) 
