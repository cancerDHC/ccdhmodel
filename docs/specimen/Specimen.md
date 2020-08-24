
# Type: Specimen




URI: [specimen:Specimen](https://ccdh.org/specimen/Specimen)


![img](images/Specimen.svg)

## Parents

 *  is_a: [Entity](Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **[Specimen](Specimen.md)** *[Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)*  <sub>0..*</sub>  **[Specimen](Specimen.md)**
 *  **None** *[derived_from_specimen](derived_from_specimen.md)*  <sub>0..*</sub>  **[Specimen](Specimen.md)**

## Attributes


### Own

 * [Specimen➞analyte_concentration](Specimen_analyte_concentration.md)  <sub>OPT</sub>
    * Description: The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'aliquot' or 'analyte'). e.g. the concentration of DNA in a specimen representing a DNA extract from a blood sample.
    * range: [Quantity](Quantity.md)
 * [Specimen➞analyte_concentration_method](Specimen_analyte_concentration_method.md)  <sub>OPT</sub>
    * Description: The method used to determine the concentration of purified analyte  within a solution.
    * range: [Coding](Coding.md)
 * [Specimen➞analyte_type](Specimen_analyte_type.md)  <sub>OPT</sub>
    * Description: When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
    * range: [Coding](Coding.md)
 * [Specimen➞associated_project](Specimen_associated_project.md)  <sub>OPT</sub>
    * Description: The Project associated with the specimen.
    * range: [Project](Project.md)
 * [Specimen➞cellular_composition](Specimen_cellular_composition.md)  <sub>OPT</sub>
    * Description: The cellular composition of the sample
    * range: [Coding](Coding.md)
 * [Specimen➞compositional_measure](Specimen_compositional_measure.md)  <sub>OPT</sub>
    * Description: A data container holding information about the area or relative proportion of a specific type of tissue in a specimen
    * range: [DataContainer](DataContainer.md)
 * [Specimen➞contained_in](Specimen_contained_in.md)  <sub>OPT</sub>
    * Description: A physical container in which a specimen is held or attached -  to store for future use,  as a substrate for growth (e.g. a cell culture dish), or as a vessel to enable analysis (e.g. a microscope slide or 96-well plate) 
    * range: [SpecimenContainer](SpecimenContainer.md)
 * [Specimen➞creation](Specimen_creation.md)  <sub>OPT</sub>
    * Description: The activity in which the specimen was created, through removing material from an biological source or natural setting, or through derivation from an existing specimen.
    * range: [SpecimenCreationActivity](SpecimenCreationActivity.md)
 * [Specimen➞current_weight](Specimen_current_weight.md)  <sub>0..*</sub>
    * Description: The present weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
    * range: [Quantity](Quantity.md)
 * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)  <sub>0..*</sub>
    * Description: The source specimen from which this one was directly derived.
    * range: [Specimen](Specimen.md)
 * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)  <sub>OPT</sub>
    * Description: The Patient/ResearchSubject from which the specimen was directly or indirectly derived.
    * range: [PatientOrBiologicallyDerivedMaterial](PatientOrBiologicallyDerivedMaterial.md)
 * [Specimen➞derived_product](Specimen_derived_product.md)  <sub>0..*</sub>
    * Description: A biologically derived product (e.g. a cell culture, tissue culture, or organoid) that was generated from the specimen
    * range: [BiologicallyDerivedProduct](BiologicallyDerivedProduct.md)
 * [Specimen➞description](Specimen_description.md)  <sub>OPT</sub>
    * Description: A free text field to capture additional information or explanation about the specimen.
    * range: [Literal](types/Literal.md)
 * [Specimen➞dimensional_measure](Specimen_dimensional_measure.md)  <sub>OPT</sub>
    * Description: A data container holding information about the one and two dimensional measurements of a specimen.
    * range: [DataContainer](DataContainer.md)
 * [Specimen➞distance_from_paired_specimen](Specimen_distance_from_paired_specimen.md)  <sub>OPT</sub>
    * Description: The observed distance of the specimen from a 'paired specimen' in the body at the time of collection. (e.g. the distance between the in vivo location of a tumor tissue specimen and its paired normal specimen)
    * range: [Literal](types/Literal.md)
 * [Specimen➞general_tissue_morphology](Specimen_general_tissue_morphology.md)  <sub>OPT</sub>
    * Description: A term describing at a high-level the kind of tissue collected in a specimen, with respect to disease status or proximity to tumor tissue (e.g. is it normal, abnormal, tumor, tumor-adjacent). 

    * range: [Coding](Coding.md)
 * [Specimen➞id](Specimen_id.md)  <sub>REQ</sub>
    * Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
    * range: [Literal](types/Literal.md)
 * [Specimen➞identifier](Specimen_identifier.md)  <sub>0..*</sub>
    * Description: A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). 
    * range: [Identifier](Identifier.md)
 * [Specimen➞matched_normal_flag](Specimen_matched_normal_flag.md)  <sub>0..*</sub>
    * Description: A flag indicating that there is no matched normal aliquot for this case that can be used for variant calling purposes.
    * range: [Coding](Coding.md)
 * [Specimen➞morphology_pathologically_confirmed](Specimen_morphology_pathologically_confirmed.md)  <sub>OPT</sub>
    * Description: A flag indicating whether the histologic assessment of specific morphology was confirmed by a pathologist review??
    * range: [Boolean](types/Boolean.md)
 * [Specimen➞paired_specimen_genotype_match_flag](Specimen_paired_specimen_genotype_match_flag.md)  <sub>OPT</sub>
    * Description: A flag to indicate whether the genotype of the paired normal or tumor specimen matches, or if the data is not available.
    * range: [Coding](Coding.md)
 * [Specimen➞processing](Specimen_processing.md)  <sub>0..*</sub>
    * Description: An activity that modifies the physical structure, composition, or state of a specimen.
    * range: [SpecimenProcessingActivity](SpecimenProcessingActivity.md)
 * [Specimen➞provided_by](Specimen_provided_by.md)  <sub>OPT</sub>
    * Description: The organization/center that provided the specimen.
    * range: [Organization](Organization.md)
 * [Specimen➞qualification_status_flag](Specimen_qualification_status_flag.md)  <sub>OPT</sub>
    * Description: A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
    * range: [Coding](Coding.md)
 * [Specimen➞reference_status_flag](Specimen_reference_status_flag.md)  <sub>OPT</sub>
    * Description: A flag indicating whether the specimen is used as a reference during analytical interrogation
    * range: [Boolean](types/Boolean.md)
 * [Specimen➞related_document](Specimen_related_document.md)  <sub>0..*</sub>
    * Description: A reference to an external document that is about or related to the specimen (e.g. a publication related to the study it is a part of, pathology report containing additional details about it, protocol describing how it was collected, or a catalog entry describing  related research resource)
    * range: [DocumentReference](DocumentReference.md)
 * [Specimen➞related_specimen](Specimen_related_specimen.md)  <sub>0..*</sub>
    * Description: Another specimen to which this one is related in some way (excluding parent-child specimen relationships, which are captured using the dedicated the source_specimen field)
    * range: [Relationship](Relationship.md)
 * [Specimen➞selected_normal_flag](Specimen_selected_normal_flag.md)  <sub>OPT</sub>
    * Description: A flag to denote which 'normal' aliquot the submitter prefers to use for variant calling. Only one normal per experimental strategy per case can be selected.
    * range: [Coding](Coding.md)
 * [Specimen➞source_body_structure](Specimen_source_body_structure.md)  <sub>0..*</sub>
    * Description: The source anatomical material from which the specimen was derived.
    * range: [BodyStructure](BodyStructure.md)
 * [Specimen➞source_material_type](Specimen_source_material_type.md)  <sub>OPT</sub>
    * Description: The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
    * range: [Coding](Coding.md)
 * [Specimen➞specific_tissue_morphology](Specimen_specific_tissue_morphology.md)  <sub>OPT</sub>
    * Description: A term describing the specific pathology exhibited by the tissue in a specimen.
    * range: [Coding](Coding.md)
 * [Specimen➞specimen_quality_measure](Specimen_specimen_quality_measure.md)  <sub>0..*</sub>
    * Description: A data container holding measures of some specimen characteristic that is indicative of its quality or suitability for use.
    * range: [DataContainer](DataContainer.md)
 * [Specimen➞specimen_type](Specimen_specimen_type.md)  <sub>OPT</sub>
    * Description: The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 

    * range: [Coding](Coding.md)
 * [Specimen➞storage](Specimen_storage.md)  <sub>OPT</sub>
    * Description: An activity that results in the storing or maintaining of the specimen in a particular location, container, or state.
    * range: [SpecimenStorageActivity](SpecimenStorageActivity.md)
 * [Specimen➞subject_diagnosis](Specimen_subject_diagnosis.md)  <sub>0..*</sub>
    * Description: A diagnosis of the condition in the patient from which the sample was derived - providing time-stamped information about the state of the condition when the specimen was collected (e.g. if it was primary, recurrent, metastatic, etc).
    * range: [ConditionDiagnosis](ConditionDiagnosis.md)
 * [Specimen➞transport](Specimen_transport.md)  <sub>OPT</sub>
    * Description: An activity through which the specimen is transported between locations.
    * range: [SpecimenTransportActvity](SpecimenTransportActvity.md)
 * [Specimen➞volume](Specimen_volume.md)  <sub>0..*</sub>
    * Description: The total volume of the specimen
    * range: [Quantity](Quantity.md)
