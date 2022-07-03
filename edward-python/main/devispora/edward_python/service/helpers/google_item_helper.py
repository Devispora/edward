from devispora.edward_python.models.google_mimetypes import GoogleMimeTypes
from devispora.edward_python.models.helpers.date_helper import sheet_is_from_this_year


def filter_to_just_files(items: [dict]):
    filtered_items = []
    for item in items:
        if item[GoogleMimeTypes.MimeType] == GoogleMimeTypes.Sheet:
            filtered_items.append(item)
    return filtered_items


def filter_sheets_by_name_being_ready(items: [dict]):
    filtered_items = []
    for item in items:
        if sheet_is_from_this_year(item['name']):
            filtered_items.append(item)
    return filtered_items
