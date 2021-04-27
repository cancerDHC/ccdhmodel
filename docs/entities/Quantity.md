
# Class: Quantity


A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including a value and unit.

URI: [ccdh:Quantity](https://example.org/ccdh/Quantity)


![img](images/Quantity.svg)

## Referenced by class

 *  **None** *[➞analyte_concentration](specimen__analyte_concentration.md)*  <sub>OPT</sub>  **[Quantity](Quantity.md)**
 *  **None** *[➞current_volume](specimen__current_volume.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**
 *  **None** *[➞current_weight](specimen__current_weight.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**

## Attributes


### Own

 * [➞comparator](quantity__comparator.md)  <sub>OPT</sub>
     * Description: How to understand the value  . . .   < | <= | >= | >
     * range: [Coding](Coding.md)
 * [➞unit](quantity__unit.md)  <sub>OPT</sub>
     * Description: Unit representation (e.g. mg, mL)
     * range: [Coding](Coding.md)
 * [➞value](quantity__value.md)  <sub>OPT</sub>
     * Description: Numerical value (with implicit precision)
     * range: [Decimal](types/Decimal.md)
