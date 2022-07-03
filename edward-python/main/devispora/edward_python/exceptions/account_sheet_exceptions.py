from enum import Enum


class AccountSheetException(Exception):
    def __init__(self, message, additional_message: str = None):
        self.message = message
        self.additional_message = additional_message

    def __str__(self):
        return self.message.value


class AccountSheetExceptionMessage(str, Enum):
    EmailNotFound = 'No email has been supplied'
    EmailCouldNotBeParsed = 'Encountered an issue trying to parse the email section'
    RequestDateNotFound = 'No date could be found where it was expected'
    RequestDateCouldNotBeParsed = 'Encountered an issue trying to parse the String at request date into a date object'
    RequestDateTimeNotISOFormat = 'The requested datetime was not in the ISO format of YYYY-MM-DD and 00:00'
    SharedStatusIssue = 'Encountered an issue trying to retrieve the shared status'
    ReservationTypeIssue = 'The reservation type could not be retrieved'
    ReservationTypeNotRecognised = 'The reservation type did not match the expected obs/account variants'
