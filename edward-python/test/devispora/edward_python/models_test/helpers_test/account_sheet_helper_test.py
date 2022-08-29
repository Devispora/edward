import unittest

from devispora.edward_python.models.helpers.account_sheet_helper import retrieve_emails


class AccountSheetHelperTest(unittest.TestCase):

    def test_things_suscces(self):
        sheet_values = [['test@gmail.com;hello@gmail.com'], ['2022-05-28'], ['00:00', '', 'Sheet gets released 4 hours in advance'], ['Press Delete on this cell to enable Auto-Share at above date'], ['Basic Jaeger Accounts']]
        print(sheet_values[0])

    def test_things_bad(self):
        sheet_values = [[], ['2022-01-01'], ['00:00', '', 'Sheet gets released 4 hours in advance'], ['Press Delete on this cell to enable Auto-Share at above date'], ['Basic Jaeger Accounts']]
        print(sheet_values[0][0])

    def test_retrieve_emails_multi(self):
        emails = [['test@gmail.com;test2@gmail.com,test3@gmail.com:test4@gmail.com test5@gmail.com']]
        result = retrieve_emails(emails)
        self.assertEqual(5, len(result))


if __name__ == '__main__':
    unittest.main()
