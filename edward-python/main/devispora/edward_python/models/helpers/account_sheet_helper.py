import re
from typing import List

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetExceptionMessage, \
    AccountSheetException
from devispora.edward_python.models.account_sheet import AccountSheetResult, AccountSheetStatus, AccountSheetType
from devispora.edward_python.models.helpers.date_helper import parse_google_string_to_date

allowed_delimiters = '[:;, ]'


def process_account_sheet(sheet_values: List, sheet_id: str) -> AccountSheetResult:
    emails = retrieve_emails(sheet_values)
    request_datetime = retrieve_date(sheet_values)
    shared_status = retrieve_shared_status(sheet_values)
    reservation_type = retrieve_reservation_type(sheet_values)
    return AccountSheetResult(sheet_id, emails, request_datetime, shared_status, reservation_type)


def retrieve_emails(sheet_values: List):
    try:
        emails = sheet_values[0][0]
        resulting_emails = re.split(allowed_delimiters, emails)
        return resulting_emails
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.EmailNotFound)


def retrieve_date(sheet_values: List):
    try:
        return parse_google_string_to_date(sheet_values[1][0], sheet_values[2][0])
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateNotFound)
    except ValueError:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateCouldNotBeParsed)


def retrieve_shared_status(sheet_values: List):
    try:
        shared_status = sheet_values[3][0]
        try:
            return AccountSheetStatus(shared_status)
        except ValueError:
            raise AccountSheetException(AccountSheetExceptionMessage.SharedStatusNotRecognised)
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.SharedStatusIssue)


def retrieve_reservation_type(sheet_values: List):
    try:
        res_type_input = sheet_values[4][0]
        if res_type_input == AccountSheetType.NormalAccountsType:
            return AccountSheetType.NormalAccountsType
        elif res_type_input == AccountSheetType.ObserverAccountsType:
            return AccountSheetType.ObserverAccountsType
        else:
            raise AccountSheetException(AccountSheetExceptionMessage.ReservationTypeNotRecognised)
    except IndexError:
        raise AccountSheetException(AccountSheetExceptionMessage.ReservationTypeIssue)
