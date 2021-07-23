SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = crdch
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema docs shex owl csv graphql python

#GEN_OPTS = --no-mergeimports
GEN_OPTS =

# We run all commands in the Pipenv.
RUN = pipenv run
all: gen stage
gen: $(patsubst %,gen-%,$(TGTS))
clean:
	rm -rf target/
	rm -rf docs/
	pipenv clean

t:
	echo $(SCHEMA_NAMES)

echo:
	echo $(patsubst %,gen-%,$(TGTS))

test: all

# We don't actually install anything if you run `make install` -- we just set up the Pipenv
# environment (if it isn't set up already).
install: pipenv-install

pipenv-install:
	pipenv install --dev

# Mark the targets above as phony.
.PHONY: all gen clean t echo test install pipenv-install

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
target/docs/%.md: $(SCHEMA_SRC) tdir-docs pipenv-install
	${RUN} gen-markdown $(GEN_OPTS) --img --dir target/docs $<
stage-docs: gen-docs
	cp -pr target/docs .

###  -- MARKDOWN DOCS --
# TODO: modularize imports
gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml tdir-python pipenv-install
	${RUN} gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@

###  -- MARKDOWN DOCS --
# TODO: modularize imports. For now imports are merged.
gen-graphql:target/graphql/$(SCHEMA_NAME).graphql
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql pipenv-install
	${RUN} gen-graphql $(GEN_OPTS) $< > $@

###  -- JSON schema --
# TODO: modularize imports. For now imports are merged.
gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema pipenv-install
	${RUN} gen-json-schema $(GEN_OPTS) -t transaction $< > $@

###  -- JSON-LD --
# TWO files per module
gen-jsonld: $(patsubst %, target/jsonld/%.jsonld, $(SCHEMA_NAMES)) $(patsubst %, target/jsonld/%.context.jsonld, $(SCHEMA_NAMES))
target/jsonld/%.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld pipenv-install
	${RUN} gen-jsonld $(GEN_OPTS) $< > $@
target/jsonld/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld pipenv-install
	${RUN} gen-jsonld-context $(GEN_OPTS) $< > $@

###  -- Shex --
# one file per module
gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex pipenv-install
	${RUN} gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

###  -- CSV --
# one file per module
gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv pipenv-install
	${RUN} gen-csv $(GEN_OPTS) $< > $@

###  -- OWL --
# TODO: modularize imports. For now imports are merged.
gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl pipenv-install
	${RUN} gen-owl $(GEN_OPTS) $< > $@

###  -- RDF (direct mapping) --
# TODO: modularize imports. For now imports are merged.
gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf pipenv-install
	${RUN} gen-rdf $(GEN_OPTS) $< > $@

###  -- LinkML --
# linkml (copy)
# one file per module
gen-linkml: target/linkml/$(SCHEMA_NAME).yaml
target/linkml/%.yaml: $(SCHEMA_DIR)/%.yaml tdir-limkml
	cp $< > $@

# test docs locally.
docserve: stage-docs pipenv-install
	${RUN} mkdocs serve

# Deploy changes to the `dev` version on the gh-pages branch.
# Note that this is not dependent on stage-docs, since you
# would generate the docs (usually as part of a `make all`)
# before you deploy it in a separate step.
gh-deploy: pipenv-install
	${RUN} mike deploy dev -p

# Regenerate from Google Sheets. Note that this uses a *separate* Pipenv in the
# generators/google-sheets directory, so we have to run pipenv install on it separately.
regen-google-sheets:
	cd generators/google-sheets && pipenv run python sheet2linkml.py && cp output/CDM_Dictionary_v1_Active.yaml ../../src/schema/crdch.yaml && cd -
