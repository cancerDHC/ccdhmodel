
# Type: Patient




URI: [ccdh:Patient](https://ccdh.example.org/ccdh/Patient)


![img](images/Patient.svg)

## Parents

 *  is_a: [Entity](Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **[Specimen](Specimen.md)** *[Specimen➞derived_from_subject](Specimen_derived_from_subject.md)*  <sub>OPT</sub>  **[Patient](Patient.md)**
 *  **None** *[derived_from_subject](derived_from_subject.md)*  <sub>OPT</sub>  **[Patient](Patient.md)**

## Attributes


### Own

 * [Patient➞associated_project](Patient_associated_project.md)  <sub>0..*</sub>
    * Description: A reference to the Project(s) of which this ResearchSubject is a member
    * range: [Project](Project.md)
 * [Patient➞taxon](Patient_taxon.md)  <sub>OPT</sub>
    * Description: The taxonomic group (e.g. species) of the patient.
    * range: [Coding](Coding.md)

### Inherited from Entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
