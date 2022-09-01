from devispora.edward_python.models.account_sheet import AccountSheetResult, AccountSheetType

google_sheets_url = 'https://docs.google.com/spreadsheets/d'


def webhook_content(sheet: AccountSheetResult, user_ids: [int]):
    return {
        'content': f'Hi {mention_users(user_ids)}. {determine_message(sheet)} {create_doc_link(sheet)}.',
        'allowed_mentions': {
            'users': user_ids
        }
    }


def create_doc_link(sheet: AccountSheetResult):
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
