import datetime
import unittest

from devispora.edward_python.exceptions.account_sheet_exceptions import AccountSheetException, \
    AccountSheetExceptionMessage
from devispora.edward_python.models.helpers.date_helper import parse_google_string_to_date, sheet_is_from_this_year, \
    five_minute_creation_cooldown


class DateHelperTest(unittest.TestCase):

    def test_parse_google_string_to_date(self):
        input_date = '2022-05-28'
        input_time = '00:00'
        result = parse_google_string_to_date(input_date, input_time)
        self.assertEqual(result.hour, 0)
        self.assertEqual(result.minute, 0)
        self.assertEqual(result.day, 28)
        self.assertEqual(result.month, 5)
        self.assertEqual(result.year, 2022)

    def test_parse_google_string_to_date_non_iso(self):
        non_iso_input_date = '28-05-2022'
        input_time = '00:00'
        self.assertRaisesRegex(AccountSheetException, AccountSheetExceptionMessage.RequestDateTimeNotISOFormat,
                               parse_google_string_to_date, non_iso_input_date, input_time)

    def test_sheet_is_from_this_year_true(self):
        sheet_name = '2022-05-28 [Name]'
        result = sheet_is_from_this_year(sheet_name)
        self.assertTrue(result)

    def test_sheet_is_from_this_year_false(self):
        sheet_name = '!2022-05-28 [Name]'
        result = sheet_is_from_this_year(sheet_name)
        self.assertFalse(result)

    def test_five_minute_creation_cooldown(self):
        sheet_creation_time = '2022-07-09T00:07:18.953Z'
        result = five_minute_creation_cooldown(sheet_creation_time)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
