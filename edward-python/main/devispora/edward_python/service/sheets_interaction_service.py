from googleapiclient.discovery import build

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException
from devispora.edward_python.google.credentials import get_credentials
from devispora.edward_python.models.account_sheet import desired_account_sheet_range
from devispora.edward_python.models.erred_sheet import ErredSheet
from devispora.edward_python.models.helpers.account_sheet_helper import process_account_sheet
from datetime import datetime
credentials = get_credentials()
sheets_service = build('sheets', 'v4', credentials=credentials)


def retrieve_sheet_information(drive_files: []) -> []:
    converted_sheets = []
    erred_sheets = []
    print(f'Sheet Step 1: {datetime.now()}')
    for item in drive_files:
        sheet_id = item['id']
        sheet_name = item['name']
        ranges = retrieve_sheet_values_by_range(spreadsheet_id=sheet_id, desired_ranges=desired_account_sheet_range)
        print(f'Sheet Step 2: {datetime.now()}')
        try:

            converted_sheet = process_account_sheet(ranges, sheet_id, sheet_name)
            converted_sheets.append(converted_sheet)
            print(f'Sheet Step 3: {datetime.now()}')
        except AccountSheetException as warning:
            erred_sheets.append(ErredSheet(sheet_id, sheet_name, warning))
    print(f'Sheet Step 4: {datetime.now()}')
    return converted_sheets, erred_sheets


def retrieve_sheet_values_by_range(spreadsheet_id: str, desired_ranges):
    """ Can be used to retrieve sheet values of an already retrieved Google Drive item """
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=desired_ranges).execute()
    return result['values']


def update_shared_status(spreadsheet_id: str, cell_range: [str], updated_status: str):
    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=cell_range,
        body={
            'values': [[updated_status]]
        },
        valueInputOption='RAW'
    ).execute()
