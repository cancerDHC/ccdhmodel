from pathlib import Path

from linkml_model.meta import SchemaDefinition, SlotDefinition, ElementName, ClassDefinition, ClassDefinitionName, TypeDefinitionName, TypeDefinition
from typing import List, Tuple
from ccdh.cdm import class_definition
import re
from dotenv import load_dotenv

from linkml.utils.yamlutils import extended_str, as_yaml

from pathlib import Path
env_path = Path('.').parent.parent / '.env'

ccdh_root = 'https://example.org/ccdh'


class TabularSchemaDefinitionLoader(object):
    def __init__(self):
        ...

    @classmethod
    def load_specimen(cls, name, rows: List[List]) -> SchemaDefinition:
        schema: SchemaDefinition = SchemaDefinition(name=name, id='https://ccdh.org/model/specimen', title=name)
        klass: ClassDefinition = ClassDefinition(name=name, is_a=ClassDefinitionName('Entity'))
        schema.classes = {name: klass}
        schema.license = 'https://creativecommons.org/publicdomain/zero/1.0/'
        schema.prefixes = {
            'linkml': 'https://w3id.org/biolink/linkml/',
            'specimen': f'{ccdh_root}/specimen/'
        }
        schema.default_prefix = 'specimen'
        schema.imports = ['prefixes', 'entities', 'datatypes']
        schema.description = rows[1][5]
        schema.comments = rows[3][5].split('\n')
        schema.notes.append('derived from [CDM_Dictionary_v1](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/)')
        # schema.mappings.extend([i.strip() for i in rows[2][5].split('\n')])
        deprecated = False
        for row in rows[5:]:
            # todo: use the deprecated slot
            # for exploratory attrs use subset
            if row[0] == 'DEPRECATED/EXPLORATORY ATTRIBUTES':
                deprecated = True
                continue
            slot: SlotDefinition = TabularSchemaDefinitionLoader.load_model_slot(row)
            if deprecated:
                slot.deprecated = True
            if slot.name == 'id':
                klass.slot_usage[slot.name] = slot
            else:
                klass.attributes[slot.name] = slot
        return schema

    @classmethod
    def load_model(cls, name, rows: List[List]) -> SchemaDefinition:
        name = name.replace(' ', '')
        klass: ClassDefinition = ClassDefinition(name=name, is_a=ClassDefinitionName('Entity'))
        for row in rows:
            # todo: use the deprecated slot
            # for exploratory attrs use subset
            if row[0] == 'DEPRECATED/EXPLORATORY ATTRIBUTES':
                deprecated = True
                continue
            slot: SlotDefinition = TabularSchemaDefinitionLoader.load_model_slot(row, name)
            if slot.name == 'id':
                klass.slot_usage[slot.name] = slot
            else:
                klass.attributes[slot.name] = slot
        return klass

    @classmethod
    def load_data_type(cls, name: str, rows: List[List]) -> ClassDefinition:
        name = name.replace('(data type)', '').strip()
        klass: ClassDefinition = ClassDefinition(name=name)
        for row in rows:
            # todo: use the deprecated slot
            # for exploratory attrs use subset
            if row[0] == 'DEPRECATED/EXPLORATORY ATTRIBUTES':
                deprecated = True
                continue
            slot: SlotDefinition = cls.load_data_class_slot(row)
            if slot.name == 'id':  # TODO: check if slot.name is in schema slots
                klass.slot_usage[slot.name] = slot
            else:
                klass.attributes[slot.name] = slot
        return klass

    @classmethod
    def load_data_class_slot(cls, row: List) -> SlotDefinition:
        slot: SlotDefinition = SlotDefinition(name=row[5])
        slot.description = row[6]
        range_str = ElementName(row[7]).replace('*', '')
        range_str = re.sub(r'\([^)]*\)', '', range_str).strip()
        if '|' in range_str:
            range_str = 'Or'.join([i.strip() for i in range_str.split('|')])
        slot.range = range_str
        slot = TabularSchemaDefinitionLoader.cardinality_to_slot(slot, row[8])
        return slot

    @classmethod
    def load_model_slot(cls, row: List, entity: str) -> SlotDefinition:
        slot: SlotDefinition = cls.load_data_class_slot(row)
        # mappings = []
        # try:
        #     mappings.extend(['ADM:' + i.strip() for i in row[11].split('\n') if i.strip()])
        # except IndexError as err:
        #     print(row)
        # mappings.extend([i.strip().replace('.', ':', 1) for i in row[12].split('\n') if i.strip()])
        # mappings.extend(['FHIR:' + i.strip() for i in row[13].split('\n') if i.strip()])
        # slot.mappings = list(filter(lambda x: re.match(r'^\w+:[\w\-\_]+\.[\w\-\_]+$', x), mappings))
        if len(row) > 9:
            slot.comments.extend(filter(lambda a: len(a.strip()) > 0, row[9].split('\n')))
        if slot.range == 'CodableConcept' or slot.range == 'CodeableConcept':
            slot.range = 'CodeableConcept'
            slot.values_from = f'{ccdh_root}/valuesets/CDM/{entity}/{slot.name}'
        return slot

    @classmethod
    def cardinality_to_slot(cls, slot, card):
        if card == '0..1':
            slot.required = False
            slot.multivalued = False
        elif card == '0..m':
            slot.required = False
            slot.multivalued = True
        if slot.name == 'id':
            slot.required = True
        return slot

    @classmethod
    def create_schema(cls, name):
        schema: SchemaDefinition = SchemaDefinition(name='CCDH-MVP', id=f'{ccdh_root}/model/{name}', title=name)
        schema.version = 'v0'
        schema.license = 'https://creativecommons.org/publicdomain/zero/1.0/'
        schema.prefixes = {
            'linkml': 'https://w3id.org/biolink/linkml/',
            'ccdh': f'{ccdh_root}/'
        }
        schema.imports = ['datatypes', 'prefixes']
        schema.default_prefix = 'ccdh'
        schema.notes.append('derived from [CDM_Dictionary_v1](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/)')
        return schema


def load_ccdh_specimen() -> str:
    rows: List[List] = class_definition('1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4', 'specimen')
    schema: SchemaDefinition = TabularSchemaDefinitionLoader.load_specimen('specimen', rows)
    yaml = as_yaml(schema)
    return '\n'.join([i for i in yaml.split('\n') if not re.match(r'^\s+name:.*', i)])


def load_ccdh_sheet(ranges) -> Tuple[SchemaDefinition, SchemaDefinition]:
    rows: List[List] = class_definition('1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4', ranges)

    models = {}
    model = []
    name = None
    for row in rows:
        if not all(v == '' for v in row[0:4]) or all(v == '' for v in row[0:20]):
            continue
        if len(row) == 5:
            if model:
                models[name] = model
            name = row[4]
            model = []
        else:
            model.append(row)
    models[name] = model

    slots = {}
    id_slot = SlotDefinition('id', key=True, required=True, multivalued=False)
    slots['id'] = id_slot

    entities = {'Entity': ClassDefinition(name='Entity', description='Any resource that has its own identifier', abstract=True, slots=['id'])}
    data_types = {}
    for name in models:
        if '(data type)' in name:
            klass: ClassDefinition = TabularSchemaDefinitionLoader.load_data_type(name, models[name])
            data_types[klass.name] = klass
        else:
            klass: ClassDefinition = TabularSchemaDefinitionLoader.load_model(name, models[name])
            entities[klass.name] = klass
    entities_schema = TabularSchemaDefinitionLoader.create_schema(ranges)
    entities_schema.slots = slots
    entities_schema.classes = entities

    data_types_schema = SchemaDefinition(name='datatypes', id=f'{ccdh_root}/model/datatypes', title='Data Types used by the CCDH model')
    data_types_schema.license = 'https://creativecommons.org/publicdomain/zero/1.0/'
    data_types_schema.prefixes = {
        'linkml': 'https://w3id.org/biolink/linkml/',
        'types': f'{ccdh_root}/datatypes/'
    }
    data_types_schema.default_prefix = 'types'
    data_types_schema.imports = ['linkml:types']
    data_types_schema.types = {
        'url': TypeDefinition(name='url', typeof='string')
    }
    data_types_schema.classes = data_types

    return entities_schema, data_types_schema


if __name__ == '__main__':
    # print(load_ccdh_sheet(ranges='Specimen'))
    root = Path(__file__).parent.parent.parent
    entities_schema, data_types_schema = load_ccdh_sheet(ranges='MVPv0')
    with open(root / 'output/entities.yaml', 'w') as yaml_file:
        yaml_file.write(as_yaml(entities_schema))
    with open(root / 'output/datatypes.yaml', 'w') as yaml_file:
        yaml_file.write(as_yaml(data_types_schema))
