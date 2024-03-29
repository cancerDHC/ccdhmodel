# CRDC-H Model in LinkML

This repository stores the [LinkML](https://linkml.github.io/) representation of the [CRDC Harmonized Data Model (CRDC-H)](https://cancerdhc.github.io/) produced by the [Center for Cancer Data Harmonization (CCDH)](https://harmonization.datacommons.cancer.gov/).

This repository includes [the LinkML model itself](./model/schema/crdch_model.yaml) (in [YAML](https://en.wikipedia.org/wiki/YAML) format) as well as a number of artifacts produced automatically by LinkML, including a JSON Schema, JSON-LD context, a GraphQL description, a CSV description and ShEx validation shapes.

Model documentation in Markdown can also be generated for this repository, and is currently hosted on GitHub Pages at https://cancerdhc.github.io/ccdhmodel/. A set of Python Data Classes can also be generated and are [available for use](./crdch_model/crdch_model.py). Examples of their use are available in the [Example Data](https://github.com/cancerDHC/example-data/) repository.

## Setup

### Generation of LinkML artifacts

All artifacts can be generated by running `make` in this repository. `make clean` will delete generated existing artifacts, allowing them to be regenerated. This Makefile uses [Poetry](https://python-poetry.org/) to manage dependencies.

We use [mike](https://github.com/jimporter/mike) to publish documentation to GitHub Pages. Use `mike deploy [version] -p` to push a new version of the documentation to Google Pages (via the `gh-pages` branch). `mike deploy [version] latest -p -u` can be used to indicate that the uploaded version should be used as the `latest` version, which will be displayed by default.

### Automated generation of YAML

The CRDC-H model is currently in development on [a Google Sheet](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/),
which is converted into a LinkML schema in [./model/schema/crdch_model.yaml](./model/schema/crdch_model.yaml). If you
would like to use the latest, in-development version of the schema as described in Google Sheets, you will need to
use the [sheet2linkml](https://github.com/cancerDHC/sheet2linkml) package to regenerate this schema to regenerate this
file by running `make generate-model`.

In order to read a Google Sheet, sheet2linkml will need access to the [Google Sheets API](https://developers.google.com/sheets/api)
in the [Google Developers Console](https://console.developers.google.com/).
[Detailed instructions and screenshots](https://pygsheets.readthedocs.io/en/stable/authorization.html) are available from
the [`pygsheets` documentation](https://pygsheets.readthedocs.io/), which is the package sheet2linkml uses to access
Google Sheets. Save the file as `google_api_credentials.json` in the root directory of this project. The first time you
run `make generate-model`, you will see a browser page asking you to log in. Follow the instructions. The script will
download a token and store it locally. You will not need to log in when rerunning this command.
