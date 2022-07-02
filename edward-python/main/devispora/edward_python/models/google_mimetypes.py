from enum import Enum


class GoogleMimeTypes(str, Enum):
    MimeType = 'mimeType'
    Folder = 'application/vnd.google-apps.folder'
    Sheet = 'application/vnd.google-apps.spreadsheet'
