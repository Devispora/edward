import unittest

from devispora.edward_python.models.google_mimetypes import GoogleMimeTypes
from devispora.edward_python.service.helpers.google_item_helper import filter_to_just_files


class GoogleItemHelperTest(unittest.TestCase):

    def test_filter_to_just_files(self):
        things = [{'id': 'folderId', 'name': 'testFolder', 'mimeType': 'application/vnd.google-apps.folder'},
                  {'id': 'secondID', 'name': 'firstSheet', 'mimeType': 'application/vnd.google-apps.spreadsheet'},
                  {'id': 'thirdId', 'name': 'secondSheet', 'mimeType': 'application/vnd.google-apps.spreadsheet'}
                  ]
        result = filter_to_just_files(things)
        self.assertEqual(2, len(result))
        self.assertEqual(result[0][GoogleMimeTypes.MimeType], GoogleMimeTypes.Sheet)
        self.assertEqual(result[1][GoogleMimeTypes.MimeType], GoogleMimeTypes.Sheet)


if __name__ == '__main__':
    unittest.main()
