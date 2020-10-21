
# Ccdh-Mvp schema





### Classes

 * [Coding](Coding.md)
 * [Entity](Entity.md) - Any resource that has its own identifier
    * [Patient](Patient.md)
    * [Project](Project.md)
    * [ResearchSubject](ResearchSubject.md)
    * [Specimen](Specimen.md)
 * [Identifier](Identifier.md)
 * [Quantity](Quantity.md)

### Mixins


### Slots

 * [analyte_concentration](analyte_concentration.md) - The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'analyte', or an 'aliquot' derived from an analyte). e.g. the concentration of DNA in a specimen created through extracting DNA from a blood sample.
    * [Specimen➞analyte_concentration](Specimen_analyte_concentration.md)
 * [analyte_concentration_method](analyte_concentration_method.md) - The method used to determine the concentration of purified analyte  within a solution.
    * [Specimen➞analyte_concentration_method](Specimen_analyte_concentration_method.md)
 * [analyte_type](analyte_type.md) - When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
    * [Specimen➞analyte_type](Specimen_analyte_type.md)
 * [associated_project](associated_project.md) - The Project associated with the specimen.
    * [Patient➞associated_project](Patient_associated_project.md) - A reference to the Project(s) of which this ResearchSubject is a member
    * [Specimen➞associated_project](Specimen_associated_project.md)
 * [cellular_composition](cellular_composition.md) - The cellular composition of the sample
    * [Specimen➞cellular_composition](Specimen_cellular_composition.md)
 * [code](code.md) - The value of the code itself.
    * [Coding➞code](Coding_code.md)
 * [comparator](comparator.md) -  how to understand the value  . . .   < | <= | >= | >
    * [Quantity➞comparator](Quantity_comparator.md)
 * [current_volume](current_volume.md) - The current total volume of the specimen, at the time of recording.
    * [Specimen➞current_volume](Specimen_current_volume.md)
 * [current_weight](current_weight.md) - The current weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
    * [Specimen➞current_weight](Specimen_current_weight.md)
 * [derived_from_specimen](derived_from_specimen.md) - A source/parent specimen from which this one was directly derived.
    * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)
 * [derived_from_subject](derived_from_subject.md) - The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.
    * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)
 * [display](display.md) - A human-readable name for the code.
    * [Coding➞display](Coding_display.md)
 * [general_tissue_morphology](general_tissue_morphology.md) - A term describing at a high-level the kind of tissue collected in a specimen, with respect to disease status or proximity to tumor tissue (e.g. is it normal, abnormal, tumor, tumor-adjacent). 
    * [Specimen➞general_tissue_morphology](Specimen_general_tissue_morphology.md)
 * [id](id.md)
    * [Project➞id](Project_id.md)
    * [ResearchSubject➞id](ResearchSubject_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
    * [Specimen➞id](Specimen_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
 * [identifier](identifier.md) - A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). 
    * [ResearchSubject➞identifier](ResearchSubject_identifier.md) - A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier. 
    * [Specimen➞identifier](Specimen_identifier.md)
 * [matched_normal_flag](matched_normal_flag.md) - A flag indicating that there is no matched normal aliquot for this case that can be used for variant calling purposes.
    * [Specimen➞matched_normal_flag](Specimen_matched_normal_flag.md)
 * [primary_disease_site](primary_disease_site.md) - The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.
    * [ResearchSubject➞primary_disease_site](ResearchSubject_primary_disease_site.md)
 * [primary_disease_type](primary_disease_type.md) - The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). 
    * [ResearchSubject➞primary_disease_type](ResearchSubject_primary_disease_type.md)
 * [qualification_status_flag](qualification_status_flag.md) - A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
    * [Specimen➞qualification_status_flag](Specimen_qualification_status_flag.md)
 * [source_material_type](source_material_type.md) - The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
    * [Specimen➞source_material_type](Specimen_source_material_type.md)
 * [specific_tissue_morphology](specific_tissue_morphology.md) - A term describing the specific pathology exhibited by the tissue in a specimen.
    * [Specimen➞specific_tissue_morphology](Specimen_specific_tissue_morphology.md)
 * [specimen_type](specimen_type.md) - The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 
    * [Specimen➞specimen_type](Specimen_specimen_type.md)
 * [system](system.md) - The system or namespace that defines the identifier.
    * [Coding➞system](Coding_system.md) - The code system where the code is defined.
    * [Identifier➞system](Identifier_system.md)
 * [taxon](taxon.md) - The taxonomic group (e.g. species) of the patient.
    * [Patient➞taxon](Patient_taxon.md)
 * [type](type.md) - A code that defines the type of the identifier.
    * [Identifier➞type](Identifier_type.md)
 * [unit](unit.md) - Unit representation (e.g. mg, mL)
    * [Quantity➞unit](Quantity_unit.md)
 * [value](value.md) - The value of the identifier, as defined by the system.
    * [Identifier➞value](Identifier_value.md)
    * [Quantity➞value](Quantity_value.md) - Numerical value (with implicit precision)
 * [version](version.md) - The version of the code system.
    * [Coding➞version](Coding_version.md)

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
 * [Url](types/Url.md)  ([String](types/String.md)) 
