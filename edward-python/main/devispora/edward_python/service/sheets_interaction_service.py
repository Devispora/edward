from googleapiclient.discovery import build

from devispora.edward_python.google.credentials import get_credentials
from devispora.edward_python.models.account_sheet import desired_account_sheet_range
from devispora.edward_python.models.helpers.account_sheet_helper import process_account_sheet

credentials = get_credentials()
sheets_service = build('sheets', 'v4', credentials=credentials)


def retrieve_sheet_information(drive_files: []) -> []:
    converted_sheets = []
    for item in drive_files:
        result = sheets_service.spreadsheets().values().batchGet(
            spreadsheetId=item['id'], ranges=desired_account_sheet_range).execute()
        ranges = result['valueRanges'][0]['values']
        converted_sheet = process_account_sheet(ranges)
        converted_sheets.append(converted_sheet)
    return converted_sheets
