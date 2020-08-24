
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

 * [Specimen➞analyte_type](Specimen_analyte_type.md)  <sub>OPT</sub>
    * Description: When the specimen is of type 'analyte' or 'aliquot', this is the type of substance the analyte represents (e.g. DNA, RNA)
    * range: [Coding](Coding.md)
 * [Specimen➞associated_project](Specimen_associated_project.md)  <sub>OPT</sub>
    * Description: The Project associated with the specimen.
    * range: [Project](Project.md)
 * [Specimen➞derived_from_specimen](Specimen_derived_from_specimen.md)  <sub>0..*</sub>
    * range: [Specimen](Specimen.md)
 * [Specimen➞derived_from_subject](Specimen_derived_from_subject.md)  <sub>OPT</sub>
    * range: [PatientOrBiologicalyDerivedMaterial](PatientOrBiologicalyDerivedMaterial.md)
 * [Specimen➞description](Specimen_description.md)  <sub>OPT</sub>
    * Description: A free text field to capture additional information or explanation about the specimen.
    * range: [Literal](types/Literal.md)
 * [Specimen➞id](Specimen_id.md)  <sub>REQ</sub>
    * Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.
    * range: [Literal](types/Literal.md)
 * [Specimen➞identifier](Specimen_identifier.md)  <sub>0..*</sub>
    * Description: A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier).
    * range: [Identifier](Identifier.md)
 * [Specimen➞provided_by](Specimen_provided_by.md)  <sub>OPT</sub>
    * Description: The organization/center that provided the specimen.
    * range: [Organization](Organization.md)
 * [Specimen➞source_material_type](Specimen_source_material_type.md)  <sub>OPT</sub>
    * Description: The general kind of material from which the specimen was derived, indicating the physical nature of the source material.
    * range: [Coding](Coding.md)
 * [Specimen➞specimen_type](Specimen_specimen_type.md)  <sub>0..*</sub>
    * Description: The high-level type of the specimen, based on its how it has been derived from the original extracted sample.
    * range: [Coding](Coding.md)
