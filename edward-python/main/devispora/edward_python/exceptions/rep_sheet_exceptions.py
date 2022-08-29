from enum import Enum


class RepSheetException(Exception):
    def __init__(self, message, additional_message: str = None):
        self.message = message
        self.additional_message = additional_message

    def __str__(self):
        return self.message.value


class RepSheetExceptionMessage(str, Enum):
    DiscordIdNotInt = 'Expected a number but received another value'
    RepTypeNotRecognised = 'The supplied rep type has not been recognised'
    RepTypeIssue = 'The rep type could not be retrieved'
    AccountLimitNotInt = 'Expected a number for account limit but encountered another value'
