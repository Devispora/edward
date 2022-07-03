from enum import Enum

desired_account_sheet_range = ["B1:D5"]


class AccountSheetResult:

    def __init__(self, emails, request_datetime, shared_status, reservation_type):
        self.emails = emails
        self.request_datetime = request_datetime
        self.shared_status = shared_status
        self.reservation_type = reservation_type


class AccountSheetConstants(str, Enum):
    NotDeletedSharedMessage = 'Press Delete on this cell to enable Auto-Share at above date'
    SharedMessage = 'Shared'
    ObserverAccountsType = "Observer Accounts"
    NormalAccountsType = "Basic Jaeger Accounts"

