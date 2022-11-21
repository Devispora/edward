from enum import Enum
from datetime import datetime

desired_account_sheet_range = "B1:D5"


class AccountSheetType(str, Enum):
    ObserverAccountsType = "Observer Accounts"
    NormalAccountsType = "Basic Jaeger Accounts"


class AccountSheetStatus(str, Enum):
    StatusCancelled = 'Cancelled'
    StatusNotReady = 'Not Ready'
    StatusReadyToShare = 'Ready to Share'
    StatusManuallyShared = 'Manually Shared'
    StatusShared = 'Shared'

    def __repr__(self):
        return self.value


class SheetResult:
    def __init__(self, sheet_id: str, sheet_name: str):
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name


class AccountSheetResult(SheetResult):

    def __init__(self, sheet_id: str, sheet_name: str, emails: [str], request_datetime: datetime,
                 shared_status: AccountSheetStatus, reservation_type: AccountSheetType):
        super().__init__(sheet_id, sheet_name)
        self.emails = emails
        self.request_datetime = request_datetime
        self.shared_status = shared_status
        self.reservation_type = reservation_type
