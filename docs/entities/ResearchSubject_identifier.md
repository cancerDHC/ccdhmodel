
# Type: ResearchSubject_identifier


A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier.

URI: [ccdh:ResearchSubject_identifier](https://ccdh.example.org/ccdh/ResearchSubject_identifier)


## Domain and Range

[ResearchSubject](ResearchSubject.md) ->  <sub>0..*</sub> [Identifier](Identifier.md)

## Parents

 *  is_a: [identifier](identifier.md)

## Children


## Used by

 * [ResearchSubject](ResearchSubject.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | ADM:Case.external_case_id |
|  | | ADM:Case.case_submitter_id |
|  | | GDC:Case.id |
|  | | GDC:Case.submitter_id |
|  | | PDC:Case.external_case_id |
|  | | PDC:Case.case_submitter_id |

