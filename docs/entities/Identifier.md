
# Type: Identifier




URI: [ccdh:Identifier](https://ccdh.example.org/ccdh/Identifier)


![img](images/Identifier.svg)

## Referenced by class

 *  **[ResearchSubject](ResearchSubject.md)** *[ResearchSubject➞identifier](ResearchSubject_identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞identifier](Specimen_identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**
 *  **None** *[identifier](identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**

## Attributes


### Own

 * [Identifier➞system](Identifier_system.md)  <sub>OPT</sub>
    * Description: The system or namespace that defines the identifier.
    * range: [Literal](types/Literal.md)
 * [Identifier➞type](Identifier_type.md)  <sub>OPT</sub>
    * Description: A code that defines the type of the identifier.
    * range: [Coding](Coding.md)
 * [Identifier➞value](Identifier_value.md)  <sub>OPT</sub>
    * Description: The value of the identifier, as defined by the system.
    * range: [Literal](types/Literal.md)
