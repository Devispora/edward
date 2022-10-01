from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException
from devispora.edward_python.models.account_sheet import SheetResult


class ErredSheet(SheetResult):

    def __init__(self, sheet_id: str, sheet_name: str, warning: AccountSheetException):
        super().__init__(sheet_id, sheet_name)
        self.warning = warning
