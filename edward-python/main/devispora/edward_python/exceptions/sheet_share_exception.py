from enum import Enum


class SheetShareException(Exception):
    def __init__(self, message, additional_message: str = None):
        self.message = message
        self.additional_message = additional_message

    def __str__(self):
        return self.message.value


class SheetShareExceptionMessage(str, Enum):
    ShareIssue = 'Encountered an issue trying to tell google to share the file'
