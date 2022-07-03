from enum import Enum


class DriveException(Exception):
    def __init__(self, message, additional_message: str = None):
        self.message = message
        self.additional_message = additional_message

    def __str__(self):
        return self.message.value


class DriveExceptionMessage(str, Enum):
    NoFilesFound = 'Not a single file could be accessed at the assigned folder'
    HTTPError = 'Encountered an error trying to communicate with Google Drive, check the logs for more info'
