from devispora.edward_python.models.account_sheet import AccountSheetResult, AccountSheetStatus
from devispora.edward_python.models.google_mimetypes import GoogleMimeTypes
from devispora.edward_python.models.helpers.date_helper import sheet_is_from_this_year, five_minute_creation_cooldown, \
    has_been_two_days, is_due_to_release


def filter_to_just_files(items: [dict]):
    filtered_items = []
    for item in items:
        if item[GoogleMimeTypes.MimeType] == GoogleMimeTypes.Sheet:
            filtered_items.append(item)
    return filtered_items


def filter_by_name_and_cooldown(items: [dict]):
    filtered_items = []
    for item in items:
        if sheet_is_from_this_year(item['name']):
            if five_minute_creation_cooldown(item['createdTime']):
                filtered_items.append(item)
    return filtered_items


def filter_by_share_and_cleaning(sheets: [AccountSheetResult]):
    sheets_to_clean = []
    sheets_to_share = []
    for sheet in sheets:
        if has_been_two_days(sheet.request_datetime):
            sheets_to_clean.append(sheet)
        elif is_due_to_release(sheet.request_datetime) and shared_status_valid(sheet.shared_status):
            sheets_to_share.append(sheet)
    return sheets_to_share, sheets_to_clean


def shared_status_valid(status: AccountSheetStatus):
    return status == AccountSheetStatus.StatusReadyToShare
