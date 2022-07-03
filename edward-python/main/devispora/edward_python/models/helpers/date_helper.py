from datetime import datetime, date, time

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException, \
    AccountSheetExceptionMessage


def parse_google_string_to_date(google_date: str, google_time: str) -> datetime:
    try:
        request_date = date.fromisoformat(google_date)
        request_time = time.fromisoformat(google_time)
        request_date_time = datetime.combine(request_date, request_time)
        return request_date_time
    except ValueError as e:
        raise AccountSheetException(AccountSheetExceptionMessage.RequestDateTimeNotISOFormat, e.args[0])
