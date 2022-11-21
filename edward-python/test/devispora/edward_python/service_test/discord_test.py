import datetime
import unittest

from devispora.edward_python.models.account_sheet import AccountSheetResult, AccountSheetType, AccountSheetStatus
from devispora.edward_python.service.discord_interaction_service import share_sheet_to_discord


class DiscordInteractionServiceTest(unittest.TestCase):

    def test_things(self):

        acc_result = AccountSheetResult(
            sheet_id='1wEijBc3lQHo6r4E12Vj9xocf5EZ12O-uUx5gSwmXBKc',
            sheet_name='test',
            reservation_type=AccountSheetType.NormalAccountsType,
            emails='',
            request_datetime=datetime.datetime.now(),
            shared_status=AccountSheetStatus.StatusReadyToShare
        )

        share_sheet_to_discord(acc_result, [97325654688681984])


if __name__ == '__main__':
    unittest.main()
