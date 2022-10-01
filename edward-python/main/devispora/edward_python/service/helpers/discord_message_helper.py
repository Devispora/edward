from devispora.edward_python.constants.constants import Constants
from devispora.edward_python.models.account_sheet import AccountSheetResult, AccountSheetType, SheetResult
from devispora.edward_python.models.erred_sheet import ErredSheet

google_sheets_url = 'https://docs.google.com/spreadsheets/d'
staff_role = Constants.discord_staff_id
discord_avatar = Constants.discord_avatar


def shared_sheet_content(sheet: AccountSheetResult, user_ids: [int]):
    return {
        'content': f'Hi {mention_users(user_ids)}. {determine_message(sheet)} {create_doc_link(sheet)}.',
        'allowed_mentions': {
            'users': user_ids
        },
        'username': 'Edward 2',
        'avatar_url': discord_avatar
    }


def share_erred_content(sheet: ErredSheet):
    return {
        'content': f'Hi <@&{staff_role}>. {reveal_error_message(sheet)} {create_doc_link(sheet)}.',
        'allowed_mentions': {
            'roles': [staff_role]
        },
        'username': 'Edward is Worried',
        'avatar_url': discord_avatar
    }


def create_doc_link(sheet: SheetResult):
    return f'[{sheet.sheet_name}]({google_sheets_url}/{sheet.sheet_id})'


def mention_users(user_ids: [int]):
    message = ''
    for user_id in user_ids:
        message += f'<@{user_id}>'
    return message


def determine_message(sheet: AccountSheetResult):
    if sheet.reservation_type == AccountSheetType.NormalAccountsType:
        return 'Account Sheet ready: '
    elif sheet.reservation_type == AccountSheetType.ObserverAccountsType:
        return 'Observer Account Sheet ready: '


def reveal_error_message(sheet: ErredSheet):
    if sheet.warning.additional_message:
        return f'{sheet.warning.message}: {sheet.warning.additional_message}'
    else:
        return sheet.warning.message
