# CRDC-H Model in LinkML

This repository stores the [LinkML](https://linkml.github.io/) representation of the [CRDC Harmonized Data Model (CRDC-H)](https://cancerdhc.github.io/) produced by the [Center for Cancer Data Harmonization (CCDH)](https://harmonization.datacommons.cancer.gov/).

This repository includes [the LinkML model itself](./model/schema/crdch_model.yaml) (in [YAML](https://en.wikipedia.org/wiki/YAML) format) as well as a number of artifacts produced automatically by LinkML, including a JSON Schema, JSON-LD context, a GraphQL description, a CSV description and ShEx validation shapes.

Model documentation in Markdown can also be generated for this repository, and is currently hosted on GitHub Pages at https://cancerdhc.github.io/ccdhmodel/. A set of Python Data Classes can also be generated and are [available for use](./crdch_model/crdch_model.py). Examples of their use are available in the [Example Data](https://github.com/cancerDHC/example-data/) repository.

## Setup

### Automated generation of YAML

The CRDC-H model is currently in development on [a Google Sheet](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/).
This repository contains a program in the [`./vendor/sheet2linkml`](./vendor/sheet2linkml) directory
that can read the Google Sheet using the Google Drive API and generate a LinkML representation of the model.

In order to run this program, you will need to create and download Google Drive client credentials. First,
[enable the Google Drive API](https://developers.google.com/drive/api/v3/enable-drive-api). After the API is enabled, 
[create and download the client credentials](https://www.iperiusbackup.net/en/how-to-enable-google-drive-api-and-get-client-credentials/)
from the [Google API Console](https://console.developers.google.com/). Save the file as `google_api_credentials.json` in
the root directory of this project. [Detailed instructions and screenshots](https://pygsheets.readthedocs.io/en/stable/authorization.html)
are also available from the [`pygsheets` documentation](https://pygsheets.readthedocs.io/), which is the package we use to
access Google Sheets.

Once this is setup, run `make generate-model` to update the schema from Google Sheets. The first time you run this script,
you will see a browser page asking you to log in. Follow the instructions. The script will download a token and store it
locally. You won't need to log in in the future.

### Generation of LinkML artifacts

All artifacts can be generated by running `make` in this repository. `make clean` will delete generated existing artifacts, allowing them to be regenerated. This Makefile uses [Pipenv](https://pipenv.pypa.io/) to manage dependencies.

We use [mike](https://github.com/jimporter/mike) to publish documentation to GitHub Pages. Use `mike deploy [version] -p` to push a new version of the documentation to Google Pages (via the `gh-pages` branch). `mike deploy [version] latest -p -u` can be used to indicate that the uploaded version should be used as the `latest` version, which will be displayed by default.
