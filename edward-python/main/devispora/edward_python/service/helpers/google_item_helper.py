from devispora.edward_python.models.google_mimetypes import GoogleMimeTypes


def filter_to_just_files(items: [dict]):
    filtered_items = []
    for item in items:
        if item[GoogleMimeTypes.MimeType] == GoogleMimeTypes.Sheet:
            filtered_items.append(item)
    return filtered_items
