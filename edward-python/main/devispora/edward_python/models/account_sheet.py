from typing import List

desired_account_sheet_range = ["B1:D5"]


class AccountSheetResult:

    def __init__(self, emails, request_date, requested_time, shared_status, reservation_type):
        self.emails = emails
        self.request_date = request_date
        self.requested_time = requested_time
        self.shared_status = shared_status
        self.reservation_type = reservation_type
