
# Type: Specimen




URI: [ccdh:Specimen](https://ccdh.example.org/ccdh/Specimen)


![img](images/Specimen.svg)

## Parents

 *  is_a: [Entity](Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **[Specimen](Specimen.md)** *[Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)*  <sub>0..*</sub>  **[Specimen](Specimen.md)**
 *  **None** *[derived_from_specimen](derived_from_specimen.md)*  <sub>0..*</sub>  **[Specimen](Specimen.md)**

## Attributes


### Own

 * [Specimen➞analyte_concentration](Specimen_analyte_concentration.md)  <sub>OPT</sub>
    * Description: The concentration of an extracted analyte that is present in a specimen (specifically, in a specimen of type 'analyte', or an 'aliquot' derived from an analyte). e.g. the concentration of DNA in a specimen created through extracting DNA from a blood sample.
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
 * [Specimen➞current_volume](Specimen_current_volume.md)  <sub>0..*</sub>
    * Description: The current total volume of the specimen, at the time of recording.
    * range: [Quantity](Quantity.md)
 * [Specimen➞current_weight](Specimen_current_weight.md)  <sub>0..*</sub>
    * Description: The current weight of the specimen, at the time of recording (as opposed to an initial weight before its processing or portioning).
    * range: [Quantity](Quantity.md)
 * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)  <sub>0..*</sub>
    * Description: A source/parent specimen from which this one was directly derived.
    * range: [Specimen](Specimen.md)
 * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)  <sub>OPT</sub>
    * Description: The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.
    * range: [Patient](Patient.md)
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
 * [Specimen➞qualification_status_flag](Specimen_qualification_status_flag.md)  <sub>OPT</sub>
    * Description: A flag indicating whether the specimen is qualified or disqualified for data analysis in a study.
    * range: [Coding](Coding.md)
 * [Specimen➞source_material_type](Specimen_source_material_type.md)  <sub>OPT</sub>
    * Description: The general kind of material from which the specimen was derived, indicating the physical nature of the source material. 
    * range: [Coding](Coding.md)
 * [Specimen➞specific_tissue_morphology](Specimen_specific_tissue_morphology.md)  <sub>OPT</sub>
    * Description: A term describing the specific pathology exhibited by the tissue in a specimen.
    * range: [Coding](Coding.md)
 * [Specimen➞specimen_type](Specimen_specimen_type.md)  <sub>OPT</sub>
    * Description: The high-level type of the specimen, based on its how it has been derived from the original extracted sample. 

    * range: [Coding](Coding.md)
