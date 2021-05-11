
# Class: CodeableConcept




URI: [ccdh:CodeableConcept](https://example.org/ccdh/CodeableConcept)


![img](images/CodeableConcept.svg)

## Referenced by class

 *  **None** *[➞type](identifier__type.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞taxon](patient__taxon.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞primary_disease_site](researchSubject__primary_disease_site.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞primary_disease_type](researchSubject__primary_disease_type.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞analyte_concentration_method](specimen__analyte_concentration_method.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞analyte_type](specimen__analyte_type.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞cellular_composition](specimen__cellular_composition.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞general_tissue_morphology](specimen__general_tissue_morphology.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞matched_normal_flag](specimen__matched_normal_flag.md)*  <sub>0..*</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞qualification_status_flag](specimen__qualification_status_flag.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞source_material_type](specimen__source_material_type.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞specific_tissue_morphology](specimen__specific_tissue_morphology.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**
 *  **None** *[➞specimen_type](specimen__specimen_type.md)*  <sub>OPT</sub>  **[CodeableConcept](CodeableConcept.md)**

## Attributes


### Own

 * [➞coding](codeableConcept__coding.md)  <sub>0..*</sub>
     * Description: A reference to a code defined by a terminology system
     * range: [Coding](Coding.md)
 * [➞text](codeableConcept__text.md)  <sub>OPT</sub>
     * Description: A human language representation of the concept represented by the Coding
     * range: [String](types/String.md)
