from googleapiclient.discovery import build

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException
from devispora.edward_python.google.credentials import get_credentials
from devispora.edward_python.models.account_sheet import desired_account_sheet_range
from devispora.edward_python.models.helpers.account_sheet_helper import process_account_sheet

credentials = get_credentials()
sheets_service = build('sheets', 'v4', credentials=credentials)


def retrieve_sheet_information(drive_files: []) -> []:
    converted_sheets = []
    erred_sheets = []
    for item in drive_files:
        sheet_id = item['id']
        ranges = retrieve_sheet_values_by_range(spreadsheet_id=sheet_id, desired_ranges=desired_account_sheet_range)
        try:
            converted_sheet = process_account_sheet(ranges, sheet_id)
            converted_sheets.append(converted_sheet)
        except AccountSheetException as warning:
            erred_sheets.append((item, warning))
    return converted_sheets, erred_sheets


def retrieve_sheet_values_by_range(spreadsheet_id: str, desired_ranges: []):
    """ Can be used to retrieve sheet values of an already retrieved Google Drive item """
    result = sheets_service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id, ranges=desired_ranges).execute()
    return result['valueRanges'][0]['values']

