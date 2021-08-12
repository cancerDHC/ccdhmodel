# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_In August 2021, This repo was updated based on the [linkml model template](https://github.com/linkml/linkml-model-template)_

Some linkml model template files, like `MakeConfig` hav been moved into `from_template`. Note that `MakeConfig` makes extensive changes to numerous files including the model, tests, docs and PyPI metadata. These updates are based on `model/CONFIG.yaml`. Updating with `MakeConfig` could be very convenient but a strategy combining `MakeConfig` with manual updates to these files could lose important work. It's probably best to commit before running `MakeConfig`.

Most recently, several steps were taken to keep the `squeaky-clean` Makefile recipe for erroring out. 
- `PKG_T_JSON_SCHEMA` was set to `json_schema` instead of `jsonschema`.
- `docs` is being cleaned with `rm -rf docs/*`. That will delete any `README.*` or `.keep` file placed in there.

There is some conflict in terms of the Python version require specifications.

- `setup.cfg` says `python_requires = >=3.7`
- `setup.py` says `if sys.version_info < (3, 7, 0):`
    - The reporting of warning string was modified due to a error when trying to run `setup.py` under 2.7
- `tox.ini` says `envlist = py37, py38, py39`
- `./Pipfile says` inherited `python_version = "3.8"` from pre-template code

TODO: 
- Aggregate Markdown/documentation files like `from_template/ABOUT.md` and `from_template/ABOUT.md` into `MAINTAINERS.md`
- A verbose `./ChangeLog` is being created in `make pypi`, Disable that or move the output somewhere less conspicuous.

## [v1.0.1] - 2021-06-08

* Model changes
  * Minor changes to the model descriptions and mappings.
  * Improved enumeration for CRDC-H.Treatment.treatment_effect.
* LinkML representation
  * Modified LinkML to improve documentation.
* Google Sheet Generator
  * Improved warning for duplicable permissible values in enumeration.

## [v1.0] - 2021-06-01

* Multiple changes to the model, repository organization and Makefile.

## [v0.2] - 2021-05-14

* Replaced CRDC-H model with newly generated model.
* Used [Mike](https://github.com/jimporter/mike) to publish multiple
  versions of the same repository to GitHub Pages via the `gh-pages` branch.

## [v0.1] - 2021-05-12

* Initial version of the CCDH model as built by @jiaola.
* Includes the new version of the Google Sheet to LinkML generator
  built by @gaurav.

[Unreleased]: https://github.com/cancerDHC/ccdhmodel/compare/v1.0.1...HEAD
[v1.0.1]: https://github.com/cancerDHC/ccdhmodel/compare/v1.0...v1.0.1
[v1.0]: https://github.com/cancerDHC/ccdhmodel/compare/v0.2...v1.0
[v0.2]: https://github.com/cancerDHC/ccdhmodel/compare/v0.1...v0.2
[v0.1]: https://github.com/cancerDHC/ccdhmodel/releases/v0.1
