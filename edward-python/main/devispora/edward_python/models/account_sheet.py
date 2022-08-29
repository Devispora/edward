from enum import Enum
from datetime import datetime

desired_account_sheet_range = ["B1:D5"]


class AccountSheetType(str, Enum):
    ObserverAccountsType = "Observer Accounts"
    NormalAccountsType = "Basic Jaeger Accounts"


class AccountSheetStatus(str, Enum):
    StatusCancelled = 'Cancelled'
    StatusNotReady = 'Not Ready'
    StatusReadyToShare = 'Ready to Share'
    StatusShared = 'Shared'


class AccountSheetResult:

    def __init__(self, sheet_id: str, emails: [str], request_datetime: datetime,
                 shared_status: AccountSheetStatus, reservation_type: AccountSheetType):
        self.sheet_id = sheet_id
        self.emails = [emails]
        self.request_datetime = request_datetime
        self.shared_status = shared_status
        self.reservation_type = reservation_type
