# BiolinkML generator for CCDH

Create a `.env` file in the current directory. Put the following in the file:

```
CDM_GOOGLE_SHEET_ID=1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4
```

Then run

```
pipenv run python -m ccdh.biolinkml.cdm_biolinkml_loader
```

or run `pipenv shell` first and then the python command.
