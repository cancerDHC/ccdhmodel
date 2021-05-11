
# Class: Quantity


A structured object to represent an amount of something (e.g., weight, mass, length, duration of time) - including a value and unit.

URI: [types:Quantity](https://example.org/ccdh/datatypes/Quantity)


![img](images/Quantity.svg)

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
