
# Type: Project




URI: [ccdh:Project](https://ccdh.example.org/ccdh/Project)


![img](images/Project.svg)

## Parents

 *  is_a: [Entity](Entity.md) - Any resource that has its own identifier

## Referenced by class

 *  **[Patient](Patient.md)** *[Patient➞associated_project](Patient_associated_project.md)*  <sub>0..*</sub>  **[Project](Project.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞associated_project](Specimen_associated_project.md)*  <sub>OPT</sub>  **[Project](Project.md)**
 *  **None** *[associated_project](associated_project.md)*  <sub>OPT</sub>  **[Project](Project.md)**

## Attributes


### Own

 * [Project➞id](Project_id.md)  <sub>REQ</sub>
    * range: [Literal](types/Literal.md)
