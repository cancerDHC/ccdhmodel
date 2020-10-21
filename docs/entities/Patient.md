
# Type: Patient




URI: [ccdh:Patient](https://example.org/ccdh/Patient)


![img](images/Patient.svg)

## Parents

 *  is_a: [Entity](Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **None** *[➞derived_from_subject](specimen__derived_from_subject.md)*  <sub>OPT</sub>  **[Patient](Patient.md)**

## Attributes


### Own

 * [➞associated_project](patient__associated_project.md)  <sub>0..*</sub>
    * Description: A reference to the Project(s) of which this ResearchSubject is a member
    * range: [Project](Project.md)
 * [➞taxon](patient__taxon.md)  <sub>OPT</sub>
    * Description: The taxonomic group (e.g. species) of the patient.
    * range: [Coding](Coding.md)

### Inherited from Entity:

 * [id](id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
