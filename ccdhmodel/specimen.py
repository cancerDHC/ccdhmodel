# Auto generated from specimen.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-18 11:33
# Schema: specimen
#
# id: https://ccdh.org/model/specimen
# description: Any material sample taken from a biological entity (living or dead), or taken from a physical
#              object or the environment. (Adapted from FHIR) Specimens are usually collected as an example of
#              their kind, often for use in some investigation.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace


metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
SPECIMEN = CurieNamespace('specimen', 'https://ccdh.org/specimen/')
DEFAULT_ = SPECIMEN


# Types

# Class references





# Slots
class slots:
    pass


