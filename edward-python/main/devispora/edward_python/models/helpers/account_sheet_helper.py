from typing import List

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetExceptionMessage, \
    AccountSheetException
from devispora.edward_python.models.account_sheet import AccountSheetResult


def process_account_sheet(sheet_values: List) -> AccountSheetResult:
    emails = retrieve_emails(sheet_values)
    request_date = sheet_values[1][0]
    requested_time = sheet_values[2][0]
    shared_status = sheet_values[3][0]
    reservation_type = sheet_values[4][0]
    return AccountSheetResult(emails, request_date, requested_time, shared_status, reservation_type)


def retrieve_emails(sheet_values: List):
    try:
        return sheet_values[0][0]
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.EmailNotFound)


# todo parse to proper date style using date_helper
def retrieve_date(sheet_values: List):
    try:
        return sheet_values[1][0]
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateNotFound)
    except ValueError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateCouldNotBeParsed)
