from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from devispora.edward_python.google.credentials import get_credentials

credentials = get_credentials()
drive_service = build('drive', 'v3', credentials=credentials)


def retrieve_items_from_folder(folder_id: str):
    file_operation = drive_service.files()
    items = []
    request = file_operation.list(
        q=f'"{folder_id}" in parents',
        pageSize=10,
        fields="nextPageToken, files(id, name, mimeType)")
    try:
        while request is not None:
            results = request.execute()
            drive_files = results.get('files', [])
            request = file_operation.list_next(request, results)
            items.extend(drive_files)
        if not items:
            # todo throw error that edward can't find anything in the current folder.
            #  This should never happen right now as there's always at least the template
            print('No files found.')
            return
        return items
    except HttpError as error:
        print(f'An error occurred: {error}')
