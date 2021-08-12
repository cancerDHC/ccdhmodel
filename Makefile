# All artifacts of the build should be preserved
.SECONDARY:

# ----------------------------------------
# Model documentation and schema directory
# ----------------------------------------
SRC_DIR = model
PKG_DIR = crdch_model
SCHEMA_DIR = $(SRC_DIR)/schema
MODEL_DOCS_DIR = $(SRC_DIR)/docs
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = crdch_model
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
PKG_TGTS = graphql json_schema shex owl csv
TGTS = docs python $(PKG_TGTS)
# add csv to match established ccdhmodel repo
# MAM 20210806 does docs and python by default
# note json_schema vs jsonschema

# Targets by PKG_TGT
PKG_T_GRAPHQL = $(PKG_DIR)/graphql
PKG_T_JSON = $(PKG_DIR)/json
PKG_T_JSONLD_CONTEXT = $(PKG_DIR)/jsonld
PKG_T_JSON_SCHEMA = $(PKG_DIR)/json_schema
PKG_T_OWL = $(PKG_DIR)/owl
PKG_T_RDF = $(PKG_DIR)/rdf
PKG_T_SHEX = $(PKG_DIR)/shex
PKG_T_SQLDDL = $(PKG_DIR)/sqlddl
PKG_T_DOCS = $(MODEL_DOCS_DIR)
PKG_T_PYTHON = $(PKG_DIR)
PKG_T_MODEL = $(PKG_DIR)/model
PKG_T_SCHEMA = $(PKG_T_MODEL)/schema
# MAM 20210806
PKG_T_CSV = $(PKG_DIR)/csv

# Global generation options
GEN_OPTS = --log_level WARNING
ENV = export PIPENV_VENV_IN_PROJECT=true && export PIPENV_PIPFILE=make-venv/Pipfile && export PIPENV_IGNORE_VIRTUALENVS=1
RUN = $(ENV) && pipenv run

# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: install gen

# ---------------------------------------
# We don't want to pollute the python environment with linkml tool specific packages.  For this reason,
# we install an isolated instance of linkml in the pipenv-linkml directory
# ---------------------------------------
install: make-venv/env.lock

make-venv/env.lock:
	$(ENV) && pipenv install
	touch make-venv/env.lock

# check for .venv or env.lock in make-venv?
uninstall:
	if [ -d 'make-venv/.venv' ] ;\
		then echo 'virtual env installed' ;\
		rm -f make-venv/env.lock ;\
		$(ENV) && pipenv --rm ;\
		else echo 'no virtual env to uninstall' ;\
	fi

# ---------------------------------------
# Test runner
# ----------------------------------------
test:
	pipenv install --dev
	pipenv run python -m unittest

# ---------------------------------------
# GEN: run generator for each target
# ---------------------------------------
gen: $(patsubst %,gen-%,$(TGTS))

# ---------------------------------------
# CLEAN: clear out all of the targets
# ---------------------------------------
clean:
	rm -rf target/*
.PHONY: clean


# ---------------------------------------
# SQUEAKY_CLEAN: remove all of the final targets to make sure we don't leave old artifacts around
# ---------------------------------------
squeaky-clean: uninstall clean $(patsubst %,squeaky-clean-%,$(PKG_TGTS))
# only depends on the existence of the $(PKG_DIR) directory
	if [ -d $(PKG_DIR)/model/schema ] ;\
		then echo '$(PKG_DIR)/model/schema present' ;\
		find $(PKG_DIR)/model/schema  ! -name 'README.*' -type f -exec rm -f {} + ;\
		else echo 'no $(PKG_DIR)/model/schema to clean up' ;\
	fi
#	# this will fail if docs is totally empty including no README.*
#	# oops it gets totally cleaned somewhere in make all
#	find docs/*  ! -name 'README.*' -exec rm -rf {} +
# just give up on a README or any placeholder in docs?
	rm -rf docs/*
	find $(PKG_DIR) -name "*.py" ! -name "__init__.py" ! -name "linkml_files.py" -exec rm -f {} +
# also uninstall the root virtual environment? how to check if one is present?
# have never seen .env, .venv or env.lock in the project root folder
	@echo 'squeaky cleaning complete'

squeaky-clean-%: clean
	echo $*
	find $(PKG_DIR)/$* ! -name 'README.*' ! -name $*  -type f -exec rm -f {} +

# ---------------------------------------
# T: List files to generate
# ---------------------------------------
t:
	echo $(SCHEMA_NAMES)

# ---------------------------------------
# ECHO: List all targets
# ---------------------------------------
echo:
	echo $(patsubst %,gen-%,$(TGTS))

tdir-%:
	rm -rf target/$*
	mkdir -p target/$*


# MAM 20210806 based on ccdhmodel main branch
###  -- CSV --
# one file per module
gen-csv: $(patsubst %, $(PKG_T_CSV)/%.csv, $(SCHEMA_NAMES))
.PHONY: gen-csv

$(PKG_T_CSV)/%.csv: target/csv/%.csv
	mkdir -p $(PKG_T_CSV)
	cp $< $@

target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv install
	${RUN} gen-csv $(GEN_OPTS) $< > $@
	# --no-mergeimports?
	# --mergeimports?

# ---------------------------------------
# MARKDOWN DOCS
#      Generate documentation ready for mkdocs
# ---------------------------------------
gen-docs: docs/index.md
.PHONY: gen-docs

docs/index.md: target/docs/index.md install
	mkdir -p $(PKG_T_DOCS)
	cp -R $(MODEL_DOCS_DIR)/*.md target/docs
	# mkdocs.yml moves from the target/docs to the docs directory
	$(RUN) mkdocs build

target/docs/index.md: $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml tdir-docs install
	$(RUN) gen-markdown $(GEN_OPTS) --mergeimports --notypesdir --warnonexist --dir target/docs $<

# ---------------------------------------
# YAML source
# ---------------------------------------
gen-model: $(patsubst %, $(PKG_T_SCHEMA)/%.yaml, $(SCHEMA_NAMES))

$(PKG_T_SCHEMA)/%.yaml: model/schema/%.yaml
	mkdir -p $(PKG_T_SCHEMA)
	cp $< $@

# ---------------------------------------
# PYTHON Source
# ---------------------------------------
gen-python: $(patsubst %, $(PKG_T_PYTHON)/%.py, $(SCHEMA_NAMES))
$(PKG_T_PYTHON)/%.py: target/python/%.py
	mkdir -p $(PKG_T_PYTHON)
	cp $< $@
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python install
	$(RUN) gen-python $(GEN_OPTS)  --no-slots --no-mergeimports $< > $@

# ---------------------------------------
# GRAPHQL Source
# ---------------------------------------
gen-graphql: $(PKG_T_GRAPHQL)/$(SCHEMA_NAME).graphql
.PHONY: gen-graphql

$(PKG_T_GRAPHQL)/%.graphql: target/graphql/%.graphql
	mkdir -p $(PKG_T_GRAPHQL)
	cp $< $@

target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql install
	$(RUN) gen-graphql $(GEN_OPTS) $< > $@

# ---------------------------------------
# JSON Schema
# ---------------------------------------
gen-json_schema: $(patsubst %, $(PKG_T_JSON_SCHEMA)/%.schema.json, $(SCHEMA_NAMES))
.PHONY: gen-json_schema

$(PKG_T_JSON_SCHEMA)/%.schema.json: target/json_schema/%.schema.json
	mkdir -p $(PKG_T_JSON_SCHEMA)
	cp $< $@

target/json_schema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-json_schema install
	$(RUN) gen-json-schema $(GEN_OPTS) -t transaction $< > $@

# ---------------------------------------
# ShEx
# ---------------------------------------
gen-shex: $(patsubst %, $(PKG_T_SHEX)/%.shex, $(SCHEMA_NAMES)) $(patsubst %, $(PKG_T_SHEX)/%.shexj, $(SCHEMA_NAMES))
.PHONY: gen-shex

$(PKG_T_SHEX)/%.shex: target/shex/%.shex
	mkdir -p $(PKG_T_SHEX)
	cp $< $@
$(PKG_T_SHEX)/%.shexj: target/shex/%.shexj
	mkdir -p $(PKG_T_SHEX)
	cp $< $@

target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex install
	$(RUN) gen-shex --no-mergeimports $(GEN_OPTS) $< > $@
target/shex/%.shexj: $(SCHEMA_DIR)/%.yaml tdir-shex install
	$(RUN) gen-shex --no-mergeimports $(GEN_OPTS) -f json $< > $@

# ---------------------------------------
# OWL
# ---------------------------------------
gen-owl: $(PKG_T_OWL)/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl

$(PKG_T_OWL)/%.owl.ttl: target/owl/%.owl.ttl
	mkdir -p $(PKG_T_OWL)
	cp $< $@
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl install
	$(RUN) gen-owl $(GEN_OPTS) $< > $@

# ---------------------------------------
# JSON-LD Context
# ---------------------------------------
gen-jsonld_context: $(patsubst %, $(PKG_T_JSONLD_CONTEXT)/%.context.jsonld, $(SCHEMA_NAMES)) $(patsubst %, $(PKG_T_JSONLD_CONTEXT)/%.model.context.jsonld, $(SCHEMA_NAMES))
.PHONY: gen-jsonld_context

$(PKG_T_JSONLD_CONTEXT)/%.context.jsonld: target/jsonld_context/%.context.jsonld
	mkdir -p $(PKG_T_JSONLD_CONTEXT)
	cp $< $@

$(PKG_T_JSONLD_CONTEXT)/%.model.context.jsonld: target/jsonld_context/%.model.context.jsonld
	mkdir -p $(PKG_T_JSONLD_CONTEXT)
	cp $< $@

target/jsonld_context/%.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld_context install
	$(RUN) gen-jsonld-context $(GEN_OPTS) --no-mergeimports $< > $@

target/jsonld_context/%.model.context.jsonld: $(SCHEMA_DIR)/%.yaml tdir-jsonld_context install
	$(RUN) gen-jsonld-context $(GEN_OPTS) --no-mergeimports $< > $@

# ---------------------------------------
# Plain Old (PO) JSON
# ---------------------------------------
gen-json: $(patsubst %, $(PKG_T_JSON)/%.json, $(SCHEMA_NAMES))
.PHONY: gen-json

$(PKG_T_JSON)/%.json: target/json/%.json
	mkdir -p $(PKG_T_JSON)
	cp $< $@
target/json/%.json: $(SCHEMA_DIR)/%.yaml tdir-json install
	$(RUN) gen-jsonld $(GEN_OPTS) --no-mergeimports $< > $@

# ---------------------------------------
# RDF
# ---------------------------------------
gen-rdf: gen-jsonld $(patsubst %, $(PKG_T_RDF)/%.ttl, $(SCHEMA_NAMES)) $(patsubst %, $(PKG_T_RDF)/%.model.ttl, $(SCHEMA_NAMES))
.PHONY: gen-rdf

$(PKG_T_RDF)/%.ttl: target/rdf/%.ttl
	mkdir -p $(PKG_T_RDF)
	cp $< $@
$(PKG_T_RDF)/%.model.ttl: target/rdf/%.model.ttl
	mkdir -p $(PKG_T_RDF)
	cp $< $@

target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml $(PKG_DIR)/jsonld/%.context.jsonld tdir-rdf install
	$(RUN) gen-rdf $(GEN_OPTS) --context $(realpath $(word 2,$^)) $< > $@
target/rdf/%.model.ttl: $(SCHEMA_DIR)/%.yaml $(PKG_DIR)/jsonld/%.model.context.jsonld tdir-rdf install
	$(RUN) gen-rdf $(GEN_OPTS) --context $(realpath $(word 2,$^)) $< > $@

# ---------------------------------------
# SQLDDL
# ---------------------------------------
gen-sqlddl: $(PKG_T_SQLDDL)/$(SCHEMA_NAME).sql
.PHONY: gen-sqlddl

$(PKG_T_SQLDDL)/%.sql: target/sqlddl/%.sql
	mkdir -p $(PKG_T_SQLDDL)
	cp $< $@
target/sqlddl/%.sql: $(SCHEMA_DIR)/%.yaml tdir-sqlddl install
	$(RUN) gen-sqlddl $(GEN_OPTS) $< > $@

# test docs locally.
docserve: gen-docs
	$(RUN) mkdocs serve


# Regenerate from Google Sheets. Note that this uses a *separate* Pipenv in the
# generators/google-sheets directory, so we have to run pipenv install on it separately.
regen-google-sheets:
	cd generators/google-sheets && $(RUN) python sheet2linkml.py && cp output/CDM_Dictionary_v1_Active.yaml ../../model/schema/crdch_model.yaml && cd -

# MAM 20210806 not sure how this fits into the linkml model template's doc building/publsihing approach
# shoudn't it be using $(RUN) not ${RUN} ?
# Deploy changes to the `dev` version on the gh-pages branch.
# Note that this is not dependent on stage-docs, since you
# would generate the docs (usually as part of a `make all`)
# before you deploy it in a separate step.
#gh-deploy: pipenv-install
#	${RUN} mike deploy dev -p

#### MAM 20210729
pypi:
	rm -f dist/*
	$(RUN) python setup.py sdist bdist_wheel
	$(RUN) twine upload dist/*
	git commit -am 'post twine push'
	git push --tags
