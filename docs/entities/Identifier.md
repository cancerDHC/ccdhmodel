
# Class: Identifier




URI: [ccdh:Identifier](https://example.org/ccdh/Identifier)


![img](images/Identifier.svg)

## Referenced by class

 *  **None** *[➞identifier](patient__identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**
 *  **None** *[➞identifier](researchSubject__identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**
 *  **None** *[➞identifier](specimen__identifier.md)*  <sub>0..*</sub>  **[Identifier](Identifier.md)**

## Attributes


### Own

 * [➞system](identifier__system.md)  <sub>OPT</sub>
     * Description: The system or namespace that defines the identifier.
     * range: [String](types/String.md)
 * [➞type](identifier__type.md)  <sub>OPT</sub>
     * Description: A code that defines the type of the identifier.
     * range: [CodeableConcept](CodeableConcept.md)
 * [➞value](identifier__value.md)  <sub>OPT</sub>
     * Description: The value of the identifier, as defined by the system.
     * range: [String](types/String.md)
