# Migrating data between CRDC-H model versions

As the CRDC-H model evolves with each release, data conforming to one edition of the model will require migration in order to conform to newer editions of the model. As the model evolves, classes may be added or removed from the model, attributes may be added or removed from classes, and the allowed values for particular attributes may change, either relating to other classes in the model or to terminology-bound enumerations.

## Approach

The CRDC-H model is released as a [LinkML document](https://github.com/cancerDHC/ccdhmodel). Using LinkML provides us with a number of automatically generated computable artifacts which directly correspond to the model, allowing us to apply the model in a number of ways, including the following:

1. **JSON schema**: validate that a JSON document uses fields and values which are valid according to the model.
2. **ShEx schema**: validate that an RDF dataset uses predicates and values which are valid according to the model.
3. **GraphQL schema**: express a GraphQL application programming interface corresponding to the LinkML model.
4. **OWL ontology**: Description Logic representation of the model.
5. **RDF dataset**: RDF representation of the model which is easily integrated into a broader triplestore.
6. **Python API**: a representation of the model as Python classes and methods.

The last artifact, the Python API, is the currently preferred approach for creating transformations from other data formats and schemas into CRDC-H. Using the API directly to construct data objects helps to ensure that the resulting structure will be conformant with the model. We are implementing demonstration use cases in this repository: https://github.com/cancerDHC/example-data

## Migrating data

Because each version of the CRDC-H LinkML model will have a corresponding Python implementation, we envision data migration as consisting of instantiating the Python objects of the newer API from those in the previous API. Ideally, we will provide a Python migration script with each model release, which takes as input a model in the previous model version. Migrations from earlier model versions can be performed as a series of single-version migrations. Migration scripts will need to be aware of which changes are “safe”, vs. which involve possible data loss (e.g., a field has been removed from a class and there is no replacement). Any such operations should be clearly reported in a migration log, particularly when no satisfactory migration could be performed for a data element.

## Generalizing migration operations

Since the LinkML infrastructure already provides us with a framework for programmatically interacting with the CRDC-H model, any generalizable issues we need to address in development of migration scripts should be incorporated into LinkML as a framework feature. Any support for these operations that could be incorporated into LinkML itself would help to make the model-specific migration implementations more declarative and more maintainable. As an example, LinkML could provide a standardized means for mapping between successive editions of an enumeration (perhaps it has been decided to use label-based enum values rather than CURIEs), such that it is only required to provide the mapping rather than implement a custom transformation.