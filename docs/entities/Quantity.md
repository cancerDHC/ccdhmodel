
# Type: Quantity




URI: [ccdh:Quantity](https://example.org/ccdh/Quantity)


![img](images/Quantity.svg)

## Referenced by class

 *  **None** *[➞analyte_concentration](specimen__analyte_concentration.md)*  <sub>OPT</sub>  **[Quantity](Quantity.md)**
 *  **None** *[➞current_volume](specimen__current_volume.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**
 *  **None** *[➞current_weight](specimen__current_weight.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**

## Attributes


### Own

 * [➞comparator](quantity__comparator.md)  <sub>OPT</sub>
    * Description:  how to understand the value  . . .   < | <= | >= | >
    * range: [Coding](Coding.md)
 * [➞unit](quantity__unit.md)  <sub>OPT</sub>
    * Description: Unit representation (e.g. mg, mL)
    * range: [Coding](Coding.md)
 * [➞value](quantity__value.md)  <sub>OPT</sub>
    * Description: Numerical value (with implicit precision)
    * range: [Literal](types/Literal.md)
