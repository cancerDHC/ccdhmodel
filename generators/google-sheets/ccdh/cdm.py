from googleapiclient.discovery import build

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
    result = service.spreadsheets().values().batchGet(spreadsheetId=sheet_id, ranges=range).execute()
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


def main():
    rows = cdm_dictionary_sheet(sheet_id=CDM_GOOGLE_SHEET_ID, ranges='MVPv0')
    with open('output.tsv', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in rows:
            tsv_output.writerow(row)


if __name__ == '__main__':
    main()
