
# Datatypes schema





### Classes

 * [Coding](Coding.md)
 * [Identifier](Identifier.md)
 * [Quantity](Quantity.md)

### Mixins


### Slots

 * [➞code](coding__code.md) - The value of the code itself.
 * [➞display](coding__display.md) - A human-readable name for the code.
 * [➞system](coding__system.md) - The code system where the code is defined.
 * [➞version](coding__version.md) - The version of the code system.
 * [➞system](identifier__system.md) - The system or namespace that defines the identifier.
 * [➞type](identifier__type.md) - A code that defines the type of the identifier.
 * [➞value](identifier__value.md) - The value of the identifier, as defined by the system.
 * [➞comparator](quantity__comparator.md) -  how to understand the value  . . .   < | <= | >= | >
 * [➞unit](quantity__unit.md) - Unit representation (e.g. mg, mL)
 * [➞value](quantity__value.md) - Numerical value (with implicit precision)

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
 * [Literal](types/Literal.md)  ([String](types/String.md)) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [Url](types/Url.md)  ([String](types/String.md)) 
