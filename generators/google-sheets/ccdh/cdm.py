from googleapiclient.discovery import build

import pygsheets

from dataclasses import dataclass

from ccdh.config import CDM_GOOGLE_SHEET_ID
from ccdh.gdrive.authorize import authorize
from typing import List
import pprint
import csv

pp = pprint.PrettyPrinter()

def class_definition(sheet_id: str, ranges: str) -> List[List]:
    """
    Extract CDM Enumerated biolinkml from Google Drive
    :param str sheet_id: The identifier of the google sheet
    :param str ranges: the ranges (sheet) name
    :return: A list of adm values
    """
    rows = []

    service = build('sheets', 'v4', credentials=authorize())

    # Call the Sheets API
    result = service.spreadsheets().values().batchGet(spreadsheetId=sheet_id, ranges=ranges).execute()
    value_ranges = result.get('valueRanges', [])

    return list(filter(lambda x: len(x) > 0, value_ranges[0]['values']))


def cdm_dictionary_sheet(sheet_id: str, ranges: str) -> List[List]:
    """
    Extract CDM Enumerated biolinkml from Google Drive
    :param str sheet_id: The identifier of the google sheet
    :return: A list of adm values
    """
    rows = []

    service = build('sheets', 'v4', credentials=authorize())

    # Call the Sheets API
    result = service.spreadsheets().values().batchGet(spreadsheetId=sheet_id, ranges=ranges).execute()
    value_ranges = result.get('valueRanges', [])
    for values in value_ranges[0]['values']:
        if len(values) < 9:
            continue
        elif values[7] != 'CodeableConcept':
            continue
        for prop in values[12].split('\n'):
            if len(prop.split('.')) != 3:
                continue
            row = [''] * 7
            row[0] = prop
            row[3] = f'{values[4]}.{values[5]}'
            rows.append(row)
    return rows

# Scopes used when accessing Google Drive.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/drive.metadata.readonly']


def get_google_sheet_with_headers_and_rows(sheet_id: str, sheet_name: str):
    """
    Get a Google Sheet as a list of rows using the header information from
    the first line of the file. The idea is for this method to be completely
    agnostic to the data being input: as long as the first row has header columns,
    it will return something sensible.

    :param sheet_id: The Google Sheet ID (see https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id)
    :param ranges: The ran
    :return:
    """

    client = pygsheets.authorize(client_secret='./google_api_credentials.json', scopes=SCOPES)

    sh = client.open_by_key(sheet_id)
    print(sh)

def main():
    # rows = cdm_dictionary_sheet(sheet_id=CDM_GOOGLE_SHEET_ID, ranges='MVPv0')
    # with open('output.tsv', 'w', newline='') as f_output:
    #    tsv_output = csv.writer(f_output, delimiter='\t')
    #    for row in rows:
    #        tsv_output.writerow(row)
    get_google_sheet_with_headers_and_rows(sheet_id=CDM_GOOGLE_SHEET_ID, sheet_name='Specimen')

if __name__ == '__main__':
    main()
