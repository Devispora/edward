from datetime import datetime, date, time, timedelta
from pytz import utc

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException, \
    AccountSheetExceptionMessage


def retrieve_current_date():
    return datetime.now(tz=utc)


def parse_google_string_to_date(google_date: str, google_time: str) -> datetime:
    try:
        request_date = date.fromisoformat(google_date)
        request_time = time.fromisoformat(google_time)
        request_date_time = datetime.combine(request_date, request_time)
        return request_date_time.astimezone(tz=utc)
    except ValueError as e:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateTimeNotISOFormat, e.args[0])


def sheet_is_from_this_year(sheet_name: str, current_date_utc):
    stripped_year = sheet_name[:4]
    try:
        return current_date_utc.year == int(stripped_year)
    except ValueError:
        # Expected when the sheet name has not been modified
        # We could modify this bit later if we feel we want to notify people forgetting after a period of time.
        return False


def five_minute_creation_cooldown(sheet_creation_date: str, current_date_utc):
    zulu_stripped = sheet_creation_date[:-1]
    try:
        creation_date = datetime.fromisoformat(zulu_stripped).astimezone(utc)
        creation_date_plus_5 = creation_date + timedelta(minutes=5)
        if current_date_utc > creation_date_plus_5:
            return True
        else:
            return False
    except ValueError:
        raise AccountSheetException(AccountSheetExceptionMessage.GoogleMightHaveChangedDateFormat, sheet_creation_date)


def has_been_two_days(request_time: datetime, current_date_utc) -> bool:
    request_time_plus_2d = request_time + timedelta(days=2)
    if current_date_utc > request_time_plus_2d:
        return True
    else:
        return False


def is_due_to_release(request_time: datetime, current_date_utc) -> bool:
    """"Currently releases from 4 hours before start"""
    request_time_plus_4h = request_time - timedelta(hours=4)
    if current_date_utc > request_time_plus_4h:
        return True
    else:
        return False
