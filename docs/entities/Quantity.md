
# Type: Quantity




URI: [ccdh:Quantity](https://ccdh.example.org/ccdh/Quantity)


![img](images/Quantity.svg)

## Referenced by class

 *  **[Specimen](Specimen.md)** *[Specimen➞analyte_concentration](Specimen_analyte_concentration.md)*  <sub>OPT</sub>  **[Quantity](Quantity.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞current_volume](Specimen_current_volume.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**
 *  **[Specimen](Specimen.md)** *[Specimen➞current_weight](Specimen_current_weight.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**
 *  **None** *[analyte_concentration](analyte_concentration.md)*  <sub>OPT</sub>  **[Quantity](Quantity.md)**
 *  **None** *[current_volume](current_volume.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**
 *  **None** *[current_weight](current_weight.md)*  <sub>0..*</sub>  **[Quantity](Quantity.md)**

## Attributes


### Own

 * [Quantity➞comparator](Quantity_comparator.md)  <sub>OPT</sub>
    * Description:  how to understand the value  . . .   < | <= | >= | >
    * range: [Coding](Coding.md)
 * [Quantity➞unit](Quantity_unit.md)  <sub>OPT</sub>
    * Description: Unit representation (e.g. mg, mL)
    * range: [Coding](Coding.md)
 * [Quantity➞value](Quantity_value.md)  <sub>OPT</sub>
    * Description: Numerical value (with implicit precision)
    * range: [Literal](types/Literal.md)
