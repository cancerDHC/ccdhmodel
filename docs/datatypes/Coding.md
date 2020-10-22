
# Type: Coding


A structured representation of a coded/enumerated data value, that includes additional metadata about the code and code system.

URI: [types:Coding](https://example.org/ccdh/datatypes/Coding)


![img](images/Coding.svg)

## Referenced by class

 *  **None** *[➞type](identifier__type.md)*  <sub>OPT</sub>  **[Coding](Coding.md)**
 *  **None** *[➞comparator](quantity__comparator.md)*  <sub>OPT</sub>  **[Coding](Coding.md)**
 *  **None** *[➞unit](quantity__unit.md)*  <sub>OPT</sub>  **[Coding](Coding.md)**

## Attributes


### Own

 * [➞code](coding__code.md)  <sub>OPT</sub>
    * Description: The value of the code itself.
    * range: [Literal](types/Literal.md)
 * [➞display](coding__display.md)  <sub>OPT</sub>
    * Description: A human-readable name for the code.
    * range: [Literal](types/Literal.md)
 * [➞system](coding__system.md)  <sub>OPT</sub>
    * Description: The code system where the code is defined.
    * range: [Url](types/Url.md)
 * [➞version](coding__version.md)  <sub>OPT</sub>
    * Description: The version of the code system.
    * range: [Literal](types/Literal.md)
