# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

* LinkML representation
  * Updated repo based on the [linkml model template](https://github.com/linkml/linkml-model-template).
    * Some LinkML model template files, like `MakeConfig` hav been moved into `from_template`. Note that `MakeConfig`
      makes extensive changes to numerous files including the model, tests, docs and PyPI metadata. These updates are
      based on `model/CONFIG.yaml`. Updating with `MakeConfig` could be very convenient but a strategy
      combining `MakeConfig` with manual updates to these files could lose important work. It's probably best to commit
      before running `MakeConfig`.
  * Necessary fixes to the `squeaky-clean` target in the Makefile.
  * We should have standardized to Python 3.7 as a minimum version (see `setup.py`, `setup.cfg` and `tox.ini`).

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
