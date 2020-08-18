
# Entities schema


This sheet holds descriptions of objects referenced as the Data Type of a field in the Biospecimen CDM, and likely to be represented as Entities/Classes/Resources in our final model, but which are out of scope to fully define in the current phase of work. We will record these candidate Entities/Classes/Resources here, and document their proposed use and requirements to support Biospecimen representation. Requiremetns accrued as we model additional subdomains will inform if and how these entties are represented in our model.


### Classes

 * [Entity](Entity.md) - Any resource that has its own identifier
    * [ConditionDiagnosis](ConditionDiagnosis.md)
    * [DocumentReference](DocumentReference.md)
    * [Organization](Organization.md)
    * [Project](Project.md)
    * [Visit](Visit.md)

### Mixins


### Slots

 * [id](id.md)
    * [Entity➞id](Entity_id.md)

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
