# Google Sheets to LinkML generator for the CRDC-H model

## Setup

### Google Drive API

In order to extract the data from Google Sheets, [enable the Google Drive API](https://developers.google.com/drive/api/v3/enable-drive-api). After the API is enabled, stay in the [Google API Console](https://console.developers.google.com/) and [create and download the client credentials](https://www.iperiusbackup.net/en/how-to-enable-google-drive-api-and-get-client-credentials/). Save the file as `google_api_credentials.json` in the root directory of this project.

The first time running the scripts, you will see a browser page asking you to log in. Follow the instructions. The script will download a token and store it locally. You won't need to log in in the future.

### Python packages

Use [pipenv](https://github.com/pypa/pipenv#readme) to install python packages.

```
pipenv install
```

If you run into any problems installing dependencies, it might be worthwhile
to enter the virtual environment so that you can debug the problem individually.

```
pipenv shell
```

### Configuration

Create a `.env` file in the current directory. Put the following in the file:

```
CDM_GOOGLE_SHEET_ID=1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4
```

## Running this script

You can run this script in a pipenv by running:

```
pipenv run python -m ccdh.linkml.cdm_linkml_loader
```

or run `pipenv shell` first and then the python command.
