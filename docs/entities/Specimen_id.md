
# Type: Specimen_id


The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.

URI: [ccdh:Specimen_id](https://ccdh.example.org/ccdh/Specimen_id)


## Domain and Range

[Specimen](Specimen.md) ->  <sub>REQ</sub> [Literal](types/Literal.md)

## Parents

 *  is_a: [id](id.md)

## Children


## Used by

 * [Specimen](Specimen.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | ADM:Sample.sample_id |
|  | | ADM:Portion.portion_id |
|  | | ADM:Aliquot.aliquot_id |
|  | | ADM:Analyte.analyte_id |
|  | | GDC:Aliquot.id |
|  | | GDC:Analyte.id |
|  | | GDC:Portion.id |
|  | | GDC:Sample.id |
|  | | PDC:Aliquot.aliquot_id |
|  | | PDC:Analyte.analyte_id |
|  | | PDC:Portion.portion_id |
|  | | PDC:Sample.sample_id |
|  | | ICDC:Sample.sample_id |
|  | | HTAN:Biospecimen.HTAN_BIOSPECIMEN_ID |
|  | | FHIR:Specimen.id |

