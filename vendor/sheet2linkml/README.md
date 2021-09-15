# Google Sheets to LinkML generator for the CRDC-H model

## Installation

See the main README file for installation instructions.

## Synopsis

Ideally, this program should be run from the root of this project by running:

    $ make generate-model

However, it can also be run directly via Pipenv:

     $ pipenv install --dev
     $ export CDM_GOOGLE_SHEET_ID=1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4
     $ pipenv run python vendor/sheet2linkml/sheet2linkml.py --output model/schema/crdch_model.yaml

