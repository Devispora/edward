from datetime import datetime, date, time
from pytz import utc

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException, \
    AccountSheetExceptionMessage

current_date_utc = datetime.now(tz=utc)


def parse_google_string_to_date(google_date: str, google_time: str) -> datetime:
    try:
        request_date = date.fromisoformat(google_date)
        request_time = time.fromisoformat(google_time)
        request_date_time = datetime.combine(request_date, request_time)
        return request_date_time
    except ValueError as e:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateTimeNotISOFormat, e.args[0])


def sheet_is_from_this_year(sheet_name: str):
    stripped_year = sheet_name[:4]
    try:
        return current_date_utc.year == int(stripped_year)
    except ValueError:
        # Expected when the sheet name has not been modified
        # We could modify this bit later if we feel we want to notify people forgetting after a period of time.
        return False
