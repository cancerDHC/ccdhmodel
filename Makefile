SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = ccdhmodel
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema docs shex owl csv graphql python

#GEN_OPTS = --no-mergeimports
GEN_OPTS =

all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
clean:
	rm -rf target/
	rm -rf docs/

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all

install:
	pipenv install	

tdir-%:
	mkdir -p target/$*
docs:
	mkdir $@

stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* .


###  -- MARKDOWN DOCS --
# Generate documentation ready for mkdocs
# TODO: modularize imports
gen-docs: target/docs/index.md copy-src-docs
.PHONY: gen-docs
copy-src-docs:
	cp $(SRC_DIR)/docs/*md target/docs/
target/docs/%.md: $(SCHEMA_SRC) tdir-docs
	pipenv run gen-markdown $(GEN_OPTS) --img --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

###  -- MARKDOWN DOCS --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
	pipenv run gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@

###  -- MARKDOWN DOCS --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	pipenv run gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON schema --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	pipenv run gen-json-schema $(GEN_OPTS) -t transaction $< > $@

###  -- JSON-LD --
# TWO files per module
gen-jsonld: $(patsubst %, target/jsonld/%.jsonld, $(SCHEMA_NAMES)) $(patsubst %, target/jsonld/%.context.jsonld, $(SCHEMA_NAMES))
target/jsonld/%.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld
	pipenv run gen-jsonld $(GEN_OPTS) $< > $@
target/jsonld/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld
	pipenv run gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- Shex --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	pipenv run gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	pipenv run gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	pipenv run gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	pipenv run gen-rdf $(GEN_OPTS) $< > $@

###  -- LinkML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

# test docs locally.
docserve:
	mkdocs serve

gh-deploy:
	mike deploy dev -p

# Regenerate from Google Sheets
regen-google-sheets:
	cd generators/google-sheets && pipenv run python sheet2linkml.py && cp output/CDM_Dictionary_v1_Active.yaml ../../src/schema/ccdhmodel.yaml && cd -
