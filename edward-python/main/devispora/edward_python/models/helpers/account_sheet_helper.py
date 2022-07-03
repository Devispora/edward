from typing import List

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetExceptionMessage, \
    AccountSheetException
from devispora.edward_python.models.account_sheet import AccountSheetResult
from devispora.edward_python.models.helpers.date_helper import parse_google_string_to_date


def process_account_sheet(sheet_values: List) -> AccountSheetResult:
    emails = retrieve_emails(sheet_values)
    request_datetime = retrieve_date(sheet_values)
    shared_status = sheet_values[3][0]
    reservation_type = sheet_values[4][0]
    return AccountSheetResult(emails, request_datetime, shared_status, reservation_type)


def retrieve_emails(sheet_values: List):
    try:
        return sheet_values[0][0]
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.EmailNotFound)


def retrieve_date(sheet_values: List):
    try:
        return parse_google_string_to_date(sheet_values[1][0], sheet_values[2][0])
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateNotFound)
    except ValueError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateCouldNotBeParsed)
