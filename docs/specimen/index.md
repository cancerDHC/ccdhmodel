
# Specimen schema


Any material sample taken from a biological entity (living or dead), or taken from a physical object or the environment. (Adapted from FHIR) 
Specimens are usually collected as an example of their kind, often for use in some investigation.


### Classes

 * [BiologicallyDerivedProduct](BiologicallyDerivedProduct.md)
 * [BodyStructure](BodyStructure.md)
 * [Coding](Coding.md)
 * [DataContainer](DataContainer.md)
 * [Entity](Entity.md) - Any resource that has its own identifier
    * [ConditionDiagnosis](ConditionDiagnosis.md)
    * [DocumentReference](DocumentReference.md)
    * [Organization](Organization.md)
    * [Project](Project.md)
    * [Specimen](Specimen.md)
    * [Visit](Visit.md)
 * [Identifier](Identifier.md)
 * [PatientOrBiologicallyDerivedMaterial](PatientOrBiologicallyDerivedMaterial.md)
    * [BiologicallyDerivedMaterial](BiologicallyDerivedMaterial.md)
    * [Patient](Patient.md)
 * [Quantity](Quantity.md)
 * [Relationship](Relationship.md)
 * [SpecimenContainer](SpecimenContainer.md)
 * [SpecimenCreationActivity](SpecimenCreationActivity.md)
 * [SpecimenProcessingActivity](SpecimenProcessingActivity.md)
 * [SpecimenStorageActivity](SpecimenStorageActivity.md)
 * [SpecimenTransportActvity](SpecimenTransportActvity.md)

### Mixins


### Slots

 * [analyte_concentration](analyte_concentration.md) - The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'aliquot' or 'analyte'). e.g. the concentration of DNA in a specimen representing a DNA extract from a blood sample.
    * [Specimen➞analyte_concentration](Specimen_analyte_concentration.md)
 * [analyte_concentration_method](analyte_concentration_method.md) - The method used to determine the concentration of purified analyte  within a solution.
    * [Specimen➞analyte_concentration_method](Specimen_analyte_concentration_method.md)
 * [analyte_type](analyte_type.md) - When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
    * [Specimen➞analyte_type](Specimen_analyte_type.md)
 * [associated_project](associated_project.md) - The Project associated with the specimen.
    * [Specimen➞associated_project](Specimen_associated_project.md)
 * [cellular_composition](cellular_composition.md) - The cellular composition of the sample
    * [Specimen➞cellular_composition](Specimen_cellular_composition.md)
 * [compositional_measure](compositional_measure.md) - A data container holding information about the area or relative proportion of a specific type of tissue in a specimen
    * [Specimen➞compositional_measure](Specimen_compositional_measure.md)
 * [contained_in](contained_in.md) - A physical container in which a specimen is held or attached -  to store for future use,  as a substrate for growth (e.g. a cell culture dish), or as a vessel to enable analysis (e.g. a microscope slide or 96-well plate) 
    * [Specimen➞contained_in](Specimen_contained_in.md)
 * [creation](creation.md) - The activity in which the specimen was created, through removing material from an biological source or natural setting, or through derivation from an existing specimen.
    * [Specimen➞creation](Specimen_creation.md)
 * [current_weight](current_weight.md) - The present weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
    * [Specimen➞current_weight](Specimen_current_weight.md)
 * [derived_from_specimen](derived_from_specimen.md) - The source specimen from which this one was directly derived.
    * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)
 * [derived_from_subject](derived_from_subject.md) - The Patient/ResearchSubject from which the specimen was directly or indirectly derived.
    * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)
 * [derived_product](derived_product.md) - A biologically derived product (e.g. a cell culture, tissue culture, or organoid) that was generated from the specimen
    * [Specimen➞derived_product](Specimen_derived_product.md)
 * [description](description.md) - A free text field to capture additional information or explanation about the specimen.
    * [Specimen➞description](Specimen_description.md)
 * [dimensional_measure](dimensional_measure.md) - A data container holding information about the one and two dimensional measurements of a specimen.
    * [Specimen➞dimensional_measure](Specimen_dimensional_measure.md)
 * [distance_from_paired_specimen](distance_from_paired_specimen.md) - The observed distance of the specimen from a 'paired specimen' in the body at the time of collection. (e.g. the distance between the in vivo location of a tumor tissue specimen and its paired normal specimen)
    * [Specimen➞distance_from_paired_specimen](Specimen_distance_from_paired_specimen.md)
 * [general_tissue_morphology](general_tissue_morphology.md) - A term describing at a high-level the kind of tissue collected in a specimen, with respect to disease status or proximity to tumor tissue (e.g. is it normal, abnormal, tumor, tumor-adjacent). 
    * [Specimen➞general_tissue_morphology](Specimen_general_tissue_morphology.md)
 * [id](id.md)
    * [Specimen➞id](Specimen_id.md) - The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
 * [identifier](identifier.md) - A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). 
    * [Specimen➞identifier](Specimen_identifier.md)
 * [matched_normal_flag](matched_normal_flag.md) - A flag indicating that there is no matched normal aliquot for this case that can be used for variant calling purposes.
    * [Specimen➞matched_normal_flag](Specimen_matched_normal_flag.md)
 * [morphology_pathologically_confirmed](morphology_pathologically_confirmed.md) - A flag indicating whether the histologic assessment of specific morphology was confirmed by a pathologist review??
    * [Specimen➞morphology_pathologically_confirmed](Specimen_morphology_pathologically_confirmed.md)
 * [paired_specimen_genotype_match_flag](paired_specimen_genotype_match_flag.md) - A flag to indicate whether the genotype of the paired normal or tumor specimen matches, or if the data is not available.
    * [Specimen➞paired_specimen_genotype_match_flag](Specimen_paired_specimen_genotype_match_flag.md)
 * [processing](processing.md) - An activity that modifies the physical structure, composition, or state of a specimen.
    * [Specimen➞processing](Specimen_processing.md)
 * [provided_by](provided_by.md) - The organization/center that provided the specimen.
    * [Specimen➞provided_by](Specimen_provided_by.md)
 * [qualification_status_flag](qualification_status_flag.md) - A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
    * [Specimen➞qualification_status_flag](Specimen_qualification_status_flag.md)
 * [reference_status_flag](reference_status_flag.md) - A flag indicating whether the specimen is used as a reference during analytical interrogation
    * [Specimen➞reference_status_flag](Specimen_reference_status_flag.md)
 * [related_document](related_document.md) - A reference to an external document that is about or related to the specimen (e.g. a publication related to the study it is a part of, pathology report containing additional details about it, protocol describing how it was collected, or a catalog entry describing  related research resource)
    * [Specimen➞related_document](Specimen_related_document.md)
 * [related_specimen](related_specimen.md) - Another specimen to which this one is related in some way (excluding parent-child specimen relationships, which are captured using the dedicated the source_specimen field)
    * [Specimen➞related_specimen](Specimen_related_specimen.md)
 * [selected_normal_flag](selected_normal_flag.md) - A flag to denote which 'normal' aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
    * [Specimen➞selected_normal_flag](Specimen_selected_normal_flag.md)
 * [source_body_structure](source_body_structure.md) - The source anatomical material from which the specimen was derived.
    * [Specimen➞source_body_structure](Specimen_source_body_structure.md)
 * [source_material_type](source_material_type.md) - The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
    * [Specimen➞source_material_type](Specimen_source_material_type.md)
 * [specific_tissue_morphology](specific_tissue_morphology.md) - A term describing the specific pathology exhibited by the tissue in a specimen.
    * [Specimen➞specific_tissue_morphology](Specimen_specific_tissue_morphology.md)
 * [specimen_quality_measure](specimen_quality_measure.md) - A data container holding measures of some specimen characteristic that is indicative of its quality or suitability for use.
    * [Specimen➞specimen_quality_measure](Specimen_specimen_quality_measure.md)
 * [specimen_type](specimen_type.md) - The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 
    * [Specimen➞specimen_type](Specimen_specimen_type.md)
 * [storage](storage.md) - An activity that results in the storing or maintaining of the specimen in a particular location, container, or state.
    * [Specimen➞storage](Specimen_storage.md)
 * [subject_diagnosis](subject_diagnosis.md) - A diagnosis of the condition in the patient from which the sample was derived - providing time-stamped information about the state of the condition when the specimen was collected (e.g. if it was primary, recurrent, metastatic, etc).
    * [Specimen➞subject_diagnosis](Specimen_subject_diagnosis.md)
 * [transport](transport.md) - An activity through which the specimen is transported between locations.
    * [Specimen➞transport](Specimen_transport.md)
 * [volume](volume.md) - The total volume of the specimen
    * [Specimen➞volume](Specimen_volume.md)

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
