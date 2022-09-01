
from requests import post

from devispora.edward_python.constants.constants import Constants
from devispora.edward_python.models.account_sheet import AccountSheetResult
from devispora.edward_python.service.helpers.discord_message_helper import webhook_content

discord_webhook = f'https://discord.com/api/webhooks/{Constants.discord_webhook_id}'


def share_to_discord(sheet: AccountSheetResult, user_ids: [int]):
    post(
        url=discord_webhook,
        json=webhook_content(sheet, user_ids)
    )
