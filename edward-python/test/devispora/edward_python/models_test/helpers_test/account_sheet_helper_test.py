import unittest


class AccountSheetHelperTest(unittest.TestCase):

    def test_things_suscces(self):
        sheet_values = [['test@gmail.com;hello@gmail.com'], ['2022-05-28'], ['00:00', '', 'Sheet gets released 4 hours in advance'], ['Press Delete on this cell to enable Auto-Share at above date'], ['Basic Jaeger Accounts']]
        print(sheet_values[0])

    def test_things_bad(self):
        sheet_values = [[], ['2022-01-01'], ['00:00', '', 'Sheet gets released 4 hours in advance'], ['Press Delete on this cell to enable Auto-Share at above date'], ['Basic Jaeger Accounts']]
        print(sheet_values[0][0])